import json
import re

# IDs of all bridging lessons
BRIDGING_IDS = [
    101, 102, 103, 104,  # Beginner bridges
    205, 206, 207, 208, 209, 210, 211, 212, 213, 214,  # Intermediate bridges
    365, 366, 367, 368, 369, 370, 371, 372, 373, 374,  # Advanced bridges
    525, 526, 527, 528, 529, 530, 531, 532,  # Expert bridges
    633, 634, 635, 636, 637, 638, 639,  # Enterprise bridges
    735  # Final bridge
]

def wrap_in_main_class(code):
    """Wrap code in public class Main if not already wrapped"""
    if 'class Main' in code:
        return code  # Already has Main class

    # If it has any public class declaration, rename it to Main
    if 'public class' in code:
        # Change class name to Main
        code = re.sub(r'public\s+class\s+\w+', 'public class Main', code, count=1)
        return code

    # If it's standalone code, wrap it
    return f'public class Main {{\n{code}\n}}'

print("Fixing Java bridging lessons...")
print("=" * 80)

# Load Java lessons
with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
    java_data = json.load(f)

fixed_count = 0

for lesson in java_data['lessons']:
    if lesson['id'] in BRIDGING_IDS:
        initial = lesson.get('initialCode', '')
        solution = lesson.get('fullSolution', '')

        # Check if either needs fixing
        needs_fix = False

        if solution and 'class Main' not in solution:
            lesson['fullSolution'] = wrap_in_main_class(solution)
            needs_fix = True

        if initial and 'class Main' not in initial:
            lesson['initialCode'] = wrap_in_main_class(initial)
            needs_fix = True

        if needs_fix:
            print(f"Fixed lesson {lesson['id']}: {lesson['title']}")
            fixed_count += 1

print("=" * 80)
print(f"Fixed {fixed_count} Java bridging lessons")

# Save
with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
    json.dump(java_data, f, indent=2, ensure_ascii=False)

print("Saved updated lessons-java.json")
