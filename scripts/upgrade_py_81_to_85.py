#!/usr/bin/env python3
"""
Upgrade Python lessons 81-85 with comprehensive content.
- Lesson 81: String Reverse
- Lesson 82: String Slicing
- Lesson 83: String Split and Join
- Lesson 84: String Validation
- Lesson 85: String padding
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 81-85
lesson81 = next(l for l in lessons if l['id'] == 81)
lesson82 = next(l for l in lessons if l['id'] == 82)
lesson83 = next(l for l in lessons if l['id'] == 83)
lesson84 = next(l for l in lessons if l['id'] == 84)
lesson85 = next(l for l in lessons if l['id'] == 85)

# Upgrade Lesson 81: String Reverse
lesson81['fullSolution'] = '''"""
String Reverse

Master all techniques for reversing strings in Python—from simple slicing
to manual algorithms, recursive approaches, and performance comparisons.
Essential for algorithms, palindromes, and string manipulation.

**Zero Package Installation Required**
"""

# Example 1: Reverse with Slicing [::-1]
print("="*70)
print("Example 1: Reverse String with Slicing [::-1]")
print("="*70)

text = "Python"
print(f"Original: '{text}'")

reversed_text = text[::-1]
print(f"Reversed: '{reversed_text}'")

# Works with any string
examples = ["Hello", "12345", "racecar"]
print("\\nMore examples:")
for ex in examples:
    print(f"  '{ex}' → '{ex[::-1]}'")
print()

# Example 2: Reverse with reversed() Function
print("="*70)
print("Example 2: reversed() Function + join()")
print("="*70)

text = "Hello World"
print(f"Original: '{text}'")

# reversed() returns an iterator
rev_iterator = reversed(text)
print(f"reversed() returns: {rev_iterator}")
print(f"Type: {type(rev_iterator)}")

# Convert to string with join
reversed_text = "".join(reversed(text))
print(f"Joined result: '{reversed_text}'")

# Can also convert to list first
rev_list = list(reversed(text))
print(f"As list: {rev_list}")
print()

# Example 3: Manual Reversal with Loop
print("="*70)
print("Example 3: Manual Reversal Algorithm")
print("="*70)

text = "Python"
print(f"Original: '{text}'")

# Build reversed string character by character
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text  # Prepend each character
    print(f"  After '{char}': '{reversed_text}'")

print(f"Final result: '{reversed_text}'")
print()

# Example 4: Reverse with List and join
print("="*70)
print("Example 4: Convert to List, Reverse, Join")
print("="*70)

text = "Hello"
print(f"Original: '{text}'")

# Convert to list
char_list = list(text)
print(f"As list: {char_list}")

# Reverse the list
char_list.reverse()
print(f"Reversed list: {char_list}")

# Join back to string
reversed_text = "".join(char_list)
print(f"Joined: '{reversed_text}'")
print()

# Example 5: Recursive Reversal
print("="*70)
print("Example 5: Recursive String Reversal")
print("="*70)

def reverse_recursive(text):
    """Reverse string using recursion"""
    # Base case
    if len(text) <= 1:
        return text

    # Recursive case: last char + reverse of rest
    return text[-1] + reverse_recursive(text[:-1])

text = "Python"
print(f"Original: '{text}'")

reversed_text = reverse_recursive(text)
print(f"Recursively reversed: '{reversed_text}'")

# Show recursion steps
print("\\nRecursion steps:")
print("  reverse_recursive('Python')")
print("  = 'n' + reverse_recursive('Pytho')")
print("  = 'n' + 'o' + reverse_recursive('Pyth')")
print("  = 'n' + 'o' + 'h' + reverse_recursive('Pyt')")
print("  = 'n' + 'o' + 'h' + 't' + reverse_recursive('Py')")
print("  = 'n' + 'o' + 'h' + 't' + 'y' + reverse_recursive('P')")
print("  = 'n' + 'o' + 'h' + 't' + 'y' + 'P'")
print("  = 'nohtyP'")
print()

# Example 6: Reverse Words in Sentence
print("="*70)
print("Example 6: Reverse Words vs Reverse Characters")
print("="*70)

sentence = "Hello World Python"
print(f"Original: '{sentence}'")

# Reverse entire string
fully_reversed = sentence[::-1]
print(f"Fully reversed: '{fully_reversed}'")

# Reverse word order only
words = sentence.split()
words.reverse()
words_reversed = " ".join(words)
print(f"Words reversed: '{words_reversed}'")

# Reverse each word individually
each_word_reversed = " ".join(word[::-1] for word in sentence.split())
print(f"Each word reversed: '{each_word_reversed}'")
print()

# Example 7: Reverse Substrings
print("="*70)
print("Example 7: Reverse Specific Portions")
print("="*70)

text = "Hello World"
print(f"Original: '{text}'")

# Reverse first 5 characters only
first_5_reversed = text[:5][::-1] + text[5:]
print(f"First 5 reversed: '{first_5_reversed}'")

# Reverse last 5 characters only
last_5_reversed = text[:-5] + text[-5:][::-1]
print(f"Last 5 reversed: '{last_5_reversed}'")

# Reverse middle portion
middle_reversed = text[:3] + text[3:8][::-1] + text[8:]
print(f"Middle (3-8) reversed: '{middle_reversed}'")
print()

# Example 8: Performance Comparison
print("="*70)
print("Example 8: Performance of Different Approaches")
print("="*70)

import time

test_string = "x" * 10000  # 10,000 character string

# Method 1: Slicing
start = time.perf_counter()
result = test_string[::-1]
slicing_time = time.perf_counter() - start

# Method 2: reversed() + join()
start = time.perf_counter()
result = "".join(reversed(test_string))
reversed_time = time.perf_counter() - start

# Method 3: Manual with list
start = time.perf_counter()
char_list = list(test_string)
char_list.reverse()
result = "".join(char_list)
manual_time = time.perf_counter() - start

print(f"String length: {len(test_string):,} characters")
print(f"\\nPerformance results:")
print(f"  [::-1] slicing: {slicing_time*1000:.4f}ms")
print(f"  reversed() + join(): {reversed_time*1000:.4f}ms")
print(f"  list.reverse() + join(): {manual_time*1000:.4f}ms")
print(f"\\nFastest: [::-1] slicing")
print()

# Example 9: Reverse with Special Characters
print("="*70)
print("Example 9: Reversing Strings with Special Characters")
print("="*70)

special_strings = [
    "Hello\\nWorld",
    "Price: $19.99",
    "Email: user@example.com",
    "Path: C:\\\\Users\\\\Alice"
]

print("Reversing special character strings:")
for s in special_strings:
    reversed_s = s[::-1]
    print(f"  Original: {s!r}")
    print(f"  Reversed: {reversed_s!r}")
    print()

# Example 10: Practical Application - Encryption Simulation
print("="*70)
print("Example 10: Real-World Use Case - Simple Cipher")
print("="*70)

def simple_encrypt(message):
    """Simple encryption: reverse string + shift characters"""
    # Step 1: Reverse the string
    reversed_msg = message[::-1]

    # Step 2: Shift each character by 1
    encrypted = ""
    for char in reversed_msg:
        if char.isalpha():
            # Shift letter by 1
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        else:
            encrypted += char

    return encrypted

def simple_decrypt(encrypted):
    """Decrypt by reversing the encryption process"""
    # Step 1: Shift back
    shifted_back = ""
    for char in encrypted:
        if char.isalpha():
            if char.islower():
                shifted_back += chr((ord(char) - ord('a') - 1) % 26 + ord('a'))
            else:
                shifted_back += chr((ord(char) - ord('A') - 1) % 26 + ord('A'))
        else:
            shifted_back += char

    # Step 2: Reverse back
    original = shifted_back[::-1]
    return original

message = "Hello World"
print(f"Original message: '{message}'")

encrypted = simple_encrypt(message)
print(f"Encrypted: '{encrypted}'")

decrypted = simple_decrypt(encrypted)
print(f"Decrypted: '{decrypted}'")

# Verify
print(f"\\nMatch: {message == decrypted}")

# Test with more messages
messages = ["Python", "Secret Message", "12345"]
print("\\nMore examples:")
for msg in messages:
    enc = simple_encrypt(msg)
    dec = simple_decrypt(enc)
    print(f"  '{msg}' → '{enc}' → '{dec}'")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. [::-1] - Fastest and most Pythonic method")
print("2. ''.join(reversed(s)) - Using reversed() iterator")
print("3. Manual loop - char + result for learning")
print("4. list.reverse() + join() - List manipulation approach")
print("5. Recursive - For educational purposes")
print("6. Can reverse entire string or portions")
print("7. Reverse words: ' '.join(s.split()[::-1])")
print("8. Reverse each word: ' '.join(w[::-1] for w in s.split())")
print("9. [::-1] has O(n) time and space complexity")
print("10. Essential for palindromes, algorithms, ciphers")
print("="*70)
'''

# Upgrade Lesson 82: String Slicing
lesson82['fullSolution'] = '''"""
String Slicing

Master Python string slicing—extract substrings, use negative indices,
step parameters, and advanced patterns. Essential for text parsing,
data extraction, and string manipulation.

**Zero Package Installation Required**
"""

# Example 1: Basic Slicing [start:end]
print("="*70)
print("Example 1: Basic String Slicing Syntax")
print("="*70)

text = "Python Programming"
print(f"String: '{text}'")
print(f"Length: {len(text)}")
print(f"Indices: 0-{len(text)-1}")

# Extract substring
first_6 = text[0:6]
print(f"\\ntext[0:6]: '{first_6}'")

# Extract different portion
programming = text[7:18]
print(f"text[7:18]: '{programming}'")

# Note: end index is exclusive
print(f"\\ntext[0:1]: '{text[0:1]}'  (only index 0)")
print(f"text[0:2]: '{text[0:2]}'  (indices 0,1)")
print()

# Example 2: Omitting Start or End
print("="*70)
print("Example 2: Slicing from Beginning or to End")
print("="*70)

text = "Hello World"
print(f"String: '{text}'")

# From beginning
first_5 = text[:5]
print(f"\\ntext[:5]: '{first_5}'  (equivalent to text[0:5])")

# To end
last_5 = text[6:]
print(f"text[6:]: '{last_5}'  (from index 6 to end)")

# Full copy
full_copy = text[:]
print(f"text[:]: '{full_copy}'  (full copy)")
print(f"Is copy: {full_copy is not text}")  # Different object
print()

# Example 3: Negative Indices
print("="*70)
print("Example 3: Slicing with Negative Indices")
print("="*70)

text = "Python"
print(f"String: '{text}'")
print(f"Positive indices: 0   1   2   3   4   5")
print(f"                  P   y   t   h   o   n")
print(f"Negative indices: -6 -5 -4 -3 -2 -1")

# Last N characters
print(f"\\ntext[-3:]: '{text[-3:]}'  (last 3 characters)")
print(f"text[-1:]: '{text[-1:]}'  (last character)")

# All but last N
print(f"\\ntext[:-2]: '{text[:-2]}'  (all but last 2)")
print(f"text[:-1]: '{text[:-1]}'  (all but last)")

# Negative start and end
print(f"\\ntext[-4:-1]: '{text[-4:-1]}'  (from -4 to -1)")
print()

# Example 4: Step Parameter [start:end:step]
print("="*70)
print("Example 4: Slicing with Step Parameter")
print("="*70)

text = "0123456789"
print(f"String: '{text}'")

# Every 2nd character
every_2nd = text[::2]
print(f"\\ntext[::2]: '{every_2nd}'  (every 2nd char)")

# Every 3rd character
every_3rd = text[::3]
print(f"text[::3]: '{every_3rd}'  (every 3rd char)")

# From index 1, every 2nd
from_1_every_2nd = text[1::2]
print(f"text[1::2]: '{from_1_every_2nd}'  (from 1, every 2nd)")

# Range with step
range_with_step = text[2:8:2]
print(f"text[2:8:2]: '{range_with_step}'  (2 to 8, every 2nd)")
print()

# Example 5: Reverse with Negative Step
print("="*70)
print("Example 5: Reversing with Negative Step")
print("="*70)

text = "Python"
print(f"String: '{text}'")

# Reverse entire string
reversed_text = text[::-1]
print(f"\\ntext[::-1]: '{reversed_text}'  (reverse)")

# Every 2nd character in reverse
every_2nd_reverse = text[::-2]
print(f"text[::-2]: '{every_2nd_reverse}'  (every 2nd, reversed)")

# Specific range reversed
partial_reverse = text[5:2:-1]
print(f"text[5:2:-1]: '{partial_reverse}'  (from 5 down to 3)")
print()

# Example 6: Out of Bounds Slicing
print("="*70)
print("Example 6: Slicing Never Raises IndexError")
print("="*70)

text = "Hello"
print(f"String: '{text}' (length {len(text)})")

# Beyond string length - returns what's available
beyond = text[2:100]
print(f"\\ntext[2:100]: '{beyond}'  (no error, returns till end)")

before_start = text[-100:3]
print(f"text[-100:3]: '{before_start}'  (returns from start)")

way_beyond = text[100:200]
print(f"text[100:200]: '{way_beyond}'  (empty string)")

# Contrast with indexing
print("\\nIndexing DOES raise error:")
try:
    char = text[100]
    print(f"text[100]: '{char}'")
except IndexError as e:
    print(f"text[100]: IndexError - {e}")
print()

# Example 7: Extracting File Extensions
print("="*70)
print("Example 7: Practical Slicing - File Extensions")
print("="*70)

filenames = [
    "document.pdf",
    "script.py",
    "archive.tar.gz",
    "image.jpg"
]

print("Extracting file extensions:")
for filename in filenames:
    # Find last dot
    dot_pos = filename.rfind(".")

    if dot_pos != -1:
        extension = filename[dot_pos:]  # From dot to end
        basename = filename[:dot_pos]   # Before dot
        print(f"  '{filename}':")
        print(f"    Base: '{basename}'")
        print(f"    Extension: '{extension}'")
print()

# Example 8: Extracting Substrings from Patterns
print("="*70)
print("Example 8: Extract Data from Formatted Strings")
print("="*70)

# Phone number: (555) 123-4567
phone = "(555) 123-4567"
print(f"Phone: '{phone}'")

area_code = phone[1:4]  # Inside parentheses
prefix = phone[6:9]     # After space
line = phone[10:14]     # After dash

print(f"  Area code: '{area_code}'")
print(f"  Prefix: '{prefix}'")
print(f"  Line: '{line}'")

# Date: 2024-01-15
date = "2024-01-15"
print(f"\\nDate: '{date}'")

year = date[:4]
month = date[5:7]
day = date[8:10]

print(f"  Year: '{year}'")
print(f"  Month: '{month}'")
print(f"  Day: '{day}'")
print()

# Example 9: Slicing in Loops
print("="*70)
print("Example 9: Processing String in Chunks")
print("="*70)

text = "ABCDEFGHIJKLMNOP"
chunk_size = 4

print(f"String: '{text}'")
print(f"Chunk size: {chunk_size}")
print("\\nChunks:")

for i in range(0, len(text), chunk_size):
    chunk = text[i:i+chunk_size]
    print(f"  [{i}:{i+chunk_size}] → '{chunk}'")

# Process DNA sequence in codons (3 nucleotides)
dna = "ATGCGATACGTAGCTA"
print(f"\\nDNA: '{dna}'")
print("Codons (3-base chunks):")

for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    if len(codon) == 3:  # Only full codons
        print(f"  Codon {i//3 + 1}: '{codon}'")
print()

# Example 10: Practical Application - Credit Card Masking
print("="*70)
print("Example 10: Real-World Use Case - Mask Sensitive Data")
print("="*70)

def mask_credit_card(card_number):
    """Mask all but last 4 digits of credit card"""
    if len(card_number) < 4:
        return "*" * len(card_number)

    # Show only last 4 digits
    last_4 = card_number[-4:]
    masked_part = "*" * (len(card_number) - 4)

    return masked_part + last_4

def mask_email(email):
    """Mask email address, show first 2 chars and domain"""
    if "@" not in email:
        return email

    username, domain = email.split("@", 1)

    if len(username) <= 2:
        masked_username = username
    else:
        masked_username = username[:2] + "*" * (len(username) - 2)

    return f"{masked_username}@{domain}"

# Test credit card masking
cards = ["1234567890123456", "9876543210", "4532"]
print("Credit card masking:")
for card in cards:
    masked = mask_credit_card(card)
    print(f"  {card} → {masked}")

# Test email masking
emails = ["alice@example.com", "bob.smith@company.org", "c@test.com"]
print("\\nEmail masking:")
for email in emails:
    masked = mask_email(email)
    print(f"  {email} → {masked}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. string[start:end] - Extract from start to end-1")
print("2. string[:end] - From beginning to end-1")
print("3. string[start:] - From start to end of string")
print("4. string[:] - Full copy of string")
print("5. string[-n:] - Last n characters")
print("6. string[:-n] - All but last n characters")
print("7. string[start:end:step] - With step parameter")
print("8. string[::-1] - Reverse string")
print("9. Slicing never raises IndexError")
print("10. Essential for parsing, extraction, masking")
print("="*70)
'''

# Continue with lessons 83-85...
lesson83['fullSolution'] = '''"""
String Split and Join

Master split() for breaking strings into lists and join() for combining
lists into strings. Essential for parsing CSV data, processing text files,
and string transformation workflows.

**Zero Package Installation Required**
"""

# Example 1: Basic split() with Whitespace
print("="*70)
print("Example 1: split() - Default Whitespace Splitting")
print("="*70)

sentence = "Python is awesome"
print(f"Sentence: '{sentence}'")

words = sentence.split()  # Split on any whitespace
print(f"split(): {words}")
print(f"Type: {type(words)}")
print(f"Length: {len(words)}")

# Multiple spaces are handled
messy = "Hello    World   Python"
print(f"\\nMessy: '{messy}'")
print(f"split(): {messy.split()}")
print("Note: Multiple spaces treated as one separator")
print()

# Example 2: split() with Custom Delimiter
print("="*70)
print("Example 2: split() with Custom Delimiter")
print("="*70)

# CSV data
csv = "apple,banana,cherry,date"
print(f"CSV: '{csv}'")
fruits = csv.split(",")
print(f"split(','): {fruits}")

# Pipe-separated
data = "Alice|30|Engineer"
print(f"\\nPipe-separated: '{data}'")
fields = data.split("|")
print(f"split('|'): {fields}")

# Multiple character delimiter
text = "one::two::three::four"
print(f"\\nDouble colon: '{text}'")
parts = text.split("::")
print(f"split('::'): {parts}")
print()

# Example 3: split() with maxsplit Parameter
print("="*70)
print("Example 3: Limiting Splits with maxsplit")
print("="*70)

text = "one,two,three,four,five"
print(f"Text: '{text}'")

# Split all
all_parts = text.split(",")
print(f"split(','): {all_parts}")

# Split at most once
one_split = text.split(",", 1)
print(f"split(',', 1): {one_split}")

# Split at most twice
two_splits = text.split(",", 2)
print(f"split(',', 2): {two_splits}")

# Useful for parsing key-value pairs
config = "server=localhost:8080"
print(f"\\nConfig: '{config}'")
key, value = config.split("=", 1)
print(f"Key: '{key}', Value: '{value}'")
print()

# Example 4: rsplit() - Split from Right
print("="*70)
print("Example 4: rsplit() - Split from Right Side")
print("="*70)

path = "folder/subfolder/file.txt"
print(f"Path: '{path}'")

# split from right, once
parts = path.rsplit("/", 1)
print(f"rsplit('/', 1): {parts}")
print(f"  Directory: '{parts[0]}'")
print(f"  Filename: '{parts[1]}'")

# Compare with split
left_split = path.split("/", 1)
print(f"\\nsplit('/', 1): {left_split}")

# rsplit with larger maxsplit
parts = path.rsplit("/", 2)
print(f"rsplit('/', 2): {parts}")
print()

# Example 5: splitlines() - Split by Line Breaks
print("="*70)
print("Example 5: splitlines() - Handle Multiple Line Endings")
print("="*70)

multiline = "Line 1\\nLine 2\\nLine 3"
print(f"Text: {multiline!r}")

lines = multiline.splitlines()
print(f"splitlines(): {lines}")

# With different line endings
mixed = "Line 1\\nLine 2\\r\\nLine 3\\rLine 4"
print(f"\\nMixed endings: {mixed!r}")
print(f"splitlines(): {mixed.splitlines()}")

# Keep line endings
with_endings = multiline.splitlines(keepends=True)
print(f"\\nsplitlines(True): {with_endings}")
print()

# Example 6: Basic join() - Combine List to String
print("="*70)
print("Example 6: join() - Combine List into String")
print("="*70)

words = ["Python", "is", "awesome"]
print(f"Words: {words}")

# Join with space
sentence = " ".join(words)
print(f"' '.join(): '{sentence}'")

# Join with different separators
comma = ", ".join(words)
print(f"', '.join(): '{comma}'")

dash = "-".join(words)
print(f"'-'.join(): '{dash}'")

# Join with no separator
mashed = "".join(words)
print(f"''.join(): '{mashed}'")
print()

# Example 7: join() with Different Iterables
print("="*70)
print("Example 7: join() Works with Any Iterable")
print("="*70)

# From tuple
tuple_data = ("apple", "banana", "cherry")
result = ", ".join(tuple_data)
print(f"Tuple: {tuple_data}")
print(f"Joined: '{result}'")

# From generator
numbers = (str(n) for n in range(5))
result = "-".join(numbers)
print(f"\\nGenerator (0-4): '{result}'")

# From characters in string
chars = "HELLO"
result = " ".join(chars)
print(f"\\nString '{chars}': '{result}'")

# Must be strings (convert numbers)
numbers = [1, 2, 3, 4, 5]
result = ", ".join(str(n) for n in numbers)
print(f"\\nNumbers {numbers}: '{result}'")
print()

# Example 8: Split and Join Pipeline
print("="*70)
print("Example 8: split() + join() for Text Processing")
print("="*70)

# Normalize spacing
messy = "  Hello    World   Python  "
print(f"Messy: '{messy}'")

normalized = " ".join(messy.split())
print(f"Normalized: '{normalized}'")

# Replace delimiter
csv = "apple,banana,cherry"
print(f"\\nCSV: '{csv}'")
tsv = "\\t".join(csv.split(","))
print(f"TSV: {tsv!r}")

# Clean and reformat
data = "  Alice  ,  30  ,  Engineer  "
print(f"\\nMessy CSV: '{data}'")
cleaned = ", ".join(field.strip() for field in data.split(","))
print(f"Cleaned: '{cleaned}'")
print()

# Example 9: partition() - Split into 3 Parts
print("="*70)
print("Example 9: partition() - Split at First Occurrence")
print("="*70)

email = "user@example.com"
print(f"Email: '{email}'")

# partition returns tuple of (before, separator, after)
username, sep, domain = email.partition("@")
print(f"partition('@'):")
print(f"  Username: '{username}'")
print(f"  Separator: '{sep}'")
print(f"  Domain: '{domain}'")

# If separator not found, returns (string, '', '')
no_at = "no-at-sign"
print(f"\\n'{no_at}'.partition('@'): {no_at.partition('@')}")

# rpartition - partition from right
url = "https://example.com/path/file.txt"
print(f"\\nURL: '{url}'")
base, sep, filename = url.rpartition("/")
print(f"rpartition('/'):")
print(f"  Base: '{base}'")
print(f"  Filename: '{filename}'")
print()

# Example 10: Practical Application - CSV Processing
print("="*70)
print("Example 10: Real-World Use Case - Process CSV Data")
print("="*70)

csv_data = """Name,Age,Department,Salary
Alice,30,Engineering,85000
Bob,25,Design,65000
Charlie,35,Management,95000"""

print("Processing CSV data:")
print(csv_data)
print("\\n" + "="*60)

lines = csv_data.splitlines()

# Parse header
header = lines[0].split(",")
print(f"Columns: {header}")

# Parse data rows
employees = []
for line in lines[1:]:
    fields = line.split(",")
    employee = dict(zip(header, fields))
    employees.append(employee)

print("\\nParsed data:")
for emp in employees:
    print(f"  {emp}")

# Generate formatted report
print("\\n" + "="*60)
print("EMPLOYEE REPORT".center(60))
print("="*60)

for emp in employees:
    name = emp["Name"]
    age = emp["Age"]
    dept = emp["Department"]
    salary = emp["Salary"]

    print(f"{name:<15} Age: {age:<3} {dept:<15} ${salary:>8}")

# Convert back to CSV
print("\\nReconstructed CSV:")
output_lines = [",".join(header)]
for emp in employees:
    row = ",".join([emp[col] for col in header])
    output_lines.append(row)

csv_output = "\\n".join(output_lines)
print(csv_output)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. split() - Split on whitespace by default")
print("2. split(delimiter) - Split on specific separator")
print("3. split(delim, maxsplit) - Limit number of splits")
print("4. rsplit() - Split from right side")
print("5. splitlines() - Split on line breaks")
print("6. 'sep'.join(iterable) - Combine strings with separator")
print("7. partition(sep) - Split into 3 parts at first occurrence")
print("8. split() + join() - Common text processing pattern")
print("9. join() requires all elements to be strings")
print("10. Essential for CSV, logs, configuration files")
print("="*70)
'''

# Continue with lessons 84-85 in the same file...
lesson84['fullSolution'] = '''"""
String Validation

Master string validation methods in Python—isdigit(), isalpha(), isalnum(),
isspace(), and more. Essential for input validation, data cleaning, and
ensuring data integrity.

**Zero Package Installation Required**
"""

# Example 1: isdigit() - Check for Digits
print("="*70)
print("Example 1: isdigit() - Numeric String Validation")
print("="*70)

test_strings = ["12345", "123.45", "-100", "abc", "123abc", ""]

print(f"{'String':<15} {'isdigit()':<10} {'Notes'}")
print("-"*50)

for s in test_strings:
    result = s.isdigit()
    notes = ""
    if "." in s:
        notes = "decimals not allowed"
    elif "-" in s:
        notes = "negative sign not allowed"
    elif any(c.isalpha() for c in s):
        notes = "contains letters"

    print(f"{s!r:<15} {str(result):<10} {notes}")

# Practical use
age_input = "25"
if age_input.isdigit():
    age = int(age_input)
    print(f"\\nValid age: {age}")
print()

# Example 2: isalpha() - Check for Letters Only
print("="*70)
print("Example 2: isalpha() - Alphabetic Character Check")
print("="*70)

test_strings = ["Python", "Hello123", "Hello World", "café", "", "ABC"]

print(f"{'String':<15} {'isalpha()':<10} {'Notes'}")
print("-"*50)

for s in test_strings:
    result = s.isalpha()
    notes = ""
    if any(c.isdigit() for c in s):
        notes = "contains digits"
    elif " " in s:
        notes = "contains space"

    print(f"{s!r:<15} {str(result):<10} {notes}")

# Validate name
name = "Alice"
if name.isalpha():
    print(f"\\nValid name: {name}")
print()

# Example 3: isalnum() - Letters or Digits
print("="*70)
print("Example 3: isalnum() - Alphanumeric Check")
print("="*70)

test_strings = ["user123", "hello_world", "Python3", "test-case", "abc 123", "5050"]

print(f"{'String':<15} {'isalnum()':<10} {'Notes'}")
print("-"*50)

for s in test_strings:
    result = s.isalnum()
    notes = ""
    if "_" in s:
        notes = "underscore not allowed"
    elif "-" in s:
        notes = "hyphen not allowed"
    elif " " in s:
        notes = "space not allowed"

    print(f"{s!r:<15} {str(result):<10} {notes}")

# Username validation
username = "user123"
if username.isalnum():
    print(f"\\nValid username: {username}")
print()

# Example 4: isspace() - Whitespace Check
print("="*70)
print("Example 4: isspace() - Whitespace Validation")
print("="*70)

test_strings = ["   ", "\\t\\t", "\\n", "  a  ", "", "hello"]

print(f"{'String':<15} {'isspace()':<10} {'Notes'}")
print("-"*50)

for s in test_strings:
    result = s.isspace()
    notes = ""
    if result:
        notes = "only whitespace"
    elif s == "":
        notes = "empty string"
    else:
        notes = "contains non-whitespace"

    print(f"{s!r:<15} {str(result):<10} {notes}")

# Check if input is blank
user_input = "   "
if user_input.isspace() or not user_input:
    print("\\nInput is blank!")
print()

# Example 5: isupper() and islower() - Case Checks
print("="*70)
print("Example 5: Case Validation - isupper() and islower()")
print("="*70)

test_strings = ["HELLO", "hello", "Hello", "HELLO123", "123"]

print(f"{'String':<15} {'isupper()':<10} {'islower()':<10} {'Notes'}")
print("-"*60)

for s in test_strings:
    upper = s.isupper()
    lower = s.islower()
    notes = ""

    if not any(c.isalpha() for c in s):
        notes = "no letters"
    elif upper and lower:
        notes = "impossible"
    elif not upper and not lower:
        notes = "mixed case"

    print(f"{s!r:<15} {str(upper):<10} {str(lower):<10} {notes}")

# Check for all caps
text = "URGENT"
if text.isupper():
    print(f"\\n'{text}' is all uppercase (might be shouting!)")
print()

# Example 6: istitle() - Title Case Check
print("="*70)
print("Example 6: istitle() - Title Case Validation")
print("="*70)

test_strings = [
    "Hello World",
    "hello world",
    "Hello world",
    "HELLO WORLD",
    "Title Case Example",
    "3 Apples"
]

print(f"{'String':<25} {'istitle()':<10} {'Expected':<15}")
print("-"*50)

for s in test_strings:
    result = s.istitle()
    expected = "Title Case" if result else "Not Title Case"
    print(f"{s!r:<25} {str(result):<10} {expected:<15}")

# Validate book title
book_title = "The Great Gatsby"
if book_title.istitle():
    print(f"\\n'{book_title}' is properly formatted")
print()

# Example 7: startswith() and endswith()
print("="*70)
print("Example 7: Prefix and Suffix Validation")
print("="*70)

filenames = [
    "script.py",
    "data.json",
    "test.py",
    "README.md",
    "backup_data.json"
]

print("Python files (.py):")
python_files = [f for f in filenames if f.endswith(".py")]
for f in python_files:
    print(f"  {f}")

print("\\nFiles starting with 'test' or 'backup':")
special_files = [f for f in filenames
                 if f.startswith("test") or f.startswith("backup")]
for f in special_files:
    print(f"  {f}")

# URL validation
url = "https://example.com"
if url.startswith(("http://", "https://")):
    print(f"\\n'{url}' is a valid HTTP(S) URL")
print()

# Example 8: Custom Validation Functions
print("="*70)
print("Example 8: Building Custom Validators")
print("="*70)

def is_valid_email(email):
    """Basic email validation"""
    has_at = "@" in email
    has_dot = "." in email
    at_position = email.find("@")

    if not has_at:
        return False, "Missing @"

    if at_position == 0:
        return False, "@ cannot be at start"

    if at_position == len(email) - 1:
        return False, "@ cannot be at end"

    domain = email[at_position + 1:]
    if "." not in domain:
        return False, "Domain needs a dot"

    return True, "Valid"

def is_strong_password(password):
    """Password strength validation"""
    errors = []

    if len(password) < 8:
        errors.append("At least 8 characters required")

    if not any(c.isupper() for c in password):
        errors.append("Need at least one uppercase letter")

    if not any(c.islower() for c in password):
        errors.append("Need at least one lowercase letter")

    if not any(c.isdigit() for c in password):
        errors.append("Need at least one digit")

    if not any(not c.isalnum() for c in password):
        errors.append("Need at least one special character")

    if not errors:
        return True, "Strong password"

    return False, "; ".join(errors)

# Test email validation
emails = ["user@example.com", "invalid", "test@", "@domain.com"]
print("Email validation:")
for email in emails:
    valid, message = is_valid_email(email)
    status = "✓" if valid else "✗"
    print(f"  {status} {email:<25} {message}")

# Test password validation
passwords = ["weak", "StrongPass1!", "NoNumbers!", "alllowercase123!"]
print("\\nPassword validation:")
for pwd in passwords:
    valid, message = is_strong_password(pwd)
    status = "✓" if valid else "✗"
    print(f"  {status} {pwd:<20} {message}")
print()

# Example 9: Combining Multiple Checks
print("="*70)
print("Example 9: Complex Validation Logic")
print("="*70)

def validate_username(username):
    """Comprehensive username validation"""
    errors = []

    # Length check
    if len(username) < 3:
        errors.append("Too short (min 3)")
    elif len(username) > 20:
        errors.append("Too long (max 20)")

    # Character check
    if not username.isalnum() and "_" not in username:
        # Only allow alphanumeric and underscore
        if not all(c.isalnum() or c == "_" for c in username):
            errors.append("Only letters, numbers, underscore allowed")

    # Cannot start with number
    if username and username[0].isdigit():
        errors.append("Cannot start with number")

    # Cannot be all numbers
    if username.isdigit():
        errors.append("Cannot be all numbers")

    return len(errors) == 0, errors

usernames = ["alice123", "123bob", "a", "very_long_username_too_long_123", "valid_user"]

print("Username validation:")
for username in usernames:
    valid, errors = validate_username(username)
    status = "✓ VALID" if valid else "✗ INVALID"
    print(f"  {username:<30} {status}")
    for error in errors:
        print(f"    - {error}")
print()

# Example 10: Practical Application - Form Validation
print("="*70)
print("Example 10: Real-World Use Case - Complete Form Validation")
print("="*70)

def validate_form(form_data):
    """Validate registration form"""
    errors = {}

    # Name validation
    name = form_data.get("name", "").strip()
    if not name:
        errors["name"] = "Name is required"
    elif not name.replace(" ", "").isalpha():
        errors["name"] = "Name can only contain letters and spaces"

    # Age validation
    age = form_data.get("age", "").strip()
    if not age:
        errors["age"] = "Age is required"
    elif not age.isdigit():
        errors["age"] = "Age must be a number"
    elif int(age) < 18:
        errors["age"] = "Must be 18 or older"

    # Email validation (basic)
    email = form_data.get("email", "").strip()
    if not email:
        errors["email"] = "Email is required"
    elif "@" not in email or "." not in email:
        errors["email"] = "Invalid email format"

    # Phone validation
    phone = form_data.get("phone", "").strip()
    digits_only = "".join(c for c in phone if c.isdigit())
    if not digits_only:
        errors["phone"] = "Phone is required"
    elif len(digits_only) != 10:
        errors["phone"] = "Phone must be 10 digits"

    return errors

# Test with various forms
test_forms = [
    {"name": "Alice Johnson", "age": "25", "email": "alice@example.com", "phone": "555-123-4567"},
    {"name": "Bob123", "age": "17", "email": "invalid", "phone": "12345"},
    {"name": "", "age": "abc", "email": "", "phone": ""}
]

for i, form in enumerate(test_forms, 1):
    print(f"Form {i}:")
    errors = validate_form(form)

    if not errors:
        print("  ✓ ALL VALID")
    else:
        print("  ✗ ERRORS FOUND:")
        for field, error in errors.items():
            print(f"    - {field}: {error}")
    print()

print("="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. isdigit() - Check if all characters are digits")
print("2. isalpha() - Check if all characters are letters")
print("3. isalnum() - Check if alphanumeric (letters or digits)")
print("4. isspace() - Check if all whitespace")
print("5. isupper()/islower() - Check case")
print("6. istitle() - Check title case")
print("7. startswith()/endswith() - Prefix/suffix validation")
print("8. Combine checks for complex validation")
print("9. Build custom validators for business logic")
print("10. Essential for form validation and data integrity")
print("="*70)
'''

# Upgrade Lesson 85: String padding
lesson85['fullSolution'] = '''"""
String Padding

Master string padding and alignment in Python—ljust(), rjust(), center(),
and zfill(). Essential for formatting tables, reports, and aligned text
output.

**Zero Package Installation Required**
"""

# Example 1: ljust() - Left Justify (Pad Right)
print("="*70)
print("Example 1: ljust() - Left Align with Right Padding")
print("="*70)

text = "Python"
width = 20

padded = text.ljust(width)
print(f"Original: '{text}' (length {len(text)})")
print(f"ljust({width}): '{padded}' (length {len(padded)})")
print(f"Visual: |{padded}|")

# With custom fill character
padded_star = text.ljust(width, "*")
print(f"\\nWith '*': |{padded_star}|")

# If string longer than width, returns original
long = "Very Long String"
print(f"\\n'{long}'.ljust(5): '{long.ljust(5)}'")
print()

# Example 2: rjust() - Right Justify (Pad Left)
print("="*70)
print("Example 2: rjust() - Right Align with Left Padding")
print("="*70)

text = "Python"
width = 20

padded = text.rjust(width)
print(f"Original: '{text}'")
print(f"rjust({width}): |{padded}|")

# With custom fill character
padded_dash = text.rjust(width, "-")
print(f"With '-': |{padded_dash}|")

# Numeric alignment
numbers = ["1", "25", "300", "4500"]
print("\\nRight-aligned numbers:")
for num in numbers:
    print(f"  |{num.rjust(10)}|")
print()

# Example 3: center() - Center with Padding
print("="*70)
print("Example 3: center() - Center Align with Padding")
print("="*70)

text = "Title"
width = 30

centered = text.center(width)
print(f"Original: '{text}'")
print(f"center({width}): |{centered}|")

# With custom fill character
centered_eq = text.center(width, "=")
print(f"With '=': |{centered_eq}|")

# Note: Odd padding adds extra space on right
text = "Hi"
for w in [5, 6, 7, 8]:
    print(f"\\n'{text}'.center({w}): |{text.center(w)}|")
print()

# Example 4: zfill() - Zero Padding for Numbers
print("="*70)
print("Example 4: zfill() - Zero Padding for Numeric Strings")
print("="*70)

numbers = ["1", "42", "123", "7890"]
print("Original numbers with zfill(6):")
for num in numbers:
    padded = num.zfill(6)
    print(f"  {num:>6} → {padded}")

# Handles negative numbers correctly
negatives = ["-5", "-42", "-123"]
print("\\nNegative numbers:")
for num in negatives:
    padded = num.zfill(6)
    print(f"  {num:>6} → {padded}")

# Handles positive sign
positive = "+42"
print(f"\\nPositive: '{positive}'.zfill(6): '{positive.zfill(6)}'")
print()

# Example 5: Format Strings with Alignment
print("="*70)
print("Example 5: Format Strings with < > ^ Alignment")
print("="*70)

name = "Alice"
age = 30

# Using f-strings
print(f"Left align:   |{name:<15}|")
print(f"Right align:  |{name:>15}|")
print(f"Center align: |{name:^15}|")

# With custom fill character
print(f"\\nWith '*': |{name:*<15}|")
print(f"With '-': |{name:->15}|")
print(f"With '=': |{name:=^15}|")

# Numbers
print(f"\\nNumber alignment:")
print(f"Left:   |{age:<10}|")
print(f"Right:  |{age:>10}|")
print(f"Center: |{age:^10}|")
print()

# Example 6: Building Aligned Tables
print("="*70)
print("Example 6: Create Formatted Table")
print("="*70)

# Define column widths
col1_width = 15
col2_width = 8
col3_width = 12

# Header
print("Simple table:")
print("Name".ljust(col1_width) + "Age".rjust(col2_width) + "City".ljust(col3_width))
print("-" * (col1_width + col2_width + col3_width))

# Data rows
data = [
    ("Alice", "30", "New York"),
    ("Bob", "25", "Boston"),
    ("Charlie", "35", "Chicago")
]

for name, age, city in data:
    print(name.ljust(col1_width) + age.rjust(col2_width) + city.ljust(col3_width))

# Fancy table with separators
print("\\nFancy table:")
header_sep = "=" * (col1_width + col2_width + col3_width + 4)
print(header_sep)
print(f"| {'Name'.ljust(col1_width)} | {'Age'.rjust(col2_width)} | {'City'.ljust(col3_width)} |")
print(header_sep)

for name, age, city in data:
    print(f"| {name.ljust(col1_width)} | {age.rjust(col2_width)} | {city.ljust(col3_width)} |")

print(header_sep)
print()

# Example 7: Invoice/Receipt Formatting
print("="*70)
print("Example 7: Formatted Invoice")
print("="*70)

items = [
    {"name": "Laptop", "quantity": 1, "price": 999.99},
    {"name": "Mouse", "quantity": 2, "price": 29.99},
    {"name": "Keyboard", "quantity": 1, "price": 79.99}
]

print("="*60)
print("INVOICE".center(60))
print("="*60)
print()
print(f"{'Item':<30} {'Qty':>5} {'Price':>10} {'Total':>12}")
print("-"*60)

total = 0
for item in items:
    name = item["name"]
    qty = item["quantity"]
    price = item["price"]
    subtotal = qty * price
    total += subtotal

    print(f"{name:<30} {str(qty):>5} ${price:>9.2f} ${subtotal:>11.2f}")

print("-"*60)
print(f"{'TOTAL':<30} {'':<5} {'':<10} ${total:>11.2f}")
print("="*60)
print()

# Example 8: Progress Bar with Padding
print("="*70)
print("Example 8: Text-Based Progress Bar")
print("="*70)

def show_progress(percent, width=50):
    """Display progress bar"""
    filled = int(width * percent / 100)
    bar = "█" * filled
    bar = bar.ljust(width, "░")
    return f"|{bar}| {percent:3d}%"

print("Progress bars:")
for progress in [0, 25, 50, 75, 100]:
    print(show_progress(progress))

print("\\nDifferent widths:")
for width in [20, 30, 40]:
    print(f"Width {width}: {show_progress(66, width)}")
print()

# Example 9: Padding with Numbers and Codes
print("="*70)
print("Example 9: Order Numbers and Transaction IDs")
print("="*70)

# Generate order IDs with padding
order_numbers = [1, 25, 150, 2001]
print("Order IDs (zero-padded to 6 digits):")
for num in order_numbers:
    order_id = str(num).zfill(6)
    print(f"  Order #{order_id}")

# Transaction codes with prefix
print("\\nTransaction codes:")
for num in order_numbers:
    code = "TXN-" + str(num).zfill(8)
    print(f"  {code}")

# Date formatting
year, month, day = 2024, 3, 5
date_str = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
print(f"\\nFormatted date: {date_str}")
print()

# Example 10: Practical Application - Formatted Report
print("="*70)
print("Example 10: Real-World Use Case - Sales Report")
print("="*70)

sales_data = [
    {"region": "North", "q1": 125000, "q2": 135000, "q3": 145000, "q4": 155000},
    {"region": "South", "q1": 98000, "q2": 105000, "q3": 110000, "q4": 120000},
    {"region": "East", "q1": 110000, "q2": 115000, "q3": 120000, "q4": 125000},
    {"region": "West", "q1": 145000, "q2": 150000, "q3": 160000, "q4": 170000}
]

# Build report
width = 70
print("="*width)
print("QUARTERLY SALES REPORT".center(width))
print("2024".center(width))
print("="*width)
print()

# Header
header = (
    "Region".ljust(12) +
    "Q1".rjust(12) +
    "Q2".rjust(12) +
    "Q3".rjust(12) +
    "Q4".rjust(12) +
    "Total".rjust(15)
)
print(header)
print("-"*width)

# Data rows
grand_total = 0
for region_data in sales_data:
    region = region_data["region"]
    q1 = region_data["q1"]
    q2 = region_data["q2"]
    q3 = region_data["q3"]
    q4 = region_data["q4"]
    total = q1 + q2 + q3 + q4
    grand_total += total

    row = (
        region.ljust(12) +
        f"${q1:,}".rjust(12) +
        f"${q2:,}".rjust(12) +
        f"${q3:,}".rjust(12) +
        f"${q4:,}".rjust(12) +
        f"${total:,}".rjust(15)
    )
    print(row)

# Footer
print("="*width)
footer = "GRAND TOTAL".ljust(12 + 12 + 12 + 12 + 12) + f"${grand_total:,}".rjust(15)
print(footer)
print("="*width)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. ljust(width, fillchar) - Left align, pad right")
print("2. rjust(width, fillchar) - Right align, pad left")
print("3. center(width, fillchar) - Center align, pad both sides")
print("4. zfill(width) - Zero padding for numbers")
print("5. Default fillchar is space ' '")
print("6. If text longer than width, returns original")
print("7. zfill() handles +/- signs correctly")
print("8. f-strings support {value:<width}, {value:>width}, {value:^width}")
print("9. Essential for tables, reports, invoices")
print("10. Combine with format() for complex layouts")
print("="*70)
'''

# Save the updated lessons
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Print summary
print("\nUpgraded lessons 81-85:")
print(f"  81: String Reverse - {len(lesson81['fullSolution'])} chars")
print(f"  82: String Slicing - {len(lesson82['fullSolution'])} chars")
print(f"  83: String Split and Join - {len(lesson83['fullSolution'])} chars")
print(f"  84: String Validation - {len(lesson84['fullSolution'])} chars")
print(f"  85: String padding - {len(lesson85['fullSolution'])} chars")
print("\nBatch 81-85 complete!")
