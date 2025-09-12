#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

function dupIds(file) {
  const p = path.resolve(file);
  const raw = JSON.parse(fs.readFileSync(p, 'utf8'));
  const list = Array.isArray(raw.lessons) ? raw.lessons : raw;
  const seen = new Map();
  const dups = new Map();
  for (const l of list) {
    const id = l && l.id;
    if (!Number.isFinite(id)) continue;
    if (seen.has(id)) dups.set(id, (dups.get(id) || 1) + 1);
    else seen.set(id, true);
  }
  return Array.from(dups.keys()).sort((a,b)=>a-b);
}

for (const f of process.argv.slice(2)) {
  const d = dupIds(f);
  console.log(f, 'dups:', d.length ? d.join(',') : '(none)');
}

