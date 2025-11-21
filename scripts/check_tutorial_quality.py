#!/usr/bin/env python3
"""
Tutorial-specific quality checker.
Focuses on tutorial content, readability, and pedagogical value.
"""
import json
import re
from pathlib import Path

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def check_tutorial_structure(tutorial):
    """Check if tutorial has proper structure"""
    issues = []

    # Check for headings
    has_headings = bool(re.search(r'<h[1-6]|^#+\s', tutorial, re.MULTILINE))

    # Check for code examples
    has_code = '<pre' in tutorial or '<code' in tutorial or '```' in tutorial

    # Check for explanatory text
    plain_text = re.sub(r'<[^>]*>', '', tutorial).strip()

    if not has_code:
        issues.append("No code examples found")

    if len(plain_text) < 100:
        issues.append(f"Tutorial very short ({len(plain_text)} chars)")
    elif len(plain_text) > 3000:
        issues.append(f"Tutorial very long ({len(plain_text)} chars, may overwhelm learners)")

    return issues

def check_tutorial_readability(tutorial):
    """Check tutorial readability"""
    issues = []

    # Remove HTML tags
    plain_text = re.sub(r'<[^>]*>', '', tutorial).strip()

    # Check sentence length (very basic heuristic)
    sentences = re.split(r'[.!?]+', plain_text)
    very_long_sentences = [s for s in sentences if len(s.split()) > 50]

    if very_long_sentences:
        issues.append(f"{len(very_long_sentences)} very long sentences (>50 words)")

    # Check for overly technical jargon without explanation
    # Common programming terms that might need explanation for beginners
    advanced_terms = [
        'polymorphism', 'encapsulation', 'inheritance', 'abstraction',
        'recursion', 'algorithm', 'complexity', 'optimization',
        'asynchronous', 'synchronous', 'concurrency', 'mutex'
    ]

    found_advanced = []
    lower_text = plain_text.lower()
    for term in advanced_terms:
        if term in lower_text:
            # Check if there's an explanation nearby (within 100 chars)
            term_pos = lower_text.find(term)
            context = lower_text[max(0, term_pos-50):min(len(lower_text), term_pos+100)]
            if 'means' not in context and 'is when' not in context and 'is a way' not in context:
                found_advanced.append(term)

    if found_advanced:
        issues.append(f"Advanced terms without clear explanation: {', '.join(found_advanced[:3])}")

    return issues

def check_tutorial_code_examples(tutorial):
    """Check quality of code examples in tutorial"""
    issues = []

    # Extract code blocks
    code_blocks = re.findall(r'<pre[^>]*>(.*?)</pre>', tutorial, re.DOTALL)
    code_blocks += re.findall(r'```[^\n]*\n(.*?)```', tutorial, re.DOTALL)

    if not code_blocks:
        issues.append("No code blocks found")
        return issues

    for i, code in enumerate(code_blocks):
        # Remove HTML entities
        code = re.sub(r'&[a-z]+;', '', code)

        # Check if code example is too short
        if len(code.strip()) < 10:
            issues.append(f"Code block {i+1} is very short")

        # Check if code has comments
        has_comments = '//' in code or '#' in code or '/*' in code

        # For longer code blocks, comments are helpful
        if len(code.strip()) > 100 and not has_comments:
            issues.append(f"Code block {i+1} is long but has no comments")

    return issues

def check_tutorial_pedagogy(tutorial, lesson_id):
    """Check pedagogical elements"""
    issues = []

    plain_text = re.sub(r'<[^>]*>', '', tutorial).strip()

    # Check for learning objectives (good tutorials state what you'll learn)
    has_objectives = any(phrase in plain_text.lower() for phrase in [
        'you will learn', 'learn how to', 'this lesson', 'in this tutorial',
        'we will', 'objective', 'goal'
    ])

    # Check for examples and explanations
    has_example_intro = any(phrase in plain_text.lower() for phrase in [
        'for example', 'here\'s an example', 'let\'s look at', 'consider',
        'imagine', 'suppose', 'example:'
    ])

    # Check for practice prompts or exercises
    has_practice = any(phrase in plain_text.lower() for phrase in [
        'try', 'practice', 'exercise', 'your turn', 'now you'
    ])

    # First few lessons should be more explicit
    if lesson_id <= 10:
        if not has_objectives:
            issues.append("Early lesson missing clear learning objective")

    if not has_example_intro and len(plain_text) > 200:
        issues.append("No clear example introduction found")

    return issues

def check_tutorial_consistency(tutorial, lesson):
    """Check if tutorial matches the code and expected output"""
    issues = []

    full_solution = lesson.get('fullSolution', '')
    initial_code = lesson.get('initialCode', '')
    expected_output = lesson.get('expectedOutput', '')

    # Check if tutorial mentions the expected output
    if expected_output and len(expected_output) > 5:
        # Look for the output in the tutorial
        if expected_output.strip() not in tutorial:
            issues.append("Expected output not shown in tutorial")

    # Check if tutorial has code that doesn't match the solution
    code_in_tutorial = re.findall(r'<pre[^>]*>(.*?)</pre>', tutorial, re.DOTALL)
    code_in_tutorial += re.findall(r'```[^\n]*\n(.*?)```', tutorial, re.DOTALL)

    # If tutorial has code, check if it's similar to the solution
    if code_in_tutorial and full_solution:
        tutorial_code = ' '.join(code_in_tutorial)
        # Remove HTML entities and whitespace for comparison
        tutorial_code_clean = re.sub(r'\s+', ' ', re.sub(r'&[a-z]+;', '', tutorial_code))
        solution_clean = re.sub(r'\s+', ' ', full_solution)

        # Check if they're completely different (might indicate a mismatch)
        # This is a heuristic - we check if key identifiers match
        tutorial_identifiers = set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', tutorial_code_clean))
        solution_identifiers = set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', solution_clean))

        # Remove common keywords
        common_keywords = {'public', 'static', 'void', 'class', 'return', 'if', 'else', 'for', 'while',
                          'def', 'print', 'import', 'from', 'int', 'String', 'main', 'System', 'out'}
        tutorial_identifiers -= common_keywords
        solution_identifiers -= common_keywords

        if tutorial_identifiers and solution_identifiers:
            overlap = len(tutorial_identifiers & solution_identifiers) / max(len(solution_identifiers), 1)
            if overlap < 0.3:
                issues.append("Tutorial code examples seem unrelated to the solution")

    return issues

def analyze_tutorials(file_path, language):
    """Analyze tutorial quality for all lessons"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}Tutorial Quality Check: {language.upper()}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lessons = json.load(f)
    except Exception as e:
        print(f"{Colors.RED}Error loading file: {e}{Colors.RESET}")
        return

    if isinstance(lessons, dict) and 'lessons' in lessons:
        lessons = lessons['lessons']

    print(f"Analyzing tutorials for {Colors.BOLD}{len(lessons)}{Colors.RESET} lessons...\n")

    issue_categories = {
        'structure': 0,
        'readability': 0,
        'code_examples': 0,
        'pedagogy': 0,
        'consistency': 0
    }

    problematic_tutorials = []
    total_issues = 0

    for lesson in lessons:
        lesson_id = lesson.get('id', 'unknown')
        title = lesson.get('title', 'Unknown')
        tutorial = lesson.get('tutorial', '')

        lesson_issues = []

        # Run all checks
        checks = [
            ('structure', check_tutorial_structure(tutorial)),
            ('readability', check_tutorial_readability(tutorial)),
            ('code_examples', check_tutorial_code_examples(tutorial)),
            ('pedagogy', check_tutorial_pedagogy(tutorial, lesson_id)),
            ('consistency', check_tutorial_consistency(tutorial, lesson))
        ]

        for category, issues in checks:
            if issues:
                issue_categories[category] += len(issues)
                lesson_issues.extend([(category, issue) for issue in issues])

        if lesson_issues:
            total_issues += len(lesson_issues)
            problematic_tutorials.append({
                'id': lesson_id,
                'title': title,
                'issues': lesson_issues
            })

    # Summary
    print(f"{Colors.BOLD}Tutorial Issue Summary:{Colors.RESET}")
    for category, count in issue_categories.items():
        color = Colors.GREEN if count == 0 else Colors.YELLOW if count < 20 else Colors.RED
        print(f"  {color}{category.title():20s}: {count:4d}{Colors.RESET}")

    print(f"\n{Colors.BOLD}Statistics:{Colors.RESET}")
    print(f"  Lessons with tutorial issues: {len(problematic_tutorials)} / {len(lessons)}")
    print(f"  Total tutorial issues: {total_issues}")

    if problematic_tutorials:
        print(f"\n{Colors.BOLD}Tutorials Needing Improvement (top 15):{Colors.RESET}")
        sorted_tutorials = sorted(problematic_tutorials, key=lambda x: len(x['issues']), reverse=True)[:15]
        for tutorial in sorted_tutorials:
            print(f"\n{Colors.YELLOW}Lesson {tutorial['id']}: {tutorial['title'][:60]}{Colors.RESET}")
            for category, issue in tutorial['issues'][:3]:
                print(f"  [{category}] {issue}")
            if len(tutorial['issues']) > 3:
                print(f"  ... and {len(tutorial['issues']) - 3} more")

    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")

    return {
        'total_lessons': len(lessons),
        'tutorials_with_issues': len(problematic_tutorials),
        'total_issues': total_issues,
        'issue_categories': issue_categories
    }

def main():
    script_dir = Path(__file__).parent
    public_dir = script_dir.parent / 'public'

    python_file = public_dir / 'lessons-python.json'
    java_file = public_dir / 'lessons-java.json'

    results = {}

    if python_file.exists():
        results['python'] = analyze_tutorials(python_file, 'python')

    if java_file.exists():
        results['java'] = analyze_tutorials(java_file, 'java')

    # Save report
    report_file = script_dir.parent / 'tutorial_quality_report.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"{Colors.CYAN}Tutorial quality report saved to: {report_file}{Colors.RESET}\n")

if __name__ == '__main__':
    main()
