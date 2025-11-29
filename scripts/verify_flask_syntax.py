"""
Verify Python syntax for all upgraded Flask lessons
"""
import json
import ast
import sys

# Read lessons file
with open(r'c:\devbootLLM-app\public\lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Flask lesson IDs from the upgrade
flask_ids = [223, 311, 312, 313, 314, 513, 514, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751]

print("Verifying Python syntax for Flask lessons...")
print("="*80)

valid = []
invalid = []

for lesson_id in flask_ids:
    lesson = next((l for l in lessons if l['id'] == lesson_id), None)
    if not lesson:
        invalid.append({'id': lesson_id, 'title': 'NOT FOUND', 'error': 'Lesson not found'})
        continue

    code = lesson.get('fullSolution', '')
    if not code:
        invalid.append({'id': lesson_id, 'title': lesson['title'], 'error': 'No code'})
        continue

    try:
        ast.parse(code)
        valid.append({'id': lesson_id, 'title': lesson['title'], 'length': len(code)})
        print(f"[OK] {lesson_id}: {lesson['title']} ({len(code)} chars)")
    except SyntaxError as e:
        invalid.append({'id': lesson_id, 'title': lesson['title'], 'error': str(e)})
        print(f"[ERROR] {lesson_id}: {lesson['title']}")
        print(f"  Syntax Error: {e}")

print("\n" + "="*80)
print("SYNTAX VERIFICATION REPORT")
print("="*80)
print(f"\nTotal lessons checked: {len(flask_ids)}")
print(f"Valid Python syntax: {len(valid)}")
print(f"Syntax errors: {len(invalid)}")

if invalid:
    print("\nLessons with errors:")
    for item in invalid:
        print(f"  {item['id']}: {item['title']}")
        print(f"    Error: {item['error']}")

if valid:
    print("\nValid lessons:")
    for item in valid:
        in_range = "[OK]" if 1000 <= item['length'] <= 3500 else "[WARN]"
        print(f"  {in_range} {item['id']}: {item['title']} ({item['length']} chars)")

    # Character statistics
    lengths = [item['length'] for item in valid]
    print(f"\nCharacter counts:")
    print(f"  Min: {min(lengths)}")
    print(f"  Max: {max(lengths)}")
    print(f"  Avg: {sum(lengths) / len(lengths):.0f}")
    print(f"  Target range (1000-3500): {len([l for l in lengths if 1000 <= l <= 3500])}/{len(lengths)}")

sys.exit(0 if len(invalid) == 0 else 1)
