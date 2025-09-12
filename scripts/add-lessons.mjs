#!/usr/bin/env node
/**
 * Append new lesson objects to a lessons JSON file with auto ids and title prefixes.
 * Usage:
 *   node scripts/add-lessons.mjs <lessons.json> <lessons-definition.js>
 *
 * Where lessons-definition.js exports an array named `lessons` with objects missing `id` and with `title` without numeric prefix.
 * This script will:
 *   - Load the JSON, compute next id
 *   - For each new lesson, set id and prefix title as `${id}. <title>`
 *   - Push to the lessons array and write back formatted JSON
 */
import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';

const [jsonPath, defPath] = process.argv.slice(2);
if (!jsonPath || !defPath) {
  console.error('Usage: node scripts/add-lessons.mjs <lessons.json> <lessons-definition.js>');
  process.exit(2);
}

const json = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
if (!Array.isArray(json.lessons)) {
  console.error('Invalid lessons file; missing lessons array');
  process.exit(3);
}

// Dynamic import of definitions
const defUrl = url.pathToFileURL(path.resolve(defPath)).href;
const mod = await import(defUrl);
const pending = mod.lessons;
if (!Array.isArray(pending) || !pending.length) {
  console.error('Definition file must export array `lessons` with at least one item');
  process.exit(4);
}

const startId = json.lessons.reduce((m, l) => (typeof l.id === 'number' && l.id > m ? l.id : m), 0) + 1;
let id = startId;
for (const l of pending) {
  const obj = { ...l };
  obj.id = id;
  if (typeof obj.title !== 'string') {
    console.error('Each lesson must have a `title`');
    process.exit(5);
  }
  obj.title = `${id}. ${obj.title.replace(/^\d+\.\s*/, '')}`;
  json.lessons.push(obj);
  id += 1;
}

fs.writeFileSync(jsonPath, JSON.stringify(json, null, 2) + '\n', 'utf8');
console.log(`Added ${pending.length} lesson(s) to ${jsonPath} starting at id ${startId}`);

