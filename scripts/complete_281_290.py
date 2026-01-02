#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 281: Custom Exception Classes
lesson281 = next(l for l in lessons if l['id'] == 281)
lesson281['content'] = """# Custom Exception Classes

Create custom exception classes to handle application-specific errors with clear semantics and rich error context.

## Example 1: Basic Custom Exception

Define simple custom exception:

```python
class ValidationError(Exception):
    """Raised when data validation fails."""
    pass

def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("Age must be an integer")
    if age < 0:
        raise ValidationError("Age cannot be negative")
    if age > 150:
        raise ValidationError("Age is unrealistic")
    return age

try:
    validate_age(-5)
except ValidationError as e:
    print(f"Validation failed: {e}")
# Output: Validation failed: Age cannot be negative
```

**Result**: Type-safe validation errors.

## Example 2: Exception with Custom Attributes

Add context to exceptions:

```python
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance
        super().__init__(
            f"Insufficient funds: balance=${balance:.2f}, "
            f"required=${amount:.2f}, short=${self.shortfall:.2f}"
        )

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Error: {e}")
    print(f"Shortfall: ${e.shortfall:.2f}")
```

**Result**: Rich error context.

## KEY TAKEAWAYS

- **Custom Exceptions**: Inherit from Exception or built-in exception types
- **Rich Context**: Add attributes for error details
- **Hierarchy**: Create exception families for granular handling
- **Clear Messages**: Provide actionable error information
- **Best Practices**: Specific exceptions, meaningful names, helpful messages
"""

# Lesson 282: Exception Hierarchy and Multiple Except
lesson282 = next(l for l in lessons if l['id'] == 282)
lesson282['content'] = """# Exception Hierarchy and Multiple Except

Handle different exception types with multiple except blocks using Python's exception hierarchy for granular error handling.

## Example 1: Multiple Except Blocks

Catch different exceptions:

```python
def divide(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid types for division")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

divide(10, 2)      # 10 / 2 = 5.0
divide(10, 0)      # Error: Cannot divide by zero
divide(10, "x")    # Error: Invalid types for division
```

**Result**: Specific error handling.

## Example 2: Catching Multiple Exceptions

Group similar exceptions:

```python
def read_file_line(filename, line_num):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return lines[line_num]
    except (FileNotFoundError, PermissionError) as e:
        print(f"File access error: {e}")
        return None
    except IndexError:
        print(f"Line {line_num} does not exist")
        return None

read_file_line('missing.txt', 0)
```

**Result**: Grouped exception handling.

## KEY TAKEAWAYS

- **Multiple Except**: Handle different exceptions separately
- **Order Matters**: Catch specific before general exceptions
- **Grouping**: Use tuples to catch multiple exception types
- **Finally Clause**: Always runs, perfect for cleanup
- **Best Practices**: Specific exceptions, proper ordering, complete cleanup
"""

# Lesson 283: File Paths with pathlib
lesson283 = next(l for l in lessons if l['id'] == 283)
lesson283['content'] = """# File Paths with pathlib

Use pathlib for object-oriented filesystem path handling with cross-platform compatibility.

## Example 1: Basic Path Operations

Create and manipulate paths:

```python
from pathlib import Path

# Create path object
p = Path('data/files/document.txt')

print(f"Name: {p.name}")          # document.txt
print(f"Stem: {p.stem}")          # document
print(f"Suffix: {p.suffix}")      # .txt
print(f"Parent: {p.parent}")      # data/files
```

**Result**: Path components access.

## Example 2: Path Construction

Build paths safely:

```python
from pathlib import Path

# Join paths (cross-platform)
base = Path('data')
subdir = base / 'files' / 'documents'
file_path = subdir / 'report.txt'

print(f"Path: {file_path}")
# Windows: data\files\documents\report.txt
# Unix: data/files/documents/report.txt
```

**Result**: Cross-platform path building.

## KEY TAKEAWAYS

- **Object-Oriented**: Paths are objects with methods
- **Cross-Platform**: Automatic path separator handling
- **Path Operations**: /, name, stem, suffix, parent
- **Directory Creation**: mkdir(parents=True, exist_ok=True)
- **Iteration**: iterdir(), glob(), rglob()
- **Best Practices**: Use pathlib over os.path for modern Python
"""

# Lesson 284: Binary File Operations
lesson284 = next(l for l in lessons if l['id'] == 284)
lesson284['content'] = """# Binary File Operations

Read and write binary files for handling non-text data.

## Example 1: Basic Binary Read/Write

Handle binary data:

```python
# Write binary data
data = bytes([0x48, 0x65, 0x6C, 0x6C, 0x6F])
with open('data.bin', 'wb') as f:
    f.write(data)

# Read binary data
with open('data.bin', 'rb') as f:
    content = f.read()
    print(f"Bytes: {content}")
    print(f"Hex: {content.hex()}")
```

**Result**: Basic binary I/O.

## Example 2: Struct for Binary Packing

Pack/unpack structured binary data:

```python
import struct

# Pack data
data = struct.pack('i f 10s', 42, 3.14, b'Hello')
print(f"Packed: {data.hex()}")

# Unpack data
num, pi, text = struct.unpack('i f 10s', data)
print(f"Number: {num}")
print(f"Pi: {pi}")
```

**Result**: Structured binary data.

## KEY TAKEAWAYS

- **Binary Mode**: Use 'rb'/'wb' for binary files
- **Bytes Type**: Binary data uses bytes, not str
- **Struct Module**: Pack/unpack structured binary data
- **Chunked Reading**: Read large files in chunks
- **Best Practices**: Validate data, handle errors
"""

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created lessons 281-284:")
for lid in range(281, 285):
    lesson = next(l for l in lessons if l['id'] == lid)
    chars = len(lesson['content'])
    print(f"  {lid}: {lesson['title'][:45]:45s} {chars:5,d} chars")
