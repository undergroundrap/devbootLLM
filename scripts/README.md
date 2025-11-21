# Scripts Directory - Complete Validation & Quality Assurance System

This directory contains comprehensive validation and quality assurance tools for lesson maintenance.

---

## 🚀 Quick Start

### For Developers

```bash
# Quick validation (10 seconds)
npm run check:quick

# Complete validation - finds output mismatches (5-10 minutes)
npm run check:solutions

# Get readable failure list
python scripts/extract_failed_lessons.py

# Full quality audit (15-20 minutes)
npm run check:all
```

### For AI Assistants

**Recommended sequential workflow:**

```bash
# Step 1: Quick smoke test
npm run check:quick

# Step 2: Full solution validation (if quick test passes)
npm run check:solutions

# Step 3: Extract and analyze failures
python scripts/extract_failed_lessons.py

# Step 4: Quality checks (optional)
npm run check:quality
npm run check:tutorials

# Step 5: Run all checks before major releases
npm run check:all
```

---

## 📚 Table of Contents

1. [Solution Validation Tools](#solution-validation-tools) - **Most Important**
2. [Quality Analysis Tools](#quality-analysis-tools)
3. [Legacy & Structure Tools](#legacy--structure-tools)
4. [Utility & Cleanup Tools](#utility--cleanup-tools)
5. [Recommended Workflows](#recommended-workflows)
6. [NPM Script Reference](#npm-script-reference)

---

## 🎯 Solution Validation Tools

### ⭐ **`validate_all_lessons.py`** - MOST IMPORTANT

**Purpose**: Executes every lesson's `fullSolution` and verifies output matches `expectedOutput`.

**This script finds the exact issue**: "❌ Not quite right. The code runs, but the output doesn't match."

**Usage**:
```bash
python scripts/validate_all_lessons.py
# Or via npm:
npm run check:solutions
```

**What it does**:
- Executes fullSolution for every Python and Java lesson
- Compares actual output with expectedOutput
- Reports compilation errors, runtime errors, timeouts
- Handles special cases (e.g., dynamic output validation)
- Normalizes whitespace for comparison

**Output**:
- Console: Color-coded pass/fail for each lesson
- `validation_report.json`: Machine-readable detailed results
- Exit code 0 if all pass, 1 if any failures

**When to use**:
- **Before committing lesson changes** (critical!)
- After modifying fullSolution or expectedOutput
- To verify all lessons work correctly
- Before major releases

**Typical runtime**: 5-10 minutes (Python: 1030 lessons, Java: 1077 lessons)

---

### ⚡ **`quick_validation_test.py`** - Fast Smoke Test

**Purpose**: Quick validation of first 10 and last 10 lessons for rapid feedback.

**Usage**:
```bash
python scripts/quick_validation_test.py
# Or via npm:
npm run check:quick
```

**What it does**:
- Tests first 10 lessons (catch basic issues)
- Tests last 10 lessons (catch recent additions)
- Same validation logic as full validation
- Reports pass/fail/error counts

**When to use**:
- **During active development** (fast iteration)
- Before running full validation
- Quick sanity check after changes
- CI/CD smoke tests

**Typical runtime**: 5-10 seconds

---

### 📋 **`extract_failed_lessons.py`** - Failure Report Generator

**Purpose**: Parses validation output and creates readable failure reports.

**Usage**:
```bash
python scripts/extract_failed_lessons.py
```

**What it does**:
- Extracts all failed lessons from validation output
- Creates human-readable summary
- Saves detailed report to `failed_lessons_report.txt`
- Shows expected vs actual output for each failure

**Output**:
- Console: Summarized failure list
- `failed_lessons_report.txt`: Detailed failure report with expected/actual

**When to use**:
- After running `validate_all_lessons.py`
- To create work items for fixing lessons
- To track progress fixing failures

---

### 📈 **`analyze_validation_output.py`** - Output Analyzer

**Purpose**: Analyzes validation output for patterns and statistics.

**Usage**:
```bash
python scripts/analyze_validation_output.py
```

**What it does**:
- Parses `validation_output.txt`
- Extracts pass/fail/error counts
- Groups failures by category
- Provides statistical summary

**When to use**:
- To understand validation results
- After running full validation
- For progress tracking

---

## 📊 Quality Analysis Tools

### **`check_lesson_quality.py`** - Comprehensive Quality Checker

**Purpose**: Analyzes lesson structure, content, and code quality.

**Usage**:
```bash
python scripts/check_lesson_quality.py
# Or via npm:
npm run check:quality
```

**What it checks**:
- **Required Fields**: All 12 required fields present and non-empty
- **Title Format**: Title starts with lesson ID
- **Tutorial Quality**: Length, code examples, no placeholder text
- **Code Quality**: Proper structure, no TODOs, no security issues
- **Output Format**: Line endings, trailing whitespace
- **Description Quality**: Length, readability

**Output**:
- Console: Categorized issue summary
- `quality_report.json`: Detailed quality report

**When to use**:
- Before major releases
- Monthly quality audits
- After bulk lesson updates
- To identify quality issues beyond output mismatches

**Typical runtime**: 1-2 minutes

---

### **`check_tutorial_quality.py`** - Tutorial Content Analyzer

**Purpose**: Focuses on tutorial content quality and pedagogical value.

**Usage**:
```bash
python scripts/check_tutorial_quality.py
# Or via npm:
npm run check:tutorials
```

**What it checks**:
- **Structure**: Headings, code blocks, appropriate length
- **Readability**: Sentence length, jargon explanation
- **Code Examples**: Quality, comments, clarity
- **Pedagogy**: Learning objectives, examples, practice prompts
- **Consistency**: Tutorial content matches solution code

**Output**:
- Console: Tutorial issue summary
- `tutorial_quality_report.json`: Detailed tutorial analysis

**When to use**:
- Improving tutorial content
- Curriculum quality reviews
- Before content updates
- Monthly educational quality checks

**Typical runtime**: 1-2 minutes

---

### **`find_duplicate_solutions.py`** - Duplicate Detector

**Purpose**: Finds lessons with identical solutions (potential copy-paste errors).

**Usage**:
```bash
python scripts/find_duplicate_solutions.py
# Or via npm:
npm run check:duplicates
```

**What it does**:
- Compares all fullSolution fields
- Identifies exact duplicates
- Reports potential copy-paste errors

**When to use**:
- After bulk lesson creation
- Quality audits
- Before releases

---

### **`final_quality_scan.py`** - Final Pre-Release Check

**Purpose**: Comprehensive pre-release quality scan.

**Usage**:
```bash
python scripts/final_quality_scan.py
```

**What it does**:
- Runs multiple quality checks
- Verifies all lessons are unique
- Checks for common issues
- Provides go/no-go recommendation

**When to use**:
- Before major releases
- Final check before deployment
- Version milestone verification

---

## 🔄 **`run_all_checks.py`** - Master Check Runner

**Purpose**: Runs all quality checks in sequence with comprehensive summary.

**Usage**:
```bash
python scripts/run_all_checks.py
# Or via npm:
npm run check:all
```

**What it runs** (in order):
1. Basic structure validation (`validate-lessons.mjs`)
2. Solution execution validation (`validate_all_lessons.py`)
3. Lesson quality analysis (`check_lesson_quality.py`)
4. Tutorial quality analysis (`check_tutorial_quality.py`)
5. Duplicate detection (`find_duplicate_solutions.py`)
6. Final quality scan (`final_quality_scan.py`)

**Output**:
- Real-time progress for each check
- Consolidated summary at end
- All individual reports generated

**When to use**:
- **Before major releases** (critical!)
- Weekly quality reviews
- After significant changes
- Complete quality audit

**Typical runtime**: 15-20 minutes

---

## 🏗️ Legacy & Structure Tools

### **`validate-lessons.mjs`** - Basic Structure Validator (Node.js)

**Purpose**: Basic JSON structure and required field validation.

**Usage**:
```bash
node scripts/validate-lessons.mjs
# Or via npm:
npm run check:validate
```

**What it validates**:
- JSON structure validity
- Required fields present
- No duplicate lesson IDs
- Title format (ID prefix)
- Tutorial has code examples
- Tutorial minimum length

**When to use**:
- Quick JSON structure checks
- CI/CD basic validation
- Backward compatibility

**Note**: For comprehensive validation, use `validate_all_lessons.py` instead.

---

## 🧹 Utility & Cleanup Tools

### **`cleanup_all_temp_files.py`** - Cleanup Utility

**Purpose**: Removes temporary files and cleanup artifacts.

**Usage**:
```bash
python scripts/cleanup_all_temp_files.py
```

**What it removes**:
- Temporary analysis files
- Old validation outputs
- One-time script artifacts

**When to use**:
- After completing major work
- Before committing changes
- Periodic cleanup

---

### **`cleanup_scripts.py`** - Script Cleanup

**Purpose**: Legacy cleanup utility.

**Usage**:
```bash
python scripts/cleanup_scripts.py
```

---

### **`lesson_templates.json`** - Lesson Templates

**Purpose**: Templates for creating new lessons.

**Available templates**:
- Beginner lessons (Java/Python)
- Professional skills (Agile, Git)
- Full-stack projects
- Database lessons

**Usage**: Copy template, fill placeholders, validate with `validate_all_lessons.py`

---

## 🔀 Recommended Workflows

### 1. Daily Development Workflow

**For developers actively working on lessons:**

```bash
# 1. Make changes to lessons
vim public/lessons-python.json

# 2. Quick smoke test (10 seconds)
npm run check:quick

# 3. If passes, full validation (5-10 minutes)
npm run check:solutions

# 4. If failures, get detailed list
python scripts/extract_failed_lessons.py

# 5. Fix issues and repeat steps 2-4 until all pass

# 6. Commit when all tests pass
git add .
git commit -m "Fix lesson output mismatches"
git push
```

---

### 2. Fixing Failed Lessons Workflow

**For systematically fixing output mismatch errors:**

```bash
# Step 1: Run validation
npm run check:solutions

# Step 2: Get failure list
python scripts/extract_failed_lessons.py

# Step 3: Review detailed report
cat failed_lessons_report.txt

# Step 4: For each failed lesson:
#   a. Find lesson in lessons-python.json or lessons-java.json
#   b. Copy fullSolution code
#   c. Run it manually to see actual output
#   d. Update expectedOutput to match OR
#   e. Fix code to be deterministic (add random seeds)

# Step 5: Quick revalidation after each batch
npm run check:quick

# Step 6: Full validation when batch is done
npm run check:solutions

# Step 7: Repeat until all lessons pass
```

---

### 3. Pre-Commit Workflow (Required)

**Before committing any lesson changes:**

```bash
# 1. Quick validation (required)
npm run check:quick

# 2. Full validation if touching multiple lessons (required)
npm run check:solutions

# 3. Check for new failures
python scripts/extract_failed_lessons.py

# 4. Only commit if validation passes
# Exit code 0 = all tests pass
if [ $? -eq 0 ]; then
    git add .
    git commit -m "Your message"
    git push
fi
```

---

### 4. Weekly Quality Review

**For maintaining high quality:**

```bash
# Monday: Run full checks
npm run check:all

# Review all generated reports:
cat failed_lessons_report.txt
cat quality_report.json
cat tutorial_quality_report.json

# Plan week's work based on findings

# Friday: Verify improvements
npm run check:solutions
python scripts/extract_failed_lessons.py

# Track progress week-over-week
```

---

### 5. Pre-Release Workflow (Critical)

**Before any major release or deployment:**

```bash
# 1. Clean up temporary files
python scripts/cleanup_all_temp_files.py
rm -f *.txt *.log validation_output.txt

# 2. Run complete quality audit
npm run check:all

# 3. Review all reports
ls -lh *report*.{txt,json}

# 4. Fix critical issues (zero tolerance)
#    - All output mismatches must be fixed
#    - Zero execution errors
#    - Zero security issues

# 5. Final validation
npm run check:solutions

# 6. Only release if exit code is 0 (all pass)
if [ $? -eq 0 ]; then
    echo "✅ Ready for release"
    git tag -a v1.0.0 -m "Release 1.0.0"
    git push --tags
else
    echo "❌ Not ready - fix failures first"
    python scripts/extract_failed_lessons.py
fi
```

---

### 6. CI/CD Integration Workflow

**For GitHub Actions / GitLab CI:**

```yaml
# .github/workflows/validate-lessons.yml
name: Lesson Quality Checks

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
      - uses: actions/setup-python@v2

      - name: Install Python dependencies
        run: pip install numpy scikit-learn pandas

      - name: Quick validation
        run: npm run check:quick

      - name: Full validation
        run: npm run check:solutions

      - name: Extract failures if any
        if: failure()
        run: python scripts/extract_failed_lessons.py

      - name: Upload failure report
        if: failure()
        uses: actions/upload-artifact@v2
        with:
          name: failed-lessons-report
          path: failed_lessons_report.txt
```

---

### 7. AI Assistant Workflow

**For AI assistants helping with lesson quality:**

```bash
# Phase 1: Assessment (Run First)
npm run check:quick                      # 10 seconds - quick health check
python scripts/extract_failed_lessons.py # Get current failure count

# Phase 2: Deep Analysis (If issues found)
npm run check:solutions                  # 5-10 min - comprehensive check
npm run check:quality                    # 1-2 min - quality issues
npm run check:tutorials                  # 1-2 min - tutorial issues

# Phase 3: Fix Planning
cat failed_lessons_report.txt            # Review detailed failures
# Group failures by type:
#   - Non-deterministic output (add seeds)
#   - Generic expected output (update to actual)
#   - Whitespace issues (clean up)
#   - Execution errors (fix code)

# Phase 4: Iterative Fixing
# For each batch of 10-20 lessons:
#   1. Fix lessons
#   2. npm run check:quick
#   3. Repeat until batch passes
#   4. Move to next batch

# Phase 5: Final Verification
npm run check:all                        # 15-20 min - complete audit
# Commit only when exit code is 0

# Phase 6: Cleanup
python scripts/cleanup_all_temp_files.py
rm *.txt *.log validation_output.txt
git add . && git commit && git push
```

---

## 📋 NPM Script Reference

All scripts are available via npm for convenience:

```bash
# Core validation
npm run check:validate      # Basic structure (Node.js)
npm run check:solutions     # ⭐ Solution execution (MAIN)
npm run check:quick         # ⚡ Fast smoke test

# Quality analysis
npm run check:quality       # Lesson quality
npm run check:tutorials     # Tutorial quality
npm run check:duplicates    # Duplicate detection

# Master runner
npm run check:all          # Run everything sequentially
```

---

## 📊 Understanding Validation Results

### Exit Codes

- **0**: All tests passed ✅
- **1**: Some tests failed ❌

### Failure Types

1. **output_mismatch**: Code runs but output doesn't match
   - Shows: "❌ Not quite right. The code runs, but the output doesn't match."
   - Most common issue (~121 Python lessons currently)

2. **execution_error**: Code failed to run
   - Compilation errors (Java)
   - Runtime errors (Python/Java)
   - Should be zero in production

3. **timeout**: Code took too long (>10 seconds)
   - Infinite loops
   - Heavy computation without optimization

### Common Issues & Fixes

#### Issue 1: Non-Deterministic Output
**Problem**: ML algorithms, random numbers produce different output each run

**Fix**:
```python
# Before
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2)

# After
import numpy as np
np.random.seed(42)
kmeans = KMeans(n_clusters=2, random_state=42)
```

#### Issue 2: Generic Expected Output
**Problem**: `expectedOutput: "(Output will vary based on implementation)"`

**Fix**: Update to actual output
```json
{
  "expectedOutput": "Test passed\nConnection successful\n"
}
```

#### Issue 3: Whitespace
**Problem**: Extra newlines or trailing spaces

**Fix**: Clean up expectedOutput
```json
{
  "expectedOutput": "Hello World\n"  // Not "Hello World\n\n"
}
```

---

## 🎯 Quality Standards

### Validation Targets

- **100%** lessons pass solution validation (no output mismatches)
- **0** execution errors
- **0** security issues
- **<10** warnings per language
- **95%+** tutorial section coverage

### Current Status (Last Run: 2025-11-21)

**Python** (943 lessons tested):
- ✅ 822 passed (87.2%)
- ❌ 121 failed (12.8%) - **needs fixing**
- 87 not yet tested (validation incomplete)

**Java** (Quick test only):
- ~98% passing
- 9 failures in lessons 1069-1077 (testing frameworks)
- Full validation needed

---

## 🔧 Technical Requirements

### Python Scripts
- **Python 3.8+** required
- **Dependencies**: numpy, scikit-learn, pandas (for data science lessons)
  ```bash
  pip install numpy scikit-learn pandas matplotlib seaborn
  ```

### Node.js Scripts
- **Node.js 16+** required
- No dependencies (uses standard library)

### Platform Support
- ✅ Windows
- ✅ Linux
- ✅ macOS

---

## 📁 Generated Reports

Scripts generate these reports in the project root:

- `validation_output.txt` - Raw validation output
- `failed_lessons_report.txt` - Detailed failure list with expected/actual
- `validation_report.json` - Machine-readable validation results
- `quality_report.json` - Quality check results
- `tutorial_quality_report.json` - Tutorial analysis results

**Note**: These files are temporary. Clean up before committing:
```bash
python scripts/cleanup_all_temp_files.py
rm *.txt *.log validation_output.txt
```

---

## 📚 Additional Documentation

- **[README_QUALITY_CHECKS.md](../README_QUALITY_CHECKS.md)** - Complete overview
- **[VALIDATION_SUMMARY.md](../VALIDATION_SUMMARY.md)** - Detailed findings
- **[LESSON_QUALITY_CHECKS.md](../LESSON_QUALITY_CHECKS.md)** - Full documentation
- **[QUICK_START_QUALITY_CHECKS.md](../QUICK_START_QUALITY_CHECKS.md)** - Quick reference

---

## 🚨 Important Notes

### For Developers

1. **Always run validation before committing**
   - At minimum: `npm run check:quick`
   - Ideally: `npm run check:solutions`

2. **Zero tolerance for output mismatches in production**
   - All lessons must pass solution validation
   - Fix issues before merging

3. **Use quick test during development**
   - Fast iteration: `npm run check:quick`
   - Full validation before commit

### For AI Assistants

1. **Start with assessment**
   - Run `npm run check:quick` first
   - Only run full validation if needed

2. **Fix systematically**
   - Group similar issues together
   - Fix in batches of 10-20 lessons
   - Validate after each batch

3. **Clean up before committing**
   - Remove temporary files
   - No validation outputs in git

---

## 🏁 Summary

This directory contains a **complete quality assurance system** for lesson validation:

- ⭐ **`validate_all_lessons.py`** - Main tool: finds output mismatches
- ⚡ **`quick_validation_test.py`** - Fast smoke testing
- 📊 **Quality analysis tools** - Tutorial, code, structure checks
- 🔄 **Master runner** - Complete audit in one command
- 📋 **Report generators** - Readable failure lists

**Key workflow**: `check:quick` → `check:solutions` → `extract_failed_lessons.py` → fix → repeat

**Current priority**: Fix 121 Python lessons with output mismatches

Run `npm run check:solutions` to see current status!

---

**Questions?** See full documentation in the root directory's quality check guides.
