import json
import re

def comprehensive_tutorial_check(lessons_file, language):
    """Verify all tutorials have proper structure"""
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    stats = {
        'total': len(lessons),
        'has_tutorial': 0,
        'has_code_blocks': 0,
        'has_pre_tags': 0,
        'missing_code': [],
        'very_short_tutorial': [],
        'missing_tutorial': []
    }

    for lesson in lessons:
        lid = lesson.get('id')
        title = lesson.get('title', '')
        tutorial = lesson.get('tutorial', '')
        additional = lesson.get('additionalExamples', '')

        # Check if tutorial exists
        if not tutorial or len(tutorial.strip()) < 10:
            stats['missing_tutorial'].append((lid, title))
            continue

        stats['has_tutorial'] += 1

        # Check for code blocks (pre/code tags or markdown)
        has_pre = bool(re.search(r'<pre[^>]*>', tutorial))
        has_code = bool(re.search(r'<code[^>]*>', tutorial))
        has_markdown_code = '```' in tutorial

        if has_pre:
            stats['has_pre_tags'] += 1

        if has_pre or has_code or has_markdown_code:
            stats['has_code_blocks'] += 1
        else:
            # No code in tutorial - check if it's in additionalExamples
            has_additional_code = bool(re.search(r'<pre[^>]*>', additional)) or bool(re.search(r'<code[^>]*>', additional))
            if not has_additional_code:
                stats['missing_code'].append((lid, title))

        # Check for very short tutorials
        if len(tutorial) < 500:
            stats['very_short_tutorial'].append((lid, title, len(tutorial)))

    return stats

# Check both languages
print("="*70)
print("COMPREHENSIVE TUTORIAL VERIFICATION")
print("="*70)

python_stats = comprehensive_tutorial_check('public/lessons-python.json', 'Python')
java_stats = comprehensive_tutorial_check('public/lessons-java.json', 'Java')

print("\nPYTHON TUTORIALS:")
print("-"*70)
print(f"Total lessons: {python_stats['total']}")
print(f"Has tutorial: {python_stats['has_tutorial']} ({python_stats['has_tutorial']/python_stats['total']*100:.1f}%)")
print(f"Has code blocks in tutorial: {python_stats['has_code_blocks']} ({python_stats['has_code_blocks']/python_stats['total']*100:.1f}%)")
print(f"Missing tutorial: {len(python_stats['missing_tutorial'])}")
print(f"Missing code examples: {len(python_stats['missing_code'])}")
print(f"Very short tutorials (<500 chars): {len(python_stats['very_short_tutorial'])}")

print("\nJAVA TUTORIALS:")
print("-"*70)
print(f"Total lessons: {java_stats['total']}")
print(f"Has tutorial: {java_stats['has_tutorial']} ({java_stats['has_tutorial']/java_stats['total']*100:.1f}%)")
print(f"Has code blocks in tutorial: {java_stats['has_code_blocks']} ({java_stats['has_code_blocks']/java_stats['total']*100:.1f}%)")
print(f"Missing tutorial: {len(java_stats['missing_tutorial'])}")
print(f"Missing code examples: {len(java_stats['missing_code'])}")
print(f"Very short tutorials (<500 chars): {len(java_stats['very_short_tutorial'])}")

# Check if the numbers match what was reported (362 lessons)
total_missing_code = len(python_stats['missing_code']) + len(java_stats['missing_code'])
print("\n" + "="*70)
print("CONCLUSION:")
print("="*70)
if total_missing_code == 0:
    print("PASS - All tutorials have code examples (either in tutorial or additionalExamples)")
    print("\nThe '362 lessons with code block issues' was likely a false alarm from")
    print("an earlier script that didn't detect <pre> tags with attributes correctly.")
else:
    print(f"ISSUES FOUND: {total_missing_code} lessons missing code examples")

# Save detailed report
with open('tutorial_verification_report.txt', 'w', encoding='utf-8') as f:
    f.write("COMPREHENSIVE TUTORIAL VERIFICATION\n")
    f.write("="*70 + "\n\n")

    f.write("PYTHON:\n")
    f.write(f"Total: {python_stats['total']}\n")
    f.write(f"Has code blocks: {python_stats['has_code_blocks']}\n")
    f.write(f"Missing code: {len(python_stats['missing_code'])}\n\n")

    if python_stats['missing_code']:
        f.write("Lessons missing code examples:\n")
        for lid, title in python_stats['missing_code']:
            f.write(f"  {lid}: {title}\n")

    f.write("\n\nJAVA:\n")
    f.write(f"Total: {java_stats['total']}\n")
    f.write(f"Has code blocks: {java_stats['has_code_blocks']}\n")
    f.write(f"Missing code: {len(java_stats['missing_code'])}\n\n")

    if java_stats['missing_code']:
        f.write("Lessons missing code examples:\n")
        for lid, title in java_stats['missing_code']:
            f.write(f"  {lid}: {title}\n")

print("\nDetailed report saved to: tutorial_verification_report.txt")
