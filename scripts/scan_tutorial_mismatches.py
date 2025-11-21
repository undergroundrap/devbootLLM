#!/usr/bin/env python3
"""
Scan all lessons for tutorial/example content that doesn't match the lesson topic.
"""

import json
import re


def detect_mismatch(lesson):
    """Detect if tutorial/examples don't match the lesson title."""
    title = lesson['title'].lower()
    description = lesson['description'].lower()
    tutorial = lesson.get('tutorial', '').lower()
    examples = lesson.get('additionalExamples', '').lower()

    mismatches = []

    # Define topic keywords and what they should/shouldn't contain
    checks = [
        # (title_keywords, should_not_contain_keywords, mismatch_description)
        (['boolean', 'logic'], ['string concatenation', 'combine strings', 'alex', 'welcome,'], 'has string concatenation content'),
        (['hello', 'world'], ['pandas', 'dataframe', 'numpy', 'class dataitem'], 'has advanced framework content'),
        (['print', 'debugging'], ['pandas', 'dataframe', 'sql', 'database'], 'has database/data science content'),
        (['variable'], ['kubernetes', 'cluster', 'deployment', 'docker'], 'has devops content'),
        (['comment'], ['kubernetes', 'neural network', 'machine learning'], 'has ML/DevOps content'),
        (['loop', 'for loop', 'while loop'], ['machine learning', 'neural', 'training'], 'has ML content'),
        (['if statement', 'conditional'], ['docker', 'container', 'kubernetes'], 'has container content'),
        (['string'], ['boolean logic', 'access granted', 'is_admin'], 'has boolean logic content'),
        (['integer', 'division', 'modulo'], ['string', 'concatenation', 'pandas'], 'has string/pandas content'),
    ]

    for title_keywords, bad_keywords, description in checks:
        # Check if this lesson is about the topic
        if any(keyword in title for keyword in title_keywords):
            # Check if tutorial contains unrelated content
            for bad in bad_keywords:
                if bad in tutorial or bad in examples:
                    mismatches.append(description)
                    break

    return mismatches


def main():
    """Scan all lessons."""
    print("\n" + "="*80)
    print("SCANNING FOR TUTORIAL/EXAMPLE MISMATCHES")
    print("="*80)

    # Scan Python
    print("\nScanning Python lessons...")
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_lessons = json.load(f)

    python_mismatches = []
    for lesson in python_lessons:
        mismatches = detect_mismatch(lesson)
        if mismatches:
            python_mismatches.append((lesson['id'], lesson['title'], mismatches))

    # Scan Java
    print("Scanning Java lessons...")
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_lessons = json.load(f)

    java_mismatches = []
    for lesson in java_lessons:
        mismatches = detect_mismatch(lesson)
        if mismatches:
            java_mismatches.append((lesson['id'], lesson['title'], mismatches))

    # Report
    print("\n" + "="*80)
    print("RESULTS")
    print("="*80)

    if python_mismatches:
        print(f"\nPython: {len(python_mismatches)} lessons with mismatched content:")
        for lid, title, mismatches in python_mismatches[:20]:
            print(f"  Lesson {lid}: {title}")
            for mismatch in mismatches:
                print(f"    - {mismatch}")
        if len(python_mismatches) > 20:
            print(f"  ... and {len(python_mismatches) - 20} more")
    else:
        print("\nPython: No mismatches found")

    if java_mismatches:
        print(f"\nJava: {len(java_mismatches)} lessons with mismatched content:")
        for lid, title, mismatches in java_mismatches[:20]:
            print(f"  Lesson {lid}: {title}")
            for mismatch in mismatches:
                print(f"    - {mismatch}")
        if len(java_mismatches) > 20:
            print(f"  ... and {len(java_mismatches) - 20} more")
    else:
        print("\nJava: No mismatches found")

    print(f"\nTotal mismatched lessons: {len(python_mismatches) + len(java_mismatches)}")
    print("\n" + "="*80)

    return python_mismatches, java_mismatches


if __name__ == "__main__":
    python_mismatches, java_mismatches = main()
