import json
import re

# Load both files
with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
    java_data = json.load(f)

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    python_data = json.load(f)

java_lessons = {l['id']: l for l in java_data['lessons']}
python_lessons_dict = {l['id']: l for l in python_data['lessons']}

# Get lessons 651-695 from Java
lessons_to_add = []
for lesson_id in range(651, 696):
    if lesson_id in java_lessons:
        lessons_to_add.append(java_lessons[lesson_id])

print(f"Found {len(lessons_to_add)} lessons to convert to Python")

def java_to_python(java_code):
    """Convert Java code to Python"""
    # For career lessons (661, 671, 681, 691, 695), keep mostly as-is with comments
    # For code lessons, do basic conversions

    code = java_code

    # Basic replacements
    code = re.sub(r'import java\.util\.\*;', 'from typing import List, Dict, Optional\nfrom datetime import datetime, timedelta, date\nimport hashlib', code)
    code = re.sub(r'import java\.time\.\*;', '', code)
    code = re.sub(r'import java\.time\.format\.\*;', '', code)

    # Class definitions
    code = re.sub(r'class (\w+) \{', r'class \1:', code)
    code = re.sub(r'public class (\w+) \{', r'class \1:', code)

    # Remove type declarations
    code = re.sub(r'private final (\w+)', r'', code)
    code = re.sub(r'private (\w+)', r'', code)
    code = re.sub(r'public (\w+)', r'', code)
    code = re.sub(r'final (\w+)', r'', code)

    # Main method
    code = re.sub(r'public static void main\(String\[\] args\)', 'def main():', code)

    # Print statements
    code = re.sub(r'System\.out\.println\((.*?)\);', r'print(\1)', code)
    code = re.sub(r'System\.out\.printf\((.*?)\);', r'print(\1)', code)

    # Remove braces
    code = code.replace('{', '').replace('}', '')

    # Fix indentation  (rough - will need manual cleanup)
    lines = code.split('\n')
    cleaned = []
    for line in lines:
        line = line.rstrip()
        if line:
            cleaned.append(line)

    return '\n'.join(cleaned)

# Convert lessons
python_lessons_to_add = []

for java_lesson in lessons_to_add:
    py_lesson = java_lesson.copy()

    # Update language
    py_lesson['language'] = 'python'

    # For career-focused lessons (661, 671, 681, 691, 695), keep code mostly as-is since they're language-agnostic
    if py_lesson['id'] in [661, 671, 681, 691, 695]:
        # Just update the minimal Python syntax
        py_lesson['initialCode'] = py_lesson['initialCode'].replace('public class', 'class').replace('public static void main(String[] args)', 'def main():').replace('System.out.println', 'print')
        py_lesson['fullSolution'] = py_lesson['fullSolution'].replace('public class', 'class').replace('public static void main(String[] args)', 'def main():').replace('System.out.println', 'print')

    python_lessons_to_add.append(py_lesson)

# Add to Python lessons
for lesson in python_lessons_to_add:
    if lesson['id'] not in python_lessons_dict:
        python_data['lessons'].append(lesson)
        print(f"Added lesson {lesson['id']}: {lesson['title']}")

# Save Python file
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(python_data, f, indent=2, ensure_ascii=False)

print(f"\nSuccess! Python now has {len(python_data['lessons'])} lessons")
