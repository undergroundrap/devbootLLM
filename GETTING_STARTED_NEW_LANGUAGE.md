# Quick Start: Adding a New Language

This guide gets you started adding lessons for a new programming language in under 30 minutes.

## Prerequisites

- [ ] Programming language installed and working
- [ ] Basic understanding of JSON
- [ ] Text editor or IDE

## Step 1: Create Your Lesson File (2 minutes)

```bash
# Create the file
echo "[]" > public/lessons-javascript.json

# Replace 'javascript' with your language (lowercase, no spaces)
```

## Step 2: Copy the Example Lesson (5 minutes)

Open `public/lessons-javascript.json` and add this starter lesson:

```json
[
  {
    "id": 1,
    "title": "Hello World",
    "language": "javascript",
    "description": "Learn to write your first program. Print output to the console.",
    "fullSolution": "console.log('Hello, World!');",
    "expectedOutput": "Hello, World!",
    "baseCode": "// TODO: Print 'Hello, World!' to the console\n",
    "tutorial": "<p class=\"mb-4 text-gray-300 text-lg leading-relaxed\">Let's write our first program! In programming, it's traditional to start with a \"Hello World\" program.</p>\n\n<div style=\"background: rgba(31, 41, 55, 0.5); border-left: 4px solid #6b7280; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;\">\n  <h4 class=\"font-semibold text-gray-200\" style=\"margin-bottom: 0.75rem;\">Overview</h4>\n  <p class=\"mb-4 text-gray-300\">\n    This lesson teaches you how to display output in your programming language. Output is essential for seeing results and debugging your code.\n  </p>\n</div>\n\n<div style=\"background: rgba(20, 83, 45, 0.2); border-left: 4px solid #22c55e; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;\">\n  <h4 class=\"font-semibold text-gray-200\" style=\"margin-bottom: 0.75rem;\">Best Practices:</h4>\n  <ul class=\"list-disc list-inside mb-4 text-gray-300 space-y-2\">\n    <li>Always test your code to verify it produces the expected output</li>\n    <li>Use clear, descriptive messages in your output</li>\n    <li>Follow your language's conventions for printing/logging</li>\n  </ul>\n</div>\n\n<div style=\"background: rgba(19, 78, 74, 0.2); border-left: 4px solid #14b8a6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;\">\n  <h4 class=\"font-semibold text-gray-200\" style=\"margin-bottom: 0.75rem;\">Key Takeaways:</h4>\n  <ul class=\"list-disc list-inside mb-4 text-gray-300 space-y-2\">\n    <li>Understand how to display output in your language</li>\n    <li>Learn the basic syntax for a complete program</li>\n    <li>Build confidence with your first working code</li>\n  </ul>\n</div>",
    "tags": ["Beginner", "Output", "Hello World"],
    "additionalExamples": "<h5>More Examples:</h5>\n\n<div class=\"example-block\">\n  <h6>Example 1: Multiple Lines</h6>\n  <pre><code class=\"language-javascript\">console.log('Line 1');\nconsole.log('Line 2');\nconsole.log('Line 3');</code></pre>\n</div>\n\n<div class=\"example-block\">\n  <h6>Example 2: Variables</h6>\n  <pre><code class=\"language-javascript\">const message = 'Hello, World!';\nconsole.log(message);</code></pre>\n</div>",
    "difficulty": "Beginner",
    "category": "Core JavaScript"
  }
]
```

**Important**: Update these fields for your language:
- `language`: Your language name (lowercase)
- `fullSolution`: Working code in your language
- `expectedOutput`: Actual output from running the code
- `baseCode`: Starter template with hints
- `category`: "Core {YourLanguage}"

## Step 3: Test Your Lesson (3 minutes)

```bash
# 1. Test the code compiles/runs
node test.js  # (or python test.py, go run test.go, etc.)

# 2. Verify output matches expectedOutput
# The output should exactly match what's in expectedOutput

# 3. Run validation
python scripts/validate_lessons.py public/lessons-javascript.json
```

## Step 4: Add More Lessons (ongoing)

Now that you have one working lesson, add more! Use the same structure:

**Recommended First 10 Lessons:**
1. Hello World (done!)
2. Variables and Data Types
3. Basic Math Operations
4. String Manipulation
5. Conditional Statements (if/else)
6. Loops (for loop)
7. Loops (while loop)
8. Functions Basics
9. Arrays/Lists Basics
10. Input and Output

**Template for Each New Lesson:**

```json
{
  "id": 2,
  "title": "Variables and Basic Data Types",
  "language": "javascript",
  "description": "Learn to declare variables and work with different data types.",
  "fullSolution": "// Your complete working code here",
  "expectedOutput": "Expected output here",
  "baseCode": "// TODO: Hints for the student",
  "tutorial": "<!-- Copy tutorial structure from lesson 1 -->",
  "tags": ["Beginner", "Variables", "Data Types"],
  "additionalExamples": "<!-- 2-3 examples -->",
  "difficulty": "Beginner",
  "category": "Core JavaScript"
}
```

## Tips for Success

### DO ✓
- Start simple with beginner lessons
- Test every lesson before adding it
- Use the validation tool frequently
- Copy tutorial structure from working lessons
- Keep titles clear and concise
- Make sure expectedOutput is accurate

### DON'T ✗
- Skip testing your code
- Forget to increment the ID
- Leave empty required fields
- Use complex examples in beginner lessons
- Ignore validation errors

## Validation Checklist

Before committing lessons, check:
- [ ] All code compiles/runs successfully
- [ ] expectedOutput matches actual output
- [ ] Tutorial has Overview, Best Practices, Key Takeaways
- [ ] Tags include difficulty level
- [ ] IDs are sequential (1, 2, 3, ...)
- [ ] No validation errors

## Next Steps

Once you have 10-20 beginner lessons:

1. **Review** [LESSON_TEMPLATE.md](LESSON_TEMPLATE.md) for comprehensive guidelines
2. **Add Intermediate lessons** - combining concepts (20-30 lessons)
3. **Add Advanced lessons** - complex patterns (15-25 lessons)
4. **Add Expert lessons** - production-ready code (50+ lessons)
5. **Run full validation** to ensure quality

## Need Help?

- **Template Guide**: See [LESSON_TEMPLATE.md](LESSON_TEMPLATE.md)
- **System Overview**: See [LESSON_SYSTEM_SUMMARY.md](LESSON_SYSTEM_SUMMARY.md)
- **Examples**: Look at Java/Python lessons for reference
- **Validation**: Run `python scripts/validate_lessons.py <your-file.json>`

## Example Languages to Add

Popular languages that would make great additions:
- **JavaScript/TypeScript** - Web development
- **Go** - Backend/systems programming
- **Rust** - Systems programming
- **C#** - .NET development
- **Ruby** - Web development
- **PHP** - Web development
- **Swift** - iOS development
- **Kotlin** - Android development
- **C/C++** - Systems programming
- **R** - Data science

---

**Ready to start? Create your first lesson file and let's go!** 🚀
