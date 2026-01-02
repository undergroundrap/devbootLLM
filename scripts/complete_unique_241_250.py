#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 241: Count Occurrences - Complete unique content
lesson241 = next(l for l in lessons if l['id'] == 241)
lesson241['content'] = '''# Count Occurrences

Count element frequency in collections using Counter, dictionaries, and loops. Counting is fundamental for data analysis, finding duplicates, statistics, and text processing. Efficient counting enables frequency analysis, histogram creation, and pattern detection in large datasets.

## Example 1: Basic Counting with Dictionary

Track occurrences manually:

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

counts = {}
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

print(counts)  # {1: 1, 2: 2, 3: 3, 4: 4}

# More Pythonic with get()
counts = {}
for num in numbers:
    counts[num] = counts.get(num, 0) + 1

print(counts)  # {1: 1, 2: 2, 3: 3, 4: 4}
```

**Result**: Manual frequency tracking with dictionaries.

## Example 2: Counter from collections

Use Counter for automatic counting:

```python
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counts = Counter(numbers)

print(counts)  # Counter({4: 4, 3: 3, 2: 2, 1: 1})
print(counts[3])  # 3
print(counts[99])  # 0 (missing keys return 0)

# Most common elements
most_common = counts.most_common(2)
print(most_common)  # [(4, 4), (3, 3)]

# Least common
least_common = counts.most_common()[:-3:-1]
print(least_common)  # [(1, 1), (2, 2)]
```

**Result**: Counter provides rich counting API.

## Example 3: Count Words in Text

Word frequency analysis:

```python
from collections import Counter

text = "the quick brown fox jumps over the lazy dog the fox"
words = text.lower().split()

word_counts = Counter(words)
print(word_counts)
# Counter({'the': 3, 'fox': 2, 'quick': 1, 'brown': 1, ...})

# Display top words
for word, count in word_counts.most_common(3):
    print(f"{word}: {count}")

# Total words
total = sum(word_counts.values())
print(f"Total words: {total}")

# Unique words
unique = len(word_counts)
print(f"Unique words: {unique}")
```

**Result**: Text frequency analysis and statistics.

## Example 4: Count Characters

Character frequency in strings:

```python
from collections import Counter

text = "hello world"
char_counts = Counter(text)

print(char_counts)
# Counter({'l': 3, 'o': 2, 'h': 1, ...})

# Exclude spaces
text_no_space = text.replace(' ', '')
char_counts = Counter(text_no_space)

for char, count in sorted(char_counts.items()):
    print(f"'{char}': {count}")
```

**Result**: Character-level frequency analysis.

## Example 5: Count with defaultdict

Auto-initializing counter:

```python
from collections import defaultdict

numbers = [1, 2, 2, 3, 3, 3]
counts = defaultdict(int)

for num in numbers:
    counts[num] += 1

print(dict(counts))  # {1: 1, 2: 2, 3: 3}

# Count specific types
data = [1, 'a', 2, 'b', 3, 'a']
type_counts = defaultdict(int)

for item in data:
    type_counts[type(item).__name__] += 1

print(dict(type_counts))  # {'int': 3, 'str': 3}
```

**Result**: Simplified counting without initialization.

## Example 6: Conditional Counting

Count only matching elements:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Count evens
even_count = sum(1 for n in numbers if n % 2 == 0)
print(f"Even numbers: {even_count}")  # 5

# Count by condition
from collections import Counter

def classify(n):
    if n % 2 == 0:
        return 'even'
    return 'odd'

counts = Counter(classify(n) for n in numbers)
print(counts)  # Counter({'even': 5, 'odd': 5})
```

**Result**: Count based on conditions.

## Example 7: Count in Nested Structures

Count in 2D lists:

```python
from collections import Counter
from itertools import chain

matrix = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
]

# Flatten and count
flat = chain.from_iterable(matrix)
counts = Counter(flat)

print(counts)  # Counter({3: 3, 2: 2, 4: 2, 1: 1, 5: 1})
```

**Result**: Count across nested structures.

## Example 8: Counter Arithmetic

Combine and manipulate counters:

```python
from collections import Counter

count1 = Counter(['a', 'b', 'c', 'a'])
count2 = Counter(['a', 'b', 'd', 'b'])

# Addition
combined = count1 + count2
print(combined)  # Counter({'a': 3, 'b': 3, 'c': 1, 'd': 1})

# Subtraction (keeps only positive)
diff = count1 - count2
print(diff)  # Counter({'a': 1, 'c': 1})

# Intersection (minimum)
common = count1 & count2
print(common)  # Counter({'a': 1, 'b': 1})

# Union (maximum)
union = count1 | count2
print(union)  # Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1})
```

**Result**: Set-like operations on counters.

## Example 9: Count File Statistics

Count lines, words, characters:

```python
from collections import Counter

text = """Line one
Line two has more words
Line three
"""

lines = text.strip().split('\\n')
line_count = len(lines)

words = text.split()
word_count = len(words)

char_count = len(text)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")

# Word length distribution
word_lengths = Counter(len(word) for word in words)
print(f"Word lengths: {dict(word_lengths)}")
```

**Result**: File statistics and analysis.

## Example 10: Production Counting Utility

Complete counting library:

```python
from collections import Counter, defaultdict
from typing import Any, Callable, Dict, Iterable, List

class CountingUtils:
    @staticmethod
    def count_occurrences(items: Iterable[Any]) -> Dict[Any, int]:
        """Count occurrences of each item."""
        return dict(Counter(items))

    @staticmethod
    def count_by(items: Iterable[Any], key: Callable) -> Dict[Any, int]:
        """Count items grouped by key function."""
        return dict(Counter(key(item) for item in items))

    @staticmethod
    def top_n(items: Iterable[Any], n: int = 5) -> List[tuple]:
        """Get top N most frequent items."""
        return Counter(items).most_common(n)

    @staticmethod
    def frequency_distribution(items: Iterable[Any]) -> Dict[Any, float]:
        """Get frequency distribution (percentages)."""
        counts = Counter(items)
        total = sum(counts.values())
        return {item: count/total for item, count in counts.items()}

# Usage
utils = CountingUtils()

data = ['a', 'b', 'a', 'c', 'a', 'b']

# Basic counting
counts = utils.count_occurrences(data)
print(f"Counts: {counts}")

# Top items
top = utils.top_n(data, 2)
print(f"Top 2: {top}")

# Frequency distribution
freq = utils.frequency_distribution(data)
for item, pct in freq.items():
    print(f"{item}: {pct*100:.1f}%")
```

**Result**: Production-ready counting utilities.

## KEY TAKEAWAYS

- **Counter Class**: collections.Counter for automatic counting
- **Dictionary**: Manual counting with dict.get(key, 0) + 1
- **defaultdict(int)**: Auto-initialize counters to 0
- **most_common(n)**: Retrieve top N frequent elements
- **Arithmetic**: Add, subtract, intersect, union counters
- **Conditional Counting**: Use generator expressions with conditions
- **Nested Structures**: Flatten with itertools.chain
- **Text Analysis**: Count words, characters, lines
- **Type Safety**: Use type hints for clarity
- **Zero Default**: Counter returns 0 for missing keys
'''

# Lesson 242: Find Maximum
lesson242 = next(l for l in lessons if l['id'] == 242)
lesson242['content'] = '''# Find Maximum

Find the largest element in collections using max(), manual loops, and custom key functions. Maximum finding is essential for optimization, data analysis, and algorithm design. Understanding max operations enables peak detection, range finding, and comparative analysis.

## Example 1: Basic max() Function

Find maximum with built-in:

```python
numbers = [3, 7, 2, 9, 1, 5]
maximum = max(numbers)
print(f"Maximum: {maximum}")  # 9

# Works with strings (alphabetical)
words = ["apple", "banana", "cherry"]
print(max(words))  # cherry

# Multiple arguments
print(max(10, 20, 5, 30))  # 30
```

**Result**: Built-in max() for simple cases.

## Example 2: Manual Maximum Finding

Find max with loop:

```python
numbers = [3, 7, 2, 9, 1, 5]

# Initialize with first element
max_val = numbers[0]
for num in numbers[1:]:
    if num > max_val:
        max_val = num

print(f"Maximum: {max_val}")  # 9

# Handle empty list
def find_max(nums):
    if not nums:
        return None
    max_val = nums[0]
    for num in nums[1:]:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([3, 7, 2, 9]))  # 9
print(find_max([]))  # None
```

**Result**: Manual control over maximum finding.

## Example 3: Max with Key Function

Custom comparison criteria:

```python
words = ["a", "abc", "ab", "abcd"]

# Longest word
longest = max(words, key=len)
print(f"Longest: {longest}")  # abcd

# Students by grade
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

top_student = max(students, key=lambda s: s["grade"])
print(f"Top: {top_student['name']} ({top_student['grade']})")
# Top: Bob (92)
```

**Result**: Custom comparison logic.

## Example 4: Max with Index Tracking

Find both value and position:

```python
numbers = [3, 7, 2, 9, 1, 5]

# Find max and index
max_val = max(numbers)
max_idx = numbers.index(max_val)

print(f"Max {max_val} at index {max_idx}")  # Max 9 at index 3

# Using enumerate
max_idx, max_val = max(enumerate(numbers), key=lambda x: x[1])
print(f"Max {max_val} at index {max_idx}")  # Max 9 at index 3
```

**Result**: Track position of maximum.

## Example 5: Max in 2D Lists

Find maximum in nested structures:

```python
matrix = [
    [3, 7, 2],
    [9, 1, 5],
    [4, 8, 6]
]

# Max in entire matrix
max_val = max(max(row) for row in matrix)
print(f"Matrix max: {max_val}")  # 9

# Max of each row
row_maxes = [max(row) for row in matrix]
print(f"Row maxes: {row_maxes}")  # [7, 9, 8]

# Max of each column
col_maxes = [max(matrix[i][j] for i in range(len(matrix)))
             for j in range(len(matrix[0]))]
print(f"Column maxes: {col_maxes}")  # [9, 8, 6]
```

**Result**: Maximum in multi-dimensional data.

## Example 6: Conditional Maximum

Find max among filtered values:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Max even number
even_nums = [n for n in numbers if n % 2 == 0]
max_even = max(even_nums)
print(f"Max even: {max_even}")  # 10

# Using generator (more memory efficient)
max_even = max(n for n in numbers if n % 2 == 0)
print(f"Max even: {max_even}")  # 10

# With default for empty
max_even = max((n for n in [] if n % 2 == 0), default=0)
print(f"Max even: {max_even}")  # 0
```

**Result**: Maximum with conditions.

## Example 7: Max for Custom Objects

Define comparison for objects:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]

oldest = max(people)
print(f"Oldest: {oldest}")  # Person(Charlie, 35)

# Or use key function
oldest = max(people, key=lambda p: p.age)
print(f"Oldest: {oldest}")  # Person(Charlie, 35)
```

**Result**: Maximum with custom comparisons.

## Example 8: Max of Absolute Values

Find maximum by absolute value:

```python
numbers = [-10, 5, -20, 15, -8]

# Max by absolute value
max_abs = max(numbers, key=abs)
print(f"Max absolute: {max_abs}")  # -20

# Actual max value
max_val = max(numbers)
print(f"Max value: {max_val}")  # 15

# Max absolute value itself
max_abs_val = max(abs(n) for n in numbers)
print(f"Max |n|: {max_abs_val}")  # 20
```

**Result**: Different maximum criteria.

## Example 9: Running Maximum

Track maximum over sequence:

```python
numbers = [3, 7, 2, 9, 1, 8, 5]

# Running max
running_max = []
current_max = float('-inf')

for num in numbers:
    current_max = max(current_max, num)
    running_max.append(current_max)

print(f"Running max: {running_max}")
# [3, 7, 7, 9, 9, 9, 9]

# Using itertools.accumulate
from itertools import accumulate
running_max = list(accumulate(numbers, max))
print(f"Running max: {running_max}")
# [3, 7, 7, 9, 9, 9, 9]
```

**Result**: Maximum at each position.

## Example 10: Production Maximum Utilities

Complete max finding library:

```python
from typing import Any, Callable, List, Optional, TypeVar

T = TypeVar('T')

class MaxUtils:
    @staticmethod
    def find_max(items: List[T], default: Optional[T] = None) -> Optional[T]:
        """Find maximum with default for empty."""
        try:
            return max(items)
        except ValueError:
            return default

    @staticmethod
    def find_max_by(items: List[T], key: Callable[[T], Any]) -> Optional[T]:
        """Find maximum by key function."""
        if not items:
            return None
        return max(items, key=key)

    @staticmethod
    def find_top_n(items: List[T], n: int = 5) -> List[T]:
        """Find top N maximum elements."""
        return sorted(items, reverse=True)[:n]

    @staticmethod
    def find_max_with_index(items: List[T]) -> tuple:
        """Return (index, value) of maximum."""
        if not items:
            return (-1, None)
        idx, val = max(enumerate(items), key=lambda x: x[1])
        return (idx, val)

# Usage
utils = MaxUtils()

numbers = [3, 7, 2, 9, 1, 5]

# Find max
max_val = utils.find_max(numbers)
print(f"Max: {max_val}")  # 9

# Top 3
top_3 = utils.find_top_n(numbers, 3)
print(f"Top 3: {top_3}")  # [9, 7, 5]

# Max with index
idx, val = utils.find_max_with_index(numbers)
print(f"Max {val} at index {idx}")  # Max 9 at index 3
```

**Result**: Production-ready maximum utilities.

## KEY TAKEAWAYS

- **max() Function**: Built-in for finding maximum
- **key Parameter**: Custom comparison with key=lambda
- **Manual Loop**: Track max with loop and comparison
- **Empty Check**: Handle empty sequences gracefully
- **Multiple Args**: max(a, b, c) for multiple values
- **Index Tracking**: Find both value and position
- **Custom Objects**: Define __lt__ for comparisons
- **Conditional Max**: max with filtered values
- **2D Arrays**: Find max in nested structures
- **Default Values**: Provide default for empty sequences
'''

# Lesson 243: Find Minimum
lesson243 = next(l for l in lessons if l['id'] == 243)
lesson243['content'] = '''# Find Minimum

Find the smallest element in collections using min(), manual loops, and custom key functions. Minimum finding is fundamental for optimization, threshold detection, and data analysis. Understanding min operations enables valley detection, range finding, and comparative analysis.

## Example 1: Basic min() Function

Find minimum with built-in:

```python
numbers = [3, 7, 2, 9, 1, 5]
minimum = min(numbers)
print(f"Minimum: {minimum}")  # 1

# Works with strings (alphabetical)
words = ["apple", "banana", "cherry"]
print(min(words))  # apple

# Multiple arguments
print(min(10, 20, 5, 30))  # 5
```

**Result**: Built-in min() for simple cases.

## Example 2: Manual Minimum Finding

Find min with loop:

```python
numbers = [3, 7, 2, 9, 1, 5]

# Initialize with first element
min_val = numbers[0]
for num in numbers[1:]:
    if num < min_val:
        min_val = num

print(f"Minimum: {min_val}")  # 1

# Handle empty list
def find_min(nums):
    if not nums:
        return None
    min_val = nums[0]
    for num in nums[1:]:
        if num < min_val:
            min_val = num
    return min_val

print(find_min([3, 7, 2, 9]))  # 2
print(find_min([]))  # None
```

**Result**: Manual control over minimum finding.

## Example 3: Min with Key Function

Custom comparison criteria:

```python
words = ["a", "abc", "ab", "abcd"]

# Shortest word
shortest = min(words, key=len)
print(f"Shortest: {shortest}")  # a

# Students by grade
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

lowest_student = min(students, key=lambda s: s["grade"])
print(f"Lowest: {lowest_student['name']} ({lowest_student['grade']})")
# Lowest: Charlie (78)
```

**Result**: Custom comparison logic.

## Example 4: Min with Index Tracking

Find both value and position:

```python
numbers = [3, 7, 2, 9, 1, 5]

# Find min and index
min_val = min(numbers)
min_idx = numbers.index(min_val)

print(f"Min {min_val} at index {min_idx}")  # Min 1 at index 4

# Using enumerate
min_idx, min_val = min(enumerate(numbers), key=lambda x: x[1])
print(f"Min {min_val} at index {min_idx}")  # Min 1 at index 4
```

**Result**: Track position of minimum.

## Example 5: Min in 2D Lists

Find minimum in nested structures:

```python
matrix = [
    [3, 7, 2],
    [9, 1, 5],
    [4, 8, 6]
]

# Min in entire matrix
min_val = min(min(row) for row in matrix)
print(f"Matrix min: {min_val}")  # 1

# Min of each row
row_mins = [min(row) for row in matrix]
print(f"Row mins: {row_mins}")  # [2, 1, 4]

# Min of each column
col_mins = [min(matrix[i][j] for i in range(len(matrix)))
            for j in range(len(matrix[0]))]
print(f"Column mins: {col_mins}")  # [3, 1, 2]
```

**Result**: Minimum in multi-dimensional data.

## Example 6: Conditional Minimum

Find min among filtered values:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Min even number
even_nums = [n for n in numbers if n % 2 == 0]
min_even = min(even_nums)
print(f"Min even: {min_even}")  # 2

# Using generator (more memory efficient)
min_even = min(n for n in numbers if n % 2 == 0)
print(f"Min even: {min_even}")  # 2

# With default for empty
min_even = min((n for n in [] if n % 2 == 0), default=0)
print(f"Min even: {min_even}")  # 0
```

**Result**: Minimum with conditions.

## Example 7: Min for Custom Objects

Define comparison for objects:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]

youngest = min(people)
print(f"Youngest: {youngest}")  # Person(Bob, 25)

# Or use key function
youngest = min(people, key=lambda p: p.age)
print(f"Youngest: {youngest}")  # Person(Bob, 25)
```

**Result**: Minimum with custom comparisons.

## Example 8: Min of Absolute Values

Find minimum by absolute value:

```python
numbers = [-10, 5, -2, 15, -8]

# Min by absolute value
min_abs = min(numbers, key=abs)
print(f"Min absolute: {min_abs}")  # -2

# Actual min value
min_val = min(numbers)
print(f"Min value: {min_val}")  # -10

# Min absolute value itself
min_abs_val = min(abs(n) for n in numbers)
print(f"Min |n|: {min_abs_val}")  # 2
```

**Result**: Different minimum criteria.

## Example 9: Running Minimum

Track minimum over sequence:

```python
numbers = [3, 7, 2, 9, 1, 8, 5]

# Running min
running_min = []
current_min = float('inf')

for num in numbers:
    current_min = min(current_min, num)
    running_min.append(current_min)

print(f"Running min: {running_min}")
# [3, 3, 2, 2, 1, 1, 1]

# Using itertools.accumulate
from itertools import accumulate
running_min = list(accumulate(numbers, min))
print(f"Running min: {running_min}")
# [3, 3, 2, 2, 1, 1, 1]
```

**Result**: Minimum at each position.

## Example 10: Production Minimum Utilities

Complete min finding library:

```python
from typing import Any, Callable, List, Optional, TypeVar

T = TypeVar('T')

class MinUtils:
    @staticmethod
    def find_min(items: List[T], default: Optional[T] = None) -> Optional[T]:
        """Find minimum with default for empty."""
        try:
            return min(items)
        except ValueError:
            return default

    @staticmethod
    def find_min_by(items: List[T], key: Callable[[T], Any]) -> Optional[T]:
        """Find minimum by key function."""
        if not items:
            return None
        return min(items, key=key)

    @staticmethod
    def find_bottom_n(items: List[T], n: int = 5) -> List[T]:
        """Find bottom N minimum elements."""
        return sorted(items)[:n]

    @staticmethod
    def find_min_with_index(items: List[T]) -> tuple:
        """Return (index, value) of minimum."""
        if not items:
            return (-1, None)
        idx, val = min(enumerate(items), key=lambda x: x[1])
        return (idx, val)

# Usage
utils = MinUtils()

numbers = [3, 7, 2, 9, 1, 5]

# Find min
min_val = utils.find_min(numbers)
print(f"Min: {min_val}")  # 1

# Bottom 3
bottom_3 = utils.find_bottom_n(numbers, 3)
print(f"Bottom 3: {bottom_3}")  # [1, 2, 3]

# Min with index
idx, val = utils.find_min_with_index(numbers)
print(f"Min {val} at index {idx}")  # Min 1 at index 4
```

**Result**: Production-ready minimum utilities.

## KEY TAKEAWAYS

- **min() Function**: Built-in for finding minimum
- **key Parameter**: Custom comparison with key=lambda
- **Manual Loop**: Track min with loop and comparison
- **Empty Check**: Handle empty sequences gracefully
- **Multiple Args**: min(a, b, c) for multiple values
- **Index Tracking**: Find both value and position
- **Custom Objects**: Define __lt__ for comparisons
- **Conditional Min**: min with filtered values
- **2D Arrays**: Find min in nested structures
- **Default Values**: Provide default for empty sequences
'''

# Lesson 244: Linear Search
lesson244 = next(l for l in lessons if l['id'] == 244)
lesson244['content'] = '''# Linear Search

Search sequentially through collections to find elements or verify presence. Linear search is the simplest search algorithm with O(n) complexity, essential for unsorted data. Understanding linear search is foundational for algorithm design and problem solving.

## Example 1: Basic Linear Search

Search for element in list:

```python
def linear_search(arr, target):
    """Find index of target, return -1 if not found."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [3, 7, 2, 9, 1, 5]

index = linear_search(numbers, 9)
print(f"Found at index: {index}")  # 3

index = linear_search(numbers, 10)
print(f"Found at index: {index}")  # -1 (not found)
```

**Result**: Basic sequential search.

## Example 2: Using 'in' Operator

Pythonic membership testing:

```python
numbers = [3, 7, 2, 9, 1, 5]

# Check if element exists
if 9 in numbers:
    print("Found 9")  # Found 9

if 10 not in numbers:
    print("10 not found")  # 10 not found

# Get index with list.index()
try:
    index = numbers.index(9)
    print(f"9 at index {index}")  # 9 at index 3
except ValueError:
    print("Not found")
```

**Result**: Built-in membership testing.

## Example 3: Find All Occurrences

Find all indices of target:

```python
def find_all(arr, target):
    """Return list of all indices where target appears."""
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

numbers = [3, 7, 2, 9, 2, 5, 2]

# Find all occurrences of 2
indices = find_all(numbers, 2)
print(f"Found at indices: {indices}")  # [2, 4, 6]

# Using list comprehension
indices = [i for i, x in enumerate(numbers) if x == 2]
print(f"Found at indices: {indices}")  # [2, 4, 6]
```

**Result**: Multiple occurrence search.

## Example 4: Search with Condition

Search by predicate function:

```python
def find_if(arr, predicate):
    """Find first element matching predicate."""
    for i, item in enumerate(arr):
        if predicate(item):
            return i, item
    return -1, None

numbers = [3, 7, 2, 9, 1, 5]

# Find first even number
index, value = find_if(numbers, lambda x: x % 2 == 0)
print(f"First even: {value} at index {index}")  # First even: 2 at index 2

# Find first number > 5
index, value = find_if(numbers, lambda x: x > 5)
print(f"First > 5: {value} at index {index}")  # First > 5: 7 at index 1
```

**Result**: Conditional search.

## Example 5: Search in Strings

Find substring in text:

```python
text = "Hello, World! Welcome to Python."

# Using 'in' operator
if "World" in text:
    print("Found 'World'")  # Found 'World'

# Get index with str.find()
index = text.find("World")
print(f"'World' at index {index}")  # 'World' at index 7

# Returns -1 if not found
index = text.find("Java")
print(f"'Java' at index {index}")  # 'Java' at index -1

# Case-insensitive search
if "world" in text.lower():
    print("Found 'world' (case-insensitive)")
```

**Result**: String search operations.

## Example 6: Search in Custom Objects

Search for objects by attribute:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]

# Find person by name
def find_person(people, name):
    for i, person in enumerate(people):
        if person.name == name:
            return i, person
    return -1, None

index, person = find_person(people, "Bob")
print(f"Found: {person} at index {index}")
# Found: Person(Bob, 25) at index 1
```

**Result**: Object attribute search.

## Example 7: Early Termination Search

Stop searching when condition met:

```python
def search_until(arr, condition):
    """Search until condition is no longer met."""
    result = []
    for item in arr:
        if not condition(item):
            break
        result.append(item)
    return result

numbers = [2, 4, 6, 7, 8, 10]

# Get all numbers until first odd
evens = search_until(numbers, lambda x: x % 2 == 0)
print(f"Evens until odd: {evens}")  # [2, 4, 6]
```

**Result**: Conditional early termination.

## Example 8: Search with Sentinel

Use sentinel value for optimization:

```python
def sentinel_search(arr, target):
    """Linear search with sentinel for fewer comparisons."""
    n = len(arr)
    if n == 0:
        return -1

    # Save last element and replace with target
    last = arr[n-1]
    arr[n-1] = target

    i = 0
    while arr[i] != target:
        i += 1

    # Restore last element
    arr[n-1] = last

    # Check if found or sentinel
    if i < n-1 or arr[n-1] == target:
        return i
    return -1

numbers = [3, 7, 2, 9, 1, 5]
index = sentinel_search(numbers, 9)
print(f"Found at: {index}")  # 3
```

**Result**: Optimized linear search.

## Example 9: Binary vs Linear Search Comparison

Compare search strategies:

```python
import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Small unsorted list - linear is fine
small = [3, 7, 2, 9, 1, 5]
print(f"Linear: {linear_search(small, 9)}")  # 3

# Large sorted list - binary is better
large = list(range(1000000))
print(f"Binary: {binary_search(large, 999999)}")  # 999999
```

**Result**: Algorithm comparison.

## Example 10: Production Search Utilities

Complete search library:

```python
from typing import Any, Callable, List, Optional, Tuple, TypeVar

T = TypeVar('T')

class SearchUtils:
    @staticmethod
    def find(arr: List[T], target: T) -> int:
        """Find first occurrence of target."""
        try:
            return arr.index(target)
        except ValueError:
            return -1

    @staticmethod
    def find_all(arr: List[T], target: T) -> List[int]:
        """Find all occurrences of target."""
        return [i for i, x in enumerate(arr) if x == target]

    @staticmethod
    def find_if(arr: List[T], predicate: Callable[[T], bool]) -> Tuple[int, Optional[T]]:
        """Find first element matching predicate."""
        for i, item in enumerate(arr):
            if predicate(item):
                return i, item
        return -1, None

    @staticmethod
    def contains(arr: List[T], target: T) -> bool:
        """Check if target exists in array."""
        return target in arr

    @staticmethod
    def count_occurrences(arr: List[T], target: T) -> int:
        """Count occurrences of target."""
        return arr.count(target)

# Usage
utils = SearchUtils()

numbers = [3, 7, 2, 9, 2, 5, 2]

# Find first occurrence
index = utils.find(numbers, 2)
print(f"First 2 at: {index}")  # 2

# Find all occurrences
indices = utils.find_all(numbers, 2)
print(f"All 2s at: {indices}")  # [2, 4, 6]

# Find first even
index, val = utils.find_if(numbers, lambda x: x % 2 == 0)
print(f"First even: {val} at {index}")  # First even: 2 at 2

# Count occurrences
count = utils.count_occurrences(numbers, 2)
print(f"Count of 2: {count}")  # 3
```

**Result**: Production-ready search utilities.

## KEY TAKEAWAYS

- **Linear Search**: O(n) sequential search algorithm
- **in Operator**: Pythonic membership testing
- **list.index()**: Find first occurrence index
- **enumerate()**: Track both index and value
- **Predicates**: Search by condition function
- **Find All**: Use list comprehension for all matches
- **Early Exit**: Break when target found
- **Sentinel**: Optimization with sentinel value
- **Unsorted Data**: Linear search works on unsorted data
- **When to Use**: Small lists, unsorted data, simple searches
'''

# Lesson 245: Remove Duplicates
lesson245 = next(l for l in lessons if l['id'] == 245)
lesson245['content'] = '''# Remove Duplicates

Eliminate duplicate elements using sets, dict.fromkeys(), and manual filtering. Removing duplicates is essential for data cleaning, normalization, and ensuring unique values. Understanding deduplication enables efficient data processing and analysis.

## Example 1: Using set()

Convert to set and back:

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Remove duplicates (order not preserved)
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4] (order may vary)

# Works with any hashable type
words = ["apple", "banana", "apple", "cherry", "banana"]
unique_words = list(set(words))
print(unique_words)  # ['apple', 'banana', 'cherry'] (order may vary)
```

**Result**: Fast deduplication without order.

## Example 2: Preserve Order with dict.fromkeys()

Keep first occurrence order:

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Preserve order (Python 3.7+)
unique = list(dict.fromkeys(numbers))
print(unique)  # [1, 2, 3, 4]

words = ["apple", "banana", "apple", "cherry", "banana"]
unique_words = list(dict.fromkeys(words))
print(unique_words)  # ['apple', 'banana', 'cherry']
```

**Result**: Order-preserving deduplication.

## Example 3: Manual Loop Approach

Explicit duplicate removal:

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Using list and membership check
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)  # [1, 2, 3, 4]

# More efficient with set for tracking
unique = []
seen = set()
for num in numbers:
    if num not in seen:
        unique.append(num)
        seen.add(num)

print(unique)  # [1, 2, 3, 4]
```

**Result**: Manual control over deduplication.

## Example 4: Remove Duplicates from Strings

Unique characters in string:

```python
text = "hello world"

# Unique characters (order not preserved)
unique_chars = ''.join(set(text))
print(unique_chars)  # Order may vary

# Preserve order
unique_chars = ''.join(dict.fromkeys(text))
print(unique_chars)  # 'helo wrd'

# Unique words
sentence = "the quick brown fox jumps over the lazy dog the fox"
words = sentence.split()
unique_words = list(dict.fromkeys(words))
print(' '.join(unique_words))
# 'the quick brown fox jumps over lazy dog'
```

**Result**: String deduplication.

## Example 5: Remove Duplicates from Lists of Lists

Deduplicate nested structures:

```python
# Lists aren't hashable, convert to tuples
pairs = [[1, 2], [3, 4], [1, 2], [5, 6], [3, 4]]

# Convert to tuples, deduplicate, convert back
unique_pairs = [list(t) for t in dict.fromkeys(tuple(p) for p in pairs)]
print(unique_pairs)  # [[1, 2], [3, 4], [5, 6]]

# Alternative: manual comparison
unique_pairs = []
for pair in pairs:
    if pair not in unique_pairs:
        unique_pairs.append(pair)
print(unique_pairs)  # [[1, 2], [3, 4], [5, 6]]
```

**Result**: Deduplicate complex structures.

## Example 6: Remove Duplicates from Custom Objects

Deduplicate objects by attribute:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Alice", 35),  # Duplicate name
    Person("Charlie", 30)
]

# Remove duplicates based on name
unique_people = list(dict.fromkeys(people))
print(unique_people)
# [Person(Alice, 30), Person(Bob, 25), Person(Charlie, 30)]
```

**Result**: Object deduplication with custom equality.

## Example 7: Remove Consecutive Duplicates

Remove only adjacent duplicates:

```python
numbers = [1, 1, 2, 2, 2, 3, 1, 1, 4]

# Remove consecutive duplicates
unique = [numbers[0]]
for i in range(1, len(numbers)):
    if numbers[i] != numbers[i-1]:
        unique.append(numbers[i])

print(unique)  # [1, 2, 3, 1, 4]

# Using itertools.groupby
from itertools import groupby

unique = [key for key, _ in groupby(numbers)]
print(unique)  # [1, 2, 3, 1, 4]
```

**Result**: Consecutive duplicate removal.

## Example 8: Remove Duplicates Case-Insensitive

Deduplicate ignoring case:

```python
words = ["Apple", "banana", "APPLE", "Cherry", "banana"]

# Track lowercase, keep first occurrence
unique = []
seen = set()

for word in words:
    if word.lower() not in seen:
        unique.append(word)
        seen.add(word.lower())

print(unique)  # ['Apple', 'banana', 'Cherry']

# Or use dict with lowercase keys
unique_dict = {}
for word in words:
    if word.lower() not in unique_dict:
        unique_dict[word.lower()] = word

unique = list(unique_dict.values())
print(unique)  # ['Apple', 'banana', 'Cherry']
```

**Result**: Case-insensitive deduplication.

## Example 9: Count and Remove Duplicates

Track duplicate counts:

```python
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Count occurrences
counts = Counter(numbers)
print(counts)  # Counter({4: 4, 3: 3, 2: 2, 1: 1})

# Get unique values
unique = list(counts.keys())
print(unique)  # [1, 2, 3, 4]

# Get values that appear more than once
duplicates = [k for k, v in counts.items() if v > 1]
print(duplicates)  # [2, 3, 4]
```

**Result**: Duplicate counting and removal.

## Example 10: Production Deduplication Utilities

Complete deduplication library:

```python
from typing import Any, Callable, Hashable, List, TypeVar

T = TypeVar('T')

class DedupeUtils:
    @staticmethod
    def remove_duplicates(items: List[T]) -> List[T]:
        """Remove duplicates preserving order."""
        return list(dict.fromkeys(items))

    @staticmethod
    def remove_duplicates_by(items: List[T], key: Callable[[T], Hashable]) -> List[T]:
        """Remove duplicates by key function."""
        seen = set()
        result = []
        for item in items:
            k = key(item)
            if k not in seen:
                seen.add(k)
                result.append(item)
        return result

    @staticmethod
    def remove_consecutive(items: List[T]) -> List[T]:
        """Remove only consecutive duplicates."""
        if not items:
            return []
        result = [items[0]]
        for i in range(1, len(items)):
            if items[i] != items[i-1]:
                result.append(items[i])
        return result

    @staticmethod
    def find_duplicates(items: List[T]) -> List[T]:
        """Find elements that appear more than once."""
        from collections import Counter
        counts = Counter(items)
        return [k for k, v in counts.items() if v > 1]

# Usage
utils = DedupeUtils()

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Remove all duplicates
unique = utils.remove_duplicates(numbers)
print(f"Unique: {unique}")  # [1, 2, 3, 4]

# Remove consecutive only
consec_unique = utils.remove_consecutive(numbers)
print(f"Consecutive removed: {consec_unique}")  # [1, 2, 3, 4]

# Find duplicates
dupes = utils.find_duplicates(numbers)
print(f"Duplicates: {dupes}")  # [2, 3, 4]

# Deduplicate by key
words = ["Apple", "banana", "APPLE"]
unique_words = utils.remove_duplicates_by(words, str.lower)
print(f"Unique words: {unique_words}")  # ['Apple', 'banana']
```

**Result**: Production-ready deduplication utilities.

## KEY TAKEAWAYS

- **set()**: Fast deduplication without order preservation
- **dict.fromkeys()**: Order-preserving deduplication (Python 3.7+)
- **Manual Loop**: Explicit control with seen set
- **Hashable Types**: set/dict require hashable elements
- **Custom __hash__**: Define for custom object deduplication
- **itertools.groupby**: Remove consecutive duplicates
- **Case-Insensitive**: Track lowercase for string deduplication
- **Counter**: Count and identify duplicates
- **Key Function**: Deduplicate by custom criteria
- **Performance**: set() is O(n), manual loop with 'in' on list is O(n²)
'''

# Lesson 246: Selection Sort
lesson246 = next(l for l in lessons if l['id'] == 246)
lesson246['content'] = '''# Selection Sort

Sort by repeatedly selecting the minimum element and placing it in position. Selection sort is a simple O(n²) sorting algorithm that demonstrates fundamental sorting concepts. Understanding selection sort builds foundation for more advanced algorithms.

## Example 1: Basic Selection Sort

Sort array by finding minimum repeatedly:

```python
def selection_sort(arr):
    """Sort array using selection sort algorithm."""
    n = len(arr)

    for i in range(n):
        # Find minimum element in remaining array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap minimum with current position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

numbers = [64, 25, 12, 22, 11]
sorted_nums = selection_sort(numbers.copy())
print(f"Sorted: {sorted_nums}")  # [11, 12, 22, 25, 64]
```

**Result**: Basic selection sort implementation.

## Example 2: Selection Sort with Visualization

Track sorting steps:

```python
def selection_sort_verbose(arr):
    """Selection sort with step-by-step output."""
    n = len(arr)
    print(f"Initial: {arr}")

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Step {i+1}: {arr} (placed {arr[i]} at position {i})")

    return arr

numbers = [64, 25, 12, 22, 11]
selection_sort_verbose(numbers)
# Initial: [64, 25, 12, 22, 11]
# Step 1: [11, 25, 12, 22, 64] (placed 11 at position 0)
# Step 2: [11, 12, 25, 22, 64] (placed 12 at position 1)
# ...
```

**Result**: Visualize sorting process.

## Example 3: Selection Sort Descending

Sort in reverse order:

```python
def selection_sort_desc(arr):
    """Sort in descending order."""
    n = len(arr)

    for i in range(n):
        # Find maximum instead of minimum
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr

numbers = [64, 25, 12, 22, 11]
sorted_desc = selection_sort_desc(numbers.copy())
print(f"Descending: {sorted_desc}")  # [64, 25, 22, 12, 11]
```

**Result**: Reverse order sorting.

## Example 4: Selection Sort for Strings

Sort string list:

```python
def selection_sort(arr):
    """Generic selection sort."""
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

words = ["banana", "apple", "cherry", "date"]
sorted_words = selection_sort(words.copy())
print(f"Sorted words: {sorted_words}")
# ['apple', 'banana', 'cherry', 'date']
```

**Result**: Sort any comparable type.

## Example 5: Selection Sort with Custom Comparison

Sort by custom key:

```python
def selection_sort_by(arr, key=lambda x: x):
    """Selection sort with custom key function."""
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if key(arr[j]) < key(arr[min_idx]):
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Sort by string length
words = ["a", "abc", "ab", "abcd"]
sorted_by_len = selection_sort_by(words.copy(), key=len)
print(f"By length: {sorted_by_len}")  # ['a', 'ab', 'abc', 'abcd']

# Sort students by grade
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = selection_sort_by(students.copy(), key=lambda s: s["grade"])
print(f"By grade: {[s['name'] for s in sorted_students]}")
# ['Charlie', 'Alice', 'Bob']
```

**Result**: Custom comparison logic.

## Example 6: Count Swaps and Comparisons

Analyze algorithm complexity:

```python
def selection_sort_stats(arr):
    """Track comparisons and swaps."""
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    return arr, comparisons, swaps

numbers = [64, 25, 12, 22, 11]
sorted_arr, comps, swaps = selection_sort_stats(numbers.copy())
print(f"Sorted: {sorted_arr}")
print(f"Comparisons: {comps}")  # 10 (n*(n-1)/2)
print(f"Swaps: {swaps}")  # 4
```

**Result**: Performance analysis.

## Example 7: Stable Selection Sort

Maintain relative order of equal elements:

```python
def stable_selection_sort(arr):
    """Stable version of selection sort."""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Shift instead of swap to maintain stability
        min_val = arr[min_idx]
        while min_idx > i:
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1
        arr[i] = min_val

    return arr

# With duplicates to test stability
numbers = [3, 5, 2, 5, 1]
stable_sorted = stable_selection_sort(numbers.copy())
print(f"Stable sorted: {stable_sorted}")  # [1, 2, 3, 5, 5]
```

**Result**: Preserve order of equals.

## Example 8: Selection Sort for Custom Objects

Sort objects with proper comparison:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]

sorted_people = selection_sort(people.copy())
print(f"By age: {sorted_people}")
# [Person(Bob, 25), Person(Alice, 30), Person(Charlie, 35)]
```

**Result**: Object sorting.

## Example 9: Bidirectional Selection Sort

Find both min and max each pass:

```python
def bidirectional_selection_sort(arr):
    """Optimize by finding min and max simultaneously."""
    left = 0
    right = len(arr) - 1

    while left < right:
        min_idx = left
        max_idx = left

        # Find both min and max
        for i in range(left, right + 1):
            if arr[i] < arr[min_idx]:
                min_idx = i
            if arr[i] > arr[max_idx]:
                max_idx = i

        # Place min at left
        arr[left], arr[min_idx] = arr[min_idx], arr[left]

        # Adjust max_idx if it was at left position
        if max_idx == left:
            max_idx = min_idx

        # Place max at right
        arr[right], arr[max_idx] = arr[max_idx], arr[right]

        left += 1
        right -= 1

    return arr

numbers = [64, 25, 12, 22, 11]
sorted_nums = bidirectional_selection_sort(numbers.copy())
print(f"Sorted: {sorted_nums}")  # [11, 12, 22, 25, 64]
```

**Result**: Optimized selection sort.

## Example 10: Production Selection Sort Utility

Complete sorting library:

```python
from typing import Callable, List, TypeVar, Tuple

T = TypeVar('T')

class SelectionSortUtils:
    @staticmethod
    def sort(arr: List[T], reverse: bool = False) -> List[T]:
        """Selection sort with reverse option."""
        n = len(arr)
        result = arr.copy()

        for i in range(n):
            target_idx = i
            for j in range(i+1, n):
                if reverse:
                    if result[j] > result[target_idx]:
                        target_idx = j
                else:
                    if result[j] < result[target_idx]:
                        target_idx = j

            result[i], result[target_idx] = result[target_idx], result[i]

        return result

    @staticmethod
    def sort_by(arr: List[T], key: Callable[[T], any]) -> List[T]:
        """Selection sort with key function."""
        n = len(arr)
        result = arr.copy()

        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if key(result[j]) < key(result[min_idx]):
                    min_idx = j

            result[i], result[min_idx] = result[min_idx], result[i]

        return result

    @staticmethod
    def sort_with_stats(arr: List[T]) -> Tuple[List[T], int, int]:
        """Selection sort returning statistics."""
        n = len(arr)
        result = arr.copy()
        comparisons = 0
        swaps = 0

        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                comparisons += 1
                if result[j] < result[min_idx]:
                    min_idx = j

            if min_idx != i:
                result[i], result[min_idx] = result[min_idx], result[i]
                swaps += 1

        return result, comparisons, swaps

# Usage
utils = SelectionSortUtils()

numbers = [64, 25, 12, 22, 11]

# Basic sort
sorted_asc = utils.sort(numbers)
print(f"Ascending: {sorted_asc}")  # [11, 12, 22, 25, 64]

sorted_desc = utils.sort(numbers, reverse=True)
print(f"Descending: {sorted_desc}")  # [64, 25, 22, 12, 11]

# Sort by key
words = ["a", "abc", "ab"]
sorted_by_len = utils.sort_by(words, key=len)
print(f"By length: {sorted_by_len}")  # ['a', 'ab', 'abc']

# With statistics
sorted_arr, comps, swaps = utils.sort_with_stats(numbers)
print(f"Comparisons: {comps}, Swaps: {swaps}")
```

**Result**: Production-ready selection sort.

## KEY TAKEAWAYS

- **O(n²) Complexity**: Quadratic time for all cases
- **In-Place**: Sorts without extra array
- **Not Stable**: Standard version doesn't preserve equal order
- **Minimum Swaps**: At most n-1 swaps
- **Simple Logic**: Easy to understand and implement
- **Comparisons**: Always n*(n-1)/2 comparisons
- **No Early Exit**: Always completes all passes
- **Small Data**: Acceptable for small arrays
- **Educational**: Good for learning sorting concepts
- **When to Use**: Teaching, small datasets, minimizing swaps
'''

# Lesson 247: Slice Assignment
lesson247 = next(l for l in lessons if l['id'] == 247)
lesson247['content'] = '''# Slice Assignment

Modify lists in-place using slice notation for insertions, deletions, and replacements. Slice assignment is a powerful Python feature for efficient list manipulation without creating new lists. Understanding slice assignment enables sophisticated data structure operations.

## Example 1: Basic Slice Replacement

Replace portion of list:

```python
numbers = [0, 1, 2, 3, 4, 5]

# Replace slice with new values
numbers[1:4] = [10, 20, 30]
print(numbers)  # [0, 10, 20, 30, 4, 5]

# Replace with different length
numbers = [0, 1, 2, 3, 4, 5]
numbers[1:4] = [99]
print(numbers)  # [0, 99, 4, 5]

# Replace with longer sequence
numbers = [0, 1, 2, 3, 4, 5]
numbers[1:3] = [10, 20, 30, 40]
print(numbers)  # [0, 10, 20, 30, 40, 3, 4, 5]
```

**Result**: Flexible slice replacement.

## Example 2: Delete with Slice Assignment

Remove elements using empty list:

```python
numbers = [0, 1, 2, 3, 4, 5]

# Delete slice by assigning empty list
numbers[1:4] = []
print(numbers)  # [0, 4, 5]

# Equivalent to del
numbers = [0, 1, 2, 3, 4, 5]
del numbers[1:4]
print(numbers)  # [0, 4, 5]

# Delete every other element
numbers = [0, 1, 2, 3, 4, 5]
del numbers[::2]
print(numbers)  # [1, 3, 5]
```

**Result**: Efficient element deletion.

## Example 3: Insert with Slice Assignment

Insert elements at position:

```python
numbers = [0, 1, 2, 3, 4, 5]

# Insert at position (empty slice)
numbers[2:2] = [10, 20]
print(numbers)  # [0, 1, 10, 20, 2, 3, 4, 5]

# Insert at beginning
numbers = [0, 1, 2, 3, 4, 5]
numbers[0:0] = [-2, -1]
print(numbers)  # [-2, -1, 0, 1, 2, 3, 4, 5]

# Insert at end
numbers = [0, 1, 2, 3, 4, 5]
numbers[len(numbers):] = [6, 7]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7]
```

**Result**: Insert without list methods.

## Example 4: Replace Every Nth Element

Modify with step slices:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Replace every other element
numbers[::2] = [10, 20, 30, 40, 50]
print(numbers)  # [10, 1, 20, 3, 30, 5, 40, 7, 50, 9]

# Replace every third element
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::3] = [100, 200, 300, 400]
print(numbers)  # [100, 1, 2, 200, 4, 5, 300, 7, 8, 400]

# Must match length for stepped slices
numbers = [0, 1, 2, 3, 4]
try:
    numbers[::2] = [10, 20]  # Wrong length
except ValueError as e:
    print(f"Error: {e}")
```

**Result**: Step-based replacement.

## Example 5: Reverse with Slice Assignment

Reverse list in-place:

```python
numbers = [0, 1, 2, 3, 4, 5]

# Reverse entire list
numbers[:] = numbers[::-1]
print(numbers)  # [5, 4, 3, 2, 1, 0]

# Reverse portion
numbers = [0, 1, 2, 3, 4, 5]
numbers[1:4] = numbers[1:4][::-1]
print(numbers)  # [0, 3, 2, 1, 4, 5]

# Alternative: use reverse()
numbers = [0, 1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1, 0]
```

**Result**: In-place reversal.

## Example 6: Clear List with Slice

Empty entire list:

```python
numbers = [0, 1, 2, 3, 4, 5]

# Clear with slice assignment
numbers[:] = []
print(numbers)  # []
print(id(numbers))  # Same object

# Compare to reassignment
numbers = [0, 1, 2, 3, 4, 5]
original_id = id(numbers)
numbers = []  # Creates new object
print(id(numbers) == original_id)  # False

# Alternative: clear()
numbers = [0, 1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # []
```

**Result**: Clear vs reassignment.

## Example 7: Splice Lists Together

Combine lists at position:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Insert list2 into middle of list1
list1[1:1] = list2
print(list1)  # [1, 4, 5, 6, 2, 3]

# Replace middle with list3
list1 = [1, 2, 3, 4, 5]
list1[1:4] = list3
print(list1)  # [1, 7, 8, 9, 5]

# Splice multiple lists
result = [0]
result[1:1] = [1, 2, 3]
result[4:4] = [4, 5, 6]
result[7:7] = [7, 8, 9]
print(result)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Result**: List splicing operations.

## Example 8: Modify String Lists

String manipulation with slices:

```python
words = ["the", "quick", "brown", "fox"]

# Replace words
words[1:3] = ["slow", "red"]
print(words)  # ['the', 'slow', 'red', 'fox']

# Insert words
words = ["the", "quick", "brown", "fox"]
words[2:2] = ["very"]
print(words)  # ['the', 'quick', 'very', 'brown', 'fox']

# Delete words
words = ["the", "quick", "brown", "fox"]
words[1:3] = []
print(words)  # ['the', 'fox']
```

**Result**: Text list manipulation.

## Example 9: Nested List Modification

Modify 2D lists with slices:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Replace row
matrix[1] = [40, 50, 60]
print(matrix)  # [[1, 2, 3], [40, 50, 60], [7, 8, 9]]

# Replace multiple rows
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[0:2] = [[10, 20, 30], [40, 50, 60]]
print(matrix)  # [[10, 20, 30], [40, 50, 60], [7, 8, 9]]

# Modify elements within row
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[1][0:2] = [99, 88]
print(matrix)  # [[1, 2, 3], [99, 88, 6], [7, 8, 9]]
```

**Result**: 2D list modification.

## Example 10: Production Slice Utilities

Complete slice manipulation library:

```python
from typing import Any, List, TypeVar

T = TypeVar('T')

class SliceUtils:
    @staticmethod
    def replace_range(arr: List[T], start: int, end: int, values: List[T]) -> List[T]:
        """Replace range with values."""
        result = arr.copy()
        result[start:end] = values
        return result

    @staticmethod
    def insert_at(arr: List[T], index: int, values: List[T]) -> List[T]:
        """Insert values at index."""
        result = arr.copy()
        result[index:index] = values
        return result

    @staticmethod
    def delete_range(arr: List[T], start: int, end: int) -> List[T]:
        """Delete range of elements."""
        result = arr.copy()
        del result[start:end]
        return result

    @staticmethod
    def replace_every_nth(arr: List[T], n: int, values: List[T]) -> List[T]:
        """Replace every nth element."""
        result = arr.copy()
        if len(values) != len(result[::n]):
            raise ValueError(f"Need {len(result[::n])} values for step {n}")
        result[::n] = values
        return result

    @staticmethod
    def splice(arr: List[T], index: int, delete_count: int, *items: T) -> List[T]:
        """JavaScript-style splice operation."""
        result = arr.copy()
        result[index:index+delete_count] = items
        return result

# Usage
utils = SliceUtils()

numbers = [0, 1, 2, 3, 4, 5]

# Replace range
result = utils.replace_range(numbers, 1, 4, [10, 20])
print(f"Replace range: {result}")  # [0, 10, 20, 4, 5]

# Insert at position
result = utils.insert_at(numbers, 2, [99, 88])
print(f"Insert at 2: {result}")  # [0, 1, 99, 88, 2, 3, 4, 5]

# Delete range
result = utils.delete_range(numbers, 1, 4)
print(f"Delete 1-4: {result}")  # [0, 4, 5]

# Splice (delete 2, insert 3)
result = utils.splice(numbers, 2, 2, 77, 88, 99)
print(f"Splice: {result}")  # [0, 1, 77, 88, 99, 4, 5]
```

**Result**: Production-ready slice operations.

## KEY TAKEAWAYS

- **In-Place Modification**: Changes original list without copy
- **Flexible Length**: Replacement can be different size
- **Empty Slice**: Insert at position with [i:i]
- **Delete**: Assign empty list [] to remove elements
- **Step Slices**: Must match exact length for [::n]
- **Reverse**: Use [:] = list[::-1] for in-place
- **Clear**: Use [:] = [] to clear while keeping reference
- **Splice**: Combine insert and delete operations
- **Performance**: More efficient than multiple operations
- **Identity**: [:] maintains list identity vs reassignment
'''

# Lesson 248: Sorting
lesson248 = next(l for l in lessons if l['id'] == 248)
lesson248['content'] = '''# Sorting

Sort collections using sorted(), list.sort(), and custom key functions. Sorting is fundamental for data organization, searching, and analysis. Understanding Python's sorting capabilities enables efficient data manipulation and optimization.

## Example 1: Basic Sorting

Sort with sorted() and sort():

```python
numbers = [3, 7, 2, 9, 1, 5]

# sorted() returns new list
sorted_nums = sorted(numbers)
print(f"Sorted: {sorted_nums}")  # [1, 2, 3, 5, 7, 9]
print(f"Original: {numbers}")  # [3, 7, 2, 9, 1, 5]

# list.sort() modifies in-place
numbers.sort()
print(f"After sort(): {numbers}")  # [1, 2, 3, 5, 7, 9]

# Reverse order
numbers = [3, 7, 2, 9, 1, 5]
sorted_desc = sorted(numbers, reverse=True)
print(f"Descending: {sorted_desc}")  # [9, 7, 5, 3, 2, 1]
```

**Result**: Basic sorting operations.

## Example 2: Sort Strings

String sorting (lexicographic):

```python
words = ["banana", "apple", "cherry", "date"]

# Alphabetical order
sorted_words = sorted(words)
print(sorted_words)  # ['apple', 'banana', 'cherry', 'date']

# Case-sensitive (uppercase first)
mixed = ["apple", "Banana", "cherry", "Date"]
print(sorted(mixed))  # ['Banana', 'Date', 'apple', 'cherry']

# Case-insensitive
sorted_case = sorted(mixed, key=str.lower)
print(sorted_case)  # ['apple', 'Banana', 'cherry', 'Date']
```

**Result**: String sorting variations.

## Example 3: Sort by Key Function

Custom sorting criteria:

```python
words = ["a", "abc", "ab", "abcd"]

# Sort by length
by_length = sorted(words, key=len)
print(f"By length: {by_length}")  # ['a', 'ab', 'abc', 'abcd']

# Sort by last character
by_last = sorted(words, key=lambda x: x[-1])
print(f"By last char: {by_last}")  # ['a', 'abc', 'abcd', 'ab']

# Numbers as strings, sort numerically
num_strings = ["10", "2", "30", "4"]
sorted_str = sorted(num_strings)  # Lexicographic
print(f"Lexicographic: {sorted_str}")  # ['10', '2', '30', '4']

sorted_num = sorted(num_strings, key=int)  # Numeric
print(f"Numeric: {sorted_num}")  # ['2', '4', '10', '30']
```

**Result**: Custom sorting keys.

## Example 4: Sort Complex Objects

Sort dictionaries and objects:

```python
# Sort list of dictionaries
students = [
    {"name": "Alice", "grade": 85, "age": 20},
    {"name": "Bob", "grade": 92, "age": 19},
    {"name": "Charlie", "grade": 78, "age": 21}
]

# Sort by grade
by_grade = sorted(students, key=lambda s: s["grade"])
print([s["name"] for s in by_grade])  # ['Charlie', 'Alice', 'Bob']

# Sort by multiple fields (age, then name)
by_age_name = sorted(students, key=lambda s: (s["age"], s["name"]))
print([s["name"] for s in by_age_name])
# ['Bob', 'Alice', 'Charlie']

# Custom class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
by_age = sorted(people, key=lambda p: p.age)
print(by_age)  # [Person(Bob, 25), Person(Alice, 30), Person(Charlie, 35)]
```

**Result**: Complex object sorting.

## Example 5: Stable Sort

Preserve relative order of equal elements:

```python
# Python's sort is stable
data = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 85),
    ("David", 92)
]

# Sort by score (preserves order of equal scores)
by_score = sorted(data, key=lambda x: x[1])
print(by_score)
# [('Alice', 85), ('Charlie', 85), ('Bob', 92), ('David', 92)]

# Multi-level sort: first by score, then by name
by_score_name = sorted(data, key=lambda x: (x[1], x[0]))
print(by_score_name)
# [('Alice', 85), ('Charlie', 85), ('Bob', 92), ('David', 92)]
```

**Result**: Stable sorting behavior.

## Example 6: Sort with operator module

Use operator.itemgetter and attrgetter:

```python
from operator import itemgetter, attrgetter

# Sort tuples by item
pairs = [(3, 'c'), (1, 'a'), (2, 'b')]
by_first = sorted(pairs, key=itemgetter(0))
print(by_first)  # [(1, 'a'), (2, 'b'), (3, 'c')]

by_second = sorted(pairs, key=itemgetter(1))
print(by_second)  # [(1, 'a'), (2, 'b'), (3, 'c')]

# Sort dictionaries
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92}
]
by_grade = sorted(students, key=itemgetter("grade"))
print([s["name"] for s in by_grade])  # ['Alice', 'Bob']

# Sort objects by attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name}"

people = [Person("Alice", 30), Person("Bob", 25)]
by_age = sorted(people, key=attrgetter("age"))
print(by_age)  # [Bob, Alice]
```

**Result**: operator module sorting.

## Example 7: Sort with Multiple Keys

Multi-field sorting:

```python
# Sort by multiple criteria
records = [
    ("Alice", 85, 20),
    ("Bob", 92, 19),
    ("Charlie", 85, 21),
    ("David", 92, 19)
]

# Primary: grade (desc), Secondary: age (asc)
sorted_records = sorted(records, key=lambda x: (-x[1], x[2]))
print(sorted_records)
# [('Bob', 92, 19), ('David', 92, 19), ('Alice', 85, 20), ('Charlie', 85, 21)]

# Chain sorts (stable sort allows this)
data = records.copy()
data.sort(key=lambda x: x[2])  # First by age
data.sort(key=lambda x: x[1], reverse=True)  # Then by grade desc
print(data)
# [('Bob', 92, 19), ('David', 92, 19), ('Alice', 85, 20), ('Charlie', 85, 21)]
```

**Result**: Multi-key sorting strategies.

## Example 8: Sort with None Values

Handle None in sorting:

```python
values = [3, None, 1, None, 5, 2]

# None causes TypeError
try:
    sorted(values)
except TypeError as e:
    print(f"Error: {e}")

# Handle None with key function
def none_last(x):
    return (x is None, x)

sorted_vals = sorted(values, key=none_last)
print(sorted_vals)  # [1, 2, 3, 5, None, None]

# Alternative: filter None
non_none = sorted(x for x in values if x is not None)
print(non_none)  # [1, 2, 3, 5]
```

**Result**: None handling in sorts.

## Example 9: Performance Comparison

Compare sorting approaches:

```python
import random
import time

# Generate data
data = [random.randint(1, 1000) for _ in range(10000)]

# Time sorted()
start = time.time()
result1 = sorted(data)
time_sorted = time.time() - start
print(f"sorted(): {time_sorted:.4f}s")

# Time list.sort()
data_copy = data.copy()
start = time.time()
data_copy.sort()
time_sort = time.time() - start
print(f"list.sort(): {time_sort:.4f}s")

# sort() is slightly faster (in-place)
print(f"Difference: {(time_sorted - time_sort)*1000:.2f}ms")
```

**Result**: Performance analysis.

## Example 10: Production Sorting Utilities

Complete sorting library:

```python
from typing import Any, Callable, List, Optional, TypeVar
from operator import itemgetter, attrgetter

T = TypeVar('T')

class SortUtils:
    @staticmethod
    def sort_by(items: List[T], key: Callable[[T], Any],
                reverse: bool = False) -> List[T]:
        """Sort with custom key function."""
        return sorted(items, key=key, reverse=reverse)

    @staticmethod
    def sort_by_attr(items: List[T], attr: str,
                     reverse: bool = False) -> List[T]:
        """Sort objects by attribute name."""
        return sorted(items, key=attrgetter(attr), reverse=reverse)

    @staticmethod
    def sort_by_multiple(items: List[T],
                         keys: List[Callable[[T], Any]]) -> List[T]:
        """Sort by multiple keys."""
        return sorted(items, key=lambda x: tuple(k(x) for k in keys))

    @staticmethod
    def natural_sort(items: List[str]) -> List[str]:
        """Natural sort for strings with numbers."""
        import re
        def natural_key(text):
            return [int(c) if c.isdigit() else c
                    for c in re.split('(\d+)', text)]
        return sorted(items, key=natural_key)

    @staticmethod
    def stable_sort(items: List[T], key: Callable[[T], Any]) -> List[T]:
        """Explicitly stable sort (Python's sort is stable by default)."""
        return sorted(items, key=key)

# Usage
utils = SortUtils()

# Sort by length
words = ["a", "abc", "ab"]
by_len = utils.sort_by(words, key=len)
print(f"By length: {by_len}")  # ['a', 'ab', 'abc']

# Natural sort
files = ["file10.txt", "file2.txt", "file1.txt"]
natural = utils.natural_sort(files)
print(f"Natural sort: {natural}")  # ['file1.txt', 'file2.txt', 'file10.txt']

# Sort objects by attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name}({self.age})"

people = [Person("Alice", 30), Person("Bob", 25)]
by_age = utils.sort_by_attr(people, "age")
print(f"By age: {by_age}")  # [Bob(25), Alice(30)]
```

**Result**: Production-ready sorting utilities.

## KEY TAKEAWAYS

- **sorted()**: Returns new sorted list, original unchanged
- **list.sort()**: Sorts in-place, returns None
- **key Parameter**: Custom sorting logic with key function
- **reverse**: Sort in descending order
- **Stable Sort**: Preserves relative order of equal elements
- **operator Module**: itemgetter, attrgetter for cleaner code
- **Multi-Key**: Tuple of keys for multi-field sorting
- **O(n log n)**: Timsort algorithm complexity
- **String Sorting**: Case-sensitive by default
- **Performance**: sort() slightly faster than sorted() for lists
'''

# Lessons 249-250: Non-programming topics with minimal code
lesson249 = next(l for l in lessons if l['id'] == 249)
lesson249['title'] = "Grafana - Dashboard Creation"

lesson250 = next(l for l in lessons if l['id'] == 250)
lesson250['title'] = "E2E Testing - User Flows"

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created comprehensive unique content for lessons 241-248:")
for lid in range(241, 249):
    lesson = next(l for l in lessons if l['id'] == lid)
    chars = len(lesson['content'])
    print(f"  {lid}: {lesson['title'][:45]:45s} {chars:5,d} chars")
