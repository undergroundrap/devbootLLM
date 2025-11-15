# Scripts Directory

This directory contains utility scripts for maintaining and validating the devbootLLM platform.

## Active Maintenance Scripts

### Quality Validation

**`comprehensive_lesson_analysis.py`**
- **Purpose**: Complete quality validation and compilation testing for all lessons
- **Usage**: `python scripts/comprehensive_lesson_analysis.py`
- **What it checks**:
  - Java code compilation (uses javac to verify all code compiles)
  - Python syntax validation (verifies all code has valid syntax)
  - Tutorial quality (content length, sections, code examples)
  - Missing required fields (expectedOutput, etc.)
  - Difficulty and category distribution
  - Tag coverage and frequency
- **Output**: Comprehensive report with pass/fail rates, compilation errors, and statistics
- **When to run**: After adding new lessons, making bulk changes, or before releases

**`validate-lessons.mjs`**
- **Purpose**: Node.js lesson validation utility
- **Usage**: `node scripts/validate-lessons.mjs`
- **What it checks**:
  - JSON structure validity
  - Required fields present (id, title, description, code, tutorial, etc.)
  - No duplicate lesson IDs
  - Proper language tags
- **When to run**: Before committing lesson changes

**`pre-commit-hook.example`**
- **Purpose**: Example Git pre-commit hook for automated validation
- **Usage**: Copy to `.git/hooks/pre-commit` and make executable
- **What it does**:
  - Runs validation checks before allowing commits
  - Helps catch issues early in development
- **When to use**: Set up once in your local repository for automated checks

## Workflow Examples

### Quality Check Before Committing

```bash
# Validate JSON structure and required fields
node scripts/validate-lessons.mjs

# Comprehensive analysis with compilation testing
python scripts/comprehensive_lesson_analysis.py
```

### After Adding or Modifying Lessons

```bash
# Run full validation suite
python scripts/comprehensive_lesson_analysis.py

# Review the output for:
# - Compilation/syntax errors
# - Missing required fields
# - Tutorial quality issues
# - Distribution across difficulty levels
```

## Repository Cleanup History

**Nov 12, 2024** - Removed one-time compilation fix scripts and backups:
- `fix_compilation_errors.py` - Fixed 187 Java/Python compilation errors (completed)
- `fix_remaining_errors.py` - Fixed advanced Java class reference issues (completed)
- `fix_python_manual.py` - Manual fixes for complex Python indentation issues (completed)
- Removed 4 backup files (*.backup_20251112_*) after successful fixes
- Added `comprehensive_lesson_analysis.py` for ongoing quality validation

**Oct 27, 2024** - Removed obsolete one-time generation scripts:
- `add_bonus_lessons.py` - Generated lesson 696 (completed)
- `add_bridging_lessons.py` - Generated lessons 697-700 (completed)
- `add_career_lessons.py` - Generated career lessons (completed)
- `add_key_concepts.py` - Added Key Concepts sections (completed)
- `add_key_concepts_v2.py` - Improved version (completed)
- `add_remaining_35_lessons.py` - Generated lessons 701-702 (completed)
- `complete_final_9_lessons.py` - Completed specific lessons (completed)
- `find_incomplete_tutorials.py` - Superseded by analyze_all_lessons.py
- `generate_final_33_lessons.py` - Generated lessons 703-735 (completed)
- `mirror_job_ready_to_python.py` - Mirrored lessons (completed)

All one-time scripts are removed after successful execution to maintain a clean repository.

## Technical Requirements

- **Python scripts**: Require Python 3.8+ (for f-strings and modern syntax)
- **Node scripts**: Require Node.js 16+ (for ES modules)
- **Dependencies**: None - all scripts use standard library only
- **Encoding**: All scripts handle UTF-8 properly for special characters

## Maintenance Notes

- Scripts are production-quality and ready for repeated use
- All scripts include error handling and validation
- Output is formatted for readability in Windows/Linux terminals
- JSON files are always formatted with 2-space indentation
- Scripts automatically backup before making changes (when appropriate)
