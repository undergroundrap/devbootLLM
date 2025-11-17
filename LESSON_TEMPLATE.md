# Lesson Template & Guidelines

## Quick Reference: Adding a New Language

### 1. Create Lesson File
Create `public/lessons-{language}.json` with array structure:
```json
[
  { /* lesson 1 */ },
  { /* lesson 2 */ },
  ...
]
```

### 2. Use This Lesson Structure

```json
{
  "id": 1,
  "title": "Variables and Data Types",
  "language": "javascript",
  "description": "Learn how to declare variables and work with different data types in JavaScript.",
  "fullSolution": "// Complete solution code here\nconst name = \"Alice\";\nconst age = 25;\nconsole.log(`${name} is ${age} years old`);",
  "expectedOutput": "Alice is 25 years old",
  "baseCode": "// TODO: Declare a variable for name\n// TODO: Declare a variable for age\n// TODO: Print a message using both variables",
  "tutorial": "<!-- See HTML Template Section Below -->",
  "tags": ["Beginner", "Variables", "Data Types", "Core"],
  "additionalExamples": "<!-- See Additional Examples Template Below -->",
  "difficulty": "Beginner",
  "category": "Core JavaScript"
}
```

---

## Field-by-Field Guidelines

### Required Fields (100% of lessons MUST have these)

#### `id` (number)
- **Type**: Positive integer
- **Rules**: Sequential, no gaps, no duplicates
- **Start at**: 1
- **Example**: `1`, `2`, `3`, ...

#### `title` (string)
- **Type**: Clear, descriptive title
- **Length**: 20-80 characters recommended
- **Format**: Title Case
- **Examples**:
  - ✅ "Working with Arrays and Lists"
  - ✅ "Object-Oriented Programming - Inheritance"
  - ❌ "arrays" (too short, not descriptive)
  - ❌ "THIS IS A LESSON ABOUT VARIABLES" (all caps)

#### `language` (string)
- **Type**: Lowercase language identifier
- **Examples**: `"java"`, `"python"`, `"javascript"`, `"typescript"`, `"go"`, `"rust"`
- **Must match**: Filename `lessons-{language}.json`

#### `description` (string)
- **Type**: Brief explanation of lesson goals
- **Length**: 80-200 characters
- **Format**: 1-2 sentences
- **Pattern**: "Learn [concept]. Practice [skill]."
- **Examples**:
  - ✅ "Learn how to work with arrays and perform common operations like sorting, filtering, and mapping. Practice with real-world examples."
  - ✅ "Master asynchronous programming with promises and async/await syntax."
  - ❌ "Arrays" (too short)
  - ❌ "This is a comprehensive lesson that will teach you everything you need to know about arrays..." (too long)

#### `fullSolution` (string)
- **Type**: Complete, working code
- **Requirements**:
  - Must be runnable as-is
  - Must produce expectedOutput
  - Should be 2-2.5x longer than baseCode
  - Include helpful comments for complex logic
  - Follow language conventions
- **Formatting**:
  - Use proper indentation (2 or 4 spaces, be consistent)
  - Include newlines with `\n`
  - Escape quotes properly: `\"` for JSON
- **Example**:
```json
"fullSolution": "// Calculate factorial recursively\nfunction factorial(n) {\n  if (n <= 1) return 1;\n  return n * factorial(n - 1);\n}\n\nconsole.log(factorial(5));"
```

#### `expectedOutput` (string)
- **Type**: Exact console output
- **Requirements**:
  - Must match actual program output character-for-character
  - Include newlines with `\n`
  - No extra whitespace
  - Test to verify accuracy
- **Examples**:
```json
"expectedOutput": "120"
"expectedOutput": "Hello, World!\nWelcome to programming"
"expectedOutput": "[1, 4, 9, 16, 25]"
```

#### `baseCode` (string)
- **Type**: Starter template with hints
- **Requirements**:
  - Include helpful TODO comments
  - Provide structure but require implementation
  - Should be ~40-50% of fullSolution length
  - Use `// TODO:` or `# TODO:` for hints
- **Example**:
```json
"baseCode": "// TODO: Create a function called factorial\n// TODO: Use recursion to calculate factorial\n// TODO: Test with factorial(5)\n\nfunction factorial(n) {\n  // Your code here\n}\n\n// Test your function"
```

#### `tutorial` (string - HTML)
- **Type**: Rich HTML tutorial content
- **See**: Tutorial Template Section below
- **Must include sections**: Overview, Best Practices, Key Takeaways
- **Recommended sections**: Key Concepts, Example, Practical Applications, When to Use

#### `tags` (array of strings)
- **Type**: Array of classification tags
- **Count**: 3-6 tags recommended
- **Requirements**:
  - MUST include difficulty tag: "Beginner", "Intermediate", "Advanced", or "Expert"
  - Should include topic tags (OOP, Arrays, Async, etc.)
  - Should include technique tags (Recursion, HashMap, etc.)
  - May include context tags (FAANG, Interview, Production)
- **Casing**: Use Title Case consistently
- **Examples**:
```json
"tags": ["Beginner", "Variables", "Data Types"]
"tags": ["Advanced", "OOP", "Inheritance", "Polymorphism"]
"tags": ["Expert", "Concurrency", "Multithreading", "FAANG"]
```

#### `difficulty` (string)
- **Type**: One of four levels
- **Options**: `"Beginner"`, `"Intermediate"`, `"Advanced"`, `"Expert"`
- **Must match**: Tag in tags array
- **Distribution guidance**:
  - Beginner: 12-18% (fundamentals)
  - Intermediate: 17-20% (combining concepts)
  - Advanced: 14-16% (complex patterns)
  - Expert: 50-55% (production-ready, enterprise patterns)

#### `category` (string)
- **Type**: Primary topic category
- **Examples**:
  - "Core {Language}" (e.g., "Core JavaScript")
  - "OOP"
  - "Web Development"
  - "Database"
  - "Async"
  - "Testing"
  - "Security"
  - "DevOps"
  - "Algorithms"
  - "Data Structures"
  - "Design Patterns"
- **Rules**: Single category per lesson, broader than tags

#### `additionalExamples` (string - HTML)
- **Type**: Extended HTML examples
- **See**: Additional Examples Template below
- **Should include**: 2-3 progressively complex examples
- **Format**: Similar styling to tutorial

---

## Tutorial HTML Template

Use this structure for the `tutorial` field:

```html
<p class="mb-4 text-gray-300 text-lg leading-relaxed">[Opening paragraph explaining the main concept]</p>

<div style="background: rgba(31, 41, 55, 0.5); border-left: 4px solid #6b7280; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">Overview</h4>
  <p class="mb-4 text-gray-300">
    [Detailed overview of what this lesson covers and why it's important]
  </p>
</div>

<div style="background: rgba(30, 58, 138, 0.2); border-left: 4px solid #3b82f6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">💡 Key Concepts:</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li><strong class="text-blue-400">Concept 1</strong>: Clear explanation</li>
    <li><strong class="text-blue-400">Concept 2</strong>: Clear explanation</li>
    <li><strong class="text-blue-400">Concept 3</strong>: Clear explanation</li>
  </ul>
</div>

<div style="background: rgba(30, 41, 59, 0.5); border-left: 4px solid #64748b; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">Example Implementation:</h4>
  <div class="code-block-wrapper" style="background: #111827; border-radius: 0.5rem; padding: 1rem; margin: 1rem 0; border: 1px solid #374151;">
    <pre class="tutorial-code-block">// Example code with comments
function example() {
  // Implementation
  return result;
}</pre>
  </div>
  <p class="mt-4 text-gray-300">[Explanation of what this example demonstrates]</p>
</div>

<div style="background: rgba(133, 77, 14, 0.2); border-left: 4px solid #eab308; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">⚠️ Common Pitfalls:</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li>Pitfall 1 and how to avoid it</li>
    <li>Pitfall 2 and how to avoid it</li>
    <li>Pitfall 3 and how to avoid it</li>
  </ul>
</div>

<div style="background: rgba(76, 29, 149, 0.2); border-left: 4px solid #8b5cf6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">Practical Applications:</h4>
  <p class="mb-4 text-gray-300">
    [Real-world use cases where this concept is applied in production systems]
  </p>
</div>

<div style="background: rgba(20, 83, 45, 0.2); border-left: 4px solid #22c55e; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">✅ Best Practices:</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li>Write clear, self-documenting code</li>
    <li>Handle edge cases and errors properly</li>
    <li>Follow language conventions and idioms</li>
    <li>Test thoroughly with various inputs</li>
    <li>Keep functions focused and single-purpose</li>
  </ul>
</div>

<div style="background: rgba(49, 46, 129, 0.2); border-left: 4px solid #6366f1; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">🎯 When to Use:</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li>Use case 1</li>
    <li>Use case 2</li>
    <li>Use case 3</li>
  </ul>
</div>

<div style="background: rgba(19, 78, 74, 0.2); border-left: 4px solid #14b8a6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">🎓 Key Takeaways:</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li>Understand the core syntax and structure</li>
    <li>Know when to apply this pattern vs alternatives</li>
    <li>Practice with variations to build mastery</li>
    <li>Build on this foundation for advanced concepts</li>
  </ul>
</div>

<div style="background: rgba(131, 24, 67, 0.2); border-left: 4px solid #ec4899; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">📚 Further Learning:</h4>
  <p class="mb-4 text-gray-300">
    [Suggestions for related topics and next steps in the learning journey]
  </p>
</div>
```

### Section Color Reference

| Section | Background Color | Border Color | Icon |
|---------|------------------|--------------|------|
| Overview | rgba(31, 41, 55, 0.5) | #6b7280 | - |
| Key Concepts | rgba(30, 58, 138, 0.2) | #3b82f6 | 💡 |
| Example | rgba(30, 41, 59, 0.5) | #64748b | - |
| Common Pitfalls | rgba(133, 77, 14, 0.2) | #eab308 | ⚠️ |
| Practical Applications | rgba(76, 29, 149, 0.2) | #8b5cf6 | - |
| Best Practices | rgba(20, 83, 45, 0.2) | #22c55e | ✅ |
| Common Patterns | rgba(22, 78, 99, 0.2) | #06b6d4 | 🔄 |
| When to Use | rgba(49, 46, 129, 0.2) | #6366f1 | 🎯 |
| Key Takeaways | rgba(19, 78, 74, 0.2) | #14b8a6 | 🎓 |
| Further Learning | rgba(131, 24, 67, 0.2) | #ec4899 | 📚 |

---

## Additional Examples Template

```html
<h5>Additional Examples:</h5>

<div class="example-block">
  <h6>Example 1: Basic Usage</h6>
  <pre><code class="language-{language}">// Basic example code
const result = basicFunction();
console.log(result);
</code></pre>
  <p class="mt-2 text-gray-300">[Explanation of basic example]</p>
</div>

<div class="example-block">
  <h6>Example 2: Intermediate Pattern</h6>
  <pre><code class="language-{language}">// More complex example
class Example {
  constructor() {
    // Setup
  }

  process() {
    // Implementation
  }
}
</code></pre>
  <p class="mt-2 text-gray-300">[Explanation of intermediate example]</p>
</div>

<div class="example-block">
  <h6>Example 3: Advanced Application</h6>
  <pre><code class="language-{language}">// Production-ready example
async function advancedExample() {
  try {
    // Complex implementation
  } catch (error) {
    // Error handling
  }
}
</code></pre>
  <p class="mt-2 text-gray-300">[Explanation of advanced example with real-world context]</p>
</div>
```

---

## Quality Checklist

Before adding a lesson, verify:

### Structure ✓
- [ ] All required fields present
- [ ] ID is sequential and unique
- [ ] Language matches filename
- [ ] No empty required fields

### Content ✓
- [ ] Title is clear and descriptive (20-80 chars)
- [ ] Description is concise (80-200 chars, 1-2 sentences)
- [ ] fullSolution runs successfully
- [ ] expectedOutput matches actual output
- [ ] baseCode provides helpful structure
- [ ] Tutorial includes required sections (Overview, Best Practices, Key Takeaways)
- [ ] additionalExamples has 2-3 examples

### Code Quality ✓
- [ ] Code follows language conventions
- [ ] Proper indentation and formatting
- [ ] Helpful comments included
- [ ] fullSolution is 2-2.5x longer than baseCode
- [ ] No syntax errors
- [ ] Edge cases handled

### Tags & Metadata ✓
- [ ] 3-6 relevant tags
- [ ] Difficulty tag included in tags array
- [ ] Difficulty field matches tag
- [ ] Tags use Title Case
- [ ] Category is appropriate
- [ ] No redundant tags

### Tutorial Quality ✓
- [ ] HTML is properly formatted
- [ ] All sections use correct styling
- [ ] Code blocks use proper escaping
- [ ] Text is clear and educational
- [ ] Examples are relevant and tested

---

## Common Tag Sets by Topic

### Core Language Fundamentals
```json
["Beginner", "Variables", "Data Types", "Core"]
["Beginner", "Control Flow", "Conditionals", "Core"]
["Beginner", "Loops", "Iteration", "Core"]
["Beginner", "Functions", "Core"]
```

### Object-Oriented Programming
```json
["Intermediate", "OOP", "Classes", "Objects"]
["Intermediate", "OOP", "Inheritance"]
["Advanced", "OOP", "Polymorphism", "Abstraction"]
["Advanced", "OOP", "Design Patterns", "SOLID"]
```

### Data Structures
```json
["Intermediate", "Arrays", "Lists", "Collections"]
["Intermediate", "Hash Tables", "HashMap", "Collections"]
["Advanced", "Trees", "Binary Search", "Algorithms"]
["Advanced", "Graphs", "Algorithms"]
```

### Asynchronous Programming
```json
["Intermediate", "Async", "Promises"]
["Advanced", "Async", "Concurrency", "Async/Await"]
["Expert", "Async", "Multithreading", "Parallelism"]
```

### Web Development
```json
["Intermediate", "Web", "HTTP", "APIs"]
["Advanced", "Web", "REST", "API Design"]
["Expert", "Web", "Microservices", "Architecture"]
```

### Enterprise Patterns
```json
["Expert", "Enterprise", "Design Patterns", "Production"]
["Expert", "Testing", "TDD", "Best Practices"]
["Expert", "Security", "Authentication", "Production"]
["Expert", "Performance", "Optimization", "Production"]
```

---

## Lesson Progression Guidelines

### Beginner Lessons (12-18% of total)
- **Focus**: Language fundamentals
- **Code length**: 100-300 characters
- **Topics**: Variables, basic types, simple control flow, functions
- **Tutorial**: Extra detailed, explain everything
- **Example titles**:
  - "Variables and Basic Data Types"
  - "If Statements and Conditionals"
  - "For Loops and Iteration"
  - "Writing Your First Function"

### Intermediate Lessons (17-20% of total)
- **Focus**: Combining concepts, common patterns
- **Code length**: 300-600 characters
- **Topics**: Classes, collections, error handling, file I/O
- **Tutorial**: Balance detail with brevity
- **Example titles**:
  - "Working with Arrays and Lists"
  - "Object-Oriented Programming Basics"
  - "Exception Handling and Error Recovery"
  - "File Reading and Writing"

### Advanced Lessons (14-16% of total)
- **Focus**: Complex patterns, integration
- **Code length**: 600-1200 characters
- **Topics**: Advanced OOP, algorithms, async, databases
- **Tutorial**: Assume prior knowledge, focus on nuances
- **Example titles**:
  - "Implementing Design Patterns"
  - "Asynchronous Programming with Promises"
  - "Database Transactions and Optimization"
  - "Graph Algorithms and Traversal"

### Expert Lessons (50-55% of total)
- **Focus**: Production-ready, enterprise patterns
- **Code length**: 800-2000 characters
- **Topics**: Architecture, testing, security, performance, DevOps
- **Tutorial**: Focus on real-world application and best practices
- **Example titles**:
  - "Microservices Architecture Patterns"
  - "Implementing OAuth2 Authentication"
  - "Performance Profiling and Optimization"
  - "CI/CD Pipeline Configuration"

---

## Language-Specific Conventions

### Java
- Use `camelCase` for methods/variables
- Use `PascalCase` for classes
- Always include `public class Main` with `public static void main(String[] args)`
- Code must compile with `javac`

### Python
- Use `snake_case` for functions/variables
- Use `PascalCase` for classes
- Include type hints in advanced/expert lessons
- Follow PEP 8 style guide
- Code must run with `python3`

### JavaScript/TypeScript
- Use `camelCase` for functions/variables
- Use `PascalCase` for classes
- Use `const`/`let`, avoid `var`
- For TypeScript: include type annotations
- Code must run with `node`

### Go
- Use `camelCase` for private, `PascalCase` for public
- Always include `package main` and `func main()`
- Follow `gofmt` conventions
- Code must compile with `go build`

### Rust
- Use `snake_case` for functions/variables
- Use `PascalCase` for types
- Always include `fn main()`
- Follow `rustfmt` conventions
- Code must compile with `rustc`

---

## Example: Complete Lesson

```json
{
  "id": 42,
  "title": "Asynchronous Programming with Promises",
  "language": "javascript",
  "description": "Learn how to handle asynchronous operations using Promises. Master then(), catch(), and Promise chaining patterns.",
  "fullSolution": "// Fetch user data asynchronously\nfunction fetchUser(userId) {\n  return new Promise((resolve, reject) => {\n    setTimeout(() => {\n      if (userId > 0) {\n        resolve({ id: userId, name: 'Alice' });\n      } else {\n        reject(new Error('Invalid user ID'));\n      }\n    }, 1000);\n  });\n}\n\n// Use the promise\nfetchUser(1)\n  .then(user => {\n    console.log(`User: ${user.name}`);\n    return user.id;\n  })\n  .then(id => {\n    console.log(`ID: ${id}`);\n  })\n  .catch(error => {\n    console.error(`Error: ${error.message}`);\n  });",
  "expectedOutput": "User: Alice\nID: 1",
  "baseCode": "// TODO: Create a function that returns a Promise\n// TODO: The promise should resolve with user data after 1 second\n// TODO: Use .then() to handle the resolved value\n// TODO: Use .catch() to handle errors\n\nfunction fetchUser(userId) {\n  // Your code here\n}\n\n// Chain promises here",
  "tutorial": "[Full HTML tutorial as per template above]",
  "tags": ["Intermediate", "Async", "Promises", "JavaScript"],
  "additionalExamples": "[HTML examples as per template above]",
  "difficulty": "Intermediate",
  "category": "Async"
}
```

---

## Validation Scripts

Use the provided `validate_lessons.py` script to check:
- Required fields present
- ID sequence correctness
- Code compilation/execution
- Tag consistency
- Tutorial section presence
- Output accuracy

Run: `python scripts/validate_lessons.py lessons-{language}.json`

---

## Quick Start: Adding Your First Lesson

1. **Copy the example lesson structure** above
2. **Update all fields** with your content
3. **Test your code** - make sure fullSolution runs correctly
4. **Verify expectedOutput** - run the code and copy actual output
5. **Write the tutorial** using the HTML template
6. **Add 2-3 additional examples**
7. **Choose appropriate tags** (3-6, including difficulty)
8. **Set difficulty and category**
9. **Run validation** to check for issues
10. **Add to lessons array** in sequential order

---

## Support

For questions or issues:
- Review existing lessons for reference
- Check the validation output for specific errors
- Follow the patterns used in Java and Python lessons
- Maintain consistency with the established structure

**Remember**: Quality over quantity! Each lesson should be educational, tested, and production-ready.
