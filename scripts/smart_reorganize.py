#!/usr/bin/env python3
"""
Smart lesson reorganization:
1. Keep Hello World at ID 1
2. Integrate new beginner lessons into beginner section in logical order
3. Keep all other difficulty levels in original order
"""

import json
from collections import defaultdict


def get_topic_priority(title, category):
    """Determine topic priority for logical ordering."""
    title_lower = title.lower()

    # Core fundamentals first
    if 'hello world' in title_lower:
        return (0, 0, title)
    if 'variable' in title_lower and 'print' in title_lower:
        return (1, 0, title)
    if 'print' in title_lower or 'output' in title_lower:
        return (1, 1, title)
    if 'comment' in title_lower:
        return (1, 2, title)
    if 'variable' in title_lower:
        return (2, 0, title)
    if 'data type' in title_lower or 'integer' in title_lower or 'float' in title_lower or 'boolean' in title_lower:
        return (3, 0, title)
    if 'string' in title_lower and 'basic' in title_lower:
        return (4, 0, title)
    if 'operator' in title_lower or 'arithmetic' in title_lower:
        return (5, 0, title)
    if 'input' in title_lower or 'scanner' in title_lower or 'reading' in title_lower:
        return (6, 0, title)

    # Control flow
    if 'if' in title_lower or 'condition' in title_lower or 'boolean' in title_lower:
        return (7, 0, title)
    if 'switch' in title_lower or 'case' in title_lower:
        return (8, 0, title)
    if 'loop' in title_lower or 'for' in title_lower or 'while' in title_lower:
        return (9, 0, title)

    # Data structures basics
    if 'array' in title_lower and ('basic' in title_lower or 'create' in title_lower or 'access' in title_lower):
        return (10, 0, title)
    if 'array' in title_lower:
        return (11, 0, title)
    if 'list' in title_lower and ('basic' in title_lower or 'create' in title_lower or 'access' in title_lower):
        return (10, 0, title)
    if 'list' in title_lower:
        return (11, 0, title)
    if 'string' in title_lower:
        return (12, 0, title)
    if 'dictionary' in title_lower or 'dict' in title_lower or 'hashmap' in title_lower or 'map' in title_lower:
        return (13, 0, title)
    if 'set' in title_lower or 'hashset' in title_lower:
        return (14, 0, title)

    # Functions/Methods
    if 'function' in title_lower or 'method' in title_lower:
        return (15, 0, title)

    # OOP basics
    if 'class' in title_lower or 'object' in title_lower or 'oop' in title_lower:
        return (16, 0, title)

    # File I/O
    if 'file' in title_lower:
        return (17, 0, title)

    # Error handling
    if 'exception' in title_lower or 'error' in title_lower or 'try' in title_lower:
        return (18, 0, title)

    # Category-based fallback
    category_priority = {
        'Core Java': 19,
        'Core Python': 19,
        'OOP': 20,
        'Algorithms': 21,
        'Data Science': 22,
        'Testing': 23,
    }

    return (category_priority.get(category, 25), 0, title)


def reorganize_curriculum(language):
    """Reorganize curriculum with smart integration of new lessons."""
    print(f"\n{'='*80}")
    print(f"SMART REORGANIZATION: {language.upper()}")
    print(f"{'='*80}")

    # Load original and current lessons
    with open(f'temp_original_{language}.json', 'r', encoding='utf-8') as f:
        original = json.load(f)

    with open(f'public/lessons-{language}.json', 'r', encoding='utf-8') as f:
        current = json.load(f)

    print(f"Original lessons: {len(original)}")
    print(f"Current lessons: {len(current)}")

    # Identify new lessons
    original_titles = {lesson['title'] for lesson in original}
    new_lessons = [l for l in current if l['title'] not in original_titles]

    print(f"New lessons: {len(new_lessons)}")

    # Separate original lessons by difficulty
    original_by_difficulty = defaultdict(list)
    for lesson in original:
        original_by_difficulty[lesson['difficulty']].append(lesson)

    # Separate new lessons by difficulty
    new_by_difficulty = defaultdict(list)
    for lesson in new_lessons:
        new_by_difficulty[lesson['difficulty']].append(lesson)

    print(f"\nOriginal distribution:")
    for diff in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
        print(f"  {diff}: {len(original_by_difficulty[diff])}")

    print(f"\nNew lessons distribution:")
    for diff in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
        count = len(new_by_difficulty[diff])
        if count > 0:
            print(f"  {diff}: {count}")

    # Reorganize beginner section
    print(f"\nReorganizing Beginner section...")
    all_beginner = original_by_difficulty['Beginner'] + new_by_difficulty['Beginner']

    # Find and separate Hello World (must be ID 1)
    hello_world = None
    other_beginners = []

    for lesson in all_beginner:
        if lesson['title'] == 'Hello, World!':
            hello_world = lesson
        else:
            other_beginners.append(lesson)

    # Sort other beginners by topic priority
    other_beginners_sorted = sorted(
        other_beginners,
        key=lambda x: get_topic_priority(x['title'], x['category'])
    )

    # Build beginner list: Hello World first, then sorted lessons
    if hello_world:
        all_beginner_sorted = [hello_world] + other_beginners_sorted
    else:
        all_beginner_sorted = other_beginners_sorted

    print(f"  Total beginner lessons: {len(all_beginner_sorted)}")
    print(f"  First 5:")
    for i, lesson in enumerate(all_beginner_sorted[:5], 1):
        print(f"    {i}. {lesson['title']} ({lesson['category']})")

    # Build final curriculum
    final_curriculum = []
    current_id = 1

    # Add sorted beginner lessons
    for lesson in all_beginner_sorted:
        lesson['id'] = current_id
        final_curriculum.append(lesson)
        current_id += 1

    beginner_end = current_id - 1

    # Add other difficulty levels in original order (with new lessons if any)
    for difficulty in ['Intermediate', 'Advanced', 'Expert']:
        original_lessons = original_by_difficulty[difficulty]
        new_lessons_diff = new_by_difficulty[difficulty]

        # Add original lessons first
        for lesson in original_lessons:
            lesson['id'] = current_id
            final_curriculum.append(lesson)
            current_id += 1

        # Add new lessons for this difficulty
        for lesson in new_lessons_diff:
            lesson['id'] = current_id
            final_curriculum.append(lesson)
            current_id += 1

        if original_lessons or new_lessons_diff:
            print(f"  {difficulty}: IDs {current_id - len(original_lessons) - len(new_lessons_diff)}-{current_id - 1}")

    total_lessons = len(final_curriculum)

    print(f"\n{'='*80}")
    print(f"REORGANIZATION COMPLETE")
    print(f"{'='*80}")
    print(f"Total lessons: {total_lessons}")
    print(f"Beginner: IDs 1-{beginner_end} ({beginner_end} lessons)")
    print(f"ID 1: {final_curriculum[0]['title']}")
    print(f"ID 2: {final_curriculum[1]['title']}")
    print(f"ID 3: {final_curriculum[2]['title']}")

    # Save reorganized curriculum
    with open(f'public/lessons-{language}.json', 'w', encoding='utf-8') as f:
        json.dump(final_curriculum, f, indent=2, ensure_ascii=False)

    return total_lessons, beginner_end


def main():
    """Reorganize both curricula."""
    print("\n" + "="*80)
    print("SMART CURRICULUM REORGANIZATION")
    print("Integrating new beginner lessons into beginner section")
    print("="*80)

    # Reorganize Java
    java_total, java_beginner_end = reorganize_curriculum('java')

    # Reorganize Python
    python_total, python_beginner_end = reorganize_curriculum('python')

    print("\n" + "="*80)
    print("FINAL SUMMARY")
    print("="*80)
    print(f"\nJava:")
    print(f"  Total: {java_total} lessons")
    print(f"  Beginner: 1-{java_beginner_end}")

    print(f"\nPython:")
    print(f"  Total: {python_total} lessons")
    print(f"  Beginner: 1-{python_beginner_end}")

    print(f"\nGrand Total: {java_total + python_total} lessons")
    print("\n" + "="*80)


if __name__ == "__main__":
    main()
