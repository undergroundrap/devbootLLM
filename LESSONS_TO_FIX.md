# Lessons Requiring Fixes

## Priority: HIGH (Actual Logic Bugs)

### Python Lesson 58: Regular Expressions
- **Issue**: Expected output "1\n2\n3" but got empty string
- **Location**: `public/lessons-python.json` - Lesson ID 58
- **Fix Needed**: Review regex pattern and code logic

### Python Lesson 93: Regex Substitution
- **Issue**: Expected "a#b#" but got "a1b2"
- **Location**: `public/lessons-python.json` - Lesson ID 93
- **Fix Needed**: Correct the substitution pattern in fullSolution

### Python Lesson 95: Logging
- **Issue**: Expected "INFO:Ready" but got empty output
- **Location**: `public/lessons-python.json` - Lesson ID 95
- **Fix Needed**: Fix logging configuration to capture output

### Python Lesson 103: Working with Multiple Arrays
- **Issue**: Expected "[1, 2, 3, 5, 6, 7, 7]" but got "[1, 2, 3, 3, 5, 6, 7, 7]"
- **Location**: `public/lessons-python.json` - Lesson ID 103
- **Fix Needed**: Remove duplicate '3' in merge logic

## Priority: MEDIUM (Test Environment Issues)

### Python Lessons 122, 160, 199, 239: pathlib.glob tests
- **Issue**: Finding extra .txt files in current directory
- **Fix Needed**: Either:
  1. Update expected output to be more flexible
  2. Change tests to use temp directories
  3. Update lesson description to note environment dependency

### Python Lesson 393: pathlib log size
- **Issue**: Expected size 13, got 15
- **Fix Needed**: Verify correct expected file size

### Python Lesson 447: Environment variables
- **Issue**: Expected placeholder "[username]" and "[count]" but got actual values
- **Fix Needed**: Update expected output to match actual behavior or make test more flexible

### Python Lessons 449-450: Logging tests
- **Issue**: Logging output goes to console, not captured in stdout
- **Fix Needed**: Update logging configuration to use StringIO or update expected output

## Priority: LOW (Platform-Specific or Design Issues)

### Python Lesson 52: Virtualenv Activate Script
- **Issue**: Backslash escape sequence formatting difference
- **Expected**: `inventory\.venv\Scripts\activate.bat`
- **Got**: `inventory\\.venv\\Scripts\\activate.bat`
- **Fix Needed**: Normalize path separator escaping

### Python Lesson 334: shared_memory ShareableList
- **Issue**: Windows platform limitation - FileNotFoundError
- **Fix Needed**: Either:
  1. Mark as Linux/Mac only
  2. Provide Windows-compatible alternative
  3. Add platform check in code

### Python Lesson 421: Validate input range
- **Issue**: Test expects ValueError to be raised (test design expects failure)
- **Fix Needed**: Clarify expected behavior - should lesson test exception handling?

## Summary Statistics

- **Total Python Lessons**: 700
- **Lessons with logic bugs**: 5-8 (~1%)
- **Lessons with environment issues**: 10-15 (~2%)
- **Lessons working perfectly**: 680+ (~97%)

## Next Steps

1. Wait for Java lesson test results
2. Fix the HIGH priority issues (lessons 58, 93, 95, 103)
3. Review MEDIUM priority issues and decide on approach
4. Document platform-specific lessons
5. Consider adding isolated test environment for glob/file tests

## Testing Script Location

- Main test script: `test_all_lessons.py`
- Run with: `python test_all_lessons.py`
- Generates detailed error report with line-by-line comparison
