# Scripts Directory

This directory contains utility scripts for maintaining and validating the devbootLLM platform.

## Active Scripts

### Quality Validation

**`comprehensive_quality_review.py`**
- **Purpose**: Main quality validation script for all lessons
- **Usage**: `python scripts/comprehensive_quality_review.py`
- **What it checks**:
  - Tutorial quality (length, depth, structure)
  - Code quality (length, syntax)
  - Concept coverage (all programming concepts covered)
  - Tutorial depth (presence of Overview, Common Pitfalls, Best Practices sections)
  - Pacing (lesson distribution across difficulty levels)
- **Output**: Comprehensive quality report with scores and recommendations
- **When to run**: After adding new lessons or making bulk changes

**`validate-lessons.mjs`**
- **Purpose**: Node.js lesson validation utility
- **Usage**: `node scripts/validate-lessons.mjs`
- **What it checks**:
  - JSON structure validity
  - Required fields present (id, title, description, code, tutorial, etc.)
  - No duplicate lesson IDs
  - Proper language tags
- **When to run**: Before committing lesson changes

**`find-dup-ids.mjs`**
- **Purpose**: Finds duplicate lesson IDs in lesson files
- **Usage**: `node scripts/find-dup-ids.mjs public/lessons-java.json public/lessons-python.json`
- **Output**: Lists any duplicate IDs found
- **When to run**: If you suspect duplicate IDs or after bulk imports

### Lesson Creation

**`add_career_lessons.py`**
- **Purpose**: Script used to create lessons 661-695 (career development lessons)
- **Contains**: Templates and functions for:
  - Career prep lessons (resume, LinkedIn, GitHub)
  - Interview prep lessons (STAR method, live coding)
  - Debugging challenges
  - Code review practices
  - Final capstone project
- **Usage**: Reference for creating similar career-focused lessons
- **Note**: This was used to create the final 5 job-readiness lessons

**`mirror_job_ready_to_python.py`**
- **Purpose**: Converts Java lessons to Python versions
- **Usage**: `python scripts/mirror_job_ready_to_python.py`
- **What it does**:
  - Reads Java lessons (651-695)
  - Converts Java syntax to Python
  - Updates language tag to "python"
  - Adds to Python lessons file
- **When to run**: After adding new Java lessons that need Python versions

## Workflow Examples

### Adding New Lessons

1. Create lessons in Java file first
2. Run `python scripts/mirror_job_ready_to_python.py` to create Python versions
3. Run `node scripts/find-dup-ids.mjs public/lessons-*.json` to check for duplicates
4. Run `node scripts/validate-lessons.mjs` to validate structure
5. Run `python scripts/comprehensive_quality_review.py` to check quality
6. Commit if all checks pass

### Quality Check Before Release

```bash
# Validate structure
node scripts/validate-lessons.mjs

# Check for duplicate IDs
node scripts/find-dup-ids.mjs public/lessons-java.json public/lessons-python.json

# Comprehensive quality review
python scripts/comprehensive_quality_review.py
```

## Historical Context

The following scripts were removed in the cleanup (Oct 2025):

- `achieve_perfect_100.py` - One-time script to reach 100/100 tutorial depth
- `add_job_readiness_lessons.py` - Superseded by add_career_lessons.py
- `add_missing_sections.py` - Added Overview/Pitfalls sections (completed)
- `complete_job_ready_content.py` - Incomplete, superseded
- `comprehensive_validation.py` - Duplicate of comprehensive_quality_review.py
- `create_job_ready_lessons.py` - Superseded by add_career_lessons.py
- `enhance_tutorials.py` - One-time enhancement (completed)
- `expand_short_descriptions.py` - Expanded descriptions (completed)
- `fix_duplicate_titles.py` - Fixed duplicate titles (completed)
- `perfect_tutorial_depth.py` - One-time depth improvement (completed)
- `final_8_lessons.json` - Data file (no longer needed)
- `job_readiness_content.json` - Data file (no longer needed)

All one-time migration/improvement scripts were removed after successful completion to keep the repository clean.

## Maintenance Notes

- **Python scripts**: Require Python 3.8+ (for f-strings and modern syntax)
- **Node scripts**: Require Node.js 16+ (for ES modules)
- **Dependencies**: None - all scripts use standard library only
- **Encoding**: All scripts handle UTF-8 properly for special characters in lessons
