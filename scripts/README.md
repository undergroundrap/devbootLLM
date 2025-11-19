# Scripts Directory

This directory contains utility scripts for validating and maintaining lesson quality.

## Available Scripts

### Core Validation Tools

#### `validate_lessons.py` (Recommended)

**Comprehensive lesson validation tool** - Validates lesson structure, content quality, and compilation.

**Usage:**
```bash
python scripts/validate_lessons.py public/lessons-java.json
python scripts/validate_lessons.py public/lessons-python.json
python scripts/validate_lessons.py public/lessons-{language}.json
```

**What it validates:**
- **Structure**: JSON validity, array format, lesson count
- **Required Fields**: All 12 required fields present and non-empty
- **ID Sequence**: Sequential numbering (1 to N), no gaps, no duplicates
- **Tags**: Difficulty tag present, consistency, appropriate count (3-6 recommended)
- **Tutorial Sections**: Required sections (Overview, Best Practices, Key Takeaways)
- **Content Quality**: Title/description lengths, code ratios, difficulty distribution
- **Language**: Correct language field matching filename

**Output:**
- Color-coded results: `[OK]` (green), `[FAIL]` (red), `[WARN]` (yellow)
- Detailed statistics and distributions
- Summary with total errors and warnings

**When to use:**
- Before committing lesson changes
- After adding new lessons
- When adding a new language
- For comprehensive quality checks

---

### `validate-lessons.mjs`

**Legacy JSON schema validator** - Basic validation using JSON schema.

**Usage:**
```bash
node scripts/validate-lessons.mjs
```

**What it validates:**
- JSON structure validity
- Required fields present (id, title, description, baseCode, fullSolution, etc.)
- No duplicate lesson IDs
- Proper language tags

**When to use:**
- Quick JSON structure checks
- Backward compatibility with older workflows

**Note**: For comprehensive validation, use `validate_lessons.py` instead.

---

### Curriculum Improvement Tools

#### `audit_difficulty.py`

**Difficulty distribution analyzer** - Analyzes lesson difficulty balance and provides reclassification recommendations.

**Usage:**
```bash
python scripts/audit_difficulty.py
python scripts/audit_difficulty.py --detailed
python scripts/audit_difficulty.py --export report.txt
```

**What it analyzes:**
- Current vs. target difficulty distribution
- Specific lessons to reclassify
- Gaps requiring new content
- Recommendations for achieving job-ready balance

**Output:**
- Current distribution with target comparison
- Gap analysis (too many/too few at each level)
- Specific reclassification recommendations
- Suggested topics for new lessons

**When to use:**
- Before starting curriculum improvements
- After major difficulty changes
- Monthly to track rebalancing progress
- To identify which lessons to reclassify

---

#### `track_progress.py`

**Progress tracking system** - Tracks curriculum improvement metrics and milestones.

**Usage:**
```bash
python scripts/track_progress.py init        # Initialize tracking (once)
python scripts/track_progress.py update      # Update after changes
python scripts/track_progress.py report      # Generate detailed report
python scripts/track_progress.py milestone   # Check milestone status
```

**What it tracks:**
- Difficulty distribution over time
- Professional skills coverage (Git, Agile, Documentation, Code Review)
- Full-stack project count
- Phase completion milestones

**Output:**
- Before/after comparisons
- Progress toward targets
- Milestone achievements
- Recommended next actions

**When to use:**
- Initialize once at project start
- Update after each batch of improvements
- Generate reports weekly to track progress
- Check milestones when completing phases

---

#### `lesson_templates.json`

**Lesson templates library** - Pre-built templates for creating new lessons.

**Available templates:**
- `beginner_java` / `beginner_python` - Basic syntax and fundamentals
- `professional_skill_agile` - Agile/Scrum methodology lessons
- `git_workflow` - Git and version control lessons
- `fullstack_project` - Full-stack application projects
- `database_lesson` - Database and ORM lessons

**Usage:**
1. Open `scripts/lesson_templates.json`
2. Copy the appropriate template
3. Fill in placeholders `[like this]`
4. Add to your lesson file
5. Validate with `validate_lessons.py`

**When to use:**
- Creating new beginner lessons
- Adding professional skills content
- Building full-stack projects
- Standardizing lesson structure

---

### Git Integration

#### `pre-commit-hook.example`

**Git pre-commit hook template** - Automatically validates lessons before commits.

**Setup:**
```bash
# Copy to git hooks directory
cp scripts/pre-commit-hook.example .git/hooks/pre-commit

# Make executable (Linux/Mac)
chmod +x .git/hooks/pre-commit
```

**What it does:**
- Runs validation checks before allowing commits
- Prevents committing lessons with validation errors
- Helps catch issues early in development

**When to use:**
- Set up once in your local repository
- Recommended for all contributors

---

## Recommended Workflows

### Daily Development Workflow

```bash
# 1. Make improvements (reclassify or create lessons)

# 2. Validate changes
python scripts/validate_lessons.py public/lessons-java.json
python scripts/validate_lessons.py public/lessons-python.json

# 3. Update progress tracking
python scripts/track_progress.py update

# 4. Commit if validation passes
git add .
git commit -m "Your commit message"
```

### Weekly Review Workflow

```bash
# 1. Generate progress report
python scripts/track_progress.py report

# 2. Check milestone status
python scripts/track_progress.py milestone

# 3. Run difficulty audit
python scripts/audit_difficulty.py

# 4. Plan next week's improvements
```

### Before Committing Changes

```bash
# 1. Validate comprehensively (required)
python scripts/validate_lessons.py public/lessons-java.json
python scripts/validate_lessons.py public/lessons-python.json

# 2. Update progress (recommended)
python scripts/track_progress.py update

# 3. Quick JSON validation (optional)
node scripts/validate-lessons.mjs
```

### Curriculum Improvement Workflow

```bash
# 1. Initialize progress tracking (once)
python scripts/track_progress.py init

# 2. Run difficulty audit to identify issues
python scripts/audit_difficulty.py --detailed

# 3. Make improvements weekly:
#    - Reclassify Expert lessons
#    - Create new Beginner/Intermediate lessons
#    - Add professional skills lessons
#    - Build full-stack projects

# 4. Validate after each batch
python scripts/validate_lessons.py public/lessons-java.json

# 5. Update progress tracking
python scripts/track_progress.py update

# 6. Generate weekly report
python scripts/track_progress.py report
```

### Adding a New Language

```bash
# 1. Create lesson file
echo "[]" > public/lessons-javascript.json

# 2. Add your lessons following LESSON_TEMPLATE.md

# 3. Validate quality
python scripts/validate_lessons.py public/lessons-javascript.json

# 4. Aim for: 0 errors, <10 warnings, 100% compilation rate

# 5. Ensure proper difficulty distribution (25/30/25/15)
python scripts/audit_difficulty.py
```

### Setting Up Automated Validation

```bash
# Enable pre-commit hook for automatic validation
cp scripts/pre-commit-hook.example .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit  # Linux/Mac only
```

---

## Technical Requirements

- **Python scripts**: Require Python 3.8+
- **Node scripts**: Require Node.js 16+
- **Dependencies**: None - all scripts use standard library only
- **Platform**: Cross-platform (Windows, Linux, macOS)

---

## Quality Standards

All validation scripts enforce the quality standards documented in:
- [LESSON_TEMPLATE.md](../LESSON_TEMPLATE.md) - Complete field specifications
- [LESSON_SYSTEM_SUMMARY.md](../LESSON_SYSTEM_SUMMARY.md) - Best practices and patterns
- [GETTING_STARTED_NEW_LANGUAGE.md](../GETTING_STARTED_NEW_LANGUAGE.md) - Quick start guide

**Target metrics:**
- 100% compilation rate (all code must run)
- 0 validation errors
- <10 warnings
- 95%+ tutorial section coverage
- Consistent tag formatting (Title Case)
- Optimal difficulty distribution: 25% Beginner | 30% Intermediate | 25% Advanced | 15% Expert
- Professional skills coverage: Git, Agile, Documentation, Code Review
- Full-stack project examples

---

## Curriculum Improvement Resources

For comprehensive guidance on improving your curriculum from good to job-ready:

- **[START_HERE.md](../START_HERE.md)** - Quick overview and getting started
- **[QUICK_START.md](../QUICK_START.md)** - Get started in 1 hour
- **[IMPLEMENTATION_ROADMAP.md](../IMPLEMENTATION_ROADMAP.md)** - 16-20 week improvement plan
- **[CURRICULUM_IMPROVEMENT_PLAN.md](../CURRICULUM_IMPROVEMENT_PLAN.md)** - Detailed gap analysis
- **[WEEKLY_CHECKLIST.md](../WEEKLY_CHECKLIST.md)** - Track weekly progress

**Quick command reference:**
```bash
# Analyze difficulty distribution
python scripts/audit_difficulty.py

# Initialize progress tracking
python scripts/track_progress.py init

# Update progress after improvements
python scripts/track_progress.py update

# See detailed progress report
python scripts/track_progress.py report
```

---

## Current Lesson Database Status

**Last validated:** 2025-11-17

### Java Lessons (`public/lessons-java.json`)
- **Total Lessons:** 917
- **Validation Errors:** 0 ✅
- **Warnings:** 5 (non-critical)
- **Tutorial Coverage:** 76-86%
- **Difficulty Distribution:** 12.5% Beginner | 19.6% Intermediate | 15.0% Advanced | 52.8% Expert
- **Top Categories:** OOP (24%), Core Java (19%), Web Development (11%), Async (9%)

### Python Lessons (`public/lessons-python.json`)
- **Total Lessons:** 904
- **Validation Errors:** 0 ✅
- **Warnings:** 5 (non-critical)
- **Tutorial Coverage:** 35-83%
- **Difficulty Distribution:** 16.4% Beginner | 17.4% Intermediate | 14.2% Advanced | 52.1% Expert
- **Top Categories:** OOP (22%), Core Python (19%), Web Development (12%), Async (12%)

### Overall Quality Summary
- **Total Lessons Across All Languages:** 1,821
- **100% Validation Success Rate** - All lessons pass structural and content validation
- **0 Critical Errors** - Production-ready quality
- **Sequential IDs** - No gaps or duplicates
- **Complete Fields** - All required fields present in every lesson
