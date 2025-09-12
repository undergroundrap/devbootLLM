#!/usr/bin/env node
/**
 * Print the next sequential id for the given lessons JSON file.
 * Usage: node scripts/next-id.mjs public/lessons-python.json
 */
import fs from 'node:fs';

const file = process.argv[2];
if (!file) {
  console.error('Usage: node scripts/next-id.mjs <path-to-lessons.json>');
  process.exit(2);
}

const raw = fs.readFileSync(file, 'utf8');
const data = JSON.parse(raw);
const lessons = Array.isArray(data?.lessons) ? data.lessons : [];
const maxId = lessons.reduce((m, l) => (typeof l.id === 'number' && l.id > m ? l.id : m), 0);
console.log(maxId + 1);

