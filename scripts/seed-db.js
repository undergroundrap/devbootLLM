#!/usr/bin/env node
const path = require('path');
const { openDb, ensureSchema, seedFromJsonFiles } = require('../db');

function main() {
  const DATA_DIR = process.env.DATA_DIR || process.env.DB_DIR || (process.platform === 'win32' ? path.join(process.cwd(), 'data') : '/data');
  const DB_FILE = process.env.DB_FILE || path.join(DATA_DIR, 'app.db');
  const PUBLIC_DIR = process.env.PUBLIC_DIR || path.join(process.cwd(), 'public');

  const db = openDb(DB_FILE);
  if (!db) {
    console.error('[seed-db] Could not open DB at', DB_FILE);
    process.exitCode = 1;
    return;
  }
  ensureSchema(db);
  const res = seedFromJsonFiles(db, { publicDir: PUBLIC_DIR });
  console.log(`[seed-db] Seeded ${res.count} lessons from JSON (${res.seeded ? 'ok' : 'no changes'})`);
}

main();

