"""
Apply Flask simulation upgrades to lessons-python.json
"""
import json
import sys
from flask_simulations import SIMULATIONS

# Read lessons file
print("Reading lessons-python.json...")
with open(r'c:\devbootLLM-app\public\lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

print(f"Total lessons: {len(lessons)}")

# Track upgrades
upgrades = []
errors = []

# Apply upgrades
for lesson_id, new_code in SIMULATIONS.items():
    lesson = next((l for l in lessons if l['id'] == lesson_id), None)
    if not lesson:
        errors.append(f"Lesson {lesson_id} not found")
        continue

    old_code = lesson.get('fullSolution', '')
    old_length = len(old_code)
    new_length = len(new_code)

    # Update the lesson
    lesson['fullSolution'] = new_code

    upgrades.append({
        'id': lesson_id,
        'title': lesson['title'],
        'old_length': old_length,
        'new_length': new_length,
        'growth': new_length - old_length
    })

    print(f"[OK] Updated {lesson_id}: {lesson['title']} ({old_length} -> {new_length} chars)")

# Write updated lessons
print(f"\nWriting updated lessons to file...")
with open(r'c:\devbootLLM-app\public\lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print(f"[OK] Successfully wrote {len(lessons)} lessons")

# Generate report
print("\n" + "="*80)
print("FLASK UPGRADE REPORT")
print("="*80)

print(f"\nTotal lessons upgraded: {len(upgrades)}")
print(f"Errors encountered: {len(errors)}")

if upgrades:
    print("\nUpgrades by lesson:")
    print(f"{'ID':<6} {'Title':<50} {'Before':<8} {'After':<8} {'Growth':<8}")
    print("-" * 80)
    for upgrade in sorted(upgrades, key=lambda x: x['id']):
        print(f"{upgrade['id']:<6} {upgrade['title'][:48]:<50} {upgrade['old_length']:<8} {upgrade['new_length']:<8} {upgrade['growth']:+<8}")

    print("\nStatistics:")
    total_old = sum(u['old_length'] for u in upgrades)
    total_new = sum(u['new_length'] for u in upgrades)
    avg_old = total_old / len(upgrades)
    avg_new = total_new / len(upgrades)
    print(f"  Total characters before: {total_old:,}")
    print(f"  Total characters after:  {total_new:,}")
    print(f"  Total growth:            {total_new - total_old:,} (+{((total_new/total_old - 1) * 100):.1f}%)")
    print(f"  Average before:          {avg_old:.0f} chars")
    print(f"  Average after:           {avg_new:.0f} chars")

    # Check target range
    in_range = [u for u in upgrades if 1000 <= u['new_length'] <= 3500]
    print(f"  Lessons in target range (1000-3500 chars): {len(in_range)}/{len(upgrades)}")

if errors:
    print("\nErrors:")
    for error in errors:
        print(f"  - {error}")

# Save report
report = {
    'total_upgraded': len(upgrades),
    'total_errors': len(errors),
    'upgrades': upgrades,
    'errors': errors
}

with open(r'c:\devbootLLM-app\flask_upgrade_report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2)

print(f"\n[OK] Report saved to flask_upgrade_report.json")
