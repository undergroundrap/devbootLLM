#!/usr/bin/env python3
import json

# Load main catalogs
with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
    java_main = json.load(f)

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    python_main = json.load(f)

print(f"Current: Java {len(java_main['lessons'])}, Python {len(python_main['lessons'])}")

# Load all 50
with open('scripts/ALL-50-JAVA.json', 'r', encoding='utf-8') as f:
    java_50 = json.load(f)

with open('scripts/ALL-50-PYTHON.json', 'r', encoding='utf-8') as f:
    python_50 = json.load(f)

print(f"Adding: Java {len(java_50['lessons'])}, Python {len(python_50['lessons'])}")

# Get existing IDs
existing_java = {l['id'] for l in java_main['lessons']}
existing_python = {l['id'] for l in python_main['lessons']}

# Add new only
java_added = 0
for lesson in java_50['lessons']:
    if lesson['id'] not in existing_java:
        java_main['lessons'].append(lesson)
        java_added += 1

python_added = 0
for lesson in python_50['lessons']:
    if lesson['id'] not in existing_python:
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

print(f"\nAdded: Java +{java_added}, Python +{python_added}")
print(f"Final: Java {len(java_main['lessons'])}, Python {len(python_main['lessons'])}")
print(f"TOTAL: {len(java_main['lessons']) + len(python_main['lessons'])} lessons")
