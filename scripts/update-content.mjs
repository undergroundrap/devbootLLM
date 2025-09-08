#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

function removeInlineBlock(filePath, startMarker, endMarker) {
  const abs = path.resolve(filePath);
  let content = fs.readFileSync(abs, 'utf8');
  const startIdx = content.indexOf(startMarker);
  if (startIdx === -1) return { changed: false, reason: 'start marker not found' };
  const endIdx = content.indexOf(endMarker, startIdx + startMarker.length);
  if (endIdx === -1) return { changed: false, reason: 'end marker not found' };
  const before = content.slice(0, startIdx);
  const after = content.slice(endIdx + endMarker.length);
  // If the next lines already include the external JSON setup, keep as is.
  content = before + after;
  fs.writeFileSync(abs, content, 'utf8');
  return { changed: true };
}

function buildPythonExample(desc) {
  const d = (desc || '').toLowerCase();
  const snips = [
    [/(hello,? world|print)/, `print("Welcome to Python!")\nprint(123)`],
    [/(variable|data\s*types?)/, `my_number = 42\nname = "Alice"\npi = 3.14\nis_active = True\nprint(name, my_number)`],
    [/(while)/, `i = 1\nwhile i <= 3:\n    print(i)\n    i += 1`],
    [/(for|loop)/, `for i in range(3):\n    print(i)`],
    [/(list|array)/, `numbers = [10, 20, 30]\nprint(numbers[1])  # 20\nnumbers.append(40)`],
    [/(function|def\s)/, `def greet(name):\n    print(f"Hello, {name}")\n\ngreet("World")`],
    [/(string)/, `s = "hello"\nprint(s.upper())   # HELLO\nprint(len(s))      # 5`],
    [/(dict|dictionary|map)/, `user = {"name": "Ada", "age": 36}\nprint(user["name"])\nuser["city"] = "London"`],
    [/(tuple)/, `t = (1, 2, 3)\nprint(t[0])`],
    [/(set)/, `s = {1, 2, 2, 3}\nprint(s)\ns.add(4)`],
    [/(class|object)/, `class Dog:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        print(f"{self.name} says woof")\n\nd = Dog("Fido")\nd.speak()`],
    [/(input)/, `name = input()\nprint("Hello, " + name)`],
    [/(file)/, `with open('data.txt', 'w') as f:\n    f.write('hi')\nwith open('data.txt') as f:\n    print(f.read())`],
    [/(exception|try)/, `try:\n    num = int("abc")\nexcept ValueError as e:\n    print("Invalid number:", e)`],
    [/(comprehension)/, `squares = [i*i for i in range(5)]\nprint(squares)`],
  ];
  for (const [re, code] of snips) {
    if (re.test(d)) return code;
  }
  return `x = 10\ny = 20\nprint(x + y)`;
}

function ensureParagraph(htmlOrText) {
  const s = String(htmlOrText || '').trim();
  if (!s) return '';
  // If looks like HTML already, return as is; else wrap in <p>
  if (s.startsWith('<')) return s;
  return `<p class="mb-4 text-gray-300">${s.replaceAll('<', '&lt;').replaceAll('>', '&gt;')}</p>`;
}

function enhancePythonTutorials(filePath) {
  const abs = path.resolve(filePath);
  const json = JSON.parse(fs.readFileSync(abs, 'utf8'));
  let modified = 0;
  if (!json || !Array.isArray(json.lessons)) return { changed: false, reason: 'lessons missing' };
  json.lessons = json.lessons.map((lesson) => {
    const lang = (lesson.language || '').toLowerCase();
    if (lang && lang !== 'python') return lesson;
    const t = String(lesson.tutorial || '').trim();
    if (t.includes('code-block-wrapper')) return lesson; // already enhanced
    const intro = t || ensureParagraph(lesson.description || '');
    const example = buildPythonExample(lesson.description || '');
    const enriched = `${intro}<h4 class="font-semibold text-gray-200 mb-2">Example:</h4><div class="code-block-wrapper"><pre class="tutorial-code-block">${example}</pre></div>`;
    modified++;
    return { ...lesson, tutorial: enriched };
  });
  fs.writeFileSync(abs, JSON.stringify(json, null, 2), 'utf8');
  return { changed: modified > 0, count: modified };
}

function main() {
  const rm = removeInlineBlock('public/index.html', '/* Inlined Java lessons removed; rely on JSON files only.', '*/');
  if (rm.changed) {
    console.log('Removed commented inline Java lessons from public/index.html');
  } else {
    console.log('No inline Java lessons block found (or already removed).');
  }

  const enh = enhancePythonTutorials('public/lessons-python.json');
  if (enh.changed) {
    console.log(`Enhanced Python tutorials with example code blocks (${enh.count} lessons updated).`);
  } else {
    console.log('Python tutorials already enhanced or file missing.');
  }
}

main();

