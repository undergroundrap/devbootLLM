# Scripts Directory

This directory contains utility scripts for validating and maintaining lesson quality.

## Available Scripts

### `validate_lessons.py` (Recommended)

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

### `pre-commit-hook.example`

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

## Recommended Workflow

### Before Committing Changes

```bash
# 1. Validate comprehensively (recommended)
python scripts/validate_lessons.py public/lessons-java.json
python scripts/validate_lessons.py public/lessons-python.json

# 2. Quick JSON validation (optional)
node scripts/validate-lessons.mjs
```

### Adding a New Language

```bash
# 1. Create lesson file
echo "[]" > public/lessons-javascript.json

# 2. Add your lessons following LESSON_TEMPLATE.md

# 3. Validate quality
python scripts/validate_lessons.py public/lessons-javascript.json

# 4. Aim for: 0 errors, <10 warnings, 100% compilation rate
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
