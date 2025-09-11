#!/usr/bin/env node
import { spawn } from 'node:child_process';
import { setTimeout as delay } from 'node:timers/promises';

const PORT = process.env.PORT || '3200';
const SERVER_URL = `http://localhost:${PORT}`;

function startServer() {
  return new Promise((resolve, reject) => {
    const child = spawn('node', ['server.js'], {
      env: { ...process.env, PORT },
      stdio: ['ignore', 'pipe', 'pipe'],
    });
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
    setTimeout(() => {
      if (!ready) reject(new Error('Server did not start within timeout'));
    }, 8000);
  });
}

async function postJson(path, payload) {
  const r = await fetch(`${SERVER_URL}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const text = await r.text();
  try {
    return { status: r.status, json: JSON.parse(text) };
  } catch {
    return { status: r.status, json: null, text };
  }
}

function ensure(cond, msg) { if (!cond) throw new Error(msg); }

async function main() {
  console.log('Starting server...');
  const child = await startServer();
  try {
    // New Python lessons full solutions
    const tests = [
      { lang: 'python', code: "from itertools import product\nprint(len(list(product([1,2], [3,4]))))\n", expect: '4' },
      { lang: 'python', code: "from collections import Counter\nprint(Counter('aab')['a'])\n", expect: '2' },
      { lang: 'python', code: "print(f\"{3.14159:.2f}\")\n", expect: '3.14' },
    ];
    for (const t of tests) {
      const ep = t.lang === 'python' ? '/run/python' : '/run/java';
      const r = await postJson(ep, { code: t.code });
      ensure(r.status === 200 && r.json, `Bad status for ${t.lang}`);
      ensure(!r.json.error, `${t.lang} run error: ${r.json.output}`);
      const out = String(r.json.output).trim();
      ensure(out === t.expect, `${t.lang} mismatch: got '${out}', want '${t.expect}'`);
      console.log(`${t.lang} OK -> ${out}`);
    }
    console.log('All new Python lessons pass.');
  } finally {
    try { process.kill(child.pid); } catch {}
  }
}

main().catch((e) => { console.error('Test failed:', e.message); process.exit(1); });

