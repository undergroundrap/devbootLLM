#!/usr/bin/env python3
"""
Find all lessons with identical fullSolution code.
Group them to understand which lessons need unique implementations.
"""

import json
from collections import defaultdict
import hashlib


def hash_code(code):
    """Create hash of normalized code."""
    normalized = code.strip().replace(' ', '').replace('\n', '').replace('\r', '')
    return hashlib.md5(normalized.encode()).hexdigest()


def find_duplicates(language):
    """Find all duplicate solutions for a language."""
    filename = f'public/lessons-{language}.json'

    with open(filename, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Group lessons by solution hash
    hash_to_lessons = defaultdict(list)

    for lesson in lessons:
        solution = lesson.get('fullSolution', '')
        if solution and len(solution) > 50:  # Skip very short solutions
            code_hash = hash_code(solution)
            hash_to_lessons[code_hash].append({
                'id': lesson['id'],
                'title': lesson['title'],
                'solution': solution
            })

    # Find groups with duplicates
    duplicates = {}
    for code_hash, lesson_group in hash_to_lessons.items():
        if len(lesson_group) > 1:
            duplicates[code_hash] = lesson_group

    return duplicates


print("\n" + "="*80)
print("FINDING DUPLICATE SOLUTIONS")
print("="*80)

# Find Java duplicates
print("\n\nJAVA DUPLICATES:")
print("-"*80)
java_dups = find_duplicates('java')

for i, (code_hash, lessons) in enumerate(sorted(java_dups.items(), key=lambda x: len(x[1]), reverse=True)[:20], 1):
    print(f"\n{i}. Duplicate group with {len(lessons)} lessons:")
    for lesson in lessons:
        print(f"   - Lesson {lesson['id']}: {lesson['title']}")

    # Show first few lines of solution
    first_solution = lessons[0]['solution']
    preview = '\n'.join(first_solution.split('\n')[:5])
    print(f"   Solution preview:\n   {preview[:150]}...")

print(f"\n\nTotal Java duplicate groups: {len(java_dups)}")
print(f"Total Java lessons with duplicates: {sum(len(g) for g in java_dups.values())}")

# Find Python duplicates
print("\n\n" + "="*80)
print("PYTHON DUPLICATES:")
print("-"*80)
python_dups = find_duplicates('python')

for i, (code_hash, lessons) in enumerate(sorted(python_dups.items(), key=lambda x: len(x[1]), reverse=True)[:20], 1):
    print(f"\n{i}. Duplicate group with {len(lessons)} lessons:")
    for lesson in lessons:
        print(f"   - Lesson {lesson['id']}: {lesson['title']}")

    # Show first few lines of solution
    first_solution = lessons[0]['solution']
    preview = '\n'.join(first_solution.split('\n')[:5])
    print(f"   Solution preview:\n   {preview[:150]}...")

print(f"\n\nTotal Python duplicate groups: {len(python_dups)}")
print(f"Total Python lessons with duplicates: {sum(len(g) for g in python_dups.values())}")

print("\n" + "="*80)
print(f"GRAND TOTAL: {len(java_dups) + len(python_dups)} duplicate groups")
print(f"LESSONS AFFECTED: {sum(len(g) for g in java_dups.values()) + sum(len(g) for g in python_dups.values())} lessons")
print("="*80 + "\n")
