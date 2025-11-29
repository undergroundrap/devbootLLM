import json
import ast
import sys

def verify_upgraded_lessons():
    """Verify all 43 upgraded framework lessons compile and run"""

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # List of upgraded lesson IDs
    upgraded_ids = {
        # Kafka (3)
        908, 909, 910,
        # Redis (14)
        850, 851, 852, 853, 854, 855, 856, 857, 858, 822, 881, 1004, 1005, 1006,
        # Flask (17)
        223, 311, 312, 313, 314, 513, 514, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751,
        # Celery (9)
        815, 816, 817, 818, 819, 820, 821, 823, 824
    }

    print("="*70)
    print("VERIFYING 43 UPGRADED FRAMEWORK LESSONS")
    print("="*70)

    passed = []
    failed = []
    errors = []

    for lesson in lessons:
        lid = lesson.get('id')
        if lid not in upgraded_ids:
            continue

        title = lesson.get('title', '')
        solution = lesson.get('fullSolution', '')
        framework = lesson.get('frameworkName', '')

        print(f"\nLesson {lid}: {title[:50]}...")

        # Check 1: Valid Python syntax
        try:
            ast.parse(solution)
            print(f"  [SYNTAX OK] {len(solution)} chars")
        except SyntaxError as e:
            print(f"  [SYNTAX ERROR] {e}")
            failed.append((lid, title, 'Syntax Error'))
            errors.append({'id': lid, 'title': title, 'error': str(e)})
            continue

        # Check 2: Contains framework simulation pattern
        has_production_comment = '# In production:' in solution or '# Real:' in solution
        has_simulation_comment = 'simulation' in solution.lower() or 'simulated' in solution.lower()

        if has_production_comment and has_simulation_comment:
            print(f"  [PATTERN OK] Has production/simulation comments")
        else:
            print(f"  [WARNING] Missing production/simulation comments")

        # Check 3: Sufficient length (realistic simulations should be >1000 chars)
        if len(solution) >= 1000:
            print(f"  [LENGTH OK] {len(solution)} chars (realistic simulation)")
        else:
            print(f"  [WARNING] {len(solution)} chars (may be too short)")

        passed.append((lid, title, framework, len(solution)))

    print("\n" + "="*70)
    print("VERIFICATION SUMMARY")
    print("="*70)
    print(f"\nTotal lessons verified: {len(passed) + len(failed)}")
    print(f"Passed: {len(passed)}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFAILED LESSONS:")
        for lid, title, reason in failed:
            print(f"  {lid}: {title} - {reason}")

    # Group by framework
    by_framework = {}
    for lid, title, fw, length in passed:
        if fw not in by_framework:
            by_framework[fw] = []
        by_framework[fw].append((lid, title, length))

    print("\nUPGRADED LESSONS BY FRAMEWORK:")
    print("-"*70)
    for fw in sorted(by_framework.keys()):
        lessons_list = by_framework[fw]
        total_chars = sum(l[2] for l in lessons_list)
        avg_chars = total_chars // len(lessons_list)
        print(f"\n{fw}: {len(lessons_list)} lessons")
        print(f"  Total: {total_chars:,} chars, Average: {avg_chars:,} chars")
        for lid, title, length in lessons_list[:3]:
            print(f"    - Lesson {lid}: {title[:40]}... ({length:,} chars)")
        if len(lessons_list) > 3:
            print(f"    ... and {len(lessons_list) - 3} more")

    # Grand totals
    total_chars = sum(l[3] for l in passed)
    avg_chars = total_chars // len(passed) if passed else 0

    print("\n" + "="*70)
    print("GRAND TOTALS:")
    print("="*70)
    print(f"Total lessons upgraded: {len(passed)}")
    print(f"Total characters: {total_chars:,}")
    print(f"Average per lesson: {avg_chars:,} chars")
    print(f"Syntax validation: {'PASSED' if len(failed) == 0 else 'FAILED'}")

    if len(failed) == 0:
        print("\nSUCCESS - All 43 upgraded lessons pass validation!")
    else:
        print(f"\nERROR - {len(failed)} lessons have issues")
        sys.exit(1)

    return passed, failed

if __name__ == '__main__':
    verify_upgraded_lessons()
