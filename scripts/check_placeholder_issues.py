import json

def check_placeholder_lessons(lessons_file, language):
    """Check if placeholder text is actual TODO or just lesson content"""
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    real_issues = []
    false_alarms = []

    for lesson in lessons:
        lid = lesson.get('id')
        title = lesson.get('title', '')
        solution = lesson.get('fullSolution', '')

        # Check for TODO (actual placeholder)
        has_todo_comment = 'TODO' in solution and ('# TODO' in solution or '// TODO' in solution)

        # Check for placeholder variables/text
        has_placeholder = 'placeholder' in solution.lower()

        # Exclude false alarms
        is_todo_lesson = 'todo' in title.lower() and 'list' in title.lower()
        is_template_lesson = 'template' in title.lower()

        if has_todo_comment and not is_todo_lesson:
            real_issues.append({
                'id': lid,
                'title': title,
                'issue': 'TODO comment',
                'snippet': solution[:200]
            })
        elif has_placeholder and not is_template_lesson:
            real_issues.append({
                'id': lid,
                'title': title,
                'issue': 'placeholder text',
                'snippet': solution[:200]
            })
        elif (has_todo_comment or has_placeholder) and (is_todo_lesson or is_template_lesson):
            false_alarms.append({
                'id': lid,
                'title': title,
                'reason': 'Lesson is about TODO/template - expected'
            })

    return real_issues, false_alarms

# Check both languages
print("="*70)
print("PLACEHOLDER TEXT INVESTIGATION")
print("="*70)

python_real, python_false = check_placeholder_lessons('public/lessons-python.json', 'Python')
java_real, java_false = check_placeholder_lessons('public/lessons-java.json', 'Java')

print(f"\nPYTHON:")
print(f"  Real issues: {len(python_real)}")
print(f"  False alarms: {len(python_false)}")

print(f"\nJAVA:")
print(f"  Real issues: {len(java_real)}")
print(f"  False alarms: {len(java_false)}")

total_real = len(python_real) + len(java_real)
total_false = len(python_false) + len(java_false)

print("\n" + "="*70)
if total_real == 0:
    print("RESULT: No real placeholder issues found!")
    print(f"All {total_false} 'placeholder' detections are false alarms")
else:
    print(f"FOUND {total_real} REAL ISSUES:")
    print("="*70)
    for issue in python_real + java_real:
        print(f"\nLesson {issue['id']}: {issue['title']}")
        print(f"  Issue: {issue['issue']}")
        print(f"  Snippet: {issue['snippet'][:150]}...")

if python_false or java_false:
    print("\n" + "="*70)
    print("FALSE ALARMS (expected behavior):")
    print("="*70)
    for fa in python_false + java_false:
        print(f"  Lesson {fa['id']}: {fa['title']} - {fa['reason']}")
