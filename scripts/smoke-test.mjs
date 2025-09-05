#!/usr/bin/env node
import { spawn } from 'node:child_process';
import { setTimeout as delay } from 'node:timers/promises';

const PORT = process.env.PORT || '3100';
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
      if (!ready) {
        reject(new Error('Server did not start within timeout'));
      }
    }, 8000);
  });
}

async function waitForHttp(url, timeoutMs = 8000) {
  const start = Date.now();
  while (Date.now() - start < timeoutMs) {
    try {
      const r = await fetch(url);
      if (r.ok) return true;
    } catch {}
    await delay(200);
  }
  return false;
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

function ensure(cond, message) {
  if (!cond) throw new Error(message);
}

async function main() {
  console.log('Starting server...');
  const child = await startServer();
  try {
    const ok = await waitForHttp(`${SERVER_URL}/`);
    ensure(ok, 'Server not responding to GET /');
    console.log('GET / OK');

    // Health
    const health = await fetch(`${SERVER_URL}/health`).then(r => r.json()).catch(() => null);
    console.log('Health:', health);

    if (health && health.javac) {
      // Java success
      const javaCode = `public class Main{public static void main(String[]a){System.out.println("Hello, Java!");}}`;
      const jr = await postJson('/run/java', { code: javaCode });
      ensure(jr.status === 200 && jr.json && !jr.json.error && (jr.json.output || '').includes('Hello, Java!'), 'Java run failed');
      console.log('Java run OK');

      // Java compilation error
      const jr2 = await postJson('/run/java', { code: 'public class Main{ public static void main(String[]a){ SYNTAX } }' });
      ensure(jr2.status === 200 && jr2.json && jr2.json.error === true && jr2.json.type === 'compilation', 'Java compilation error not detected');
      console.log('Java compilation error path OK');
    } else {
      console.log('Skipping Java tests (javac not available).');
    }

    // Python success
    const py = await postJson('/run/python', { code: 'print("Hello, Python!")' });
    ensure(py.status === 200 && py.json && !py.json.error && (py.json.output || '').includes('Hello, Python!'), 'Python run failed');
    console.log('Python run OK');

    console.log('Smoke tests passed.');
  } finally {
    try { process.kill(child.pid); } catch {}
  }
}

main().catch((err) => {
  console.error('\nSmoke tests failed:', err.message);
  process.exit(1);
});
