#!/usr/bin/env node
/**
 * Validate lessons JSON files for required fields, id continuity, and basic tutorial quality.
 * Usage:
 *   node scripts/validate-lessons.mjs [paths...]
 * If no paths are provided, validates public/lessons-python.json and public/lessons-java.json if present.
 */
import fs from 'node:fs';
import path from 'node:path';

const defaultFiles = [
  path.join('public', 'lessons-python.json'),
  path.join('public', 'lessons-java.json'),
];

const files = process.argv.slice(2);
const targets = files.length ? files : defaultFiles.filter(f => fs.existsSync(f));

if (!targets.length) {
  console.error('No lesson files found. Specify paths or ensure defaults exist.');
  process.exit(2);
}

const REQUIRED = ['id', 'title', 'language', 'description', 'initialCode', 'fullSolution', 'expectedOutput', 'tutorial'];

function summarize(file) {
  let data;
  try {
    const raw = fs.readFileSync(file, 'utf8');
    data = JSON.parse(raw);
  } catch (err) {
    return { file, error: `Invalid JSON: ${err.message}` };
  }
  const lessons = Array.isArray(data?.lessons) ? data.lessons : [];
  const issues = [];
  const byId = new Map();
  const byTitle = new Map();
  let prevId = 0;
  for (const l of lessons) {
    // Required fields
    const miss = REQUIRED.filter(k => !(k in l) || l[k] === null || String(l[k]).trim() === '');
    if (miss.length) issues.push({ type: 'missing_fields', id: l.id, title: l.title, miss });

    // ID continuity
    if (typeof l.id !== 'number' || !Number.isInteger(l.id)) {
      issues.push({ type: 'bad_id', id: l.id, title: l.title });
    } else if (l.id !== prevId + 1) {
      issues.push({ type: 'gap_or_out_of_order', prev: prevId, got: l.id, title: l.title });
      prevId = l.id; // continue from here to avoid cascades
    } else {
      prevId = l.id;
    }

    // Title numeric prefix
    if (typeof l.title === 'string') {
      const expectedPrefix = `${l.id}.`;
      if (!l.title.trim().startsWith(expectedPrefix)) {
        issues.push({ type: 'title_id_mismatch', id: l.id, title: l.title });
      }
    }

    // Tutorial basic quality checks
    if (typeof l.tutorial === 'string') {
      const hasCodeBlock = l.tutorial.includes('<pre');
      if (!hasCodeBlock) issues.push({ type: 'tutorial_missing_example', id: l.id, title: l.title });
      const plainText = l.tutorial.replace(/<[^>]*>/g, '').trim();
      if (plainText.length < 60) issues.push({ type: 'tutorial_too_short', id: l.id, title: l.title, len: plainText.length });
    }

    // Duplicate checks
    if (byId.has(l.id)) issues.push({ type: 'duplicate_id', id: l.id, titles: [byId.get(l.id), l.title] });
    byId.set(l.id, l.title);
    if (typeof l.title === 'string') {
      const t = l.title.trim().toLowerCase();
      if (byTitle.has(t)) issues.push({ type: 'duplicate_title', id: l.id, title: l.title });
      byTitle.set(t, l.id);
    }
  }
  return { file, count: lessons.length, issues };
}

const results = targets.map(summarize);
for (const r of results) {
  if (r.error) {
    console.log(`FILE: ${r.file} -> ERROR: ${r.error}`);
    continue;
  }
  console.log(`FILE: ${r.file}`);
  console.log(`  lessons: ${r.count}`);
  const grouped = r.issues.reduce((acc, it) => { (acc[it.type] ||= []).push(it); return acc; }, {});
  const types = Object.keys(grouped);
  if (!types.length) {
    console.log('  issues: none');
  } else {
    for (const t of types) {
      console.log(`  ${t}: ${grouped[t].length}`);
    }
    // Show sample of most important categories
    const show = ['missing_fields', 'gap_or_out_of_order', 'title_id_mismatch', 'tutorial_missing_example', 'tutorial_too_short', 'duplicate_id', 'duplicate_title'];
    for (const t of show) {
      if (grouped[t]?.length) {
        console.log(`  sample ${t}:`, grouped[t].slice(0, 3));
      }
    }
  }
}

