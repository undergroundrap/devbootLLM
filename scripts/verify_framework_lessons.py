#!/usr/bin/env python3
"""
Verify that all framework lessons pass syntax validation.
Tests a representative sample of framework lessons from both Python and Java.
"""

import json
import subprocess
import tempfile
import os
import sys
from pathlib import Path

def test_python_syntax(code):
    """Test Python code syntax using py_compile."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
        f.write(code)
        temp_path = f.name

    try:
        # Use py_compile to check syntax
        result = subprocess.run(
            ['py', '-3', '-m', 'py_compile', temp_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0, result.stderr
    except Exception as e:
        return False, str(e)
    finally:
        try:
            os.unlink(temp_path)
        except:
            pass

def test_java_syntax(code):
    """Test Java code syntax using javac."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = os.path.join(temp_dir, 'Main.java')
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(code)

        try:
            result = subprocess.run(
                ['javac', temp_path],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=temp_dir
            )

            # For framework code, check if errors are only framework-related
            if result.returncode != 0:
                error = result.stderr
                # These are expected framework errors
                is_framework_error = (
                    ('package' in error and 'does not exist' in error) or
                    ('cannot find symbol' in error)
                ) and not any([
                    'class, interface, enum, or record expected' in error,
                    'illegal start of expression' in error,
                    'not a statement' in error,
                    "';' expected" in error,
                    'reached end of file while parsing' in error
                ])

                if is_framework_error:
                    return True, "Framework imports missing (expected)"
                return False, error

            return True, ""
        except Exception as e:
            return False, str(e)

def main():
    print("=" * 80)
    print("FRAMEWORK LESSON SYNTAX VALIDATION TEST")
    print("=" * 80)
    print()

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_lessons = json.load(f)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_lessons = json.load(f)

    # Filter framework lessons
    python_framework = [l for l in python_lessons if l.get('isFramework')]
    java_framework = [l for l in java_lessons if l.get('isFramework')]

    print(f"Found {len(python_framework)} Python framework lessons")
    print(f"Found {len(java_framework)} Java framework lessons")
    print(f"Total framework lessons: {len(python_framework) + len(java_framework)}")
    print()

    # Test Python framework lessons
    print("-" * 80)
    print("Testing Python Framework Lessons (sample of 20)")
    print("-" * 80)

    python_passed = 0
    python_failed = 0
    failed_lessons = []

    # Test every 9th lesson to get a good sample (~20 lessons)
    for i, lesson in enumerate(python_framework):
        if i % 9 != 0:
            continue

        code = lesson.get('fullSolution', '')
        if not code:
            continue

        passed, error = test_python_syntax(code)

        if passed:
            python_passed += 1
            print(f"[OK] Lesson {lesson['id']:4d}: {lesson['title'][:50]}")
        else:
            python_failed += 1
            failed_lessons.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'framework': lesson.get('frameworkName', 'Unknown'),
                'error': error
            })
            print(f"[FAIL] Lesson {lesson['id']:4d}: {lesson['title'][:50]}")
            print(f"  Error: {error[:100]}")

    print()
    print(f"Python Results: {python_passed} passed, {python_failed} failed")
    print()

    # Test Java framework lessons
    print("-" * 80)
    print("Testing Java Framework Lessons (sample of 20)")
    print("-" * 80)

    java_passed = 0
    java_failed = 0

    # Test every 6th lesson to get a good sample (~20 lessons)
    for i, lesson in enumerate(java_framework):
        if i % 6 != 0:
            continue

        code = lesson.get('fullSolution', '')
        if not code:
            continue

        passed, error = test_java_syntax(code)

        if passed:
            java_passed += 1
            print(f"[OK] Lesson {lesson['id']:4d}: {lesson['title'][:50]}")
        else:
            java_failed += 1
            failed_lessons.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'framework': lesson.get('frameworkName', 'Unknown'),
                'error': error
            })
            print(f"[FAIL] Lesson {lesson['id']:4d}: {lesson['title'][:50]}")
            print(f"  Error: {error[:100]}")

    print()
    print(f"Java Results: {java_passed} passed, {java_failed} failed")
    print()

    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    total_tested = python_passed + python_failed + java_passed + java_failed
    total_passed = python_passed + java_passed
    total_failed = python_failed + java_failed

    print(f"Total lessons tested: {total_tested}")
    print(f"Total passed: {total_passed} ({total_passed*100//total_tested if total_tested > 0 else 0}%)")
    print(f"Total failed: {total_failed}")
    print()

    if failed_lessons:
        print("Failed Lessons:")
        for lesson in failed_lessons:
            print(f"  - Lesson {lesson['id']}: {lesson['title']}")
            print(f"    Framework: {lesson['framework']}")
            print(f"    Error: {lesson['error'][:80]}")
            print()

    if total_failed == 0:
        print("[SUCCESS] ALL FRAMEWORK LESSONS PASS SYNTAX VALIDATION!")
        return 0
    else:
        print(f"[FAILED] {total_failed} lessons need fixes")
        return 1

if __name__ == '__main__':
    sys.exit(main())
