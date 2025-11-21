#!/usr/bin/env python3
"""Quick compilation test for all lessons."""

import json
import subprocess
import tempfile
import os


def test_python_compilation(solution):
    """Test if Python code compiles."""
    try:
        compile(solution, '<string>', 'exec')
        return True, "OK"
    except SyntaxError as e:
        return False, f"Syntax error: {e.msg}"


def test_java_compilation(solution):
    """Test if Java code compiles."""
    with tempfile.TemporaryDirectory() as tmpdir:
        java_file = os.path.join(tmpdir, 'Main.java')

        with open(java_file, 'w', encoding='utf-8') as f:
            f.write(solution)

        try:
            result = subprocess.run(
                ['javac', java_file],
                capture_output=True,
                text=True,
                timeout=10,
                encoding='utf-8',
                errors='ignore'
            )

            if result.returncode != 0:
                # Extract first error
                if 'error:' in result.stderr:
                    error = result.stderr.split('error:')[1].split('\\n')[0].strip()
                    return False, error[:100]
                return False, "Compilation failed"

            return True, "OK"
        except subprocess.TimeoutExpired:
            return False, "Timeout"
        except Exception as e:
            return False, str(e)[:100]


def main():
    print("\\n" + "="*80)
    print("COMPREHENSIVE COMPILATION TEST")
    print("="*80)

    # Test Java
    print("\\nTesting Java lessons...")
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_lessons = json.load(f)

    java_errors = []
    for i, lesson in enumerate(java_lessons, 1):
        if i % 100 == 0:
            print(f"  Tested {i}/{len(java_lessons)}...", end='\\r')

        success, msg = test_java_compilation(lesson['fullSolution'])
        if not success:
            java_errors.append((lesson['id'], lesson['title'], msg))

    print(f"  Tested {len(java_lessons)}/{len(java_lessons)} lessons.    ")

    # Test Python
    print("\\nTesting Python lessons...")
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_lessons = json.load(f)

    python_errors = []
    for i, lesson in enumerate(python_lessons, 1):
        if i % 100 == 0:
            print(f"  Tested {i}/{len(python_lessons)}...", end='\\r')

        success, msg = test_python_compilation(lesson['fullSolution'])
        if not success:
            python_errors.append((lesson['id'], lesson['title'], msg))

    print(f"  Tested {len(python_lessons)}/{len(python_lessons)} lessons.    ")

    # Results
    print("\\n" + "="*80)
    print("COMPILATION RESULTS")
    print("="*80)

    print(f"\\nJava:")
    print(f"  Total: {len(java_lessons)}")
    print(f"  Compiled: {len(java_lessons) - len(java_errors)}")
    print(f"  Errors: {len(java_errors)}")

    print(f"\\nPython:")
    print(f"  Total: {len(python_lessons)}")
    print(f"  Compiled: {len(python_lessons) - len(python_errors)}")
    print(f"  Errors: {len(python_errors)}")

    total = len(java_lessons) + len(python_lessons)
    total_errors = len(java_errors) + len(python_errors)
    total_compiled = total - total_errors

    print(f"\\nOVERALL:")
    print(f"  Total lessons: {total}")
    print(f"  Successfully compiled: {total_compiled} ({total_compiled/total*100:.1f}%)")
    print(f"  Compilation errors: {total_errors}")

    if java_errors:
        print(f"\\n{'='*80}")
        print(f"JAVA COMPILATION ERRORS ({len(java_errors)})")
        print(f"{'='*80}")
        for lid, title, error in java_errors[:10]:
            print(f"\\nLesson {lid}: {title}")
            print(f"  Error: {error}")
        if len(java_errors) > 10:
            print(f"\\n... and {len(java_errors) - 10} more")

    if python_errors:
        print(f"\\n{'='*80}")
        print(f"PYTHON COMPILATION ERRORS ({len(python_errors)})")
        print(f"{'='*80}")
        for lid, title, error in python_errors[:10]:
            print(f"\\nLesson {lid}: {title}")
            print(f"  Error: {error}")
        if len(python_errors) > 10:
            print(f"\\n... and {len(python_errors) - 10} more")

    print("\\n" + "="*80)

    if total_errors == 0:
        print("SUCCESS! All 2,107 lessons compile correctly!")
    else:
        print(f"FOUND {total_errors} lessons with compilation errors")

    print("="*80 + "\\n")

    return total_errors


if __name__ == "__main__":
    errors = main()
