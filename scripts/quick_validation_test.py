#!/usr/bin/env python3
"""
Quick validation test - checks first 10 and last 10 lessons to get a quick sense of issues.
"""
import json
import subprocess
import tempfile
import os
from pathlib import Path
import sys

def normalize_output(text):
    if text is None:
        return ''
    return text.strip().replace('\r\n', '\n')

def run_python_code(code, timeout=10):
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(code)
            temp_file = f.name

        try:
            result = subprocess.run(
                ['python', temp_file],
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8',
                errors='replace'
            )
            if result.returncode != 0:
                return result.stderr, True, 'runtime'
            return result.stdout, False, None
        finally:
            try:
                os.unlink(temp_file)
            except:
                pass
    except subprocess.TimeoutExpired:
        return '', True, 'timeout'
    except Exception as e:
        return str(e), True, 'execution'

def run_java_code(code, timeout=10):
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            java_file = Path(temp_dir) / 'Main.java'
            with open(java_file, 'w', encoding='utf-8') as f:
                f.write(code)

            compile_result = subprocess.run(
                ['javac', str(java_file)],
                capture_output=True,
                text=True,
                cwd=temp_dir,
                timeout=timeout,
                encoding='utf-8',
                errors='replace'
            )

            if compile_result.returncode != 0:
                return compile_result.stderr, True, 'compilation'

            try:
                run_result = subprocess.run(
                    ['java', '-Xmx64m', '-cp', temp_dir, 'Main'],
                    capture_output=True,
                    text=True,
                    cwd=temp_dir,
                    timeout=timeout,
                    encoding='utf-8',
                    errors='replace'
                )

                if run_result.returncode != 0:
                    return run_result.stderr, True, 'runtime'
                return run_result.stdout, False, None
            except subprocess.TimeoutExpired:
                return '', True, 'timeout'
    except Exception as e:
        return str(e), True, 'execution'

def quick_test_language(file_path, language):
    print(f"\n{'='*80}")
    print(f"Quick test: {language.upper()} lessons")
    print(f"{'='*80}\n")

    with open(file_path, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    if isinstance(lessons, dict) and 'lessons' in lessons:
        lessons = lessons['lessons']

    print(f"Total lessons: {len(lessons)}")
    print(f"Testing first 10 and last 10 lessons...\n")

    # Test first 10 and last 10
    test_indices = list(range(min(10, len(lessons)))) + list(range(max(0, len(lessons)-10), len(lessons)))
    test_indices = sorted(set(test_indices))  # Remove duplicates

    failures = []
    errors = []
    passes = 0

    for idx in test_indices:
        lesson = lessons[idx]
        lesson_id = lesson.get('id')
        title = lesson.get('title', 'Unknown')
        full_solution = lesson.get('fullSolution', '')
        expected_output = lesson.get('expectedOutput', '')

        if not full_solution:
            continue

        # Run code
        if language == 'python':
            actual_output, has_error, error_type = run_python_code(full_solution)
        else:
            actual_output, has_error, error_type = run_java_code(full_solution)

        if has_error:
            errors.append({
                'id': lesson_id,
                'title': title,
                'error_type': error_type,
                'message': actual_output[:200]
            })
            print(f"[ERROR] {lesson_id}. {title[:50]}")
            print(f"        {error_type}: {actual_output[:100]}")
        elif normalize_output(actual_output) != normalize_output(expected_output):
            failures.append({
                'id': lesson_id,
                'title': title,
                'expected': expected_output,
                'actual': actual_output
            })
            print(f"[FAIL]  {lesson_id}. {title[:50]}")
            print(f"        Expected: {repr(expected_output[:50])}")
            print(f"        Actual:   {repr(actual_output[:50])}")
        else:
            passes += 1
            print(f"[PASS]  {lesson_id}. {title[:50]}")

    print(f"\n{'='*80}")
    print(f"Quick Test Summary for {language.upper()}:")
    print(f"  Tested: {len(test_indices)} lessons")
    print(f"  Passed: {passes}")
    print(f"  Failed: {len(failures)}")
    print(f"  Errors: {len(errors)}")
    print(f"{'='*80}\n")

    return {
        'total_tested': len(test_indices),
        'passes': passes,
        'failures': failures,
        'errors': errors
    }

def main():
    script_dir = Path(__file__).parent
    public_dir = script_dir.parent / 'public'

    python_file = public_dir / 'lessons-python.json'
    java_file = public_dir / 'lessons-java.json'

    all_failures = []
    all_errors = []

    if python_file.exists():
        result = quick_test_language(python_file, 'python')
        all_failures.extend([(f, 'python') for f in result['failures']])
        all_errors.extend([(e, 'python') for e in result['errors']])

    if java_file.exists():
        result = quick_test_language(java_file, 'java')
        all_failures.extend([(f, 'java') for f in result['failures']])
        all_errors.extend([(e, 'java') for e in result['errors']])

    if all_failures or all_errors:
        print("\n" + "="*80)
        print("ISSUES FOUND - These lessons will fail when students click 'Solve Lesson':")
        print("="*80)

        if all_failures:
            print(f"\nOutput Mismatches ({len(all_failures)}):")
            for failure, lang in all_failures[:20]:
                print(f"  [{lang}] Lesson {failure['id']}: {failure['title'][:50]}")

        if all_errors:
            print(f"\nExecution Errors ({len(all_errors)}):")
            for error, lang in all_errors[:20]:
                print(f"  [{lang}] Lesson {error['id']}: {error['title'][:50]}")
                print(f"          {error['error_type']}: {error['message'][:80]}")

        print("\nRecommendation: Run full validation with: python scripts/validate_all_lessons.py")
        sys.exit(1)
    else:
        print("\n" + "="*80)
        print("Quick test passed! Run full validation for complete check.")
        print("="*80)
        sys.exit(0)

if __name__ == '__main__':
    main()
