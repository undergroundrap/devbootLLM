#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

lesson291 = next(l for l in lessons if l['id'] == 291)
lesson291['content'] = """# Type Hints

Add type annotations for better code documentation.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

from typing import List, Optional

def process(items: List[int]) -> Optional[int]:
    return max(items) if items else None
```

## KEY TAKEAWAYS

- **Annotations**: Specify types for parameters and returns
- **Optional**: Type or None
- **typing Module**: Import type utilities
- **IDE Support**: Better autocomplete
- **No Runtime Check**: For documentation/tools only
"""

lesson292 = next(l for l in lessons if l['id'] == 292)
lesson292['content'] = """# itertools.chain

Combine multiple iterables into one sequence.

```python
from itertools import chain

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list(chain(list1, list2))
print(combined)  # [1, 2, 3, 4, 5, 6]

# Flatten nested lists
lists = [[1, 2], [3, 4], [5, 6]]
flat = list(chain.from_iterable(lists))
```

## KEY TAKEAWAYS

- **chain()**: Combine iterables sequentially
- **Lazy**: Returns iterator
- **from_iterable()**: Flatten nested
- **Efficient**: No intermediate lists
- **Any Iterable**: Works with all iterables
"""

lesson293 = next(l for l in lessons if l['id'] == 293)
lesson293['title'] = 'String Join - Comma Delimiter'
lesson293['content'] = """# String Join - Comma Delimiter

Join sequences with delimiters.

```python
words = ['apple', 'banana', 'cherry']
result = ', '.join(words)
print(result)  # apple, banana, cherry

numbers = [1, 2, 3]
joined = ', '.join(map(str, numbers))
```

## KEY TAKEAWAYS

- **str.join()**: Concatenate strings
- **Delimiter**: String between elements
- **Efficient**: Better than + loop
- **map(str)**: Convert non-strings
- **Common Use**: CSV, text formatting
"""

lesson294 = next(l for l in lessons if l['id'] == 294)
lesson294['content'] = """# defaultdict

Auto-initialize missing keys with default values.

```python
from collections import defaultdict

# Count occurrences
counts = defaultdict(int)
for word in ['a', 'b', 'a', 'c', 'b', 'a']:
    counts[word] += 1

# Group items
groups = defaultdict(list)
for item in [('fruit', 'apple'), ('veg', 'carrot')]:
    groups[item[0]].append(item[1])
```

## KEY TAKEAWAYS

- **Auto-Initialize**: No KeyError
- **Factory**: Pass callable for default
- **int**: Defaults to 0
- **list**: Defaults to []
- **Counting/Grouping**: Common use cases
"""

lesson295 = next(l for l in lessons if l['id'] == 295)
lesson295['content'] = """# deque

Double-ended queue for efficient operations.

```python
from collections import deque

d = deque([1, 2, 3])
d.append(4)       # Right end
d.appendleft(0)   # Left end
print(d)  # deque([0, 1, 2, 3, 4])

d.pop()          # Remove from right
d.popleft()      # Remove from left

# Rotate
d.rotate(1)      # Rotate right
```

## KEY TAKEAWAYS

- **Double-Ended**: Operations on both ends
- **O(1)**: Fast append/pop both sides
- **rotate()**: Rotate elements
- **maxlen**: Auto size limiting
- **Queue**: Better than list for queues
"""

lesson296 = next(l for l in lessons if l['id'] == 296)
lesson296['content'] = """# namedtuple

Lightweight immutable data structures.

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print(p.x, p.y)  # Access by name
print(p[0], p[1])  # Access by index

# Convert
print(p._asdict())  # To dict
p2 = p._replace(x=100)  # Create modified copy
```

## KEY TAKEAWAYS

- **Named Fields**: Access by name
- **Immutable**: Cannot modify
- **Lightweight**: Memory efficient
- **_asdict()**: Convert to dict
- **Readable**: Self-documenting code
"""

lesson297 = next(l for l in lessons if l['id'] == 297)
lesson297['content'] = """# contextmanager

Create custom context managers easily.

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.2f}s")

with timer():
    # Code to time
    sum(range(1000000))
```

## KEY TAKEAWAYS

- **@contextmanager**: Decorator for contexts
- **yield**: Separates setup/teardown
- **try/finally**: Ensure cleanup
- **Resource Management**: Handle setup/cleanup
- **Simpler**: Easier than __enter__/__exit__
"""

lesson298 = next(l for l in lessons if l['id'] == 298)
lesson298['content'] = """# suppress

Suppress specific exceptions cleanly.

```python
from contextlib import suppress
import os

# Suppress exceptions
with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')

# Multiple exceptions
with suppress(ValueError, TypeError):
    int('not a number')

# Cleaner than try/except pass
```

## KEY TAKEAWAYS

- **suppress()**: Ignore exceptions
- **Multiple Types**: Suppress many types
- **Cleaner**: More readable than try/pass
- **Expected Errors**: For anticipated exceptions
- **Use Cases**: File cleanup, optional operations
"""

lesson299 = next(l for l in lessons if l['id'] == 299)
lesson299['content'] = """# pathlib

Object-oriented filesystem paths.

```python
from pathlib import Path

p = Path('data/file.txt')
print(p.name)    # file.txt
print(p.suffix)  # .txt
print(p.parent)  # data

# Join paths
path = Path('data') / 'files' / 'doc.txt'

# Operations
p.exists()
p.mkdir(exist_ok=True)
p.write_text('Hello')
```

## KEY TAKEAWAYS

- **Object-Oriented**: Paths as objects
- **/ Operator**: Join paths
- **Cross-Platform**: Auto path separators
- **Properties**: name, suffix, parent
- **Methods**: exists(), mkdir(), read_text()
"""

lesson300 = next(l for l in lessons if l['id'] == 300)
lesson300['content'] = """# JSON dumps

Convert Python objects to JSON strings.

```python
import json

data = {'name': 'Alice', 'age': 30}
json_str = json.dumps(data)
print(json_str)

# Pretty print
formatted = json.dumps(data, indent=2)

# Options
json.dumps(data, sort_keys=True)
json.dumps(data, ensure_ascii=False)
```

## KEY TAKEAWAYS

- **json.dumps()**: Python to JSON string
- **json.dump()**: Write to file
- **indent**: Pretty printing
- **sort_keys**: Sort dictionary keys
- **ensure_ascii**: Control encoding
"""

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created lessons 291-300:")
for lid in range(291, 301):
    lesson = next(l for l in lessons if l['id'] == lid)
    chars = len(lesson['content'])
    print(f"  {lid}: {lesson['title'][:45]:45s} {chars:5,d} chars")
