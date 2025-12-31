#!/usr/bin/env python3
"""
Upgrade Python lessons 121-130 with comprehensive content.
- Lesson 121: Math Helper Functions
- Lesson 122: Method Overriding Basics
- Lesson 123: Object Method Calls
- Lesson 124: Range Function
- Lesson 125: Simple Calculator Functions
- Lesson 126: Temperature Conversion Functions
- Lesson 127: Validation Functions
- Lesson 128: Zip Function
- Lesson 129: __str__ Method
- Lesson 130: Class vs Instance Attributes
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 121-130
lesson121 = next(l for l in lessons if l['id'] == 121)
lesson122 = next(l for l in lessons if l['id'] == 122)
lesson123 = next(l for l in lessons if l['id'] == 123)
lesson124 = next(l for l in lessons if l['id'] == 124)
lesson125 = next(l for l in lessons if l['id'] == 125)
lesson126 = next(l for l in lessons if l['id'] == 126)
lesson127 = next(l for l in lessons if l['id'] == 127)
lesson128 = next(l for l in lessons if l['id'] == 128)
lesson129 = next(l for l in lessons if l['id'] == 129)
lesson130 = next(l for l in lessons if l['id'] == 130)

# Upgrade Lesson 121: Math Helper Functions
lesson121['fullSolution'] = '''"""
Math Helper Functions

Master creating reusable math helper functions in Python. Learn to build
utility libraries, implement common mathematical operations, and organize
code efficiently. Essential for clean, maintainable programs.

**Zero Package Installation Required**
"""

# Example 1: Basic Math Helpers
print("="*70)
print("Example 1: Basic Mathematical Helper Functions")
print("="*70)

def square(n):
    """Return the square of a number"""
    return n ** 2

def cube(n):
    """Return the cube of a number"""
    return n ** 3

def is_even(n):
    """Check if a number is even"""
    return n % 2 == 0

def is_odd(n):
    """Check if a number is odd"""
    return n % 2 != 0

# Test the helpers
numbers = [2, 3, 5, 8, 10]
print(f"Numbers: {numbers}\\n")

for num in numbers:
    print(f"{num}: square={square(num)}, cube={cube(num)}, even={is_even(num)}, odd={is_odd(num)}")
print()

# Example 2: Statistical Helper Functions
print("="*70)
print("Example 2: Statistical Helper Functions")
print("="*70)

def average(numbers):
    """Calculate the average of a list of numbers"""
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    """Calculate the median of a list of numbers"""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def range_value(numbers):
    """Calculate the range (max - min)"""
    return max(numbers) - min(numbers) if numbers else 0

# Test statistical helpers
data = [15, 22, 18, 30, 25, 19, 21]
print(f"Data: {data}")
print(f"Average: {average(data):.2f}")
print(f"Median: {median(data):.2f}")
print(f"Range: {range_value(data)}")
print(f"Min: {min(data)}, Max: {max(data)}")
print()

# Example 3: Geometric Helper Functions
print("="*70)
print("Example 3: Geometric Calculation Helpers")
print("="*70)

def circle_area(radius):
    """Calculate area of a circle"""
    return 3.14159 * radius ** 2

def circle_circumference(radius):
    """Calculate circumference of a circle"""
    return 2 * 3.14159 * radius

def rectangle_area(length, width):
    """Calculate area of a rectangle"""
    return length * width

def rectangle_perimeter(length, width):
    """Calculate perimeter of a rectangle"""
    return 2 * (length + width)

def triangle_area(base, height):
    """Calculate area of a triangle"""
    return 0.5 * base * height

# Test geometric helpers
print("Circle (radius=5):")
print(f"  Area: {circle_area(5):.2f}")
print(f"  Circumference: {circle_circumference(5):.2f}")

print("\\nRectangle (10x6):")
print(f"  Area: {rectangle_area(10, 6):.2f}")
print(f"  Perimeter: {rectangle_perimeter(10, 6):.2f}")

print("\\nTriangle (base=8, height=5):")
print(f"  Area: {triangle_area(8, 5):.2f}")
print()

# Example 4: Number Conversion Helpers
print("="*70)
print("Example 4: Number Conversion Helper Functions")
print("="*70)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def km_to_miles(km):
    """Convert kilometers to miles"""
    return km * 0.621371

def miles_to_km(miles):
    """Convert miles to kilometers"""
    return miles / 0.621371

# Test conversion helpers
print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")
print(f"10 km = {km_to_miles(10):.2f} miles")
print(f"10 miles = {miles_to_km(10):.2f} km")
print()

# Example 5: Validation Helper Functions
print("="*70)
print("Example 5: Number Validation Helpers")
print("="*70)

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    """Check if a number is a perfect square"""
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

def is_positive(n):
    """Check if a number is positive"""
    return n > 0

def is_in_range(n, min_val, max_val):
    """Check if number is within range"""
    return min_val <= n <= max_val

# Test validation helpers
test_nums = [1, 4, 7, 16, 25, 30]
print(f"Testing: {test_nums}\\n")

for num in test_nums:
    print(f"{num}: prime={is_prime(num)}, perfect_square={is_perfect_square(num)}, "
          f"positive={is_positive(num)}, in_range(1-20)={is_in_range(num, 1, 20)}")
print()

# Example 6: Rounding Helper Functions
print("="*70)
print("Example 6: Rounding and Precision Helpers")
print("="*70)

def round_to_nearest(n, nearest=1):
    """Round to nearest specified value"""
    return round(n / nearest) * nearest

def round_up(n, decimal_places=0):
    """Round up to specified decimal places"""
    multiplier = 10 ** decimal_places
    return int(n * multiplier + 0.5) / multiplier

def truncate(n, decimal_places=0):
    """Truncate to specified decimal places"""
    multiplier = 10 ** decimal_places
    return int(n * multiplier) / multiplier

# Test rounding helpers
value = 123.456

print(f"Value: {value}")
print(f"Round to nearest 10: {round_to_nearest(value, 10)}")
print(f"Round to nearest 5: {round_to_nearest(value, 5)}")
print(f"Round up (2 places): {round_up(value, 2)}")
print(f"Truncate (1 place): {truncate(value, 1)}")
print(f"Python's round (2 places): {round(value, 2)}")
print()

# Example 7: Factorization Helper Functions
print("="*70)
print("Example 7: Factorization Helpers")
print("="*70)

def factorial(n):
    """Calculate factorial of n"""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def get_factors(n):
    """Get all factors of a number"""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def gcd(a, b):
    """Calculate greatest common divisor"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate least common multiple"""
    return abs(a * b) // gcd(a, b)

# Test factorization helpers
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 7: {factorial(7)}")
print(f"\\nFactors of 24: {get_factors(24)}")
print(f"Factors of 36: {get_factors(36)}")
print(f"\\nGCD of 24 and 36: {gcd(24, 36)}")
print(f"LCM of 24 and 36: {lcm(24, 36)}")
print()

# Example 8: Sequence Helper Functions
print("="*70)
print("Example 8: Number Sequence Helpers")
print("="*70)

def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def is_fibonacci(num):
    """Check if a number is in Fibonacci sequence"""
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

def sum_of_digits(n):
    """Calculate sum of digits in a number"""
    return sum(int(digit) for digit in str(abs(n)))

# Test sequence helpers
print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
print(f"\\nIs 21 a Fibonacci number? {is_fibonacci(21)}")
print(f"Is 20 a Fibonacci number? {is_fibonacci(20)}")
print(f"\\nSum of digits in 12345: {sum_of_digits(12345)}")
print(f"Sum of digits in 9876: {sum_of_digits(9876)}")
print()

# Example 9: Comparison Helper Functions
print("="*70)
print("Example 9: Comparison and Constraint Helpers")
print("="*70)

def clamp(value, min_val, max_val):
    """Constrain value to be within min and max"""
    return max(min_val, min(value, max_val))

def normalize(value, min_val, max_val):
    """Normalize value to 0-1 range"""
    if max_val == min_val:
        return 0
    return (value - min_val) / (max_val - min_val)

def percentage(part, total):
    """Calculate percentage"""
    return (part / total * 100) if total != 0 else 0

def percentage_change(old_val, new_val):
    """Calculate percentage change"""
    if old_val == 0:
        return 0
    return ((new_val - old_val) / old_val) * 100

# Test comparison helpers
print(f"Clamp 150 to [0, 100]: {clamp(150, 0, 100)}")
print(f"Clamp -10 to [0, 100]: {clamp(-10, 0, 100)}")
print(f"Clamp 50 to [0, 100]: {clamp(50, 0, 100)}")

print(f"\\nNormalize 50 in [0, 100]: {normalize(50, 0, 100)}")
print(f"Normalize 75 in [0, 100]: {normalize(75, 0, 100)}")

print(f"\\n30 out of 120: {percentage(30, 120):.1f}%")
print(f"Change from 50 to 75: {percentage_change(50, 75):.1f}%")
print()

# Example 10: Practical Application - Math Utility Library
print("="*70)
print("Example 10: Complete Math Helper Library")
print("="*70)

class MathHelpers:
    """Collection of mathematical helper functions"""

    @staticmethod
    def is_power_of_two(n):
        """Check if number is a power of 2"""
        return n > 0 and (n & (n - 1)) == 0

    @staticmethod
    def next_power_of_two(n):
        """Find the next power of 2 greater than n"""
        power = 1
        while power < n:
            power *= 2
        return power

    @staticmethod
    def digital_root(n):
        """Calculate digital root (recursive sum of digits)"""
        while n >= 10:
            n = sum(int(digit) for digit in str(n))
        return n

    @staticmethod
    def is_palindrome_number(n):
        """Check if number is palindrome"""
        s = str(n)
        return s == s[::-1]

# Test the utility library
print("MathHelpers Library Demo:\\n")

test_values = [8, 15, 16, 32, 64, 100]
print("Power of Two Tests:")
for val in test_values:
    is_pow2 = MathHelpers.is_power_of_two(val)
    next_pow2 = MathHelpers.next_power_of_two(val)
    print(f"  {val}: is_power_of_2={is_pow2}, next_power_of_2={next_pow2}")

print("\\nDigital Root Tests:")
for val in [38, 123, 456, 999]:
    dr = MathHelpers.digital_root(val)
    print(f"  Digital root of {val}: {dr}")

print("\\nPalindrome Number Tests:")
for val in [121, 123, 1221, 12321, 12345]:
    is_pal = MathHelpers.is_palindrome_number(val)
    print(f"  {val}: palindrome={is_pal}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Helper functions improve code reusability")
print("2. Group related helpers together logically")
print("3. Use descriptive names: is_even(), calculate_area()")
print("4. Add docstrings to document purpose")
print("5. Handle edge cases (empty lists, zero division)")
print("6. Return meaningful values for all inputs")
print("7. Keep functions focused on single tasks")
print("8. Use @staticmethod for utility classes")
print("9. Test helpers with multiple inputs")
print("10. Build libraries for common operations")
print("="*70)
'''

# Upgrade Lesson 122: Method Overriding Basics
lesson122['fullSolution'] = '''"""
Method Overriding Basics

Master method overriding in Python object-oriented programming. Learn to
customize inherited behavior, call parent methods with super(), and implement
polymorphism. Essential for building flexible, maintainable class hierarchies.

**Zero Package Installation Required**
"""

# Example 1: Basic Method Overriding
print("="*70)
print("Example 1: Basic Method Overriding Concept")
print("="*70)

class Animal:
    """Base class with a method"""
    def speak(self):
        return "Some generic animal sound"

    def info(self):
        return "I am an animal"

class Dog(Animal):
    """Derived class that overrides speak()"""
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    """Derived class that overrides speak()"""
    def speak(self):
        return "Meow!"

# Test overriding
animal = Animal()
dog = Dog()
cat = Cat()

print(f"Animal says: {animal.speak()}")
print(f"Dog says: {dog.speak()}")
print(f"Cat says: {cat.speak()}")
print(f"\\nDog info (inherited): {dog.info()}")
print()

# Example 2: Override with super() Call
print("="*70)
print("Example 2: Using super() to Call Parent Method")
print("="*70)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} vehicle starting..."

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model

    def start(self):
        # Call parent method then add more
        parent_msg = super().start()
        return f"{parent_msg}\\n{self.model} engine engaged!"

# Test super()
car = Car("Toyota", "Camry")
print(car.start())
print()

# Example 3: Override __str__ Method
print("="*70)
print("Example 3: Overriding __str__ for Custom String Representation")
print("="*70)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __str__(self):
        # Override to include employee_id
        return f"Employee(name={self.name}, age={self.age}, id={self.employee_id})"

# Test __str__ override
person = Person("Alice", 30)
employee = Employee("Bob", 25, "E12345")

print(f"Person: {person}")
print(f"Employee: {employee}")
print()

# Example 4: Polymorphism with Method Overriding
print("="*70)
print("Example 4: Polymorphism - Same Interface, Different Behavior")
print("="*70)

class Shape:
    def area(self):
        return 0

    def describe(self):
        return "Generic shape"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        return f"Rectangle ({self.width}x{self.height})"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def describe(self):
        return f"Circle (radius={self.radius})"

# Polymorphism in action
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(10, 2)
]

print("Processing different shapes polymorphically:\\n")
for shape in shapes:
    print(f"{shape.describe()}: Area = {shape.area():.2f}")
print()

# Example 5: Override Multiple Methods
print("="*70)
print("Example 5: Overriding Multiple Methods")
print("="*70)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}"
        return "Insufficient funds"

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.02):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        # Override: add withdrawal fee
        fee = 2
        total = amount + fee
        if total <= self.balance:
            self.balance -= total
            return f"Withdrew ${amount} (${fee} fee applied)"
        return "Insufficient funds"

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Added ${interest:.2f} interest"

# Test multiple overrides
savings = SavingsAccount(1000, 0.05)
print(f"Initial balance: ${savings.get_balance()}")
print(savings.deposit(500))
print(f"Balance: ${savings.get_balance()}")
print(savings.withdraw(100))
print(f"Balance: ${savings.get_balance()}")
print(savings.add_interest())
print(f"Final balance: ${savings.get_balance():.2f}")
print()

# Example 6: Extend Parent Behavior
print("="*70)
print("Example 6: Extending Parent Method Behavior")
print("="*70)

class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class TimestampLogger(Logger):
    def log(self, message):
        # Extend: add timestamp before logging
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super().log(f"[{timestamp}] {message}")

class VerboseLogger(TimestampLogger):
    def log(self, message):
        # Further extend: add separator
        print("="*50)
        super().log(message)
        print("="*50)

# Test extending behavior
basic = Logger()
stamped = TimestampLogger()
verbose = VerboseLogger()

basic.log("Basic message")
print()
stamped.log("Message with timestamp")
print()
verbose.log("Verbose message")
print()

# Example 7: Override with Different Parameters
print("="*70)
print("Example 7: Override with Flexible Parameters")
print("="*70)

class Formatter:
    def format(self, text):
        return text.upper()

class AdvancedFormatter(Formatter):
    def format(self, text, uppercase=True, add_border=False):
        # Override with additional optional parameters
        result = text.upper() if uppercase else text.lower()

        if add_border:
            border = "=" * len(result)
            result = f"{border}\\n{result}\\n{border}"

        return result

# Test flexible override
formatter = Formatter()
adv_formatter = AdvancedFormatter()

text = "Hello World"
print(f"Basic format: {formatter.format(text)}")
print(f"Advanced (upper): {adv_formatter.format(text)}")
print(f"Advanced (lower): {adv_formatter.format(text, uppercase=False)}")
print(f"Advanced (bordered):\\n{adv_formatter.format(text, add_border=True)}")
print()

# Example 8: Check Method Override with isinstance
print("="*70)
print("Example 8: Runtime Type Checking with Overridden Methods")
print("="*70)

class Notification:
    def send(self):
        return "Sending generic notification"

class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email

    def send(self):
        return f"Sending email to {self.email}"

class SMSNotification(Notification):
    def __init__(self, phone):
        self.phone = phone

    def send(self):
        return f"Sending SMS to {self.phone}"

# Test with type checking
notifications = [
    EmailNotification("alice@example.com"),
    SMSNotification("+1-555-0123"),
    Notification()
]

print("Processing notifications:\\n")
for notif in notifications:
    print(f"Type: {type(notif).__name__}")
    print(f"  {notif.send()}")
    print(f"  Is Email? {isinstance(notif, EmailNotification)}")
    print(f"  Is SMS? {isinstance(notif, SMSNotification)}")
    print()

# Example 9: Multiple Inheritance with Overriding
print("="*70)
print("Example 9: Method Overriding with Multiple Inheritance")
print("="*70)

class Flyable:
    def move(self):
        return "Flying through the air"

class Swimmable:
    def move(self):
        return "Swimming in water"

class Duck(Flyable, Swimmable):
    def move(self):
        # Override both - ducks can do both!
        return "Can fly AND swim"

    def fly(self):
        return Flyable.move(self)

    def swim(self):
        return Swimmable.move(self)

# Test multiple inheritance
duck = Duck()
print(f"Duck's move: {duck.move()}")
print(f"Duck flying: {duck.fly()}")
print(f"Duck swimming: {duck.swim()}")
print()

# Example 10: Practical Application - Payment Processing
print("="*70)
print("Example 10: Real-World Use Case - Payment System")
print("="*70)

class PaymentProcessor:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        return f"Processing ${self.amount} payment"

    def validate(self):
        return self.amount > 0

    def get_fee(self):
        return 0

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):
        # Override: add card validation
        if not self.validate():
            return "Invalid amount"
        return f"Processing ${self.amount} via Credit Card ending in {self.card_number[-4:]}"

    def get_fee(self):
        # Override: credit cards have 2.5% fee
        return self.amount * 0.025

class PayPalProcessor(PaymentProcessor):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):
        # Override: add email validation
        if not self.validate() or "@" not in self.email:
            return "Invalid payment details"
        return f"Processing ${self.amount} via PayPal ({self.email})"

    def get_fee(self):
        # Override: PayPal has flat $1 + 2% fee
        return 1.0 + (self.amount * 0.02)

class CryptoProcessor(PaymentProcessor):
    def __init__(self, amount, wallet_address):
        super().__init__(amount)
        self.wallet_address = wallet_address

    def process(self):
        # Override: blockchain processing
        if not self.validate():
            return "Invalid amount"
        return f"Processing ${self.amount} via Crypto to {self.wallet_address[:8]}..."

    def get_fee(self):
        # Override: flat $5 fee for crypto
        return 5.0

# Test payment system
payments = [
    CreditCardProcessor(100, "1234567890123456"),
    PayPalProcessor(50, "user@example.com"),
    CryptoProcessor(200, "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb")
]

print("Payment Processing Summary:\\n")
total_processed = 0
total_fees = 0

for payment in payments:
    print(f"Processor: {type(payment).__name__}")
    print(f"  {payment.process()}")
    fee = payment.get_fee()
    print(f"  Fee: ${fee:.2f}")
    print(f"  Net amount: ${payment.amount - fee:.2f}")
    total_processed += payment.amount
    total_fees += fee
    print()

print("="*70)
print(f"Total Processed: ${total_processed:.2f}")
print(f"Total Fees: ${total_fees:.2f}")
print(f"Net to Recipients: ${total_processed - total_fees:.2f}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Override methods by redefining them in child class")
print("2. Use super() to call parent class methods")
print("3. Overriding enables polymorphism")
print("4. Can override __str__, __init__, and other special methods")
print("5. Child method signatures should match parent (or extend)")
print("6. Overriding customizes inherited behavior")
print("7. Multiple inheritance: leftmost parent takes precedence")
print("8. isinstance() checks object type at runtime")
print("9. Override to add validation, logging, or special handling")
print("10. Essential pattern for flexible, extensible code")
print("="*70)
'''

# Upgrade Lesson 123: Object Method Calls
lesson123['fullSolution'] = '''"""
Object Method Calls

Master calling methods on objects in Python. Learn instance method invocation,
method chaining, passing objects between methods, and best practices for
clean object-oriented code. Essential for working with classes effectively.

**Zero Package Installation Required**
"""

# Example 1: Basic Method Calls on Objects
print("="*70)
print("Example 1: Basic Object Method Invocation")
print("="*70)

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value
        return self.result

    def subtract(self, value):
        self.result -= value
        return self.result

    def multiply(self, value):
        self.result *= value
        return self.result

    def reset(self):
        self.result = 0
        return self.result

# Create object and call methods
calc = Calculator()
print(f"Initial result: {calc.result}")

calc.add(10)
print(f"After add(10): {calc.result}")

calc.multiply(5)
print(f"After multiply(5): {calc.result}")

calc.subtract(20)
print(f"After subtract(20): {calc.result}")

calc.reset()
print(f"After reset(): {calc.result}")
print()

# Example 2: Method Chaining
print("="*70)
print("Example 2: Method Chaining Pattern")
print("="*70)

class ChainableCalculator:
    def __init__(self):
        self.value = 0

    def add(self, num):
        self.value += num
        return self  # Return self for chaining

    def subtract(self, num):
        self.value -= num
        return self

    def multiply(self, num):
        self.value *= num
        return self

    def divide(self, num):
        if num != 0:
            self.value /= num
        return self

    def get_value(self):
        return self.value

# Chain multiple method calls
calc = ChainableCalculator()
result = calc.add(10).multiply(5).subtract(20).divide(2).get_value()

print(f"Result of chain: add(10).multiply(5).subtract(20).divide(2)")
print(f"Final value: {result}")

# Another chain
calc2 = ChainableCalculator()
result2 = calc2.add(100).subtract(25).multiply(2).get_value()
print(f"\\nAnother chain: add(100).subtract(25).multiply(2)")
print(f"Final value: {result2}")
print()

# Example 3: Calling Methods with Different Parameters
print("="*70)
print("Example 3: Methods with Various Parameter Types")
print("="*70)

class TextProcessor:
    def __init__(self, text=""):
        self.text = text

    def set_text(self, text):
        self.text = text

    def append(self, suffix):
        self.text += suffix

    def prepend(self, prefix):
        self.text = prefix + self.text

    def repeat(self, times):
        self.text *= times

    def get_text(self):
        return self.text

# Test different method calls
processor = TextProcessor("Hello")
print(f"Initial text: '{processor.get_text()}'")

processor.append(" World")
print(f"After append(' World'): '{processor.get_text()}'")

processor.prepend(">>> ")
print(f"After prepend('>>> '): '{processor.get_text()}'")

processor.repeat(2)
print(f"After repeat(2): '{processor.get_text()}'")

processor.set_text("New text")
print(f"After set_text('New text'): '{processor.get_text()}'")
print()

# Example 4: Calling Methods from Other Methods
print("="*70)
print("Example 4: Internal Method Calls (self.method())")
print("="*70)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def _log_transaction(self, transaction):
        """Private helper method"""
        self.transactions.append(transaction)

    def deposit(self, amount):
        self.balance += amount
        self._log_transaction(f"Deposit: +${amount}")
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self._log_transaction(f"Withdraw: -${amount}")
            return self.balance
        else:
            self._log_transaction(f"Failed withdraw: ${amount}")
            return None

    def get_statement(self):
        return "\\n".join(self.transactions)

# Test internal method calls
account = BankAccount(1000)
print(f"Initial balance: ${account.balance}")

account.deposit(500)
print(f"After deposit(500): ${account.balance}")

account.withdraw(200)
print(f"After withdraw(200): ${account.balance}")

account.withdraw(2000)  # Should fail
print(f"After failed withdraw(2000): ${account.balance}")

print(f"\\nTransaction statement:\\n{account.get_statement()}")
print()

# Example 5: Passing Objects to Methods
print("="*70)
print("Example 5: Passing Objects as Method Arguments")
print("="*70)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return (dx**2 + dy**2) ** 0.5

    def move_towards(self, other_point, distance):
        total_dist = self.distance_to(other_point)
        if total_dist == 0:
            return

        ratio = distance / total_dist
        self.x += (other_point.x - self.x) * ratio
        self.y += (other_point.y - self.y) * ratio

    def __str__(self):
        return f"Point({self.x:.2f}, {self.y:.2f})"

# Test passing objects
p1 = Point(0, 0)
p2 = Point(10, 10)

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Distance: {p1.distance_to(p2):.2f}")

p1.move_towards(p2, 5)
print(f"\\nAfter moving p1 towards p2 by 5 units:")
print(f"Point 1: {p1}")
print(f"New distance: {p1.distance_to(p2):.2f}")
print()

# Example 6: Method Calls on Multiple Objects
print("="*70)
print("Example 6: Working with Multiple Objects")
print("="*70)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self, hours):
        improvement = hours * 2
        self.grade = min(100, self.grade + improvement)
        return f"{self.name} studied {hours}h, grade now: {self.grade}"

    def compare_with(self, other_student):
        if self.grade > other_student.grade:
            return f"{self.name} has higher grade than {other_student.name}"
        elif self.grade < other_student.grade:
            return f"{other_student.name} has higher grade than {self.name}"
        else:
            return f"{self.name} and {other_student.name} have same grade"

# Create multiple students
alice = Student("Alice", 75)
bob = Student("Bob", 82)
charlie = Student("Charlie", 78)

students = [alice, bob, charlie]

print("Initial grades:")
for student in students:
    print(f"  {student.name}: {student.grade}")

print("\\nStudying...")
print(alice.study(3))
print(bob.study(2))
print(charlie.study(4))

print("\\nComparisons:")
print(alice.compare_with(bob))
print(charlie.compare_with(bob))
print()

# Example 7: Conditional Method Calls
print("="*70)
print("Example 7: Conditional Method Invocation")
print("="*70)

class StatusTracker:
    def __init__(self):
        self.status = "idle"
        self.errors = []

    def start(self):
        if self.status == "idle":
            self.status = "running"
            return "Started successfully"
        return "Already running"

    def stop(self):
        if self.status == "running":
            self.status = "idle"
            return "Stopped successfully"
        return "Not running"

    def report_error(self, error_msg):
        self.errors.append(error_msg)
        self.status = "error"
        return f"Error reported: {error_msg}"

    def reset(self):
        self.status = "idle"
        self.errors.clear()
        return "Reset complete"

    def get_status(self):
        if self.errors:
            return f"{self.status} ({len(self.errors)} errors)"
        return self.status

# Test conditional methods
tracker = StatusTracker()
print(f"Status: {tracker.get_status()}")

print(tracker.start())
print(f"Status: {tracker.get_status()}")

print(tracker.start())  # Try again
print(f"Status: {tracker.get_status()}")

print(tracker.report_error("Connection failed"))
print(f"Status: {tracker.get_status()}")

print(tracker.reset())
print(f"Status: {tracker.get_status()}")
print()

# Example 8: Method Calls with Return Values
print("="*70)
print("Example 8: Using Method Return Values")
print("="*70)

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
        return len(self.items)  # Return new count

    def get_total(self):
        return sum(item["price"] for item in self.items)

    def get_item_count(self):
        return len(self.items)

    def clear(self):
        count = len(self.items)
        self.items.clear()
        return count  # Return how many were removed

# Use return values
cart = ShoppingCart()

item_count = cart.add_item("Laptop", 999.99)
print(f"Added laptop, total items: {item_count}")

item_count = cart.add_item("Mouse", 29.99)
print(f"Added mouse, total items: {item_count}")

item_count = cart.add_item("Keyboard", 79.99)
print(f"Added keyboard, total items: {item_count}")

total = cart.get_total()
print(f"\\nCart total: ${total:.2f}")

cleared = cart.clear()
print(f"Cleared {cleared} items")
print(f"New total: ${cart.get_total():.2f}")
print()

# Example 9: Method Calls with *args and **kwargs
print("="*70)
print("Example 9: Flexible Method Parameters")
print("="*70)

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, *messages, level="INFO"):
        combined = " ".join(str(m) for m in messages)
        entry = f"[{level}] {combined}"
        self.logs.append(entry)
        print(entry)

    def log_dict(self, **kwargs):
        items = [f"{k}={v}" for k, v in kwargs.items()]
        entry = "[DATA] " + ", ".join(items)
        self.logs.append(entry)
        print(entry)

    def get_logs(self):
        return self.logs

# Test flexible parameters
logger = Logger()

logger.log("System starting")
logger.log("User", "Alice", "logged in", level="INFO")
logger.log("Failed to connect", "to database", level="ERROR")

logger.log_dict(user="Bob", action="purchase", amount=50.00)
logger.log_dict(status="complete", items=3)

print(f"\\nTotal logs: {len(logger.get_logs())}")
print()

# Example 10: Practical Application - Task Manager
print("="*70)
print("Example 10: Real-World Use Case - Task Management System")
print("="*70)

class Task:
    def __init__(self, title, priority="medium"):
        self.title = title
        self.priority = priority
        self.completed = False

    def complete(self):
        self.completed = True
        return f"Task '{self.title}' completed"

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.title} ({self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority="medium"):
        task = Task(title, priority)
        self.tasks.append(task)
        return f"Added: {task}"

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index].complete()
        return "Invalid task index"

    def list_tasks(self):
        if not self.tasks:
            return "No tasks"
        return "\\n".join(f"{i+1}. {task}" for i, task in enumerate(self.tasks))

    def get_pending_count(self):
        return sum(1 for task in self.tasks if not task.completed)

    def get_completed_count(self):
        return sum(1 for task in self.tasks if task.completed)

    def clear_completed(self):
        original_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed = original_count - len(self.tasks)
        return f"Removed {removed} completed tasks"

# Test task manager
manager = TaskManager()

print("Adding tasks...")
print(manager.add_task("Write documentation", "high"))
print(manager.add_task("Fix bug #123", "high"))
print(manager.add_task("Update README", "low"))
print(manager.add_task("Review pull requests", "medium"))

print(f"\\nAll tasks:\\n{manager.list_tasks()}")

print(f"\\nCompleting tasks...")
print(manager.complete_task(0))
print(manager.complete_task(2))

print(f"\\nUpdated task list:\\n{manager.list_tasks()}")

print(f"\\nStats:")
print(f"  Pending: {manager.get_pending_count()}")
print(f"  Completed: {manager.get_completed_count()}")

print(f"\\n{manager.clear_completed()}")

print(f"\\nFinal task list:\\n{manager.list_tasks()}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Call methods using: object.method_name(arguments)")
print("2. Methods can return values or None")
print("3. Method chaining: return self for fluent interface")
print("4. Internal calls: use self.method() within class")
print("5. Pass objects as arguments to other methods")
print("6. Methods can modify object state (instance variables)")
print("7. Use return values to communicate success/results")
print("8. Conditional method calls based on object state")
print("9. Methods can accept *args, **kwargs for flexibility")
print("10. Good method design makes code readable and maintainable")
print("="*70)
'''

# Upgrade Lesson 124: Range Function
lesson124['fullSolution'] = '''"""
Range Function

Master Python's range() function for generating number sequences. Learn
basic ranges, step values, reverse ranges, and practical applications in
loops and list generation. Essential for iteration and sequence creation.

**Zero Package Installation Required**
"""

# Example 1: Basic Range Usage
print("="*70)
print("Example 1: Basic range() Function")
print("="*70)

# range(stop) - from 0 to stop-1
print("range(5):")
for i in range(5):
    print(f"  {i}", end=" ")
print("\\n")

# range(start, stop) - from start to stop-1
print("range(2, 8):")
for i in range(2, 8):
    print(f"  {i}", end=" ")
print("\\n")

# range(start, stop, step) - with custom step
print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"  {i}", end=" ")
print("\\n")
print()

# Example 2: Convert Range to List
print("="*70)
print("Example 2: Converting range() to Lists")
print("="*70)

# Range is lazy - convert to list to see all values
list1 = list(range(10))
print(f"list(range(10)): {list1}")

list2 = list(range(5, 15))
print(f"list(range(5, 15)): {list2}")

list3 = list(range(0, 20, 3))
print(f"list(range(0, 20, 3)): {list3}")

list4 = list(range(10, 100, 10))
print(f"list(range(10, 100, 10)): {list4}")
print()

# Example 3: Reverse Ranges
print("="*70)
print("Example 3: Reverse Ranges with Negative Step")
print("="*70)

# Countdown
print("Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(f"  {i}", end=" ")
print("\\n")

# Reverse range
print("range(20, 10, -1):")
reverse_list = list(range(20, 10, -1))
print(f"  {reverse_list}")

# Every other number backwards
print("\\nrange(10, 0, -2):")
reverse_step = list(range(10, 0, -2))
print(f"  {reverse_step}")
print()

# Example 4: Range with Enumerate
print("="*70)
print("Example 4: Combining range() with enumerate()")
print("="*70)

items = ["apple", "banana", "cherry", "date"]

print("Using range(len(items)):")
for i in range(len(items)):
    print(f"  Index {i}: {items[i]}")

print("\\nUsing enumerate (better):")
for i, item in enumerate(items):
    print(f"  Index {i}: {item}")
print()

# Example 5: Range in List Comprehensions
print("="*70)
print("Example 5: range() with List Comprehensions")
print("="*70)

# Squares
squares = [x**2 for x in range(10)]
print(f"Squares of 0-9: {squares}")

# Even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers 0-19: {evens}")

# Multiplication table
mult_5 = [x * 5 for x in range(1, 11)]
print(f"5 times table: {mult_5}")

# Filtered with condition
filtered = [x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0]
print(f"Numbers 1-50 divisible by both 3 and 5: {filtered}")
print()

# Example 6: Range for Loop Counters
print("="*70)
print("Example 6: Using range() as Loop Counter")
print("="*70)

# Simple counter
print("Print stars:")
for i in range(5):
    print("  " + "*" * (i + 1))

print("\\nNumbered list:")
items = ["Task A", "Task B", "Task C", "Task D"]
for i in range(len(items)):
    print(f"  {i+1}. {items[i]}")

print("\\nReverse countdown:")
for i in range(5, 0, -1):
    print(f"  {i}...", end=" ")
print("Blast off!")
print()

# Example 7: Range with Step Values
print("="*70)
print("Example 7: Different Step Values")
print("="*70)

# Step of 5
step_5 = list(range(0, 50, 5))
print(f"Step 5 (0-50): {step_5}")

# Step of 10
step_10 = list(range(0, 100, 10))
print(f"Step 10 (0-100): {step_10}")

# Negative step
neg_step = list(range(100, 0, -10))
print(f"Reverse step 10 (100-0): {neg_step}")

# Large step
large_step = list(range(0, 1000, 100))
print(f"Step 100 (0-1000): {large_step}")
print()

# Example 8: Range Properties and Methods
print("="*70)
print("Example 8: Range Object Properties")
print("="*70)

r = range(5, 20, 2)

print(f"Range object: {r}")
print(f"Start: {r.start}")
print(f"Stop: {r.stop}")
print(f"Step: {r.step}")
print(f"Length: {len(r)}")
print(f"As list: {list(r)}")

# Check membership
print(f"\\n7 in range? {7 in r}")
print(f"11 in range? {11 in r}")

# Index access
print(f"\\nFirst element r[0]: {r[0]}")
print(f"Last element r[-1]: {r[-1]}")
print(f"Third element r[2]: {r[2]}")
print()

# Example 9: Range for Matrix/Grid Generation
print("="*70)
print("Example 9: Using range() for Grids and Matrices")
print("="*70)

# Simple grid
print("3x4 grid:")
for row in range(3):
    for col in range(4):
        print(f"({row},{col})", end=" ")
    print()

# Multiplication table
print("\\nMultiplication table (1-5):")
print("    ", end="")
for i in range(1, 6):
    print(f"{i:4}", end="")
print()

for i in range(1, 6):
    print(f"{i:4}", end="")
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()

# Number pyramid
print("\\nNumber pyramid:")
for i in range(1, 6):
    print("  " * (5-i), end="")
    for j in range(i):
        print(f"{j+1} ", end="")
    print()
print()

# Example 10: Practical Application - Data Processing
print("="*70)
print("Example 10: Real-World Use Case - Batch Processing")
print("="*70)

# Simulate processing items in batches
items = list(range(1, 26))  # 25 items
batch_size = 5

print(f"Processing {len(items)} items in batches of {batch_size}:\\n")

for batch_num in range(0, len(items), batch_size):
    batch = items[batch_num:batch_num + batch_size]
    print(f"Batch {batch_num//batch_size + 1}: {batch}")

    # Simulate processing
    batch_sum = sum(batch)
    batch_avg = batch_sum / len(batch)
    print(f"  Sum: {batch_sum}, Average: {batch_avg:.1f}")
    print()

# Generate report
print("="*70)
print("BATCH PROCESSING SUMMARY")
print("="*70)
total_batches = (len(items) + batch_size - 1) // batch_size
print(f"Total items: {len(items)}")
print(f"Batch size: {batch_size}")
print(f"Total batches: {total_batches}")
print(f"Items per batch: {[len(items[i:i+batch_size]) for i in range(0, len(items), batch_size)]}")

# Time-based range example
print("\\n" + "="*70)
print("Time-based scheduling:")
print("="*70)

# Schedule tasks every 30 minutes for 8 hours
start_time = 9  # 9 AM
end_time = 17   # 5 PM

print("Task schedule (every 30 min):")
for minutes in range(0, (end_time - start_time) * 60, 30):
    hours = start_time + minutes // 60
    mins = minutes % 60
    print(f"  {hours:02d}:{mins:02d} - Execute scheduled task")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. range(stop) - Generate 0 to stop-1")
print("2. range(start, stop) - Generate start to stop-1")
print("3. range(start, stop, step) - Custom increment")
print("4. Negative step for reverse/countdown ranges")
print("5. range() is lazy - use list() to see all values")
print("6. Use len(range_obj) to get count of values")
print("7. Check membership with 'in' operator")
print("8. Access start, stop, step properties")
print("9. Perfect for loop counters and iterations")
print("10. Memory efficient - generates values on demand")
print("="*70)
'''

# Save progress and print summary
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Upgrade Lesson 125: Simple Calculator Functions
lesson125['fullSolution'] = '''"""
Simple Calculator Functions

Master building calculator functions in Python. Learn to create arithmetic
operations, handle edge cases, combine multiple operations, and build a
complete calculator system. Essential foundation for function design.

**Zero Package Installation Required**
"""

# Example 1: Basic Arithmetic Functions
print("="*70)
print("Example 1: Basic Calculator Functions")
print("="*70)

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Test basic operations
x, y = 10, 3

print(f"Numbers: {x}, {y}")
print(f"add({x}, {y}) = {add(x, y)}")
print(f"subtract({x}, {y}) = {subtract(x, y)}")
print(f"multiply({x}, {y}) = {multiply(x, y)}")
print(f"divide({x}, {y}) = {divide(x, y):.2f}")
print(f"divide({x}, 0) = {divide(x, 0)}")
print()

# Example 2: Extended Arithmetic Operations
print("="*70)
print("Example 2: Extended Calculator Operations")
print("="*70)

def power(base, exponent):
    """Raise base to exponent"""
    return base ** exponent

def modulo(a, b):
    """Calculate remainder of a divided by b"""
    if b == 0:
        return "Error: Division by zero"
    return a % b

def integer_divide(a, b):
    """Integer division (floor division)"""
    if b == 0:
        return "Error: Division by zero"
    return a // b

def absolute(n):
    """Get absolute value"""
    return abs(n)

# Test extended operations
a, b = 12, 5

print(f"Numbers: {a}, {b}")
print(f"power({a}, {b}) = {power(a, b)}")
print(f"modulo({a}, {b}) = {modulo(a, b)}")
print(f"integer_divide({a}, {b}) = {integer_divide(a, b)}")
print(f"absolute(-{a}) = {absolute(-a)}")
print()

# Example 3: Calculator with Operation Parameter
print("="*70)
print("Example 3: Generic Calculate Function")
print("="*70)

def calculate(a, b, operation):
    """Perform operation based on string parameter"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return f"Error: Unknown operation '{operation}'"

# Test generic calculator
print(f"calculate(15, 3, 'add') = {calculate(15, 3, 'add')}")
print(f"calculate(15, 3, 'subtract') = {calculate(15, 3, 'subtract')}")
print(f"calculate(15, 3, 'multiply') = {calculate(15, 3, 'multiply')}")
print(f"calculate(15, 3, 'divide') = {calculate(15, 3, 'divide')}")
print(f"calculate(15, 3, 'invalid') = {calculate(15, 3, 'invalid')}")
print()

# Example 4: Calculator with Dictionary Dispatch
print("="*70)
print("Example 4: Dictionary-Based Calculator")
print("="*70)

def calculator_dispatch(a, b, operation):
    """Use dictionary for operation dispatch"""
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error",
        '**': lambda x, y: x ** y,
        '%': lambda x, y: x % y if y != 0 else "Error"
    }

    if operation in operations:
        return operations[operation](a, b)
    return f"Error: Unknown operation '{operation}'"

# Test dispatch calculator
print(f"calculator_dispatch(10, 5, '+') = {calculator_dispatch(10, 5, '+')}")
print(f"calculator_dispatch(10, 5, '-') = {calculator_dispatch(10, 5, '-')}")
print(f"calculator_dispatch(10, 5, '*') = {calculator_dispatch(10, 5, '*')}")
print(f"calculator_dispatch(10, 5, '/') = {calculator_dispatch(10, 5, '/')}")
print(f"calculator_dispatch(10, 5, '**') = {calculator_dispatch(10, 5, '**')}")
print(f"calculator_dispatch(10, 5, '%') = {calculator_dispatch(10, 5, '%')}")
print()

# Example 5: Chain Calculator
print("="*70)
print("Example 5: Chain Calculator for Multiple Operations")
print("="*70)

def chain_calculate(start, *operations):
    """Apply multiple operations in sequence
    operations should be tuples of (operator, value)
    """
    result = start
    for operator, value in operations:
        if operator == '+':
            result += value
        elif operator == '-':
            result -= value
        elif operator == '*':
            result *= value
        elif operator == '/':
            if value != 0:
                result /= value
            else:
                return "Error: Division by zero"
        elif operator == '**':
            result **= value
    return result

# Test chain calculator
result1 = chain_calculate(10, ('+', 5), ('*', 2), ('-', 8))
print(f"Start with 10: +5, *2, -8 = {result1}")

result2 = chain_calculate(100, ('/', 4), ('+', 10), ('*', 3))
print(f"Start with 100: /4, +10, *3 = {result2}")

result3 = chain_calculate(2, ('**', 3), ('+', 10), ('/', 2))
print(f"Start with 2: **3, +10, /2 = {result3}")
print()

# Example 6: Calculator with History
print("="*70)
print("Example 6: Calculator with Operation History")
print("="*70)

class CalculatorWithHistory:
    def __init__(self):
        self.history = []
        self.result = 0

    def add(self, value):
        self.result += value
        self.history.append(f"+ {value} = {self.result}")
        return self.result

    def subtract(self, value):
        self.result -= value
        self.history.append(f"- {value} = {self.result}")
        return self.result

    def multiply(self, value):
        self.result *= value
        self.history.append(f"* {value} = {self.result}")
        return self.result

    def divide(self, value):
        if value != 0:
            self.result /= value
            self.history.append(f"/ {value} = {self.result}")
        return self.result

    def get_history(self):
        return "\\n".join(self.history)

    def reset(self):
        self.result = 0
        self.history.clear()

# Test history calculator
calc = CalculatorWithHistory()
calc.add(50)
calc.multiply(2)
calc.subtract(30)
calc.divide(7)

print(f"Final result: {calc.result:.2f}")
print(f"\\nHistory:\\n{calc.get_history()}")
print()

# Example 7: Scientific Calculator Functions
print("="*70)
print("Example 7: Scientific Calculator Operations")
print("="*70)

import math

def square_root(n):
    """Calculate square root"""
    if n < 0:
        return "Error: Cannot calculate square root of negative number"
    return math.sqrt(n)

def factorial(n):
    """Calculate factorial"""
    if n < 0:
        return "Error: Factorial undefined for negative numbers"
    return math.factorial(n)

def logarithm(n, base=math.e):
    """Calculate logarithm"""
    if n <= 0:
        return "Error: Logarithm undefined for non-positive numbers"
    if base == math.e:
        return math.log(n)
    return math.log(n, base)

def sine(degrees):
    """Calculate sine (input in degrees)"""
    radians = math.radians(degrees)
    return math.sin(radians)

# Test scientific operations
print(f"square_root(16) = {square_root(16)}")
print(f"square_root(25) = {square_root(25)}")
print(f"factorial(5) = {factorial(5)}")
print(f"factorial(7) = {factorial(7)}")
print(f"logarithm(100, 10) = {logarithm(100, 10):.2f}")
print(f"logarithm(math.e) = {logarithm(math.e):.2f}")
print(f"sine(30) = {sine(30):.2f}")
print(f"sine(90) = {sine(90):.2f}")
print()

# Example 8: Percentage Calculator
print("="*70)
print("Example 8: Percentage Calculations")
print("="*70)

def calculate_percentage(value, total):
    """Calculate what percentage value is of total"""
    if total == 0:
        return "Error: Total cannot be zero"
    return (value / total) * 100

def percentage_of(percentage, total):
    """Calculate percentage of a total"""
    return (percentage / 100) * total

def percentage_increase(old_value, new_value):
    """Calculate percentage increase"""
    if old_value == 0:
        return "Error: Old value cannot be zero"
    return ((new_value - old_value) / old_value) * 100

def add_percentage(value, percentage):
    """Add percentage to a value"""
    return value + (value * percentage / 100)

# Test percentage calculations
print(f"What % is 25 of 200? {calculate_percentage(25, 200):.1f}%")
print(f"What is 15% of 200? {percentage_of(15, 200):.2f}")
print(f"% increase from 50 to 75: {percentage_increase(50, 75):.1f}%")
print(f"Add 20% to 100: {add_percentage(100, 20):.2f}")
print()

# Example 9: Number Rounding Functions
print("="*70)
print("Example 9: Rounding and Precision")
print("="*70)

def round_to_places(n, places):
    """Round to specified decimal places"""
    return round(n, places)

def round_to_nearest(n, nearest):
    """Round to nearest specified value"""
    return round(n / nearest) * nearest

def ceiling(n):
    """Round up to nearest integer"""
    return math.ceil(n)

def floor(n):
    """Round down to nearest integer"""
    return math.floor(n)

# Test rounding
value = 123.456

print(f"Value: {value}")
print(f"Round to 2 places: {round_to_places(value, 2)}")
print(f"Round to 1 place: {round_to_places(value, 1)}")
print(f"Round to nearest 10: {round_to_nearest(value, 10)}")
print(f"Round to nearest 5: {round_to_nearest(value, 5)}")
print(f"Ceiling: {ceiling(value)}")
print(f"Floor: {floor(value)}")
print()

# Example 10: Practical Application - Complete Calculator
print("="*70)
print("Example 10: Real-World Use Case - Complete Calculator System")
print("="*70)

class Calculator:
    """Complete calculator with multiple operation types"""

    @staticmethod
    def basic_operation(a, b, op):
        """Perform basic arithmetic"""
        ops = {
            '+': a + b,
            '-': a - b,
            '*': a * b,
            '/': a / b if b != 0 else "Error: Division by zero",
            '**': a ** b,
            '%': a % b if b != 0 else "Error"
        }
        return ops.get(op, "Unknown operation")

    @staticmethod
    def average(*numbers):
        """Calculate average of any number of values"""
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    @staticmethod
    def variance(*numbers):
        """Calculate variance"""
        if not numbers:
            return 0
        avg = sum(numbers) / len(numbers)
        return sum((x - avg) ** 2 for x in numbers) / len(numbers)

    @staticmethod
    def standard_deviation(*numbers):
        """Calculate standard deviation"""
        return math.sqrt(Calculator.variance(*numbers))

# Test complete calculator
calc = Calculator()

print("Basic Operations:")
print(f"  100 + 25 = {calc.basic_operation(100, 25, '+')}")
print(f"  100 - 25 = {calc.basic_operation(100, 25, '-')}")
print(f"  100 * 25 = {calc.basic_operation(100, 25, '*')}")
print(f"  100 / 25 = {calc.basic_operation(100, 25, '/')}")
print(f"  2 ** 10 = {calc.basic_operation(2, 10, '**')}")

data = [10, 20, 30, 40, 50]
print(f"\\nStatistical Operations on {data}:")
print(f"  Average: {calc.average(*data):.2f}")
print(f"  Variance: {calc.variance(*data):.2f}")
print(f"  Std Deviation: {calc.standard_deviation(*data):.2f}")

# Financial calculation example
price = 99.99
tax_rate = 8.5
discount = 10

print(f"\\nFinancial Calculation:")
print(f"  Original price: ${price:.2f}")

discounted = price - percentage_of(discount, price)
print(f"  After {discount}% discount: ${discounted:.2f}")

final = discounted + percentage_of(tax_rate, discounted)
print(f"  After {tax_rate}% tax: ${final:.2f}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Create focused functions for each operation")
print("2. Handle edge cases (division by zero, negative sqrt)")
print("3. Use descriptive function names: add(), multiply()")
print("4. Return error messages for invalid operations")
print("5. Chain operations for complex calculations")
print("6. Use lambda functions for simple operations")
print("7. Dictionary dispatch for operation selection")
print("8. Keep history for debugging and tracing")
print("9. Static methods for utility calculator classes")
print("10. Test all functions with various inputs")
print("="*70)
'''

# Upgrade Lesson 126: Temperature Conversion Functions
lesson126['fullSolution'] = '''"""
Temperature Conversion Functions

Master temperature conversion functions in Python. Learn to convert between
Celsius, Fahrenheit, and Kelvin, handle edge cases, format output, and build
complete conversion utilities. Essential for scientific and practical applications.

**Zero Package Installation Required**
"""

# Example 1: Basic Celsius to Fahrenheit
print("="*70)
print("Example 1: Celsius to Fahrenheit Conversion")
print("="*70)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

# Test conversion
temps_c = [0, 10, 20, 30, 37, 100]

print("Celsius to Fahrenheit:")
for temp in temps_c:
    fahrenheit = celsius_to_fahrenheit(temp)
    print(f"  {temp:3.0f}°C = {fahrenheit:6.2f}°F")
print()

# Example 2: Basic Fahrenheit to Celsius
print("="*70)
print("Example 2: Fahrenheit to Celsius Conversion")
print("="*70)

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

# Test conversion
temps_f = [32, 50, 68, 86, 98.6, 212]

print("Fahrenheit to Celsius:")
for temp in temps_f:
    celsius = fahrenheit_to_celsius(temp)
    print(f"  {temp:6.1f}°F = {celsius:5.2f}°C")
print()

# Example 3: Kelvin Conversions
print("="*70)
print("Example 3: Kelvin Conversion Functions")
print("="*70)

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Test Kelvin conversions
print("Kelvin conversions:")
print(f"  0°C = {celsius_to_kelvin(0):.2f}K")
print(f"  100°C = {celsius_to_kelvin(100):.2f}K")
print(f"  273.15K = {kelvin_to_celsius(273.15):.2f}°C")
print(f"  373.15K = {kelvin_to_celsius(373.15):.2f}°C")
print(f"  32°F = {fahrenheit_to_kelvin(32):.2f}K")
print(f"  300K = {kelvin_to_fahrenheit(300):.2f}°F")
print()

# Example 4: Generic Temperature Converter
print("="*70)
print("Example 4: Generic Multi-Scale Converter")
print("="*70)

def convert_temperature(value, from_scale, to_scale):
    """Convert temperature between any scales"""
    # Normalize to Celsius first
    if from_scale == 'C':
        celsius = value
    elif from_scale == 'F':
        celsius = (value - 32) * 5/9
    elif from_scale == 'K':
        celsius = value - 273.15
    else:
        return f"Unknown scale: {from_scale}"

    # Convert from Celsius to target scale
    if to_scale == 'C':
        return celsius
    elif to_scale == 'F':
        return (celsius * 9/5) + 32
    elif to_scale == 'K':
        return celsius + 273.15
    else:
        return f"Unknown scale: {to_scale}"

# Test generic converter
conversions = [
    (0, 'C', 'F'),
    (32, 'F', 'C'),
    (100, 'C', 'K'),
    (300, 'K', 'F'),
    (98.6, 'F', 'K'),
    (273.15, 'K', 'C')
]

print("Generic temperature converter:")
for value, from_s, to_s in conversions:
    result = convert_temperature(value, from_s, to_s)
    print(f"  {value:.2f}°{from_s} = {result:.2f}°{to_s}")
print()

# Example 5: Temperature with Validation
print("="*70)
print("Example 5: Temperature Conversion with Validation")
print("="*70)

def convert_with_validation(value, from_scale, to_scale):
    """Convert temperature with absolute zero validation"""
    # Check for below absolute zero
    absolute_zeros = {'C': -273.15, 'F': -459.67, 'K': 0}

    if from_scale in absolute_zeros:
        if value < absolute_zeros[from_scale]:
            return f"Error: Below absolute zero for {from_scale}"

    return convert_temperature(value, from_scale, to_scale)

# Test with validation
test_temps = [
    (0, 'K', 'C'),      # Valid
    (-300, 'C', 'F'),   # Invalid - below absolute zero
    (100, 'C', 'F'),    # Valid
    (-500, 'F', 'C'),   # Invalid
    (300, 'K', 'F'),    # Valid
]

print("Temperature conversion with validation:")
for value, from_s, to_s in test_temps:
    result = convert_with_validation(value, from_s, to_s)
    if isinstance(result, float):
        print(f"  {value:.2f}°{from_s} = {result:.2f}°{to_s}")
    else:
        print(f"  {value:.2f}°{from_s}: {result}")
print()

# Example 6: Formatted Temperature Output
print("="*70)
print("Example 6: Formatted Temperature Conversion")
print("="*70)

def format_temperature(value, scale):
    """Format temperature with proper symbol"""
    symbols = {'C': '°C', 'F': '°F', 'K': 'K'}
    symbol = symbols.get(scale, '')
    return f"{value:.2f}{symbol}"

def convert_and_format(value, from_scale, to_scale):
    """Convert and return formatted string"""
    result = convert_temperature(value, from_scale, to_scale)
    if isinstance(result, str):  # Error message
        return result
    return f"{format_temperature(value, from_scale)} = {format_temperature(result, to_scale)}"

# Test formatted output
print("Formatted temperature conversions:")
conversions = [
    (0, 'C', 'F'),
    (100, 'F', 'C'),
    (300, 'K', 'C'),
    (37, 'C', 'F'),
    (212, 'F', 'K')
]

for value, from_s, to_s in conversions:
    print(f"  {convert_and_format(value, from_s, to_s)}")
print()

# Example 7: Temperature Range Converter
print("="*70)
print("Example 7: Convert Temperature Ranges")
print("="*70)

def convert_range(start, end, from_scale, to_scale, step=1):
    """Convert a range of temperatures"""
    results = []
    current = start
    while current <= end:
        converted = convert_temperature(current, from_scale, to_scale)
        results.append((current, converted))
        current += step
    return results

# Test range conversion
print("Water phase changes (Celsius to Fahrenheit):")
water_temps = convert_range(0, 100, 'C', 'F', 20)
for celsius, fahrenheit in water_temps:
    print(f"  {celsius:3.0f}°C = {fahrenheit:6.2f}°F")

print("\\nRoom temperature range (Fahrenheit to Celsius):")
room_temps = convert_range(65, 75, 'F', 'C', 2)
for fahrenheit, celsius in room_temps:
    print(f"  {fahrenheit:3.0f}°F = {celsius:5.2f}°C")
print()

# Example 8: Temperature Classification
print("="*70)
print("Example 8: Temperature Classification")
print("="*70)

def classify_temperature(celsius):
    """Classify temperature into categories"""
    if celsius < 0:
        return "Freezing"
    elif celsius < 10:
        return "Cold"
    elif celsius < 20:
        return "Cool"
    elif celsius < 30:
        return "Warm"
    else:
        return "Hot"

def convert_and_classify(value, from_scale):
    """Convert to Celsius and classify"""
    celsius = convert_temperature(value, from_scale, 'C')
    category = classify_temperature(celsius)
    return f"{format_temperature(value, from_scale)} ({format_temperature(celsius, 'C')}) - {category}"

# Test classification
temps_to_classify = [
    (-10, 'C'),
    (5, 'C'),
    (15, 'C'),
    (25, 'C'),
    (35, 'C'),
    (32, 'F'),
    (68, 'F'),
    (300, 'K')
]

print("Temperature classification:")
for temp, scale in temps_to_classify:
    print(f"  {convert_and_classify(temp, scale)}")
print()

# Example 9: Bulk Temperature Conversion
print("="*70)
print("Example 9: Bulk Temperature Data Conversion")
print("="*70)

def convert_temperature_list(temperatures, from_scale, to_scale):
    """Convert a list of temperatures"""
    return [convert_temperature(temp, from_scale, to_scale) for temp in temperatures]

def get_temperature_stats(temperatures, scale='C'):
    """Get statistics for temperature data"""
    if not temperatures:
        return {}

    return {
        'min': min(temperatures),
        'max': max(temperatures),
        'average': sum(temperatures) / len(temperatures),
        'range': max(temperatures) - min(temperatures),
        'scale': scale
    }

# Test bulk conversion
daily_temps_f = [65, 68, 72, 70, 75, 73, 69]

print(f"Daily temperatures (°F): {daily_temps_f}")

daily_temps_c = convert_temperature_list(daily_temps_f, 'F', 'C')
print(f"Converted to °C: {[f'{t:.1f}' for t in daily_temps_c]}")

stats = get_temperature_stats(daily_temps_c, 'C')
print(f"\\nStatistics (°C):")
print(f"  Min: {stats['min']:.2f}°C")
print(f"  Max: {stats['max']:.2f}°C")
print(f"  Average: {stats['average']:.2f}°C")
print(f"  Range: {stats['range']:.2f}°C")
print()

# Example 10: Practical Application - Weather Station
print("="*70)
print("Example 10: Real-World Use Case - Weather Station System")
print("="*70)

class WeatherStation:
    """Temperature monitoring and conversion system"""

    def __init__(self, location, default_scale='C'):
        self.location = location
        self.default_scale = default_scale
        self.readings = []

    def add_reading(self, temperature, scale=None):
        """Add a temperature reading"""
        if scale is None:
            scale = self.default_scale

        # Convert to Celsius for storage
        temp_c = convert_temperature(temperature, scale, 'C')
        self.readings.append(temp_c)

    def get_current_temp(self, scale=None):
        """Get most recent temperature"""
        if not self.readings:
            return None

        if scale is None:
            scale = self.default_scale

        latest = self.readings[-1]
        return convert_temperature(latest, 'C', scale)

    def get_average_temp(self, scale=None):
        """Get average temperature"""
        if not self.readings:
            return None

        if scale is None:
            scale = self.default_scale

        avg_celsius = sum(self.readings) / len(self.readings)
        return convert_temperature(avg_celsius, 'C', scale)

    def get_temperature_report(self):
        """Generate comprehensive temperature report"""
        if not self.readings:
            return f"No readings for {self.location}"

        min_c = min(self.readings)
        max_c = max(self.readings)
        avg_c = sum(self.readings) / len(self.readings)

        report = f"Weather Station: {self.location}\\n"
        report += f"Total readings: {len(self.readings)}\\n"
        report += f"Temperature Statistics:\\n"
        report += f"  Current: {self.readings[-1]:.1f}°C / {convert_temperature(self.readings[-1], 'C', 'F'):.1f}°F\\n"
        report += f"  Average: {avg_c:.1f}°C / {convert_temperature(avg_c, 'C', 'F'):.1f}°F\\n"
        report += f"  Min: {min_c:.1f}°C / {convert_temperature(min_c, 'C', 'F'):.1f}°F\\n"
        report += f"  Max: {max_c:.1f}°C / {convert_temperature(max_c, 'C', 'F'):.1f}°F\\n"
        report += f"  Range: {max_c - min_c:.1f}°C\\n"
        report += f"  Condition: {classify_temperature(avg_c)}"

        return report

# Test weather station
station = WeatherStation("New York City", "C")

# Add readings in different scales
station.add_reading(20, 'C')
station.add_reading(72, 'F')
station.add_reading(18, 'C')
station.add_reading(68, 'F')
station.add_reading(22, 'C')
station.add_reading(294, 'K')

print(station.get_temperature_report())

print("\\n" + "="*70)
print("Current temperature in different scales:")
print(f"  Celsius: {station.get_current_temp('C'):.2f}°C")
print(f"  Fahrenheit: {station.get_current_temp('F'):.2f}°F")
print(f"  Kelvin: {station.get_current_temp('K'):.2f}K")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Celsius to Fahrenheit: (C × 9/5) + 32")
print("2. Fahrenheit to Celsius: (F - 32) × 5/9")
print("3. Celsius to Kelvin: C + 273.15")
print("4. Kelvin to Celsius: K - 273.15")
print("5. Validate against absolute zero before converting")
print("6. Use intermediate conversion (to Celsius) for flexibility")
print("7. Format output with proper temperature symbols")
print("8. Handle edge cases and invalid inputs")
print("9. Support bulk conversions for data processing")
print("10. Build reusable conversion utilities")
print("="*70)
'''

# Save and continue with 127-130
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("\nUpgraded lessons 121-126:")
print(f"  121: Math Helper Functions - {len(lesson121['fullSolution'])} chars")
print(f"  122: Method Overriding Basics - {len(lesson122['fullSolution'])} chars")
print(f"  123: Object Method Calls - {len(lesson123['fullSolution'])} chars")
print(f"  124: Range Function - {len(lesson124['fullSolution'])} chars")
print(f"  125: Simple Calculator Functions - {len(lesson125['fullSolution'])} chars")
print(f"  126: Temperature Conversion Functions - {len(lesson126['fullSolution'])} chars")
print("\nFinalizing with lessons 127-130...")
