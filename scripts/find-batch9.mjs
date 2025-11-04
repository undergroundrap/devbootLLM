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

console.log('=== BATCH 9 CANDIDATES ===');
console.log(`\nTotal Python beginner without examples: ${pythonBeginner.length}`);
console.log(`Total Java beginner without examples: ${javaBeginner.length}`);

console.log('\nPYTHON LESSONS (picking 11, 12, 13, 14):');
[11, 12, 13, 14].forEach(id => {
  const l = pythonLessons.find(x => x.id === id);
  if (l) {
    console.log(`  ${id}: ${l.title} - Has examples: ${!!l.additionalExamples}`);
    console.log(`      Solution: ${l.fullSolution.substring(0, 60)}...`);
  }
});

console.log('\nJAVA LESSONS (picking 21, 22, 23, 24):');
[21, 22, 23, 24].forEach(id => {
  const l = javaLessons.find(x => x.id === id);
  if (l) {
    console.log(`  ${id}: ${l.title} - Has examples: ${!!l.additionalExamples}`);
    console.log(`      Solution: ${l.fullSolution.substring(0, 60)}...`);
  }
});
