#!/usr/bin/env python3
"""
Append all generated lessons to main catalog
Final push to get maximum lesson count
"""

import json

def main():
    print("=" * 70)
    print("FINAL LESSON APPEND - Getting to Maximum Coverage")
    print("=" * 70)

    # Load main catalogs
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_main = json.load(f)

    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_main = json.load(f)

    print(f"\nCurrent catalog:")
    print(f"  Java: {len(java_main['lessons'])} lessons")
    print(f"  Python: {len(python_main['lessons'])} lessons")

    # Load generated lessons
    with open('scripts/final-java-lessons-601-650.json', 'r', encoding='utf-8') as f:
        java_new = json.load(f)

    with open('scripts/final-python-lessons-601-650.json', 'r', encoding='utf-8') as f:
        python_new = json.load(f)

    print(f"\nGenerated lessons to add:")
    print(f"  Java: {len(java_new['lessons'])} lessons")
    print(f"  Python: {len(python_new['lessons'])} lessons")

    # Get existing IDs
    existing_java_ids = {l['id'] for l in java_main['lessons']}
    existing_python_ids = {l['id'] for l in python_main['lessons']}

    # Add only new ones
    java_added = 0
    for lesson in java_new['lessons']:
        if lesson['id'] not in existing_java_ids:
            java_main['lessons'].append(lesson)
            java_added += 1

    python_added = 0
    for lesson in python_new['lessons']:
        if lesson['id'] not in existing_python_ids:
            python_main['lessons'].append(lesson)
            python_added += 1

    # Sort
    java_main['lessons'].sort(key=lambda x: x['id'])
    python_main['lessons'].sort(key=lambda x: x['id'])

    # Save
    with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
        json.dump(java_main, f, indent=2, ensure_ascii=False)

    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(python_main, f, indent=2, ensure_ascii=False)

    print(f"\n[SUCCESS]")
    print(f"  Added {java_added} Java lessons")
    print(f"  Added {python_added} Python lessons")
    print(f"\nFinal totals:")
    print(f"  Java: {len(java_main['lessons'])} lessons")
    print(f"  Python: {len(python_main['lessons'])} lessons")
    print(f"  Combined: {len(java_main['lessons']) + len(python_main['lessons'])} total")

    new_ids = sorted([l['id'] for l in java_new['lessons']])
    print(f"\nLesson IDs in catalog: {new_ids}")

if __name__ == "__main__":
    main()
