#!/usr/bin/env python3
"""
Extract failed lesson IDs and details from validation output.
"""
import re
from pathlib import Path

def extract_failures(file_path):
    """Extract all failed lessons from validation output"""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    failures = []
    passes = []
    errors = []

    for i, line in enumerate(lines):
        # Look for FAIL markers (with or without ANSI codes)
        if '[FAIL]' in line or 'FAIL' in line:
            # Extract lesson ID and title
            match = re.search(r'(\d+)\.\s+(.+)$', line)
            if match:
                lesson_id = int(match.group(1))
                title = match.group(2).strip()

                # Try to get expected/actual from next lines
                expected = ""
                actual = ""
                if i + 1 < len(lines) and 'Expected:' in lines[i + 1]:
                    expected = lines[i + 1].split('Expected:')[1].strip()[:100]
                if i + 2 < len(lines) and 'Actual:' in lines[i + 2]:
                    actual = lines[i + 2].split('Actual:')[1].strip()[:100]

                failures.append({
                    'id': lesson_id,
                    'title': title,
                    'expected': expected,
                    'actual': actual
                })

        elif '[PASS]' in line or 'PASS' in line:
            match = re.search(r'(\d+)\.\s+', line)
            if match:
                passes.append(int(match.group(1)))

        elif '[ERROR]' in line or 'ERROR' in line:
            match = re.search(r'(\d+)\.\s+(.+)$', line)
            if match:
                errors.append({
                    'id': int(match.group(1)),
                    'title': match.group(2).strip()
                })

    return failures, passes, errors

def main():
    output_file = Path(__file__).parent.parent / 'validation_output.txt'

    if not output_file.exists():
        print("Validation output file not found.")
        return

    failures, passes, errors = extract_failures(output_file)

    print("="*80)
    print("LESSON VALIDATION RESULTS")
    print("="*80)
    print()
    print(f"[PASS] Passed:  {len(passes):4d} lessons")
    print(f"[FAIL] Failed:  {len(failures):4d} lessons (output mismatch)")
    print(f"[ERR]  Errors:  {len(errors):4d} lessons (execution error)")
    print(f"       Total:   {len(passes) + len(failures) + len(errors):4d} lessons tested")
    print()

    if failures:
        print("="*80)
        print("FAILED LESSONS - Will show output mismatch error")
        print("="*80)
        print()
        print("These lessons will display:")
        print("'[X] Not quite right. The code runs, but the output doesn't match.'")
        print()

        # Group failures by ID range
        ranges = []
        for f in sorted(failures, key=lambda x: x['id']):
            print(f"  {f['id']:4d}. {f['title'][:60]}")

        # Save detailed report
        report_file = Path(__file__).parent.parent / 'failed_lessons_report.txt'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("FAILED LESSONS - DETAILED REPORT\n")
            f.write("="*80 + "\n\n")
            f.write(f"Total failures: {len(failures)}\n\n")

            for failure in sorted(failures, key=lambda x: x['id']):
                f.write(f"Lesson {failure['id']}: {failure['title']}\n")
                if failure['expected']:
                    f.write(f"  Expected: {failure['expected']}\n")
                if failure['actual']:
                    f.write(f"  Actual:   {failure['actual']}\n")
                f.write("\n")

        print(f"\nDetailed report saved to: {report_file}")

    if errors:
        print()
        print("="*80)
        print("LESSONS WITH EXECUTION ERRORS")
        print("="*80)
        print()
        for error in sorted(errors, key=lambda x: x['id']):
            print(f"  {error['id']:4d}. {error['title'][:60]}")

    print()
    print("="*80)

if __name__ == '__main__':
    main()
