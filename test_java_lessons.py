#!/usr/bin/env python3
"""
Comprehensive test suite for Java lessons
Tests all lessons by compiling and running them, comparing output
"""

import json
import tempfile
import subprocess
import sys
import os
from pathlib import Path

def test_java_lesson(lesson):
    """Test a single Java lesson"""
    lesson_id = lesson['id']
    title = lesson['title']
    code = lesson['fullSolution']
    expected_output = lesson['expectedOutput'].strip()

    # Create temporary directory for Java compilation
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract class name from code
        class_name = extract_class_name(code)
        if not class_name:
            return False, "Could not extract class name"

        # Write Java file
        java_file = Path(temp_dir) / f"{class_name}.java"
        java_file.write_text(code, encoding='utf-8')

        # Compile
        compile_result = subprocess.run(
            ['javac', str(java_file)],
            capture_output=True,
            text=True,
            cwd=temp_dir,
            encoding='utf-8'
        )

        if compile_result.returncode != 0:
            return False, f"Compilation error: {compile_result.stderr[:200]}"

        # Run
        run_result = subprocess.run(
            ['java', '-cp', temp_dir, class_name],
            capture_output=True,
            text=True,
            timeout=10,
            encoding='utf-8'
        )

        if run_result.returncode != 0:
            return False, f"Runtime error: {run_result.stderr[:200]}"

        # Compare output
        actual_output = run_result.stdout.strip()
        if actual_output == expected_output:
            return True, "PASSED"
        else:
            return False, f"Output mismatch"

def extract_class_name(code):
    """Extract the public class name from Java code"""
    import re
    match = re.search(r'public\s+class\s+(\w+)', code)
    if match:
        return match.group(1)
    # Try without public
    match = re.search(r'class\s+(\w+)', code)
    if match:
        return match.group(1)
    return None

def main():
    # Load Java lessons
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    print(f"TESTING JAVA LESSONS")
    print(f"Total lessons: {len(lessons)}")
    print("=" * 60)

    passed = 0
    failed = 0
    failed_lessons = []

    for i, lesson in enumerate(lessons, 1):
        lesson_id = lesson['id']
        title = lesson['title']

        try:
            success, message = test_java_lesson(lesson)

            if success:
                passed += 1
                if i % 50 == 0:
                    print(f"Testing Lesson {lesson_id}: {title[:40]}... PASSED")
            else:
                failed += 1
                failed_lessons.append((lesson_id, title, message))
                print(f"Testing Lesson {lesson_id}: {title[:40]}... FAILED")
                print(f"  {message}")
        except Exception as e:
            failed += 1
            failed_lessons.append((lesson_id, title, str(e)[:100]))
            print(f"Testing Lesson {lesson_id}: {title[:40]}... FAILED")
            print(f"  Exception: {str(e)[:100]}")

        # Progress indicator
        if i % 100 == 0:
            print(f"\nProgress: {i}/{len(lessons)} ({passed} passed, {failed} failed)")

    # Summary
    total = passed + failed
    pass_rate = (passed / total * 100) if total > 0 else 0

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total lessons tested: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Pass rate: {pass_rate:.2f}%")
    print("=" * 60)

    if failed_lessons:
        print(f"\nFailed lessons ({len(failed_lessons)}):")
        for lesson_id, title, message in failed_lessons[:20]:
            print(f"  Lesson {lesson_id}: {title[:40]}")
            print(f"    {message[:100]}")
        if len(failed_lessons) > 20:
            print(f"  ... and {len(failed_lessons) - 20} more")

    return 0 if failed == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
