import fs from 'fs';

const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

console.log('PYTHON LESSONS TO CHECK:');
[20, 24, 37, 61].forEach(id => {
  const lesson = pythonLessons.find(l => l.id === id);
  console.log(`Lesson ${id}: ${lesson.title}`);
  console.log(`  Has examples: ${!!lesson.additionalExamples}`);
  console.log(`  Solution: ${lesson.fullSolution.substring(0, 80)}...`);
  console.log('');
});

console.log('JAVA LESSONS TO CHECK:');
[9, 11, 74, 80].forEach(id => {
  const lesson = javaLessons.find(l => l.id === id);
  console.log(`Lesson ${id}: ${lesson.title}`);
  console.log(`  Has examples: ${!!lesson.additionalExamples}`);
  console.log(`  Solution: ${lesson.fullSolution.substring(0, 80)}...`);
  console.log('');
});
