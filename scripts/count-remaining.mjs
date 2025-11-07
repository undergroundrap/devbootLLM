import fs from 'fs';

const p = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const j = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

const levels = ['Beginner', 'Advanced', 'Expert'];

console.log('REMAINING LESSONS TO ENHANCE:\n');

levels.forEach(level => {
  const pythonCount = p.filter(l => l.tags && l.tags.includes(level)).length;
  const javaCount = j.filter(l => l.tags && l.tags.includes(level)).length;
  const total = pythonCount + javaCount;

  console.log(`${level}:`);
  console.log(`  Python: ${pythonCount}`);
  console.log(`  Java: ${javaCount}`);
  console.log(`  Total: ${total}`);
  console.log();
});

const totalPython = p.filter(l => l.tags && (l.tags.includes('Beginner') || l.tags.includes('Advanced') || l.tags.includes('Expert'))).length;
const totalJava = j.filter(l => l.tags && (l.tags.includes('Beginner') || l.tags.includes('Advanced') || l.tags.includes('Expert'))).length;

console.log('GRAND TOTAL:', totalPython + totalJava, 'lessons');
console.log('  Python:', totalPython);
console.log('  Java:', totalJava);
