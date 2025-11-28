#!/usr/bin/env python3
"""
Find lessons that have REAL framework imports but aren't tagged as framework lessons.
"""

import json
import re

def has_real_python_framework_import(code):
    """Check if code has real framework imports."""
    imports = []

    # Common frameworks
    frameworks = {
        'flask': r'from flask import|import flask',
        'django': r'from django|import django',
        'fastapi': r'from fastapi import|import fastapi',
        'sqlalchemy': r'from sqlalchemy import|import sqlalchemy',
        'pandas': r'import pandas|from pandas import',
        'numpy': r'import numpy|from numpy import',
        'sklearn': r'from sklearn|import sklearn',
        'pytest': r'import pytest|from pytest import',
        'boto3': r'import boto3|from boto3 import',
        'requests': r'import requests|from requests import',
    }

    for fw, pattern in frameworks.items():
        if re.search(pattern, code, re.IGNORECASE):
            imports.append(fw)

    return imports

def has_real_java_framework_import(code):
    """Check if code has real framework imports."""
    imports = []

    # Common frameworks
    frameworks = {
        'Spring': r'import org\.springframework',
        'Hibernate': r'import org\.hibernate',
        'JPA': r'import javax\.persistence',
        'Mockito': r'import org\.mockito',
        'JUnit': r'import org\.junit',
        'Kafka': r'import org\.apache\.kafka',
        'Gson': r'import com\.google\.gson',
        'Jackson': r'import com\.fasterxml\.jackson',
    }

    for fw, pattern in frameworks.items():
        if re.search(pattern, code, re.IGNORECASE):
            imports.append(fw)

    return imports

def main():
    print("=" * 80)
    print("FINDING LESSONS WITH REAL FRAMEWORK IMPORTS BUT NOT TAGGED")
    print("=" * 80)
    print()

    # Python lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_data = json.load(f)

    python_untagged = []
    for lesson in python_data:
        if not lesson.get('isFramework', False):
            code = lesson.get('fullSolution', '')
            imports = has_real_python_framework_import(code)
            if imports:
                python_untagged.append({
                    'id': lesson['id'],
                    'title': lesson['title'],
                    'imports': imports
                })

    # Java lessons
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    java_untagged = []
    for lesson in java_data:
        if not lesson.get('isFramework', False):
            code = lesson.get('fullSolution', '')
            imports = has_real_java_framework_import(code)
            if imports:
                java_untagged.append({
                    'id': lesson['id'],
                    'title': lesson['title'],
                    'imports': imports
                })

    print(f"Python lessons with real framework imports but not tagged: {len(python_untagged)}")
    print(f"Java lessons with real framework imports but not tagged: {len(java_untagged)}")
    print()

    if python_untagged:
        print("-" * 80)
        print("PYTHON LESSONS THAT NEED FRAMEWORK TAG:")
        print("-" * 80)
        for lesson in python_untagged:
            print(f"Lesson {lesson['id']:4d}: {lesson['title']}")
            print(f"  Imports: {', '.join(lesson['imports'])}")
            print()

    if java_untagged:
        print("-" * 80)
        print("JAVA LESSONS THAT NEED FRAMEWORK TAG:")
        print("-" * 80)
        for lesson in java_untagged:
            print(f"Lesson {lesson['id']:4d}: {lesson['title']}")
            print(f"  Imports: {', '.join(lesson['imports'])}")
            print()

    total = len(python_untagged) + len(java_untagged)

    if total == 0:
        print("=" * 80)
        print("[SUCCESS] All lessons with framework imports are properly tagged!")
        print("=" * 80)
        return 0
    else:
        print("=" * 80)
        print(f"[ACTION NEEDED] {total} lessons need to be tagged as framework lessons")
        print("=" * 80)
        return total

if __name__ == '__main__':
    total = main()
    print(f"\nTotal untagged framework lessons: {total}")
