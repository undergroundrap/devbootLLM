#!/usr/bin/env node
/**
 * Normalize lessons JSON:
 * - Ensure `language` field is set (derived from filename if missing)
 * - Ensure tutorial contains a code example block; if missing, append from fullSolution
 * - Ensure tutorial has a minimum length; if too short, append a rationale sentence
 * - Ensure title numeric prefix matches id
 * - Sort lessons by id ascending
 *
 * Usage: node scripts/normalize-lessons.mjs <path-to-lessons.json>
 */
import fs from 'node:fs';
import path from 'node:path';

const file = process.argv[2];
if (!file) {
  console.error('Usage: node scripts/normalize-lessons.mjs <path-to-lessons.json>');
  process.exit(2);
}

const raw = fs.readFileSync(file, 'utf8');
const data = JSON.parse(raw);
if (!Array.isArray(data?.lessons)) {
  console.error('Invalid lessons file; missing lessons array');
  process.exit(3);
}

const inferredLang = file.toLowerCase().includes('python') ? 'python' : (file.toLowerCase().includes('java') ? 'java' : null);

const MIN_TUTORIAL_TEXT = 80;

function toCodeBlock(code, lang) {
  // Trim to a reasonable snippet
  const lines = String(code ?? '').split(/\r?\n/).slice(0, 12); // at most 12 lines
  const block = lines.join('\n').trim();
  if (!block) return '';
  return `<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>` +
         `<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">${escapeHtml(block)}</pre></div>`;
}

function escapeHtml(s) {
  return String(s)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;');
}

let changed = 0;
for (const l of data.lessons) {
  // Language
  if (!l.language && inferredLang) {
    l.language = inferredLang;
    changed++;
  }

  // Title prefix
  if (typeof l.id === 'number' && typeof l.title === 'string') {
    const rest = l.title.replace(/^\d+\.\s*/, '');
    const want = `${l.id}. ${rest}`;
    if (l.title !== want) {
      l.title = want;
      changed++;
    }
  }

  // Tutorial content
  if (typeof l.tutorial === 'string') {
    const hasBlock = l.tutorial.includes('<pre');
    let plain = l.tutorial.replace(/<[^>]*>/g, '').trim();
    if (!hasBlock) {
      const block = toCodeBlock(l.fullSolution || l.initialCode, l.language);
      if (block) {
        // Insert before end or just append
        l.tutorial = l.tutorial.trimEnd() + (l.tutorial.endsWith('</p>') ? '' : '') + block;
        plain = l.tutorial.replace(/<[^>]*>/g, '').trim();
        changed++;
      }
    }
    if (plain.length < MIN_TUTORIAL_TEXT) {
      const add = `<p class=\"mb-4 text-gray-300\">Tip: Read the prompt carefully and build up the solution step-by-step. Run often to verify output matches exactly.</p>`;
      l.tutorial = l.tutorial.trimEnd() + add;
      changed++;
    }
  }
}

// Sort by id ascending
data.lessons.sort((a, b) => (a.id ?? 0) - (b.id ?? 0));

fs.writeFileSync(file, JSON.stringify(data, null, 2) + '\n', 'utf8');
console.log(`Normalized ${file}. Changes applied: ${changed}`);

