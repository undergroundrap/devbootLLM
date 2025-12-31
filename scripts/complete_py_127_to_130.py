#!/usr/bin/env python3
"""
Complete Python lessons 127-130 with comprehensive content.
- Lesson 127: Validation Functions
- Lesson 128: Zip Function
- Lesson 129: __str__ Method
- Lesson 130: Class vs Instance Attributes
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 127-130
lesson127 = next(l for l in lessons if l['id'] == 127)
lesson128 = next(l for l in lessons if l['id'] == 128)
lesson129 = next(l for l in lessons if l['id'] == 129)
lesson130 = next(l for l in lessons if l['id'] == 130)

# Upgrade Lesson 127: Validation Functions
lesson127['fullSolution'] = '''"""
Validation Functions

Master input validation functions in Python. Learn to validate data types,
ranges, formats, and business rules. Build robust validation systems that
ensure data integrity and prevent errors. Essential for production applications.

**Zero Package Installation Required**
"""

# Example 1: Basic Type Validation
print("="*70)
print("Example 1: Type Validation Functions")
print("="*70)

def is_string(value):
    """Check if value is a string"""
    return isinstance(value, str)

def is_number(value):
    """Check if value is a number (int or float)"""
    return isinstance(value, (int, float))

def is_integer(value):
    """Check if value is an integer"""
    return isinstance(value, int)

def is_list(value):
    """Check if value is a list"""
    return isinstance(value, list)

# Test type validation
test_values = ["hello", 42, 3.14, [1, 2, 3], True, None]

print("Type validation:")
for val in test_values:
    print(f"  {val!r:15} - string: {is_string(val)}, number: {is_number(val)}, "
          f"int: {is_integer(val)}, list: {is_list(val)}")
print()

# Example 2: Range Validation
print("="*70)
print("Example 2: Range Validation Functions")
print("="*70)

def is_in_range(value, min_val, max_val):
    """Check if value is within range"""
    return min_val <= value <= max_val

def is_positive(value):
    """Check if value is positive"""
    return value > 0

def is_non_negative(value):
    """Check if value is non-negative (>= 0)"""
    return value >= 0

def is_percentage(value):
    """Check if value is a valid percentage (0-100)"""
    return 0 <= value <= 100

# Test range validation
print("Range validation:")
print(f"  is_in_range(50, 0, 100): {is_in_range(50, 0, 100)}")
print(f"  is_in_range(150, 0, 100): {is_in_range(150, 0, 100)}")
print(f"  is_positive(10): {is_positive(10)}")
print(f"  is_positive(-5): {is_positive(-5)}")
print(f"  is_non_negative(0): {is_non_negative(0)}")
print(f"  is_percentage(85): {is_percentage(85)}")
print(f"  is_percentage(105): {is_percentage(105)}")
print()

# Example 3: String Validation
print("="*70)
print("Example 3: String Content Validation")
print("="*70)

def is_not_empty(text):
    """Check if string is not empty"""
    return bool(text and text.strip())

def is_alpha(text):
    """Check if string contains only letters"""
    return text.isalpha()

def is_alphanumeric(text):
    """Check if string contains only letters and numbers"""
    return text.isalnum()

def is_numeric(text):
    """Check if string contains only digits"""
    return text.isdigit()

def has_minimum_length(text, min_length):
    """Check if string meets minimum length"""
    return len(text) >= min_length

# Test string validation
test_strings = ["hello", "hello123", "123", "", "   ", "Hello World"]

print("String validation:")
for text in test_strings:
    print(f"  '{text}' - not_empty: {is_not_empty(text)}, alpha: {is_alpha(text)}, "
          f"alnum: {is_alphanumeric(text)}, numeric: {is_numeric(text)}")

print(f"\\n  'password' length >= 8: {has_minimum_length('password', 8)}")
print(f"  'pass' length >= 8: {has_minimum_length('pass', 8)}")
print()

# Example 4: Email Validation
print("="*70)
print("Example 4: Email Format Validation")
print("="*70)

def is_valid_email(email):
    """Basic email validation"""
    if not isinstance(email, str):
        return False

    # Basic checks
    if '@' not in email:
        return False

    parts = email.split('@')
    if len(parts) != 2:
        return False

    local, domain = parts

    # Check local part (before @)
    if not local or len(local) > 64:
        return False

    # Check domain part (after @)
    if not domain or '.' not in domain:
        return False

    # Check domain has valid format
    domain_parts = domain.split('.')
    if any(not part for part in domain_parts):
        return False

    return True

# Test email validation
emails = [
    "user@example.com",
    "john.doe@company.co.uk",
    "invalid",
    "@example.com",
    "user@",
    "user@@example.com",
    "user@example",
    ""
]

print("Email validation:")
for email in emails:
    is_valid = is_valid_email(email)
    status = "VALID" if is_valid else "INVALID"
    print(f"  {email:30} - {status}")
print()

# Example 5: Password Validation
print("="*70)
print("Example 5: Password Strength Validation")
print("="*70)

def validate_password(password):
    """Validate password strength
    Requirements:
    - At least 8 characters
    - Contains uppercase letter
    - Contains lowercase letter
    - Contains digit
    - Contains special character
    """
    errors = []

    if len(password) < 8:
        errors.append("Must be at least 8 characters")

    if not any(c.isupper() for c in password):
        errors.append("Must contain uppercase letter")

    if not any(c.islower() for c in password):
        errors.append("Must contain lowercase letter")

    if not any(c.isdigit() for c in password):
        errors.append("Must contain digit")

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in special_chars for c in password):
        errors.append("Must contain special character")

    return len(errors) == 0, errors

# Test password validation
passwords = [
    "Pass123!",
    "password",
    "PASSWORD123",
    "Pass123",
    "P@ss1",
    "MySecureP@ssw0rd"
]

print("Password validation:")
for pwd in passwords:
    is_valid, errors = validate_password(pwd)
    if is_valid:
        print(f"  '{pwd}' - VALID")
    else:
        print(f"  '{pwd}' - INVALID:")
        for error in errors:
            print(f"    - {error}")
print()

# Example 6: Date Validation
print("="*70)
print("Example 6: Date Format Validation")
print("="*70)

def is_valid_date(date_str, format='YYYY-MM-DD'):
    """Validate date string format"""
    if not isinstance(date_str, str):
        return False

    if format == 'YYYY-MM-DD':
        parts = date_str.split('-')
        if len(parts) != 3:
            return False

        year, month, day = parts

        # Check if all parts are numeric
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return False

        # Check lengths
        if len(year) != 4 or len(month) != 2 or len(day) != 2:
            return False

        # Check ranges
        y, m, d = int(year), int(month), int(day)
        if not (1 <= m <= 12):
            return False

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Check for leap year
        if m == 2 and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):
            max_days = 29
        else:
            max_days = days_in_month[m - 1]

        if not (1 <= d <= max_days):
            return False

        return True

    return False

# Test date validation
dates = [
    "2024-01-15",
    "2024-02-29",  # Leap year
    "2023-02-29",  # Not leap year
    "2024-13-01",  # Invalid month
    "2024-01-32",  # Invalid day
    "24-01-15",    # Wrong year format
    "2024/01/15",  # Wrong separator
]

print("Date validation (YYYY-MM-DD):")
for date in dates:
    is_valid = is_valid_date(date)
    status = "VALID" if is_valid else "INVALID"
    print(f"  {date:15} - {status}")
print()

# Example 7: URL Validation
print("="*70)
print("Example 7: URL Format Validation")
print("="*70)

def is_valid_url(url):
    """Basic URL validation"""
    if not isinstance(url, str):
        return False

    # Check for protocol
    if not (url.startswith('http://') or url.startswith('https://')):
        return False

    # Remove protocol
    url_without_protocol = url.replace('https://', '').replace('http://', '')

    # Check for domain
    if not url_without_protocol or '.' not in url_without_protocol.split('/')[0]:
        return False

    return True

# Test URL validation
urls = [
    "https://www.example.com",
    "http://example.com/path",
    "https://sub.example.co.uk/page?param=value",
    "www.example.com",
    "ftp://example.com",
    "https://",
    ""
]

print("URL validation:")
for url in urls:
    is_valid = is_valid_url(url)
    status = "VALID" if is_valid else "INVALID"
    print(f"  {url:45} - {status}")
print()

# Example 8: Credit Card Validation (Luhn Algorithm)
print("="*70)
print("Example 8: Credit Card Number Validation")
print("="*70)

def validate_credit_card(card_number):
    """Validate credit card using Luhn algorithm"""
    # Remove spaces and dashes
    card_number = str(card_number).replace(' ', '').replace('-', '')

    # Check if all digits
    if not card_number.isdigit():
        return False

    # Check length (most cards are 13-19 digits)
    if not (13 <= len(card_number) <= 19):
        return False

    # Luhn algorithm
    digits = [int(d) for d in card_number]
    checksum = 0

    # Process from right to left
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    return sum(digits) % 10 == 0

# Test credit card validation
cards = [
    "4532015112830366",      # Valid Visa
    "6011514433546201",      # Valid Discover
    "1234567890123456",      # Invalid
    "4532-0151-1283-0366",   # Valid with dashes
    "123",                   # Too short
]

print("Credit card validation:")
for card in cards:
    is_valid = validate_credit_card(card)
    status = "VALID" if is_valid else "INVALID"
    print(f"  {card:25} - {status}")
print()

# Example 9: Business Rule Validation
print("="*70)
print("Example 9: Custom Business Rule Validation")
print("="*70)

def validate_age_for_license(age):
    """Validate if age qualifies for driver's license"""
    errors = []

    if not isinstance(age, (int, float)):
        return False, ["Age must be a number"]

    if age < 16:
        errors.append("Must be at least 16 years old")
    elif age > 120:
        errors.append("Invalid age")

    return len(errors) == 0, errors

def validate_order(quantity, price):
    """Validate order parameters"""
    errors = []

    if not isinstance(quantity, int):
        errors.append("Quantity must be an integer")
    elif quantity <= 0:
        errors.append("Quantity must be positive")
    elif quantity > 1000:
        errors.append("Quantity exceeds maximum (1000)")

    if not isinstance(price, (int, float)):
        errors.append("Price must be a number")
    elif price < 0:
        errors.append("Price cannot be negative")

    return len(errors) == 0, errors

# Test business rules
print("Age validation for license:")
for age in [15, 16, 25, 65, 121]:
    is_valid, errors = validate_age_for_license(age)
    if is_valid:
        print(f"  Age {age}: VALID")
    else:
        print(f"  Age {age}: INVALID - {', '.join(errors)}")

print("\\nOrder validation:")
test_orders = [(10, 99.99), (-5, 50.00), (1500, 25.00), (50, -10.00)]
for qty, price in test_orders:
    is_valid, errors = validate_order(qty, price)
    if is_valid:
        print(f"  Qty: {qty}, Price: ${price:.2f} - VALID")
    else:
        print(f"  Qty: {qty}, Price: ${price:.2f} - INVALID:")
        for error in errors:
            print(f"    - {error}")
print()

# Example 10: Practical Application - Form Validator
print("="*70)
print("Example 10: Real-World Use Case - Complete Form Validation")
print("="*70)

class FormValidator:
    """Comprehensive form validation system"""

    @staticmethod
    def validate_registration_form(data):
        """Validate user registration form"""
        errors = {}

        # Validate username
        username = data.get('username', '')
        if not is_not_empty(username):
            errors['username'] = "Username is required"
        elif not has_minimum_length(username, 3):
            errors['username'] = "Username must be at least 3 characters"
        elif not is_alphanumeric(username):
            errors['username'] = "Username must be alphanumeric"

        # Validate email
        email = data.get('email', '')
        if not is_not_empty(email):
            errors['email'] = "Email is required"
        elif not is_valid_email(email):
            errors['email'] = "Invalid email format"

        # Validate password
        password = data.get('password', '')
        is_valid_pwd, pwd_errors = validate_password(password)
        if not is_valid_pwd:
            errors['password'] = pwd_errors

        # Validate age
        age = data.get('age')
        if age is None:
            errors['age'] = "Age is required"
        elif not isinstance(age, int):
            errors['age'] = "Age must be a number"
        elif not is_in_range(age, 13, 120):
            errors['age'] = "Age must be between 13 and 120"

        # Validate terms acceptance
        if not data.get('accepted_terms', False):
            errors['terms'] = "You must accept the terms and conditions"

        return len(errors) == 0, errors

# Test form validation
form_data_valid = {
    'username': 'john123',
    'email': 'john@example.com',
    'password': 'SecureP@ss1',
    'age': 25,
    'accepted_terms': True
}

form_data_invalid = {
    'username': 'ab',
    'email': 'invalid-email',
    'password': 'weak',
    'age': 10,
    'accepted_terms': False
}

print("Form Validation Test 1 (Valid form):")
is_valid, errors = FormValidator.validate_registration_form(form_data_valid)
if is_valid:
    print("  FORM IS VALID - Registration successful!")
else:
    print("  FORM HAS ERRORS:")
    for field, error in errors.items():
        print(f"    {field}: {error}")

print("\\nForm Validation Test 2 (Invalid form):")
is_valid, errors = FormValidator.validate_registration_form(form_data_invalid)
if is_valid:
    print("  FORM IS VALID")
else:
    print("  FORM HAS ERRORS:")
    for field, error in errors.items():
        if isinstance(error, list):
            print(f"    {field}:")
            for e in error:
                print(f"      - {e}")
        else:
            print(f"    {field}: {error}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Validate data types before processing")
print("2. Check ranges for numeric values")
print("3. Validate string formats (email, URL, dates)")
print("4. Implement business rule validation")
print("5. Return meaningful error messages")
print("6. Use isinstance() for type checking")
print("7. Combine multiple validations for complex rules")
print("8. Validate at system boundaries (user input, APIs)")
print("9. Build reusable validator functions")
print("10. Always validate before processing data")
print("="*70)
'''

# Upgrade Lesson 128: Zip Function
lesson128['fullSolution'] = '''"""
Zip Function

Master Python's zip() function for combining multiple iterables. Learn to
pair elements, create dictionaries, transpose matrices, and process parallel
data streams. Essential for elegant data manipulation.

**Zero Package Installation Required**
"""

# Example 1: Basic Zip Usage
print("="*70)
print("Example 1: Basic zip() Function")
print("="*70)

names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]

# Zip two lists together
combined = zip(names, ages)

print("Combining two lists:")
print(f"Names: {names}")
print(f"Ages: {ages}")
print("\\nZipped pairs:")
for name, age in zip(names, ages):
    print(f"  {name}: {age} years old")
print()

# Example 2: Convert Zip to List/Tuple
print("="*70)
print("Example 2: Converting zip() Results")
print("="*70)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Convert to list of tuples
pairs_list = list(zip(list1, list2))
print(f"As list: {pairs_list}")

# Convert to tuple of tuples
pairs_tuple = tuple(zip(list1, list2))
print(f"As tuple: {pairs_tuple}")

# Individual tuples
print("\\nIndividual pairs:")
for pair in zip(list1, list2):
    print(f"  {pair} - type: {type(pair)}")
print()

# Example 3: Zip with Different Lengths
print("="*70)
print("Example 3: Zipping Lists of Different Lengths")
print("="*70)

short = [1, 2, 3]
long = ['a', 'b', 'c', 'd', 'e']

print(f"Short list: {short}")
print(f"Long list: {long}")
print("\\nzip() stops at shortest:")
for num, letter in zip(short, long):
    print(f"  {num} - {letter}")

print(f"\\nResult length: {len(list(zip(short, long)))}")
print()

# Example 4: Zip with Three or More Iterables
print("="*70)
print("Example 4: Zipping Multiple Iterables")
print("="*70)

names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
cities = ["NYC", "LA", "Chicago"]
scores = [95, 88, 92]

print("Combining four lists:\\n")
for name, age, city, score in zip(names, ages, cities, scores):
    print(f"  {name} (age {age}) from {city} - Score: {score}")
print()

# Example 5: Create Dictionary from Zip
print("="*70)
print("Example 5: Creating Dictionaries with zip()")
print("="*70)

keys = ['name', 'age', 'city', 'occupation']
values = ['Alice', 30, 'New York', 'Engineer']

# Create dictionary
person = dict(zip(keys, values))

print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"\\nDictionary: {person}")

# Multiple people
names = ["Alice", "Bob", "Charlie"]
salaries = [75000, 65000, 80000]

salary_dict = dict(zip(names, salaries))
print(f"\\nSalary dictionary: {salary_dict}")
print()

# Example 6: Unzip with Zip and Unpacking
print("="*70)
print("Example 6: Unzipping Data with zip(*)")
print("="*70)

pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

print(f"Original pairs: {pairs}")

# Unzip using zip with unpacking
numbers, letters = zip(*pairs)

print(f"\\nUnzipped:")
print(f"  Numbers: {numbers}")
print(f"  Letters: {letters}")

# Convert to lists
numbers_list = list(numbers)
letters_list = list(letters)

print(f"\\nAs lists:")
print(f"  Numbers: {numbers_list}")
print(f"  Letters: {letters_list}")
print()

# Example 7: Zip with Enumerate
print("="*70)
print("Example 7: Combining zip() with enumerate()")
print("="*70)

fruits = ["apple", "banana", "cherry"]
prices = [1.20, 0.50, 2.30]

print("Enumerate with zip:")
for i, (fruit, price) in enumerate(zip(fruits, prices), start=1):
    print(f"  {i}. {fruit}: ${price:.2f}")

print("\\nZip with enumerated lists:")
for idx, fruit, price in zip(range(1, 4), fruits, prices):
    print(f"  Item #{idx}: {fruit} - ${price:.2f}")
print()

# Example 8: Transpose Matrix with Zip
print("="*70)
print("Example 8: Matrix Transposition")
print("="*70)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(f"  {row}")

# Transpose using zip
transposed = list(zip(*matrix))

print("\\nTransposed matrix:")
for row in transposed:
    print(f"  {list(row)}")

# More readable format
print("\\nTransposed (formatted):")
for col_idx, column in enumerate(transposed):
    print(f"  Column {col_idx + 1}: {list(column)}")
print()

# Example 9: Zip for Parallel Iteration
print("="*70)
print("Example 9: Parallel Data Processing")
print("="*70)

temperatures_f = [32, 68, 86, 104]
temperatures_c = [0, 20, 30, 40]
cities = ["NYC", "LA", "Miami", "Phoenix"]

print("Weather Report:\\n")
for city, temp_f, temp_c in zip(cities, temperatures_f, temperatures_c):
    print(f"  {city}: {temp_f}°F ({temp_c}°C)")

# Calculate statistics in parallel
scores_math = [85, 92, 78, 95]
scores_science = [88, 85, 92, 90]
students = ["Alice", "Bob", "Charlie", "David"]

print("\\nStudent Scores:\\n")
for student, math, science in zip(students, scores_math, scores_science):
    average = (math + science) / 2
    print(f"  {student}: Math={math}, Science={science}, Average={average:.1f}")
print()

# Example 10: Practical Application - Data Processing
print("="*70)
print("Example 10: Real-World Use Case - Sales Data Analysis")
print("="*70)

# Sales data from different sources
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
units_sold = [45, 120, 85, 32, 95]
unit_prices = [999.99, 29.99, 79.99, 299.99, 149.99]
costs = [650.00, 15.00, 45.00, 180.00, 80.00]

print("SALES ANALYSIS REPORT")
print("="*70)

total_revenue = 0
total_cost = 0
total_profit = 0

# Process all data in parallel
for product, units, price, cost in zip(products, units_sold, unit_prices, costs):
    revenue = units * price
    total_cost_item = units * cost
    profit = revenue - total_cost_item
    margin = (profit / revenue * 100) if revenue > 0 else 0

    print(f"\\nProduct: {product}")
    print(f"  Units sold: {units}")
    print(f"  Unit price: ${price:.2f}")
    print(f"  Revenue: ${revenue:,.2f}")
    print(f"  Cost: ${total_cost_item:,.2f}")
    print(f"  Profit: ${profit:,.2f}")
    print(f"  Margin: {margin:.1f}%")

    total_revenue += revenue
    total_cost += total_cost_item
    total_profit += profit

print("\\n" + "="*70)
print("SUMMARY")
print("="*70)
print(f"Total products: {len(products)}")
print(f"Total units sold: {sum(units_sold)}")
print(f"Total revenue: ${total_revenue:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")
print(f"Total profit: ${total_profit:,.2f}")
print(f"Overall margin: {(total_profit / total_revenue * 100):.1f}%")

# Find best and worst performers
revenue_per_product = [u * p for u, p in zip(units_sold, unit_prices)]
best_idx = revenue_per_product.index(max(revenue_per_product))
worst_idx = revenue_per_product.index(min(revenue_per_product))

print("\\nTop performer:", products[best_idx], f"(${revenue_per_product[best_idx]:,.2f})")
print("Lowest performer:", products[worst_idx], f"(${revenue_per_product[worst_idx]:,.2f})")

# Create summary dictionary
summary = dict(zip(
    products,
    [{'units': u, 'revenue': u*p, 'profit': u*(p-c)}
     for u, p, c in zip(units_sold, unit_prices, costs)]
))

print("\\nProduct summary dictionary created with", len(summary), "entries")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. zip(list1, list2) - Pair elements from iterables")
print("2. zip() returns an iterator (convert to list/tuple to see)")
print("3. Stops at shortest iterable")
print("4. dict(zip(keys, values)) - Create dictionaries")
print("5. zip(*pairs) - Unzip paired data")
print("6. Combine with enumerate() for indexed pairing")
print("7. Transpose matrices with zip(*matrix)")
print("8. Process parallel data streams together")
print("9. Works with 3+ iterables simultaneously")
print("10. Memory efficient - generates pairs on demand")
print("="*70)
'''

# Save lessons 127-128 and continue
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Upgrade Lesson 129: __str__ Method
lesson129['fullSolution'] = '''"""
__str__ Method

Master the __str__ special method in Python for custom string representations.
Learn to create readable object descriptions, format output, and implement
best practices for string conversion. Essential for debugging and user-facing output.

**Zero Package Installation Required**
"""

# Example 1: Basic __str__ Method
print("="*70)
print("Example 1: Basic __str__ Implementation")
print("="*70)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# Test __str__
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(f"Using print(): {person1}")
print(f"Using str(): {str(person2)}")
print(f"String formatting: Person is {person1}")
print()

# Example 2: __str__ vs Default Representation
print("="*70)
print("Example 2: With and Without __str__")
print("="*70)

class WithoutStr:
    def __init__(self, value):
        self.value = value

class WithStr:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"WithStr object containing: {self.value}"

# Compare
obj_without = WithoutStr(42)
obj_with = WithStr(42)

print("Without __str__:")
print(f"  {obj_without}")

print("\\nWith __str__:")
print(f"  {obj_with}")
print()

# Example 3: Formatted __str__ Output
print("="*70)
print("Example 3: Nicely Formatted __str__")
print("="*70)

class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        return (f"'{self.title}' by {self.author} "
                f"({self.year}) - {self.pages} pages")

# Test formatted output
book1 = Book("1984", "George Orwell", 1949, 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 281)

print("Books:")
print(f"  {book1}")
print(f"  {book2}")
print()

# Example 4: Multi-line __str__
print("="*70)
print("Example 4: Multi-line String Representation")
print("="*70)

class Employee:
    def __init__(self, name, position, salary, department):
        self.name = name
        self.position = position
        self.salary = salary
        self.department = department

    def __str__(self):
        return (f"Employee Details:\\n"
                f"  Name: {self.name}\\n"
                f"  Position: {self.position}\\n"
                f"  Department: {self.department}\\n"
                f"  Salary: ${self.salary:,.2f}")

# Test multi-line output
emp = Employee("Alice Johnson", "Senior Developer", 95000, "Engineering")
print(emp)
print()

# Example 5: __str__ with Conditional Formatting
print("="*70)
print("Example 5: Conditional String Representation")
print("="*70)

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        status = "POSITIVE" if self.balance >= 0 else "OVERDRAWN"
        balance_str = f"${abs(self.balance):,.2f}"

        if self.balance < 0:
            balance_str = f"-{balance_str}"

        return f"Account {self.account_number}: {balance_str} ({status})"

# Test conditional formatting
accounts = [
    BankAccount("12345", 1500.50),
    BankAccount("67890", -250.00),
    BankAccount("11111", 0.00)
]

print("Bank accounts:")
for account in accounts:
    print(f"  {account}")
print()

# Example 6: __str__ in Container Classes
print("="*70)
print("Example 6: __str__ for Collections")
print("="*70)

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def __str__(self):
        if not self.members:
            return f"Team '{self.name}' (no members)"

        members_str = ", ".join(self.members)
        return f"Team '{self.name}' ({len(self.members)} members): {members_str}"

# Test container __str__
team = Team("Python Developers")
print(team)

team.add_member("Alice")
team.add_member("Bob")
team.add_member("Charlie")
print(team)
print()

# Example 7: __str__ vs __repr__
print("="*70)
print("Example 7: __str__ vs __repr__ Methods")
print("="*70)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # User-friendly representation
        return f"Point at ({self.x}, {self.y})"

    def __repr__(self):
        # Developer-friendly representation
        return f"Point(x={self.x}, y={self.y})"

# Test both methods
point = Point(10, 20)

print(f"str(point):  {str(point)}")
print(f"repr(point): {repr(point)}")
print(f"print(point): {point}")

# In a list, __repr__ is used
points = [Point(1, 2), Point(3, 4)]
print(f"\\nList of points: {points}")
print()

# Example 8: __str__ with Calculated Values
print("="*70)
print("Example 8: __str__ Including Calculated Properties")
print("="*70)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return (f"Rectangle {self.width}x{self.height} "
                f"(area={self.area()}, perimeter={self.perimeter()})")

# Test with calculations
rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 10)

print(f"Rectangle 1: {rect1}")
print(f"Rectangle 2: {rect2}")
print()

# Example 9: __str__ in Inheritance
print("="*70)
print("Example 9: __str__ with Inheritance")
print("="*70)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def __str__(self):
        # Call parent __str__ and extend
        base = super().__str__()
        return f"{base} ({self.doors} doors)"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def __str__(self):
        base = super().__str__()
        return f"{base} ({self.engine_cc}cc)"

# Test inheritance
vehicle = Vehicle("Generic", "Model X")
car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Harley", "Sportster", 1200)

print(f"Vehicle: {vehicle}")
print(f"Car: {car}")
print(f"Motorcycle: {motorcycle}")
print()

# Example 10: Practical Application - Product Catalog
print("="*70)
print("Example 10: Real-World Use Case - E-commerce Product Display")
print("="*70)

class Product:
    def __init__(self, id, name, price, stock, category):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.reviews = []

    def add_review(self, rating):
        self.reviews.append(rating)

    def average_rating(self):
        if not self.reviews:
            return 0
        return sum(self.reviews) / len(self.reviews)

    def __str__(self):
        # Build detailed product description
        stock_status = "In Stock" if self.stock > 0 else "Out of Stock"
        stock_info = f"{self.stock} available" if self.stock > 0 else "Sold out"

        # Rating display
        avg_rating = self.average_rating()
        if avg_rating > 0:
            stars = "★" * int(avg_rating) + "☆" * (5 - int(avg_rating))
            rating_info = f"{stars} ({avg_rating:.1f}/5.0 from {len(self.reviews)} reviews)"
        else:
            rating_info = "No reviews yet"

        return (f"[{self.id}] {self.name}\\n"
                f"  Category: {self.category}\\n"
                f"  Price: ${self.price:.2f}\\n"
                f"  Status: {stock_status} ({stock_info})\\n"
                f"  Rating: {rating_info}")

# Create product catalog
products = [
    Product("P001", "Wireless Mouse", 29.99, 45, "Electronics"),
    Product("P002", "USB-C Cable", 12.99, 0, "Accessories"),
    Product("P003", "Laptop Stand", 49.99, 12, "Office")
]

# Add some reviews
products[0].add_review(5)
products[0].add_review(4)
products[0].add_review(5)
products[2].add_review(4)
products[2].add_review(3)

print("PRODUCT CATALOG")
print("="*70)

for product in products:
    print(product)
    print()

# Demonstrate string usage in different contexts
print("="*70)
print("Using __str__ in various contexts:")
print("="*70)

print("1. Direct print:")
print(products[0])

print("\\n2. String concatenation:")
msg = "Featured product: " + str(products[0])
print(msg)

print("\\n3. In f-string:")
print(f"Check out:\\n{products[0]}")

print("\\n4. String formatting:")
print("Product info:\\n{}".format(products[0]))

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. __str__ defines how objects appear when printed")
print("2. Return user-friendly, readable strings")
print("3. Called by str(), print(), and string formatting")
print("4. Should not raise exceptions")
print("5. Use f-strings for clean, formatted output")
print("6. Can include calculated values and properties")
print("7. __str__ for users, __repr__ for developers")
print("8. Support multi-line output with \\\\n")
print("9. Call super().__str__() in inheritance")
print("10. Essential for debugging and user interfaces")
print("="*70)
'''

# Upgrade Lesson 130: Class vs Instance Attributes
lesson130['fullSolution'] = '''"""
Class vs Instance Attributes

Master the difference between class and instance attributes in Python.
Learn when to use each, understand shared vs individual state, and avoid
common pitfalls. Essential for object-oriented programming design.

**Zero Package Installation Required**
"""

# Example 1: Instance Attributes Basics
print("="*70)
print("Example 1: Instance Attributes")
print("="*70)

class Dog:
    def __init__(self, name, age):
        # Instance attributes - unique to each object
        self.name = name
        self.age = age

# Each instance has its own attributes
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"Dog 1: {dog1.name}, age {dog1.age}")
print(f"Dog 2: {dog2.name}, age {dog2.age}")

# Modifying one doesn't affect the other
dog1.age = 4
print(f"\\nAfter birthday:")
print(f"Dog 1: {dog1.name}, age {dog1.age}")
print(f"Dog 2: {dog2.name}, age {dog2.age}")
print()

# Example 2: Class Attributes Basics
print("="*70)
print("Example 2: Class Attributes")
print("="*70)

class Cat:
    # Class attribute - shared by all instances
    species = "Felis catus"
    legs = 4

    def __init__(self, name):
        # Instance attribute - unique to each cat
        self.name = name

# All instances share class attributes
cat1 = Cat("Whiskers")
cat2 = Cat("Mittens")

print(f"{cat1.name} - Species: {cat1.species}, Legs: {cat1.legs}")
print(f"{cat2.name} - Species: {cat2.species}, Legs: {cat2.legs}")

# Access via class
print(f"\\nAccessed via class: Cat.species = {Cat.species}")
print()

# Example 3: Class Attribute Counter
print("="*70)
print("Example 3: Using Class Attributes as Counters")
print("="*70)

class User:
    # Class attribute to track total users
    total_users = 0

    def __init__(self, username):
        self.username = username
        # Increment class attribute
        User.total_users += 1

# Create users and track count
print(f"Initial count: {User.total_users}")

user1 = User("alice")
print(f"After creating alice: {User.total_users}")

user2 = User("bob")
print(f"After creating bob: {User.total_users}")

user3 = User("charlie")
print(f"After creating charlie: {User.total_users}")

print(f"\\nTotal users created: {User.total_users}")
print()

# Example 4: Modifying Class Attributes
print("="*70)
print("Example 4: Modifying Class vs Instance Attributes")
print("="*70)

class Product:
    tax_rate = 0.10  # Class attribute - 10% tax

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self):
        return self.price * (1 + Product.tax_rate)

# Create products
laptop = Product("Laptop", 1000)
mouse = Product("Mouse", 25)

print(f"{laptop.name}: ${laptop.total_price():.2f}")
print(f"{mouse.name}: ${mouse.total_price():.2f}")

# Change class attribute - affects all instances
print("\\nTax rate increased to 15%:")
Product.tax_rate = 0.15

print(f"{laptop.name}: ${laptop.total_price():.2f}")
print(f"{mouse.name}: ${mouse.total_price():.2f}")
print()

# Example 5: Instance Attribute Shadows Class Attribute
print("="*70)
print("Example 5: Instance Attributes Shadow Class Attributes")
print("="*70)

class Settings:
    theme = "light"  # Class attribute

    def __init__(self, user):
        self.user = user

# Create instances
settings1 = Settings("Alice")
settings2 = Settings("Bob")

print(f"Alice theme: {settings1.theme}")
print(f"Bob theme: {settings2.theme}")
print(f"Class theme: {Settings.theme}")

# Set instance attribute (shadows class attribute)
print("\\nAlice changes theme to 'dark':")
settings1.theme = "dark"

print(f"Alice theme: {settings1.theme}")
print(f"Bob theme: {settings2.theme}")
print(f"Class theme: {Settings.theme}")

# Delete instance attribute to reveal class attribute
print("\\nDeleting Alice's instance attribute:")
del settings1.theme
print(f"Alice theme: {settings1.theme}")
print()

# Example 6: Mutable Class Attributes Pitfall
print("="*70)
print("Example 6: PITFALL - Mutable Class Attributes")
print("="*70)

class TeamWrong:
    members = []  # WRONG: Mutable class attribute

    def __init__(self, name):
        self.name = name

    def add_member(self, member):
        self.members.append(member)  # Modifies shared list!

# This will cause problems
team1 = TeamWrong("Team A")
team2 = TeamWrong("Team B")

team1.add_member("Alice")
team2.add_member("Bob")

print(f"Team A members: {team1.members}")
print(f"Team B members: {team2.members}")
print("Problem: Both teams share the same list!")

# CORRECT way
class TeamCorrect:
    def __init__(self, name):
        self.name = name
        self.members = []  # Instance attribute

    def add_member(self, member):
        self.members.append(member)

team3 = TeamCorrect("Team C")
team4 = TeamCorrect("Team D")

team3.add_member("Charlie")
team4.add_member("David")

print(f"\\nCorrect approach:")
print(f"Team C members: {team3.members}")
print(f"Team D members: {team4.members}")
print()

# Example 7: Class Methods vs Instance Methods
print("="*70)
print("Example 7: Class Methods Accessing Class Attributes")
print("="*70)

class Employee:
    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def get_company_info(cls):
        return f"{cls.company} - {cls.employee_count} employees"

    def get_info(self):
        # Instance method accessing both instance and class attributes
        return f"{self.name} works at {Employee.company}"

# Test class and instance methods
emp1 = Employee("Alice", 75000)
emp2 = Employee("Bob", 65000)

print(f"Company info: {Employee.get_company_info()}")
print(f"Employee info: {emp1.get_info()}")
print(f"Employee info: {emp2.get_info()}")
print()

# Example 8: Class Attributes for Constants
print("="*70)
print("Example 8: Class Attributes as Constants")
print("="*70)

class MathConstants:
    PI = 3.14159
    E = 2.71828
    GOLDEN_RATIO = 1.61803

    @staticmethod
    def circle_area(radius):
        return MathConstants.PI * radius ** 2

    @staticmethod
    def circle_circumference(radius):
        return 2 * MathConstants.PI * radius

# Use class constants
radius = 5
print(f"Radius: {radius}")
print(f"Area: {MathConstants.circle_area(radius):.2f}")
print(f"Circumference: {MathConstants.circle_circumference(radius):.2f}")

# Access constants directly
print(f"\\nConstants:")
print(f"  PI = {MathConstants.PI}")
print(f"  E = {MathConstants.E}")
print(f"  Golden Ratio = {MathConstants.GOLDEN_RATIO}")
print()

# Example 9: __dict__ to Inspect Attributes
print("="*70)
print("Example 9: Inspecting Class and Instance Attributes")
print("="*70)

class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand, model):
        self.brand = brand  # Instance attributes
        self.model = model

car = Car("Toyota", "Camry")

print("Class attributes (Car.__dict__):")
for key, value in Car.__dict__.items():
    if not key.startswith('__'):
        print(f"  {key}: {value}")

print("\\nInstance attributes (car.__dict__):")
for key, value in car.__dict__.items():
    print(f"  {key}: {value}")

print("\\nAll attributes accessible from instance:")
print(f"  car.brand: {car.brand} (instance)")
print(f"  car.model: {car.model} (instance)")
print(f"  car.wheels: {car.wheels} (class)")
print()

# Example 10: Practical Application - Game Character System
print("="*70)
print("Example 10: Real-World Use Case - RPG Character System")
print("="*70)

class Character:
    # Class attributes - shared by all characters
    game_name = "Epic Quest"
    total_characters = 0
    max_level = 100

    # Class attribute for default stats
    default_health = 100
    default_mana = 50

    def __init__(self, name, char_class):
        # Instance attributes - unique to each character
        self.name = name
        self.char_class = char_class
        self.level = 1
        self.health = Character.default_health
        self.mana = Character.default_mana
        self.experience = 0

        # Update class counter
        Character.total_characters += 1

    def gain_experience(self, exp):
        self.experience += exp
        # Level up logic
        while self.experience >= self.level * 100 and self.level < Character.max_level:
            self.level += 1
            self.health += 20
            self.mana += 10
            print(f"  {self.name} leveled up to {self.level}!")

    @classmethod
    def game_info(cls):
        return f"{cls.game_name} - {cls.total_characters} characters created"

    def __str__(self):
        return (f"{self.name} the {self.char_class} "
                f"(Level {self.level}, HP: {self.health}, MP: {self.mana}, "
                f"XP: {self.experience})")

# Create characters
print(f"Game: {Character.game_info()}\\n")

warrior = Character("Arthas", "Warrior")
mage = Character("Gandalf", "Mage")
rogue = Character("Stealth", "Rogue")

print("Characters created:")
print(f"  {warrior}")
print(f"  {mage}")
print(f"  {rogue}")

print(f"\\n{Character.game_info()}")

# Gain experience
print("\\nBattle commenced!")
warrior.gain_experience(250)
mage.gain_experience(180)

print("\\nAfter battle:")
print(f"  {warrior}")
print(f"  {mage}")

# Modify class attribute
print("\\nGame update: Max level increased to 150!")
Character.max_level = 150
print(f"New max level: {Character.max_level}")

# Show all attributes
print("\\nAttribute breakdown for Warrior:")
print(f"  Instance attributes: {warrior.__dict__}")
print(f"  Class attributes used: game_name, total_characters, max_level")

print("\\n" + "="*70)
print("GAME SUMMARY")
print("="*70)
print(Character.game_info())
print(f"Max level: {Character.max_level}")
print(f"Default stats: HP={Character.default_health}, MP={Character.default_mana}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Instance attributes: unique to each object (self.x)")
print("2. Class attributes: shared by all instances (ClassName.x)")
print("3. Define instance attributes in __init__()")
print("4. Define class attributes at class level")
print("5. Access class attributes via ClassName.attr or self.attr")
print("6. Instance attribute shadows class attribute if same name")
print("7. NEVER use mutable class attributes (lists, dicts)")
print("8. Use class attributes for constants and counters")
print("9. Class methods access class attributes with cls")
print("10. Check __dict__ to inspect instance attributes")
print("="*70)
'''

# Save all lessons and print final summary
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("\n" + "="*70)
print("LESSONS 127-130 COMPLETE!")
print("="*70)
print(f"  127: Validation Functions - {len(lesson127['fullSolution'])} chars")
print(f"  128: Zip Function - {len(lesson128['fullSolution'])} chars")
print(f"  129: __str__ Method - {len(lesson129['fullSolution'])} chars")
print(f"  130: Class vs Instance Attributes - {len(lesson130['fullSolution'])} chars")

total_chars = (len(lesson127['fullSolution']) + len(lesson128['fullSolution']) +
               len(lesson129['fullSolution']) + len(lesson130['fullSolution']))

print(f"\\nTotal characters added: {total_chars:,}")
print(f"Average per lesson: {total_chars // 4:,} chars")
print("="*70)
