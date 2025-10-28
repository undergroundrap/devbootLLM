# Track Switching Issues Found

## Issue 1: Double loadLesson() Call ⚠️

### Problem
When switching tracks, `loadLesson()` is called **twice**:

1. **First call**: In `loadLessonsForTrack()` finally block (line 1652)
   ```javascript
   finally {
       this.loadLesson(this.currentLessonIndex, { isReload: true });
   }
   ```

2. **Second call**: In `loadStateFromDb()` (line 1711)
   ```javascript
   loadStateFromDb(state) {
       this.currentLessonIndex = state.currentLessonIndex || 0;
       this.loadLesson(this.currentLessonIndex, {isReload: true});
   }
   ```

### Call Stack
```
switchCourse('python')
  ├─> loadLessonsForTrack('python')
  │    └─> [finally] loadLesson(currentLessonIndex)  // CALL #1
  └─> storageService.loadData()
       └─> loadStateFromDb(state)
            └─> loadLesson(state.currentLessonIndex)  // CALL #2
```

### Impact
- **Performance**: Unnecessary lesson loading
- **UI flicker**: Lesson might flash between two different lessons
- **Potential race condition**: If CALL #1 hasn't finished when CALL #2 starts

### Scenario
1. User is on Java lesson index 50 (ID 50: "2D Arrays")
2. User switches to Python
3. Python lessons load (700 lessons)
4. CALL #1: Loads Python lesson at index 50 (whatever `currentLessonIndex` is NOW)
5. CALL #2: Loads Python lesson from saved state (might be different index)
6. User sees wrong lesson briefly, then correct lesson

### Severity
**Medium** - Causes confusion but doesn't break functionality

---

## Issue 2: Incorrect Lesson Shown After Switch (Potential)

### Problem
The `finally` block in `loadLessonsForTrack()` calls `loadLesson(this.currentLessonIndex)` using the CURRENT index, but this index might not be correct for the new track.

### Scenario
1. User on Java, `currentLessonIndex = 50`
2. Switches to Python
3. Python lessons load
4. `finally` block runs: `loadLesson(50)` - Loads Python lesson 50
5. Then `loadStateFromDb()` runs with saved Python state: `currentLessonIndex = 75`
6. `loadLesson(75)` - Loads Python lesson 75

**Result**: User briefly sees lesson 50, then jumps to lesson 75

### Expected Behavior
User should see lesson 75 immediately (their last saved position in Python)

### Severity
**Medium** - Confusing UX, shows wrong lesson briefly

---

## Issue 3: Missing Bounds Check in Finally Block

### Problem
Line 1644-1646:
```javascript
if (this.currentLessonIndex >= this.lessons.length) {
    this.currentLessonIndex = 0;
}
```

This checks if index is >= length, but doesn't check if lessons array is empty or if index is negative.

### Potential Edge Cases
- If `this.lessons.length === 0`: Will set index to 0, then try to load lesson 0 (undefined)
- If `this.currentLessonIndex === -1`: Will not be caught

### Severity
**Low** - Edge case, unlikely to occur

---

## Recommended Fixes

### Fix 1: Remove Duplicate loadLesson() Call

**Option A**: Remove from `loadLessonsForTrack` finally block
```javascript
finally {
    if (this.currentLessonIndex >= this.lessons.length) {
        this.currentLessonIndex = 0;
    }
    if (this.elements && this.elements.lessonList) {
        this.refreshTagFilterOptions();
        this.initTagFilter();
        this.populateLessonSidebar();
        // REMOVE: this.loadLesson(this.currentLessonIndex, { isReload: true });
    }
}
```

**Reasoning**: Let `loadStateFromDb()` be responsible for loading the correct lesson

**Option B**: Add flag to prevent double loading
```javascript
finally {
    // ...
    if (!options.skipLoadLesson) {
        this.loadLesson(this.currentLessonIndex, { isReload: true });
    }
}
```

Then when called from `switchCourse`:
```javascript
await this.loadLessonsForTrack(track, { skipLoadLesson: true });
```

### Fix 2: Better Bounds Checking

```javascript
finally {
    // Ensure valid lesson index
    if (!this.lessons || this.lessons.length === 0) {
        this.currentLessonIndex = 0;
    } else if (this.currentLessonIndex < 0 || this.currentLessonIndex >= this.lessons.length) {
        this.currentLessonIndex = 0;
    }
    // ...
}
```

---

## Testing Recommendations

### Test Case 1: Basic Switch
1. Start on Java lesson 1
2. Switch to Python
3. **Expected**: See Python lesson 0 or last saved Python lesson
4. **Check**: No UI flicker, single lesson load

### Test Case 2: Preserved Position
1. Java lesson 50, switch to Python (Python shows lesson 20)
2. Switch back to Java
3. **Expected**: Return to Java lesson 50
4. **Check**: Progress is preserved per track

### Test Case 3: Rapid Switching
1. Click Java -> Python -> Java -> Python rapidly
2. **Expected**: No crashes, final track is correct
3. **Check**: Console logs show proper cleanup

### Test Case 4: Bounds Edge Case
1. On Java lesson 699 (last lesson)
2. Switch to Python
3. **Expected**: Show valid Python lesson (not crash)
4. **Check**: Index is properly bounded

---

## Current Status

✅ **Bounds checking exists** in `loadLesson()` (line 1003)
⚠️ **Double loading occurs** when switching tracks
⚠️ **Potential UI flicker** between lessons
✅ **Separate storage keys** prevent progress contamination
✅ **Lessons properly filtered** by language

## Priority

**Should fix**: Issue #1 (double loading) - causes poor UX
**Nice to fix**: Issue #2 (better bounds checking) - edge case prevention
**Low priority**: Other edge cases - unlikely to occur

---

## Implementation Status

- [x] Issues identified
- [ ] Fixes implemented
- [ ] Tests created
- [ ] Verified in browser
