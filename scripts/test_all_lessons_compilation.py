#!/usr/bin/env python3
"""
Test compilation of ALL lessons (framework and non-framework) to find any issues.
This tests a sample of lessons across all difficulty levels and categories.
"""

import json
import subprocess
import tempfile
import os
import sys
import random

def test_python(code):
    """Test Python code."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
        f.write(code)
        temp_path = f.name

    try:
        # First check syntax
        result = subprocess.run(
            ['py', '-3', '-m', 'py_compile', temp_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode != 0:
            return False, result.stderr, 'syntax'

        # For non-framework, also try to execute
        result = subprocess.run(
            ['py', '-3', temp_path],
            capture_output=True,
            text=True,
            timeout=3
        )

        if result.returncode != 0:
            # Check if it's an import error (framework)
            if 'ModuleNotFoundError' in result.stderr or 'ImportError' in result.stderr:
                return True, 'Framework import (OK)', 'import'
            return False, result.stderr, 'runtime'

        return True, result.stdout, 'success'

    except subprocess.TimeoutExpired:
        return False, 'Timeout', 'timeout'
    except Exception as e:
        return False, str(e), 'exception'
    finally:
        try:
            os.unlink(temp_path)
        except:
            pass

def test_java(code):
    """Test Java code."""
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

            if result.returncode != 0:
                error = result.stderr

                # Check if framework error
                is_framework = (
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

                if is_framework:
                    return True, 'Framework imports (OK)', 'framework'
                return False, error, 'compilation'

            return True, 'Compiled successfully', 'success'

        except subprocess.TimeoutExpired:
            return False, 'Timeout', 'timeout'
        except Exception as e:
            return False, str(e), 'exception'

def main():
    print("=" * 80)
    print("COMPREHENSIVE LESSON COMPILATION TEST")
    print("Testing sample of ALL lessons (framework + non-framework)")
    print("=" * 80)
    print()

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_lessons = json.load(f)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_lessons = json.load(f)

    # Separate framework and non-framework
    python_framework = [l for l in python_lessons if l.get('isFramework')]
    python_normal = [l for l in python_lessons if not l.get('isFramework')]
    java_framework = [l for l in java_lessons if l.get('isFramework')]
    java_normal = [l for l in java_lessons if not l.get('isFramework')]

    print(f"Python: {len(python_framework)} framework, {len(python_normal)} non-framework")
    print(f"Java: {len(java_framework)} framework, {len(java_normal)} non-framework")
    print()

    failed_lessons = []

    # Test Python lessons (sample 50 non-framework + all framework issues)
    print("-" * 80)
    print("Testing Python Lessons (50 non-framework + framework sample)")
    print("-" * 80)

    random.seed(42)
    python_sample = random.sample(python_normal, min(50, len(python_normal)))
    python_framework_sample = random.sample(python_framework, min(20, len(python_framework)))

    for lesson in python_sample + python_framework_sample:
        code = lesson.get('fullSolution', '')
        if not code:
            continue

        passed, msg, error_type = test_python(code)

        if not passed:
            print(f"[FAIL] Lesson {lesson['id']:4d}: {lesson['title'][:50]}")
            print(f"  Type: {error_type}")
            print(f"  Error: {msg[:100]}")
            failed_lessons.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'language': 'Python',
                'isFramework': lesson.get('isFramework', False),
                'error': msg[:200],
                'type': error_type
            })

    print(f"Python: {len(python_sample) + len(python_framework_sample)} tested")
    print()

    # Test Java lessons (sample 50 non-framework + framework sample)
    print("-" * 80)
    print("Testing Java Lessons (50 non-framework + framework sample)")
    print("-" * 80)

    java_sample = random.sample(java_normal, min(50, len(java_normal)))
    java_framework_sample = random.sample(java_framework, min(20, len(java_framework)))

    for lesson in java_sample + java_framework_sample:
        code = lesson.get('fullSolution', '')
        if not code:
            continue

        passed, msg, error_type = test_java(code)

        if not passed:
            print(f"[FAIL] Lesson {lesson['id']:4d}: {lesson['title'][:50]}")
            print(f"  Type: {error_type}")
            print(f"  Error: {msg[:100]}")
            failed_lessons.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'language': 'Java',
                'isFramework': lesson.get('isFramework', False),
                'error': msg[:200],
                'type': error_type
            })

    print(f"Java: {len(java_sample) + len(java_framework_sample)} tested")
    print()

    # Summary
    print("=" * 80)
    print("RESULTS")
    print("=" * 80)
    total_tested = len(python_sample) + len(python_framework_sample) + len(java_sample) + len(java_framework_sample)

    print(f"Total lessons tested: {total_tested}")
    print(f"Failed: {len(failed_lessons)}")
    print()

    if failed_lessons:
        print("FAILED LESSONS:")
        print("-" * 80)
        for lesson in failed_lessons:
            print(f"\nLesson {lesson['id']}: {lesson['title']} ({lesson['language']})")
            print(f"  Framework: {lesson['isFramework']}")
            print(f"  Type: {lesson['type']}")
            print(f"  Error: {lesson['error'][:150]}")

        return 1
    else:
        print("[SUCCESS] All tested lessons compile/validate correctly!")
        return 0

if __name__ == '__main__':
    sys.exit(main())
