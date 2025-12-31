#!/usr/bin/env python3
"""
Upgrade Python lessons 76-80 with comprehensive content.
- Lesson 76: String Methods
- Lesson 77: String Methods - strip
- Lesson 78: String Methods - upper and lower
- Lesson 79: String Palindrome Check
- Lesson 80: String Replace
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 76-80
lesson76 = next(l for l in lessons if l['id'] == 76)
lesson77 = next(l for l in lessons if l['id'] == 77)
lesson78 = next(l for l in lessons if l['id'] == 78)
lesson79 = next(l for l in lessons if l['id'] == 79)
lesson80 = next(l for l in lessons if l['id'] == 80)

# Upgrade Lesson 76: String Methods
lesson76['fullSolution'] = '''"""
String Methods

Master the complete arsenal of Python string methods—from basics like
upper() and lower() to advanced techniques with partition(), translate(),
and more. Essential reference for professional string manipulation.

**Zero Package Installation Required**
"""

# Example 1: Case Transformation Methods
print("="*70)
print("Example 1: Complete Case Transformation Suite")
print("="*70)

text = "python programming"
print(f"Original: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"capitalize(): '{text.capitalize()}'")  # First char only
print(f"title(): '{text.title()}'")  # Each word
print(f"swapcase(): '{text.swapcase()}'")

mixed = "PyThOn"
print(f"\\n'{mixed}' swapcase: '{mixed.swapcase()}'")
print()

# Example 2: Whitespace and Character Stripping
print("="*70)
print("Example 2: strip(), lstrip(), rstrip() Variations")
print("="*70)

# Whitespace stripping
padded = "   Hello World   "
print(f"Original: '{padded}'")
print(f"strip(): '{padded.strip()}'")
print(f"lstrip(): '{padded.lstrip()}'")
print(f"rstrip(): '{padded.rstrip()}'")

# Custom character stripping
url = "https://example.com///"
print(f"\\nURL: '{url}'")
print(f"rstrip('/'): '{url.rstrip('/')}'")

code = "***Important***"
print(f"\\nCode: '{code}'")
print(f"strip('*'): '{code.strip('*')}'")

# Multiple characters
messy = "...!!!Hello!!!..."
print(f"\\nMessy: '{messy}'")
print(f"strip('.!'): '{messy.strip('.!')}'")
print()

# Example 3: Search and Find Methods
print("="*70)
print("Example 3: Searching - find(), index(), count()")
print("="*70)

text = "Python is awesome and Python is powerful"
print(f"Text: '{text}'")

print(f"\\nfind('Python'): {text.find('Python')}")
print(f"rfind('Python'): {text.rfind('Python')}")
print(f"count('Python'): {text.count('Python')}")
print(f"count('is'): {text.count('is')}")

# index vs find
print("\\nindex() vs find():")
print(f"find('Java'): {text.find('Java')}")  # Returns -1

try:
    print(f"index('Java'): {text.index('Java')}")
except ValueError:
    print("index('Java'): ValueError - not found")
print()

# Example 4: Boolean Check Methods
print("="*70)
print("Example 4: Validation Methods (is...)")
print("="*70)

test_cases = {
    "12345": "digits",
    "Python": "letters",
    "abc123": "alphanumeric",
    "   ": "whitespace",
    "HELLO": "uppercase",
    "hello": "lowercase",
    "Hello World": "title case",
    "": "empty"
}

print(f"{'String':<15} {'isdigit':<8} {'isalpha':<8} {'isalnum':<8} {'isspace':<8} {'isupper':<8} {'islower':<8} {'istitle':<8}")
print("-"*90)

for string, desc in test_cases.items():
    if string:  # Skip empty for display
        display = repr(string)
        print(f"{display:<15} {str(string.isdigit()):<8} {str(string.isalpha()):<8} "
              f"{str(string.isalnum()):<8} {str(string.isspace()):<8} "
              f"{str(string.isupper()):<8} {str(string.islower()):<8} {str(string.istitle()):<8}")
print()

# Example 5: Prefix and Suffix Checking
print("="*70)
print("Example 5: startswith() and endswith()")
print("="*70)

filename = "document.pdf"
print(f"Filename: '{filename}'")
print(f"startswith('doc'): {filename.startswith('doc')}")
print(f"endswith('.pdf'): {filename.endswith('.pdf')}")
print(f"endswith('.txt'): {filename.endswith('.txt')}")

# Multiple options (tuple)
url = "https://example.com"
print(f"\\nURL: '{url}'")
print(f"starts with http/https: {url.startswith(('http://', 'https://'))}")

files = ["script.py", "data.json", "test.py", "README.md"]
print(f"\\nPython files in {files}:")
for f in files:
    if f.endswith('.py'):
        print(f"  {f}")
print()

# Example 6: Splitting and Joining
print("="*70)
print("Example 6: split(), rsplit(), splitlines(), partition()")
print("="*70)

text = "apple,banana,cherry,date"
print(f"CSV: '{text}'")
print(f"split(','): {text.split(',')}")

# Split with limit
limited = text.split(',', 2)
print(f"split(',', 2): {limited}")

# rsplit - from right
print(f"rsplit(',', 2): {text.rsplit(',', 2)}")

# splitlines
multiline = "Line 1\\nLine 2\\nLine 3"
print(f"\\nMultiline: {repr(multiline)}")
print(f"splitlines(): {multiline.splitlines()}")

# partition - split into 3 parts
email = "user@example.com"
print(f"\\nEmail: '{email}'")
parts = email.partition('@')
print(f"partition('@'): {parts}")
print(f"  Username: {parts[0]}, Separator: {parts[1]}, Domain: {parts[2]}")
print()

# Example 7: Replacement Methods
print("="*70)
print("Example 7: replace() and translate()")
print("="*70)

text = "I love Java. Java is great!"
print(f"Original: '{text}'")
print(f"replace('Java', 'Python'): '{text.replace('Java', 'Python')}'")
print(f"replace('Java', 'Python', 1): '{text.replace('Java', 'Python', 1)}'")

# translate - character mapping
translation_table = str.maketrans("aeiou", "12345")
original = "hello world"
translated = original.translate(translation_table)
print(f"\\nOriginal: '{original}'")
print(f"Vowels→Numbers: '{translated}'")

# Remove characters
remove_vowels = str.maketrans("", "", "aeiou")
no_vowels = "hello world".translate(remove_vowels)
print(f"Remove vowels: '{no_vowels}'")
print()

# Example 8: Alignment and Padding
print("="*70)
print("Example 8: center(), ljust(), rjust(), zfill()")
print("="*70)

text = "Python"
width = 20

print(f"Original: '{text}'")
print(f"center({width}): '{text.center(width)}'")
print(f"ljust({width}): '{text.ljust(width)}'")
print(f"rjust({width}): '{text.rjust(width)}'")
print(f"center({width}, '*'): '{text.center(width, '*')}'")

# zfill - zero padding for numbers
number = "42"
print(f"\\n'{number}'.zfill(5): '{number.zfill(5)}'")
print(f"'-42'.zfill(5): '{'-42'.zfill(5)}'")
print()

# Example 9: Formatting Methods
print("="*70)
print("Example 9: format(), format_map(), expandtabs()")
print("="*70)

# format
template = "Name: {}, Age: {}, City: {}"
result = template.format("Alice", 30, "NYC")
print(f"format(): '{result}'")

# Named placeholders
template2 = "Name: {name}, Age: {age}"
result2 = template2.format(name="Bob", age=25)
print(f"Named format: '{result2}'")

# format_map with dictionary
data = {"name": "Charlie", "age": 35}
template3 = "Name: {name}, Age: {age}"
result3 = template3.format_map(data)
print(f"format_map: '{result3}'")

# expandtabs
tabbed = "Column1\\tColumn2\\tColumn3"
print(f"\\nWith tabs: '{tabbed}'")
print(f"expandtabs(): '{tabbed.expandtabs()}'")
print(f"expandtabs(4): '{tabbed.expandtabs(4)}'")
print()

# Example 10: Practical Application - Text Processing Pipeline
print("="*70)
print("Example 10: Real-World Use Case - Process User Input")
print("="*70)

user_inputs = [
    "  ALICE@EXAMPLE.COM  ",
    "bob.smith@company.org",
    "  Charlie_Jones@Domain.COM  "
]

print("Email processing pipeline:")
print(f"{'Raw Input':<30} {'Processed':<30}")
print("-"*60)

for raw_input in user_inputs:
    # Pipeline: strip → lowercase → remove dots from username
    processed = raw_input.strip().lower()

    # Split email
    if '@' in processed:
        username, domain = processed.split('@')

        # Clean username (remove dots, common in emails)
        clean_username = username.replace('.', '')

        # Reconstruct
        final = f"{clean_username}@{domain}"

        print(f"{raw_input!r:<30} {final:<30}")

print("\\nText cleaning pipeline:")
messy_text = "  HELLO    WORLD!!!  "
print(f"Original: {messy_text!r}")

# Multi-step cleaning
cleaned = (messy_text
           .strip()          # Remove outer whitespace
           .lower()          # Lowercase
           .replace('!!!', '')  # Remove punctuation
           .replace('    ', ' ')  # Normalize spaces
           )

print(f"Cleaned: '{cleaned}'")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Case: upper(), lower(), title(), capitalize(), swapcase()")
print("2. Strip: strip(), lstrip(), rstrip() - whitespace or chars")
print("3. Search: find(), rfind(), index(), rindex(), count()")
print("4. Check: startswith(), endswith(), in operator")
print("5. Validate: isdigit(), isalpha(), isalnum(), isspace(), etc.")
print("6. Split: split(), rsplit(), partition(), splitlines()")
print("7. Replace: replace(), translate()")
print("8. Align: center(), ljust(), rjust(), zfill()")
print("9. Format: format(), format_map()")
print("10. Chain methods for complex transformations")
print("="*70)
'''

# Upgrade Lesson 77: String Methods - strip
lesson77['fullSolution'] = '''"""
String Methods - strip

Master strip(), lstrip(), and rstrip() methods for removing unwanted
characters from strings. Essential for data cleaning, parsing, and
input validation.

**Zero Package Installation Required**
"""

# Example 1: Basic strip() - Remove Whitespace
print("="*70)
print("Example 1: strip() - Remove Leading/Trailing Whitespace")
print("="*70)

padded = "   Hello World   "
print(f"Original: '{padded}' (length: {len(padded)})")

stripped = padded.strip()
print(f"Stripped: '{stripped}' (length: {len(stripped)})")

# Show what was removed
print(f"\\nRemoved {len(padded) - len(stripped)} characters")
print(f"Leading spaces: {len(padded) - len(padded.lstrip())}")
print(f"Trailing spaces: {len(padded) - len(padded.rstrip())}")
print()

# Example 2: lstrip() - Left Strip Only
print("="*70)
print("Example 2: lstrip() - Remove Leading Whitespace Only")
print("="*70)

text = "   Python Programming   "
print(f"Original: '{text}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")
print(f"strip(): '{text.strip()}'")

# Demonstrate difference
print("\\nVisual comparison:")
print(f"Original: |{text}|")
print(f"lstrip(): |{text.lstrip()}|")
print(f"rstrip(): |{text.rstrip()}|")
print(f"strip():  |{text.strip()}|")
print()

# Example 3: Strip Specific Characters
print("="*70)
print("Example 3: Strip Custom Characters")
print("="*70)

url = "https://example.com///"
print(f"URL: '{url}'")
cleaned = url.rstrip('/')
print(f"rstrip('/'): '{cleaned}'")

# Strip multiple characters
markdown = "***Important Message***"
print(f"\\nMarkdown: '{markdown}'")
print(f"strip('*'): '{markdown.strip('*')}'")

# Order doesn't matter
messy = "...!!!Hello!!!..."
print(f"\\nMessy: '{messy}'")
print(f"strip('.!'): '{messy.strip('.!')}'")
print(f"strip('!.'): '{messy.strip('!.')}'")  # Same result
print()

# Example 4: Strip from Both Ends vs One End
print("="*70)
print("Example 4: Comparing strip(), lstrip(), rstrip()")
print("="*70)

data = "###DATA###"
print(f"Original: '{data}'")
print(f"strip('#'): '{data.strip('#')}'")
print(f"lstrip('#'): '{data.lstrip('#')}'")
print(f"rstrip('#'): '{data.rstrip('#')}'")

# Asymmetric stripping
log_entry = ">>> Error in module <<<"
print(f"\\nLog: '{log_entry}'")
print(f"lstrip('> '): '{log_entry.lstrip('> ')}'")
print(f"rstrip('< '): '{log_entry.rstrip('< ')}'")
print(f"strip('< >'): '{log_entry.strip('< >')}'")
print()

# Example 5: Strip Doesn't Remove from Middle
print("="*70)
print("Example 5: strip() Only Affects Edges")
print("="*70)

text = "  Hello  World  "
print(f"Original: '{text}'")
stripped = text.strip()
print(f"Stripped: '{stripped}'")
print("Note: Middle spaces preserved!")

# To remove ALL spaces, use replace
no_spaces = text.replace(" ", "")
print(f"replace(' ', ''): '{no_spaces}'")

# Or normalize multiple spaces
normalized = " ".join(text.split())
print(f"Normalized: '{normalized}'")
print()

# Example 6: Common Use Case - Cleaning User Input
print("="*70)
print("Example 6: Cleaning User Input")
print("="*70)

user_inputs = [
    "  alice  ",
    "\\t\\tbob\\t\\t",
    "\\n\\ncharlie\\n\\n",
    "  \\t david \\n  "
]

print("Raw input → Cleaned:")
for raw in user_inputs:
    cleaned = raw.strip()
    print(f"  {raw!r:<20} → '{cleaned}'")

# Strip multiple whitespace types
messy_input = "  \\t\\n  Hello  \\n\\t  "
print(f"\\nMessy: {messy_input!r}")
print(f"Cleaned: '{messy_input.strip()}'")
print()

# Example 7: Strip Newlines and Carriage Returns
print("="*70)
print("Example 7: Removing Line Endings")
print("="*70)

# Unix line ending
unix_line = "Hello World\\n"
print(f"Unix: {unix_line!r}")
print(f"strip(): {unix_line.strip()!r}")

# Windows line ending
windows_line = "Hello World\\r\\n"
print(f"\\nWindows: {windows_line!r}")
print(f"strip(): {windows_line.strip()!r}")

# Old Mac line ending
mac_line = "Hello World\\r"
print(f"\\nOld Mac: {mac_line!r}")
print(f"strip(): {mac_line.strip()!r}")

# Reading file lines
file_lines = ["Line 1\\n", "Line 2\\n", "Line 3\\n"]
print(f"\\nFile lines: {file_lines}")
cleaned_lines = [line.strip() for line in file_lines]
print(f"Cleaned: {cleaned_lines}")
print()

# Example 8: Strip with Character Sets
print("="*70)
print("Example 8: Stripping Multiple Character Types")
print("="*70)

# Strip punctuation
text = "...Hello, World!..."
print(f"Original: '{text}'")
print(f"strip('.,!'): '{text.strip('.,!')}'")

# Strip digits
code = "123ABC456"
print(f"\\nCode: '{code}'")
print(f"strip('0123456789'): '{code.strip('0123456789')}'")

# More elegant with string constants
import string
digits_code = "999Python999"
print(f"\\nDigits code: '{digits_code}'")
print(f"strip(digits): '{digits_code.strip(string.digits)}'")

punctuated = "!!!Hello!!!"
print(f"\\nPunctuated: '{punctuated}'")
print(f"strip(punctuation): '{punctuated.strip(string.punctuation)}'")
print()

# Example 9: Strip in Data Processing Pipeline
print("="*70)
print("Example 9: strip() in Data Processing")
print("="*70)

csv_line = "  Alice  ,  30  ,  Engineer  "
print(f"CSV line: '{csv_line}'")

# Split then strip each field
fields = [field.strip() for field in csv_line.split(',')]
print(f"Parsed fields: {fields}")

# Process multiple lines
csv_data = [
    " Name , Age , Title ",
    " Alice , 30 , Engineer ",
    " Bob , 25 , Designer "
]

print("\\nProcessing CSV:")
for i, line in enumerate(csv_data):
    fields = [f.strip() for f in line.split(',')]
    if i == 0:
        print(f"Header: {fields}")
    else:
        print(f"Row {i}: {fields}")
print()

# Example 10: Practical Application - Password Validation
print("="*70)
print("Example 10: Real-World Use Case - Form Validation")
print("="*70)

# Simulated form inputs (with common whitespace issues)
form_data = {
    "username": "  alice123  ",
    "email": "  alice@example.com  \\n",
    "password": "  SecurePass123!  ",  # Should NOT strip passwords
    "phone": "  555-1234  "
}

print("Form data cleaning:")
print(f"{'Field':<12} {'Raw':<30} {'Cleaned':<30}")
print("-"*72)

cleaned_data = {}
for field, value in form_data.items():
    # Don't strip passwords (whitespace might be intentional)
    if field == "password":
        cleaned = value  # Keep as-is
        print(f"{field:<12} {value!r:<30} (not cleaned)")
    else:
        cleaned = value.strip()
        cleaned_data[field] = cleaned
        print(f"{field:<12} {value!r:<30} {cleaned!r:<30}")

print("\\nWARNING: Passwords should generally NOT be stripped!")
print("Whitespace in passwords might be intentional.")

# Email normalization
email_input = "  User@EXAMPLE.COM  \\n"
normalized_email = email_input.strip().lower()
print(f"\\nEmail: {email_input!r} → '{normalized_email}'")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. strip() - Remove from both ends")
print("2. lstrip() - Remove from left (start) only")
print("3. rstrip() - Remove from right (end) only")
print("4. Default: removes whitespace (space, tab, newline, etc.)")
print("5. strip(chars) - Remove specified characters")
print("6. Only affects edges, not middle of string")
print("7. Order of chars argument doesn't matter")
print("8. Returns new string (strings are immutable)")
print("9. Essential for cleaning user input and parsing data")
print("10. Common pattern: [x.strip() for x in list]")
print("="*70)
'''

# Upgrade Lesson 78: String Methods - upper and lower
lesson78['fullSolution'] = '''"""
String Methods - upper and lower

Master case conversion methods in Python—upper(), lower(), capitalize(),
title(), and swapcase(). Essential for text normalization, case-insensitive
comparisons, and formatting.

**Zero Package Installation Required**
"""

# Example 1: Basic upper() and lower()
print("="*70)
print("Example 1: upper() and lower() - Basic Case Conversion")
print("="*70)

text = "Python Programming"
print(f"Original: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")

# Already converted
all_caps = "HELLO"
print(f"\\n'{all_caps}'.upper(): '{all_caps.upper()}'")  # No change

all_lower = "hello"
print(f"'{all_lower}'.lower(): '{all_lower.lower()}'")  # No change
print()

# Example 2: Case-Insensitive Comparison
print("="*70)
print("Example 2: Case-Insensitive String Comparison")
print("="*70)

password_input = "MyPassword123"
stored_password = "mypassword123"

# Wrong way - case sensitive
print(f"Input: '{password_input}'")
print(f"Stored: '{stored_password}'")
print(f"Direct comparison: {password_input == stored_password}")

# Better - case insensitive
print(f"Case-insensitive: {password_input.lower() == stored_password.lower()}")

# Multiple comparisons
search_term = "PYTHON"
documents = ["Learn Python", "Java Guide", "python basics", "PYTHON tutorial"]

print(f"\\nSearching for: '{search_term}'")
print("Matching documents:")
for doc in documents:
    if search_term.lower() in doc.lower():
        print(f"  - {doc}")
print()

# Example 3: capitalize() - First Character Only
print("="*70)
print("Example 3: capitalize() - First Letter Only")
print("="*70)

sentences = [
    "python programming",
    "HELLO WORLD",
    "mIxEd CaSe"
]

print("capitalize() results:")
for sentence in sentences:
    capitalized = sentence.capitalize()
    print(f"  '{sentence}' → '{capitalized}'")

# Important: capitalize() lowers everything else
weird = "hELLO wORLD"
print(f"\\n'{weird}'.capitalize(): '{weird.capitalize()}'")
print("Note: Everything after first char becomes lowercase!")
print()

# Example 4: title() - Capitalize Each Word
print("="*70)
print("Example 4: title() - Title Case Each Word")
print("="*70)

book_titles = [
    "the lord of the rings",
    "HARRY POTTER",
    "to kill a mockingbird"
]

print("title() results:")
for title in book_titles:
    formatted = title.title()
    print(f"  '{title}'")
    print(f"  → '{formatted}'")
    print()

# Watch out for apostrophes
name = "o'brien"
print(f"'{name}'.title(): '{name.title()}'")
print("Note: Characters after apostrophes get capitalized too!")
print()

# Example 5: swapcase() - Invert Case
print("="*70)
print("Example 5: swapcase() - Toggle Case")
print("="*70)

examples = [
    "Hello World",
    "PYTHON",
    "python",
    "PyThOn"
]

print("swapcase() results:")
for example in examples:
    swapped = example.swapcase()
    print(f"  '{example}' → '{swapped}'")

# Double swap returns to original
text = "Hello World"
double_swapped = text.swapcase().swapcase()
print(f"\\nDouble swap: '{text}' → '{double_swapped}'")
print()

# Example 6: Normalization for Storage
print("="*70)
print("Example 6: Data Normalization - Email and Username")
print("="*70)

user_registrations = [
    {"email": "Alice@EXAMPLE.COM", "username": "Alice123"},
    {"email": "BOB@company.org", "username": "bob_admin"},
    {"email": "Charlie@Domain.COM", "username": "CHARLIE"}
]

print("Normalizing user data:")
print(f"{'Original Email':<25} {'Normalized':<25} {'Username':<15}")
print("-"*65)

for user in user_registrations:
    normalized_email = user["email"].lower()
    normalized_username = user["username"].lower()

    print(f"{user['email']:<25} {normalized_email:<25} {normalized_username:<15}")

print("\\nWhy normalize?")
print("  - Prevents duplicate accounts (Alice@test.com vs alice@test.com)")
print("  - Enables case-insensitive login")
print("  - Consistent data storage")
print()

# Example 7: Case Validation Methods
print("="*70)
print("Example 7: Checking Case - isupper(), islower(), istitle()")
print("="*70)

test_strings = [
    "HELLO",
    "hello",
    "Hello World",
    "Hello",
    "123",
    "PyThOn"
]

print(f"{'String':<15} {'isupper()':<10} {'islower()':<10} {'istitle()':<10}")
print("-"*45)

for s in test_strings:
    print(f"'{s}':<15} {str(s.isupper()):<10} {str(s.islower()):<10} {str(s.istitle()):<10}")

print("\\nNotes:")
print("  - Non-letter characters don't affect case checks")
print("  - '123'.isupper() is False (no cased characters)")
print("  - istitle() checks if each word starts with uppercase")
print()

# Example 8: Conditional Case Conversion
print("="*70)
print("Example 8: Smart Case Conversion Based on Content")
print("="*70)

def smart_format(text):
    """Apply appropriate case based on content"""
    if text.isupper():
        # All caps → Title case
        return text.title()
    elif text.islower():
        # All lower → Capitalize
        return text.capitalize()
    else:
        # Mixed → No change
        return text

examples = ["HELLO WORLD", "hello world", "Hello World"]

print("Smart formatting:")
for ex in examples:
    formatted = smart_format(ex)
    print(f"  '{ex}' → '{formatted}'")
print()

# Example 9: Constants and Environment Variables
print("="*70)
print("Example 9: Naming Conventions - Constants and Variables")
print("="*70)

# Constants typically UPPERCASE
API_KEY = "abc123"
MAX_RETRIES = 3
BASE_URL = "https://api.example.com"

print("Constants (UPPERCASE by convention):")
print(f"  API_KEY = '{API_KEY}'")
print(f"  MAX_RETRIES = {MAX_RETRIES}")
print(f"  BASE_URL = '{BASE_URL}'")

# Convert variable name to constant name
def to_constant_name(name):
    """Convert variable name to CONSTANT_NAME"""
    return name.replace(" ", "_").upper()

var_names = ["api key", "max retries", "base url"]
print("\\nConverting to constant names:")
for var in var_names:
    constant = to_constant_name(var)
    print(f"  '{var}' → '{constant}'")
print()

# Example 10: Practical Application - Text Processing
print("="*70)
print("Example 10: Real-World Use Case - Process Article Titles")
print("="*70)

articles = [
    "BREAKING: new python release",
    "how to learn programming",
    "TOP 10 CODING TIPS",
    "python vs. java: a comparison"
]

print("Processing article titles:")
print(f"{'Original':<40} {'Formatted':<40}")
print("-"*80)

for article in articles:
    # Smart formatting based on case
    if article.isupper() or article.islower():
        # Fix all-caps or all-lowercase
        formatted = article.title()
    else:
        # Already mixed case, capitalize first letter
        formatted = article.capitalize()

    # Handle special cases
    formatted = formatted.replace(" A ", " a ")
    formatted = formatted.replace(" And ", " and ")
    formatted = formatted.replace(" The ", " the ")
    formatted = formatted.replace("Vs.", "vs.")

    print(f"{article:<40} {formatted:<40}")

# URL slug generation
title = "Python Programming: A Complete Guide"
slug = title.lower().replace(" ", "-").replace(":", "")
print(f"\\nURL slug generation:")
print(f"  Title: '{title}'")
print(f"  Slug: '{slug}'")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. upper() - Convert all to uppercase")
print("2. lower() - Convert all to lowercase")
print("3. capitalize() - First char upper, rest lower")
print("4. title() - Capitalize first letter of each word")
print("5. swapcase() - Invert case of all characters")
print("6. isupper() - Check if all cased chars are uppercase")
print("7. islower() - Check if all cased chars are lowercase")
print("8. istitle() - Check if title cased")
print("9. Use lower() for case-insensitive comparisons")
print("10. Normalize data (emails, usernames) with lower()")
print("="*70)
'''

# Upgrade Lesson 79: String Palindrome Check
lesson79['fullSolution'] = '''"""
String Palindrome Check

Master techniques to check if strings are palindromes—from basic reversals
to advanced handling of spaces, punctuation, and case. Essential for
string algorithms and pattern recognition.

**Zero Package Installation Required**
"""

# Example 1: Basic Palindrome Check
print("="*70)
print("Example 1: Simple Palindrome Check with Reversal")
print("="*70)

def is_palindrome_simple(text):
    """Check if string is palindrome using reversal"""
    return text == text[::-1]

words = ["racecar", "hello", "level", "python", "noon", "world"]

print("Basic palindrome check:")
for word in words:
    result = is_palindrome_simple(word)
    status = "✓ PALINDROME" if result else "✗ Not palindrome"
    print(f"  '{word}': {status}")
print()

# Example 2: Case-Insensitive Palindrome
print("="*70)
print("Example 2: Case-Insensitive Palindrome Check")
print("="*70)

def is_palindrome_case_insensitive(text):
    """Check palindrome ignoring case"""
    text_lower = text.lower()
    return text_lower == text_lower[::-1]

words = ["Racecar", "Level", "NOON", "Python", "Madam"]

print("Case-insensitive check:")
for word in words:
    result = is_palindrome_case_insensitive(word)
    status = "✓ PALINDROME" if result else "✗ Not palindrome"
    print(f"  '{word}': {status}")
print()

# Example 3: Two-Pointer Approach
print("="*70)
print("Example 3: Two-Pointer Algorithm (No Reversal)")
print("="*70)

def is_palindrome_two_pointer(text):
    """Check palindrome using two pointers"""
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True

words = ["racecar", "hello", "kayak"]

print("Two-pointer palindrome check:")
for word in words:
    result = is_palindrome_two_pointer(word)
    print(f"  '{word}': {result}")

    # Show comparison steps
    left, right = 0, len(word) - 1
    print(f"    Comparisons: ", end="")
    comparisons = []
    while left < right:
        comparisons.append(f"{word[left]}=={word[right]}")
        left += 1
        right -= 1
    print(", ".join(comparisons))
print()

# Example 4: Handling Spaces and Punctuation
print("="*70)
print("Example 4: Palindrome with Spaces and Punctuation")
print("="*70)

def is_palindrome_alphanumeric(text):
    """Check palindrome considering only alphanumeric chars"""
    # Remove non-alphanumeric and convert to lowercase
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

phrases = [
    "A man a plan a canal Panama",
    "race a car",
    "Was it a car or a cat I saw?",
    "Hello World",
    "Madam, I'm Adam"
]

print("Palindrome phrases (ignoring spaces/punctuation):")
for phrase in phrases:
    result = is_palindrome_alphanumeric(phrase)
    status = "✓ PALINDROME" if result else "✗ Not palindrome"
    print(f"  '{phrase}'")
    print(f"    {status}")
print()

# Example 5: Step-by-Step Palindrome Analysis
print("="*70)
print("Example 5: Detailed Palindrome Analysis")
print("="*70)

def analyze_palindrome(text):
    """Analyze why a string is or isn't a palindrome"""
    print(f"Analyzing: '{text}'")
    print(f"  Length: {len(text)}")

    reversed_text = text[::-1]
    print(f"  Reversed: '{reversed_text}'")

    is_palindrome = text == reversed_text
    print(f"  Is palindrome: {is_palindrome}")

    if not is_palindrome:
        # Find first mismatch
        for i in range(len(text)):
            if i >= len(text) - 1 - i:
                break
            if text[i] != text[len(text) - 1 - i]:
                print(f"  First mismatch: position {i} ('{text[i]}') vs position {len(text)-1-i} ('{text[len(text)-1-i]}')")
                break

examples = ["racecar", "python", "level"]
for ex in examples:
    analyze_palindrome(ex)
    print()

# Example 6: Numeric Palindromes
print("="*70)
print("Example 6: Numeric Palindrome Check")
print("="*70)

def is_numeric_palindrome(number):
    """Check if number is palindrome"""
    num_str = str(number)
    return num_str == num_str[::-1]

numbers = [121, 123, 12321, 1001, 12345, 9009]

print("Numeric palindrome check:")
for num in numbers:
    result = is_numeric_palindrome(num)
    status = "✓ PALINDROME" if result else "✗ Not palindrome"
    print(f"  {num}: {status}")
print()

# Example 7: Finding Palindromes in Text
print("="*70)
print("Example 7: Extract Palindromes from Text")
print("="*70)

def find_palindromes(text, min_length=3):
    """Find all palindrome words in text"""
    words = text.lower().split()
    palindromes = []

    for word in words:
        # Clean word
        cleaned = "".join(c for c in word if c.isalnum())
        if len(cleaned) >= min_length and cleaned == cleaned[::-1]:
            palindromes.append(cleaned)

    return palindromes

texts = [
    "The racecar drove at noon",
    "Madam, in level three we saw Hannah",
    "A kayak and a civic were there"
]

print("Finding palindromes in text:")
for text in texts:
    palindromes = find_palindromes(text)
    print(f"  '{text}'")
    print(f"    Palindromes: {palindromes if palindromes else 'None'}")
print()

# Example 8: Longest Palindrome Substring
print("="*70)
print("Example 8: Find Longest Palindrome Substring")
print("="*70)

def longest_palindrome_substring(text):
    """Find the longest palindromic substring"""
    if not text:
        return ""

    longest = ""

    for i in range(len(text)):
        # Check odd-length palindromes (center at i)
        left = right = i
        while left >= 0 and right < len(text) and text[left] == text[right]:
            current = text[left:right+1]
            if len(current) > len(longest):
                longest = current
            left -= 1
            right += 1

        # Check even-length palindromes (center between i and i+1)
        left, right = i, i + 1
        while left >= 0 and right < len(text) and text[left] == text[right]:
            current = text[left:right+1]
            if len(current) > len(longest):
                longest = current
            left -= 1
            right += 1

    return longest

examples = ["babad", "cbbd", "racecar", "python"]

print("Longest palindrome substring:")
for ex in examples:
    longest = longest_palindrome_substring(ex)
    print(f"  '{ex}' → '{longest}' (length {len(longest)})")
print()

# Example 9: Palindrome Generator
print("="*70)
print("Example 9: Generate Palindromes")
print("="*70)

def make_palindrome(text):
    """Create palindrome by mirroring text"""
    return text + text[::-1]

def make_palindrome_skip_middle(text):
    """Create palindrome skipping middle character"""
    if len(text) == 0:
        return text
    return text + text[-2::-1]

words = ["race", "abc", "py"]

print("Generating palindromes:")
for word in words:
    full = make_palindrome(word)
    skip = make_palindrome_skip_middle(word)
    print(f"  '{word}':")
    print(f"    Full mirror: '{full}'")
    print(f"    Skip middle: '{skip}'")
print()

# Example 10: Practical Application - Username Validation
print("="*70)
print("Example 10: Real-World Use Case - Fun Facts About Usernames")
print("="*70)

usernames = ["racecar123", "level", "bob", "alice", "anna", "john_doe"]

print("Username analysis:")
print(f"{'Username':<15} {'Is Palindrome':<15} {'Cleaned':<15}")
print("-"*45)

for username in usernames:
    # Clean: remove non-letters, lowercase
    cleaned = "".join(c.lower() for c in username if c.isalpha())
    is_palindrome = cleaned == cleaned[::-1] if cleaned else False

    status = "Yes" if is_palindrome else "No"
    print(f"{username:<15} {status:<15} {cleaned:<15}")

print("\\nPalindrome usernames might be:")
print("  - Easier to remember")
print("  - More aesthetically pleasing")
print("  - Harder to create (limited options)")

# Fun: Check if user input is palindrome
def check_user_palindrome(text):
    """Interactive palindrome checker"""
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    is_palindrome = cleaned == cleaned[::-1]

    print(f"\\nChecking: '{text}'")
    print(f"Cleaned: '{cleaned}'")
    print(f"Reversed: '{cleaned[::-1]}'")
    print(f"Result: {'PALINDROME!' if is_palindrome else 'Not a palindrome'}")

check_user_palindrome("A man, a plan, a canal: Panama")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Basic check: text == text[::-1]")
print("2. Case-insensitive: text.lower() == text.lower()[::-1]")
print("3. Two-pointer approach: compare from both ends")
print("4. Clean first: remove spaces/punctuation with isalnum()")
print("5. Works for strings and numbers (convert to string)")
print("6. Can find palindromes in larger text")
print("7. Substring palindromes require nested loops")
print("8. Generate palindromes by mirroring text")
print("9. Time complexity: O(n) for basic check")
print("10. Useful for algorithms, puzzles, and pattern matching")
print("="*70)
'''

# Upgrade Lesson 80: String Replace
lesson80['fullSolution'] = '''"""
String Replace

Master the replace() method for string substitution in Python—from simple
text replacement to advanced patterns with count limits. Essential for
data cleaning, text processing, and string transformation.

**Zero Package Installation Required**
"""

# Example 1: Basic replace()
print("="*70)
print("Example 1: Basic String Replacement")
print("="*70)

text = "I love Java. Java is great!"
print(f"Original: '{text}'")

replaced = text.replace("Java", "Python")
print(f"replace('Java', 'Python'): '{replaced}'")

# Original unchanged (strings are immutable)
print(f"Original after replace: '{text}'")
print()

# Example 2: Replace with Count Limit
print("="*70)
print("Example 2: Limit Number of Replacements")
print("="*70)

text = "apple apple apple apple"
print(f"Original: '{text}'")

# Replace all
all_replaced = text.replace("apple", "orange")
print(f"Replace all: '{all_replaced}'")

# Replace first occurrence only
first_only = text.replace("apple", "orange", 1)
print(f"Replace first (count=1): '{first_only}'")

# Replace first two
first_two = text.replace("apple", "orange", 2)
print(f"Replace first 2 (count=2): '{first_two}'")
print()

# Example 3: Case-Sensitive Replacement
print("="*70)
print("Example 3: Case Sensitivity in replace()")
print("="*70)

text = "Python is fun. python is powerful. PYTHON rocks!"
print(f"Original: '{text}'")

# Case-sensitive (default)
replaced = text.replace("python", "Java")
print(f"\\nreplace('python', 'Java'): '{replaced}'")
print("Note: Only lowercase 'python' replaced!")

# Case-insensitive approach
def replace_case_insensitive(text, old, new):
    """Replace ignoring case"""
    # Find positions of all occurrences
    result = text
    old_lower = old.lower()
    i = 0

    while i < len(result):
        pos = result.lower().find(old_lower, i)
        if pos == -1:
            break
        result = result[:pos] + new + result[pos + len(old):]
        i = pos + len(new)

    return result

all_pythons = replace_case_insensitive(text, "python", "Java")
print(f"\\nCase-insensitive: '{all_pythons}'")
print()

# Example 4: Removing Substrings
print("="*70)
print("Example 4: Remove Substrings (Replace with Empty String)")
print("="*70)

text = "Hello***World***!"
print(f"Original: '{text}'")

# Remove asterisks
no_stars = text.replace("*", "")
print(f"Remove '*': '{no_stars}'")

# Remove multiple substrings
messy = "***URGENT*** Read this now!!!"
clean = messy.replace("*", "").replace("URGENT", "Info").replace("!", "")
print(f"\\nMessy: '{messy}'")
print(f"Cleaned: '{clean}'")
print()

# Example 5: Chaining Multiple Replacements
print("="*70)
print("Example 5: Chain Multiple replace() Calls")
print("="*70)

code = "var x = 10; var y = 20;"
print(f"Original: '{code}'")

# Convert JavaScript-style to Python
python_code = (code
               .replace("var ", "")
               .replace(";", "")
               .replace("x", "num1")
               .replace("y", "num2"))

print(f"Converted: '{python_code}'")

# Clean user input
user_input = "  Hello!!!  How are you???  "
cleaned = (user_input
           .strip()
           .replace("!!!", "!")
           .replace("???", "?")
           .replace("  ", " "))

print(f"\\nUser input: '{user_input}'")
print(f"Cleaned: '{cleaned}'")
print()

# Example 6: Replace with Special Characters
print("="*70)
print("Example 6: Replacing Special Characters")
print("="*70)

# Replace newlines
multiline = "Line1\\nLine2\\nLine3"
print(f"Original: {multiline!r}")

with_br = multiline.replace("\\n", "<br>")
print(f"HTML breaks: {with_br!r}")

# Replace tabs
tabbed = "Name\\tAge\\tCity"
print(f"\\nTabbed: {tabbed!r}")
csv = tabbed.replace("\\t", ",")
print(f"CSV: '{csv}'")

# Escape quotes
text_with_quotes = 'He said "Hello" to me'
escaped = text_with_quotes.replace('"', '\\"')
print(f"\\nOriginal: {text_with_quotes}")
print(f"Escaped: {escaped}")
print()

# Example 7: Replacement in File Paths
print("="*70)
print("Example 7: Path Manipulation")
print("="*70)

# Windows to Unix path
windows_path = "C:\\\\Users\\\\Alice\\\\Documents\\\\file.txt"
unix_path = windows_path.replace("\\\\", "/")

print(f"Windows: {windows_path}")
print(f"Unix: {unix_path}")

# Change file extension
filename = "document.txt"
new_filename = filename.replace(".txt", ".md")
print(f"\\n'{filename}' → '{new_filename}'")

# More robust extension change
def change_extension(filename, new_ext):
    """Change file extension safely"""
    if "." in filename:
        base = filename.rsplit(".", 1)[0]
        return f"{base}.{new_ext.lstrip('.')}"
    return f"{filename}.{new_ext.lstrip('.')}"

print(f"\\nRobust: '{filename}' → '{change_extension(filename, 'pdf')}'")
print()

# Example 8: Replace for Data Cleaning
print("="*70)
print("Example 8: Data Cleaning with replace()")
print("="*70)

# Clean phone numbers
phone_numbers = [
    "(555) 123-4567",
    "555-123-4567",
    "555.123.4567"
]

print("Cleaning phone numbers:")
for phone in phone_numbers:
    # Remove all non-digit characters
    cleaned = (phone
               .replace("(", "")
               .replace(")", "")
               .replace("-", "")
               .replace(".", "")
               .replace(" ", ""))

    # Format as XXX-XXX-XXXX
    if len(cleaned) == 10:
        formatted = f"{cleaned[:3]}-{cleaned[3:6]}-{cleaned[6:]}"
        print(f"  '{phone}' → '{formatted}'")
print()

# Example 9: Replace for Text Normalization
print("="*70)
print("Example 9: Normalize Text for Comparison")
print("="*70)

def normalize_text(text):
    """Normalize text for comparison"""
    normalized = text.lower()
    # Replace common variations
    normalized = normalized.replace("'", "'")  # Smart quote
    normalized = normalized.replace(""", '"')  # Smart double quote
    normalized = normalized.replace(""", '"')
    normalized = normalized.replace("–", "-")  # En dash
    normalized = normalized.replace("—", "-")  # Em dash
    # Remove extra spaces
    normalized = " ".join(normalized.split())
    return normalized

texts = [
    "Hello  World",
    "Hello—World",
    "Hello–World",
    "Hello-World"
]

print("Text normalization:")
for text in texts:
    normalized = normalize_text(text)
    print(f"  '{text}' → '{normalized}'")
print()

# Example 10: Practical Application - Template Processing
print("="*70)
print("Example 10: Real-World Use Case - Email Template")
print("="*70)

email_template = """Dear {{name}},

Thank you for your order #{{order_id}}.

Your total: ${{total}}
Shipping to: {{address}}

We appreciate your business!

Best regards,
The {{company}} Team"""

# Replace placeholders
order_data = {
    "name": "Alice Johnson",
    "order_id": "12345",
    "total": "99.99",
    "address": "123 Main St, City, State",
    "company": "TechStore"
}

personalized_email = email_template
for key, value in order_data.items():
    placeholder = "{{" + key + "}}"
    personalized_email = personalized_email.replace(placeholder, value)

print("Personalized email:")
print(personalized_email)

# URL slug creation
title = "Python Programming: A Complete Guide!"
slug = (title
        .lower()
        .replace(" ", "-")
        .replace(":", "")
        .replace("!", "")
        .replace("--", "-"))

print(f"\\nBlog post title: '{title}'")
print(f"URL slug: '{slug}'")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. str.replace(old, new) - Replace all occurrences")
print("2. str.replace(old, new, count) - Limit replacements")
print("3. Returns new string (original unchanged)")
print("4. Case-sensitive by default")
print("5. replace('x', '') - Remove substrings")
print("6. Chain multiple replace() calls for complex transforms")
print("7. Works with special characters (\\\\n, \\\\t, etc.)")
print("8. Use for data cleaning, normalization, formatting")
print("9. For regex patterns, use re.sub() instead")
print("10. Common pattern: .replace().replace().replace()")
print("="*70)
'''

# Save the updated lessons
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Print summary
print("\nUpgraded lessons 76-80:")
print(f"  76: String Methods - {len(lesson76['fullSolution'])} chars")
print(f"  77: String Methods - strip - {len(lesson77['fullSolution'])} chars")
print(f"  78: String Methods - upper and lower - {len(lesson78['fullSolution'])} chars")
print(f"  79: String Palindrome Check - {len(lesson79['fullSolution'])} chars")
print(f"  80: String Replace - {len(lesson80['fullSolution'])} chars")
print("\nBatch 76-80 complete!")
