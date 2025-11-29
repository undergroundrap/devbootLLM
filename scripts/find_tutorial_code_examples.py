import json
import re

def check_tutorial_code_structure(lessons_file, language):
    """Check how tutorials present code examples"""
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    issues = []

    for lesson in lessons:
        lid = lesson.get('id')
        title = lesson.get('title', '')
        tutorial = lesson.get('tutorial', '')
        additional = lesson.get('additionalExamples', '')

        # Check if tutorial says "study the code" or similar
        study_phrases = [
            'study the code',
            'examine the code',
            'look at the code',
            'review the code',
            'check the code',
            'see the code',
            'observe the code'
        ]

        has_study_phrase = any(phrase in tutorial.lower() for phrase in study_phrases)

        # Check if tutorial has actual code blocks
        has_code_in_tutorial = bool(re.search(r'<pre[^>]*>.*?<code', tutorial, re.DOTALL)) or \
                               bool(re.search(r'```', tutorial))

        # Check if additionalExamples has code blocks
        has_code_in_additional = bool(re.search(r'<pre[^>]*>.*?<code', additional, re.DOTALL)) or \
                                 bool(re.search(r'```', additional))

        # Flag if tutorial says "study code" but doesn't show code inline
        if has_study_phrase and not has_code_in_tutorial:
            issues.append({
                'id': lid,
                'title': title,
                'has_code_in_additional': has_code_in_additional,
                'tutorial_length': len(tutorial),
                'additional_length': len(additional)
            })

    return issues

# Check both languages
print("Checking Python lessons...")
python_issues = check_tutorial_code_structure('public/lessons-python.json', 'Python')

print("Checking Java lessons...")
java_issues = check_tutorial_code_structure('public/lessons-java.json', 'Java')

print("\n" + "="*70)
print("TUTORIAL CODE BLOCK INVESTIGATION")
print("="*70)

print(f"\nPython: {len(python_issues)} lessons say 'study the code' without showing it")
print(f"Java: {len(java_issues)} lessons say 'study the code' without showing it")
print(f"Total: {len(python_issues) + len(java_issues)} lessons affected")

# Sample 10 from each
print("\n" + "="*70)
print("SAMPLE PYTHON LESSONS:")
print("="*70)
for issue in python_issues[:10]:
    print(f"\nLesson {issue['id']}: {issue['title']}")
    print(f"  Tutorial length: {issue['tutorial_length']} chars")
    print(f"  Additional examples length: {issue['additional_length']} chars")
    print(f"  Has code in additionalExamples: {issue['has_code_in_additional']}")

print("\n" + "="*70)
print("SAMPLE JAVA LESSONS:")
print("="*70)
for issue in java_issues[:10]:
    print(f"\nLesson {issue['id']}: {issue['title']}")
    print(f"  Tutorial length: {issue['tutorial_length']} chars")
    print(f"  Additional examples length: {issue['additional_length']} chars")
    print(f"  Has code in additionalExamples: {issue['has_code_in_additional']}")

# Save full report
with open('tutorial_code_structure_report.txt', 'w', encoding='utf-8') as f:
    f.write("TUTORIAL CODE STRUCTURE INVESTIGATION\n")
    f.write("="*70 + "\n\n")
    f.write(f"Found {len(python_issues) + len(java_issues)} lessons that say 'study the code' without showing it inline\n\n")

    f.write("PYTHON LESSONS:\n")
    f.write("-"*70 + "\n")
    for issue in python_issues:
        f.write(f"{issue['id']}\t{issue['title']}\tAdditional: {issue['has_code_in_additional']}\n")

    f.write("\n\nJAVA LESSONS:\n")
    f.write("-"*70 + "\n")
    for issue in java_issues:
        f.write(f"{issue['id']}\t{issue['title']}\tAdditional: {issue['has_code_in_additional']}\n")

print("\n\nFull report saved to: tutorial_code_structure_report.txt")
