#!/usr/bin/env python3
import json

with open("public/lessons-python.json", "r", encoding="utf-8") as f:
    lessons = json.load(f)

lesson285 = next(l for l in lessons if l["id"] == 285)
lesson285["content"] = """# JSON File Handling

Read, write, and manipulate JSON files.

## Example: Basic JSON Operations

```python
import json

data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json", "r") as f:
    loaded = json.load(f)
```

## KEY TAKEAWAYS

- **json.dump()**: Write to file
- **json.load()**: Read from file
- **json.dumps()**: Convert to string
- **json.loads()**: Parse string
- **indent**: Pretty-print
"""

lesson286 = next(l for l in lessons if l["id"] == 286)
lesson286["content"] = """# zip() Pairs

Combine multiple iterables element-wise.

## Example: Basic zip

```python
names = ["Alice", "Bob"]
ages = [25, 30]

for name, age in zip(names, ages):
    print(f"{name} is {age}")

user_dict = dict(zip(names, ages))
```

## KEY TAKEAWAYS

- **zip()**: Combine iterables
- **dict()**: Create from pairs
- **Unzip**: Use zip(*iterable)
- **Lazy**: Returns iterator
- **Length**: Stops at shortest
"""

lesson287 = next(l for l in lessons if l["id"] == 287)
lesson287["content"] = """# Git Commit Summary

Analyze Git commits programmatically.

## Example: Get Commits

```python
import subprocess

result = subprocess.run(
    ["git", "log", "-5", "--format=%H|%an|%s"],
    capture_output=True,
    text=True
)

for line in result.stdout.splitlines():
    hash, author, msg = line.split("|")
    print(f"{hash[:7]} - {msg}")
```

## KEY TAKEAWAYS

- **subprocess**: Run Git commands
- **Parsing**: Extract metadata
- **Automation**: Git workflows
- **Analysis**: Generate reports
- **Integration**: CI/CD pipelines
"""

lesson288 = next(l for l in lessons if l["id"] == 288)
lesson288["content"] = """# Git Merge Plan

Plan and analyze Git merges.

## Example: Check Merge

```python
import subprocess

def get_merge_base(b1, b2):
    result = subprocess.run(
        ["git", "merge-base", b1, b2],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

base = get_merge_base("main", "feature")
print(f"Merge base: {base[:7]}")
```

## KEY TAKEAWAYS

- **Merge Base**: Find common ancestor
- **Commit Range**: List commits
- **Conflict Detection**: Check issues
- **Planning**: Analyze before merge
- **Safety**: Validate first
"""

lesson289 = next(l for l in lessons if l["id"] == 289)
lesson289["content"] = """# Type Hints and Generics

Use type hints for documentation and IDE support.

## Example: Type Hints

```python
from typing import List, Optional

def greet(name: str) -> str:
    return f"Hello, {name}"

def sum_list(nums: List[int]) -> int:
    return sum(nums)

def find_user(id: int) -> Optional[dict]:
    return None if id < 0 else {"name": "Alice"}
```

## KEY TAKEAWAYS

- **Type Hints**: Add annotations
- **Optional**: Value or None
- **Union**: Multiple types
- **Generics**: Type-safe classes
- **IDE Support**: Better autocomplete
"""

lesson290 = next(l for l in lessons if l["id"] == 290)
lesson290["content"] = """# Pickle Serialization

Serialize Python objects to binary format.

## Example: Pickle Objects

```python
import pickle

data = {"name": "Alice", "scores": [95, 87]}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)
    print(loaded)
```

## KEY TAKEAWAYS

- **pickle.dump()**: Serialize to file
- **pickle.load()**: Deserialize
- **Binary Format**: Efficient storage
- **Security**: Never unpickle untrusted data
- **Alternatives**: Use JSON for interoperability
"""

with open("public/lessons-python.json", "w", encoding="utf-8") as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created lessons 285-290:")
for lid in range(285, 291):
    lesson = next(l for l in lessons if l["id"] == lid)
    chars = len(lesson["content"])
    print(f"  {lid}: {lesson["title"][:45]:45s} {chars:5,d} chars")
