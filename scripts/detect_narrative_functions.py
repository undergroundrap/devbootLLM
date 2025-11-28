#!/usr/bin/env python3
"""
Detect lessons with functions that only print generic narrative.
These lessons have def demonstrate() or similar but teach nothing.
"""

import json

def is_generic_narrative_lesson(lesson):
    """Check if lesson has function that only prints generic narrative"""
    code = lesson.get('fullSolution', '')

    # Must have function definition
    if 'def ' not in code and 'public static void' not in code:
        return False

    # Check for the exact generic template pattern
    template_phrases = [
        'key concepts:',
        'understanding the pattern/concept',
        'when to use it',
        'implementation approach',
        'benefits and trade-offs',
        'this is a teaching example demonstrating the core concepts'
    ]

    # Count how many template phrases are present
    matches = sum(1 for phrase in template_phrases if phrase.lower() in code.lower())

    # If has 4+ of these exact phrases, it's the generic template
    if matches >= 4:
        return True

    return False

def main():
    print("=" * 80)
    print("DETECTING GENERIC NARRATIVE FUNCTION LESSONS")
    print("=" * 80)
    print()

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_data = json.load(f)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    bad_lessons = []

    # Check Python lessons
    for lesson in python_data:
        if is_generic_narrative_lesson(lesson):
            bad_lessons.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'language': 'Python',
                'category': lesson.get('category', 'Unknown'),
                'difficulty': lesson.get('difficulty', 'Unknown')
            })

    # Check Java lessons
    for lesson in java_data:
        if is_generic_narrative_lesson(lesson):
            bad_lessons.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'language': 'Java',
                'category': lesson.get('category', 'Unknown'),
                'difficulty': lesson.get('difficulty', 'Unknown')
            })

    if bad_lessons:
        print(f"Found {len(bad_lessons)} lessons with generic narrative functions")
        print()
        print("These lessons have a demonstrate() function that only prints:")
        print("  'Key Concepts', 'Understanding the pattern', etc.")
        print("  WITHOUT any actual implementation!")
        print()
        print("=" * 80)
        print()

        for lesson in bad_lessons:
            print(f"Lesson {lesson['id']:4d} ({lesson['language']:6s}) - {lesson['category']:20s}")
            print(f"  {lesson['title']}")
            print()
    else:
        print("[SUCCESS] No generic narrative function lessons found!")

    return len(bad_lessons)

if __name__ == '__main__':
    count = main()
    print(f"Total generic narrative lessons: {count}")
