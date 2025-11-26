"""
Add expectedOutput to lessons by running their solutions
Critical for solve lesson validation feature
"""
import json
import subprocess
import tempfile
import os
import sys
from io import StringIO

def run_python_solution(solution):
    """Run Python solution and capture output"""
    try:
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        # Execute the solution
        exec(solution)

        # Get the output
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        return output.strip(), None
    except Exception as e:
        sys.stdout = old_stdout
        return None, str(e)

def run_java_solution(solution):
    """Compile and run Java solution, capture output"""
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            java_file = os.path.join(tmpdir, 'Main.java')

            with open(java_file, 'w', encoding='utf-8') as f:
                f.write(solution)

            # Compile
            compile_result = subprocess.run(
                ['javac', java_file],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=tmpdir
            )

            if compile_result.returncode != 0:
                return None, f'Compilation error: {compile_result.stderr[:100]}'

            # Run
            run_result = subprocess.run(
                ['java', 'Main'],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=tmpdir
            )

            if run_result.returncode != 0:
                return None, f'Runtime error: {run_result.stderr[:100]}'

            return run_result.stdout.strip(), None

    except subprocess.TimeoutExpired:
        return None, 'Timeout'
    except Exception as e:
        return None, str(e)

def add_expected_outputs(lessons_file, lang):
    """Add expectedOutput to all lessons that need it"""

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    print(f'\n{"="*70}')
    print(f'ADDING EXPECTED OUTPUT - {lang.upper()}')
    print(f'{"="*70}\n')

    updated_count = 0
    error_count = 0
    skipped_count = 0

    runner = run_python_solution if lang == 'python' else run_java_solution

    for lesson in lessons:
        solution = lesson.get('fullSolution', '')
        expected = lesson.get('expectedOutput', '')

        # Check if needs expectedOutput
        has_print = ('print(' in solution) if lang == 'python' else ('System.out' in solution or 'println' in solution)

        if not has_print or len(expected.strip()) >= 3:
            continue  # Already has output or doesn't print

        # Skip framework lessons (need external dependencies)
        if lang == 'python':
            if any(fw in solution.lower() for fw in ['from flask', 'from django', 'import flask', 'import django']):
                skipped_count += 1
                continue
        else:
            if 'org.springframework' in solution:
                skipped_count += 1
                continue

        # Run the solution to get output
        output, error = runner(solution)

        if output is not None and len(output) > 0:
            lesson['expectedOutput'] = output
            updated_count += 1
            print(f'[{updated_count}] Lesson {lesson["id"]}: {lesson["title"][:50]}')
            print(f'    Output ({len(output)} chars): {output[:80]}...' if len(output) > 80 else f'    Output: {output}')
        elif error:
            error_count += 1
            if error_count <= 10:  # Only show first 10 errors
                print(f'[ERROR] Lesson {lesson["id"]}: {error[:60]}')
        else:
            # No output generated (empty)
            skipped_count += 1

    # Save
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    print(f'\n{"="*70}')
    print(f'SUMMARY - {lang.upper()}')
    print(f'{"="*70}')
    print(f'Updated:  {updated_count} lessons')
    print(f'Errors:   {error_count} lessons (couldn\'t run)')
    print(f'Skipped:  {skipped_count} lessons (framework/no output)')
    print(f'{"="*70}\n')

    return updated_count, error_count, skipped_count

if __name__ == '__main__':
    print('\n' + '='*70)
    print('EXPECTED OUTPUT FIXER')
    print('Adding expectedOutput for solve lesson validation')
    print('='*70)

    # Add to Python lessons
    py_updated, py_errors, py_skipped = add_expected_outputs(
        'public/lessons-python.json', 'python'
    )

    # Add to Java lessons
    java_updated, java_errors, java_skipped = add_expected_outputs(
        'public/lessons-java.json', 'java'
    )

    print(f'\n{"="*70}')
    print('OVERALL RESULTS')
    print(f'{"="*70}')
    print(f'Python: {py_updated} updated, {py_errors} errors, {py_skipped} skipped')
    print(f'Java:   {java_updated} updated, {java_errors} errors, {java_skipped} skipped')
    print(f'\nTOTAL UPDATED: {py_updated + java_updated}')
    print(f'{"="*70}\n')
