#!/usr/bin/env python3
"""
Comprehensive scan for potential issues in lessons:
1. Framework keywords in non-tagged lessons
2. Missing imports that should be framework
3. Unusual patterns
"""

import json
import re

# Framework keywords that should trigger isFramework
PYTHON_FRAMEWORKS = [
    'flask', 'django', 'fastapi', 'sqlalchemy', 'boto3', 'kafka',
    'redis', 'celery', 'sklearn', 'tensorflow', 'pandas', 'numpy',
    'mockito', 'unittest.mock', 'pytest', 'requests', 'aiohttp',
    'tornado', 'bottle', 'pyramid', 'scrapy', 'beautifulsoup',
    'selenium', 'pillow', 'opencv', 'matplotlib', 'seaborn',
    'plotly', 'dash', 'streamlit', 'gradio', 'transformers',
    'pytorch', 'keras', 'scipy', 'statsmodels', 'networkx',
    'pydantic', 'marshmallow', 'alembic', 'peewee', 'mongoengine'
]

JAVA_FRAMEWORKS = [
    'spring', 'hibernate', 'jpa', 'kafka', 'kubernetes', 'graphql',
    'grpc', 'reactor', 'webflux', 'mockito', 'junit', 'testng',
    'lombok', 'jackson', 'gson', 'guava', 'apache.commons',
    'netty', 'vertx', 'akka', 'micronaut', 'quarkus',
    'jooq', 'mybatis', 'cassandra', 'elasticsearch', 'redis',
    'javax.servlet', 'javax.inject', 'javax.persistence',
    'org.springframework', 'org.hibernate', 'org.apache',
    'com.fasterxml.jackson', 'io.netty', 'io.grpc'
]

def scan_python_lessons():
    """Scan Python lessons for potential issues."""
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    issues = []

    for lesson in data:
        code = lesson.get('fullSolution', '').lower()
        title = lesson.get('title', '').lower()
        is_framework = lesson.get('isFramework', False)

        # Check for framework keywords in non-tagged lessons
        if not is_framework:
            found_frameworks = []
            for fw in PYTHON_FRAMEWORKS:
                # Check for imports like "import flask" or "from flask import"
                if f'import {fw}' in code or f'from {fw} import' in code:
                    found_frameworks.append(fw)
                elif fw in title and fw not in ['mock', 'test']:  # Avoid false positives
                    found_frameworks.append(fw)

            if found_frameworks:
                issues.append({
                    'id': lesson['id'],
                    'title': lesson['title'],
                    'type': 'Missing framework tag',
                    'details': f"Found framework keywords: {', '.join(found_frameworks)}",
                    'isFramework': is_framework
                })

    return issues

def scan_java_lessons():
    """Scan Java lessons for potential issues."""
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    issues = []

    for lesson in data:
        code = lesson.get('fullSolution', '').lower()
        title = lesson.get('title', '').lower()
        is_framework = lesson.get('isFramework', False)

        # Check for framework keywords in non-tagged lessons
        if not is_framework:
            found_frameworks = []
            for fw in JAVA_FRAMEWORKS:
                # Check for imports
                if f'import {fw}' in code or fw in title:
                    # Avoid false positives for common words
                    if fw not in ['test', 'mock'] or (f'import {fw}' in code):
                        found_frameworks.append(fw)

            if found_frameworks:
                issues.append({
                    'id': lesson['id'],
                    'title': lesson['title'],
                    'type': 'Missing framework tag',
                    'details': f"Found framework keywords: {', '.join(found_frameworks)}",
                    'isFramework': is_framework
                })

    return issues

def main():
    print("=" * 80)
    print("SCANNING FOR POTENTIAL ISSUES IN LESSONS")
    print("=" * 80)
    print()

    print("Scanning Python lessons...")
    python_issues = scan_python_lessons()
    print(f"Found {len(python_issues)} potential issues in Python lessons")
    print()

    print("Scanning Java lessons...")
    java_issues = scan_java_lessons()
    print(f"Found {len(java_issues)} potential issues in Java lessons")
    print()

    all_issues = python_issues + java_issues

    if all_issues:
        print("=" * 80)
        print(f"FOUND {len(all_issues)} POTENTIAL ISSUES:")
        print("=" * 80)
        print()

        for issue in all_issues[:30]:  # Show first 30
            print(f"Lesson {issue['id']:4d}: {issue['title']}")
            print(f"  Type: {issue['type']}")
            print(f"  Details: {issue['details']}")
            print()

        if len(all_issues) > 30:
            print(f"... and {len(all_issues) - 30} more issues")
    else:
        print("=" * 80)
        print("[SUCCESS] No issues found!")
        print("=" * 80)

    return 0

if __name__ == '__main__':
    main()
