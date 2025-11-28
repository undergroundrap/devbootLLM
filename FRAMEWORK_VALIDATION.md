# Framework Lesson Validation - Implementation Guide

## Overview

Framework lessons (Flask, Django, Spring Boot, etc.) cannot be executed in the platform without installing heavy dependencies. Instead, we provide **syntax-only validation** with clear user messaging.

## How It Works

### 1. Lesson Tagging

All 302 framework lessons are now tagged with:
```json
{
  "id": 148,
  "title": "Spring-Style Controller Method",
  "isFramework": true,
  "frameworkName": "Spring",
  ...
}
```

- `isFramework`: Boolean flag indicating this needs external dependencies
- `frameworkName`: Name of framework (Flask, Django, Spring, etc.)

### 2. Syntax Validation

When a framework lesson is run:

**Python:**
```python
# Syntax-only check (no execution)
try:
    compile(code, '<string>', 'exec')
    return {"success": True, "message": "✓ Syntax valid", "isFramework": True}
except SyntaxError as e:
    return {"success": False, "error": str(e), "isFramework": True}
```

**Java:**
```bash
# Compile only (don't run)
javac Main.java
# Return compilation result
```

### 3. User Messaging

The UI shows clear indicators:

**Badge:** "Framework Example - {FrameworkName}"

**Message:**
```
This lesson demonstrates real {Framework} code.

✓ Your code is syntactically valid
ℹ️ To run this code locally, install: pip install {framework}

Expected Output:
{expectedOutput}
```

## Benefits

✅ Students learn real framework code patterns
✅ Code is verified for syntax errors
✅ Clear expectations set (not executable in platform)
✅ expectedOutput shows what code should produce
✅ Fast validation (no framework installation needed)
✅ Small Docker image (500MB vs 5GB)

## Implementation

### Current Status

1. ✅ All framework lessons tagged with isFramework flag
2. ⏳ Server endpoints updated to handle framework lessons
3. ⏳ UI updated to show framework badges
4. ⏳ Clear user messaging added

### Server Changes Needed

Update `/run/python` and `/run/java` endpoints:

```javascript
app.post('/run/python', (req, res) => {
    const { code, isFramework, frameworkName } = req.body;

    // If it's a framework lesson, only validate syntax
    if (isFramework) {
        return validatePythonSyntax(code, frameworkName, res);
    }

    // Otherwise, run normally
    executePythonCode(code, res);
});
```

### Frontend Changes Needed

Show badge and message for framework lessons:

```javascript
if (lesson.isFramework) {
    showFrameworkBadge(lesson.frameworkName);
    showFrameworkMessage(lesson.frameworkName, lesson.expectedOutput);
}
```

## Testing

After implementation:

1. Test non-framework lesson (should run normally)
2. Test framework lesson (should show syntax validation only)
3. Test syntax error in framework lesson (should show error)
4. Verify UI shows appropriate badges and messages

## Rollout Plan

1. Update server.js with framework validation logic
2. Update frontend to detect isFramework flag
3. Add UI badges and messaging
4. Test with sample lessons
5. Deploy

## FAQ

**Q: Can students run framework code at all?**
A: Yes, locally. The lesson shows them real code + installation instructions.

**Q: Does this affect learning?**
A: No - students learn by reading and typing code, not running it.

**Q: What about expectedOutput?**
A: Still shown - students see what the code should produce.

**Q: Can we add real execution later?**
A: Yes - can provide optional Docker images for power users.
