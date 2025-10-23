#!/usr/bin/env python3
"""
Append the 11 complete priority lessons to the main catalog
"""

import json

def append_lessons():
    print("Appending 11 new priority lessons to catalog...")
    print("=" * 60)

    # Load existing catalogs
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_data = json.load(f)

    # Load new lessons
    with open('scripts/generated-java-lessons-601-650-COMPLETE.json', 'r', encoding='utf-8') as f:
        new_java = json.load(f)

    with open('scripts/generated-python-lessons-601-650-COMPLETE.json', 'r', encoding='utf-8') as f:
        new_python = json.load(f)

    print(f"Current Java lessons: {len(java_data['lessons'])}")
    print(f"Current Python lessons: {len(python_data['lessons'])}")
    print(f"New Java lessons to add: {len(new_java['lessons'])}")
    print(f"New Python lessons to add: {len(new_python['lessons'])}")

    # Get existing IDs to avoid duplicates
    existing_java_ids = {l['id'] for l in java_data['lessons']}
    existing_python_ids = {l['id'] for l in python_data['lessons']}

    # Add only new lessons
    added_java = 0
    for lesson in new_java['lessons']:
        if lesson['id'] not in existing_java_ids:
            java_data['lessons'].append(lesson)
            added_java += 1

    added_python = 0
    for lesson in new_python['lessons']:
        if lesson['id'] not in existing_python_ids:
            python_data['lessons'].append(lesson)
            added_python += 1

    # Sort by ID
    java_data['lessons'].sort(key=lambda x: x['id'])
    python_data['lessons'].sort(key=lambda x: x['id'])

    # Save
    with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
        json.dump(java_data, f, indent=2, ensure_ascii=False)

    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(python_data, f, indent=2, ensure_ascii=False)

    print(f"\n[SUCCESS] Appended lessons!")
    print(f"Added {added_java} Java lessons")
    print(f"Added {added_python} Python lessons")
    print(f"\nNew totals:")
    print(f"Java: {len(java_data['lessons'])} lessons")
    print(f"Python: {len(python_data['lessons'])} lessons")
    print(f"Combined: {len(java_data['lessons']) + len(python_data['lessons'])} total")

    # Show new lesson IDs
    new_ids = sorted([l['id'] for l in new_java['lessons']])
    print(f"\nLesson IDs added: {new_ids}")

if __name__ == "__main__":
    append_lessons()
