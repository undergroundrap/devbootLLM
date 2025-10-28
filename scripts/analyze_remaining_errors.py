import json

def check_for_java_syntax(code):
    """Check if code contains Java syntax"""
    java_indicators = [
        'Map<', 'List<', 'Set<', 'HashMap<', 'ArrayList<',
        'private ', 'public ', 'class {', 'String ', 'Integer '
    ]
    return any(indicator in code for indicator in java_indicators)

print("Analyzing remaining syntax errors...")
print("=" * 80)

# Load Python lessons
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    python_data = json.load(f)

# Error IDs from syntax check
error_ids = [643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663]

print(f"Checking {len(error_ids)} Python lessons with errors...\n")

java_syntax_count = 0
for lesson_id in error_ids:
    lesson = next((l for l in python_data['lessons'] if l['id'] == lesson_id), None)
    if lesson:
        code = lesson.get('fullSolution', '')
        has_java = check_for_java_syntax(code)
        if has_java:
            print(f"Lesson {lesson_id}: {lesson['title'][:50]} - HAS JAVA SYNTAX")
            java_syntax_count += 1
        else:
            print(f"Lesson {lesson_id}: {lesson['title'][:50]} - Python but has syntax error")

print(f"\n{java_syntax_count} lessons have Java syntax and need conversion")
print(f"{len(error_ids) - java_syntax_count} lessons have Python but with errors")
