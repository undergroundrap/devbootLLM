# Contributing to DevBoot LLM

Thank you for your interest in contributing! This is an open-source coding education platform with **2,107 verified lessons** (1,030 Python + 1,077 Java). All contributions are welcome.

## Table of Contents
- [How to Contribute](#how-to-contribute)
- [Adding New Lessons](#adding-new-lessons)
- [Lesson Quality Standards](#lesson-quality-standards)
- [Testing Requirements](#testing-requirements)
- [Code Style Guidelines](#code-style-guidelines)
- [Pull Request Process](#pull-request-process)

## How to Contribute

There are many ways to contribute:

- **Add new lessons** - Create lessons for Python or Java
- **Improve existing lessons** - Fix typos, clarify tutorials, add examples
- **Fix bugs** - Report or fix issues in the platform
- **Improve documentation** - Help others understand the project
- **Add features** - Progress tracking, search, learning paths, etc.

## Adding New Lessons

### Lesson Structure

Each lesson is a JSON object with these required fields:

```json
{
  "id": 1,
  "title": "Lesson Title",
  "description": "Brief description (1-2 sentences)",
  "language": "python",
  "difficulty": "Beginner",
  "category": "Core",
  "tags": ["Beginner", "Core", "Fundamentals"],
  "baseCode": "# Starting code with TODO\ndef greet():\n    # TODO: ...",
  "fullSolution": "# Complete working solution\ndef greet():\n    print('Hello!')\n\ngreet()",
  "expectedOutput": "Hello!\n",
  "tutorial": "<div>HTML tutorial content</div>",
  "additionalExamples": ""
}
```

### Field Guidelines

**`id`** (required)
- Must be unique within the language
- For Python: next available number in `public/lessons-python.json`
- For Java: next available number in `public/lessons-java.json`

**`title`** (required)
- Clear, descriptive title (3-8 words)
- Examples: "Hello, World!", "List Comprehensions", "Spring Boot REST API"

**`description`** (required)
- 1-2 sentence summary
- Explains what the learner will do
- Example: "Learn to use list comprehensions to transform data efficiently."

**`language`** (required)
- Either `"python"` or `"java"`

**`difficulty`** (required)
- One of: `"Beginner"`, `"Intermediate"`, `"Advanced"`, `"Expert"`
- Beginner: Basic syntax, first concepts
- Intermediate: Multiple concepts combined
- Advanced: Complex patterns, frameworks
- Expert: Architecture, optimization, advanced topics

**`category`** (required)
- Core: Basic language features
- OOP: Object-oriented programming
- Web: Web frameworks (Flask, Django, Spring Boot)
- Async: Asynchronous programming
- Database: SQL, ORM, data persistence
- Testing: Unit tests, integration tests
- DevOps: Docker, deployment, CI/CD
- AI/ML: Machine learning, data science (Python only)

**`tags`** (required)
- Array of 2-5 descriptive tags
- Include difficulty level
- Include main concepts
- Example: `["Intermediate", "Collections", "Streams"]`

**`baseCode`** (required)
- Starting code for the learner
- Should include helpful structure
- Use `# TODO: ...` or `// TODO: ...` for parts they need to complete
- Must be valid syntax (even with TODOs)

**`fullSolution`** (required)
- Complete, working solution
- **MUST compile/run without errors**
- Must produce the expected output
- Should demonstrate best practices

**`expectedOutput`** (required)
- Exact output the solution produces
- Include newlines (`\n`) where appropriate
- Leave empty `""` only if the program has no output
- Verify this by actually running the code

**`tutorial`** (required)
- HTML content explaining the concept
- Should include:
  - Overview section
  - Code examples
  - Best practices
  - Common pitfalls (if applicable)
- Use inline styles for formatting (see existing lessons)
- Minimum 200 characters of actual content

**`additionalExamples`** (optional)
- Extra code examples or explanations
- Can be empty string `""`

## Lesson Quality Standards

### Every lesson MUST:

✅ **Compile and run** - Zero errors when executed
✅ **Produce expected output** - Output matches `expectedOutput` field exactly
✅ **Be self-contained** - No external dependencies (except standard library and common frameworks)
✅ **Have clear tutorial** - Explains the concept with examples
✅ **Follow best practices** - Demonstrates good code style
✅ **Be appropriately scoped** - Focused on one concept or related concepts

### Code Quality Requirements

**Python:**
- Python 3.12+ syntax
- Follow PEP 8 style guide
- Use meaningful variable names
- Include docstrings for complex functions
- Standard library preferred; external packages only if necessary
- Common frameworks OK: Flask, Django, FastAPI, pandas, NumPy, pytest

**Java:**
- Java 17+ syntax
- Follow Java naming conventions (camelCase, PascalCase)
- Include necessary imports
- For Spring Boot: use annotations appropriately
- Common frameworks OK: Spring Boot, Spring Security, JPA, JUnit, Mockito

### Tutorial Quality

Good tutorials should:
- Start with a clear overview
- Include working code examples
- Explain WHY, not just WHAT
- Provide best practices
- Be concise but complete (aim for 300-1000 characters)
- Use proper HTML structure

Example tutorial structure:
```html
<div style="...">
  <h4>Overview</h4>
  <p>Brief explanation of the concept...</p>
</div>
<div style="...">
  <h4>Example:</h4>
  <pre class="tutorial-code-block">code example here</pre>
  <p>Explanation of the example...</p>
</div>
<div style="...">
  <h4>✅ Best Practices:</h4>
  <ul>
    <li>Best practice 1</li>
    <li>Best practice 2</li>
  </ul>
</div>
```

## Testing Requirements

### Before Submitting

1. **Validate your lesson JSON** - Ensure valid JSON syntax
   ```bash
   node scripts/validate-lessons.mjs
   ```

2. **Test code compilation** (Python)
   ```bash
   python -c "exec('''your code here''')"
   ```

3. **Test code compilation** (Java)
   ```bash
   javac Main.java && java Main
   ```

4. **Verify expected output**
   - Run your solution
   - Copy the EXACT output (including newlines)
   - Paste into `expectedOutput` field

5. **Test in the app**
   ```bash
   npm install
   npm start
   # Visit http://localhost:3000
   # Navigate to your lesson
   # Verify tutorial displays correctly
   # Test code execution
   ```

### Running Validation Scripts

```bash
# Validate all lessons
node scripts/validate-lessons.mjs

# Check lesson quality
python scripts/check_lesson_quality.py

# Check tutorial quality
python scripts/check_tutorial_quality.py
```

All scripts should pass with no errors before submitting a PR.

## Code Style Guidelines

### General
- Use consistent indentation (4 spaces for Python, 4 spaces for Java)
- Keep lines under 100 characters when possible
- Use descriptive names, avoid abbreviations
- Add comments only where code isn't self-explanatory

### Python Specific
```python
# Good
def calculate_total(prices):
    """Calculate the sum of all prices."""
    return sum(prices)

# Avoid
def calc_tot(p):  # Too abbreviated
    return sum(p)
```

### Java Specific
```java
// Good
public class UserService {
    public User findUserById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException(id));
    }
}

// Avoid - unclear names
public class UsrSvc {
    public User get(Long i) {
        return repo.findById(i).get();  // Can throw unchecked exception
    }
}
```

## Pull Request Process

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/devbootLLM-app.git
cd devbootLLM-app
npm install
```

### 2. Create a Branch

```bash
git checkout -b add-python-decorators-lesson
# or
git checkout -b fix-java-lesson-42
```

### 3. Make Your Changes

- Add or modify lessons in `public/lessons-python.json` or `public/lessons-java.json`
- Test thoroughly (see [Testing Requirements](#testing-requirements))
- Run validation scripts

### 4. Commit Your Changes

```bash
git add public/lessons-python.json
git commit -m "Add lesson on Python decorators

- Added lesson #1031: Decorator basics
- Includes function decorators with examples
- Shows @property and @staticmethod usage"
```

**Commit message format:**
- First line: Brief summary (50 chars or less)
- Blank line
- Detailed description with bullet points
- Focus on WHAT and WHY, not HOW

### 5. Push and Create PR

```bash
git push origin add-python-decorators-lesson
```

Then create a Pull Request on GitHub with:

**PR Title:** Clear, descriptive (e.g., "Add Python decorators lesson")

**PR Description:**
```markdown
## Summary
Added a new lesson on Python decorators covering basic function decorators.

## Changes
- Added lesson #1031 to lessons-python.json
- Tutorial covers @property, @staticmethod, @classmethod
- Includes 3 code examples
- Expected output verified

## Testing
- [x] Lesson JSON is valid
- [x] Code compiles and runs
- [x] Expected output matches actual output
- [x] Tutorial displays correctly
- [x] Validation scripts pass
```

### 6. PR Review Checklist

Before requesting review, ensure:

- [ ] All required fields present and valid
- [ ] Code compiles without errors
- [ ] Expected output is exact (run the code to verify)
- [ ] Tutorial has clear explanations and examples
- [ ] Validation scripts pass (`node scripts/validate-lessons.mjs`)
- [ ] Lesson ID is unique and sequential
- [ ] Difficulty and category are appropriate
- [ ] Tags are descriptive and include difficulty
- [ ] Commit messages are clear
- [ ] PR description explains the changes

## Questions?

- **General questions:** Open a [GitHub Discussion](https://github.com/undergroundrap/devbootLLM-app/discussions)
- **Bug reports:** Open a [GitHub Issue](https://github.com/undergroundrap/devbootLLM-app/issues)
- **Quick questions:** Ask in PR comments

## Code of Conduct

Be respectful, constructive, and collaborative. We're all here to learn and improve.

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0 (see [LICENSE](LICENSE)).

### What This Means

**Apache 2.0 includes patent protection:**
- You grant users a patent license for your contributions
- Users can't sue for patent infringement based on your code
- If someone sues claiming patent infringement, their license terminates
- This protects both contributors and users

**You retain copyright:**
- You keep ownership of your contributions
- The license just grants others rights to use it
- Your name is attributed in the contribution

**It's permissive:**
- Commercial use allowed
- Modifications allowed
- Distribution allowed
- Private use allowed
- Users must include the license and copyright notice

For full details, see the [LICENSE](LICENSE) file.

---

Thank you for contributing to DevBoot LLM! 🚀
