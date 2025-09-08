const fs = require('fs');
const path = require('path');

let BetterSqlite3 = null;
try {
  // Defer requiring so server still runs if dependency missing
  BetterSqlite3 = require('better-sqlite3');
} catch (_) {
  BetterSqlite3 = null;
}

function ensureDirSync(dirPath) {
  try {
    if (!fs.existsSync(dirPath)) {
      fs.mkdirSync(dirPath, { recursive: true });
    }
    return true;
  } catch (_) {
    return false;
  }
}

function openDb(dbFilePath) {
  if (!BetterSqlite3) return null;
  try {
    const dir = path.dirname(dbFilePath);
    ensureDirSync(dir);
    const db = new BetterSqlite3(dbFilePath);
    db.pragma('journal_mode = WAL');
    return db;
  } catch (e) {
    // If opening fails (e.g., read-only FS), run without DB
    return null;
  }
}

function ensureSchema(db) {
  if (!db) return;
  db.exec(`
    CREATE TABLE IF NOT EXISTS lessons (
      language TEXT NOT NULL,
      id INTEGER NOT NULL,
      title TEXT NOT NULL,
      description TEXT DEFAULT '',
      initial_code TEXT DEFAULT '',
      full_solution TEXT DEFAULT '',
      full_solution_commented TEXT DEFAULT '',
      expected_output TEXT DEFAULT '',
      user_input_json TEXT DEFAULT NULL,
      tutorial TEXT DEFAULT '',
      order_index INTEGER DEFAULT NULL,
      PRIMARY KEY (language, id)
    );
  `);
}

function normalizeLesson(raw, defaultLang) {
  const lang = (raw.language ? String(raw.language) : defaultLang || 'java').toLowerCase();
  return {
    language: lang,
    id: Number(raw.id),
    title: String(raw.title || ''),
    description: String(raw.description || ''),
    initial_code: raw.initialCode != null ? String(raw.initialCode) : '',
    full_solution: raw.fullSolution != null ? String(raw.fullSolution) : '',
    full_solution_commented: raw.fullSolutionCommented != null ? String(raw.fullSolutionCommented) : '',
    expected_output: raw.expectedOutput != null ? String(raw.expectedOutput) : '',
    user_input_json: Array.isArray(raw.userInput) ? JSON.stringify(raw.userInput) : null,
    tutorial: raw.tutorial != null ? String(raw.tutorial) : '',
    order_index: Number.isFinite(raw.orderIndex) ? Number(raw.orderIndex) : null,
  };
}

function seedFromJsonFiles(db, opts = {}) {
  if (!db) return { seeded: false, count: 0 };
  const publicDir = opts.publicDir || path.join(process.cwd(), 'public');
  const files = [];
  const pushIf = (p) => { if (fs.existsSync(p)) files.push(p); };
  pushIf(path.join(publicDir, 'lessons-java.json'));
  pushIf(path.join(publicDir, 'lessons-python.json'));
  pushIf(path.join(publicDir, 'lessons.json'));
  let total = 0;
  const insert = db.prepare(`
    INSERT INTO lessons (
      language, id, title, description, initial_code, full_solution, full_solution_commented,
      expected_output, user_input_json, tutorial, order_index
    ) VALUES (@language, @id, @title, @description, @initial_code, @full_solution, @full_solution_commented,
      @expected_output, @user_input_json, @tutorial, @order_index)
    ON CONFLICT(language, id) DO UPDATE SET
      title = excluded.title,
      description = excluded.description,
      initial_code = excluded.initial_code,
      full_solution = excluded.full_solution,
      full_solution_commented = excluded.full_solution_commented,
      expected_output = excluded.expected_output,
      user_input_json = excluded.user_input_json,
      tutorial = excluded.tutorial,
      order_index = excluded.order_index
  `);
  const tx = db.transaction((items) => {
    for (const it of items) insert.run(it);
  });

  let any = false;
  for (const f of files) {
    try {
      const raw = JSON.parse(fs.readFileSync(f, 'utf8'));
      const list = Array.isArray(raw) ? raw : (Array.isArray(raw.lessons) ? raw.lessons : []);
      if (!list || list.length === 0) continue;
      const defaultLang = f.includes('python') ? 'python' : 'java';
      const items = list.map(l => normalizeLesson(l, defaultLang));
      tx(items);
      total += items.length;
      any = true;
    } catch (_) {
      // skip bad file
    }
  }
  return { seeded: any, count: total };
}

function seedFromJsonIfEmpty(db, opts = {}) {
  if (!db) return { seeded: false, count: 0 };
  const row = db.prepare('SELECT COUNT(1) AS c FROM lessons').get();
  if (row && row.c > 0) return { seeded: false, count: 0 };
  try {
    return seedFromJsonFiles(db, opts);
  } catch (_) {
    return { seeded: false, count: 0 };
  }
}

function getLessons(db, language /* 'java' | 'python' | undefined */) {
  if (!db) return [];
  if (language) {
    const rows = db.prepare('SELECT * FROM lessons WHERE language = ? ORDER BY COALESCE(order_index, id) ASC').all(String(language).toLowerCase());
    return rows.map(rowToJsonLesson);
  }
  const rows = db.prepare('SELECT * FROM lessons ORDER BY language ASC, COALESCE(order_index, id) ASC').all();
  return rows.map(rowToJsonLesson);
}

function rowToJsonLesson(r) {
  const obj = {
    id: r.id,
    title: r.title,
    language: r.language,
    description: r.description || '',
    initialCode: r.initial_code || '',
    fullSolution: r.full_solution || '',
    expectedOutput: r.expected_output || '',
    tutorial: r.tutorial || '',
  };
  if (r.full_solution_commented) obj.fullSolutionCommented = r.full_solution_commented;
  if (r.user_input_json) {
    try { obj.userInput = JSON.parse(r.user_input_json); } catch { obj.userInput = []; }
  }
  return obj;
}

module.exports = {
  openDb,
  ensureSchema,
  seedFromJsonFiles,
  seedFromJsonIfEmpty,
  getLessons,
};

