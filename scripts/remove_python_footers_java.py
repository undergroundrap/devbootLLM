"""
Remove Python-style comment footers from Java lessons
These were accidentally added during solution expansion
"""
import json

def remove_python_footer(solution):
    """Remove Python-style footer comments from Java code"""
    # Split at the Python footer marker
    if '# This implementation follows best practices:' in solution:
        solution = solution.split('# This implementation follows best practices:')[0].rstrip()
    return solution

def process_java_lessons(lessons_file):
    """Remove Python footers from all Java lessons"""

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    fixed_count = 0

    for lesson in lessons:
        solution = lesson.get('fullSolution', '')

        if '# This implementation follows best practices:' in solution:
            old_len = len(solution)
            cleaned = remove_python_footer(solution)
            lesson['fullSolution'] = cleaned
            new_len = len(cleaned)
            fixed_count += 1

            print(f"[{fixed_count}] Lesson {lesson['id']}: {lesson['title'][:50]}")
            print(f"  Removed footer: {old_len} -> {new_len} chars (-{old_len - new_len})")

    # Save
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    print(f"\n[DONE] Removed Python footers from {fixed_count} Java lessons")
    return fixed_count

if __name__ == '__main__':
    print("=== Removing Python-style footers from Java lessons ===\n")
    count = process_java_lessons('public/lessons-java.json')
    print(f"\nFixed {count} Java lessons")
