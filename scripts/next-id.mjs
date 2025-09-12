#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const file = process.argv[2];
if (!file) {
  console.error('Usage: node scripts/next-id.mjs public/lessons-<lang>.json');
  process.exit(1);
}

const abs = path.resolve(file);
const raw = JSON.parse(fs.readFileSync(abs, 'utf8'));
const list = Array.isArray(raw.lessons) ? raw.lessons : raw;
const ids = list.map(l => l && l.id).filter(n => Number.isFinite(n));
const max = ids.length ? Math.max(...ids) : 0;
console.log(String(max + 1));

