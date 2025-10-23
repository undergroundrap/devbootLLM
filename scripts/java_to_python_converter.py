#!/usr/bin/env python3
"""
Convert Java implementations to Python for all lessons 601-650.
Simple conversion for educational code.
"""

import json
import re


def java_to_python(java_code, expected_output):
    """Convert simple Java code to Python equivalent"""

    # Handle simple cases for soft skills/security lessons
    if "See tutorial for implementation details" in expected_output:
        title_match = re.search(r'// (.+)', java_code)
        title = title_match.group(1) if title_match else "Lesson"
        return f"""# {title}

if __name__ == "__main__":
    print("=== {title} ===")
    print("See tutorial for implementation details")
    print("This lesson focuses on concepts and best practices")
"""

    # Basic Java to Python conversions
    python = java_code

    # Remove import statements and replace with Python equivalents
    python = re.sub(r'import java\.util\.\*;', 'from typing import List, Dict, Set\nfrom collections import deque\nimport heapq', python)

    # Convert class structure
    python = re.sub(r'public class Main \{', '', python)
    python = re.sub(r'static class (\w+) \{', r'class \1:', python)

    # Convert method signatures
    python = re.sub(r'public static (\w+) (\w+)\((.*?)\) \{', r'def \2(\3):', python)
    python = re.sub(r'public (\w+) (\w+)\((.*?)\) \{', r'def \2(self, \3):', python)
    python = re.sub(r'private static (\w+) (\w+)\((.*?)\) \{', r'def \2(\3):', python)

    # Convert data types
    python = python.replace('String', 'str')
    python = python.replace('int[]', 'List[int]')
    python = python.replace('String[]', 'List[str]')
    python = python.replace('Map<String, String>', 'Dict[str, str]')
    python = python.replace('Map<String, Integer>', 'Dict[str, int]')
    python = python.replace('List<String>', 'List[str]')
    python = python.replace('List<Integer>', 'List[int]')
    python = python.replace('Set<String>', 'Set[str]')
    python = python.replace('Queue<String>', 'deque')
    python = python.replace('int ', '')
    python = python.replace('double ', '')
    python = python.replace('boolean ', '')

    # Convert collections
    python = python.replace('new HashMap<>()', '{}')
    python = python.replace('new ArrayList<>()', '[]')
    python = python.replace('new HashSet<>()', 'set()')
    python = python.replace('new LinkedList<>()', 'deque()')

    # Convert common methods
    python = python.replace('.add(', '.append(')
    python = python.replace('.put(', '[')
    python = re.sub(r'\.put\(([^,]+),\s*([^)]+)\)', r'[\1] = \2', python)
    python = python.replace('.get(', '[')
    python = python.replace('.containsKey(', ' in ')
    python = python.replace('.getOrDefault(', '.get(')
    python = python.replace('.size()', '(len())')
    python = python.replace('.length()', '(len())')
    python = python.replace('.charAt(', '[')
    python = python.replace('.toCharArray()', '')
    python = python.replace('.isEmpty()', ' == []')

    # Convert System.out.println
    python = re.sub(r'System\.out\.println\((.*?)\);', r'print(\1)', python)

    # Convert String.format
    python = re.sub(r'String\.format\("([^"]*)",\s*(.*?)\)', r'f"\1".format(\2)', python)

    # Remove semicolons
    python = python.replace(';', '')

    # Remove braces (keep some for dict literals)
    python = re.sub(r'\s*\{\s*$', ':', python, flags=re.MULTILINE)
    python = re.sub(r'^\s*\}\s*$', '', python, flags=re.MULTILINE)

    # Fix main method
    python = re.sub(r'public static void main\(String\[\] args\) \{', 'if __name__ == "__main__":', python)

    # Clean up extra whitespace
    python = re.sub(r'\n\n\n+', '\n\n', python)

    return python.strip()


def main():
    print("=" * 70)
    print("CONVERTING JAVA TO PYTHON FOR ALL LESSONS")
    print("=" * 70)
    print()

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_data = json.load(f)

    updated = 0

    for java_lesson, python_lesson in zip(java_data['lessons'], python_data['lessons']):
        if java_lesson['id'] != python_lesson['id']:
            print(f"ERROR: Lesson ID mismatch {java_lesson['id']} != {python_lesson['id']}")
            continue

        lid = java_lesson['id']

        # Only update lessons 601-650
        if not (601 <= lid <= 650):
            continue

        # Only update if Java has been fixed but Python hasn't
        if len(java_lesson['fullSolution']) > 200 and len(python_lesson['fullSolution']) < 200:
            python_lesson['initialCode'] = java_to_python(java_lesson['initialCode'], java_lesson['expectedOutput'])
            python_lesson['fullSolution'] = java_to_python(java_lesson['fullSolution'], java_lesson['expectedOutput'])
            python_lesson['expectedOutput'] = java_lesson['expectedOutput']

            print(f"  [CONVERTED] Lesson {lid}: {python_lesson['title']}")
            updated += 1

    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(python_data, f, indent=2, ensure_ascii=False)

    print(f"\n[SUCCESS] Converted {updated} lessons to Python")
    print("=" * 70)

if __name__ == "__main__":
    main()
