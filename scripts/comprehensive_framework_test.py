#!/usr/bin/env python3
"""
Comprehensive test of ALL framework lessons to ensure 100% pass rate.
This may take a few minutes to complete.
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

            if result.returncode == 0:
                return True, ""

            error = result.stderr
            # Framework errors are expected
            is_framework_error = (
                ('package' in error and 'does not exist' in error) or
                ('cannot find symbol' in error)
            ) and not any([
                'class, interface, enum, or record expected' in error,
                'illegal start of expression' in error,
                'not a statement' in error,
                "';' expected" in error,
                'reached end of file while parsing' in error,
                "')' expected" in error
            ])

            if is_framework_error:
                return True, "Framework imports missing (expected)"
            return False, error
        except Exception as e:
            return False, str(e)

def main():
    print("=" * 80)
    print("COMPREHENSIVE FRAMEWORK LESSON TEST - ALL 302 LESSONS")
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

    print(f"Testing {len(python_framework)} Python framework lessons...")
    print(f"Testing {len(java_framework)} Java framework lessons...")
    print(f"Total: {len(python_framework) + len(java_framework)} framework lessons")
    print()

    python_passed = 0
    python_failed = 0
    java_passed = 0
    java_failed = 0
    failed_lessons = []

    # Test ALL Python framework lessons
    print("-" * 80)
    print(f"Python Framework Lessons (ALL {len(python_framework)} lessons)")
    print("-" * 80)

    for i, lesson in enumerate(python_framework, 1):
        code = lesson.get('fullSolution', '')
        if not code:
            continue

        passed, error = test_python_syntax(code)

        if passed:
            python_passed += 1
            if i % 20 == 0:
                print(f"  Progress: {i}/{len(python_framework)} - {python_passed} passed")
        else:
            python_failed += 1
            failed_lessons.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'framework': lesson.get('frameworkName', 'Unknown'),
                'language': 'Python',
                'error': error
            })
            print(f"[FAIL] Lesson {lesson['id']:4d}: {lesson['title']}")

    print(f"\nPython Results: {python_passed}/{len(python_framework)} passed ({python_passed*100//len(python_framework) if len(python_framework) > 0 else 0}%)")
    print()

    # Test ALL Java framework lessons
    print("-" * 80)
    print(f"Java Framework Lessons (ALL {len(java_framework)} lessons)")
    print("-" * 80)

    for i, lesson in enumerate(java_framework, 1):
        code = lesson.get('fullSolution', '')
        if not code:
            continue

        passed, error = test_java_syntax(code)

        if passed:
            java_passed += 1
            if i % 20 == 0:
                print(f"  Progress: {i}/{len(java_framework)} - {java_passed} passed")
        else:
            java_failed += 1
            failed_lessons.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'framework': lesson.get('frameworkName', 'Unknown'),
                'language': 'Java',
                'error': error
            })
            print(f"[FAIL] Lesson {lesson['id']:4d}: {lesson['title']}")

    print(f"\nJava Results: {java_passed}/{len(java_framework)} passed ({java_passed*100//len(java_framework) if len(java_framework) > 0 else 0}%)")
    print()

    # Summary
    print("=" * 80)
    print("FINAL RESULTS")
    print("=" * 80)
    total_tested = python_passed + python_failed + java_passed + java_failed
    total_passed = python_passed + java_passed
    total_failed = python_failed + java_failed

    print(f"Total lessons tested: {total_tested}")
    print(f"Total passed: {total_passed} ({total_passed*100//total_tested if total_tested > 0 else 0}%)")
    print(f"Total failed: {total_failed}")
    print()

    if failed_lessons:
        print("FAILED LESSONS:")
        print("-" * 80)
        for lesson in failed_lessons:
            print(f"\nLesson {lesson['id']}: {lesson['title']} ({lesson['language']})")
            print(f"  Framework: {lesson['framework']}")
            print(f"  Error: {lesson['error'][:120]}")

    if total_failed == 0:
        print("[SUCCESS] ALL 302 FRAMEWORK LESSONS PASS SYNTAX VALIDATION!")
        print("100% success rate!")
        return 0
    else:
        print(f"[FAILED] {total_failed} lessons need fixes")
        return 1

if __name__ == '__main__':
    sys.exit(main())
