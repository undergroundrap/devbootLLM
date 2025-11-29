import json
import sys

# Read the framework stubs to upgrade
with open(r'c:\devbootLLM-app\framework_stubs_to_upgrade.json', 'r', encoding='utf-8') as f:
    stubs_data = json.load(f)

# Filter Flask stubs
flask_stubs = [s for s in stubs_data['stubs'] if s['framework'] == 'Flask']

# Read the lessons file in chunks to find Flask lessons
print(f"Found {len(flask_stubs)} Flask stubs to potentially upgrade")
print("\nFlask Stub IDs:", [s['id'] for s in flask_stubs])

# Read lessons file
with open(r'c:\devbootLLM-app\public\lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

print(f"\nTotal lessons in file: {len(lessons)}")

# Find and display current code for each Flask stub
for stub in flask_stubs:
    lesson_id = stub['id']
    lesson = next((l for l in lessons if l['id'] == lesson_id), None)
    if lesson:
        print(f"\n{'='*80}")
        print(f"ID {lesson_id}: {lesson['title']}")
        print(f"Current length: {len(lesson.get('code', ''))} chars")
        print(f"Is print stub: {stub['is_print_stub']}")
        print(f"\nCurrent code:")
        print(lesson.get('code', 'NO CODE FOUND'))
        print('='*80)
