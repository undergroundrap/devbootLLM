import json
import re

def check_tutorial_sections(tutorial):
    """Check which sections are present in a tutorial"""
    tutorial_lower = tutorial.lower()

    sections = {
        'Overview': bool(re.search(r'overview|introduction', tutorial_lower)),
        'Key Concepts': bool(re.search(r'key concepts?|main concepts?|core concepts?', tutorial_lower)),
        'Code Examples': bool(re.search(r'example|code|implementation', tutorial_lower)),
        'Best Practices': bool(re.search(r'best practices?|tips|guidelines', tutorial_lower)),
        'Common Pitfalls': bool(re.search(r'common pitfalls?|mistakes?|errors?|watch out', tutorial_lower)),
        'Real-World': bool(re.search(r'real.world|practical|applications?|use case', tutorial_lower))
    }

    return sections

def analyze_lessons(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    lessons = data['lessons']
    incomplete = []

    for lesson in lessons:
        sections = check_tutorial_sections(lesson['tutorial'])
        section_count = sum(sections.values())

        if section_count < 6:
            missing = [name for name, present in sections.items() if not present]
            incomplete.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'section_count': section_count,
                'missing': missing,
                'tutorial_length': len(lesson['tutorial'])
            })

    return incomplete

# Analyze Java lessons
print("=" * 80)
print("INCOMPLETE TUTORIALS ANALYSIS")
print("=" * 80)

incomplete = analyze_lessons('public/lessons-java.json')

print(f"\nFound {len(incomplete)} lessons with incomplete tutorials:\n")

# Group by section count
by_count = {}
for lesson in incomplete:
    count = lesson['section_count']
    if count not in by_count:
        by_count[count] = []
    by_count[count].append(lesson)

for count in sorted(by_count.keys()):
    lessons = by_count[count]
    print(f"\n{count} sections ({len(lessons)} lessons):")
    print("-" * 80)
    for lesson in lessons:
        print(f"  Lesson {lesson['id']}: {lesson['title']}")
        print(f"    Missing: {', '.join(lesson['missing'])}")
        print(f"    Tutorial length: {lesson['tutorial_length']} chars")
        print()

print("\nSUMMARY:")
print("-" * 80)
print(f"Total incomplete: {len(incomplete)}")
print(f"Target: 0 incomplete (100% tutorial depth)")
print(f"Current: {len(incomplete)} need sections added")
