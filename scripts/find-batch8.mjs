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

console.log(`Total Python beginner lessons without examples: ${pythonBeginner.length}`);
console.log(`Total Java beginner lessons without examples: ${javaBeginner.length}`);

console.log('\nPYTHON BEGINNER LESSONS (next 4):');
pythonBeginner.slice(0, 4).forEach(l => {
  console.log(`  Lesson ${l.id}: ${l.title}`);
});

console.log('\nJAVA BEGINNER LESSONS (next 4):');
javaBeginner.slice(0, 4).forEach(l => {
  console.log(`  Lesson ${l.id}: ${l.title}`);
});
