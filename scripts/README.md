# Scripts Directory

This directory contains utility scripts for maintaining and validating the devbootLLM platform.

## Active Maintenance Scripts

### Quality Validation

**`comprehensive_quality_review.py`**
- **Purpose**: Main quality validation script for all lessons
- **Usage**: `python scripts/comprehensive_quality_review.py`
- **What it checks**:
  - Tutorial quality (length, depth, structure)
  - Code quality (length, syntax)
  - Concept coverage (all programming concepts covered)
  - Tutorial depth (presence of 6 required sections)
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

**`verify_database.js`**
- **Purpose**: Verify SQLite database has correct lesson counts
- **Usage**: `node scripts/verify_database.js`
- **What it checks**:
  - Java lessons count (should be 700)
  - Python lessons count (should be 700)
- **Output**: Reports if database needs rebuilding
- **When to run**: After server restart or if lessons aren't loading correctly

**`find-dup-ids.mjs`**
- **Purpose**: Finds duplicate lesson IDs in lesson files
- **Usage**: `node scripts/find-dup-ids.mjs public/lessons-java.json public/lessons-python.json`
- **Output**: Lists any duplicate IDs found
- **When to run**: If you suspect duplicate IDs or after bulk imports

**`analyze_all_lessons.py`**
- **Purpose**: Comprehensive tutorial and tag analysis
- **Usage**: `python scripts/analyze_all_lessons.py`
- **What it checks**:
  - Tutorial completeness (all 6 sections present)
  - Tag coverage and consistency
  - Tag frequency and distribution
  - Identifies lessons needing improvements
- **Output**: Detailed analysis report with specific lesson IDs
- **When to run**: When auditing tutorial quality or tag consistency

### Maintenance & Improvement Scripts

**`fix_tutorial_sections.py`**
- **Purpose**: Adds missing tutorial sections to specific lessons
- **Usage**: `python scripts/fix_tutorial_sections.py`
- **What it does**:
  - Adds Best Practices sections to portfolio lessons
  - Adds Common Pitfalls sections where missing
  - Adds Real-World Applications sections
- **When to run**: After identifying lessons with missing sections

**`standardize_tags.py`**
- **Purpose**: Standardizes and consolidates tags across all lessons
- **Usage**: `python scripts/standardize_tags.py`
- **What it does**:
  - Fixes capitalization inconsistencies (enterprise → Enterprise)
  - Consolidates duplicate tags (Basics/basics → Beginner)
  - Standardizes common terms (api → API, oop → OOP)
- **When to run**: After adding lessons with new tags or noticing inconsistencies

**`reposition_bridging_lessons.py`**
- **Purpose**: Repositions bridging lessons to their correct locations
- **Usage**: `python scripts/reposition_bridging_lessons.py`
- **What it does**:
  - Shifts existing lesson IDs to make room for bridges
  - Inserts bridging lessons between difficulty levels
  - Validates no duplicate IDs created
- **When to run**: When restructuring lesson organization (rarely needed)

## Workflow Examples

### Quality Check Before Committing

```bash
# Validate structure
node scripts/validate-lessons.mjs

# Check for duplicate IDs
node scripts/find-dup-ids.mjs public/lessons-java.json public/lessons-python.json

# Comprehensive quality review
python scripts/comprehensive_quality_review.py
```

### Improving Tutorial Quality

```bash
# 1. Analyze current state
python scripts/analyze_all_lessons.py

# 2. Fix identified issues
python scripts/fix_tutorial_sections.py

# 3. Validate improvements
python scripts/comprehensive_quality_review.py
```

### Tag System Maintenance

```bash
# 1. Analyze tag usage
python scripts/analyze_all_lessons.py

# 2. Standardize tags
python scripts/standardize_tags.py

# 3. Verify consistency
python scripts/analyze_all_lessons.py
```

## Repository Cleanup History

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

All one-time scripts were archived after successful execution to maintain a clean repository.

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
