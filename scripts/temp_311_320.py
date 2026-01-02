import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 311
lesson311 = next(l for l in lessons if l['id'] == 311)
lesson311['title'] = 'Optional Values - Default Value'
lesson311['content'] = """# Optional Values and Defaults

Handle optional values with defaults.

```python
# Dict.get() with default
config = {'port': 8080}
host = config.get('host', 'localhost')

# or operator
name = user_name or 'Anonymous'

# getattr() with default
value = getattr(obj, 'attr', 'default')
```

## KEY TAKEAWAYS

- get() for dict defaults
- or for truthy defaults
- getattr() for object defaults
- is not None for explicit checks
- Default parameters in functions
"""

# Lesson 312
lesson312 = next(l for l in lessons if l['id'] == 312)
lesson312['title'] = 'String Join - Custom Delimiter'
lesson312['content'] = """# String Join with Custom Delimiter

Join strings with delimiters.

```python
words = ['apple', 'banana']
result = ', '.join(words)
print(result)  # apple, banana

# Custom delimiters
print(' | '.join(words))
print(' -> '.join(words))

# Numbers
nums = [1, 2, 3]
result = '-'.join(map(str, nums))
```

## KEY TAKEAWAYS

- str.join() combines strings
- Delimiter is joining string
- map(str) for non-strings
- More efficient than loops
- Common for CSV, formatting
"""

# Lesson 313-320 (simplified for now)
for lid in range(313, 321):
    lesson = next(l for l in lessons if l['id'] == lid)
    if lid == 313:
        lesson['content'] = "# Release Checklist\n\nAutomate release verification.\n\n## KEY TAKEAWAYS\n\n- Automate checks\n- Verify tests pass\n- Check version\n- Prevent bad releases"
    elif lid == 314:
        lesson['content'] = "# Smoke Tests\n\nBasic deployment checks.\n\n## KEY TAKEAWAYS\n\n- Test critical endpoints\n- Quick verification\n- Run after deploy\n- Catch issues early"
    elif lid == 315:
        lesson['content'] = "# glob\n\nFind files by pattern.\n\n```python\nimport glob\npy_files = glob.glob('*.py')\nall_py = glob.glob('**/*.py', recursive=True)\n```\n\n## KEY TAKEAWAYS\n\n- glob() finds files\n- ** for recursive\n- Returns list of paths"
    elif lid == 316:
        lesson['content'] = "# decimal\n\nPrecise decimal math.\n\n```python\nfrom decimal import Decimal\na = Decimal('0.1')\nb = Decimal('0.2')\nprint(a + b)  # 0.3\n```\n\n## KEY TAKEAWAYS\n\n- Exact decimal arithmetic\n- Better than float for money\n- Use string constructor"
    elif lid == 317:
        lesson['content'] = "# fractions\n\nRational numbers.\n\n```python\nfrom fractions import Fraction\nf = Fraction(1, 3)\nprint(f + f)  # 2/3\n```\n\n## KEY TAKEAWAYS\n\n- Exact rational numbers\n- Auto simplification\n- Access numerator/denominator"
    elif lid == 318:
        lesson['content'] = "# bisect_left\n\nBinary search.\n\n```python\nimport bisect\npos = bisect.bisect_left([1,3,5], 4)\nprint(pos)  # 2\n```\n\n## KEY TAKEAWAYS\n\n- O(log n) search\n- List must be sorted\n- Returns insertion point"
    elif lid == 319:
        lesson['content'] = "# statistics.mean\n\nStatistical functions.\n\n```python\nfrom statistics import mean\navg = mean([1,2,3,4,5])\nprint(avg)  # 3\n```\n\n## KEY TAKEAWAYS\n\n- mean() for average\n- median() for middle\n- mode() for most common"
    elif lid == 320:
        lesson['content'] = "# frozenset\n\nImmutable set.\n\n```python\nfs = frozenset([1,2,3])\ndata = {fs: 'value'}\n```\n\n## KEY TAKEAWAYS\n\n- Immutable set\n- Hashable\n- Can be dict key\n- Cannot modify"

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created lessons 311-320:")
for lid in range(311, 321):
    lesson = next(l for l in lessons if l['id'] == lid)
    chars = len(lesson['content'])
    print(f"  {lid}: {lesson['title'][:45]:45s} {chars:5,d} chars")
