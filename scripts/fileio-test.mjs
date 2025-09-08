#!/usr/bin/env node
import { spawn } from 'node:child_process';
import { setTimeout as delay } from 'node:timers/promises';

const PORT = process.env.PORT || '3100';
const SERVER_URL = `http://localhost:${PORT}`;

function startServer() {
  return new Promise((resolve, reject) => {
    const child = spawn('node', ['server.js'], { env: { ...process.env, PORT }, stdio: ['ignore', 'pipe', 'pipe'] });
    let ready = false;
    const onData = (buf) => {
      const line = buf.toString();
      process.stdout.write(line);
      if (!ready && line.includes('devbootLLM server listening')) {
        ready = true;
        resolve(child);
      }
    };
    child.stdout.on('data', onData);
    child.stderr.on('data', (b) => process.stderr.write(b));
    child.on('error', reject);
    setTimeout(() => { if (!ready) reject(new Error('Server did not start within timeout')); }, 8000);
  });
}

async function postJson(path, payload) {
  const r = await fetch(`${SERVER_URL}${path}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
  const text = await r.text();
  try { return { status: r.status, json: JSON.parse(text) }; } catch { return { status: r.status, json: null, text }; }
}

function ensure(cond, message) { if (!cond) throw new Error(message); }

async function main() {
  console.log('Starting server...');
  const child = await startServer();
  try {
    const code = "with open('notes.txt','w') as f:\n    f.write('A\\nB')\nwith open('notes.txt') as f:\n    print(f.read())\n";
    const resp = await postJson('/run/python', { code });
    console.log('Response:', resp);
    const out = (resp.json && resp.json.output) ? String(resp.json.output).replaceAll('\r\n', '\n') : '';
    ensure(resp.status === 200 && resp.json && !resp.json.error && out.includes('A\nB'), 'Python file I/O test failed');
    console.log('Python file I/O test OK');
  } finally {
    try { process.kill(child.pid); } catch {}
  }
}

main().catch((err) => { console.error('\nFile I/O test failed:', err.message); process.exit(1); });
