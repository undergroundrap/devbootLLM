#!/usr/bin/env node
/**
 * Insert a lesson with a specific id into a lessons JSON file.
 * Usage:
 *   node scripts/insert-lesson.mjs <lessons.json> <id> <lesson-definition.js>
 *
 * The definition module must export an object named `lesson` with no `id` and with a `title` without numeric prefix.
 */
import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';

const [jsonPath, idArg, defPath] = process.argv.slice(2);
if (!jsonPath || !idArg || !defPath) {
  console.error('Usage: node scripts/insert-lesson.mjs <lessons.json> <id> <lesson-definition.js>');
  process.exit(2);
}
const id = Number(idArg);
if (!Number.isInteger(id) || id <= 0) {
  console.error('Invalid id. Must be positive integer.');
  process.exit(3);
}

const json = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
if (!Array.isArray(json.lessons)) {
  console.error('Invalid lessons file; missing lessons array');
  process.exit(4);
}

const exists = json.lessons.some(l => l.id === id);
if (exists) {
  console.error(`Lesson id ${id} already exists in ${jsonPath}`);
  process.exit(5);
}

const defUrl = url.pathToFileURL(path.resolve(defPath)).href;
const mod = await import(defUrl);
const src = mod.lesson;
if (!src || typeof src !== 'object') {
  console.error('Definition must export object `lesson`.');
  process.exit(6);
}

const inferredLang = jsonPath.toLowerCase().includes('python') ? 'python' : (jsonPath.toLowerCase().includes('java') ? 'java' : null);
const obj = { ...src };
obj.id = id;
if (!obj.language && inferredLang) obj.language = inferredLang;
if (typeof obj.title !== 'string') {
  console.error('Lesson must have `title`.');
  process.exit(7);
}
obj.title = `${id}. ${obj.title.replace(/^\d+\.\s*/, '')}`;

json.lessons.push(obj);
json.lessons.sort((a,b) => (a.id ?? 0) - (b.id ?? 0));
fs.writeFileSync(jsonPath, JSON.stringify(json, null, 2) + '\n', 'utf8');
console.log(`Inserted lesson id ${id} into ${jsonPath}`);

