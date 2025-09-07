const express = require('express');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const app = express();
const port = Number(process.env.PORT || 3000);
const OLLAMA_URL = process.env.OLLAMA_URL || 'http://localhost:11434';
const LMSTUDIO_URL = process.env.LMSTUDIO_URL || 'http://127.0.0.1:1234';
const LMSTUDIO_API_KEY = process.env.LMSTUDIO_API_KEY || '';

// Utility: best-effort Python executable resolution across OSes
function resolvePythonCmd() {
    // Allow override
    if (process.env.PYTHON_BIN) {
        const bin = process.env.PYTHON_BIN.trim();
        if (bin.length > 0) return { cmd: bin, args: [] };
    }
    if (process.platform === 'win32') {
        // Prefer Python launcher for Windows
        return { cmd: 'py', args: ['-3'] };
    }
    // Linux/macOS commonly have python3; fallback to python
    return { cmd: 'python3', args: [] };
}

// Safety limits
const MAX_CODE_SIZE_BYTES = 100 * 1024; // 100KB per request body
const MAX_EXECUTION_MS = 10_000; // 10 seconds per run

// Middleware to parse JSON and serve static files
// Limit request body to reduce risk of memory abuse
app.use(express.json({ limit: '100kb' }));
app.use(express.static('public'));

// ----------------------
// Ollama integration
// ----------------------
// List available local Ollama models
app.get('/ollama/models', async (req, res) => {
    try {
        const resp = await fetch(`${OLLAMA_URL}/api/tags`);
        if (!resp.ok) {
            return res.status(resp.status).json({ error: `Ollama responded with ${resp.status}` });
        }
        const data = await resp.json();
        const models = (data.models || []).map(m => ({
            name: m.name,
            modified_at: m.modified_at,
            size: m.size,
            digest: m.digest,
            details: m.details || {}
        }));
        res.json({ models });
    } catch (err) {
        res.status(500).json({ error: 'Failed to contact Ollama', details: err.message });
    }
});

// ----------------------
// LM Studio integration (OpenAI-compatible)
// ----------------------
// List available LM Studio models (maps to OpenAI /v1/models)
app.get('/lmstudio/models', async (req, res) => {
    try {
        const resp = await fetch(`${LMSTUDIO_URL}/v1/models`, {
            headers: LMSTUDIO_API_KEY ? { Authorization: `Bearer ${LMSTUDIO_API_KEY}` } : undefined,
        });
        if (!resp.ok) {
            return res.status(resp.status).json({ error: `LM Studio responded with ${resp.status}` });
        }
        const data = await resp.json();
        const models = (data.data || []).map(m => ({ name: m.id }));
        res.json({ models });
    } catch (err) {
        res.status(500).json({ error: 'Failed to contact LM Studio', details: err.message });
    }
});

// Chat with a selected LM Studio model (OpenAI chat.completions)
app.post('/lmstudio/chat', async (req, res) => {
    const { model, history } = req.body || {};
    if (!model) return res.status(400).json({ error: 'Missing model' });

    const toText = (parts) => Array.isArray(parts) ? parts.map(p => p.text || '').join('\n') : '';
    const messages = (history || []).map(m => ({
        role: m.role === 'model' ? 'assistant' : (m.role || 'user'),
        content: toText(m.parts)
    })).filter(m => m.content && m.content.trim().length > 0);

    try {
        const headers = { 'Content-Type': 'application/json' };
        if (LMSTUDIO_API_KEY) headers['Authorization'] = `Bearer ${LMSTUDIO_API_KEY}`;
        const resp = await fetch(`${LMSTUDIO_URL}/v1/chat/completions`, {
            method: 'POST',
            headers,
            body: JSON.stringify({
                model,
                messages,
                stream: false
            })
        });
        if (!resp.ok) {
            const text = await resp.text().catch(() => '');
            return res.status(resp.status).json({ error: `LM Studio chat error ${resp.status}`, details: text });
        }
        const data = await resp.json();
        const choice = data && data.choices && data.choices[0];
        const text = (choice && choice.message && choice.message.content) || '';
        res.json({ text });
    } catch (err) {
        res.status(500).json({ error: 'Failed to reach LM Studio chat', details: err.message });
    }
});

// Streaming chat proxy for LM Studio (sends raw text chunks)
app.post('/lmstudio/chat/stream', async (req, res) => {
    const { model, history } = req.body || {};
    if (!model) return res.status(400).json({ error: 'Missing model' });

    const toText = (parts) => Array.isArray(parts) ? parts.map(p => p.text || '').join('\n') : '';
    const messages = (history || []).map(m => ({
        role: m.role === 'model' ? 'assistant' : (m.role || 'user'),
        content: toText(m.parts)
    })).filter(m => m.content && m.content.trim().length > 0);

    const headers = { 'Content-Type': 'application/json' };
    if (LMSTUDIO_API_KEY) headers['Authorization'] = `Bearer ${LMSTUDIO_API_KEY}`;

    let controller;
    try {
        controller = new AbortController();
        const upstream = await fetch(`${LMSTUDIO_URL}/v1/chat/completions`, {
            method: 'POST',
            headers,
            body: JSON.stringify({ model, messages, stream: true }),
            signal: controller.signal,
        });
        if (!upstream.ok || !upstream.body) {
            const text = await upstream.text().catch(() => '');
            return res.status(upstream.status || 500).json({ error: `LM Studio chat error ${upstream.status}`, details: text });
        }

        res.setHeader('Content-Type', 'text/plain; charset=utf-8');
        res.setHeader('Cache-Control', 'no-cache');
        res.setHeader('Connection', 'keep-alive');

        const decoder = new TextDecoder();
        let buffer = '';
        let clientAborted = false;

        req.on('close', () => {
            clientAborted = true;
            try { controller.abort(); } catch (_) {}
        });

        const reader = upstream.body.getReader();
        while (true) {
            const { value, done } = await reader.read();
            if (done) break;
            if (clientAborted) break;
            buffer += decoder.decode(value, { stream: true });
            // Parse SSE lines like: "data: {json}\n\n" or partial lines
            let idx;
            while ((idx = buffer.indexOf('\n')) !== -1) {
                const lineRaw = buffer.slice(0, idx);
                buffer = buffer.slice(idx + 1);
                const line = lineRaw.trimEnd();
                if (!line) continue;
                if (line.startsWith('data: ')) {
                    const dataStr = line.slice(6).trim();
                    if (dataStr === '[DONE]') {
                        res.end();
                        return;
                    }
                    try {
                        const obj = JSON.parse(dataStr);
                        const choice = obj && obj.choices && obj.choices[0];
                        const delta = choice && choice.delta && choice.delta.content;
                        const text = delta || (choice && choice.text) || '';
                        if (text) {
                            res.write(text);
                        }
                    } catch (_) {
                        // ignore JSON parse errors on partial lines
                    }
                }
            }
        }
        // Flush any remaining content if present
        if (buffer.trim().length > 0) {
            // Try to parse last line
            const line = buffer.trim();
            if (line.startsWith('data: ')) {
                const dataStr = line.slice(6).trim();
                if (dataStr !== '[DONE]') {
                    try {
                        const obj = JSON.parse(dataStr);
                        const choice = obj && obj.choices && obj.choices[0];
                        const delta = choice && choice.delta && choice.delta.content;
                        const text = delta || (choice && choice.text) || '';
                        if (text) res.write(text);
                    } catch (_) { /* ignore */ }
                }
            }
        }
        res.end();
    } catch (err) {
        if (!res.headersSent) {
            res.status(500).json({ error: 'Failed to stream from LM Studio', details: err.message });
        } else {
            try { res.end(); } catch (_) {}
        }
    }
});

// Streaming chat proxy for Ollama (NDJSON lines)
app.post('/ollama/chat/stream', async (req, res) => {
    const { model, history } = req.body || {};
    if (!model) return res.status(400).json({ error: 'Missing model' });

    const toText = (parts) => Array.isArray(parts) ? parts.map(p => p.text || '').join('\n') : '';
    const messages = (history || []).map(m => ({
        role: m.role === 'model' ? 'assistant' : (m.role || 'user'),
        content: toText(m.parts)
    })).filter(m => m.content && m.content.trim().length > 0);

    let controller;
    try {
        controller = new AbortController();
        const upstream = await fetch(`${OLLAMA_URL}/api/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ model, messages, stream: true }),
            signal: controller.signal,
        });
        if (!upstream.ok || !upstream.body) {
            const text = await upstream.text().catch(() => '');
            return res.status(upstream.status || 500).json({ error: `Ollama chat error ${upstream.status}`, details: text });
        }

        res.setHeader('Content-Type', 'text/plain; charset=utf-8');
        res.setHeader('Cache-Control', 'no-cache');
        res.setHeader('Connection', 'keep-alive');

        const decoder = new TextDecoder();
        let buffer = '';
        let clientAborted = false;
        req.on('close', () => {
            clientAborted = true;
            try { controller.abort(); } catch (_) {}
        });

        const reader = upstream.body.getReader();
        while (true) {
            const { value, done } = await reader.read();
            if (done) break;
            if (clientAborted) break;
            buffer += decoder.decode(value, { stream: true });
            let idx;
            while ((idx = buffer.indexOf('\n')) !== -1) {
                const line = buffer.slice(0, idx).trim();
                buffer = buffer.slice(idx + 1);
                if (!line) continue;
                try {
                    const obj = JSON.parse(line);
                    if (obj && obj.done) {
                        res.end();
                        return;
                    }
                    const text = (obj && obj.message && obj.message.content) || obj.response || '';
                    if (text) {
                        res.write(text);
                    }
                } catch (_) {
                    // ignore partial JSON
                }
            }
        }
        // Try to parse any leftover content
        const rem = buffer.trim();
        if (rem) {
            try {
                const obj = JSON.parse(rem);
                const text = (obj && obj.message && obj.message.content) || obj.response || '';
                if (text) res.write(text);
            } catch (_) { /* ignore */ }
        }
        res.end();
    } catch (err) {
        if (!res.headersSent) {
            res.status(500).json({ error: 'Failed to stream from Ollama', details: err.message });
        } else {
            try { res.end(); } catch (_) {}
        }
    }
});

// Simple health endpoint to check runtime availability
app.get('/health', async (req, res) => {
    const checks = {
        node: process.version,
        platform: process.platform,
        ollama_url: OLLAMA_URL,
        lmstudio_url: LMSTUDIO_URL,
    };
    const runVersion = (cmd, args) => new Promise((resolve) => {
        try {
            const p = spawn(cmd, args, { stdio: ['ignore', 'pipe', 'pipe'] });
            let out = '';
            p.stdout.on('data', d => out += d.toString());
            p.on('close', (code) => resolve(code === 0 ? out.trim() : null));
            p.on('error', () => resolve(null));
        } catch {
            resolve(null);
        }
    });
    const py = resolvePythonCmd();
    const [javacV, javaV, pythonV] = await Promise.all([
        runVersion('javac', ['-version']).then(v => v || null),
        runVersion('java', ['-version']).then(v => v || null),
        runVersion(py.cmd, [...py.args, '--version']).then(v => v || null),
    ]);
    checks.javac = javacV;
    checks.java = javaV;
    checks.python = pythonV;

    // Try contacting Ollama and LM Studio quickly (ignore failures)
    try {
        const controller = new AbortController();
        const t = setTimeout(() => controller.abort(), 1000);
        const r = await fetch(`${OLLAMA_URL}/api/tags`, { signal: controller.signal });
        clearTimeout(t);
        checks.ollamaReachable = r.ok;
    } catch {
        checks.ollamaReachable = false;
    }
    try {
        const controller2 = new AbortController();
        const t2 = setTimeout(() => controller2.abort(), 1000);
        const r2 = await fetch(`${LMSTUDIO_URL}/v1/models`, { signal: controller2.signal });
        clearTimeout(t2);
        checks.lmstudioReachable = r2.ok;
    } catch {
        checks.lmstudioReachable = false;
    }
    res.json(checks);
});

// Chat with a selected Ollama model
app.post('/ollama/chat', async (req, res) => {
    const { model, history } = req.body || {};
    if (!model) return res.status(400).json({ error: 'Missing model' });

    // Convert existing chatHistory format to Ollama messages
    const toText = (parts) => Array.isArray(parts) ? parts.map(p => p.text || '').join('\n') : '';
    const messages = (history || []).map(m => ({
        role: m.role === 'model' ? 'assistant' : (m.role || 'user'),
        content: toText(m.parts)
    })).filter(m => m.content && m.content.trim().length > 0);

    try {
        const resp = await fetch(`${OLLAMA_URL}/api/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ model, stream: false, messages })
        });
        if (!resp.ok) {
            const text = await resp.text().catch(() => '');
            return res.status(resp.status).json({ error: `Ollama chat error ${resp.status}`, details: text });
        }
        const data = await resp.json();
        const text = (data && data.message && data.message.content) || data.response || '';
        res.json({ text });
    } catch (err) {
        res.status(500).json({ error: 'Failed to reach Ollama chat', details: err.message });
    }
});

// Endpoint to execute Java code
app.post('/run/java', (req, res) => {
    console.log('Received Java execution request');
    const { code, input } = req.body;
    
    if (typeof code !== 'string' || code.length === 0) {
        console.error('No code provided in request');
        return res.status(400).json({ error: 'No code provided.' });
    }
    if (Buffer.byteLength(code, 'utf8') > MAX_CODE_SIZE_BYTES) {
        console.error('Code size exceeds limit');
        return res.status(413).json({ error: 'Code too large (max 100KB).' });
    }

    console.log('Creating temporary directory...');
    const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'java-run-'));
    const filePath = path.join(tempDir, 'Main.java');
    console.log(`Temporary directory created at: ${tempDir}`);

    // Save the user's code to a .java file
    fs.writeFile(filePath, code, (err) => {
        if (err) {
            console.error('File write error:', err);
            return res.status(500).json({ error: 'Failed to write code to file.' });
        }
        console.log('Code written to file, compiling...');

        // Response guard to prevent double-send (timeouts vs close event)
        let responded = false;
        const safeRespond = (statusCode, payload) => {
            if (responded) return;
            responded = true;
            try {
                if (statusCode) {
                    res.status(statusCode).json(payload);
                } else {
                    res.json(payload);
                }
            } catch (_) { /* ignore */ }
        };

        // Step 1: Compile the Java code
        const compile = spawn('javac', [filePath]);
        let compileError = '';

        compile.stderr.on('data', (data) => {
            const error = data.toString();
            console.error('Compilation error:', error);
            compileError += error;
        });

        compile.on('error', (err) => {
            console.error('Failed to start javac:', err);
            cleanup();
            return safeRespond(500, { output: `Failed to start javac: ${err.message}` , error: true, type: 'startup' });
        });

        compile.on('close', (code) => {
            if (code !== 0) {
                console.error(`Compilation failed with code ${code}`);
                cleanup();
                return safeRespond(200, { output: compileError, error: true, type: 'compilation' });
            }
            console.log('Compilation successful, running code...');

            // Step 2: Run the compiled Java code with a small heap to limit memory
            const run = spawn('java', ['-Xmx64m', '-cp', tempDir, 'Main']);
            let output = '';
            let runError = '';
            
            // Handle input if provided
            if (input) {
                console.log('Providing input to Java process:', JSON.stringify(input));
                run.stdin.write(input);
                run.stdin.end();
            } else {
                console.log('No input provided for this execution');
            }

            // Set a timeout to prevent hanging
            const timeout = setTimeout(() => {
                console.error('Execution timed out');
                try { run.kill(); } catch (_) {}
                cleanup();
                safeRespond(200, { output: 'Execution timed out after 10 seconds', error: true, type: 'timeout' });
            }, MAX_EXECUTION_MS);

            run.stdout.on('data', (data) => {
                const dataStr = data.toString();
                console.log('Java stdout:', dataStr);
                output += dataStr;
            });

            run.stderr.on('data', (data) => {
                const error = data.toString();
                console.error('Java stderr:', error);
                runError += error;
            });

            run.on('close', (code) => {
                clearTimeout(timeout);
                console.log(`Java process exited with code ${code}`);
                cleanup();
                if (responded) return;
                if (runError) {
                    console.error('Runtime error occurred:', runError);
                    return safeRespond(200, { output: runError, error: true, type: 'runtime' });
                }
                console.log('Execution successful, output length:', output.length);
                safeRespond(200, { output: output, error: false });
            });

            run.on('error', (err) => {
                console.error('Failed to start Java process:', err);
                clearTimeout(timeout);
                cleanup();
                safeRespond(500, { output: `Failed to start Java process: ${err.message}`, error: true, type: 'startup' });
            });
        });

        function cleanup() {
            console.log('Cleaning up temporary files...');
            try {
                // Remove temp dir recursively; ignore errors
                if (fs.existsSync(tempDir)) {
                    fs.rmSync(tempDir, { recursive: true, force: true });
                }
                console.log('Cleanup complete');
            } catch (cleanupErr) {
                console.error('Error during cleanup:', cleanupErr);
            }
        }
    });
});


// Endpoint to execute Python code
app.post('/run/python', (req, res) => {
    const { code } = req.body;
    if (typeof code !== 'string' || code.length === 0) {
        return res.status(400).json({ error: 'No code provided.' });
    }
    if (Buffer.byteLength(code, 'utf8') > MAX_CODE_SIZE_BYTES) {
        return res.status(413).json({ error: 'Code too large (max 100KB).' });
    }

    const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'python-run-'));
    const filePath = path.join(tempDir, 'script.py');

    fs.writeFile(filePath, code, (err) => {
        if (err) {
            return res.status(500).json({ error: 'Failed to write code to file.' });
        }

        // Response guard
        let responded = false;
        const safeRespond = (statusCode, payload) => {
            if (responded) return;
            responded = true;
            try {
                if (statusCode) {
                    res.status(statusCode).json(payload);
                } else {
                    res.json(payload);
                }
            } catch (_) { /* ignore */ }
        };

        // Use resolved python executable
        const py = resolvePythonCmd();
        const run = spawn(py.cmd, [...py.args, filePath]);
        let output = '';
        let runError = '';
        let timedOut = false;

        // Timeout to prevent hanging processes
        const timeout = setTimeout(() => {
            timedOut = true;
            try { run.kill(); } catch (_) {}
        }, MAX_EXECUTION_MS);

        run.stdout.on('data', (data) => {
            output += data.toString();
        });

        run.stderr.on('data', (data) => {
            runError += data.toString();
        });

        run.on('close', (code) => {
            clearTimeout(timeout);
            try { fs.rmSync(filePath, { force: true }); } catch (_) {}
            try { fs.rmSync(tempDir, { recursive: true, force: true }); } catch (_) {}
            if (responded) return;
            if (timedOut) {
                return safeRespond(200, { output: 'Execution timed out after 10 seconds', error: true, type: 'timeout' });
            }
            if (runError) {
                return safeRespond(200, { output: runError, error: true, type: 'runtime' });
            }
            safeRespond(200, { output: output, error: false });
        });
    });
});


app.listen(port, () => {
    console.log(`devbootLLM server listening at http://localhost:${port}`);
});
