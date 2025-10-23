#!/usr/bin/env python3
"""
Append generated lessons (601-650) to the main lesson catalogs.
"""

import json
import sys

def append_lessons():
    # Load existing Java lessons
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    # Load existing Python lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_data = json.load(f)

    # Load generated Java lessons
    with open('scripts/generated-java-lessons-601-650.json', 'r', encoding='utf-8') as f:
        new_java = json.load(f)

    # Load generated Python lessons
    with open('scripts/generated-python-lessons-601-650.json', 'r', encoding='utf-8') as f:
        new_python = json.load(f)

    print("Current state:")
    print(f"  Java lessons: {len(java_data['lessons'])}")
    print(f"  Python lessons: {len(python_data['lessons'])}")
    print(f"\nNew lessons to add:")
    print(f"  Java: {len(new_java['lessons'])}")
    print(f"  Python: {len(new_python['lessons'])}")

    # Append new lessons
    java_data['lessons'].extend(new_java['lessons'])
    python_data['lessons'].extend(new_python['lessons'])

    # Sort by ID to ensure order
    java_data['lessons'].sort(key=lambda x: x['id'])
    python_data['lessons'].sort(key=lambda x: x['id'])

    # Save updated catalogs
    with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
        json.dump(java_data, f, indent=2, ensure_ascii=False)

    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(python_data, f, indent=2, ensure_ascii=False)

    print(f"\n[SUCCESS] Lessons appended!")
    print(f"  Total Java lessons: {len(java_data['lessons'])}")
    print(f"  Total Python lessons: {len(python_data['lessons'])}")
    print(f"\nLesson IDs added:")
    print(f"  {[l['id'] for l in new_java['lessons']]}")

if __name__ == "__main__":
    append_lessons()
