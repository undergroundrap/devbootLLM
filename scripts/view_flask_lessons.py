import json

# Read the framework stubs to upgrade
with open(r'c:\devbootLLM-app\framework_stubs_to_upgrade.json', 'r', encoding='utf-8') as f:
    stubs_data = json.load(f)

# Filter Flask stubs
flask_stubs = [s for s in stubs_data['stubs'] if s['framework'] == 'Flask']
flask_ids = [s['id'] for s in flask_stubs]

# Read lessons file
with open(r'c:\devbootLLM-app\public\lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

print(f"Found {len(flask_stubs)} Flask stubs to upgrade\n")

# Find and display current code for each Flask stub
for stub in flask_stubs:
    lesson_id = stub['id']
    lesson = next((l for l in lessons if l['id'] == lesson_id), None)
    if lesson:
        code = lesson.get('fullSolution', '')
        print(f"\n{'='*80}")
        print(f"ID {lesson_id}: {lesson['title']}")
        print(f"Current length: {len(code)} chars")
        print(f"Is print stub: {stub['is_print_stub']}")
        print(f"\nCurrent code:")
        print(code if code else "EMPTY")
        print('='*80)
