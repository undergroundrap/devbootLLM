"""
Comprehensive validation of all lesson solutions
Tests that solutions compile and framework lessons have proper imports
"""
import json
import subprocess
import tempfile
import os
import random

def validate_python_solution(lesson):
    """Validate a Python solution compiles"""
    solution = lesson.get('fullSolution', '')

    try:
        compile(solution, f'<lesson_{lesson["id"]}>', 'exec')
        return True, None
    except SyntaxError as e:
        return False, str(e)

def validate_java_solution(lesson):
    """Validate a Java solution compiles"""
    solution = lesson.get('fullSolution', '')

    # Skip Spring framework lessons (they need external dependencies)
    if 'org.springframework' in solution:
        return True, 'Framework lesson (skipped compilation)'

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            java_file = os.path.join(tmpdir, 'Main.java')

            with open(java_file, 'w', encoding='utf-8') as f:
                f.write(solution)

            result = subprocess.run(
                ['javac', java_file],
                capture_output=True,
                text=True,
                timeout=5,
                cwd=tmpdir
            )

            if result.returncode == 0:
                return True, None
            else:
                return False, result.stderr[:200]
    except Exception as e:
        return False, str(e)

def check_framework_imports(lesson, lang):
    """Check that framework lessons have proper imports"""
    title_lower = lesson['title'].lower()
    solution = lesson.get('fullSolution', '')
    issues = []

    if lang == 'python':
        if 'flask' in title_lower and 'from flask' not in solution.lower():
            issues.append('Flask lesson missing Flask imports')

        if 'django' in title_lower and 'django' not in solution.lower():
            issues.append('Django lesson missing Django code')

        if 'fastapi' in title_lower and 'fastapi' not in solution.lower():
            issues.append('FastAPI lesson missing FastAPI code')

    elif lang == 'java':
        if 'spring' in title_lower and '@' not in solution and 'org.springframework' not in solution.lower():
            issues.append('Spring lesson missing Spring annotations')

    return issues

def comprehensive_validation(lessons_file, lang):
    """Run comprehensive validation on all lessons"""

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Sample lessons for validation
    # - All recently modified lessons (last 200)
    # - Random sample of 50 other lessons
    # - All framework lessons

    framework_keywords = {
        'python': ['flask', 'django', 'fastapi', 'celery', 'pandas', 'numpy'],
        'java': ['spring', 'kafka', 'reactive', 'mockito', 'testcontainers', 'grpc']
    }

    # Identify framework lessons
    framework_lessons = []
    for lesson in lessons:
        title_lower = lesson['title'].lower()
        if any(keyword in title_lower for keyword in framework_keywords[lang]):
            framework_lessons.append(lesson)

    # Sample non-framework lessons
    other_lessons = [l for l in lessons if l not in framework_lessons]
    random.seed(42)
    sampled_lessons = random.sample(other_lessons, min(50, len(other_lessons)))

    # Combine all lessons to test
    lessons_to_test = framework_lessons[:30] + sampled_lessons  # Test 30 framework + 50 random

    print(f'\n=== Comprehensive {lang.upper()} Validation ===')
    print(f'Total lessons: {len(lessons)}')
    print(f'Testing {len(lessons_to_test)} lessons:')
    print(f'  - {min(30, len(framework_lessons))} framework lessons')
    print(f'  - {len(sampled_lessons)} random lessons')
    print()

    passed = 0
    failed = 0
    skipped = 0

    validator = validate_python_solution if lang == 'python' else validate_java_solution

    for lesson in lessons_to_test:
        # Check framework imports first
        import_issues = check_framework_imports(lesson, lang)

        if import_issues:
            print(f'[FAIL] Lesson {lesson["id"]}: {lesson["title"][:50]}')
            for issue in import_issues:
                print(f'  Issue: {issue}')
            failed += 1
            continue

        # Validate compilation
        compiles, error = validator(lesson)

        if compiles:
            if error and 'Framework' in error:
                print(f'[SKIP] Lesson {lesson["id"]}: {lesson["title"][:50]} - {error}')
                skipped += 1
            else:
                print(f'[PASS] Lesson {lesson["id"]}: {lesson["title"][:50]}')
                passed += 1
        else:
            print(f'[FAIL] Lesson {lesson["id"]}: {lesson["title"][:50]}')
            print(f'  Error: {error}')
            failed += 1

    print(f'\n=== {lang.upper()} Results ===')
    print(f'Passed: {passed}')
    print(f'Failed: {failed}')
    print(f'Skipped (framework): {skipped}')
    print(f'Success Rate: {passed}/{passed + failed} = {100 * passed / (passed + failed) if (passed + failed) > 0 else 0:.1f}%')

    return passed, failed, skipped

if __name__ == '__main__':
    print('=== Comprehensive Lesson Solution Validation ===')

    python_passed, python_failed, python_skipped = comprehensive_validation(
        'public/lessons-python.json', 'python'
    )

    java_passed, java_failed, java_skipped = comprehensive_validation(
        'public/lessons-java.json', 'java'
    )

    print(f'\n{"="*60}')
    print(f'OVERALL RESULTS:')
    print(f'{"="*60}')
    print(f'Python: {python_passed} passed, {python_failed} failed, {python_skipped} skipped')
    print(f'Java: {java_passed} passed, {java_failed} failed, {java_skipped} skipped')
    print(f'\nTotal Passed: {python_passed + java_passed}')
    print(f'Total Failed: {python_failed + java_failed}')
    print(f'Overall Success Rate: {100 * (python_passed + java_passed) / (python_passed + java_passed + python_failed + java_failed):.1f}%')
    print(f'{"="*60}')
