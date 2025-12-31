#!/usr/bin/env python3
"""
Upgrade Python lessons 92-100 with comprehensive content.
- Lesson 92: Dictionaries
- Lesson 93: Dictionary Fundamentals
- Lesson 94: Dictionary Updates
- Lesson 95: Iterate Dict (keys)
- Lesson 96: Iterating Dictionaries
- Lesson 97: Lambda + map
- Lesson 98: Lambda/map/filter
- Lesson 99: Removing from Dictionaries
- Lesson 100: Sort Dicts
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 92-100
lesson92 = next(l for l in lessons if l['id'] == 92)
lesson93 = next(l for l in lessons if l['id'] == 93)
lesson94 = next(l for l in lessons if l['id'] == 94)
lesson95 = next(l for l in lessons if l['id'] == 95)
lesson96 = next(l for l in lessons if l['id'] == 96)
lesson97 = next(l for l in lessons if l['id'] == 97)
lesson98 = next(l for l in lessons if l['id'] == 98)
lesson99 = next(l for l in lessons if l['id'] == 99)
lesson100 = next(l for l in lessons if l['id'] == 100)

# Upgrade Lesson 92: Dictionaries
lesson92['fullSolution'] = '''"""
Dictionaries

Master Python dictionaries—the fundamental key-value data structure for
mapping, caching, configuration, and data organization. Learn creation,
access, modification, and best practices. Essential for all Python programs.

**Zero Package Installation Required**
"""

# Example 1: What Are Dictionaries?
print("="*70)
print("Example 1: Dictionary Basics - Key-Value Pairs")
print("="*70)

# Dictionary stores data as key: value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}

print("Dictionary:")
print(person)
print(f"\\nType: {type(person)}")
print(f"Length: {len(person)} key-value pairs")

# Access values by key
print(f"\\nName: {person['name']}")
print(f"Age: {person['age']}")
print()

# Example 2: Dictionaries vs Lists
print("="*70)
print("Example 2: When to Use Dictionaries vs Lists")
print("="*70)

# List - ordered, indexed by position
scores_list = [95, 87, 92, 78]
print(f"List: {scores_list}")
print(f"Access by index: scores_list[0] = {scores_list[0]}")

# Dictionary - unordered (Python 3.7+ maintains insertion order)
scores_dict = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "David": 78
}
print(f"\\nDictionary: {scores_dict}")
print(f"Access by key: scores_dict['Alice'] = {scores_dict['Alice']}")

print("\\nUse dictionaries when:")
print("  - Data has natural key-value relationships")
print("  - Need fast lookups by key (O(1) average)")
print("  - Keys are meaningful (names, IDs, etc.)")
print()

# Example 3: Dictionary Keys Must Be Immutable
print("="*70)
print("Example 3: Valid and Invalid Dictionary Keys")
print("="*70)

# Valid keys: strings, numbers, tuples
valid_dict = {
    "string_key": "value1",
    42: "value2",
    (1, 2): "value3",
    3.14: "value4"
}

print("Valid keys:")
for key, value in valid_dict.items():
    print(f"  {key} ({type(key).__name__}): {value}")

# Invalid keys would raise TypeError
print("\\nInvalid keys (will cause errors):")
print("  - Lists: [1, 2, 3] (mutable)")
print("  - Dictionaries: {'a': 1} (mutable)")
print("  - Sets: {1, 2, 3} (mutable)")
print()

# Example 4: Dictionary Values Can Be Anything
print("="*70)
print("Example 4: Dictionary Values - Any Type")
print("="*70)

mixed_values = {
    "string": "hello",
    "number": 42,
    "float": 3.14,
    "boolean": True,
    "list": [1, 2, 3],
    "dict": {"nested": "value"},
    "none": None
}

print("Dictionary with mixed value types:")
for key, value in mixed_values.items():
    print(f"  {key}: {value} ({type(value).__name__})")
print()

# Example 5: Common Dictionary Operations
print("="*70)
print("Example 5: Essential Dictionary Operations")
print("="*70)

config = {"host": "localhost", "port": 8080}
print(f"Original: {config}")

# Add new key
config["debug"] = True
print(f"\\nAfter add: {config}")

# Update existing key
config["port"] = 3000
print(f"After update: {config}")

# Delete key
del config["debug"]
print(f"After delete: {config}")

# Check key exists
if "host" in config:
    print("\\n'host' key exists")

# Get all keys
print(f"\\nKeys: {list(config.keys())}")

# Get all values
print(f"Values: {list(config.values())}")
print()

# Example 6: Dictionaries for Counting
print("="*70)
print("Example 6: Count Occurrences with Dictionary")
print("="*70)

text = "hello world"
print(f"Text: '{text}'")

# Count character frequency
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("\\nCharacter counts:")
for char, count in sorted(char_count.items()):
    if char != ' ':
        print(f"  '{char}': {count}")

# Count words
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"\\nWords: {words}")
print("Word counts:")
for word, count in word_count.items():
    print(f"  {word}: {count}")
print()

# Example 7: Dictionary as Cache/Lookup Table
print("="*70)
print("Example 7: Fast Lookups - O(1) Average Time")
print("="*70)

# User database simulation
users = {
    "alice123": {"name": "Alice", "email": "alice@example.com"},
    "bob456": {"name": "Bob", "email": "bob@example.com"},
    "charlie789": {"name": "Charlie", "email": "charlie@example.com"}
}

# Fast lookup by username
username = "bob456"
if username in users:
    user = users[username]
    print(f"Found user: {user['name']}")
    print(f"Email: {user['email']}")

# Price lookup
prices = {
    "AAPL": 150.25,
    "GOOGL": 2750.80,
    "MSFT": 305.50
}

symbol = "GOOGL"
price = prices.get(symbol, "Not found")
print(f"\\n{symbol} price: ${price}")
print()

# Example 8: Dictionary for Configuration
print("="*70)
print("Example 8: Application Configuration")
print("="*70)

app_config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "server": {
        "host": "0.0.0.0",
        "port": 8080,
        "ssl": True
    },
    "database": {
        "type": "postgresql",
        "host": "db.example.com",
        "port": 5432
    },
    "features": {
        "logging": True,
        "caching": True,
        "monitoring": False
    }
}

print("Application Configuration:")
print(f"App: {app_config['app_name']} v{app_config['version']}")
print(f"Server: {app_config['server']['host']}:{app_config['server']['port']}")
print(f"Database: {app_config['database']['type']}")
print("\\nEnabled features:")
for feature, enabled in app_config['features'].items():
    if enabled:
        print(f"  - {feature}")
print()

# Example 9: Dictionary Gotchas
print("="*70)
print("Example 9: Common Dictionary Pitfalls")
print("="*70)

# Pitfall 1: KeyError on missing key
data = {"a": 1, "b": 2}
print(f"Dictionary: {data}")

try:
    value = data["c"]  # Raises KeyError
except KeyError:
    print("\\nKeyError: Key 'c' doesn't exist")
    print("Solution: Use get() or check with 'in'")

# Solution
value = data.get("c", "default")
print(f"Using get(): {value}")

# Pitfall 2: Modifying during iteration
print("\\nPitfall: Modifying dict during iteration")
d = {"a": 1, "b": 2, "c": 3}
print(f"Original: {d}")

# Safe way: iterate over copy
for key in list(d.keys()):
    if d[key] > 1:
        del d[key]

print(f"After deletion: {d}")
print()

# Example 10: Practical Application - Student Gradebook
print("="*70)
print("Example 10: Real-World Use Case - Gradebook System")
print("="*70)

gradebook = {
    "Alice": {"Math": 95, "Science": 88, "English": 92},
    "Bob": {"Math": 87, "Science": 91, "English": 85},
    "Charlie": {"Math": 92, "Science": 89, "English": 94}
}

print("Student Gradebook:")
print("="*70)

for student, subjects in gradebook.items():
    avg = sum(subjects.values()) / len(subjects)
    print(f"\\n{student}:")
    for subject, grade in subjects.items():
        print(f"  {subject}: {grade}")
    print(f"  Average: {avg:.2f}")

# Calculate subject averages
subject_totals = {}
student_count = len(gradebook)

for student, subjects in gradebook.items():
    for subject, grade in subjects.items():
        if subject not in subject_totals:
            subject_totals[subject] = 0
        subject_totals[subject] += grade

print("\\n" + "="*70)
print("Subject Averages:")
for subject, total in subject_totals.items():
    avg = total / student_count
    print(f"  {subject}: {avg:.2f}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Dictionaries store key-value pairs")
print("2. Keys must be immutable (strings, numbers, tuples)")
print("3. Values can be any type")
print("4. Access: dict[key] or dict.get(key)")
print("5. Add/Update: dict[key] = value")
print("6. Delete: del dict[key]")
print("7. Check existence: key in dict")
print("8. O(1) average lookup time")
print("9. Use for mappings, caching, configuration")
print("10. Essential Python data structure")
print("="*70)
'''

# Upgrade Lesson 93: Dictionary Fundamentals
lesson93['fullSolution'] = '''"""
Dictionary Fundamentals

Deep dive into dictionary internals, operations, and patterns. Master
iteration, copying, merging, and understanding dictionary behavior.
Essential for advanced Python programming.

**Zero Package Installation Required**
"""

# Example 1: Dictionary Order (Python 3.7+)
print("="*70)
print("Example 1: Dictionary Insertion Order")
print("="*70)

# Python 3.7+ maintains insertion order
d = {}
d["third"] = 3
d["first"] = 1
d["second"] = 2

print("Dictionary (insertion order preserved):")
for key, value in d.items():
    print(f"  {key}: {value}")

# Compare with sorted
print("\\nSorted by key:")
for key in sorted(d.keys()):
    print(f"  {key}: {d[key]}")
print()

# Example 2: Dictionary Equality
print("="*70)
print("Example 2: Dictionary Comparison")
print("="*70)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}  # Same content, different order
dict3 = {"a": 1, "b": 3}  # Different values

print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"dict3: {dict3}")

print(f"\\ndict1 == dict2: {dict1 == dict2}")  # True (same content)
print(f"dict1 == dict3: {dict1 == dict3}")  # False (different values)
print(f"dict1 is dict2: {dict1 is dict2}")  # False (different objects)
print()

# Example 3: Shallow vs Deep Copy
print("="*70)
print("Example 3: Copying Dictionaries")
print("="*70)

original = {"a": 1, "b": [2, 3]}
print(f"Original: {original}")

# Reference (not a copy)
reference = original
reference["a"] = 999
print(f"\\nAfter modifying reference:")
print(f"Original: {original}")  # Changed!

# Shallow copy
original2 = {"a": 1, "b": [2, 3]}
shallow = original2.copy()
shallow["a"] = 999  # Doesn't affect original
shallow["b"].append(4)  # DOES affect original (list is shared)

print(f"\\nAfter shallow copy modifications:")
print(f"Original2: {original2}")
print(f"Shallow: {shallow}")

# Deep copy
import copy
original3 = {"a": 1, "b": [2, 3]}
deep = copy.deepcopy(original3)
deep["a"] = 999
deep["b"].append(4)

print(f"\\nAfter deep copy modifications:")
print(f"Original3: {original3}")  # Unchanged
print(f"Deep: {deep}")
print()

# Example 4: Dictionary Methods Overview
print("="*70)
print("Example 4: Essential Dictionary Methods")
print("="*70)

d = {"a": 1, "b": 2, "c": 3}
print(f"Dictionary: {d}")

# keys(), values(), items()
print(f"\\nkeys(): {list(d.keys())}")
print(f"values(): {list(d.values())}")
print(f"items(): {list(d.items())}")

# get() with default
print(f"\\nget('a'): {d.get('a')}")
print(f"get('x', 0): {d.get('x', 0)}")

# setdefault()
d.setdefault("d", 4)  # Adds if missing
d.setdefault("a", 999)  # Does nothing (key exists)
print(f"\\nAfter setdefault: {d}")

# pop()
value = d.pop("b")
print(f"\\npop('b') returned: {value}")
print(f"After pop: {d}")

# clear()
d_copy = d.copy()
d_copy.clear()
print(f"\\nAfter clear(): {d_copy}")
print()

# Example 5: Default Dictionary Pattern
print("="*70)
print("Example 5: Default Values Pattern")
print("="*70)

# Count word occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Method 1: Manual check
count1 = {}
for word in words:
    if word not in count1:
        count1[word] = 0
    count1[word] += 1

print(f"Method 1 (manual): {count1}")

# Method 2: get() with default
count2 = {}
for word in words:
    count2[word] = count2.get(word, 0) + 1

print(f"Method 2 (get): {count2}")

# Method 3: setdefault()
count3 = {}
for word in words:
    count3.setdefault(word, 0)
    count3[word] += 1

print(f"Method 3 (setdefault): {count3}")
print()

# Example 6: Dictionary Unpacking
print("="*70)
print("Example 6: Dictionary Unpacking with **")
print("="*70)

def greet(name, age, city):
    return f"{name} is {age} years old and lives in {city}"

person = {"name": "Alice", "age": 30, "city": "NYC"}
print(f"Dictionary: {person}")

# Unpack dict as function arguments
result = greet(**person)
print(f"\\nResult: {result}")

# Unpacking in dict literals
defaults = {"theme": "light", "volume": 50}
preferences = {"volume": 75, "notifications": True}

# Merge with unpacking
combined = {**defaults, **preferences}
print(f"\\nDefaults: {defaults}")
print(f"Preferences: {preferences}")
print(f"Combined: {combined}")
print()

# Example 7: Dictionary Comprehension Patterns
print("="*70)
print("Example 7: Common Comprehension Patterns")
print("="*70)

# Invert dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Inverted: {inverted}")

# Filter dictionary
data = {"a": 10, "b": 5, "c": 15, "d": 3}
filtered = {k: v for k, v in data.items() if v > 5}
print(f"\\nData: {data}")
print(f"Filtered (>5): {filtered}")

# Transform values
prices = {"apple": 1.20, "banana": 0.50}
with_tax = {item: price * 1.1 for item, price in prices.items()}
print(f"\\nPrices: {prices}")
print(f"With 10% tax: {with_tax}")
print()

# Example 8: Nested Dictionary Navigation
print("="*70)
print("Example 8: Safe Navigation in Nested Dictionaries")
print("="*70)

data = {
    "user": {
        "profile": {
            "name": "Alice",
            "email": "alice@example.com"
        }
    }
}

# Unsafe way (raises KeyError if missing)
try:
    email = data["user"]["profile"]["email"]
    print(f"Email (direct): {email}")
except KeyError as e:
    print(f"KeyError: {e}")

# Safe way with get()
email = data.get("user", {}).get("profile", {}).get("email", "Not found")
print(f"Email (safe): {email}")

# Check for missing path
phone = data.get("user", {}).get("profile", {}).get("phone", "Not found")
print(f"Phone (safe): {phone}")
print()

# Example 9: Dictionary Performance
print("="*70)
print("Example 9: Dictionary Performance Characteristics")
print("="*70)

import time

# Create large dictionary
large_dict = {i: i * 2 for i in range(100000)}

# Test lookup performance
start = time.perf_counter()
for i in range(1000):
    _ = large_dict.get(50000)
dict_time = time.perf_counter() - start

print(f"Dictionary size: {len(large_dict):,} items")
print(f"1,000 lookups: {dict_time*1000:.4f}ms")
print(f"Average: {dict_time*1000000:.2f}µs per lookup")

# Compare with list
large_list = list(range(100000))
start = time.perf_counter()
for i in range(1000):
    _ = 50000 in large_list
list_time = time.perf_counter() - start

print(f"\\nList size: {len(large_list):,} items")
print(f"1,000 lookups: {list_time*1000:.4f}ms")
print(f"\\nDictionary is {list_time/dict_time:.0f}x faster!")
print()

# Example 10: Practical Application - Configuration Management
print("="*70)
print("Example 10: Real-World Use Case - Config System")
print("="*70)

class Config:
    """Configuration manager with defaults and overrides"""

    def __init__(self):
        self.config = {
            "app": {
                "name": "MyApp",
                "version": "1.0.0",
                "debug": False
            },
            "server": {
                "host": "localhost",
                "port": 8080,
                "workers": 4
            },
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "mydb"
            }
        }

    def get(self, path, default=None):
        """Get config value by dot-separated path"""
        keys = path.split(".")
        value = self.config

        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
                if value is None:
                    return default
            else:
                return default

        return value

    def set(self, path, value):
        """Set config value by dot-separated path"""
        keys = path.split(".")
        d = self.config

        for key in keys[:-1]:
            d = d.setdefault(key, {})

        d[keys[-1]] = value

    def update(self, updates):
        """Update config with new values"""
        def deep_update(base, updates):
            for key, value in updates.items():
                if isinstance(value, dict) and key in base:
                    deep_update(base[key], value)
                else:
                    base[key] = value

        deep_update(self.config, updates)

# Usage example
config = Config()

print("Default configuration:")
print(f"  App name: {config.get('app.name')}")
print(f"  Server port: {config.get('server.port')}")
print(f"  Debug: {config.get('app.debug')}")

# Update configuration
config.set("app.debug", True)
config.set("server.port", 3000)

print("\\nAfter updates:")
print(f"  Debug: {config.get('app.debug')}")
print(f"  Server port: {config.get('server.port')}")

# Bulk update
config.update({
    "server": {"host": "0.0.0.0", "workers": 8},
    "app": {"environment": "production"}
})

print("\\nAfter bulk update:")
print(f"  Server host: {config.get('server.host')}")
print(f"  Workers: {config.get('server.workers')}")
print(f"  Environment: {config.get('app.environment')}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Python 3.7+ dictionaries preserve insertion order")
print("2. Use .copy() for shallow copy, deepcopy() for deep copy")
print("3. get() safer than [] for missing keys")
print("4. setdefault() adds key only if missing")
print("5. Dictionary unpacking: {**dict1, **dict2}")
print("6. Comprehensions: {k: v for k, v in items}")
print("7. O(1) average lookup, insert, delete")
print("8. Nested access: use get() chaining for safety")
print("9. Keys must be hashable (immutable)")
print("10. Dictionaries are fundamental to Python internals")
print("="*70)
'''

# Continue with remaining lessons 94-100 in next part of script...

# Save the updated lessons
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Print summary
print("\nUpgraded lessons 92-93:")
print(f"  92: Dictionaries - {len(lesson92['fullSolution'])} chars")
print(f"  93: Dictionary Fundamentals - {len(lesson93['fullSolution'])} chars")
print("\nBatch 92-100: Lessons 92-93 complete, continuing with 94-100...")
