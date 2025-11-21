#!/usr/bin/env python3
"""
Comprehensive lesson quality checker.
Checks for:
- Required fields
- Title format and ID consistency
- Tutorial quality (length, code examples)
- Code quality in solutions
- Common mistakes
- Security issues
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

REQUIRED_FIELDS = ['id', 'title', 'language', 'description', 'initialCode', 'fullSolution', 'expectedOutput', 'tutorial']

def check_required_fields(lesson):
    """Check if all required fields are present and non-empty"""
    issues = []
    for field in REQUIRED_FIELDS:
        if field not in lesson:
            issues.append(f"Missing field: {field}")
        elif lesson[field] is None:
            issues.append(f"Field is null: {field}")
        elif isinstance(lesson[field], str) and lesson[field].strip() == '':
            # expectedOutput can be empty string for lessons with no output
            if field != 'expectedOutput':
                issues.append(f"Field is empty: {field}")
    return issues

def check_title_format(lesson):
    """Check if title starts with lesson ID"""
    issues = []
    lesson_id = lesson.get('id')
    title = lesson.get('title', '')

    if not title.startswith(f"{lesson_id}."):
        issues.append(f"Title should start with '{lesson_id}.' but is: {title}")

    return issues

def check_tutorial_quality(lesson):
    """Check tutorial content quality"""
    issues = []
    tutorial = lesson.get('tutorial', '')

    # Check for code examples
    if '<pre' not in tutorial and '<code' not in tutorial and '```' not in tutorial:
        issues.append("Tutorial missing code examples")

    # Remove HTML tags for length check
    plain_text = re.sub(r'<[^>]*>', '', tutorial).strip()

    if len(plain_text) < 100:
        issues.append(f"Tutorial too short ({len(plain_text)} chars, should be at least 100)")

    # Check for common placeholder text
    placeholders = ['TODO', 'FIXME', 'placeholder', 'lorem ipsum', 'coming soon']
    lower_text = plain_text.lower()
    for placeholder in placeholders:
        if placeholder in lower_text:
            issues.append(f"Tutorial contains placeholder text: {placeholder}")

    return issues

def check_code_quality(lesson, language):
    """Check for common code issues"""
    issues = []
    full_solution = lesson.get('fullSolution', '')
    initial_code = lesson.get('initialCode', '')

    # Check if solutions are not empty
    if not full_solution.strip():
        issues.append("fullSolution is empty")

    # Check for TODO/FIXME in solutions
    if 'TODO' in full_solution or 'FIXME' in full_solution:
        issues.append("fullSolution contains TODO/FIXME")

    # Language-specific checks
    if language == 'python':
        # Check for proper Python syntax patterns
        if full_solution and not any(keyword in full_solution for keyword in ['print', 'def', 'class', 'import', '#']):
            if len(full_solution) > 20:  # Only flag if it's not a trivial example
                issues.append("Python code might be missing common keywords")

    elif language == 'java':
        # Check for proper Java structure
        if full_solution and 'public class' not in full_solution:
            issues.append("Java code missing 'public class' declaration")

        if full_solution and 'public static void main' not in full_solution and 'System.out.println' in full_solution:
            issues.append("Java code has println but no main method")

    # Security checks
    dangerous_patterns = [
        (r'eval\(', 'eval() usage (security risk)'),
        (r'exec\(', 'exec() usage (security risk)'),
        (r'__import__', '__import__ usage (security risk)'),
        (r'Runtime\.getRuntime\(\)\.exec', 'Runtime.exec() usage (security risk)'),
    ]

    for pattern, message in dangerous_patterns:
        if re.search(pattern, full_solution):
            issues.append(f"Security issue: {message}")

    return issues

def check_output_format(lesson):
    """Check expectedOutput format"""
    issues = []
    expected = lesson.get('expectedOutput', '')

    # Check for Windows line endings
    if '\r\n' in expected:
        issues.append("expectedOutput contains Windows line endings (\\r\\n)")

    # Check for trailing whitespace
    lines = expected.split('\n')
    for i, line in enumerate(lines):
        if line != line.rstrip():
            issues.append(f"expectedOutput line {i+1} has trailing whitespace")
            break  # Only report once

    return issues

def check_description_quality(lesson):
    """Check description field quality"""
    issues = []
    description = lesson.get('description', '')

    if len(description) < 20:
        issues.append(f"Description too short ({len(description)} chars)")

    if len(description) > 500:
        issues.append(f"Description too long ({len(description)} chars, consider being more concise)")

    # Check for HTML tags in description (should be plain text)
    if '<' in description and '>' in description:
        issues.append("Description contains HTML tags (should be plain text)")

    return issues

def check_lesson_continuity(lessons):
    """Check for ID gaps and duplicates"""
    issues = []
    ids_seen = set()
    prev_id = 0

    for lesson in lessons:
        lesson_id = lesson.get('id')

        # Check for duplicate IDs
        if lesson_id in ids_seen:
            issues.append({
                'id': lesson_id,
                'title': lesson.get('title'),
                'issue': 'Duplicate lesson ID'
            })

        ids_seen.add(lesson_id)

        # Check for ID continuity
        if lesson_id != prev_id + 1:
            issues.append({
                'id': lesson_id,
                'title': lesson.get('title'),
                'issue': f'ID gap or out of order (expected {prev_id + 1}, got {lesson_id})'
            })

        prev_id = lesson_id

    return issues

def analyze_lessons(file_path, language):
    """Analyze all lessons in a file"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}Quality Check: {language.upper()} lessons{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}File: {file_path}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lessons = json.load(f)
    except Exception as e:
        print(f"{Colors.RED}Error loading file: {e}{Colors.RESET}")
        return

    # Handle both array and object with lessons array
    if isinstance(lessons, dict) and 'lessons' in lessons:
        lessons = lessons['lessons']

    if not isinstance(lessons, list):
        print(f"{Colors.RED}Invalid file format: expected array of lessons{Colors.RESET}")
        return

    print(f"Analyzing {Colors.BOLD}{len(lessons)}{Colors.RESET} lessons...\n")

    # First, check continuity issues
    print(f"{Colors.BOLD}Checking ID continuity...{Colors.RESET}")
    continuity_issues = check_lesson_continuity(lessons)
    if continuity_issues:
        print(f"{Colors.RED}Found {len(continuity_issues)} continuity issues:{Colors.RESET}")
        for issue in continuity_issues[:10]:  # Show first 10
            print(f"  {Colors.YELLOW}Lesson {issue['id']}: {issue['issue']}{Colors.RESET}")
        if len(continuity_issues) > 10:
            print(f"  ... and {len(continuity_issues) - 10} more")
    else:
        print(f"{Colors.GREEN}✓ No continuity issues found{Colors.RESET}")
    print()

    # Check individual lessons
    total_issues = 0
    lessons_with_issues = 0
    issue_categories = {
        'required_fields': 0,
        'title_format': 0,
        'tutorial_quality': 0,
        'code_quality': 0,
        'output_format': 0,
        'description': 0
    }

    problematic_lessons = []

    for lesson in lessons:
        lesson_id = lesson.get('id', 'unknown')
        title = lesson.get('title', 'Unknown')
        lesson_issues = []

        # Run all checks
        checks = [
            ('required_fields', check_required_fields(lesson)),
            ('title_format', check_title_format(lesson)),
            ('tutorial_quality', check_tutorial_quality(lesson)),
            ('code_quality', check_code_quality(lesson, language)),
            ('output_format', check_output_format(lesson)),
            ('description', check_description_quality(lesson))
        ]

        for category, issues in checks:
            if issues:
                issue_categories[category] += len(issues)
                lesson_issues.extend(issues)

        if lesson_issues:
            lessons_with_issues += 1
            total_issues += len(lesson_issues)
            problematic_lessons.append({
                'id': lesson_id,
                'title': title,
                'issues': lesson_issues
            })

    # Summary
    print(f"{Colors.BOLD}Issue Summary by Category:{Colors.RESET}")
    for category, count in issue_categories.items():
        color = Colors.GREEN if count == 0 else Colors.YELLOW if count < 10 else Colors.RED
        print(f"  {color}{category.replace('_', ' ').title():20s}: {count:4d}{Colors.RESET}")

    print(f"\n{Colors.BOLD}Overall Statistics:{Colors.RESET}")
    print(f"  Total Lessons: {len(lessons)}")
    print(f"  Lessons with Issues: {lessons_with_issues} ({100*lessons_with_issues//len(lessons)}%)")
    print(f"  Total Issues: {total_issues}")

    # Show most problematic lessons
    if problematic_lessons:
        print(f"\n{Colors.BOLD}Most Problematic Lessons (showing first 20):{Colors.RESET}")
        sorted_lessons = sorted(problematic_lessons, key=lambda x: len(x['issues']), reverse=True)[:20]
        for lesson in sorted_lessons:
            print(f"\n{Colors.RED}Lesson {lesson['id']}: {lesson['title'][:60]}{Colors.RESET}")
            print(f"  {Colors.YELLOW}{len(lesson['issues'])} issues:{Colors.RESET}")
            for issue in lesson['issues'][:5]:  # Show first 5 issues
                print(f"    • {issue}")
            if len(lesson['issues']) > 5:
                print(f"    ... and {len(lesson['issues']) - 5} more")

    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")

    return {
        'total_lessons': len(lessons),
        'lessons_with_issues': lessons_with_issues,
        'total_issues': total_issues,
        'issue_categories': issue_categories,
        'problematic_lessons': problematic_lessons
    }

def main():
    script_dir = Path(__file__).parent
    public_dir = script_dir.parent / 'public'

    python_file = public_dir / 'lessons-python.json'
    java_file = public_dir / 'lessons-java.json'

    results = {}

    # Analyze Python lessons
    if python_file.exists():
        results['python'] = analyze_lessons(python_file, 'python')
    else:
        print(f"{Colors.YELLOW}Warning: {python_file} not found{Colors.RESET}")

    # Analyze Java lessons
    if java_file.exists():
        results['java'] = analyze_lessons(java_file, 'java')
    else:
        print(f"{Colors.YELLOW}Warning: {java_file} not found{Colors.RESET}")

    # Save report
    report_file = script_dir.parent / 'quality_report.json'
    # Convert to JSON-serializable format
    json_results = {
        lang: {
            'total_lessons': r['total_lessons'],
            'lessons_with_issues': r['lessons_with_issues'],
            'total_issues': r['total_issues'],
            'issue_categories': r['issue_categories'],
            'problematic_lessons': r['problematic_lessons'][:50]  # Limit to 50
        }
        for lang, r in results.items()
    }

    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(json_results, f, indent=2, ensure_ascii=False)

    print(f"{Colors.CYAN}Quality report saved to: {report_file}{Colors.RESET}\n")

if __name__ == '__main__':
    main()
