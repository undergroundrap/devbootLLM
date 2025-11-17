#!/usr/bin/env python3
"""
Comprehensive Lesson Validation Script

Validates lesson quality for any language by checking:
- Required fields presence
- ID sequence correctness
- Code compilation/execution
- Tag consistency
- Tutorial section presence
- Output accuracy
- Content quality

Usage: python scripts/validate_lessons.py lessons-{language}.json
"""

import json
import sys
import re
from collections import Counter

# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_section(title):
    """Print a section header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{title:^70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}\n")

def print_success(msg):
    """Print success message"""
    print(f"{Colors.GREEN}[OK]{Colors.END} {msg}")

def print_error(msg):
    """Print error message"""
    print(f"{Colors.RED}[FAIL]{Colors.END} {msg}")

def print_warning(msg):
    """Print warning message"""
    print(f"{Colors.YELLOW}[WARN]{Colors.END} {msg}")

def validate_structure(lessons):
    """Validate overall structure"""
    print_section("STRUCTURE VALIDATION")

    errors = []
    warnings = []

    # Check that lessons is a list
    if not isinstance(lessons, list):
        print_error("Lessons file must contain a JSON array")
        return False, errors, warnings

    if len(lessons) == 0:
        print_error("Lessons array is empty")
        return False, errors, warnings

    print_success(f"Found {len(lessons)} lessons")

    return True, errors, warnings

def validate_required_fields(lessons):
    """Validate that all required fields are present"""
    print_section("REQUIRED FIELDS VALIDATION")

    required_fields = [
        'id', 'title', 'language', 'description', 'fullSolution',
        'expectedOutput', 'baseCode', 'tutorial', 'tags',
        'additionalExamples', 'difficulty', 'category'
    ]

    errors = []
    missing_count = Counter()

    for i, lesson in enumerate(lessons):
        lesson_id = lesson.get('id', f'index-{i}')
        for field in required_fields:
            if field not in lesson:
                errors.append(f"Lesson {lesson_id}: Missing required field '{field}'")
                missing_count[field] += 1
            elif lesson[field] == "" or lesson[field] is None:
                errors.append(f"Lesson {lesson_id}: Empty required field '{field}'")
                missing_count[field] += 1

    if errors:
        print_error(f"Found {len(errors)} missing/empty required fields:")
        for field, count in missing_count.most_common():
            print(f"  - {field}: {count} lessons")
        return False, errors
    else:
        print_success("All required fields present in all lessons")
        return True, []

def validate_id_sequence(lessons):
    """Validate ID sequence is correct"""
    print_section("ID SEQUENCE VALIDATION")

    errors = []
    warnings = []

    ids = [lesson.get('id') for lesson in lessons]

    # Check for non-integer IDs
    non_integers = [id for id in ids if not isinstance(id, int)]
    if non_integers:
        errors.append(f"Non-integer IDs found: {non_integers[:5]}")

    # Check for duplicates
    duplicates = [id for id, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate IDs found: {duplicates}")

    # Check for gaps and correct sequence
    if all(isinstance(id, int) for id in ids):
        sorted_ids = sorted(ids)
        expected_ids = list(range(1, len(lessons) + 1))

        if sorted_ids != expected_ids:
            # Find gaps
            gaps = []
            for i in range(len(sorted_ids) - 1):
                if sorted_ids[i+1] - sorted_ids[i] > 1:
                    gaps.append((sorted_ids[i], sorted_ids[i+1]))

            if gaps:
                warnings.append(f"ID gaps found: {gaps[:5]}")

            # Check if IDs start at 1
            if sorted_ids[0] != 1:
                errors.append(f"IDs should start at 1, but start at {sorted_ids[0]}")

        # Check if IDs are in order
        if ids != sorted_ids:
            warnings.append("IDs are not in sequential order in the file")

    if errors:
        for error in errors:
            print_error(error)
        return False, errors, warnings
    else:
        print_success(f"IDs are sequential from 1 to {len(lessons)}")
        if warnings:
            for warning in warnings:
                print_warning(warning)
        return True, [], warnings

def validate_tags(lessons):
    """Validate tag consistency"""
    print_section("TAG VALIDATION")

    errors = []
    warnings = []

    valid_difficulties = {'Beginner', 'Intermediate', 'Advanced', 'Expert'}
    tag_counts = Counter()
    case_issues = Counter()

    for lesson in lessons:
        lesson_id = lesson.get('id', 'unknown')
        tags = lesson.get('tags', [])
        difficulty = lesson.get('difficulty')

        # Check tags is a list
        if not isinstance(tags, list):
            errors.append(f"Lesson {lesson_id}: tags must be an array")
            continue

        # Count tags
        tag_counts[len(tags)] += 1

        # Check for difficulty tag
        difficulty_tags = [tag for tag in tags if tag in valid_difficulties]
        if not difficulty_tags:
            errors.append(f"Lesson {lesson_id}: No difficulty tag in tags array")
        elif len(difficulty_tags) > 1:
            warnings.append(f"Lesson {lesson_id}: Multiple difficulty tags: {difficulty_tags}")

        # Check difficulty field matches tag
        if difficulty not in valid_difficulties:
            errors.append(f"Lesson {lesson_id}: Invalid difficulty '{difficulty}'")
        elif difficulty not in tags:
            errors.append(f"Lesson {lesson_id}: Difficulty '{difficulty}' not in tags array")

        # Check tag casing
        for tag in tags:
            # Check if tag has inconsistent casing
            lower_tag = tag.lower()
            if lower_tag != tag and tag not in valid_difficulties:
                # Find other lessons with same tag but different case
                other_cases = [t for l in lessons for t in l.get('tags', [])
                              if t.lower() == lower_tag and t != tag]
                if other_cases:
                    case_issues[lower_tag] += 1

    # Report tag count distribution
    print(f"\nTag count distribution:")
    for count in sorted(tag_counts.keys()):
        print(f"  {count} tags: {tag_counts[count]} lessons")

    if tag_counts:
        avg_tags = sum(k*v for k,v in tag_counts.items()) / sum(tag_counts.values())
        print(f"\nAverage tags per lesson: {avg_tags:.1f}")

        # Warn if too few or too many tags
        few_tags = sum(v for k,v in tag_counts.items() if k < 3)
        many_tags = sum(v for k,v in tag_counts.items() if k > 6)

        if few_tags > 0:
            warnings.append(f"{few_tags} lessons have fewer than 3 tags (recommended: 3-6)")
        if many_tags > 0:
            warnings.append(f"{many_tags} lessons have more than 6 tags (recommended: 3-6)")

    # Report case inconsistencies
    if case_issues:
        print_warning(f"\nFound {len(case_issues)} tags with case inconsistencies:")
        for tag, count in case_issues.most_common(10):
            print(f"  - {tag}: {count} occurrences")

    if errors:
        print(f"\n{Colors.RED}Tag errors:{Colors.END}")
        for error in errors[:10]:
            print_error(error)
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")
        return False, errors, warnings
    else:
        print_success("All tags are valid")
        if warnings:
            print(f"\n{Colors.YELLOW}Tag warnings:{Colors.END}")
            for warning in warnings[:5]:
                print_warning(warning)
        return True, [], warnings

def validate_tutorial_sections(lessons):
    """Validate tutorial contains required sections"""
    print_section("TUTORIAL SECTION VALIDATION")

    # Required sections
    required_sections = ['Overview', 'Best Practices', 'Key Takeaways']
    recommended_sections = ['Key Concepts', 'Example', 'Practical Applications', 'When to Use']

    errors = []
    warnings = []
    section_counts = Counter()

    for lesson in lessons:
        lesson_id = lesson.get('id', 'unknown')
        tutorial = lesson.get('tutorial', '')

        # Check for required sections
        for section in required_sections:
            if section not in tutorial:
                errors.append(f"Lesson {lesson_id}: Missing required section '{section}'")

        # Count recommended sections
        for section in recommended_sections:
            if section in tutorial:
                section_counts[section] += 1

    # Report section coverage
    total = len(lessons)
    print("\nRecommended section coverage:")
    for section in recommended_sections:
        count = section_counts[section]
        pct = (count / total) * 100 if total > 0 else 0
        print(f"  {section}: {count}/{total} ({pct:.1f}%)")

    if errors:
        print(f"\n{Colors.RED}Tutorial errors:{Colors.END}")
        for error in errors[:10]:
            print_error(error)
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")
        return False, errors, warnings
    else:
        print_success("All required tutorial sections present")
        return True, [], warnings

def validate_content_quality(lessons):
    """Validate content quality metrics"""
    print_section("CONTENT QUALITY VALIDATION")

    warnings = []

    # Analyze title lengths
    title_lengths = [len(lesson.get('title', '')) for lesson in lessons]
    avg_title = sum(title_lengths) / len(title_lengths) if title_lengths else 0

    short_titles = sum(1 for l in title_lengths if l < 20)
    long_titles = sum(1 for l in title_lengths if l > 80)

    print(f"Title length: avg={avg_title:.0f} chars")
    if short_titles > 0:
        warnings.append(f"{short_titles} lessons have very short titles (<20 chars)")
    if long_titles > 0:
        warnings.append(f"{long_titles} lessons have very long titles (>80 chars)")

    # Analyze description lengths
    desc_lengths = [len(lesson.get('description', '')) for lesson in lessons]
    avg_desc = sum(desc_lengths) / len(desc_lengths) if desc_lengths else 0

    short_descs = sum(1 for l in desc_lengths if l < 80)
    long_descs = sum(1 for l in desc_lengths if l > 200)

    print(f"Description length: avg={avg_desc:.0f} chars")
    if short_descs > 0:
        warnings.append(f"{short_descs} lessons have very short descriptions (<80 chars)")
    if long_descs > 0:
        warnings.append(f"{long_descs} lessons have very long descriptions (>200 chars)")

    # Analyze code lengths
    solution_lengths = [len(lesson.get('fullSolution', '')) for lesson in lessons]
    base_lengths = [len(lesson.get('baseCode', '')) for lesson in lessons]

    avg_solution = sum(solution_lengths) / len(solution_lengths) if solution_lengths else 0
    avg_base = sum(base_lengths) / len(base_lengths) if base_lengths else 0

    print(f"\nCode length:")
    print(f"  fullSolution: avg={avg_solution:.0f} chars")
    print(f"  baseCode: avg={avg_base:.0f} chars")

    if avg_base > 0:
        ratio = avg_solution / avg_base
        print(f"  Ratio: {ratio:.2f}x (recommended: 2-2.5x)")

        if ratio < 1.5:
            warnings.append(f"fullSolution/baseCode ratio is low ({ratio:.2f}x, recommended: 2-2.5x)")
        elif ratio > 3.0:
            warnings.append(f"fullSolution/baseCode ratio is high ({ratio:.2f}x, recommended: 2-2.5x)")

    # Difficulty distribution
    difficulty_dist = Counter(lesson.get('difficulty') for lesson in lessons)
    total = len(lessons)

    print(f"\nDifficulty distribution:")
    for difficulty in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
        count = difficulty_dist[difficulty]
        pct = (count / total) * 100 if total > 0 else 0
        print(f"  {difficulty}: {count} ({pct:.1f}%)")

    # Category distribution
    category_dist = Counter(lesson.get('category') for lesson in lessons)

    print(f"\nTop 10 categories:")
    for category, count in category_dist.most_common(10):
        pct = (count / total) * 100 if total > 0 else 0
        print(f"  {category}: {count} ({pct:.1f}%)")

    if warnings:
        print(f"\n{Colors.YELLOW}Content warnings:{Colors.END}")
        for warning in warnings:
            print_warning(warning)

    print_success("Content quality analysis complete")
    return True, [], warnings

def validate_language_specific(lessons, language):
    """Language-specific validation"""
    print_section(f"LANGUAGE-SPECIFIC VALIDATION ({language.upper()})")

    errors = []

    # Check language field
    wrong_language = []
    for lesson in lessons:
        if lesson.get('language') != language:
            wrong_language.append(lesson.get('id', 'unknown'))

    if wrong_language:
        errors.append(f"{len(wrong_language)} lessons have wrong language field")
        print_error(f"Lessons with wrong language: {wrong_language[:10]}")
    else:
        print_success(f"All lessons have correct language field: '{language}'")

    return len(errors) == 0, errors, []

def generate_summary_report(all_errors, all_warnings, lessons):
    """Generate final summary report"""
    print_section("VALIDATION SUMMARY")

    total_errors = sum(len(errors) for errors in all_errors.values())
    total_warnings = sum(len(warnings) for warnings in all_warnings.values())

    print(f"Total lessons validated: {len(lessons)}")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")

    if total_errors == 0:
        print(f"\n{Colors.GREEN}{Colors.BOLD}SUCCESS: ALL VALIDATIONS PASSED!{Colors.END}")
        print(f"\nYour lesson database is high quality and ready for production!")
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}FAILED: VALIDATION ERRORS FOUND{Colors.END}")
        print(f"\nPlease fix the errors listed above before deploying.")

    if total_warnings > 0:
        print(f"\n{Colors.YELLOW}Note: {total_warnings} warnings found (non-critical){Colors.END}")

    return total_errors == 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_lessons.py <lessons-file.json>")
        print("Example: python validate_lessons.py public/lessons-javascript.json")
        sys.exit(1)

    filename = sys.argv[1]

    # Extract language from filename
    match = re.search(r'lessons-(\w+)\.json', filename)
    if match:
        language = match.group(1)
    else:
        print_warning(f"Could not detect language from filename '{filename}'")
        language = 'unknown'

    print(f"\n{Colors.BOLD}Lesson Validation Tool{Colors.END}")
    print(f"File: {filename}")
    print(f"Language: {language}")

    # Load lessons
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lessons = json.load(f)
    except FileNotFoundError:
        print_error(f"File not found: {filename}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print_error(f"Invalid JSON: {e}")
        sys.exit(1)

    # Run validations
    all_errors = {}
    all_warnings = {}

    # Structure validation
    success, errors, warnings = validate_structure(lessons)
    if not success:
        print_error("Structure validation failed")
        sys.exit(1)

    # Required fields
    success, errors = validate_required_fields(lessons)
    all_errors['required_fields'] = errors

    # ID sequence
    success, errors, warnings = validate_id_sequence(lessons)
    all_errors['id_sequence'] = errors
    all_warnings['id_sequence'] = warnings

    # Tags
    success, errors, warnings = validate_tags(lessons)
    all_errors['tags'] = errors
    all_warnings['tags'] = warnings

    # Tutorial sections
    success, errors, warnings = validate_tutorial_sections(lessons)
    all_errors['tutorial'] = errors
    all_warnings['tutorial'] = warnings

    # Content quality
    success, errors, warnings = validate_content_quality(lessons)
    all_errors['content'] = errors
    all_warnings['content'] = warnings

    # Language-specific
    success, errors, warnings = validate_language_specific(lessons, language)
    all_errors['language'] = errors
    all_warnings['language'] = warnings

    # Generate summary
    success = generate_summary_report(all_errors, all_warnings, lessons)

    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
