"""
Verify Python syntax for all upgraded Redis lessons
"""
import json
import ast
import sys

def verify_syntax(code, lesson_id, title):
    """Verify Python syntax using AST"""
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, f"Line {e.lineno}: {e.msg}"

def main():
    print("Verifying Python syntax for Redis lessons...")

    # Read lessons
    with open(r'c:\devbootLLM-app\public\lessons-python.json', encoding='utf-8') as f:
        lessons = json.load(f)

    # Redis lesson IDs
    redis_ids = [822, 850, 851, 852, 853, 854, 855, 856, 857, 858, 881, 1004, 1005, 1006]

    all_valid = True
    errors = []

    for lesson_id in redis_ids:
        lesson = next((l for l in lessons if l['id'] == lesson_id), None)
        if not lesson:
            print(f"ERROR: Lesson {lesson_id} not found")
            all_valid = False
            continue

        title = lesson['title']
        code = lesson.get('fullSolution', '')

        is_valid, error = verify_syntax(code, lesson_id, title)

        if is_valid:
            print(f"[OK] {lesson_id}: {title}")
            print(f"     Length: {len(code)} chars")
        else:
            print(f"[FAIL] {lesson_id}: {title}")
            print(f"       Error: {error}")
            all_valid = False
            errors.append({
                'id': lesson_id,
                'title': title,
                'error': error
            })

    print("\n" + "="*60)
    if all_valid:
        print("SUCCESS: All lessons have valid Python syntax!")
    else:
        print(f"ERRORS: {len(errors)} lessons have syntax errors:")
        for err in errors:
            print(f"  - {err['id']}: {err['title']}")
            print(f"    {err['error']}")

    return 0 if all_valid else 1

if __name__ == '__main__':
    sys.exit(main())
