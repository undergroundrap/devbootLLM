import fs from 'fs';

const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

console.log('PYTHON LESSONS:');
[6, 7, 8, 9].forEach(id => {
  const lesson = pythonLessons.find(l => l.id === id);
  console.log(`Lesson ${id}: ${lesson.title} - Has examples: ${!!lesson.additionalExamples}`);
});

console.log('\nJAVA LESSONS:');
[13, 14, 15, 16].forEach(id => {
  const lesson = javaLessons.find(l => l.id === id);
  console.log(`Lesson ${id}: ${lesson.title} - Has examples: ${!!lesson.additionalExamples}`);
});
