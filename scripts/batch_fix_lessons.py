#!/usr/bin/env python3
"""
Batch fix lessons based on common patterns.
Handles multiple issue types automatically.
"""
import json
import subprocess
import tempfile
import re
from pathlib import Path

def run_code(code, language, timeout=10):
    """Execute code and return output"""
    try:
        if language == 'python':
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                f.write(code)
                temp_file = f.name

            result = subprocess.run(
                ['python', temp_file],
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8',
                errors='replace'
            )

            import os
            os.unlink(temp_file)

            if result.returncode != 0:
                return None, f"Runtime: {result.stderr[:200]}"
            return result.stdout, None

        elif language == 'java':
            with tempfile.TemporaryDirectory() as temp_dir:
                java_file = Path(temp_dir) / 'Main.java'
                with open(java_file, 'w', encoding='utf-8') as f:
                    f.write(code)

                # Compile
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
                    return None, f"Compile: {compile_result.stderr[:200]}"

                # Run
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
                    return None, f"Runtime: {run_result.stderr[:200]}"
                return run_result.stdout, None
    except subprocess.TimeoutExpired:
        return None, "Timeout"
    except Exception as e:
        return None, str(e)

def detect_issue_type(lesson, language):
    """Detect what type of issue this lesson has"""
    expected = lesson.get('expectedOutput', '')
    solution = lesson.get('fullSolution', '')

    # Generic expected output
    if expected in ['(Output will vary based on implementation)',
                    '(Output will vary)',
                    'See tutorial for implementation details']:
        return 'generic_output'

    # Placeholder expected output
    if 'TODO' in expected or 'FIXME' in expected or '===' in expected and 'See tutorial' in expected:
        return 'placeholder_output'

    # Non-deterministic (Python ML)
    if language == 'python' and ('sklearn' in solution or 'random' in solution.lower()):
        if 'np.random.seed' not in solution and 'random.seed' not in solution:
            return 'non_deterministic'

    # Whitespace issues
    if expected.endswith('\n\n') or expected.startswith('\n') or '  \n' in expected:
        return 'whitespace'

    return 'unknown'

def fix_generic_output(lesson, language):
    """Fix lessons with generic expected output"""
    solution = lesson['fullSolution']

    # Run the solution
    output, error = run_code(solution, language)

    if error:
        return None, f"Cannot fix - {error}"

    # Update expectedOutput
    lesson['expectedOutput'] = output
    return lesson, "Updated to actual output"

def fix_placeholder_output(lesson, language):
    """Fix lessons with placeholder expected output"""
    return fix_generic_output(lesson, language)

def fix_non_deterministic(lesson, language):
    """Fix non-deterministic Python code"""
    if language != 'python':
        return None, "Not a Python lesson"

    solution = lesson['fullSolution']

    # Add random seed
    if 'import numpy' in solution or 'from numpy' in solution:
        if 'np.random.seed' not in solution:
            # Add seed after numpy import
            lines = solution.split('\n')
            new_lines = []
            added = False
            for line in lines:
                new_lines.append(line)
                if not added and ('import numpy' in line or 'from numpy' in line):
                    new_lines.append('np.random.seed(42)')
                    added = True
            solution = '\n'.join(new_lines)

    # Add random_state to sklearn models
    solution = re.sub(r'(\w+Classifier\()', r'\1random_state=42, ', solution)
    solution = re.sub(r'(\w+Regressor\()', r'\1random_state=42, ', solution)
    solution = re.sub(r'(KMeans\()', r'\1random_state=42, ', solution)
    solution = re.sub(r'(train_test_split\()', r'\1random_state=42, ', solution)
    solution = re.sub(r'(PCA\()', r'\1random_state=42, ', solution)

    # Clean up double random_state
    solution = solution.replace('random_state=42, random_state=42', 'random_state=42')

    lesson['fullSolution'] = solution

    # Get new output
    output, error = run_code(solution, language)

    if error:
        return None, f"After seed fix - {error}"

    lesson['expectedOutput'] = output
    return lesson, "Added random seeds"

def fix_whitespace(lesson, language):
    """Fix whitespace issues in expected output"""
    expected = lesson['expectedOutput']

    # Clean trailing newlines (keep one)
    while expected.endswith('\n\n'):
        expected = expected[:-1]

    # Clean leading newlines
    expected = expected.lstrip('\n')

    # Clean trailing spaces on lines
    lines = expected.split('\n')
    lines = [line.rstrip() for line in lines]
    expected = '\n'.join(lines)

    lesson['expectedOutput'] = expected
    return lesson, "Cleaned whitespace"

def batch_fix_lessons(language, lesson_ids=None, issue_type=None):
    """Fix multiple lessons at once"""

    lessons_file = Path(f'public/lessons-{language}.json')

    print(f"Loading {language} lessons...")
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    if not isinstance(lessons, list):
        print("[ERROR] Expected array of lessons")
        return

    print(f"Total {language} lessons: {len(lessons)}")

    # Filter lessons
    if lesson_ids:
        lessons_to_fix = [l for l in lessons if l['id'] in lesson_ids]
        print(f"Fixing specific lessons: {lesson_ids}")
    else:
        lessons_to_fix = lessons
        print(f"Scanning all lessons for {issue_type} issues...")

    fixed = []
    errors = []

    for lesson in lessons_to_fix:
        lesson_id = lesson['id']
        title = lesson.get('title', 'Unknown')

        # Detect issue if not specified
        detected_issue = detect_issue_type(lesson, language) if not issue_type else issue_type

        if issue_type and detected_issue != issue_type and not lesson_ids:
            continue  # Skip if doesn't match issue type

        print(f"[{lesson_id}] {title[:50]} - {detected_issue}")

        # Apply appropriate fix
        if detected_issue == 'generic_output':
            result, msg = fix_generic_output(lesson, language)
        elif detected_issue == 'placeholder_output':
            result, msg = fix_placeholder_output(lesson, language)
        elif detected_issue == 'non_deterministic':
            result, msg = fix_non_deterministic(lesson, language)
        elif detected_issue == 'whitespace':
            result, msg = fix_whitespace(lesson, language)
        else:
            errors.append((lesson_id, title, "Unknown issue type"))
            continue

        if result:
            fixed.append((lesson_id, title, msg))
            print(f"  [OK] {msg}")
            # Update in main list
            idx = next(i for i, l in enumerate(lessons) if l['id'] == lesson_id)
            lessons[idx] = result
        else:
            errors.append((lesson_id, title, msg))
            print(f"  [ERROR] {msg}")

    if not fixed:
        print("\n[WARNING] No lessons were fixed!")
        if errors:
            print(f"[ERROR] {len(errors)} lessons had errors")
        return

    print(f"\n[SUCCESS] Fixed {len(fixed)} lessons")

    # Save
    print("Saving...")
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Saved {lessons_file}")

    # Summary
    print("\n" + "="*80)
    print("FIXED LESSONS:")
    for lesson_id, title, msg in fixed:
        print(f"  {lesson_id:4d}. {title[:50]} - {msg}")

    if errors:
        print("\nERRORS:")
        for lesson_id, title, msg in errors:
            print(f"  {lesson_id:4d}. {title[:50]} - {msg}")

    print("="*80)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python batch_fix_lessons.py <language> [issue_type]")
        print("  python batch_fix_lessons.py python generic_output")
        print("  python batch_fix_lessons.py java placeholder_output")
        print("")
        print("Issue types:")
        print("  - generic_output: '(Output will vary...)'")
        print("  - placeholder_output: Placeholder text")
        print("  - non_deterministic: Random/ML code")
        print("  - whitespace: Extra newlines/spaces")
        sys.exit(1)

    language = sys.argv[1]
    issue_type = sys.argv[2] if len(sys.argv) > 2 else None

    batch_fix_lessons(language, issue_type=issue_type)
