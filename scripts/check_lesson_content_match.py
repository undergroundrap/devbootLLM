#!/usr/bin/env python3
"""
Check that lesson tutorials and examples match the lesson topic.
"""

import json
import re


def check_content_mismatch(lesson, language):
    """Check if lesson content matches its title/description."""
    title = lesson['title'].lower()
    description = lesson['description'].lower()
    tutorial = lesson.get('tutorial', '').lower()
    solution = lesson.get('fullSolution', '').lower()
    examples = lesson.get('additionalExamples', '').lower()

    issues = []

    # Extract key topic words from title
    # Remove common words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'as', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'should', 'could', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'your', 'use', 'using', 'implement', 'create', 'basic', 'simple', 'advanced'}

    title_words = set(re.findall(r'\w+', title)) - stop_words

    # Skip very generic titles
    if len(title_words) == 0:
        return []

    # Check if tutorial mentions other unrelated topics more than the main topic
    # Look for mentions of common frameworks/topics that shouldn't be in certain lessons
    unrelated_topics = {
        'pandas', 'numpy', 'django', 'flask', 'fastapi', 'spring', 'hibernate',
        'kubernetes', 'docker', 'kafka', 'redis', 'mongodb', 'postgresql',
        'react', 'vue', 'angular', 'tensorflow', 'pytorch', 'scikit-learn'
    }

    # Count mentions in tutorial
    tutorial_mentions = {}
    for topic in unrelated_topics:
        count = tutorial.count(topic)
        if count > 0:
            tutorial_mentions[topic] = count

    # Check if title topic is barely mentioned but other topics are heavily mentioned
    title_mention_count = sum(1 for word in title_words if word in tutorial)

    if tutorial_mentions and title_mention_count == 0:
        # Tutorial talks about other topics but not the main topic
        most_mentioned = max(tutorial_mentions.items(), key=lambda x: x[1])
        if most_mentioned[1] > 3:  # Mentioned more than 3 times
            issues.append(f"Tutorial focuses on '{most_mentioned[0]}' ({most_mentioned[1]} times) but lesson is about '{title}'")

    # Check for specific problematic patterns

    # Hello World should not have complex examples
    if 'hello' in title and 'world' in title:
        if 'dataframe' in tutorial or 'class' in solution or 'import pandas' in solution:
            issues.append("Hello World has overly complex content")

    # Check if description mentions something not in solution
    desc_words = set(re.findall(r'\w+', description)) - stop_words
    key_desc_words = desc_words - title_words  # Words unique to description

    # Look for completely wrong tutorial content
    wrong_tutorials = [
        ('string concatenation', ['pandas', 'dataframe', 'numpy array']),
        ('print', ['database', 'sql', 'orm', 'query']),
        ('variable', ['kubernetes', 'cluster', 'deployment']),
        ('loop', ['machine learning', 'neural network', 'training']),
        ('if statement', ['docker', 'container', 'image'])
    ]

    for topic, wrong_keywords in wrong_tutorials:
        if topic in title:
            for keyword in wrong_keywords:
                if keyword in tutorial and keyword not in title:
                    issues.append(f"'{topic}' lesson contains '{keyword}' content")

    return issues


def main():
    """Check all lessons for content mismatches."""
    print("\n" + "="*80)
    print("CHECKING LESSON CONTENT MATCHES")
    print("="*80)

    # Check Java
    print("\nChecking Java lessons...")
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_lessons = json.load(f)

    java_issues = []
    for lesson in java_lessons[:50]:  # Check first 50
        issues = check_content_mismatch(lesson, 'java')
        if issues:
            java_issues.append((lesson['id'], lesson['title'], issues))

    # Check Python
    print("Checking Python lessons...")
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_lessons = json.load(f)

    python_issues = []
    for lesson in python_lessons[:50]:  # Check first 50
        issues = check_content_mismatch(lesson, 'python')
        if issues:
            python_issues.append((lesson['id'], lesson['title'], issues))

    # Report
    print("\n" + "="*80)
    print("RESULTS")
    print("="*80)

    if java_issues:
        print(f"\nJava: {len(java_issues)} lessons with potential mismatches:")
        for lid, title, issues in java_issues:
            print(f"\n  Lesson {lid}: {title}")
            for issue in issues:
                print(f"    - {issue}")
    else:
        print("\nJava: No obvious content mismatches found in first 50 lessons")

    if python_issues:
        print(f"\nPython: {len(python_issues)} lessons with potential mismatches:")
        for lid, title, issues in python_issues:
            print(f"\n  Lesson {lid}: {title}")
            for issue in issues:
                print(f"    - {issue}")
    else:
        print("\nPython: No obvious content mismatches found in first 50 lessons")

    print("\n" + "="*80)


if __name__ == "__main__":
    main()
