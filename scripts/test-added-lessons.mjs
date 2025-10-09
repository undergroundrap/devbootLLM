#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';

const PORT = process.env.PORT || '3200';
const SERVER_URL = `http://localhost:${PORT}`;

function loadLessons(relPath) {
  const resolved = path.resolve(relPath);
  const raw = fs.readFileSync(resolved, 'utf8');
  const data = JSON.parse(raw);
  if (!Array.isArray(data?.lessons)) {
    throw new Error(`Invalid lessons file: ${relPath}`);
  }
  return new Map(data.lessons.map((lesson) => [lesson.id, lesson]));
}

function normalizeOutput(text) {
  let value = String(text ?? '');
  value = value.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
  while (value.endsWith('\n')) {
    value = value.slice(0, -1);
  }
  return value;
}

function sanitizeJavaCode(code) {
  let result = '';
  let inString = false;
  let inChar = false;

  for (let i = 0; i < code.length; i += 1) {
    const ch = code[i];

    const prevBackslashes = (() => {
      let count = 0;
      for (let j = i - 1; j >= 0 && code[j] === '\\'; j -= 1) {
        count += 1;
      }
      return count;
    })();
    const escaped = prevBackslashes % 2 === 1;

    if (ch === '"' && !inChar && !escaped) {
      inString = !inString;
      result += ch;
      continue;
    }
    if (ch === "'" && !inString && !escaped) {
      inChar = !inChar;
      result += ch;
      continue;
    }
    if (ch === '\n' && inString) {
      result += '\\n';
      continue;
    }
    result += ch;
  }

  return result;
}

function createLessonTest(lang, id, lessons) {
  const lesson = lessons.get(id);
  if (!lesson) {
    throw new Error(`Missing ${lang} lesson ${id}`);
  }
  if (typeof lesson.fullSolution !== 'string' || !lesson.fullSolution.trim()) {
    throw new Error(`Lesson ${lang} ${id} missing fullSolution`);
  }
  return {
    name: `${lang} ${lesson.id} ${lesson.title.replace(/^[0-9]+\.\s*/, '')}`,
    lang,
    code: lang === 'java' ? sanitizeJavaCode(lesson.fullSolution) : lesson.fullSolution,
    expect: lesson.expectedOutput ?? '',
    expectNormalized: normalizeOutput(lesson.expectedOutput ?? ''),
  };
}

const pythonLessons = loadLessons(path.join('public', 'lessons-python.json'));
const javaLessons = loadLessons(path.join('public', 'lessons-java.json'));

const pythonLessonIds = Array.from({ length: 30 }, (_, index) => 330 + index);
const javaLessonIds = Array.from({ length: 18 }, (_, index) => 340 + index);

const tests = [
  ...pythonLessonIds.map((id) => createLessonTest('python', id, pythonLessons)),
  ...javaLessonIds.map((id) => createLessonTest('java', id, javaLessons)),
];

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

async function postJson(pathname, payload) {
  const r = await fetch(`${SERVER_URL}${pathname}`, {
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

function ensure(cond, msg) {
  if (!cond) throw new Error(msg);
}

async function main() {
  console.log(`Starting server for ${tests.length} tests...`);
  const child = await startServer();
  try {
    for (const t of tests) {
      const endpoint = t.lang === 'python' ? '/run/python' : '/run/java';
      const response = await postJson(endpoint, { code: t.code });
      ensure(response.status === 200 && response.json, `Bad status for ${t.name}`);
      ensure(!response.json.error, `${t.name} runtime error: ${response.json.output || response.json.error}`);
      const rawOut = String(response.json.output ?? '');
      const normalized = normalizeOutput(rawOut);
      ensure(normalized === t.expectNormalized, `${t.name} mismatch: got '${normalized}' (raw '${rawOut}'), want '${t.expectNormalized}'`);
      console.log(`${t.name} OK -> ${normalized}`);
    }
    console.log('All lesson smoke tests passed.');
  } finally {
    try { process.kill(child.pid); } catch {}
  }
}

main().catch((e) => {
  console.error('Test failed:', e.message);
  process.exit(1);
});
