#!/usr/bin/env python3
"""
Upgrade Python lessons 86-90 with comprehensive content.
- Lesson 86: Strings & f-Strings
- Lesson 87: Accessing Dictionary Values
- Lesson 88: Adding to Dictionaries
- Lesson 89: Checking Dictionary Keys
- Lesson 90: Creating Dictionaries
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 86-90
lesson86 = next(l for l in lessons if l['id'] == 86)
lesson87 = next(l for l in lessons if l['id'] == 87)
lesson88 = next(l for l in lessons if l['id'] == 88)
lesson89 = next(l for l in lessons if l['id'] == 89)
lesson90 = next(l for l in lessons if l['id'] == 90)

# Upgrade Lesson 86: Strings & f-Strings
lesson86['fullSolution'] = '''"""
Strings & f-Strings

Master f-strings (formatted string literals) in Python—the modern, fast, and
readable way to format strings. Learn expressions, formatting options, and
advanced patterns. Essential for clean, professional string output.

**Zero Package Installation Required**
"""

# Example 1: Basic f-String Syntax
print("="*70)
print("Example 1: Basic f-String - Variable Interpolation")
print("="*70)

name = "Alice"
age = 30
city = "New York"

# Old way with concatenation
old_way = "My name is " + name + " and I am " + str(age) + " years old."
print(f"Old way: {old_way}")

# Modern f-string
f_string = f"My name is {name} and I am {age} years old."
print(f"f-string: {f_string}")

# Multiple variables
full_intro = f"{name} is {age} years old and lives in {city}."
print(f"Full intro: {full_intro}")
print()

# Example 2: Expressions Inside f-Strings
print("="*70)
print("Example 2: Expressions and Calculations in f-Strings")
print("="*70)

a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")

# String operations
name = "alice"
print(f"\\nOriginal: {name}")
print(f"Uppercase: {name.upper()}")
print(f"Capitalized: {name.capitalize()}")
print(f"Length: {len(name)}")

# Conditional expressions
age = 25
print(f"\\nAge: {age}")
print(f"Status: {('Adult' if age >= 18 else 'Minor')}")
print()

# Example 3: Number Formatting
print("="*70)
print("Example 3: Number Formatting with f-Strings")
print("="*70)

price = 19.99567
large_number = 1234567.89

# Decimal places
print(f"Price: ${price:.2f}")  # 2 decimal places
print(f"Price: ${price:.4f}")  # 4 decimal places

# Thousand separators
print(f"\\nLarge: {large_number:,.2f}")  # Comma separator

# Percentage
ratio = 0.8567
print(f"\\nRatio: {ratio:.2%}")  # As percentage

# Scientific notation
big = 123456789
print(f"Scientific: {big:.2e}")

# Padding with zeros
number = 42
print(f"\\nZero-padded: {number:05d}")  # 00042
print()

# Example 4: Alignment and Padding
print("="*70)
print("Example 4: Text Alignment in f-Strings")
print("="*70)

name = "Alice"
age = 30

# Left align (default for strings)
print(f"|{name:<15}|")  # Left align, width 15

# Right align
print(f"|{name:>15}|")  # Right align, width 15

# Center align
print(f"|{name:^15}|")  # Center, width 15

# With custom fill character
print(f"|{name:*<15}|")  # Left, fill with *
print(f"|{name:->15}|")  # Right, fill with -
print(f"|{name:=^15}|")  # Center, fill with =

# Numbers
print(f"\\n|{age:<10}|")  # Left
print(f"|{age:>10}|")  # Right
print(f"|{age:^10}|")  # Center
print()

# Example 5: Multi-Line f-Strings
print("="*70)
print("Example 5: Multi-Line f-Strings")
print("="*70)

name = "Bob"
age = 25
city = "Boston"
occupation = "Engineer"

# Multi-line f-string
info = f"""
Name: {name}
Age: {age}
City: {city}
Occupation: {occupation}
Status: {('Employed' if occupation else 'Unemployed')}
"""

print(info)

# Building a report
total = 1234.56
tax = total * 0.08

receipt = f"""
{'='*40}
        RECEIPT
{'='*40}
Subtotal:  ${total:>10.2f}
Tax (8%):  ${tax:>10.2f}
{'='*40}
Total:     ${total + tax:>10.2f}
{'='*40}
"""
print(receipt)
print()

# Example 6: Debugging with f-Strings (Python 3.8+)
print("="*70)
print("Example 6: f-String Debug Syntax (= operator)")
print("="*70)

x = 10
y = 20
name = "Alice"

# Debug syntax - shows variable name and value
print(f"{x=}")  # Prints: x=10
print(f"{y=}")  # Prints: y=20
print(f"{x + y=}")  # Prints: x + y=30

print(f"\\n{name=}")
print(f"{name.upper()=}")
print(f"{len(name)=}")
print()

# Example 7: Date and Time Formatting
print("="*70)
print("Example 7: Formatting Dates and Times")
print("="*70)

from datetime import datetime

now = datetime.now()

print(f"Full datetime: {now}")
print(f"Date only: {now:%Y-%m-%d}")
print(f"Time only: {now:%H:%M:%S}")
print(f"Formatted: {now:%B %d, %Y}")  # Month DD, YYYY
print(f"12-hour: {now:%I:%M %p}")

# Custom format
print(f"\\nCustom: {now:%A, %b %d, %Y at %I:%M %p}")

# ISO format
print(f"ISO: {now:%Y-%m-%dT%H:%M:%S}")
print()

# Example 8: Dictionary and List Formatting
print("="*70)
print("Example 8: Formatting Collections")
print("="*70)

person = {"name": "Charlie", "age": 35, "city": "Chicago"}

# Access dict values in f-string
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

# List
numbers = [1, 2, 3, 4, 5]
print(f"\\nNumbers: {numbers}")
print(f"First: {numbers[0]}")
print(f"Last: {numbers[-1]}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")

# Nested access
data = {"user": {"name": "David", "scores": [85, 90, 95]}}
print(f"\\nUser: {data['user']['name']}")
print(f"Best score: {max(data['user']['scores'])}")
print()

# Example 9: Raw f-Strings
print("="*70)
print("Example 9: Raw f-Strings (fr or rf prefix)")
print("="*70)

path = "C:\\\\Users\\\\Alice"

# Regular f-string
print(f"Regular: {path}")

# Raw f-string - treats backslashes as literal
directory = "Users"
filename = "file.txt"
raw_path = fr"C:\\{directory}\\{filename}"
print(f"Raw f-string: {raw_path}")

# Useful for regex patterns
pattern = fr"\\d{{3}}-\\d{{4}}"  # \d{3}-\d{4}
print(f"Regex pattern: {pattern}")
print()

# Example 10: Practical Application - Formatted Tables
print("="*70)
print("Example 10: Real-World Use Case - Generate Report")
print("="*70)

employees = [
    {"name": "Alice Johnson", "id": 1001, "dept": "Engineering", "salary": 85000},
    {"name": "Bob Smith", "id": 1002, "dept": "Design", "salary": 65000},
    {"name": "Charlie Brown", "id": 1003, "dept": "Management", "salary": 95000},
    {"name": "Diana Prince", "id": 1004, "dept": "Marketing", "salary": 70000}
]

# Build formatted report
width = 75
print("="*width)
print(f"{'EMPLOYEE REPORT':^{width}}")
print("="*width)
print()

# Header
print(f"{'ID':<6} {'Name':<20} {'Department':<15} {'Salary':>12}")
print("-"*width)

# Data rows
total_salary = 0
for emp in employees:
    print(f"{emp['id']:<6} {emp['name']:<20} {emp['dept']:<15} ${emp['salary']:>11,}")
    total_salary += emp['salary']

# Footer
print("="*width)
print(f"{'Total Payroll:':<42} ${total_salary:>11,}")
print(f"{'Average Salary:':<42} ${total_salary / len(employees):>11,.2f}")
print("="*width)

# Generate email for each employee
print("\\nGenerated emails:")
for emp in employees:
    email = f"""
To: {emp['name']} <{emp['name'].lower().replace(' ', '.')}@company.com>
Subject: Salary Confirmation

Dear {emp['name'].split()[0]},

Your current salary: ${emp['salary']:,}
Department: {emp['dept']}
Employee ID: {emp['id']}

Thank you for your continued service.
    """.strip()

    print(email)
    print("-"*width)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. f'text {variable}' - Basic f-string syntax")
print("2. f'{expression}' - Execute Python expressions")
print("3. f'{value:.2f}' - Format to 2 decimal places")
print("4. f'{value:,}' - Thousand separator")
print("5. f'{value:<10}' / f'{value:>10}' - Alignment")
print("6. f'{value=}' - Debug syntax (Python 3.8+)")
print("7. f'{date:%Y-%m-%d}' - Date formatting")
print("8. f-strings support multiline with triple quotes")
print("9. fr'raw \\\\path' - Raw f-strings")
print("10. Fastest and most readable formatting method")
print("="*70)
'''

# Upgrade Lesson 87: Accessing Dictionary Values
lesson87['fullSolution'] = '''"""
Accessing Dictionary Values

Master techniques to access dictionary values in Python—using keys,
get() method, handling missing keys, and nested dictionaries. Essential
for data retrieval and manipulation.

**Zero Package Installation Required**
"""

# Example 1: Basic Dictionary Access with []
print("="*70)
print("Example 1: Accessing Values with Square Brackets")
print("="*70)

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}

print(f"Dictionary: {person}")
print()

# Access individual values
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
print(f"Occupation: {person['occupation']}")
print()

# Example 2: KeyError When Key Doesn't Exist
print("="*70)
print("Example 2: Handling Missing Keys - KeyError")
print("="*70)

person = {"name": "Bob", "age": 25}
print(f"Dictionary: {person}")

# Successful access
print(f"\\nName: {person['name']}")

# This raises KeyError
print("\\nAttempting to access 'city':")
try:
    print(f"City: {person['city']}")
except KeyError as e:
    print(f"KeyError: {e}")
    print("Key 'city' does not exist!")
print()

# Example 3: get() Method - Safe Access
print("="*70)
print("Example 3: get() Method - No Exception")
print("="*70)

person = {"name": "Charlie", "age": 35}
print(f"Dictionary: {person}")

# get() returns None if key doesn't exist
city = person.get("city")
print(f"\\nCity: {city}")  # None
print(f"Type: {type(city)}")

# get() with existing key
name = person.get("name")
print(f"\\nName: {name}")

# Can safely use in conditionals
if person.get("city"):
    print("Has city")
else:
    print("No city specified")
print()

# Example 4: get() with Default Values
print("="*70)
print("Example 4: get() with Custom Default Value")
print("="*70)

person = {"name": "David", "age": 28}
print(f"Dictionary: {person}")

# Provide default value
city = person.get("city", "Unknown")
print(f"\\nCity: {city}")

country = person.get("country", "USA")
print(f"Country: {country}")

# More examples
score = person.get("score", 0)
print(f"Score: {score}")

active = person.get("active", True)
print(f"Active: {active}")
print()

# Example 5: Accessing Nested Dictionaries
print("="*70)
print("Example 5: Nested Dictionary Access")
print("="*70)

user = {
    "name": "Eve",
    "contact": {
        "email": "eve@example.com",
        "phone": "555-1234"
    },
    "address": {
        "street": "123 Main St",
        "city": "Boston",
        "zip": "02101"
    }
}

print("Nested dictionary:")
print(user)

# Access nested values
print(f"\\nEmail: {user['contact']['email']}")
print(f"Phone: {user['contact']['phone']}")
print(f"City: {user['address']['city']}")
print(f"ZIP: {user['address']['zip']}")

# Safe access with get()
country = user.get("address", {}).get("country", "USA")
print(f"\\nCountry (with default): {country}")
print()

# Example 6: Accessing Dictionary in Loops
print("="*70)
print("Example 6: Iterating and Accessing Values")
print("="*70)

scores = {
    "Math": 95,
    "Science": 88,
    "English": 92,
    "History": 85
}

print("Scores:")
for subject in scores:
    score = scores[subject]
    print(f"  {subject}: {score}")

# Calculate average
print(f"\\nAverage: {sum(scores.values()) / len(scores):.2f}")
print()

# Example 7: Using Dictionary with values()
print("="*70)
print("Example 7: values() Method - Get All Values")
print("="*70)

product = {
    "name": "Laptop",
    "price": 999.99,
    "stock": 15,
    "category": "Electronics"
}

print(f"Dictionary: {product}")

# Get all values
all_values = product.values()
print(f"\\nAll values: {all_values}")
print(f"Type: {type(all_values)}")

# Convert to list
values_list = list(product.values())
print(f"As list: {values_list}")

# Iterate over values
print("\\nValues:")
for value in product.values():
    print(f"  {value}")
print()

# Example 8: Multiple Ways to Access
print("="*70)
print("Example 8: Comparison of Access Methods")
print("="*70)

data = {"x": 10, "y": 20}
print(f"Dictionary: {data}")

# Method 1: Direct access with []
try:
    value1 = data["x"]
    print(f"\\nMethod 1 ([]): x = {value1}")

    value2 = data["z"]  # Raises KeyError
except KeyError:
    print("Method 1: KeyError for missing key")

# Method 2: get() with default
value3 = data.get("x")
print(f"\\nMethod 2 (get): x = {value3}")

value4 = data.get("z")
print(f"Method 2 (get): z = {value4}")  # None

value5 = data.get("z", 0)
print(f"Method 2 (get with default): z = {value5}")  # 0

# When to use which
print("\\nUse [] when:")
print("  - You KNOW the key exists")
print("  - You WANT an exception if key is missing")
print("\\nUse get() when:")
print("  - Key might not exist")
print("  - You want a default value")
print("  - You want to avoid try/except")
print()

# Example 9: Dynamic Key Access
print("="*70)
print("Example 9: Access Keys Dynamically")
print("="*70)

settings = {
    "theme": "dark",
    "language": "en",
    "notifications": True,
    "volume": 75
}

# User chooses which setting to view
print("Available settings:")
for key in settings:
    print(f"  - {key}")

# Access based on variable
key_to_access = "theme"
value = settings[key_to_access]
print(f"\\n{key_to_access}: {value}")

# Multiple dynamic accesses
keys_to_get = ["theme", "volume", "missing_key"]
print("\\nDynamic access:")
for key in keys_to_get:
    value = settings.get(key, "Not set")
    print(f"  {key}: {value}")
print()

# Example 10: Practical Application - User Profile
print("="*70)
print("Example 10: Real-World Use Case - Display User Profile")
print("="*70)

user_profile = {
    "username": "alice_coder",
    "email": "alice@example.com",
    "name": "Alice Johnson",
    "bio": "Software engineer passionate about Python",
    "location": "San Francisco, CA",
    "verified": True
}

# Display profile with proper formatting
print("="*60)
print("USER PROFILE".center(60))
print("="*60)

# Required fields
print(f"Username: @{user_profile['username']}")
print(f"Name: {user_profile['name']}")
print(f"Email: {user_profile['email']}")

# Optional fields with get()
print(f"\\nBio: {user_profile.get('bio', 'No bio provided')}")
print(f"Location: {user_profile.get('location', 'Not specified')}")
print(f"Website: {user_profile.get('website', 'Not provided')}")

# Boolean field
verified_badge = "✓ Verified" if user_profile.get("verified") else "Not verified"
print(f"\\nStatus: {verified_badge}")

# Stats (with defaults)
followers = user_profile.get("followers", 0)
following = user_profile.get("following", 0)
posts = user_profile.get("posts", 0)

print(f"\\nStats:")
print(f"  Posts: {posts}")
print(f"  Followers: {followers}")
print(f"  Following: {following}")
print("="*60)

# Safe navigation through potentially missing data
preferences = user_profile.get("preferences", {})
theme = preferences.get("theme", "light")
notifications = preferences.get("notifications", True)

print(f"\\nPreferences:")
print(f"  Theme: {theme}")
print(f"  Notifications: {('Enabled' if notifications else 'Disabled')}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. dict[key] - Direct access, raises KeyError if missing")
print("2. dict.get(key) - Returns None if key doesn't exist")
print("3. dict.get(key, default) - Returns default if missing")
print("4. dict.values() - Get all values")
print("5. Nested: dict[key1][key2] - Access nested values")
print("6. Safe nested: dict.get(k1, {}).get(k2, default)")
print("7. Use [] when you expect key to exist")
print("8. Use get() to avoid KeyError exceptions")
print("9. get() is safer for user input or API responses")
print("10. Always handle missing keys gracefully")
print("="*70)
'''

# Continue with lessons 88-90...
# (Due to length, I'll create the remaining lessons in the same comprehensive style)

lesson88['fullSolution'] = '''"""
Adding to Dictionaries

Master techniques to add key-value pairs to dictionaries in Python—
assignment, update(), setdefault(), and merge operations. Essential
for building and modifying data structures.

**Zero Package Installation Required**
"""

# Example 1: Adding with Assignment
print("="*70)
print("Example 1: Add Key-Value Pairs with Assignment")
print("="*70)

person = {"name": "Alice", "age": 30}
print(f"Original: {person}")

# Add new key-value pair
person["city"] = "New York"
print(f"After adding city: {person}")

# Add another
person["occupation"] = "Engineer"
print(f"After adding occupation: {person}")

# Add multiple one by one
person["email"] = "alice@example.com"
person["phone"] = "555-1234"
print(f"\\nFinal: {person}")
print()

# Example 2: Updating Existing vs Adding New
print("="*70)
print("Example 2: Assignment Updates if Key Exists")
print("="*70)

settings = {"theme": "light", "volume": 50}
print(f"Original: {settings}")

# Add new key
settings["notifications"] = True
print(f"Add new key: {settings}")

# Update existing key
settings["volume"] = 75
print(f"Update existing: {settings}")

# Can't tell if key existed before
settings["language"] = "en"  # New
settings["theme"] = "dark"   # Update
print(f"\\nFinal: {settings}")
print()

# Example 3: update() Method - Add Multiple Items
print("="*70)
print("Example 3: update() - Add/Update Multiple Keys")
print("="*70)

user = {"name": "Bob", "age": 25}
print(f"Original: {user}")

# Update with another dictionary
new_data = {"city": "Boston", "email": "bob@example.com"}
user.update(new_data)
print(f"\\nAfter update: {user}")

# Update with keyword arguments
user.update(occupation="Designer", phone="555-5678")
print(f"With kwargs: {user}")

# Update can mix new and existing
user.update({"age": 26, "verified": True})  # age exists, verified is new
print(f"\\nMixed update: {user}")
print()

# Example 4: setdefault() - Add Only if Missing
print("="*70)
print("Example 4: setdefault() - Add If Key Doesn't Exist")
print("="*70)

config = {"host": "localhost", "port": 8080}
print(f"Original: {config}")

# Add new key with setdefault
timeout = config.setdefault("timeout", 30)
print(f"\\nsetdefault('timeout', 30): {timeout}")
print(f"Config: {config}")

# Try to set existing key - does nothing
port = config.setdefault("port", 3000)
print(f"\\nsetdefault('port', 3000): {port}")
print(f"Port unchanged: {config}")

# Multiple setdefaults
config.setdefault("debug", False)
config.setdefault("ssl", True)
print(f"\\nFinal config: {config}")
print()

# Example 5: Dictionary Merge with | Operator (Python 3.9+)
print("="*70)
print("Example 5: Merge Dictionaries with | Operator")
print("="*70)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

print(f"Dict 1: {dict1}")
print(f"Dict 2: {dict2}")

# Merge - creates new dictionary
merged = dict1 | dict2
print(f"\\nMerged (|): {merged}")

# Original dictionaries unchanged
print(f"Dict 1 still: {dict1}")

# Later values override earlier ones
dict3 = {"b": 20, "e": 5}
merged2 = dict1 | dict3
print(f"\\nWith overlap: {merged2}")  # b is 20, not 2
print()

# Example 6: In-Place Update with |= (Python 3.9+)
print("="*70)
print("Example 6: In-Place Merge with |= Operator")
print("="*70)

base = {"x": 10, "y": 20}
additions = {"z": 30, "w": 40}

print(f"Base: {base}")
print(f"Additions: {additions}")

# In-place merge
base |= additions
print(f"\\nAfter |=: {base}")

# Can chain
base |= {"a": 1, "b": 2}
print(f"After another |=: {base}")
print()

# Example 7: Adding Nested Dictionaries
print("="*70)
print("Example 7: Adding Nested Structures")
print("="*70)

user = {
    "name": "Charlie",
    "age": 35
}

print(f"Original: {user}")

# Add nested dictionary
user["address"] = {
    "street": "123 Main St",
    "city": "Chicago",
    "zip": "60601"
}

print(f"\\nWith address: {user}")

# Add another nested dict
user["preferences"] = {
    "theme": "dark",
    "notifications": True
}

print(f"\\nWith preferences:")
for key, value in user.items():
    print(f"  {key}: {value}")
print()

# Example 8: Conditional Adding
print("="*70)
print("Example 8: Add Key-Value Conditionally")
print("="*70)

data = {"status": "active"}
print(f"Original: {data}")

# Add only if condition is true
user_input = "alice@example.com"
if "@" in user_input:
    data["email"] = user_input
    print(f"Added email: {data}")

# Add based on variable
include_timestamp = True
if include_timestamp:
    from datetime import datetime
    data["timestamp"] = datetime.now().isoformat()
    print(f"Added timestamp: {data}")

# Add non-empty values only
def add_if_not_empty(dict_obj, key, value):
    """Add to dictionary only if value is not empty"""
    if value:
        dict_obj[key] = value

add_if_not_empty(data, "name", "Alice")
add_if_not_empty(data, "bio", "")  # Won't add
print(f"\\nFinal: {data}")
print()

# Example 9: Building Dictionary Incrementally
print("="*70)
print("Example 9: Build Dictionary Step by Step")
print("="*70)

# Start empty
employee = {}
print(f"Start: {employee}")

# Add required fields
employee["id"] = 1001
employee["name"] = "Diana Prince"
employee["department"] = "Marketing"
print(f"\\nRequired fields: {employee}")

# Add optional fields
employee["email"] = "diana@company.com"
employee["phone"] = "555-9999"
print(f"With contact: {employee}")

# Add computed fields
employee["full_name"] = employee["name"]
employee["username"] = employee["name"].lower().replace(" ", ".")
print(f"\\nWith computed fields: {employee}")

# Add metadata
employee["created"] = "2024-01-15"
employee["active"] = True
print(f"Final employee: {employee}")
print()

# Example 10: Practical Application - Build Configuration
print("="*70)
print("Example 10: Real-World Use Case - Application Config")
print("="*70)

# Build configuration from multiple sources
config = {}

# Step 1: Add defaults
defaults = {
    "host": "localhost",
    "port": 8080,
    "debug": False,
    "timeout": 30
}
config.update(defaults)
print("After defaults:")
print(config)

# Step 2: Add environment-specific settings
environment = "production"
if environment == "production":
    config["debug"] = False
    config["host"] = "prod.example.com"
    config["ssl"] = True
elif environment == "development":
    config["debug"] = True
    config["hot_reload"] = True

print(f"\\nAfter environment ({environment}):")
print(config)

# Step 3: Add optional features
features = ["logging", "caching", "monitoring"]
for feature in features:
    config[f"{feature}_enabled"] = True

print("\\nAfter features:")
print(config)

# Step 4: Add user preferences (only if not already set)
user_prefs = {
    "theme": "dark",
    "port": 9000,  # Won't override existing
    "language": "en"
}

for key, value in user_prefs.items():
    config.setdefault(key, value)

print("\\nFinal configuration:")
for key, value in sorted(config.items()):
    print(f"  {key}: {value}")

# Export config
print("\\n" + "="*60)
print("CONFIGURATION SUMMARY".center(60))
print("="*60)
print(f"Environment: {environment}")
print(f"Server: {config['host']}:{config['port']}")
print(f"Debug mode: {('Enabled' if config['debug'] else 'Disabled')}")
print(f"SSL: {('Enabled' if config.get('ssl') else 'Disabled')}")
print(f"Features: {', '.join([k.replace('_enabled', '') for k in config if k.endswith('_enabled')])}")
print("="*60)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. dict[key] = value - Add or update single key")
print("2. dict.update(other) - Add/update multiple keys")
print("3. dict.update(key=value) - Add with keyword args")
print("4. dict.setdefault(key, default) - Add only if missing")
print("5. dict1 | dict2 - Merge (Python 3.9+, new dict)")
print("6. dict1 |= dict2 - In-place merge (Python 3.9+)")
print("7. Assignment always succeeds (adds or updates)")
print("8. update() can take dict or keyword arguments")
print("9. setdefault() useful for default values")
print("10. Build dictionaries incrementally as needed")
print("="*70)
'''

lesson89['fullSolution'] = '''"""
Checking Dictionary Keys

Master techniques to check for key existence in dictionaries—using in
operator, get(), keys() method, and handling edge cases. Essential for
safe dictionary operations and data validation.

**Zero Package Installation Required**
"""

# Example 1: in Operator - Check Key Existence
print("="*70)
print("Example 1: Check if Key Exists with 'in'")
print("="*70)

person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Dictionary: {person}")

# Check if key exists
if "name" in person:
    print("\\n'name' exists")

if "email" in person:
    print("'email' exists")
else:
    print("'email' does NOT exist")

# Multiple checks
keys_to_check = ["name", "age", "phone", "city"]
print("\\nKey existence:")
for key in keys_to_check:
    exists = key in person
    status = "✓" if exists else "✗"
    print(f"  {status} {key}: {exists}")
print()

# Example 2: not in Operator
print("="*70)
print("Example 2: Check if Key Does NOT Exist")
print("="*70)

user = {"username": "alice123", "email": "alice@example.com"}
print(f"User: {user}")

# Check for missing keys
if "password" not in user:
    print("\\nPassword not stored (good!)")

if "phone" not in user:
    print("Phone number missing")
    user["phone"] = "Not provided"
    print(f"Added default: {user}")
print()

# Example 3: keys() Method - Get All Keys
print("="*70)
print("Example 3: keys() Method - View All Keys")
print("="*70)

product = {
    "name": "Laptop",
    "price": 999.99,
    "stock": 15,
    "category": "Electronics"
}

print(f"Product: {product}")

# Get all keys
all_keys = product.keys()
print(f"\\nAll keys: {all_keys}")
print(f"Type: {type(all_keys)}")

# Convert to list
keys_list = list(product.keys())
print(f"As list: {keys_list}")

# Iterate over keys
print("\\nKeys:")
for key in product.keys():
    print(f"  - {key}")
print()

# Example 4: Check Before Access
print("="*70)
print("Example 4: Safe Access Pattern - Check Then Access")
print("="*70)

settings = {"theme": "dark", "volume": 75}
print(f"Settings: {settings}")

# Pattern 1: Check with if/in
if "theme" in settings:
    theme = settings["theme"]
    print(f"\\nTheme: {theme}")

if "language" in settings:
    language = settings["language"]
    print(f"Language: {language}")
else:
    print("Language not set")

# Pattern 2: Use get() instead
language = settings.get("language", "en")
print(f"\\nLanguage (with get): {language}")
print()

# Example 5: Checking Multiple Keys
print("="*70)
print("Example 5: Check for Multiple Required Keys")
print("="*70)

user_data = {
    "username": "bob123",
    "email": "bob@example.com",
    "age": 25
}

# Required keys for registration
required_keys = ["username", "email", "password"]

print(f"User data: {user_data}")
print(f"Required keys: {required_keys}")

# Check all required keys exist
missing_keys = []
for key in required_keys:
    if key not in user_data:
        missing_keys.append(key)

if missing_keys:
    print(f"\\nMissing required keys: {missing_keys}")
else:
    print("\\nAll required keys present!")

# More elegant with list comprehension
missing = [k for k in required_keys if k not in user_data]
print(f"Missing (list comp): {missing}")

# Check if ALL keys exist
all_present = all(k in user_data for k in required_keys)
print(f"All present: {all_present}")
print()

# Example 6: Checking Nested Keys
print("="*70)
print("Example 6: Check Keys in Nested Dictionaries")
print("="*70)

data = {
    "user": {
        "name": "Charlie",
        "contact": {
            "email": "charlie@example.com"
        }
    }
}

print("Nested data:")
print(data)

# Check nested keys exist
if "user" in data:
    print("\\n'user' key exists")

    if "contact" in data["user"]:
        print("'user.contact' exists")

        if "email" in data["user"]["contact"]:
            email = data["user"]["contact"]["email"]
            print(f"Email: {email}")

# Safe navigation with get()
email = data.get("user", {}).get("contact", {}).get("email")
phone = data.get("user", {}).get("contact", {}).get("phone")
print(f"\\nEmail (safe): {email}")
print(f"Phone (safe): {phone}")
print()

# Example 7: Checking with Any/All
print("="*70)
print("Example 7: any() and all() with Key Checks")
print("="*70)

permissions = {
    "read": True,
    "write": False,
    "delete": False,
    "admin": False
}

print(f"Permissions: {permissions}")

# Check if user has ANY dangerous permission
dangerous = ["delete", "admin"]
has_dangerous = any(permissions.get(p) for p in dangerous)
print(f"\\nHas dangerous permission: {has_dangerous}")

# Check if ALL basic permissions exist
basic = ["read", "write"]
all_basic_exist = all(p in permissions for p in basic)
print(f"All basic permissions defined: {all_basic_exist}")

# Check if user has ALL basic permissions enabled
all_basic_enabled = all(permissions.get(p) for p in basic)
print(f"All basic permissions enabled: {all_basic_enabled}")
print()

# Example 8: Key Validation Function
print("="*70)
print("Example 8: Create Key Validation Helper")
print("="*70)

def validate_keys(data, required=None, optional=None):
    """Validate dictionary has required keys and only allowed keys"""
    required = required or []
    optional = optional or []

    errors = []

    # Check required keys
    missing = [k for k in required if k not in data]
    if missing:
        errors.append(f"Missing required keys: {missing}")

    # Check for unexpected keys
    allowed = set(required + optional)
    unexpected = [k for k in data if k not in allowed]
    if unexpected:
        errors.append(f"Unexpected keys: {unexpected}")

    return len(errors) == 0, errors

# Test validation
user1 = {"username": "alice", "email": "alice@example.com", "age": 30}
user2 = {"username": "bob"}
user3 = {"username": "charlie", "email": "c@example.com", "hacker": True}

print("Validating user data:")
for i, user in enumerate([user1, user2, user3], 1):
    valid, errors = validate_keys(
        user,
        required=["username", "email"],
        optional=["age", "phone"]
    )

    print(f"\\nUser {i}: {user}")
    if valid:
        print("  ✓ VALID")
    else:
        print("  ✗ INVALID")
        for error in errors:
            print(f"    - {error}")
print()

# Example 9: Dynamic Key Checking
print("="*70)
print("Example 9: Check Keys Based on Conditions")
print("="*70)

order = {
    "id": 12345,
    "items": ["laptop", "mouse"],
    "total": 1029.98,
    "payment_method": "credit_card"
}

print(f"Order: {order}")

# Check different keys based on payment method
payment_method = order.get("payment_method")

if payment_method == "credit_card":
    required_keys = ["card_number", "cvv", "expiry"]
elif payment_method == "paypal":
    required_keys = ["paypal_email"]
else:
    required_keys = []

print(f"\\nPayment method: {payment_method}")
print(f"Required payment keys: {required_keys}")

missing = [k for k in required_keys if k not in order]
if missing:
    print(f"Missing payment info: {missing}")
else:
    print("All payment info present")
print()

# Example 10: Practical Application - Form Validation
print("="*70)
print("Example 10: Real-World Use Case - Validate Form Submission")
print("="*70)

def validate_registration_form(form):
    """Comprehensive form validation"""
    errors = []

    # Required fields
    required = ["username", "email", "password", "age"]
    missing = [f for f in required if f not in form]
    if missing:
        errors.append(f"Required fields missing: {', '.join(missing)}")

    # Username validation (if present)
    if "username" in form:
        username = form["username"]
        if len(username) < 3:
            errors.append("Username too short (min 3 chars)")

    # Email validation (if present)
    if "email" in form:
        email = form["email"]
        if "@" not in email:
            errors.append("Invalid email format")

    # Password validation (if present)
    if "password" in form:
        password = form["password"]
        if len(password) < 8:
            errors.append("Password too short (min 8 chars)")

    # Age validation (if present)
    if "age" in form:
        try:
            age = int(form["age"])
            if age < 18:
                errors.append("Must be 18 or older")
        except ValueError:
            errors.append("Age must be a number")

    # Check for suspicious keys
    allowed = ["username", "email", "password", "age", "phone", "bio"]
    suspicious = [k for k in form if k not in allowed]
    if suspicious:
        errors.append(f"Unexpected fields: {', '.join(suspicious)}")

    return len(errors) == 0, errors

# Test forms
test_forms = [
    {
        "username": "alice_coder",
        "email": "alice@example.com",
        "password": "SecurePass123",
        "age": "25"
    },
    {
        "username": "ab",  # Too short
        "email": "invalid",  # No @
        "password": "short",  # Too short
        "age": "17"  # Too young
    },
    {
        "username": "bob",
        "age": "30"
        # Missing email and password
    },
    {
        "username": "charlie",
        "email": "charlie@example.com",
        "password": "GoodPassword123",
        "age": "28",
        "admin": True  # Suspicious
    }
]

print("Form Validation Results:")
print("="*70)

for i, form in enumerate(test_forms, 1):
    print(f"\\nForm {i}:")
    print(f"Data: {form}")

    valid, errors = validate_registration_form(form)

    if valid:
        print("✓ VALID - Registration accepted")
    else:
        print("✗ INVALID - Registration rejected")
        for error in errors:
            print(f"  - {error}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. 'key' in dict - Check if key exists (returns bool)")
print("2. 'key' not in dict - Check if key doesn't exist")
print("3. dict.keys() - Get view of all keys")
print("4. Check before access to avoid KeyError")
print("5. Or use dict.get(key) for safe access")
print("6. list(dict.keys()) - Convert keys to list")
print("7. all(k in dict for k in keys) - Check all keys exist")
print("8. any(k in dict for k in keys) - Check any key exists")
print("9. Validate nested keys with get() chaining")
print("10. Essential for form validation and API responses")
print("="*70)
'''

lesson90['fullSolution'] = '''"""
Creating Dictionaries

Master all techniques for creating dictionaries in Python—literals,
dict() constructor, comprehensions, fromkeys(), and advanced patterns.
Essential for data structure initialization and manipulation.

**Zero Package Installation Required**
"""

# Example 1: Dictionary Literal - Most Common Method
print("="*70)
print("Example 1: Create Dictionary with Literal Syntax")
print("="*70)

# Empty dictionary
empty = {}
print(f"Empty: {empty}")
print(f"Type: {type(empty)}")

# With initial key-value pairs
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"\\nPerson: {person}")

# Different value types
mixed = {
    "string": "hello",
    "number": 42,
    "float": 3.14,
    "boolean": True,
    "list": [1, 2, 3],
    "nested": {"key": "value"}
}
print(f"\\nMixed types: {mixed}")
print()

# Example 2: dict() Constructor
print("="*70)
print("Example 2: Create Dictionary with dict() Constructor")
print("="*70)

# Empty
empty = dict()
print(f"Empty with dict(): {empty}")

# From keyword arguments
person = dict(name="Bob", age=25, city="Boston")
print(f"\\nWith kwargs: {person}")

# From list of tuples
pairs = [("x", 10), ("y", 20), ("z", 30)]
coords = dict(pairs)
print(f"\\nFrom tuples: {coords}")

# From list of lists
lists = [["a", 1], ["b", 2], ["c", 3]]
letters = dict(lists)
print(f"From lists: {letters}")
print()

# Example 3: Dictionary Comprehension
print("="*70)
print("Example 3: Create Dictionary with Comprehension")
print("="*70)

# Square numbers
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# From two lists
keys = ["name", "age", "city"]
values = ["Charlie", 35, "Chicago"]
combined = {k: v for k, v in zip(keys, values)}
print(f"\\nFrom zip: {combined}")

# With condition
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"\\nEven squares: {evens}")

# Transform strings
fruits = ["apple", "banana", "cherry"]
lengths = {fruit: len(fruit) for fruit in fruits}
print(f"\\nFruit lengths: {lengths}")
print()

# Example 4: fromkeys() Method
print("="*70)
print("Example 4: Create Dictionary with fromkeys()")
print("="*70)

# Create dict with same value for all keys
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(f"Keys {keys} with value 0:")
print(default_dict)

# Without value (defaults to None)
none_dict = dict.fromkeys(["x", "y", "z"])
print(f"\\nWith default None: {none_dict}")

# Useful for initialization
settings = dict.fromkeys(["theme", "language", "notifications"], "default")
print(f"\\nDefault settings: {settings}")
print()

# Example 5: Creating from Sequences
print("="*70)
print("Example 5: Create from Various Sequences")
print("="*70)

# From string (characters as keys)
char_dict = dict.fromkeys("hello", 0)
print(f"From string 'hello': {char_dict}")

# From range
range_dict = {i: i*10 for i in range(5)}
print(f"\\nFrom range(5): {range_dict}")

# From enumerate
items = ["apple", "banana", "cherry"]
indexed = {i: item for i, item in enumerate(items)}
print(f"\\nEnumerated items: {indexed}")

# Reverse (item as key, index as value)
reverse_indexed = {item: i for i, item in enumerate(items)}
print(f"Reverse indexed: {reverse_indexed}")
print()

# Example 6: Nested Dictionary Creation
print("="*70)
print("Example 6: Create Nested Dictionaries")
print("="*70)

# Nested literal
user = {
    "name": "David",
    "contact": {
        "email": "david@example.com",
        "phone": "555-1234"
    },
    "preferences": {
        "theme": "dark",
        "notifications": True
    }
}

print("Nested dictionary:")
for key, value in user.items():
    print(f"  {key}: {value}")

# Build nested incrementally
company = {}
company["name"] = "TechCorp"
company["employees"] = {
    "engineering": 50,
    "sales": 20,
    "marketing": 15
}
company["locations"] = {
    "HQ": "San Francisco",
    "Branch": "New York"
}

print(f"\\nCompany: {company}")
print()

# Example 7: Dictionary from Two Lists with zip()
print("="*70)
print("Example 7: Combine Lists into Dictionary")
print("="*70)

# Parallel lists
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]

# Zip and convert
people_ages = dict(zip(names, ages))
print(f"Names: {names}")
print(f"Ages: {ages}")
print(f"Combined: {people_ages}")

# More complex
products = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 29.99, 79.99]
stock = [10, 50, 30]

# Create nested
inventory = {
    product: {"price": price, "stock": qty}
    for product, price, qty in zip(products, prices, stock)
}

print(f"\\nInventory:")
for item, details in inventory.items():
    print(f"  {item}: {details}")
print()

# Example 8: Copy vs Reference
print("="*70)
print("Example 8: Creating Copies of Dictionaries")
print("="*70)

original = {"a": 1, "b": 2}
print(f"Original: {original}")

# Reference (not a copy!)
reference = original
reference["c"] = 3
print(f"\\nAfter modifying reference:")
print(f"Original: {original}")  # Changed!
print(f"Reference: {reference}")

# Shallow copy
original2 = {"x": 10, "y": 20}
shallow = original2.copy()
shallow["z"] = 30
print(f"\\nAfter modifying shallow copy:")
print(f"Original2: {original2}")  # Unchanged
print(f"Shallow: {shallow}")

# Using dict()
copy2 = dict(original2)
print(f"\\nUsing dict(): {copy2}")
print()

# Example 9: Merging Multiple Dictionaries
print("="*70)
print("Example 9: Combine Multiple Dictionaries")
print("="*70)

defaults = {"theme": "light", "volume": 50, "notifications": True}
user_prefs = {"theme": "dark", "language": "en"}
session = {"user_id": 12345}

# Method 1: update() (modifies first dict)
config = {}
config.update(defaults)
config.update(user_prefs)
config.update(session)
print("Method 1 (update):")
print(config)

# Method 2: dict unpacking
config2 = {**defaults, **user_prefs, **session}
print(f"\\nMethod 2 (unpacking):")
print(config2)

# Method 3: | operator (Python 3.9+)
config3 = defaults | user_prefs | session
print(f"\\nMethod 3 (| operator):")
print(config3)
print()

# Example 10: Practical Application - Data Transformation
print("="*70)
print("Example 10: Real-World Use Case - Process CSV Data")
print("="*70)

# Simulate CSV data
csv_rows = [
    "Alice,30,Engineering,85000",
    "Bob,25,Design,65000",
    "Charlie,35,Management,95000",
    "Diana,28,Marketing,70000"
]

headers = ["name", "age", "department", "salary"]

print("Raw CSV data:")
for row in csv_rows:
    print(f"  {row}")

# Transform each row into dictionary
employees = []
for row in csv_rows:
    values = row.split(",")
    employee = dict(zip(headers, values))

    # Convert types
    employee["age"] = int(employee["age"])
    employee["salary"] = int(employee["salary"])

    employees.append(employee)

print("\\nParsed employees:")
for emp in employees:
    print(f"  {emp}")

# Create lookup dictionary (name → employee)
employee_lookup = {emp["name"]: emp for emp in employees}

print("\\nEmployee lookup:")
print(employee_lookup)

# Create department summary
dept_summary = {}
for emp in employees:
    dept = emp["department"]
    if dept not in dept_summary:
        dept_summary[dept] = {
            "count": 0,
            "total_salary": 0
        }

    dept_summary[dept]["count"] += 1
    dept_summary[dept]["total_salary"] += emp["salary"]

print("\\nDepartment Summary:")
for dept, stats in dept_summary.items():
    avg_salary = stats["total_salary"] / stats["count"]
    print(f"  {dept}:")
    print(f"    Employees: {stats['count']}")
    print(f"    Total Salary: ${stats['total_salary']:,}")
    print(f"    Avg Salary: ${avg_salary:,.2f}")

# Build formatted report
print("\\n" + "="*70)
print("EMPLOYEE REPORT".center(70))
print("="*70)

for emp in employees:
    print(f"Name: {emp['name']:<15} Age: {emp['age']:<3} "
          f"Dept: {emp['department']:<15} Salary: ${emp['salary']:,}")

print("="*70)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. {} - Create empty or literal dictionary")
print("2. dict() - Constructor, from kwargs or pairs")
print("3. {k: v for ...} - Dictionary comprehension")
print("4. dict.fromkeys(keys, value) - Same value for all keys")
print("5. dict(zip(keys, vals)) - From two sequences")
print("6. dict.copy() - Create shallow copy")
print("7. {**d1, **d2} - Merge dictionaries (unpacking)")
print("8. d1 | d2 - Merge operator (Python 3.9+)")
print("9. Assignment creates reference, not copy")
print("10. Choose method based on data source and use case")
print("="*70)
'''

# Save the updated lessons
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Print summary
print("\nUpgraded lessons 86-90:")
print(f"  86: Strings & f-Strings - {len(lesson86['fullSolution'])} chars")
print(f"  87: Accessing Dictionary Values - {len(lesson87['fullSolution'])} chars")
print(f"  88: Adding to Dictionaries - {len(lesson88['fullSolution'])} chars")
print(f"  89: Checking Dictionary Keys - {len(lesson89['fullSolution'])} chars")
print(f"  90: Creating Dictionaries - {len(lesson90['fullSolution'])} chars")
print("\nBatch 86-90 complete!")
