#!/usr/bin/env python3
"""
Restore original lesson order while keeping new lessons at the end.
"""

import json

def restore_curriculum(language):
    """Restore original order with new lessons appended."""
    print(f"\nProcessing {language.upper()}...")

    # Get original lessons from temp file
    with open(f'temp_original_{language}.json', 'r', encoding='utf-8') as f:
        original = json.load(f)

    # Get current lessons
    with open(f'public/lessons-{language}.json', 'r', encoding='utf-8') as f:
        current = json.load(f)

    print(f"  Original lessons: {len(original)}")
    print(f"  Current lessons: {len(current)}")

    # Find new lessons (by title)
    original_titles = {lesson['title'] for lesson in original}
    new_lessons = []

    for lesson in current:
        if lesson['title'] not in original_titles:
            new_lessons.append(lesson)

    print(f"  New lessons found: {len(new_lessons)}")

    # Create combined list: original + new
    combined = original.copy()

    # Renumber new lessons to append at the end
    next_id = len(original) + 1
    for lesson in new_lessons:
        lesson['id'] = next_id
        combined.append(lesson)
        if next_id <= len(original) + 5:
            print(f"    Added: ID {next_id} - {lesson['title']}")
        next_id += 1

    if len(new_lessons) > 5:
        print(f"    ... and {len(new_lessons) - 5} more")

    print(f"  Total lessons: {len(combined)}")
    print(f"  ID range: 1-{len(combined)}")

    # Save
    with open(f'public/lessons-{language}.json', 'w', encoding='utf-8') as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)

    return len(original), len(new_lessons), len(combined)

def main():
    """Restore both curricula."""
    print("="*80)
    print("RESTORING ORIGINAL LESSON ORDER")
    print("="*80)

    # Restore Java
    java_orig, java_new, java_total = restore_curriculum('java')

    # Restore Python
    python_orig, python_new, python_total = restore_curriculum('python')

    print("\n" + "="*80)
    print("RESTORATION COMPLETE!")
    print("="*80)
    print(f"\nJava:")
    print(f"  Original lessons (IDs 1-{java_orig}): {java_orig}")
    print(f"  New lessons (IDs {java_orig+1}-{java_total}): {java_new}")
    print(f"  Total: {java_total}")

    print(f"\nPython:")
    print(f"  Original lessons (IDs 1-{python_orig}): {python_orig}")
    print(f"  New lessons (IDs {python_orig+1}-{python_total}): {python_new}")
    print(f"  Total: {python_total}")

    print(f"\nGrand Total: {java_total + python_total} lessons")
    print("\n" + "="*80)
    print("Verifying...")
    print("="*80)

    # Verify
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_verify = json.load(f)
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_verify = json.load(f)

    print(f"Java: ID 1 = '{java_verify[0]['title']}'")
    print(f"Python: ID 1 = '{python_verify[0]['title']}'")
    print("="*80)

if __name__ == "__main__":
    main()
