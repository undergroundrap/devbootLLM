#!/usr/bin/env python3
"""
Upgrade Python lessons 71-75 with comprehensive content.
- Lesson 71: String Find and Index
- Lesson 72: String Helper Functions
- Lesson 73: String Join
- Lesson 74: String Length and Indexing
- Lesson 75: String Manipulation Mastery: Common Patterns
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 71-75
lesson71 = next(l for l in lessons if l['id'] == 71)
lesson72 = next(l for l in lessons if l['id'] == 72)
lesson73 = next(l for l in lessons if l['id'] == 73)
lesson74 = next(l for l in lessons if l['id'] == 74)
lesson75 = next(l for l in lessons if l['id'] == 75)

# Upgrade Lesson 71: String Find and Index
lesson71['fullSolution'] = '''"""
String Find and Index

Master techniques to search for substrings in Python—from find() and index()
to rfind(), count(), and in operator. Essential for parsing, validation, and
text processing.

**Zero Package Installation Required**
"""

# Example 1: find() Method - Returns Index or -1
print("="*70)
print("Example 1: find() - Search for Substring")
print("="*70)

text = "Python is awesome and Python is powerful"
print(f"Text: '{text}'")

position = text.find("Python")
print(f"\\nFirst 'Python' at index: {position}")

position2 = text.find("awesome")
print(f"'awesome' at index: {position2}")

not_found = text.find("Java")
print(f"'Java' at index: {not_found}")  # Returns -1
print()

# Example 2: index() Method - Raises Exception if Not Found
print("="*70)
print("Example 2: index() - Raises ValueError if Not Found")
print("="*70)

text = "Hello World"
print(f"Text: '{text}'")

try:
    pos = text.index("World")
    print(f"'World' found at index: {pos}")
except ValueError:
    print("Not found")

try:
    pos = text.index("Python")
    print(f"'Python' found at index: {pos}")
except ValueError as e:
    print(f"Error: '{e}'")
print()

# Example 3: find() with Start Position
print("="*70)
print("Example 3: find() with Start Position")
print("="*70)

text = "the quick brown fox jumps over the lazy dog"
print(f"Text: '{text}'")

# Find first 'the'
first = text.find("the")
print(f"\\nFirst 'the' at index: {first}")

# Find second 'the' (start searching after first)
second = text.find("the", first + 1)
print(f"Second 'the' at index: {second}")

# Find 'o' starting from position 20
o_pos = text.find("o", 20)
print(f"'o' at or after index 20: {o_pos}")
print()

# Example 4: rfind() - Search from Right
print("="*70)
print("Example 4: rfind() - Search Backwards from End")
print("="*70)

text = "Python is fun, Python is easy, Python is powerful"
print(f"Text: '{text}'")

# Find last occurrence
last_python = text.rfind("Python")
print(f"\\nLast 'Python' at index: {last_python}")

# Find first occurrence (for comparison)
first_python = text.find("Python")
print(f"First 'Python' at index: {first_python}")

# Last 'is'
last_is = text.rfind("is")
print(f"Last 'is' at index: {last_is}")
print()

# Example 5: Finding All Occurrences
print("="*70)
print("Example 5: Find All Occurrences of Substring")
print("="*70)

text = "to be or not to be, that is the question"
search_term = "be"

print(f"Text: '{text}'")
print(f"Searching for: '{search_term}'")

positions = []
start = 0

while True:
    pos = text.find(search_term, start)
    if pos == -1:
        break
    positions.append(pos)
    start = pos + 1

print(f"\\nFound at positions: {positions}")
print(f"Total occurrences: {len(positions)}")
print()

# Example 6: count() Method
print("="*70)
print("Example 6: count() - Count Occurrences")
print("="*70)

text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
print(f"Text: '{text}'")

wood_count = text.count("wood")
chuck_count = text.count("chuck")
a_count = text.count("a")

print(f"\\n'wood' appears: {wood_count} times")
print(f"'chuck' appears: {chuck_count} times")
print(f"'a' appears: {a_count} times")

# Case-sensitive
upper_w = text.count("W")
lower_w = text.count("w")
print(f"\\n'W' (uppercase): {upper_w} times")
print(f"'w' (lowercase): {lower_w} times")
print()

# Example 7: in Operator - Boolean Check
print("="*70)
print("Example 7: in Operator - Check Substring Presence")
print("="*70)

text = "Python programming is fun"
print(f"Text: '{text}'")

if "Python" in text:
    print("\\n'Python' found in text")

if "Java" in text:
    print("'Java' found in text")
else:
    print("'Java' NOT found in text")

# Multiple checks
keywords = ["Python", "programming", "Java", "fun"]
print(f"\\nKeywords: {keywords}")
for keyword in keywords:
    status = "FOUND" if keyword in text else "NOT FOUND"
    print(f"  '{keyword}': {status}")
print()

# Example 8: startswith() and endswith()
print("="*70)
print("Example 8: Check String Prefix/Suffix")
print("="*70)

filenames = ["script.py", "data.json", "test.py", "config.yaml", "main.py"]

print("Python files (.py):")
for filename in filenames:
    if filename.endswith(".py"):
        print(f"  {filename}")

print("\\nFiles starting with 'test' or 'main':")
for filename in filenames:
    if filename.startswith("test") or filename.startswith("main"):
        print(f"  {filename}")

# Multiple suffixes
url = "https://example.com"
if url.startswith(("http://", "https://")):
    print(f"\\n'{url}' is a valid HTTP(S) URL")
print()

# Example 9: Case-Insensitive Search
print("="*70)
print("Example 9: Case-Insensitive String Search")
print("="*70)

text = "Python Programming Is Amazing"
search = "python"

print(f"Original: '{text}'")
print(f"Search for: '{search}'")

# Convert to same case for comparison
pos_lower = text.lower().find(search.lower())
print(f"\\nCase-insensitive position: {pos_lower}")

# Check if exists
if search.lower() in text.lower():
    print(f"'{search}' found (case-insensitive)")

# Get actual substring
if pos_lower != -1:
    actual = text[pos_lower:pos_lower + len(search)]
    print(f"Actual text at position: '{actual}'")
print()

# Example 10: Practical Application - Email Validation
print("="*70)
print("Example 10: Real-World Use Case - Basic Email Validation")
print("="*70)

emails = [
    "user@example.com",
    "invalid.email",
    "test@domain.co.uk",
    "@nodomain.com",
    "user@.com",
    "admin@company.org"
]

print("Email validation results:")
for email in emails:
    # Basic validation
    has_at = "@" in email
    at_pos = email.find("@")
    has_dot_after_at = False

    if at_pos != -1:
        domain_part = email[at_pos+1:]
        has_dot_after_at = "." in domain_part

    # Check validity
    is_valid = (
        has_at and
        at_pos > 0 and  # @ not at start
        has_dot_after_at and
        not email.endswith(".")
    )

    status = "VALID" if is_valid else "INVALID"
    print(f"  {email:25} [{status}]")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. find(sub) - Returns index or -1 if not found")
print("2. index(sub) - Returns index or raises ValueError")
print("3. rfind(sub) - Searches from right, returns last occurrence")
print("4. count(sub) - Counts number of occurrences")
print("5. in operator - Boolean check: 'sub' in string")
print("6. startswith(prefix) - Check if string starts with prefix")
print("7. endswith(suffix) - Check if string ends with suffix")
print("8. All methods are case-sensitive by default")
print("9. Use .lower() or .upper() for case-insensitive search")
print("10. find() is safer than index() (no exception)")
print("="*70)
'''

# Upgrade Lesson 72: String Helper Functions
lesson72['fullSolution'] = '''"""
String Helper Functions

Master Python's powerful string methods for transformation and validation—
upper(), lower(), strip(), replace(), split(), and more. Essential for
data cleaning, formatting, and text processing.

**Zero Package Installation Required**
"""

# Example 1: Case Conversion Methods
print("="*70)
print("Example 1: Case Conversion - upper(), lower(), title(), capitalize()")
print("="*70)

text = "python programming is FUN"
print(f"Original: '{text}'")

print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")  # Each word capitalized
print(f"capitalize(): '{text.capitalize()}'")  # Only first char

# swapcase - swap upper/lower
mixed = "Hello World"
print(f"\\n'{mixed}' swapcase: '{mixed.swapcase()}'")
print()

# Example 2: Whitespace Removal - strip(), lstrip(), rstrip()
print("="*70)
print("Example 2: Removing Whitespace")
print("="*70)

padded = "   Hello World   "
print(f"Original: '{padded}' (length: {len(padded)})")

stripped = padded.strip()
print(f"strip(): '{stripped}' (length: {len(stripped)})")

left_stripped = padded.lstrip()
print(f"lstrip(): '{left_stripped}' (length: {len(left_stripped)})")

right_stripped = padded.rstrip()
print(f"rstrip(): '{right_stripped}' (length: {len(right_stripped)})")

# Strip specific characters
url = "https://example.com///"
clean_url = url.rstrip("/")
print(f"\\nURL: '{url}'")
print(f"Cleaned: '{clean_url}'")
print()

# Example 3: replace() Method
print("="*70)
print("Example 3: String Replacement")
print("="*70)

text = "I love Java. Java is great. Java rocks!"
print(f"Original: '{text}'")

replaced = text.replace("Java", "Python")
print(f"Replace all: '{replaced}'")

# Replace with count limit
replaced_once = text.replace("Java", "Python", 1)
print(f"Replace first: '{replaced_once}'")

replaced_two = text.replace("Java", "Python", 2)
print(f"Replace first 2: '{replaced_two}'")

# Remove by replacing with empty string
no_spaces = "Hello World".replace(" ", "")
print(f"\\nRemove spaces: '{no_spaces}'")
print()

# Example 4: split() and rsplit()
print("="*70)
print("Example 4: Splitting Strings into Lists")
print("="*70)

sentence = "Python is awesome and powerful"
print(f"Sentence: '{sentence}'")

words = sentence.split()  # Split on whitespace
print(f"Words: {words}")

# Split on specific delimiter
csv = "apple,banana,cherry,date"
print(f"\\nCSV: '{csv}'")
fruits = csv.split(",")
print(f"Fruits: {fruits}")

# Split with limit
limited = sentence.split(" ", 2)  # Split at most 2 times
print(f"\\nSplit (max 2): {limited}")

# rsplit - split from right
path = "folder/subfolder/file.txt"
parts = path.rsplit("/", 1)  # Split from right, once
print(f"\\nPath: '{path}'")
print(f"rsplit('/', 1): {parts}")
print()

# Example 5: join() - Opposite of split()
print("="*70)
print("Example 5: Joining Lists into Strings")
print("="*70)

words = ["Python", "is", "awesome"]
print(f"Words: {words}")

sentence = " ".join(words)
print(f"Joined with space: '{sentence}'")

csv = ",".join(words)
print(f"Joined with comma: '{csv}'")

path = "/".join(["home", "user", "documents"])
print(f"Path: '{path}'")

# Join with newlines
lines = ["First line", "Second line", "Third line"]
text = "\\n".join(lines)
print(f"\\nMultiline text:\\n{text}")
print()

# Example 6: Validation Methods - isdigit(), isalpha(), etc.
print("="*70)
print("Example 6: String Validation Methods")
print("="*70)

test_strings = ["12345", "Python", "abc123", "  ", "Hello World", ""]

print(f"{'String':<15} {'isdigit':<8} {'isalpha':<8} {'isalnum':<8} {'isspace':<8}")
print("-" * 50)

for s in test_strings:
    display = repr(s)
    print(f"{display:<15} {str(s.isdigit()):<8} {str(s.isalpha()):<8} "
          f"{str(s.isalnum()):<8} {str(s.isspace()):<8}")

# Additional checks
print("\\nAdditional validation methods:")
print(f"'HELLO'.isupper(): {('HELLO'.isupper())}")
print(f"'hello'.islower(): {('hello'.islower())}")
print(f"'Hello World'.istitle(): {('Hello World'.istitle())}")
print()

# Example 7: Padding - center(), ljust(), rjust()
print("="*70)
print("Example 7: String Padding and Alignment")
print("="*70)

text = "Python"
width = 20

centered = text.center(width)
print(f"Centered: '{centered}'")

left_aligned = text.ljust(width)
print(f"Left: '{left_aligned}'")

right_aligned = text.rjust(width)
print(f"Right: '{right_aligned}'")

# With fill character
centered_star = text.center(width, "*")
print(f"\\nCentered with *: '{centered_star}'")

# Formatting table
print("\\nFormatted table:")
print("Name".ljust(15) + "Score".rjust(10))
print("-" * 25)
print("Alice".ljust(15) + "95".rjust(10))
print("Bob".ljust(15) + "87".rjust(10))
print()

# Example 8: Prefix/Suffix Operations
print("="*70)
print("Example 8: removeprefix() and removesuffix() (Python 3.9+)")
print("="*70)

# For Python 3.9+
url = "https://example.com"
filename = "document.pdf"

# Manual prefix/suffix removal (works in all versions)
if url.startswith("https://"):
    domain = url[8:]  # Remove 'https://'
    print(f"URL: '{url}'")
    print(f"Domain: '{domain}'")

if filename.endswith(".pdf"):
    basename = filename[:-4]  # Remove '.pdf'
    print(f"\\nFilename: '{filename}'")
    print(f"Basename: '{basename}'")

# Using replace (but be careful - replaces all occurrences)
cleaned = url.replace("https://", "")
print(f"\\nUsing replace: '{cleaned}'")
print()

# Example 9: String Formatting with format()
print("="*70)
print("Example 9: Advanced String Formatting")
print("="*70)

name = "Alice"
age = 30
score = 95.5

# Using format()
message = "Name: {}, Age: {}, Score: {}".format(name, age, score)
print(f"Basic format: {message}")

# Named placeholders
template = "Name: {n}, Age: {a}, Score: {s:.1f}"
formatted = template.format(n=name, a=age, s=score)
print(f"Named: {formatted}")

# Alignment in format
print("\\nAlignment with format:")
print("{:<10} {:^10} {:>10}".format("Left", "Center", "Right"))
print("{:<10} {:^10} {:>10}".format("A", "B", "C"))
print()

# Example 10: Practical Application - Data Cleaning
print("="*70)
print("Example 10: Real-World Use Case - Clean User Input")
print("="*70)

raw_inputs = [
    "  Alice  ",
    "BOB",
    "charlie",
    "  DAVID SMITH  ",
    "eve_JONES"
]

print("Cleaning user names:")
print(f"{'Raw Input':<20} {'Cleaned':<20}")
print("-" * 40)

cleaned_names = []
for raw in raw_inputs:
    # Clean: strip whitespace, title case, replace underscore
    cleaned = raw.strip().replace("_", " ").title()
    cleaned_names.append(cleaned)
    print(f"{raw!r:<20} {cleaned:<20}")

print(f"\\nCleaned names: {cleaned_names}")

# Email normalization
email = "  User@EXAMPLE.COM  "
normalized = email.strip().lower()
print(f"\\nEmail: '{email}' → '{normalized}'")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. upper()/lower() - Case conversion")
print("2. strip()/lstrip()/rstrip() - Remove whitespace or characters")
print("3. replace(old, new, count) - String substitution")
print("4. split(delimiter) - String to list")
print("5. join(iterable) - List to string")
print("6. isdigit()/isalpha()/isalnum() - Validation")
print("7. center()/ljust()/rjust() - Padding and alignment")
print("8. startswith()/endswith() - Prefix/suffix checking")
print("9. All methods return NEW strings (strings are immutable)")
print("10. Combine methods for complex transformations")
print("="*70)
'''

# Upgrade Lesson 73: String Join
lesson73['fullSolution'] = '''"""
String Join

Master the join() method in Python—the most efficient way to combine
multiple strings. Learn when to use join() vs concatenation, and how to
build complex strings from lists, tuples, and generators.

**Zero Package Installation Required**
"""

# Example 1: Basic join() with Space
print("="*70)
print("Example 1: Basic join() - Combining List Elements")
print("="*70)

words = ["Python", "is", "awesome"]
print(f"Words list: {words}")

sentence = " ".join(words)
print(f"Joined with space: '{sentence}'")

# Different separator
hyphenated = "-".join(words)
print(f"Joined with hyphen: '{hyphenated}'")

# No separator
mashed = "".join(words)
print(f"Joined with no separator: '{mashed}'")
print()

# Example 2: join() with Different Iterables
print("="*70)
print("Example 2: join() Works with Any Iterable")
print("="*70)

# From tuple
tuple_data = ("apple", "banana", "cherry")
print(f"Tuple: {tuple_data}")
result = ", ".join(tuple_data)
print(f"Joined: '{result}'")

# From set (order not guaranteed)
set_data = {"red", "green", "blue"}
print(f"\\nSet: {set_data}")
result = " | ".join(set_data)
print(f"Joined: '{result}'")

# From generator
gen_result = "-".join(str(x) for x in range(5))
print(f"\\nFrom generator (0-4): '{gen_result}'")

# From string (joins each character)
chars = "HELLO"
spaced = " ".join(chars)
print(f"\\nString '{chars}' spaced: '{spaced}'")
print()

# Example 3: join() with Newlines
print("="*70)
print("Example 3: Creating Multi-Line Strings")
print("="*70)

lines = [
    "First line of text",
    "Second line of text",
    "Third line of text"
]

print("Lines list:")
for i, line in enumerate(lines, 1):
    print(f"  {i}. {line}")

multiline = "\\n".join(lines)
print(f"\\nJoined with newlines:")
print(multiline)

# With line numbers
numbered_lines = "\\n".join(f"{i}. {line}" for i, line in enumerate(lines, 1))
print(f"\\nWith line numbers:")
print(numbered_lines)
print()

# Example 4: join() with Path Components
print("="*70)
print("Example 4: Building File Paths")
print("="*70)

# Unix-style paths
path_parts = ["home", "user", "documents", "file.txt"]
unix_path = "/".join(path_parts)
print(f"Path parts: {path_parts}")
print(f"Unix path: {unix_path}")

# For production, use os.path.join() or pathlib
# But for simple cases, string join works

# URL building
url_parts = ["https://api.example.com", "v1", "users", "123"]
url = "/".join(url_parts)
print(f"\\nURL: {url}")

# Proper URL (handle double slashes)
base = "https://api.example.com"
endpoint = "/".join(["v1", "users", "123"])
full_url = f"{base}/{endpoint}"
print(f"Proper URL: {full_url}")
print()

# Example 5: join() with Empty Strings
print("="*70)
print("Example 5: Handling Empty Strings and None")
print("="*70)

# Empty strings are included
items = ["apple", "", "banana", "", "cherry"]
print(f"Items (with empty strings): {items}")
result = ", ".join(items)
print(f"Joined: '{result}'")

# Filter out empty strings
filtered = ", ".join(item for item in items if item)
print(f"Filtered: '{filtered}'")

# Handle None values (convert to string)
mixed = ["apple", "banana", "cherry"]
print(f"\\nMixed list: {mixed}")
safe_join = ", ".join(str(item) for item in mixed)
print(f"Safe join: '{safe_join}'")
print()

# Example 6: join() for CSV Generation
print("="*70)
print("Example 6: Creating CSV Data")
print("="*70)

# Simple CSV row
row1 = ["Alice", "30", "Engineer"]
csv_row = ",".join(row1)
print(f"Row data: {row1}")
print(f"CSV: {csv_row}")

# Multiple rows
rows = [
    ["Name", "Age", "Title"],
    ["Alice", "30", "Engineer"],
    ["Bob", "25", "Designer"],
    ["Charlie", "35", "Manager"]
]

print("\\nFull CSV:")
csv_content = "\\n".join(",".join(row) for row in rows)
print(csv_content)

# With proper quoting (simplified)
print("\\nWith quotes:")
quoted_csv = "\\n".join(",".join(f'"{cell}"' for cell in row) for row in rows)
print(quoted_csv)
print()

# Example 7: join() vs + Concatenation Performance
print("="*70)
print("Example 7: Performance - join() vs + Operator")
print("="*70)

import time

# Small number of strings
words = ["word"] * 100

# Using + operator
start = time.perf_counter()
result = ""
for word in words:
    result = result + word + " "
plus_time = time.perf_counter() - start

# Using join
start = time.perf_counter()
result = " ".join(words)
join_time = time.perf_counter() - start

print(f"Combining {len(words)} strings:")
print(f"  + operator: {plus_time*1000:.4f}ms")
print(f"  join(): {join_time*1000:.4f}ms")
print(f"  join() is {plus_time/join_time:.1f}x faster!")
print()

# Example 8: join() with Comprehensions
print("="*70)
print("Example 8: join() with List Comprehensions and Filters")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")

# Even numbers as comma-separated string
evens = ", ".join(str(n) for n in numbers if n % 2 == 0)
print(f"Even numbers: {evens}")

# Squares
squares = " | ".join(f"{n}²={n**2}" for n in numbers if n <= 5)
print(f"Squares: {squares}")

# Formatted currency
prices = [19.99, 29.99, 9.99]
price_list = ", ".join(f"${price:.2f}" for price in prices)
print(f"\\nPrices: {price_list}")
print()

# Example 9: join() for Sentence Building
print("="*70)
print("Example 9: Building Natural Language Sentences")
print("="*70)

names = ["Alice", "Bob", "Charlie"]

# Simple list
simple = ", ".join(names)
print(f"Simple: {simple}")

# Oxford comma (last with 'and')
if len(names) > 1:
    oxford = ", ".join(names[:-1]) + ", and " + names[-1]
    print(f"Oxford comma: {oxford}")

# Different for 2 items
if len(names) == 2:
    two_items = " and ".join(names)
    print(f"Two items: {two_items}")

# Generic function
def format_list(items):
    """Format list with proper grammar"""
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return f"{', '.join(items[:-1])}, and {items[-1]}"

print(f"\\nFormatted:")
print(f"  1 item: {format_list(['Alice'])}")
print(f"  2 items: {format_list(['Alice', 'Bob'])}")
print(f"  3 items: {format_list(names)}")
print()

# Example 10: Practical Application - SQL Query Building
print("="*70)
print("Example 10: Real-World Use Case - Building SQL Queries")
print("="*70)

# SELECT clause
columns = ["id", "name", "email", "created_at"]
select_clause = ", ".join(columns)
print(f"Columns: {columns}")
print(f"SELECT {select_clause}")

# WHERE clause with multiple conditions
conditions = [
    "status = 'active'",
    "age >= 18",
    "country = 'USA'"
]
where_clause = " AND ".join(conditions)
print(f"\\nWHERE {where_clause}")

# Full query
table = "users"
query = f"SELECT {select_clause} FROM {table} WHERE {where_clause}"
print(f"\\nFull query:")
print(query)

# INSERT query
values = ["'John Doe'", "'john@example.com'", "25"]
insert_query = f"INSERT INTO {table} ({', '.join(columns[:3])}) VALUES ({', '.join(values)})"
print(f"\\nInsert query:")
print(insert_query)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. 'separator'.join(iterable) - Combine strings efficiently")
print("2. join() is MUCH faster than repeated + concatenation")
print("3. Works with lists, tuples, sets, generators, strings")
print("4. All elements must be strings (use str() if needed)")
print("5. Empty strings are included in result")
print("6. '\\\\n'.join() - Create multi-line strings")
print("7. ''.join() - Concatenate with no separator")
print("8. Common separators: ' ', ', ', '\\\\n', '/', '-'")
print("9. Combine with comprehensions for filtering/transforming")
print("10. Use join() for building: CSV, SQL, paths, sentences")
print("="*70)
'''

# Upgrade Lesson 74: String Length and Indexing
lesson74['fullSolution'] = '''"""
String Length and Indexing

Master string length calculation and character access in Python—from basic
len() and indexing to slicing, negative indices, and bounds checking.
Essential for string manipulation, parsing, and validation.

**Zero Package Installation Required**
"""

# Example 1: len() Function - String Length
print("="*70)
print("Example 1: Getting String Length with len()")
print("="*70)

text = "Python"
print(f"String: '{text}'")
print(f"Length: {len(text)}")

empty = ""
print(f"\\nEmpty string: '{empty}'")
print(f"Length: {len(empty)}")

long_text = "Python programming is fun and powerful"
print(f"\\nLonger text: '{long_text}'")
print(f"Length: {len(long_text)}")

# With special characters
special = "Hello\\nWorld\\t!"
print(f"\\nWith escapes: {repr(special)}")
print(f"Length: {len(special)}")  # Counts actual characters
print()

# Example 2: Basic Indexing - Accessing Characters
print("="*70)
print("Example 2: Accessing Characters by Index")
print("="*70)

text = "Python"
print(f"String: '{text}'")
print(f"Length: {len(text)}")

print("\\nPositive indices (0-based):")
for i in range(len(text)):
    print(f"  Index {i}: '{text[i]}'")

# First and last
print(f"\\nFirst character (index 0): '{text[0]}'")
print(f"Last character (index {len(text)-1}): '{text[len(text)-1]}'")
print()

# Example 3: Negative Indexing - Count from End
print("="*70)
print("Example 3: Negative Indices (Count from Right)")
print("="*70)

text = "Python"
print(f"String: '{text}'")

print("\\nNegative indices:")
print(f"  text[-1]: '{text[-1]}'  (last character)")
print(f"  text[-2]: '{text[-2]}'  (second to last)")
print(f"  text[-3]: '{text[-3]}'")
print(f"  text[-6]: '{text[-6]}'  (first character)")

# Equivalence
print(f"\\ntext[0] == text[-6]: {text[0] == text[-6]}")
print(f"text[5] == text[-1]: {text[5] == text[-1]}")
print()

# Example 4: Index Out of Range Errors
print("="*70)
print("Example 4: Handling Index Out of Range")
print("="*70)

text = "Hello"
print(f"String: '{text}' (length {len(text)})")

try:
    char = text[10]
    print(f"Character at index 10: '{char}'")
except IndexError as e:
    print(f"\\nError accessing index 10: {e}")

try:
    char = text[-10]
    print(f"Character at index -10: '{char}'")
except IndexError as e:
    print(f"Error accessing index -10: {e}")

# Safe access
index = 10
if index < len(text):
    print(f"\\nCharacter at {index}: '{text[index]}'")
else:
    print(f"\\nIndex {index} is out of range (length is {len(text)})")
print()

# Example 5: Slicing - Extract Substrings
print("="*70)
print("Example 5: String Slicing - Extract Substrings")
print("="*70)

text = "Python Programming"
print(f"String: '{text}'")

# Basic slicing [start:end]
print(f"\\ntext[0:6]: '{text[0:6]}'")
print(f"text[7:18]: '{text[7:18]}'")

# Omit start or end
print(f"\\ntext[:6]: '{text[:6]}'  (from beginning)")
print(f"text[7:]: '{text[7:]}'  (to end)")

# Get everything
print(f"text[:]: '{text[:]}'  (full copy)")
print()

# Example 6: Slicing with Negative Indices
print("="*70)
print("Example 6: Slicing with Negative Indices")
print("="*70)

text = "Python Programming"
print(f"String: '{text}'")

# Last N characters
last_5 = text[-5:]
print(f"\\nLast 5 characters: '{last_5}'")

# All but last N
all_but_last_3 = text[:-3]
print(f"All but last 3: '{all_but_last_3}'")

# Middle section
middle = text[-11:-4]
print(f"text[-11:-4]: '{middle}'")
print()

# Example 7: Slicing with Step
print("="*70)
print("Example 7: Slicing with Step Parameter")
print("="*70)

text = "0123456789"
print(f"String: '{text}'")

# Every 2nd character
every_2nd = text[::2]
print(f"\\nEvery 2nd char (::2): '{every_2nd}'")

# Every 3rd character
every_3rd = text[::3]
print(f"Every 3rd char (::3): '{every_3rd}'")

# Reverse string
reversed_text = text[::-1]
print(f"Reversed (::-1): '{reversed_text}'")

# Skip first 2, every 2nd
partial = text[2::2]
print(f"From index 2, every 2nd: '{partial}'")
print()

# Example 8: Iterating Over String with Index
print("="*70)
print("Example 8: Iterating with Enumerate")
print("="*70)

text = "Python"
print(f"String: '{text}'")

print("\\nUsing enumerate:")
for index, char in enumerate(text):
    print(f"  Index {index}: '{char}'")

# Start index from different value
print("\\nWith start=1:")
for index, char in enumerate(text, start=1):
    print(f"  Position {index}: '{char}'")
print()

# Example 9: Finding Character Positions
print("="*70)
print("Example 9: Finding Positions of Specific Characters")
print("="*70)

text = "Hello World"
search_char = "o"

print(f"String: '{text}'")
print(f"Finding all positions of '{search_char}':")

positions = []
for i, char in enumerate(text):
    if char == search_char:
        positions.append(i)
        print(f"  Found at index {i}")

print(f"All positions: {positions}")

# Using list comprehension
positions_lc = [i for i, char in enumerate(text) if char == search_char]
print(f"Using list comp: {positions_lc}")
print()

# Example 10: Practical Application - Password Validation
print("="*70)
print("Example 10: Real-World Use Case - Password Strength Check")
print("="*70)

passwords = [
    "abc123",
    "MyP@ssw0rd",
    "short",
    "VeryLongPasswordWith123Numbers!",
    "NoNumbersOrSpecial"
]

print("Password validation (8+ chars, has digit, has special):")
print()

for password in passwords:
    length = len(password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    # Check criteria
    length_ok = length >= 8

    is_strong = length_ok and has_digit and has_special

    print(f"Password: '{password}'")
    print(f"  Length: {length} {'✓' if length_ok else '✗'}")
    print(f"  Has digit: {'✓' if has_digit else '✗'}")
    print(f"  Has special char: {'✓' if has_special else '✗'}")
    print(f"  Result: {'STRONG' if is_strong else 'WEAK'}")
    print()

print("="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. len(string) - Returns number of characters")
print("2. string[i] - Access character at index i (0-based)")
print("3. string[-i] - Access from end (-1 is last)")
print("4. string[start:end] - Slice from start to end-1")
print("5. string[start:] - From start to end")
print("6. string[:end] - From beginning to end-1")
print("7. string[::step] - Slice with step (::2 every 2nd)")
print("8. string[::-1] - Reverse string")
print("9. IndexError raised if index out of range")
print("10. Slicing never raises error (returns empty string)")
print("="*70)
'''

# Upgrade Lesson 75: String Manipulation Mastery
lesson75['fullSolution'] = '''"""
String Manipulation Mastery: Common Patterns

Master advanced string manipulation patterns in Python—combining multiple
techniques for real-world scenarios like parsing, formatting, validation,
and transformation. Essential for professional string processing.

**Zero Package Installation Required**
"""

# Example 1: Extract and Format Names
print("="*70)
print("Example 1: Name Parsing and Formatting")
print("="*70)

full_names = [
    "john doe",
    "ALICE SMITH",
    "Bob_Jones",
    "charlie-brown"
]

print("Original names:")
for name in full_names:
    print(f"  '{name}'")

print("\\nFormatted names:")
for name in full_names:
    # Clean: replace separators, title case
    cleaned = name.replace("_", " ").replace("-", " ").title()
    print(f"  '{name}' → '{cleaned}'")

# Extract first and last name
example = "Alice Marie Smith"
parts = example.split()
first_name = parts[0]
last_name = parts[-1]
middle = " ".join(parts[1:-1]) if len(parts) > 2 else ""

print(f"\\nFrom '{example}':")
print(f"  First: {first_name}")
print(f"  Middle: {middle or '(none)'}")
print(f"  Last: {last_name}")
print()

# Example 2: URL Parsing and Construction
print("="*70)
print("Example 2: URL Manipulation")
print("="*70)

url = "https://api.example.com/v1/users/123?active=true&limit=10"
print(f"URL: {url}")

# Extract protocol
if "://" in url:
    protocol, rest = url.split("://", 1)
    print(f"Protocol: {protocol}")

    # Extract domain and path
    if "/" in rest:
        domain = rest.split("/")[0]
        path = "/" + "/".join(rest.split("/")[1:])

        # Separate query string
        if "?" in path:
            path_only, query = path.split("?", 1)
            print(f"Domain: {domain}")
            print(f"Path: {path_only}")
            print(f"Query: {query}")

            # Parse query parameters
            params = {}
            for param in query.split("&"):
                if "=" in param:
                    key, value = param.split("=", 1)
                    params[key] = value

            print(f"Parameters: {params}")

# Build URL
base = "https://api.example.com"
endpoint = "users"
user_id = 456
query_params = {"status": "active", "sort": "name"}

query_string = "&".join(f"{k}={v}" for k, v in query_params.items())
full_url = f"{base}/{endpoint}/{user_id}?{query_string}"
print(f"\\nBuilt URL: {full_url}")
print()

# Example 3: Phone Number Formatting
print("="*70)
print("Example 3: Phone Number Normalization")
print("="*70)

phone_numbers = [
    "1234567890",
    "(123) 456-7890",
    "123-456-7890",
    "+1 123 456 7890",
    "123.456.7890"
]

print("Normalizing phone numbers:")
for phone in phone_numbers:
    # Remove all non-digits
    digits_only = "".join(char for char in phone if char.isdigit())

    # Format as (XXX) XXX-XXXX
    if len(digits_only) == 10:
        formatted = f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    elif len(digits_only) == 11 and digits_only[0] == "1":
        formatted = f"+1 ({digits_only[1:4]}) {digits_only[4:7]}-{digits_only[7:]}"
    else:
        formatted = "Invalid"

    print(f"  '{phone}' → '{formatted}'")
print()

# Example 4: Email Validation and Parsing
print("="*70)
print("Example 4: Email Address Manipulation")
print("="*70)

emails = [
    "user@example.com",
    "First.Last@Company.ORG",
    "invalid.email",
    "test+tag@domain.co.uk"
]

print("Email analysis:")
for email in emails:
    email_lower = email.lower()

    # Basic validation
    has_at = "@" in email_lower
    at_position = email_lower.find("@")

    if has_at and at_position > 0:
        username = email_lower[:at_position]
        domain = email_lower[at_position + 1:]
        has_dot_in_domain = "." in domain

        # Remove tags (everything after +)
        if "+" in username:
            clean_username = username[:username.find("+")]
        else:
            clean_username = username

        clean_email = f"{clean_username}@{domain}"

        is_valid = has_dot_in_domain and not domain.startswith(".")

        print(f"\\n  '{email}'")
        print(f"    Username: {username}")
        print(f"    Domain: {domain}")
        print(f"    Clean: {clean_email}")
        print(f"    Valid: {'Yes' if is_valid else 'No'}")
    else:
        print(f"\\n  '{email}' - INVALID FORMAT")
print()

# Example 5: Text Truncation with Ellipsis
print("="*70)
print("Example 5: Smart Text Truncation")
print("="*70)

def truncate(text, max_length, suffix="..."):
    """Truncate text to max_length, adding suffix if truncated"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

long_text = "This is a very long piece of text that needs to be truncated"
print(f"Original ({len(long_text)} chars): '{long_text}'")

for length in [20, 30, 50, 100]:
    truncated = truncate(long_text, length)
    print(f"Max {length:3}: '{truncated}'")

# Word-aware truncation
def truncate_words(text, max_length, suffix="..."):
    """Truncate at word boundary"""
    if len(text) <= max_length:
        return text

    # Truncate and find last space
    truncated = text[:max_length - len(suffix)]
    last_space = truncated.rfind(" ")

    if last_space > 0:
        truncated = truncated[:last_space]

    return truncated + suffix

print(f"\\nWord-aware truncation:")
word_truncated = truncate_words(long_text, 30)
print(f"  '{word_truncated}'")
print()

# Example 6: Case-Insensitive String Comparison
print("="*70)
print("Example 6: Case-Insensitive Operations")
print("="*70)

def contains_ignore_case(text, search):
    """Check if text contains search (case-insensitive)"""
    return search.lower() in text.lower()

text = "Python Programming is FUN"
searches = ["python", "PROGRAMMING", "fun", "java"]

print(f"Text: '{text}'")
print("\\nCase-insensitive search:")
for search in searches:
    found = contains_ignore_case(text, search)
    print(f"  '{search}': {'Found' if found else 'Not found'}")

# Case-insensitive replace
def replace_ignore_case(text, old, new):
    """Replace all occurrences (case-insensitive)"""
    result = text
    old_lower = old.lower()

    # Find all positions
    i = 0
    while i < len(result):
        pos = result.lower().find(old_lower, i)
        if pos == -1:
            break
        result = result[:pos] + new + result[pos + len(old):]
        i = pos + len(new)

    return result

replaced = replace_ignore_case(text, "python", "Java")
print(f"\\nReplace 'python' with 'Java': '{replaced}'")
print()

# Example 7: Extracting Numbers from Text
print("="*70)
print("Example 7: Extract Numbers from Strings")
print("="*70)

texts = [
    "The price is $19.99",
    "Room 304, Building 12",
    "Call me at 555-1234",
    "Version 3.14.159"
]

print("Extracting numbers:")
for text in texts:
    # Extract all numeric characters and periods
    numbers = []
    current = ""

    for char in text:
        if char.isdigit() or char == ".":
            current += char
        else:
            if current:
                numbers.append(current)
                current = ""

    if current:
        numbers.append(current)

    print(f"  '{text}'")
    print(f"    Numbers: {numbers}")
print()

# Example 8: Title Case with Exceptions
print("="*70)
print("Example 8: Smart Title Case (Preserve Small Words)")
print("="*70)

def smart_title(text):
    """Title case but keep small words lowercase"""
    small_words = {"a", "an", "the", "and", "but", "or", "for", "nor", "on", "at", "to", "by", "in", "of"}

    words = text.lower().split()
    result = []

    for i, word in enumerate(words):
        # Always capitalize first and last word
        if i == 0 or i == len(words) - 1 or word not in small_words:
            result.append(word.capitalize())
        else:
            result.append(word)

    return " ".join(result)

titles = [
    "the lord of the rings",
    "a tale of two cities",
    "the old man and the sea"
]

print("Smart title casing:")
for title in titles:
    formatted = smart_title(title)
    print(f"  '{title}'")
    print(f"  → '{formatted}'")
print()

# Example 9: Remove Extra Whitespace
print("="*70)
print("Example 9: Normalize Whitespace")
print("="*70)

messy_texts = [
    "  extra   spaces    everywhere  ",
    "tabs\\t\\tand\\tnewlines\\n\\n",
    "  multiple   types   of   whitespace  "
]

print("Cleaning whitespace:")
for text in messy_texts:
    # Split on any whitespace and rejoin with single space
    cleaned = " ".join(text.split())

    print(f"  Original: {repr(text)}")
    print(f"  Cleaned:  '{cleaned}'")
    print()

# Example 10: Building Formatted Reports
print("="*70)
print("Example 10: Real-World Use Case - Formatted Report")
print("="*70)

sales_data = [
    {"product": "Laptop", "quantity": 5, "price": 999.99},
    {"product": "Mouse", "quantity": 25, "price": 29.99},
    {"product": "Keyboard", "quantity": 15, "price": 79.99},
    {"product": "Monitor", "quantity": 8, "price": 299.99}
]

# Build report
report_lines = []
report_lines.append("="*60)
report_lines.append("SALES REPORT".center(60))
report_lines.append("="*60)

# Header
header = f"{'Product':<20} {'Qty':>8} {'Price':>12} {'Total':>12}"
report_lines.append(header)
report_lines.append("-"*60)

# Data rows
grand_total = 0
for item in sales_data:
    total = item['quantity'] * item['price']
    grand_total += total

    row = f"{item['product']:<20} {item['quantity']:>8} ${item['price']:>11.2f} ${total:>11.2f}"
    report_lines.append(row)

# Footer
report_lines.append("-"*60)
report_lines.append(f"{'GRAND TOTAL':<20} {'':<8} {'':<12} ${grand_total:>11.2f}")
report_lines.append("="*60)

# Join and print
report = "\\n".join(report_lines)
print(report)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Combine multiple string methods for complex tasks")
print("2. split() + join() pattern for cleaning/formatting")
print("3. Use .lower() or .upper() for case-insensitive operations")
print("4. ''.join(char for char in text if condition) for filtering")
print("5. String slicing [start:end] for extracting parts")
print("6. f-strings for clean formatting and templates")
print("7. str.split(delimiter, maxsplit) for controlled parsing")
print("8. Always validate input before processing")
print("9. Consider edge cases (empty strings, None, special chars)")
print("10. Build complex strings with lists + join() for performance")
print("="*70)
'''

# Save the updated lessons
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Print summary
print("\nUpgraded lessons 71-75:")
print(f"  71: String Find and Index - {len(lesson71['fullSolution'])} chars")
print(f"  72: String Helper Functions - {len(lesson72['fullSolution'])} chars")
print(f"  73: String Join - {len(lesson73['fullSolution'])} chars")
print(f"  74: String Length and Indexing - {len(lesson74['fullSolution'])} chars")
print(f"  75: String Manipulation Mastery: Common Patterns - {len(lesson75['fullSolution'])} chars")
print("\nBatch 71-75 complete!")
