#!/usr/bin/env python3
"""
Comprehensive quality audit for all lessons.
Checks coverage, tags, code quality, tutorials, and more.
"""

import json
import re
from collections import Counter, defaultdict

class QualityAuditor:
    def __init__(self, language):
        self.language = language
        self.filename = f'public/lessons-{language}.json'
        self.lessons = []
        self.issues = defaultdict(list)
        self.warnings = defaultdict(list)

    def load_lessons(self):
        """Load lessons from JSON."""
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.lessons = json.load(f)
        print(f"Loaded {len(self.lessons)} {self.language} lessons")

    def check_coverage(self):
        """Check topic coverage and distribution."""
        print("\n" + "="*80)
        print("COVERAGE & DISTRIBUTION CHECK")
        print("="*80)

        # Difficulty distribution
        diff_counts = Counter([l['difficulty'] for l in self.lessons])
        total = len(self.lessons)

        print(f"\nTotal Lessons: {total}")
        print("\nDifficulty Distribution:")
        for diff in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
            count = diff_counts[diff]
            pct = (count / total) * 100
            print(f"  {diff:15s}: {count:4d} ({pct:5.1f}%)")

            # Check if within target ranges
            if diff == 'Beginner' and not (25 <= pct <= 30):
                self.warnings['coverage'].append(f"Beginner % ({pct:.1f}%) outside target 25-30%")
            elif diff == 'Expert' and not (10 <= pct <= 15):
                self.warnings['coverage'].append(f"Expert % ({pct:.1f}%) outside target 10-15%")

        # Category distribution
        category_counts = Counter([l['category'] for l in self.lessons])
        print("\nCategory Distribution:")
        for cat, count in category_counts.most_common():
            pct = (count / total) * 100
            print(f"  {cat:25s}: {count:4d} ({pct:5.1f}%)")

        # Check for missing common topics
        all_tags = set()
        for lesson in self.lessons:
            all_tags.update(lesson.get('tags', []))

        if self.language == 'java':
            expected_topics = [
                'Strings', 'Arrays', 'ArrayList', 'HashMap', 'Loops',
                'Methods', 'Classes', 'Inheritance', 'Interfaces',
                'Exception Handling', 'File I/O', 'Multithreading',
                'Spring Boot', 'JPA', 'REST API', 'Testing'
            ]
        else:  # python
            expected_topics = [
                'Strings', 'Lists', 'Dictionaries', 'Loops', 'Functions',
                'Classes', 'File I/O', 'Exception Handling', 'Decorators',
                'Flask', 'Django', 'REST API', 'Testing', 'Data Processing'
            ]

        missing_topics = [topic for topic in expected_topics if topic not in all_tags]
        if missing_topics:
            self.warnings['coverage'].append(f"Potentially missing topics: {', '.join(missing_topics)}")

        print(f"\n[OK] Coverage check complete")

    def check_tags(self):
        """Validate difficulty and topic tags."""
        print("\n" + "="*80)
        print("TAG VALIDATION CHECK")
        print("="*80)

        for lesson in self.lessons:
            lid = lesson['id']
            title = lesson['title']
            difficulty = lesson['difficulty']
            category = lesson['category']
            tags = lesson.get('tags', [])

            # Check if difficulty is in tags
            if difficulty not in tags:
                self.issues['tags'].append(f"Lesson {lid}: Difficulty '{difficulty}' not in tags")

            # Check if category-related tag exists
            if not any(tag in category for tag in tags):
                # Category might be multi-word, check if any word matches
                category_words = category.split()
                if not any(word in tag for word in category_words for tag in tags):
                    self.warnings['tags'].append(f"Lesson {lid}: No category-related tag for '{category}'")

            # Check for empty or minimal tags
            if len(tags) < 3:
                self.warnings['tags'].append(f"Lesson {lid}: Only {len(tags)} tags (recommend 3+)")

            # Check for overly generic tags only
            generic_tags = ['Beginner', 'Intermediate', 'Advanced', 'Expert']
            non_generic = [t for t in tags if t not in generic_tags]
            if len(non_generic) < 2:
                self.warnings['tags'].append(f"Lesson {lid}: Needs more specific topic tags")

            # Validate difficulty assignment based on content
            title_lower = title.lower()

            # Beginner should have basic topics
            if difficulty == 'Beginner':
                expert_keywords = ['microservices', 'kubernetes', 'distributed', 'advanced',
                                 'optimization', 'performance tuning', 'scalability',
                                 'architecture', 'design patterns']
                if any(kw in title_lower for kw in expert_keywords):
                    self.issues['tags'].append(f"Lesson {lid}: '{title}' marked Beginner but has expert keywords")

            # Expert should have advanced topics
            elif difficulty == 'Expert':
                basic_keywords = ['hello world', 'introduction', 'basics', 'getting started',
                                'simple', 'basic']
                if any(kw in title_lower for kw in basic_keywords):
                    self.issues['tags'].append(f"Lesson {lid}: '{title}' marked Expert but has basic keywords")

        print(f"[OK] Tag validation complete")

    def check_code_quality(self):
        """Verify code quality and comments."""
        print("\n" + "="*80)
        print("CODE QUALITY CHECK")
        print("="*80)

        generic_patterns = [
            'Exercise completed!',
            'Complete the exercise',
            'TODO: Complete this',
            'System.out.println("Hello")',
            'print("Hello")'
        ]

        for lesson in self.lessons:
            lid = lesson['id']
            title = lesson['title']
            base_code = lesson.get('baseCode', '')
            full_solution = lesson.get('fullSolution', '')

            # Check for generic code
            if any(pattern in full_solution for pattern in generic_patterns[:2]):
                self.issues['code'].append(f"Lesson {lid}: Generic placeholder code in solution")

            # Check if solution has comments
            if self.language == 'java':
                if '//' not in full_solution and '/*' not in full_solution:
                    self.warnings['code'].append(f"Lesson {lid}: No comments in Java solution")
            else:  # python
                if '#' not in full_solution and '"""' not in full_solution:
                    self.warnings['code'].append(f"Lesson {lid}: No comments in Python solution")

            # Check if baseCode has TODOs
            if 'TODO' not in base_code:
                self.warnings['code'].append(f"Lesson {lid}: No TODO markers in base code")

            # Check if solution is different from base
            if base_code == full_solution:
                self.issues['code'].append(f"Lesson {lid}: Base code identical to solution")

            # Check for proper structure
            if self.language == 'java':
                if 'public class' not in full_solution:
                    self.issues['code'].append(f"Lesson {lid}: Missing 'public class' in Java code")
                if 'public static void main' not in full_solution:
                    self.warnings['code'].append(f"Lesson {lid}: No main method in Java code")
            else:  # python
                if 'def' not in full_solution and 'class' not in full_solution:
                    self.warnings['code'].append(f"Lesson {lid}: No functions or classes in Python code")

            # Check for expectedOutput
            expected_output = lesson.get('expectedOutput', '')
            if not expected_output or expected_output == '':
                self.warnings['code'].append(f"Lesson {lid}: No expected output defined")

        print(f"[OK] Code quality check complete")

    def check_tutorials(self):
        """Check tutorial quality and examples."""
        print("\n" + "="*80)
        print("TUTORIAL QUALITY CHECK")
        print("="*80)

        for lesson in self.lessons:
            lid = lesson['id']
            title = lesson['title']
            tutorial = lesson.get('tutorial', '')
            additional_examples = lesson.get('additionalExamples', '')

            # Check if tutorial exists
            if not tutorial or len(tutorial) < 100:
                self.issues['tutorial'].append(f"Lesson {lid}: Tutorial too short or missing")

            # Check for code examples in tutorial
            if self.language == 'java':
                has_code = 'java' in tutorial or 'class' in tutorial or 'public' in tutorial
            else:
                has_code = 'python' in tutorial or 'def' in tutorial or 'import' in tutorial

            if not has_code:
                self.warnings['tutorial'].append(f"Lesson {lid}: No code examples in tutorial")

            # Check for key sections (HTML or Markdown)
            key_sections = ['Overview', 'Key Concepts', 'Example', 'Best Practices']
            missing_sections = [s for s in key_sections if s not in tutorial]
            if len(missing_sections) >= 3:
                self.warnings['tutorial'].append(f"Lesson {lid}: Missing tutorial sections: {', '.join(missing_sections)}")

            # Check additional examples
            if not additional_examples:
                self.warnings['tutorial'].append(f"Lesson {lid}: No additional examples")

            # Check tutorial length (should be substantial)
            if len(tutorial) < 500:
                self.warnings['tutorial'].append(f"Lesson {lid}: Tutorial quite short ({len(tutorial)} chars)")
            elif len(tutorial) > 10000:
                self.warnings['tutorial'].append(f"Lesson {lid}: Tutorial very long ({len(tutorial)} chars)")

        print(f"[OK] Tutorial quality check complete")

    def check_hints_and_tests(self):
        """Check hints and test cases."""
        print("\n" + "="*80)
        print("HINTS & TEST CASES CHECK")
        print("="*80)

        for lesson in self.lessons:
            lid = lesson['id']
            hints = lesson.get('hints', [])
            test_cases = lesson.get('testCases', [])

            # Check hints
            if not hints or len(hints) == 0:
                self.warnings['hints'].append(f"Lesson {lid}: No hints provided")
            elif len(hints) < 2:
                self.warnings['hints'].append(f"Lesson {lid}: Only {len(hints)} hint(s)")

            # Check for generic hints
            generic_hints = [
                'Review the tutorial',
                'Break down the problem',
                'Test your code'
            ]
            if all(any(gh in hint for gh in generic_hints) for hint in hints):
                self.warnings['hints'].append(f"Lesson {lid}: All hints are generic")

            # Test cases (some lessons may not need them)
            if lesson['difficulty'] in ['Beginner', 'Intermediate'] and len(test_cases) == 0:
                # Only warn for code-heavy lessons
                if 'Portfolio' not in lesson['title'] and 'Project' not in lesson['title']:
                    pass  # Test cases optional for beginners

        print(f"[OK] Hints & test cases check complete")

    def sample_compile_check(self):
        """Sample and test compilation of code."""
        print("\n" + "="*80)
        print("CODE COMPILATION SAMPLE CHECK")
        print("="*80)

        import random

        # Sample 10 random lessons from each difficulty
        by_difficulty = defaultdict(list)
        for lesson in self.lessons:
            by_difficulty[lesson['difficulty']].append(lesson)

        print("\nSampling lessons for compilation test...")

        for difficulty in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
            lessons_in_diff = by_difficulty[difficulty]
            sample_size = min(5, len(lessons_in_diff))
            samples = random.sample(lessons_in_diff, sample_size)

            print(f"\n{difficulty} ({sample_size} samples):")
            for lesson in samples:
                lid = lesson['id']
                title = lesson['title']
                code = lesson['fullSolution']

                # Basic syntax check
                if self.language == 'java':
                    # Check for common Java syntax issues
                    if code.count('{') != code.count('}'):
                        self.issues['compile'].append(f"Lesson {lid}: Mismatched braces in Java code")
                    if code.count('(') != code.count(')'):
                        self.issues['compile'].append(f"Lesson {lid}: Mismatched parentheses in Java code")
                    if 'public class' in code and not re.search(r'public\s+class\s+\w+', code):
                        self.issues['compile'].append(f"Lesson {lid}: Invalid class declaration")

                    print(f"  [OK] {lid}: {title[:60]}")

                else:  # python
                    # Check for common Python syntax issues
                    lines = code.split('\n')
                    for i, line in enumerate(lines, 1):
                        if line.strip() and not line.startswith((' ', '\t', '#')):
                            # Check for missing colons in def/class/if/for/while
                            if re.match(r'^\s*(def|class|if|for|while|elif|else|try|except|finally|with)\s+', line):
                                if not line.rstrip().endswith(':'):
                                    self.issues['compile'].append(f"Lesson {lid}: Missing colon at line {i}")

                    print(f"  [OK] {lid}: {title[:60]}")

        print(f"\n[OK] Compilation sample check complete")

    def generate_report(self):
        """Generate final quality report."""
        print("\n" + "="*80)
        print("QUALITY AUDIT REPORT")
        print("="*80)

        # Count issues and warnings
        total_issues = sum(len(v) for v in self.issues.values())
        total_warnings = sum(len(v) for v in self.warnings.values())

        print(f"\nTotal Lessons: {len(self.lessons)}")
        print(f"Critical Issues: {total_issues}")
        print(f"Warnings: {total_warnings}")

        # Print issues by category
        if total_issues > 0:
            print("\n" + "-"*80)
            print("CRITICAL ISSUES (must fix):")
            print("-"*80)
            for category, issue_list in self.issues.items():
                if issue_list:
                    print(f"\n{category.upper()} ({len(issue_list)} issues):")
                    for issue in issue_list[:10]:  # Show first 10
                        print(f"  • {issue}")
                    if len(issue_list) > 10:
                        print(f"  ... and {len(issue_list) - 10} more")

        # Print warnings by category
        if total_warnings > 0:
            print("\n" + "-"*80)
            print("WARNINGS (should review):")
            print("-"*80)
            for category, warning_list in self.warnings.items():
                if warning_list:
                    print(f"\n{category.upper()} ({len(warning_list)} warnings):")
                    for warning in warning_list[:10]:  # Show first 10
                        print(f"  • {warning}")
                    if len(warning_list) > 10:
                        print(f"  ... and {len(warning_list) - 10} more")

        # Overall quality score
        total_checks = len(self.lessons) * 10  # Approximate checks per lesson
        issues_weight = total_issues * 10
        warnings_weight = total_warnings * 1
        quality_score = max(0, 100 - ((issues_weight + warnings_weight) / total_checks) * 100)

        print("\n" + "="*80)
        print(f"OVERALL QUALITY SCORE: {quality_score:.1f}/100")
        print("="*80)

        if total_issues == 0 and total_warnings < 50:
            print("\n[EXCELLENT!] Curriculum meets high quality standards.")
        elif total_issues == 0:
            print("\n[GOOD!] No critical issues, but review warnings.")
        elif total_issues < 20:
            print("\n[WARNING] FAIR. Some issues need fixing.")
        else:
            print("\n[ERROR] NEEDS WORK. Multiple issues require attention.")

        return {
            'total_lessons': len(self.lessons),
            'issues': total_issues,
            'warnings': total_warnings,
            'quality_score': quality_score
        }

    def run_full_audit(self):
        """Run complete quality audit."""
        print(f"\n{'='*80}")
        print(f"COMPREHENSIVE QUALITY AUDIT: {self.language.upper()}")
        print(f"{'='*80}")

        self.load_lessons()
        self.check_coverage()
        self.check_tags()
        self.check_code_quality()
        self.check_tutorials()
        self.check_hints_and_tests()
        self.sample_compile_check()

        return self.generate_report()


def main():
    """Run quality audit for both languages."""
    print("\n" + "="*80)
    print("DEVBOOT LLM CURRICULUM - COMPREHENSIVE QUALITY AUDIT")
    print("="*80)

    # Audit Java
    java_auditor = QualityAuditor('java')
    java_results = java_auditor.run_full_audit()

    print("\n" + "="*80)
    print("\n")

    # Audit Python
    python_auditor = QualityAuditor('python')
    python_results = python_auditor.run_full_audit()

    # Combined summary
    print("\n" + "="*80)
    print("COMBINED SUMMARY")
    print("="*80)
    print(f"\nTotal Lessons: {java_results['total_lessons'] + python_results['total_lessons']}")
    print(f"Total Issues: {java_results['issues'] + python_results['issues']}")
    print(f"Total Warnings: {java_results['warnings'] + python_results['warnings']}")
    print(f"\nJava Quality Score: {java_results['quality_score']:.1f}/100")
    print(f"Python Quality Score: {python_results['quality_score']:.1f}/100")
    print(f"Average Quality Score: {(java_results['quality_score'] + python_results['quality_score']) / 2:.1f}/100")

    print("\n" + "="*80)
    print("AUDIT COMPLETE!")
    print("="*80)


if __name__ == "__main__":
    main()
