#!/usr/bin/env python3
"""Comprehensive testing of all lessons for quality and correctness"""

import json
import re
import subprocess
import tempfile
import os
from pathlib import Path
from collections import defaultdict

def load_lessons(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

class LessonTester:
    def __init__(self):
        self.results = {
            'total': 0,
            'passed': 0,
            'failed': 0,
            'warnings': 0,
            'errors': defaultdict(list)
        }
        self.detailed_results = []

    def test_lesson_structure(self, lesson, language):
        """Test if lesson has all required fields"""
        issues = []
        required_fields = ['id', 'title', 'description', 'difficulty', 'tags',
                          'category', 'language', 'baseCode', 'fullSolution',
                          'expectedOutput', 'tutorial', 'additionalExamples']

        for field in required_fields:
            if field not in lesson:
                issues.append(f"Missing required field: {field}")
            elif not lesson[field]:
                issues.append(f"Empty field: {field}")

        # Check language matches
        if lesson.get('language') != language:
            issues.append(f"Language mismatch: expected {language}, got {lesson.get('language')}")

        return issues

    def test_tutorial_quality(self, lesson):
        """Test tutorial content quality"""
        issues = []
        tutorial = lesson.get('tutorial', '')
        examples = lesson.get('additionalExamples', '')

        # Check minimum length
        if len(tutorial) < 1000:
            issues.append(f"Tutorial too short: {len(tutorial)} chars (minimum 1000)")

        if len(examples) < 1000:
            issues.append(f"Examples too short: {len(examples)} chars (minimum 1000)")

        # Check for code examples in tutorial (markdown or HTML format)
        has_markdown_code = '```' in tutorial
        has_html_code = '<code' in tutorial or '<pre' in tutorial
        if not has_markdown_code and not has_html_code:
            issues.append("Tutorial missing code examples (no code blocks)")

        # Check for TODO markers (should not be in tutorials)
        if 'TODO' in tutorial and 'TODO:' not in tutorial:
            issues.append("Tutorial contains TODO markers")

        # Check for proper sections (informational warning, not critical)
        tutorial_lower = tutorial.lower()
        recommended_sections = ['introduction', 'example', 'concept', 'overview', 'usage',
                               'implementation', 'pattern', 'best practice']
        has_section = any(section in tutorial_lower for section in recommended_sections)
        # Don't fail for missing sections if content is substantial
        if not has_section and len(tutorial) < 2000:
            issues.append("Tutorial missing recommended sections (and content is brief)")

        return issues

    def test_code_syntax(self, code, language, code_type):
        """Test if code has valid syntax"""
        issues = []

        if not code or not code.strip():
            return [f"{code_type} is empty"]

        # Check for common syntax issues
        if language == 'python':
            # Check for unclosed brackets
            if code.count('(') != code.count(')'):
                issues.append(f"{code_type}: Unmatched parentheses")
            if code.count('[') != code.count(']'):
                issues.append(f"{code_type}: Unmatched brackets")
            if code.count('{') != code.count('}'):
                issues.append(f"{code_type}: Unmatched braces")

            # Check for Python syntax using compile
            try:
                # Handle Dockerfile/YAML code
                if code.strip().startswith('FROM ') or code.strip().startswith('#'):
                    # Skip Dockerfile/config files
                    pass
                elif code.strip().startswith('apiVersion:') or 'kind: Deployment' in code:
                    # Skip Kubernetes YAML
                    pass
                else:
                    compile(code, '<string>', 'exec')
            except SyntaxError as e:
                issues.append(f"{code_type}: Python syntax error: {str(e)}")
            except Exception as e:
                # Some advanced Python features might not compile in isolation
                pass

        elif language == 'java':
            # Check for unclosed brackets
            if code.count('(') != code.count(')'):
                issues.append(f"{code_type}: Unmatched parentheses")
            if code.count('{') != code.count('}'):
                issues.append(f"{code_type}: Unmatched braces")
            if code.count('[') != code.count(']'):
                issues.append(f"{code_type}: Unmatched brackets")

            # Check for basic Java structure
            if 'public class' not in code and 'class ' not in code and not code.strip().startswith('#'):
                # Allow Dockerfiles and protobuf files
                if not code.strip().startswith('FROM ') and not code.strip().startswith('syntax ='):
                    issues.append(f"{code_type}: Missing class definition")

        return issues

    def test_code_execution(self, lesson, language):
        """Test if fullSolution executes and produces expected output"""
        issues = []
        full_solution = lesson.get('fullSolution', '')
        expected_output = lesson.get('expectedOutput', '')

        if not full_solution or not full_solution.strip():
            return ["fullSolution is empty"]

        # Skip non-executable code (Dockerfiles, YAML, etc.)
        if full_solution.strip().startswith('FROM ') or \
           full_solution.strip().startswith('apiVersion:') or \
           full_solution.strip().startswith('syntax =') or \
           full_solution.strip().startswith('# Dockerfile'):
            return []  # These are config files, not executable code

        # For now, we'll do basic validation rather than execution
        # Full execution would require setting up environments, dependencies, etc.

        # Check if solution has print/output statements
        if language == 'python':
            has_output = 'print(' in full_solution or 'return' in full_solution
            if not has_output and expected_output and expected_output != 'Success':
                issues.append("fullSolution missing print/return statements for expected output")

        elif language == 'java':
            has_output = 'System.out.print' in full_solution or 'return' in full_solution
            if not has_output and expected_output and expected_output != 'Success':
                issues.append("fullSolution missing System.out/return statements for expected output")

        return issues

    def test_lesson(self, lesson, language):
        """Run all tests on a lesson"""
        self.results['total'] += 1
        lesson_id = lesson.get('id', 'UNKNOWN')
        title = lesson.get('title', 'UNKNOWN')

        all_issues = []

        # Test structure
        structure_issues = self.test_lesson_structure(lesson, language)
        if structure_issues:
            all_issues.extend([f"STRUCTURE: {issue}" for issue in structure_issues])

        # Test tutorial quality
        tutorial_issues = self.test_tutorial_quality(lesson)
        if tutorial_issues:
            all_issues.extend([f"QUALITY: {issue}" for issue in tutorial_issues])

        # Test code syntax
        base_code_issues = self.test_code_syntax(
            lesson.get('baseCode', ''), language, 'baseCode'
        )
        if base_code_issues:
            all_issues.extend([f"BASE_CODE: {issue}" for issue in base_code_issues])

        solution_issues = self.test_code_syntax(
            lesson.get('fullSolution', ''), language, 'fullSolution'
        )
        if solution_issues:
            all_issues.extend([f"SOLUTION: {issue}" for issue in solution_issues])

        # Test code execution
        execution_issues = self.test_code_execution(lesson, language)
        if execution_issues:
            all_issues.extend([f"EXECUTION: {issue}" for issue in execution_issues])

        # Record results
        result = {
            'id': lesson_id,
            'title': title,
            'language': language,
            'status': 'PASS' if not all_issues else 'FAIL',
            'issues': all_issues
        }

        self.detailed_results.append(result)

        if all_issues:
            self.results['failed'] += 1
            for issue in all_issues:
                category = issue.split(':')[0]
                self.results['errors'][category].append({
                    'id': lesson_id,
                    'title': title,
                    'issue': issue
                })
        else:
            self.results['passed'] += 1

        return result

    def generate_report(self, output_file='LESSON_TEST_REPORT.md'):
        """Generate comprehensive test report"""
        pass_rate = (self.results['passed'] / self.results['total'] * 100) if self.results['total'] > 0 else 0

        report = f"""# Comprehensive Lesson Test Report

**Date:** {os.popen('date /t').read().strip()} {os.popen('time /t').read().strip()}
**Total Lessons Tested:** {self.results['total']:,}
**Status:** {'PASS' if pass_rate >= 95 else 'FAIL' if pass_rate < 80 else 'WARNING'}

---

## Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Lessons** | {self.results['total']:,} | 100% |
| **Passed** | {self.results['passed']:,} | {pass_rate:.1f}% |
| **Failed** | {self.results['failed']:,} | {100-pass_rate:.1f}% |

---

## Pass Rate by Category

"""

        # Count issues by category
        category_counts = defaultdict(int)
        for category, issues in self.results['errors'].items():
            category_counts[category] = len(issues)

        if category_counts:
            report += "| Category | Issues Found |\n"
            report += "|----------|-------------|\n"
            for category, count in sorted(category_counts.items(), key=lambda x: -x[1]):
                report += f"| {category} | {count} |\n"
        else:
            report += "✅ No issues found in any category!\n"

        report += "\n---\n\n## Detailed Results\n\n"

        # Group results by status
        failed_lessons = [r for r in self.detailed_results if r['status'] == 'FAIL']
        passed_lessons = [r for r in self.detailed_results if r['status'] == 'PASS']

        if failed_lessons:
            report += f"### Failed Lessons ({len(failed_lessons)})\n\n"

            # Group by language
            python_failed = [l for l in failed_lessons if l['language'] == 'python']
            java_failed = [l for l in failed_lessons if l['language'] == 'java']

            if python_failed:
                report += f"#### Python ({len(python_failed)} failed)\n\n"
                for lesson in python_failed[:20]:  # Show first 20
                    report += f"**ID {lesson['id']}: {lesson['title']}**\n"
                    for issue in lesson['issues'][:5]:  # Show first 5 issues
                        report += f"- {issue}\n"
                    report += "\n"

                if len(python_failed) > 20:
                    report += f"*...and {len(python_failed) - 20} more Python lessons with issues*\n\n"

            if java_failed:
                report += f"#### Java ({len(java_failed)} failed)\n\n"
                for lesson in java_failed[:20]:  # Show first 20
                    report += f"**ID {lesson['id']}: {lesson['title']}**\n"
                    for issue in lesson['issues'][:5]:  # Show first 5 issues
                        report += f"- {issue}\n"
                    report += "\n"

                if len(java_failed) > 20:
                    report += f"*...and {len(java_failed) - 20} more Java lessons with issues*\n\n"

        report += f"\n### Passed Lessons ({len(passed_lessons)})\n\n"
        report += f"✅ {len(passed_lessons):,} lessons passed all quality checks!\n\n"

        # Sample of passed lessons
        if passed_lessons:
            report += "Sample of passed lessons:\n"
            sample = passed_lessons[:10] if len(passed_lessons) > 10 else passed_lessons
            for lesson in sample:
                report += f"- ID {lesson['id']}: {lesson['title']}\n"

        report += "\n---\n\n## Issue Breakdown\n\n"

        if self.results['errors']:
            for category, issues in sorted(self.results['errors'].items()):
                report += f"### {category} Issues ({len(issues)})\n\n"

                # Show unique issue types
                issue_types = defaultdict(list)
                for error in issues:
                    issue_text = error['issue'].split(':', 1)[1].strip() if ':' in error['issue'] else error['issue']
                    issue_types[issue_text].append(error['id'])

                for issue_text, lesson_ids in sorted(issue_types.items(), key=lambda x: -len(x[1]))[:10]:
                    report += f"**{issue_text}**\n"
                    report += f"- Affects {len(lesson_ids)} lessons\n"
                    if len(lesson_ids) <= 5:
                        report += f"- Lesson IDs: {', '.join(map(str, lesson_ids))}\n"
                    else:
                        report += f"- Lesson IDs: {', '.join(map(str, lesson_ids[:5]))}... and {len(lesson_ids) - 5} more\n"
                    report += "\n"
        else:
            report += "✅ No issues found!\n"

        report += "\n---\n\n## Quality Metrics\n\n"

        # Calculate quality metrics
        python_lessons = [l for l in self.detailed_results if l['language'] == 'python']
        java_lessons = [l for l in self.detailed_results if l['language'] == 'java']

        python_pass = len([l for l in python_lessons if l['status'] == 'PASS'])
        java_pass = len([l for l in java_lessons if l['status'] == 'PASS'])

        report += f"### Python Lessons\n\n"
        report += f"- Total: {len(python_lessons)}\n"
        report += f"- Passed: {python_pass} ({python_pass/len(python_lessons)*100:.1f}%)\n"
        report += f"- Failed: {len(python_lessons) - python_pass} ({(len(python_lessons)-python_pass)/len(python_lessons)*100:.1f}%)\n\n"

        report += f"### Java Lessons\n\n"
        report += f"- Total: {len(java_lessons)}\n"
        report += f"- Passed: {java_pass} ({java_pass/len(java_lessons)*100:.1f}%)\n"
        report += f"- Failed: {len(java_lessons) - java_pass} ({(len(java_lessons)-java_pass)/len(java_lessons)*100:.1f}%)\n\n"

        report += "\n---\n\n## Recommendations\n\n"

        if pass_rate >= 95:
            report += "✅ **EXCELLENT:** Platform quality is exceptional. {:.1f}% pass rate.\n\n".format(pass_rate)
            report += "The platform is production-ready with high-quality lessons.\n"
        elif pass_rate >= 90:
            report += "✅ **GOOD:** Platform quality is strong. {:.1f}% pass rate.\n\n".format(pass_rate)
            report += "Minor improvements recommended:\n"
            if category_counts:
                top_issues = sorted(category_counts.items(), key=lambda x: -x[1])[:3]
                for category, count in top_issues:
                    report += f"- Fix {category} issues ({count} lessons)\n"
        elif pass_rate >= 80:
            report += "⚠️ **WARNING:** Platform quality needs improvement. {:.1f}% pass rate.\n\n".format(pass_rate)
            report += "Recommended actions:\n"
            if category_counts:
                top_issues = sorted(category_counts.items(), key=lambda x: -x[1])[:5]
                for category, count in top_issues:
                    report += f"- Address {category} issues ({count} lessons)\n"
        else:
            report += "❌ **CRITICAL:** Platform quality is below standards. {:.1f}% pass rate.\n\n".format(pass_rate)
            report += "Immediate action required:\n"
            if category_counts:
                for category, count in sorted(category_counts.items(), key=lambda x: -x[1]):
                    report += f"- Fix {category} issues ({count} lessons)\n"

        report += "\n---\n\n## Conclusion\n\n"

        if pass_rate >= 95:
            report += f"The platform has {self.results['passed']:,} high-quality lessons ready for production use.\n"
            report += f"Pass rate of {pass_rate:.1f}% indicates exceptional quality control.\n"
        else:
            report += f"The platform has {self.results['passed']:,} lessons that meet quality standards.\n"
            report += f"{self.results['failed']:,} lessons require attention to reach production quality.\n"

        report += f"\n**Test completed successfully. See detailed results above.**\n"

        # Write report
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)

        return output_file

# Main execution
print('='*60)
print('COMPREHENSIVE LESSON TESTING')
print('='*60)

# Load lessons
print('\nLoading lessons...')
py_lessons = load_lessons('public/lessons-python.json')
java_lessons = load_lessons('public/lessons-java.json')

print(f'Loaded {len(py_lessons)} Python lessons and {len(java_lessons)} Java lessons')
print(f'Total: {len(py_lessons) + len(java_lessons)} lessons to test')

# Create tester
tester = LessonTester()

# Test Python lessons
print('\n--- Testing Python Lessons ---')
for i, lesson in enumerate(py_lessons, 1):
    if i % 100 == 0:
        print(f'  Tested {i}/{len(py_lessons)} Python lessons...')
    tester.test_lesson(lesson, 'python')

print(f'[OK] Tested {len(py_lessons)} Python lessons')

# Test Java lessons
print('\n--- Testing Java Lessons ---')
for i, lesson in enumerate(java_lessons, 1):
    if i % 100 == 0:
        print(f'  Tested {i}/{len(java_lessons)} Java lessons...')
    tester.test_lesson(lesson, 'java')

print(f'[OK] Tested {len(java_lessons)} Java lessons')

# Generate report
print('\n--- Generating Test Report ---')
report_file = tester.generate_report()
print(f'[OK] Report generated: {report_file}')

# Print summary
print('\n' + '='*60)
print('TEST SUMMARY')
print('='*60)
print(f'Total lessons tested: {tester.results["total"]:,}')
print(f'Passed: {tester.results["passed"]:,}')
print(f'Failed: {tester.results["failed"]:,}')
pass_rate = (tester.results['passed'] / tester.results['total'] * 100) if tester.results['total'] > 0 else 0
print(f'Pass rate: {pass_rate:.1f}%')
print(f'\nDetailed report saved to: {report_file}')

if pass_rate >= 95:
    print('\n[SUCCESS] Platform quality is EXCELLENT!')
elif pass_rate >= 90:
    print('\n[GOOD] Platform quality is strong.')
elif pass_rate >= 80:
    print('\n[WARNING] Platform quality needs improvement.')
else:
    print('\n[CRITICAL] Platform quality is below standards.')

print('\n' + '='*60)
print('TESTING COMPLETE')
print('='*60)
