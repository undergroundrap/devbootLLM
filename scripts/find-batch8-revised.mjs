import fs from 'fs';

const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

// Find Python beginner lessons without examples
const pythonBeginner = pythonLessons.filter(l =>
  l.tags && l.tags.includes('Beginner') && !l.additionalExamples
);

// Find Java beginner lessons without examples
const javaBeginner = javaLessons.filter(l =>
  l.tags && l.tags.includes('Beginner') && !l.additionalExamples
);

console.log('PYTHON BEGINNER LESSONS (IDs):');
pythonBeginner.slice(0, 10).forEach(l => {
  console.log(`  ${l.id}: ${l.title}`);
});

console.log('\nJAVA BEGINNER LESSONS (IDs):');
javaBeginner.slice(0, 10).forEach(l => {
  console.log(`  ${l.id}: ${l.title}`);
});

// Pick lessons 10, 54, 65, 66 for Python
console.log('\n=== BATCH 8 CANDIDATES ===');
console.log('Python: 10, 54, 65, 66');
console.log('Java: 17, 18, 19, 20');

[10, 54, 65, 66].forEach(id => {
  const l = pythonLessons.find(x => x.id === id);
  console.log(`\nPython ${id}: ${l.title}`);
  console.log(`  Solution: ${l.fullSolution.substring(0, 80)}...`);
});

[17, 18, 19, 20].forEach(id => {
  const l = javaLessons.find(x => x.id === id);
  console.log(`\nJava ${id}: ${l.title}`);
  console.log(`  Solution: ${l.fullSolution.substring(0, 80)}...`);
});
