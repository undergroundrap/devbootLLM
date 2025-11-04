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

console.log('=== BATCH 10 CANDIDATES ===');
console.log(`\nTotal Python beginner without examples: ${pythonBeginner.length}`);
console.log(`Total Java beginner without examples: ${javaBeginner.length}`);

console.log('\nPYTHON LESSONS (picking 15, 16, 19, 25):');
[15, 16, 19, 25].forEach(id => {
  const l = pythonLessons.find(x => x.id === id);
  if (l) {
    console.log(`  ${id}: ${l.title} - Has examples: ${!!l.additionalExamples}`);
    console.log(`      Solution: ${l.fullSolution.substring(0, 60)}...`);
  }
});

console.log('\nJAVA LESSONS (picking 25, 26, 27, 28):');
[25, 26, 27, 28].forEach(id => {
  const l = javaLessons.find(x => x.id === id);
  if (l) {
    console.log(`  ${id}: ${l.title} - Has examples: ${!!l.additionalExamples}`);
    console.log(`      Solution: ${l.fullSolution.substring(0, 60)}...`);
  }
});
