const express = require('express');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const app = express();
const port = 3000;
const OLLAMA_URL = process.env.OLLAMA_URL || 'http://localhost:11434';

// Middleware to parse JSON and serve static files
app.use(express.json());
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
    
    if (!code) {
        console.error('No code provided in request');
        return res.status(400).json({ error: 'No code provided.' });
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

        // Step 1: Compile the Java code
        const compile = spawn('javac', [filePath]);
        let compileError = '';

        compile.stderr.on('data', (data) => {
            const error = data.toString();
            console.error('Compilation error:', error);
            compileError += error;
        });

        compile.on('close', (code) => {
            if (code !== 0) {
                console.error(`Compilation failed with code ${code}`);
                cleanup();
                return res.json({ output: compileError, error: true, type: 'compilation' });
            }
            console.log('Compilation successful, running code...');

            // Step 2: Run the compiled Java code
            const run = spawn('java', ['-cp', tempDir, 'Main']);
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
                run.kill();
                cleanup();
                return res.json({ output: 'Execution timed out after 10 seconds', error: true, type: 'timeout' });
            }, 10000);

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
                if (runError) {
                    console.error('Runtime error occurred:', runError);
                    return res.json({ output: runError, error: true, type: 'runtime' });
                }
                console.log('Execution successful, output length:', output.length);
                res.json({ output: output, error: false });
            });

            run.on('error', (err) => {
                console.error('Failed to start Java process:', err);
                clearTimeout(timeout);
                cleanup();
                res.status(500).json({ output: `Failed to start Java process: ${err.message}`, error: true, type: 'startup' });
            });
        });

        function cleanup() {
            console.log('Cleaning up temporary files...');
            try {
                if (fs.existsSync(filePath)) {
                    fs.unlinkSync(filePath);
                }
                const classFile = filePath.replace('.java', '.class');
                if (fs.existsSync(classFile)) {
                    fs.unlinkSync(classFile);
                }
                if (fs.existsSync(tempDir)) {
                    fs.rmdirSync(tempDir);
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
    if (!code) {
        return res.status(400).json({ error: 'No code provided.' });
    }

    const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'python-run-'));
    const filePath = path.join(tempDir, 'script.py');

    fs.writeFile(filePath, code, (err) => {
        if (err) {
            return res.status(500).json({ error: 'Failed to write code to file.' });
        }

        const run = spawn('python', [filePath]);
        let output = '';
        let runError = '';

        run.stdout.on('data', (data) => {
            output += data.toString();
        });

        run.stderr.on('data', (data) => {
            runError += data.toString();
        });

        run.on('close', (code) => {
            fs.unlink(filePath, () => {});
            fs.rmdir(tempDir, () => {});
            if (runError) {
                return res.json({ output: runError, error: true, type: 'runtime' });
            }
            res.json({ output: output, error: false });
        });
    });
});


app.listen(port, () => {
    console.log(`devbootLLM server listening at http://localhost:${port}`);
});
