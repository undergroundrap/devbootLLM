const { openDb, countLessons } = require('../db');
const path = require('path');

const DB_FILE = path.join(process.cwd(), 'data', 'app.db');

console.log('Checking database:', DB_FILE);

try {
    const db = openDb(DB_FILE);
    if (!db) {
        console.log('[ERROR] Could not open database');
        process.exit(1);
    }

    const javaCount = countLessons(db, 'java');
    const pythonCount = countLessons(db, 'python');

    console.log(`\n[RESULTS]`);
    console.log(`Java lessons:   ${javaCount} ${javaCount === 700 ? '[OK]' : '[MISMATCH - Expected 700]'}`);
    console.log(`Python lessons: ${pythonCount} ${pythonCount === 700 ? '[OK]' : '[MISMATCH - Expected 700]'}`);

    if (javaCount === 700 && pythonCount === 700) {
        console.log(`\n[SUCCESS] Database contains all 700 lessons for both languages!`);
        process.exit(0);
    } else {
        console.log(`\n[ISSUE] Database is missing lessons. Please restart server to rebuild.`);
        process.exit(1);
    }
} catch (err) {
    console.error('[ERROR]', err.message);
    process.exit(1);
}
