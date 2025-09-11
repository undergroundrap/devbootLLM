#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const pub = path.join(root, 'public');
const files = ['lessons-java.json', 'lessons-python.json'];

let hasError = false;

function readJson(file) {
  try {
    const s = fs.readFileSync(path.join(pub, file), 'utf8');
    return JSON.parse(s);
  } catch (e) {
    console.error(`[error] Failed to read ${file}: ${e.message}`);
    hasError = true;
    return null;
  }
}

function validateList(list, langLabel) {
  const issues = [];
  const ids = new Set();
  for (let i = 0; i < list.length; i++) {
    const l = list[i];
    const key = `${langLabel}:${l?.id ?? `idx${i}`}`;
    if (!l || typeof l !== 'object') { issues.push(`${key} invalid object`); continue; }
    if (typeof l.id === 'undefined') issues.push(`${key} missing id`);
    if (typeof l.title !== 'string' || !l.title.trim()) issues.push(`${key} missing title`);
    if (typeof l.description !== 'string' || !l.description.trim()) issues.push(`${key} missing description`);
    if (typeof l.initialCode !== 'string' || !l.initialCode.trim()) issues.push(`${key} missing initialCode`);
    if (typeof l.expectedOutput !== 'string' || !l.expectedOutput.trim()) issues.push(`${key} missing expectedOutput`);
    if (typeof l.tutorial !== 'string' || !l.tutorial.trim()) issues.push(`${key} missing tutorial`);
    if (ids.has(l.id)) issues.push(`${key} duplicate id in ${langLabel}`); else ids.add(l.id);
  }
  // Check monotonic id growth (not strictly required, but helpful)
  const sorted = [...list].map(l => l.id).filter(n => Number.isFinite(n)).sort((a,b)=>a-b);
  for (let i = 1; i < sorted.length; i++) {
    if (sorted[i] === sorted[i-1]) continue; // already reported duplicate
    if (sorted[i] < sorted[i-1]) {
      issues.push(`${langLabel}: id order not ascending around ${sorted[i-1]} -> ${sorted[i]}`);
      break;
    }
  }
  return issues;
}

for (const f of files) {
  const data = readJson(f);
  if (!data) continue;
  const list = Array.isArray(data.lessons) ? data.lessons : (Array.isArray(data) ? data : []);
  const langLabel = f.includes('python') ? 'python' : 'java';
  const issues = validateList(list, langLabel);
  if (issues.length) {
    console.error(`\n[${langLabel}] ${issues.length} issue(s):`);
    for (const is of issues) console.error(' -', is);
    hasError = true;
  } else {
    console.log(`[${langLabel}] OK (${list.length} lessons)`);
  }
}

process.exit(hasError ? 1 : 0);

