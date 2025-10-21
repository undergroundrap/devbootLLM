#!/usr/bin/env python3
"""
Comprehensive lesson analyzer:
1. Check for compilation/syntax issues
2. Detect redundant topics
3. Verify learning progression
4. Identify gaps in coverage
"""

import json
from collections import defaultdict, Counter

def load_lessons(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['lessons']

def analyze_redundancy(lessons):
    """Find potentially redundant lessons by comparing titles and descriptions"""
    title_groups = defaultdict(list)
    desc_groups = defaultdict(list)

    for lesson in lessons:
        # Group by similar title keywords
        title_lower = lesson['title'].lower()
        for word in title_lower.split():
            if len(word) > 3:  # Ignore short words
                title_groups[word].append(lesson['id'])

        # Check description similarity
        desc_lower = lesson.get('description', '').lower()
        desc_groups[desc_lower].append(lesson['id'])

    # Find duplicates
    duplicate_descriptions = {desc: ids for desc, ids in desc_groups.items() if len(ids) > 1 and desc}

    return title_groups, duplicate_descriptions

def check_java_syntax(lessons):
    """Check for common Java syntax issues"""
    issues = []

    for lesson in lessons:
        if lesson.get('language') != 'java':
            continue

        lid = lesson['id']
        code = lesson.get('fullSolution', '')

        # Check for common issues
        if 'public class Main' not in code:
            issues.append(f"Lesson {lid}: Missing 'public class Main'")

        if 'public static void main' not in code:
            issues.append(f"Lesson {lid}: Missing main method")

        # Check for unmatched braces
        if code.count('{') != code.count('}'):
            issues.append(f"Lesson {lid}: Unmatched braces")

        # Check for unmatched quotes (simple check)
        quote_count = code.count('"') - code.count('\\"')
        if quote_count % 2 != 0:
            issues.append(f"Lesson {lid}: Unmatched quotes")

    return issues

def check_python_syntax(lessons):
    """Check for common Python syntax issues"""
    issues = []

    for lesson in lessons:
        if lesson.get('language') != 'python':
            continue

        lid = lesson['id']
        code = lesson.get('fullSolution', '')

        # Check for unmatched quotes
        single_quotes = code.count("'") - code.count("\\'")
        double_quotes = code.count('"') - code.count('\\"')

        if single_quotes % 2 != 0:
            issues.append(f"Lesson {lid}: Unmatched single quotes")
        if double_quotes % 2 != 0:
            issues.append(f"Lesson {lid}: Unmatched double quotes")

        # Check for unmatched parentheses
        if code.count('(') != code.count(')'):
            issues.append(f"Lesson {lid}: Unmatched parentheses")

        if code.count('[') != code.count(']'):
            issues.append(f"Lesson {lid}: Unmatched brackets")

    return issues

def analyze_topic_coverage(lessons):
    """Analyze what topics are covered"""
    tag_counts = Counter()
    topics_by_id = {}

    for lesson in lessons:
        tags = lesson.get('tags', [])
        tag_counts.update(tags)
        topics_by_id[lesson['id']] = {
            'title': lesson['title'],
            'tags': tags,
            'description': lesson.get('description', '')
        }

    return tag_counts, topics_by_id

def check_mirroring(java_lessons, python_lessons):
    """Check if Java and Python lessons are properly mirrored"""
    issues = []

    java_by_id = {l['id']: l for l in java_lessons}
    python_by_id = {l['id']: l for l in python_lessons}

    all_ids = set(java_by_id.keys()) | set(python_by_id.keys())

    for lid in sorted(all_ids):
        if lid not in java_by_id:
            issues.append(f"ID {lid}: Missing in Java")
        elif lid not in python_by_id:
            issues.append(f"ID {lid}: Missing in Python")
        else:
            j_title = java_by_id[lid]['title']
            p_title = python_by_id[lid]['title']

            # Check if titles are reasonably similar (same ID number)
            if not j_title.startswith(f"{lid}."):
                issues.append(f"ID {lid}: Java title doesn't start with lesson number")
            if not p_title.startswith(f"{lid}."):
                issues.append(f"ID {lid}: Python title doesn't start with lesson number")

    return issues

def main():
    print("=" * 80)
    print("LESSON ANALYSIS REPORT")
    print("=" * 80)

    # Load lessons
    java_lessons = load_lessons('public/lessons-java.json')
    python_lessons = load_lessons('public/lessons-python.json')

    print(f"\nTotal lessons: Java={len(java_lessons)}, Python={len(python_lessons)}")

    # Check mirroring
    print("\n" + "=" * 80)
    print("MIRRORING CHECK")
    print("=" * 80)
    mirror_issues = check_mirroring(java_lessons, python_lessons)
    if mirror_issues:
        print("Issues found:")
        for issue in mirror_issues[:20]:  # Limit output
            print(f"  - {issue}")
        if len(mirror_issues) > 20:
            print(f"  ... and {len(mirror_issues) - 20} more")
    else:
        print("[OK] All lessons properly mirrored")

    # Check Java syntax
    print("\n" + "=" * 80)
    print("JAVA SYNTAX CHECK")
    print("=" * 80)
    java_issues = check_java_syntax(java_lessons)
    if java_issues:
        print("Issues found:")
        for issue in java_issues[:20]:
            print(f"  - {issue}")
        if len(java_issues) > 20:
            print(f"  ... and {len(java_issues) - 20} more")
    else:
        print("[OK] No obvious Java syntax issues")

    # Check Python syntax
    print("\n" + "=" * 80)
    print("PYTHON SYNTAX CHECK")
    print("=" * 80)
    python_issues = check_python_syntax(python_lessons)
    if python_issues:
        print("Issues found:")
        for issue in python_issues[:20]:
            print(f"  - {issue}")
        if len(python_issues) > 20:
            print(f"  ... and {len(python_issues) - 20} more")
    else:
        print("[OK] No obvious Python syntax issues")

    # Analyze redundancy
    print("\n" + "=" * 80)
    print("REDUNDANCY ANALYSIS")
    print("=" * 80)

    java_title_groups, java_dup_desc = analyze_redundancy(java_lessons)
    python_title_groups, python_dup_desc = analyze_redundancy(python_lessons)

    if java_dup_desc:
        print("\nJava lessons with duplicate descriptions:")
        for desc, ids in list(java_dup_desc.items())[:5]:
            print(f"  IDs {ids}: {desc[:60]}...")
    else:
        print("[OK] No duplicate Java descriptions")

    if python_dup_desc:
        print("\nPython lessons with duplicate descriptions:")
        for desc, ids in list(python_dup_desc.items())[:5]:
            print(f"  IDs {ids}: {desc[:60]}...")
    else:
        print("[OK] No duplicate Python descriptions")

    # Topic coverage
    print("\n" + "=" * 80)
    print("TOPIC COVERAGE")
    print("=" * 80)

    java_tags, java_topics = analyze_topic_coverage(java_lessons)
    python_tags, python_topics = analyze_topic_coverage(python_lessons)

    print("\nJava topic distribution:")
    for tag, count in java_tags.most_common(15):
        print(f"  {tag}: {count} lessons")

    print("\nPython topic distribution:")
    for tag, count in python_tags.most_common(15):
        print(f"  {tag}: {count} lessons")

    # Check for potential gaps
    print("\n" + "=" * 80)
    print("POTENTIAL GAPS IN COVERAGE")
    print("=" * 80)

    common_topics = {
        'Strings', 'Collections', 'I/O', 'Error Handling', 'OOP',
        'Control Flow', 'Functions', 'Algorithms', 'Data Structures',
        'Concurrency', 'Streams', 'JSON', 'Files'
    }

    java_covered = set(java_tags.keys())
    python_covered = set(python_tags.keys())

    java_gaps = common_topics - java_covered
    python_gaps = common_topics - python_covered

    if java_gaps:
        print(f"\nPotential Java gaps: {', '.join(java_gaps)}")
    else:
        print("[OK] Java covers all common topics")

    if python_gaps:
        print(f"\nPotential Python gaps: {', '.join(python_gaps)}")
    else:
        print("[OK] Python covers all common topics")

    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
