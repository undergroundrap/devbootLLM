#!/usr/bin/env python3
"""
Comprehensive validation of all 650 lessons for both Java and Python.
Checks: placeholders, tutorial quality, tags, filters, ordering, mirroring.
"""

import json
import re
from collections import defaultdict


def validate_lesson_structure(lesson, lesson_num, language):
    """Validate a single lesson's structure and content"""
    issues = []

    # Check required fields
    required_fields = ['id', 'title', 'description', 'initialCode', 'fullSolution',
                      'expectedOutput', 'tutorial', 'language', 'tags']
    for field in required_fields:
        if field not in lesson or not lesson[field]:
            issues.append(f"Missing or empty field: {field}")

    # Check ID matches position
    if lesson.get('id') != lesson_num:
        issues.append(f"ID mismatch: expected {lesson_num}, got {lesson.get('id')}")

    # Check language
    if lesson.get('language') != language:
        issues.append(f"Language mismatch: expected {language}, got {lesson.get('language')}")

    # Check for placeholder code (more lenient for early lessons, strict for 601-650)
    solution = lesson.get('fullSolution', '')
    lesson_id = lesson.get('id', 0)

    if lesson_id >= 601:
        # FAANG lessons should have substantial code
        if len(solution) < 200:
            issues.append(f"FAANG lesson solution too short ({len(solution)} chars)")
        if 'TODO' in solution:
            issues.append("FAANG lesson contains TODO - must be complete")
        if 'System.out.println("TODO")' in solution:
            issues.append("FAANG lesson has placeholder println")
    else:
        # Early lessons can be shorter but shouldn't be completely empty
        if len(solution) < 20:
            issues.append(f"Solution empty or too short ({len(solution)} chars)")

    # Check tutorial quality
    tutorial = lesson.get('tutorial', '')
    if len(tutorial) < 300:
        issues.append(f"Tutorial too short ({len(tutorial)} chars)")
    if '<h4' not in tutorial and '<h3' not in tutorial:
        issues.append("Tutorial missing section headers")
    # For FAANG lessons, require substantial tutorials (>1000 chars)
    if lesson_id >= 601 and len(tutorial) < 1000:
        issues.append(f"FAANG tutorial too short ({len(tutorial)} chars - should be >1000)")

    # Check tags
    tags = lesson.get('tags', [])
    if not tags:
        issues.append("No tags defined")
    if len(tags) < 2:
        issues.append(f"Only {len(tags)} tag(s) - should have multiple categories")

    # Check description
    description = lesson.get('description', '')
    if len(description) < 20:
        issues.append(f"Description too short ({len(description)} chars)")

    return issues


def check_lesson_mirroring(java_lesson, python_lesson):
    """Check if Java and Python lessons mirror each other"""
    issues = []

    if java_lesson['id'] != python_lesson['id']:
        issues.append(f"ID mismatch: Java {java_lesson['id']} vs Python {python_lesson['id']}")

    if java_lesson['title'] != python_lesson['title']:
        issues.append(f"Title mismatch: '{java_lesson['title']}' vs '{python_lesson['title']}'")

    # Tutorial should be identical for lessons 601-650 (FAANG lessons)
    # Earlier lessons may have language-specific tutorials
    if java_lesson['id'] >= 601 and java_lesson['tutorial'] != python_lesson['tutorial']:
        issues.append("FAANG lesson tutorials don't match between Java and Python")

    # Tags should be identical
    if set(java_lesson['tags']) != set(python_lesson['tags']):
        issues.append(f"Tags differ: Java {java_lesson['tags']} vs Python {python_lesson['tags']}")

    # Expected output should be similar
    java_output = java_lesson['expectedOutput'].strip()
    python_output = python_lesson['expectedOutput'].strip()
    if java_output != python_output and len(java_output) > 0 and len(python_output) > 0:
        # Allow minor differences but flag large discrepancies
        if abs(len(java_output) - len(python_output)) > 50:
            issues.append(f"Expected output length differs significantly")

    return issues


def analyze_tags(lessons):
    """Analyze tag distribution and coverage"""
    tag_counts = defaultdict(int)
    lessons_by_tag = defaultdict(list)

    for lesson in lessons:
        for tag in lesson.get('tags', []):
            tag_counts[tag] += 1
            lessons_by_tag[tag].append(lesson['id'])

    return tag_counts, lessons_by_tag


def check_lesson_progression(lessons):
    """Check if lessons progress logically"""
    issues = []

    # Check IDs are sequential
    expected_ids = set(range(1, len(lessons) + 1))
    actual_ids = set(lesson['id'] for lesson in lessons)

    missing = expected_ids - actual_ids
    if missing:
        issues.append(f"Missing lesson IDs: {sorted(missing)}")

    extra = actual_ids - expected_ids
    if extra:
        issues.append(f"Extra lesson IDs: {sorted(extra)}")

    # Check for duplicate IDs
    id_counts = defaultdict(int)
    for lesson in lessons:
        id_counts[lesson['id']] += 1

    duplicates = {lid: count for lid, count in id_counts.items() if count > 1}
    if duplicates:
        issues.append(f"Duplicate lesson IDs: {duplicates}")

    return issues


def main():
    print("=" * 80)
    print("COMPREHENSIVE LESSON VALIDATION - ALL 650 LESSONS")
    print("=" * 80)
    print()

    # Load both lesson files
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_data = json.load(f)

    java_lessons = java_data['lessons']
    python_lessons = python_data['lessons']

    print(f"Loaded {len(java_lessons)} Java lessons and {len(python_lessons)} Python lessons")
    print()

    # Track all issues
    all_issues = {
        'java': {},
        'python': {},
        'mirroring': {},
        'structure': []
    }

    # 1. Validate Java lessons
    print("=" * 80)
    print("VALIDATING JAVA LESSONS")
    print("=" * 80)

    for i, lesson in enumerate(java_lessons, 1):
        issues = validate_lesson_structure(lesson, i, 'java')
        if issues:
            all_issues['java'][i] = issues

    if all_issues['java']:
        print(f"\n[FAIL] Found issues in {len(all_issues['java'])} Java lessons:")
        for lid, issues in sorted(all_issues['java'].items())[:10]:  # Show first 10
            print(f"\n  Lesson {lid}: {java_lessons[lid-1].get('title', 'Unknown')}")
            for issue in issues:
                print(f"    - {issue}")
        if len(all_issues['java']) > 10:
            print(f"\n  ... and {len(all_issues['java']) - 10} more lessons with issues")
    else:
        print("[PASS] All Java lessons passed validation!")

    # 2. Validate Python lessons
    print("\n" + "=" * 80)
    print("VALIDATING PYTHON LESSONS")
    print("=" * 80)

    for i, lesson in enumerate(python_lessons, 1):
        issues = validate_lesson_structure(lesson, i, 'python')
        if issues:
            all_issues['python'][i] = issues

    if all_issues['python']:
        print(f"\n[FAIL] Found issues in {len(all_issues['python'])} Python lessons:")
        for lid, issues in sorted(all_issues['python'].items())[:10]:
            print(f"\n  Lesson {lid}: {python_lessons[lid-1].get('title', 'Unknown')}")
            for issue in issues:
                print(f"    - {issue}")
        if len(all_issues['python']) > 10:
            print(f"\n  ... and {len(all_issues['python']) - 10} more lessons with issues")
    else:
        print("[PASS] All Python lessons passed validation!")

    # 3. Check mirroring between Java and Python
    print("\n" + "=" * 80)
    print("VALIDATING JAVA <-> PYTHON MIRRORING")
    print("=" * 80)

    for java_lesson, python_lesson in zip(java_lessons, python_lessons):
        issues = check_lesson_mirroring(java_lesson, python_lesson)
        if issues:
            all_issues['mirroring'][java_lesson['id']] = issues

    if all_issues['mirroring']:
        print(f"\n[FAIL] Found mirroring issues in {len(all_issues['mirroring'])} lessons:")
        for lid, issues in sorted(all_issues['mirroring'].items())[:10]:
            print(f"\n  Lesson {lid}:")
            for issue in issues:
                print(f"    - {issue}")
        if len(all_issues['mirroring']) > 10:
            print(f"\n  ... and {len(all_issues['mirroring']) - 10} more lessons with issues")
    else:
        print("[PASS] Java and Python lessons mirror correctly!")

    # 4. Check lesson progression
    print("\n" + "=" * 80)
    print("VALIDATING LESSON PROGRESSION")
    print("=" * 80)

    java_progression = check_lesson_progression(java_lessons)
    python_progression = check_lesson_progression(python_lessons)

    if java_progression or python_progression:
        print("\n[FAIL] Progression issues found:")
        if java_progression:
            print("\n  Java:")
            for issue in java_progression:
                print(f"    - {issue}")
        if python_progression:
            print("\n  Python:")
            for issue in python_progression:
                print(f"    - {issue}")
    else:
        print("[PASS] Lesson progression is correct!")

    # 5. Analyze tags
    print("\n" + "=" * 80)
    print("TAG ANALYSIS")
    print("=" * 80)

    java_tag_counts, java_lessons_by_tag = analyze_tags(java_lessons)

    print(f"\nTotal unique tags: {len(java_tag_counts)}")
    print("\nTop tags:")
    for tag, count in sorted(java_tag_counts.items(), key=lambda x: -x[1])[:15]:
        print(f"  {tag}: {count} lessons")

    # Check for lessons without common tags
    beginner_count = len([l for l in java_lessons if 'Beginner' in l.get('tags', [])])
    faang_count = len([l for l in java_lessons if 'FAANG' in l.get('tags', [])])

    print(f"\nTag coverage:")
    print(f"  Beginner lessons: {beginner_count}")
    print(f"  FAANG lessons: {faang_count}")

    # 6. Summary
    print("\n" + "=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)

    total_issues = len(all_issues['java']) + len(all_issues['python']) + len(all_issues['mirroring'])

    if total_issues == 0 and not java_progression and not python_progression:
        print("\n[PASS] [PASS] [PASS] ALL VALIDATIONS PASSED! [PASS] [PASS] [PASS]")
        print("\nYour lesson catalog is production-ready!")
        print(f"  - {len(java_lessons)} Java lessons: 100% validated")
        print(f"  - {len(python_lessons)} Python lessons: 100% validated")
        print(f"  - Perfect mirroring between languages")
        print(f"  - {len(java_tag_counts)} unique tags for filtering")
        print(f"  - Sequential lesson IDs (1-{len(java_lessons)})")
    else:
        print(f"\n[WARN]  Found {total_issues} lessons with issues that need fixing:")
        print(f"  - Java lessons: {len(all_issues['java'])} issues")
        print(f"  - Python lessons: {len(all_issues['python'])} issues")
        print(f"  - Mirroring: {len(all_issues['mirroring'])} issues")

        # Save detailed report
        with open('scripts/validation_report.json', 'w', encoding='utf-8') as f:
            json.dump(all_issues, f, indent=2)

        print("\n[INFO] Detailed report saved to: scripts/validation_report.json")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
