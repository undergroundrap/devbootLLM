# Track Switching Analysis

## Current Flow

When switching from Java to Python (or vice versa):

1. `switchCourse(track)` is called
2. `this.currentTrack = track` - Updates current track
3. `localStorage.setItem('courseTrack', track)` - Saves track preference
4. `this.storageService.storageKey = this.getStorageKey()` - Changes storage key
   - Java: `devbootllm-java-progress`
   - Python: `devbootllm-python-progress`
5. `await this.loadLessonsForTrack(track)` - Loads 700 lessons for new track
6. `this.storageService.loadData()` - Loads saved state for this track
7. `loadStateFromDb(state)` is called with saved state
8. Sets `this.currentLessonIndex`, `this.userCode`, `this.lessonCompletion`
9. Calls `this.loadLesson(this.currentLessonIndex)` - **Loads the lesson at saved index**

## Potential Issues

### Issue 1: Lesson Index Confusion ⚠️
**Scenario**:
- User is on Java lesson 50 (ID 50: "2D Arrays")
- Switches to Python
- Python track loads lesson at index 50
- But Python lesson 50 is "Context Managers" (different content)

**Is this a problem?**
- **NO** - This is expected behavior!
- Each track maintains its own progress
- If user was last on Python lesson 100, they should return to lesson 100 when switching back
- The lesson IDs match (1-735) but content differs intentionally

### Issue 2: Wrong Lesson Content Shown ⚠️
**Scenario**:
- Could lessons show Java code when Python is selected?

**Root Cause Analysis**:
- Lessons are loaded via `loadLessonsForTrack(track)`
- This loads from `/lessons-python.json` or `/lessons-java.json`
- Then filtered by `language` field
- `this.lessons` array is replaced entirely

**Verification needed**:
- Check if `this.lessons` is properly cleared before loading new track
- Check if any caching could show old lessons

### Issue 3: Progress Contamination ⚠️
**Scenario**:
- Could Java progress affect Python progress?

**Root Cause Analysis**:
- Each track has separate localStorage key
- Java: `devbootllm-java-progress`
- Python: `devbootllm-python-progress`
- Storage key is updated BEFORE loading state

**Status**: Should be isolated ✅

### Issue 4: Lesson Loading Race Condition ⚠️
**Scenario**:
- User switches tracks rapidly
- Could old lessons show for new track?

**Code Flow**:
```javascript
// Line 1161: await this.loadLessonsForTrack(track);
// Line 1162: console.log('[switchCourse] After loadLessonsForTrack...')
// Line 1164: this.storageService.loadData();
```

**Status**: `await` ensures lessons load before state ✅

### Issue 5: currentLessonIndex Bounds Check ❓
**Check needed**:
```javascript
loadStateFromDb(state) {
    this.currentLessonIndex = state.currentLessonIndex || 0;
    // ...
    this.loadLesson(this.currentLessonIndex, {isReload: true});
}
```

**Question**: What if `currentLessonIndex` > 700?
- If user somehow had index 750 saved
- Would try to load `this.lessons[750]` which is undefined

Let me check if there's bounds checking in `loadLesson()`...

## Recommended Checks

1. ✅ Verify `this.lessons` is cleared before loading new track
2. ❓ Check if `loadLesson()` has bounds checking
3. ✅ Verify localStorage keys are properly separated
4. ❓ Test rapid track switching
5. ❓ Check if sidebar shows correct lessons after switch
