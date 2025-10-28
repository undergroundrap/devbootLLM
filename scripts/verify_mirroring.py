import json

print("Verifying Java and Python lessons are properly mirrored...")
print("=" * 80)

# Load both files
with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
    java_data = json.load(f)

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    python_data = json.load(f)

java_lessons = java_data['lessons']
python_lessons = python_data['lessons']

print(f"\nJava lessons: {len(java_lessons)}")
print(f"Python lessons: {len(python_lessons)}")

# Create ID maps
java_ids = {lesson['id']: lesson for lesson in java_lessons}
python_ids = {lesson['id']: lesson for lesson in python_lessons}

# Check counts
if len(java_lessons) != len(python_lessons):
    print(f"\n[WARNING] Lesson counts don't match!")
    print(f"  Java: {len(java_lessons)}, Python: {len(python_lessons)}")
else:
    print(f"\n[OK] Both tracks have {len(java_lessons)} lessons")

# Check IDs match
java_id_set = set(java_ids.keys())
python_id_set = set(python_ids.keys())

missing_in_python = java_id_set - python_id_set
missing_in_java = python_id_set - java_id_set

if missing_in_python:
    print(f"\n[WARNING] {len(missing_in_python)} lesson IDs in Java but not Python:")
    print(f"  {sorted(list(missing_in_python))[:10]}")

if missing_in_java:
    print(f"\n[WARNING] {len(missing_in_java)} lesson IDs in Python but not Java:")
    print(f"  {sorted(list(missing_in_java))[:10]}")

if not missing_in_python and not missing_in_java:
    print("[OK] All lesson IDs match between Java and Python")

# Check titles match
title_mismatches = []
for lesson_id in java_id_set & python_id_set:
    java_title = java_ids[lesson_id]['title']
    python_title = python_ids[lesson_id]['title']

    if java_title != python_title:
        title_mismatches.append({
            'id': lesson_id,
            'java': java_title,
            'python': python_title
        })

if title_mismatches:
    print(f"\n[WARNING] {len(title_mismatches)} lessons with different titles:")
    for mismatch in title_mismatches[:5]:
        print(f"  Lesson {mismatch['id']}:")
        print(f"    Java:   {mismatch['java']}")
        print(f"    Python: {mismatch['python']}")
    if len(title_mismatches) > 5:
        print(f"  ... and {len(title_mismatches) - 5} more")
else:
    print("\n[OK] All lesson titles match between tracks")

# Check descriptions match
desc_mismatches = []
for lesson_id in java_id_set & python_id_set:
    java_desc = java_ids[lesson_id].get('description', '')
    python_desc = python_ids[lesson_id].get('description', '')

    if java_desc != python_desc:
        desc_mismatches.append(lesson_id)

if desc_mismatches:
    print(f"\n[WARNING] {len(desc_mismatches)} lessons with different descriptions")
else:
    print("[OK] All lesson descriptions match between tracks")

# Check language field
java_wrong_lang = []
python_wrong_lang = []

for lesson in java_lessons:
    lang = lesson.get('language', 'java').lower()
    if lang != 'java':
        java_wrong_lang.append(lesson['id'])

for lesson in python_lessons:
    lang = lesson.get('language', 'python').lower()
    if lang != 'python':
        python_wrong_lang.append(lesson['id'])

if java_wrong_lang:
    print(f"\n[WARNING] {len(java_wrong_lang)} Java lessons with wrong language field:")
    print(f"  IDs: {java_wrong_lang[:10]}")

if python_wrong_lang:
    print(f"\n[WARNING] {len(python_wrong_lang)} Python lessons with wrong language field:")
    print(f"  IDs: {python_wrong_lang[:10]}")

if not java_wrong_lang and not python_wrong_lang:
    print("\n[OK] All lessons have correct language field")

# Check tags match
tag_mismatches = []
for lesson_id in java_id_set & python_id_set:
    java_tags = set(java_ids[lesson_id].get('tags', []))
    python_tags = set(python_ids[lesson_id].get('tags', []))

    if java_tags != python_tags:
        tag_mismatches.append(lesson_id)

if tag_mismatches:
    print(f"\n[INFO] {len(tag_mismatches)} lessons have different tags (this may be intentional)")
else:
    print("\n[OK] All lessons have matching tags")

# Summary
print("\n" + "=" * 80)
print("MIRRORING SUMMARY")
print("=" * 80)
print(f"Lesson count match: {'YES' if len(java_lessons) == len(python_lessons) else 'NO'}")
print(f"Lesson IDs match: {'YES' if not (missing_in_python or missing_in_java) else 'NO'}")
print(f"Titles match: {'YES' if not title_mismatches else f'NO ({len(title_mismatches)} mismatches)'}")
print(f"Descriptions match: {'YES' if not desc_mismatches else f'NO ({len(desc_mismatches)} mismatches)'}")
print(f"Language fields correct: {'YES' if not (java_wrong_lang or python_wrong_lang) else 'NO'}")

total_issues = len(missing_in_python) + len(missing_in_java) + len(title_mismatches) + len(java_wrong_lang) + len(python_wrong_lang)

if total_issues == 0:
    print("\n[SUCCESS] Java and Python lessons are properly mirrored!")
else:
    print(f"\n[NEEDS ATTENTION] {total_issues} mirroring issues found")
