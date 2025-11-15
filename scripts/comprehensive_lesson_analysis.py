#!/usr/bin/env python3
"""
Comprehensive lesson quality and compilation analysis for Java and Python lessons.
This script:
- Validates lesson structure
- Tests Java code compilation
- Tests Python code syntax
- Assesses tutorial quality
- Provides coverage analysis
"""

import json
import os
import subprocess
import tempfile
import sys
from pathlib import Path
from collections import defaultdict, Counter

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*80}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text:^80}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*80}{Colors.ENDC}\n")


def print_section(text):
    print(f"\n{Colors.OKBLUE}{Colors.BOLD}{text}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'-'*len(text)}{Colors.ENDC}")


def load_lessons(filepath):
    """Load lessons from JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and 'lessons' in data:
                return data['lessons']
            else:
                print(f"{Colors.FAIL}Error: Unexpected JSON structure in {filepath}{Colors.ENDC}")
                return []
    except Exception as e:
        print(f"{Colors.FAIL}Error loading {filepath}: {e}{Colors.ENDC}")
        return []


def test_java_compilation(code, lesson_id):
    """Test if Java code compiles."""
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            # Write Java file
            java_file = os.path.join(tmpdir, 'Main.java')
            with open(java_file, 'w', encoding='utf-8') as f:
                f.write(code)

            # Try to compile
            result = subprocess.run(
                ['javac', java_file],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode == 0:
                return True, None
            else:
                return False, result.stderr
    except FileNotFoundError:
        return None, "Java compiler (javac) not found"
    except subprocess.TimeoutExpired:
        return False, "Compilation timeout"
    except Exception as e:
        return False, str(e)


def test_python_syntax(code, lesson_id):
    """Test if Python code has valid syntax."""
    try:
        compile(code, f'<lesson_{lesson_id}>', 'exec')
        return True, None
    except SyntaxError as e:
        return False, f"Line {e.lineno}: {e.msg}"
    except Exception as e:
        return False, str(e)


def analyze_tutorial_quality(tutorial):
    """Analyze tutorial content quality."""
    if not tutorial or not isinstance(tutorial, str):
        return {
            'has_content': False,
            'length': 0,
            'has_code_examples': False,
            'has_sections': False,
            'plain_text_length': 0
        }

    # Remove HTML tags to get plain text length
    import re
    plain_text = re.sub(r'<[^>]+>', '', tutorial)
    plain_text = plain_text.strip()

    return {
        'has_content': len(plain_text) > 0,
        'length': len(tutorial),
        'plain_text_length': len(plain_text),
        'has_code_examples': '<pre' in tutorial or '<code' in tutorial,
        'has_sections': tutorial.count('<h') >= 2,  # At least 2 section headers
        'is_substantial': len(plain_text) >= 200  # At least 200 chars of content
    }


def analyze_lessons(filepath, language):
    """Comprehensive analysis of lessons."""
    print_header(f"{language.upper()} LESSONS ANALYSIS")

    lessons = load_lessons(filepath)
    if not lessons:
        print(f"{Colors.FAIL}No lessons found in {filepath}{Colors.ENDC}")
        return None

    print(f"{Colors.OKGREEN}Loaded {len(lessons)} lessons{Colors.ENDC}")

    # Statistics
    stats = {
        'total': len(lessons),
        'compilation_pass': 0,
        'compilation_fail': 0,
        'compilation_unknown': 0,
        'compilation_errors': [],
        'missing_fields': [],
        'quality_issues': [],
        'difficulty_distribution': Counter(),
        'category_distribution': Counter(),
        'tag_distribution': Counter(),
        'tutorial_quality': {
            'with_content': 0,
            'with_code_examples': 0,
            'with_sections': 0,
            'substantial': 0
        }
    }

    # Required fields
    required_fields = ['id', 'title', 'description', 'fullSolution', 'expectedOutput', 'tutorial', 'language']

    print_section("Validating Structure and Testing Compilation...")

    for i, lesson in enumerate(lessons):
        lesson_id = lesson.get('id', f'unknown_{i}')

        # Check required fields
        missing = [field for field in required_fields if field not in lesson or not lesson[field]]
        if missing:
            stats['missing_fields'].append({
                'id': lesson_id,
                'title': lesson.get('title', 'N/A'),
                'missing': missing
            })

        # Test compilation/syntax
        code = lesson.get('fullSolution', '')
        if code:
            if language.lower() == 'java':
                success, error = test_java_compilation(code, lesson_id)
            else:  # Python
                success, error = test_python_syntax(code, lesson_id)

            if success is None:
                stats['compilation_unknown'] += 1
            elif success:
                stats['compilation_pass'] += 1
            else:
                stats['compilation_fail'] += 1
                stats['compilation_errors'].append({
                    'id': lesson_id,
                    'title': lesson.get('title', 'N/A'),
                    'error': error
                })

        # Analyze tutorial quality
        tutorial = lesson.get('tutorial', '')
        quality = analyze_tutorial_quality(tutorial)
        if quality['has_content']:
            stats['tutorial_quality']['with_content'] += 1
        if quality['has_code_examples']:
            stats['tutorial_quality']['with_code_examples'] += 1
        if quality['has_sections']:
            stats['tutorial_quality']['with_sections'] += 1
        if quality['is_substantial']:
            stats['tutorial_quality']['substantial'] += 1

        if not quality['is_substantial']:
            stats['quality_issues'].append({
                'id': lesson_id,
                'title': lesson.get('title', 'N/A'),
                'issue': 'Tutorial too short or missing',
                'length': quality['plain_text_length']
            })

        # Collect distribution data
        if 'difficulty' in lesson:
            stats['difficulty_distribution'][lesson['difficulty']] += 1
        if 'category' in lesson:
            stats['category_distribution'][lesson['category']] += 1
        if 'tags' in lesson and isinstance(lesson['tags'], list):
            for tag in lesson['tags']:
                stats['tag_distribution'][tag] += 1

        # Progress indicator
        if (i + 1) % 100 == 0:
            print(f"  Processed {i + 1}/{len(lessons)} lessons...", end='\r')

    print(f"  Processed {len(lessons)}/{len(lessons)} lessons - Complete!   ")

    return stats


def print_report(java_stats, python_stats):
    """Print comprehensive report."""
    print_header("COMPREHENSIVE QUALITY REPORT")

    for lang, stats in [('Java', java_stats), ('Python', python_stats)]:
        if not stats:
            continue

        print_section(f"{lang} Lessons Summary")

        print(f"\n{Colors.BOLD}Total Lessons:{Colors.ENDC} {stats['total']}")

        # Compilation results
        print(f"\n{Colors.BOLD}Compilation/Syntax Check:{Colors.ENDC}")
        total_tested = stats['compilation_pass'] + stats['compilation_fail']
        if total_tested > 0:
            pass_rate = (stats['compilation_pass'] / total_tested) * 100
            color = Colors.OKGREEN if pass_rate >= 95 else Colors.WARNING if pass_rate >= 80 else Colors.FAIL
            print(f"  {Colors.OKGREEN}[PASS] Passed:{Colors.ENDC} {stats['compilation_pass']}")
            print(f"  {Colors.FAIL}[FAIL] Failed:{Colors.ENDC} {stats['compilation_fail']}")
            print(f"  {color}Pass Rate: {pass_rate:.1f}%{Colors.ENDC}")
        if stats['compilation_unknown'] > 0:
            print(f"  {Colors.WARNING}? Unknown:{Colors.ENDC} {stats['compilation_unknown']} (compiler not available)")

        # Show compilation errors if any
        if stats['compilation_errors']:
            print(f"\n{Colors.BOLD}Compilation/Syntax Errors (showing first 10):{Colors.ENDC}")
            for error in stats['compilation_errors'][:10]:
                print(f"  {Colors.FAIL}Lesson {error['id']}: {error['title']}{Colors.ENDC}")
                print(f"    {error['error'][:200]}")

        # Missing fields
        if stats['missing_fields']:
            print(f"\n{Colors.BOLD}Missing Required Fields:{Colors.ENDC}")
            print(f"  {Colors.WARNING}{len(stats['missing_fields'])} lessons with missing fields{Colors.ENDC}")
            for item in stats['missing_fields'][:5]:
                print(f"  Lesson {item['id']}: Missing {', '.join(item['missing'])}")

        # Tutorial quality
        print(f"\n{Colors.BOLD}Tutorial Quality:{Colors.ENDC}")
        total = stats['total']
        print(f"  With content: {stats['tutorial_quality']['with_content']}/{total} ({stats['tutorial_quality']['with_content']/total*100:.1f}%)")
        print(f"  With code examples: {stats['tutorial_quality']['with_code_examples']}/{total} ({stats['tutorial_quality']['with_code_examples']/total*100:.1f}%)")
        print(f"  With multiple sections: {stats['tutorial_quality']['with_sections']}/{total} ({stats['tutorial_quality']['with_sections']/total*100:.1f}%)")
        print(f"  Substantial content: {stats['tutorial_quality']['substantial']}/{total} ({stats['tutorial_quality']['substantial']/total*100:.1f}%)")

        # Quality issues
        if stats['quality_issues']:
            print(f"\n{Colors.WARNING}Quality Issues: {len(stats['quality_issues'])} lessons with short tutorials{Colors.ENDC}")

        # Difficulty distribution
        print(f"\n{Colors.BOLD}Difficulty Distribution:{Colors.ENDC}")
        for difficulty, count in sorted(stats['difficulty_distribution'].items()):
            print(f"  {difficulty}: {count}")

        # Category distribution
        print(f"\n{Colors.BOLD}Category Distribution:{Colors.ENDC}")
        for category, count in sorted(stats['category_distribution'].most_common(10)):
            print(f"  {category}: {count}")

        # Top tags
        print(f"\n{Colors.BOLD}Top 15 Tags:{Colors.ENDC}")
        for tag, count in stats['tag_distribution'].most_common(15):
            print(f"  {tag}: {count}")

        print()

    # Overall summary
    print_section("Overall Summary")
    if java_stats and python_stats:
        total_lessons = java_stats['total'] + python_stats['total']
        total_pass = java_stats['compilation_pass'] + python_stats['compilation_pass']
        total_fail = java_stats['compilation_fail'] + python_stats['compilation_fail']

        print(f"\n{Colors.BOLD}Combined Statistics:{Colors.ENDC}")
        print(f"  Total lessons: {total_lessons}")
        print(f"  Compilation pass: {total_pass}")
        print(f"  Compilation fail: {total_fail}")
        if total_pass + total_fail > 0:
            overall_rate = (total_pass / (total_pass + total_fail)) * 100
            color = Colors.OKGREEN if overall_rate >= 95 else Colors.WARNING if overall_rate >= 80 else Colors.FAIL
            print(f"  {color}Overall pass rate: {overall_rate:.1f}%{Colors.ENDC}")


def main():
    """Main entry point."""
    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    java_file = project_root / 'public' / 'lessons-java.json'
    python_file = project_root / 'public' / 'lessons-python.json'

    # Analyze both languages
    java_stats = analyze_lessons(java_file, 'Java')
    python_stats = analyze_lessons(python_file, 'Python')

    # Print comprehensive report
    print_report(java_stats, python_stats)

    # Exit with error if there are critical issues
    critical_issues = 0
    if java_stats:
        critical_issues += java_stats['compilation_fail']
    if python_stats:
        critical_issues += python_stats['compilation_fail']

    if critical_issues > 0:
        print(f"\n{Colors.WARNING}Warning: {critical_issues} lessons have compilation/syntax errors{Colors.ENDC}")
        return 1
    else:
        print(f"\n{Colors.OKGREEN}All lessons passed compilation/syntax checks!{Colors.ENDC}")
        return 0


if __name__ == '__main__':
    sys.exit(main())
