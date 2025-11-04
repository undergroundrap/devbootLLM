import fs from 'fs';

const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

// Find Python beginner lessons without examples
const pythonBeginner = pythonLessons.filter(l =>
  l.tags && l.tags.includes('Beginner') && !l.additionalExamples
).slice(0, 8);

// Find Java beginner lessons without examples
const javaBeginner = javaLessons.filter(l =>
  l.tags && l.tags.includes('Beginner') && !l.additionalExamples
).slice(0, 8);

console.log('PYTHON BEGINNER LESSONS (next batch):');
pythonBeginner.forEach(l => {
  console.log(`  Lesson ${l.id}: ${l.title}`);
});

console.log('\nJAVA BEGINNER LESSONS (next batch):');
javaBeginner.forEach(l => {
  console.log(`  Lesson ${l.id}: ${l.title}`);
});
