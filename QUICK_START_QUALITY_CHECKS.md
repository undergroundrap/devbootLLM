# Quick Start: Lesson Quality Checks

## Run These Commands Now

### 1. Quick Test (10 seconds)
```bash
npm run check:quick
```
Tests first/last 10 lessons of each language. Use this for fast feedback.

### 2. Validate All Solutions (5-10 minutes)
```bash
npm run check:solutions
```
**THIS IS THE MAIN ONE** - Tests every lesson's solution to find output mismatches.

### 3. Get List of Failures
```bash
python scripts/extract_failed_lessons.py
```
Shows which lessons are failing and saves detailed report.

### 4. Full Quality Audit (10-15 minutes)
```bash
npm run check:all
```
Runs all quality checks in sequence.

## What We Found

**121 Python lessons are failing** with output mismatch errors.

These lessons will show students:
> ❌ Not quite right. The code runs, but the output doesn't match.

## Most Common Issues

### 1. Non-Deterministic Output (Easy Fix)

**Problem**: ML algorithms, random numbers, timestamps produce different output each run.

**Fix**: Add random seeds

```python
# Before
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2)

# After
import numpy as np
np.random.seed(42)
kmeans = KMeans(n_clusters=2, random_state=42)
```

### 2. Generic Expected Output (Easy Fix)

**Problem**: expectedOutput says "(Output will vary based on implementation)" but code produces specific output.

**Fix**: Update expectedOutput to match actual output

```json
{
  "expectedOutput": "(Output will vary based on implementation)"
}
```

Change to:

```json
{
  "expectedOutput": "Test passed\nDatabase connection successful\n"
}
```

### 3. Whitespace Issues (Easy Fix)

**Problem**: Extra newlines or spaces

**Fix**: Clean up the expectedOutput string

```json
{
  "expectedOutput": "Hello World\n\n"  // ❌ Extra newline
}
```

Change to:

```json
{
  "expectedOutput": "Hello World\n"  // ✅ Correct
}
```

## Files You Need to Edit

All lessons are in these files:
- `public/lessons-python.json` - All Python lessons
- `public/lessons-java.json` - All Java lessons

## Example: Fixing Lesson 1021

### Step 1: Find the lesson

Open `public/lessons-python.json` and search for `"id": 1021`

### Step 2: Run the fullSolution manually

Copy the code from `fullSolution` and run it:

```python
python -c "
from sklearn.cluster import KMeans
X = [[1,2], [1,4], [1,0], [10,2], [10,4]]
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
print('Cluster assignments:', kmeans.labels_)
"
```

Output: `Cluster assignments: [0 0 1 1 0]`

But expectedOutput says: `Cluster assignments: [1 1 0 0 1]`

### Step 3: Fix it

Add random seed to the code:

```python
import numpy as np
np.random.seed(42)
from sklearn.cluster import KMeans
X = [[1,2], [1,4], [1,0], [10,2], [10,4]]
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)
print('Cluster assignments:', kmeans.labels_)
```

Run again, get: `Cluster assignments: [1 1 0 0 1]`

### Step 4: Update JSON

Update the lesson in the JSON file:

```json
{
  "id": 1021,
  "fullSolution": "import numpy as np\nnp.random.seed(42)\n...",
  "expectedOutput": "Cluster assignments: [1 1 0 0 1]\n"
}
```

### Step 5: Verify

```bash
npm run check:quick
```

## Complete List of Failed Lessons

See `failed_lessons_report.txt` for the complete list with expected/actual output for each.

Or run:
```bash
python scripts/extract_failed_lessons.py
```

## Failed Lesson Categories

- **Kubernetes**: 690-694 (5 lessons)
- **Auth/Security**: 704-712 (9 lessons)
- **Design Patterns**: 598-607 (10 lessons)
- **Concurrency**: 683-687 (5 lessons)
- **DevOps/CI/CD**: Multiple lessons
- **Data Science/ML**: Multiple lessons
- **Date/Time**: Lesson 205
- **File I/O**: 283, 494
- **And many more** - see full list in VALIDATION_SUMMARY.md

## Next Steps

1. **Start with easy fixes** (whitespace, deterministic output)
   ```bash
   # Fix a few lessons
   # Then test
   npm run check:quick
   ```

2. **Work through the list systematically**
   - Use `failed_lessons_report.txt` as your checklist
   - Fix 10-20 lessons at a time
   - Re-run validation after each batch

3. **Once Python is done, validate Java**
   ```bash
   npm run check:solutions
   ```

## Need Help?

- **Detailed docs**: See `LESSON_QUALITY_CHECKS.md`
- **Summary**: See `VALIDATION_SUMMARY.md`
- **Failure details**: See `failed_lessons_report.txt`

## Available Scripts

```bash
npm run check:validate    # Basic structure validation
npm run check:solutions   # ⭐ Main validation - find output mismatches
npm run check:quick       # ⚡ Fast test - first/last 10 lessons
npm run check:quality     # Quality analysis
npm run check:tutorials   # Tutorial analysis
npm run check:duplicates  # Find duplicate solutions
npm run check:all         # Run everything
```

## Automation

Add to CI/CD:

```yaml
# .github/workflows/validate.yml
- name: Validate Lessons
  run: npm run check:solutions
```

This prevents new broken lessons from being merged!

---

**Remember**: The goal is to make sure every lesson works when students click "Solve Lesson"!
