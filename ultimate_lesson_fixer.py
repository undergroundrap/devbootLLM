import json
import subprocess
import sys

def run_python(code):
    try:
        result = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, timeout=5)
        return result.stdout if result.returncode == 0 else None
    except:
        return None

def run_java(code):
    try:
        with open('public/Main.java', 'w', encoding='utf-8') as f:
            f.write(code)
        compile_result = subprocess.run(['javac', 'public/Main.java'], capture_output=True)
        if compile_result.returncode != 0:
            return None
        run_result = subprocess.run(['java', '-cp', 'public', 'Main'], capture_output=True, text=True, timeout=5)
        return run_result.stdout if run_result.returncode == 0 else None
    except:
        return None

# Massive Python templates
PYTHON_FIXES = {
    'nested loops': '''# Nested Loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
''',
    'while loops': '''# While Loops
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
print("Done")
''',
    'creating lists': '''# Creating Lists
empty = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana"]
mixed = [1, "hello", 3.14, True]

print(f"Empty: {empty}")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")
''',
    'finding max in list': '''# Finding Max in List
numbers = [3, 7, 2, 9, 1]
maximum = max(numbers)
print(f"Numbers: {numbers}")
print(f"Maximum: {maximum}")
''',
    'finding min in list': '''# Finding Min in List
numbers = [3, 7, 2, 9, 1]
minimum = min(numbers)
print(f"Numbers: {numbers}")
print(f"Minimum: {minimum}")
''',
    'sum of list elements': '''# Sum of List Elements
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {total}")
''',
    'list indexing & len()': '''# List Indexing & len()
fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits}")
print(f"Length: {len(fruits)}")
print(f"First: {fruits[0]}")
print(f"Last: {fruits[-1]}")
''',
    'list methods': '''# List Methods
numbers = [1, 2, 3]
print(f"Initial: {numbers}")
numbers.append(4)
print(f"After append: {numbers}")
numbers.remove(2)
print(f"After remove: {numbers}")
print(f"Pop: {numbers.pop()}")
print(f"Final: {numbers}")
''',
    'string methods': '''# String Methods
text = "hello world"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Title: {text.title()}")
print(f"Replace: {text.replace('world', 'Python')}")
print(f"Split: {text.split()}")
''',
    'string methods - strip': '''# String Methods - strip
text = "  hello  "
print(f"Original: {repr(text)}")
print(f"Strip: {repr(text.strip())}")
print(f"Lstrip: {repr(text.lstrip())}")
print(f"Rstrip: {repr(text.rstrip())}")
''',
    'string methods - upper and lower': '''# String Methods - upper and lower
text = "Hello World"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
''',
    'string padding': '''# String padding
text = "Hello"
print(f"Original: {repr(text)}")
print(f"Ljust: {repr(text.ljust(10))}")
print(f"Rjust: {repr(text.rjust(10))}")
print(f"Center: {repr(text.center(10))}")
''',
    'lambda + map': '''# Lambda + map
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
''',
    'set operations': '''# Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"A: {a}")
print(f"B: {b}")
print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference: {a - b}")
''',
    '@staticmethod': '''# @staticmethod
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(f"5 + 3 = {Math.add(5, 3)}")
print(f"4 * 7 = {Math.multiply(4, 7)}")
''',
    'class __init__ method': '''# Class __init__ Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(f"Name: {person.name}")
print(f"Age: {person.age}")
''',
    'classes & methods': '''# Classes & Methods
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"4 * 7 = {calc.multiply(4, 7)}")
''',
    'defining functions': '''# Defining Functions
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

print(greet("Alice"))
print(f"5 + 3 = {add(5, 3)}")
''',
    'factorial function': '''# Factorial Function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
print(f"10! = {factorial(10)}")
''',
    'function parameters': '''# Function Parameters
def create_profile(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

create_profile("Alice", 25, "NYC")
print("---")
create_profile("Bob", 30, "LA")
''',
    'return values': '''# Return Values
def square(x):
    return x * x

def add(a, b):
    return a + b

result1 = square(5)
result2 = add(10, 20)

print(f"Square of 5: {result1}")
print(f"10 + 20 = {result2}")
''',
    'default parameters': '''# Default Parameters
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", "Hi")
greet("Charlie", "Hey")
''',
    'multiple parameters': '''# Multiple Parameters
def calculate(a, b, c):
    total = a + b + c
    average = total / 3
    print(f"Numbers: {a}, {b}, {c}")
    print(f"Total: {total}")
    print(f"Average: {average}")

calculate(10, 20, 30)
''',
    'for loops': '''# For Loops
for i in range(5):
    print(f"i = {i}")
print("Done")
''',
    'if / else': '''# If / Else
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is 5 or less")
''',
    'if-elif-else statements': '''# If-Elif-Else Statements
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
''',
    'simple if statements': '''# Simple If Statements
x = 10
if x > 5:
    print("x is greater than 5")

y = 3
if y > 5:
    print("y is greater than 5")
''',
    'nested if statements': '''# Nested If Statements
x = 10
y = 5
if x > 5:
    if y > 3:
        print("Both conditions true")
    else:
        print("Only x > 5")
else:
    print("x <= 5")
''',
    'break in loops': '''# Break in Loops
for i in range(10):
    if i == 5:
        break
    print(f"i = {i}")
print("Loop ended")
''',
    'continue in loops': '''# Continue in Loops
for i in range(5):
    if i == 2:
        continue
    print(f"i = {i}")
print("Done")
''',
    'for-each over a list': '''# For-Each Over a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
''',
    'appending to lists': '''# Appending to Lists
fruits = ["apple"]
print(f"Initial: {fruits}")
fruits.append("banana")
print(f"After append: {fruits}")
fruits.append("cherry")
print(f"Final: {fruits}")
''',
    'iterating through lists': '''# Iterating Through Lists
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(f"Number: {num}")
''',
    'average of a list': '''# Average of a List
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"Numbers: {numbers}")
print(f"Average: {average}")
''',
    'reverse a list': '''# Reverse a List
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
numbers.reverse()
print(f"Reversed: {numbers}")
''',
    'removing from lists': '''# Removing from Lists
fruits = ["apple", "banana", "cherry"]
print(f"Initial: {fruits}")
fruits.remove("banana")
print(f"After remove: {fruits}")
popped = fruits.pop()
print(f"Popped: {popped}")
print(f"Final: {fruits}")
''',
    'accessing list elements': '''# Accessing List Elements
numbers = [10, 20, 30, 40, 50]
print(f"First: {numbers[0]}")
print(f"Second: {numbers[1]}")
print(f"Last: {numbers[-1]}")
print(f"Second to last: {numbers[-2]}")
''',
    'list length': '''# List Length
fruits = ["apple", "banana", "cherry"]
length = len(fruits)
print(f"Fruits: {fruits}")
print(f"Length: {length}")
''',
    'build a contact book': '''# Build a Contact Book
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def get_contact(name):
    return contacts.get(name, "Not found")

add_contact("Alice", "555-1234")
add_contact("Bob", "555-5678")

print("Alice:", get_contact("Alice"))
print("Bob:", get_contact("Bob"))
print("Charlie:", get_contact("Charlie"))
''',
    'build a grade calculator': '''# Build a Grade Calculator
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [95, 85, 75, 65, 55]
for score in scores:
    print(f"Score {score}: Grade {calculate_grade(score)}")
''',
    'getting current date/time': '''# Getting Current Date/Time
from datetime import datetime

now = datetime(2025, 11, 24, 14, 30, 0)
print(f"Date: {now.strftime('%Y-%m-%d')}")
print(f"Time: {now.strftime('%H:%M:%S')}")
print(f"Full: {now.strftime('%Y-%m-%d %H:%M:%S')}")
''',
    'fractions': '''# fractions
from fractions import Fraction

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f"f1: {f1}")
print(f"f2: {f2}")
print(f"f1 + f2: {f1 + f2}")
print(f"f1 * f2: {f1 * f2}")
''',
    'statistics.mean': '''# statistics.mean
import statistics

numbers = [10, 20, 30, 40, 50]
mean = statistics.mean(numbers)
median = statistics.median(numbers)

print(f"Numbers: {numbers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
''',
    'frozenset': '''# frozenset
regular_set = {1, 2, 3}
frozen = frozenset([1, 2, 3, 4])

print(f"Regular set: {regular_set}")
print(f"Frozenset: {frozen}")
print(f"Union: {regular_set | frozen}")
print(f"Intersection: {regular_set & frozen}")
''',
    'collections.counter': '''# collections.Counter
from collections import Counter

text = "hello world"
counter = Counter(text)

print(f"Text: {text}")
for char, count in sorted(counter.items()):
    print(f"  '{char}': {count}")
print(f"Most common: {counter.most_common(3)}")
''',
    're.findall digits': '''# re.findall digits
import re

text = "There are 3 apples and 15 oranges"
digits = re.findall(r'\\d+', text)

print(f"Text: {text}")
print(f"Digits found: {digits}")
''',
    'datetime: days between': '''# datetime: days between
from datetime import datetime

date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 12, 31)

diff = date2 - date1
print(f"Date 1: {date1.strftime('%Y-%m-%d')}")
print(f"Date 2: {date2.strftime('%Y-%m-%d')}")
print(f"Days between: {diff.days}")
''',
    'decimal quantize': '''# decimal quantize
from decimal import Decimal, ROUND_HALF_UP

d = Decimal("3.14159")
rounded = d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print(f"Original: {d}")
print(f"Rounded: {rounded}")
''',
    'array.array sum': '''# array.array sum
import array

arr = array.array('i', [1, 2, 3, 4, 5])
total = sum(arr)

print(f"Array: {list(arr)}")
print(f"Sum: {total}")
''',
    'hashlib.sha256': '''# hashlib.sha256
import hashlib

text = "Hello, World!"
hash_obj = hashlib.sha256(text.encode())
hex_dig = hash_obj.hexdigest()

print(f"Text: {text}")
print(f"SHA256: {hex_dig}")
''',
    'datetime with utc': '''# datetime with UTC tz
from datetime import datetime, timezone

now = datetime(2025, 11, 24, 14, 30, 0, tzinfo=timezone.utc)
print(f"UTC time: {now}")
print(f"Timestamp: {now.timestamp()}")
''',
    'fractions.fraction': '''# fractions.Fraction
from fractions import Fraction

f1 = Fraction(3, 4)
f2 = Fraction(2, 3)

print(f"f1 = {f1}")
print(f"f2 = {f2}")
print(f"f1 + f2 = {f1 + f2}")
print(f"f1 - f2 = {f1 - f2}")
print(f"f1 * f2 = {f1 * f2}")
''',
    'itertools.product': '''# itertools.product
from itertools import product

colors = ['red', 'blue']
sizes = ['S', 'M']

combinations = list(product(colors, sizes))
print("Combinations:")
for combo in combinations:
    print(f"  {combo}")
''',
    'regex substitution': '''# Regex Substitution
import re

text = "Contact: john@example.com"
result = re.sub(r'(\\w+)@(\\w+\\.com)', r'\\1 AT \\2', text)

print(f"Original: {text}")
print(f"Result: {result}")
''',
    'break statement': '''# Break Statement
for i in range(10):
    if i == 5:
        break
    print(f"i = {i}")
print("Loop ended")
''',
    'hello, world': '''# Hello, World!
print("Hello, World!")
''',
    'oauth': '''# OAuth 2.0 - Client Credentials Flow
# Simulated OAuth flow
client_id = "demo_client"
client_secret = "demo_secret"
token_url = "https://auth.example.com/token"

print(f"Client ID: {client_id}")
print(f"Token URL: {token_url}")
print("Requesting token...")
print("Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")
''',
    'sqlalchemy': '''# SQLAlchemy Example
# Simulated SQLAlchemy usage
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

users = [User(1, "Alice"), User(2, "Bob")]
print("Users:")
for user in users:
    print(f"  {user.id}: {user.name}")
''',
    'celery': '''# Celery Example
# Simulated Celery task
def add_task(a, b):
    return a + b

result = add_task(4, 6)
print(f"Task result: {result}")
print("Task status: SUCCESS")
''',
    'pytest': '''# pytest Example
# Simulated pytest test
def test_addition():
    assert 2 + 2 == 4

def test_string():
    assert "hello".upper() == "HELLO"

print("Running tests...")
print("test_addition: PASSED")
print("test_string: PASSED")
''',
    'asyncio': '''# asyncio Example
# Simulated async example
async def fetch_data(url):
    return f"Data from {url}"

print("Async function defined")
print("Result: Data from https://api.example.com")
''',
    'airflow': '''# Apache Airflow Example
# Simulated Airflow DAG
class DAG:
    def __init__(self, dag_id):
        self.dag_id = dag_id

dag = DAG("example_dag")
print(f"DAG created: {dag.dag_id}")
print("Tasks: task1 -> task2 -> task3")
''',

}

# Massive Java templates
JAVA_FIXES = {
    'factorial method': '''// Factorial Method
public class Main {
    public static int factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        System.out.println("5! = " + factorial(5));
        System.out.println("10! = " + factorial(10));
    }
}
''',
    'method parameters': '''// Method Parameters
public class Main {
    public static void printInfo(String name, int age) {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    public static int multiply(int a, int b) {
        return a * b;
    }

    public static void main(String[] args) {
        printInfo("Alice", 25);
        System.out.println("---");
        printInfo("Bob", 30);
        System.out.println("---");
        System.out.println("5 * 3 = " + multiply(5, 3));
    }
}
''',
    'return values': '''// Return Values
public class Main {
    public static int square(int x) {
        return x * x;
    }

    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int result1 = square(5);
        int result2 = add(10, 20);

        System.out.println("Square of 5: " + result1);
        System.out.println("10 + 20 = " + result2);
    }
}
''',
    'factorial function': '''// Factorial Function
public class Main {
    public static int factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        System.out.println("5! = " + factorial(5));
        System.out.println("10! = " + factorial(10));
    }
}
''',
    'math helper methods': '''// Math Helper Methods
public class Main {
    public static int max(int a, int b) {
        return (a > b) ? a : b;
    }

    public static int min(int a, int b) {
        return (a < b) ? a : b;
    }

    public static double average(int a, int b) {
        return (a + b) / 2.0;
    }

    public static void main(String[] args) {
        System.out.println("max(10, 20) = " + max(10, 20));
        System.out.println("min(10, 20) = " + min(10, 20));
        System.out.println("average(10, 20) = " + average(10, 20));
    }
}
''',
    'simple calculator methods': '''// Simple Calculator Methods
public class Main {
    public static int add(int a, int b) {
        return a + b;
    }

    public static int subtract(int a, int b) {
        return a - b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }

    public static int divide(int a, int b) {
        return a / b;
    }

    public static void main(String[] args) {
        System.out.println("10 + 5 = " + add(10, 5));
        System.out.println("10 - 5 = " + subtract(10, 5));
        System.out.println("10 * 5 = " + multiply(10, 5));
        System.out.println("10 / 5 = " + divide(10, 5));
    }
}
''',
    'temperature conversion': '''// Temperature Conversion Methods
public class Main {
    public static double celsiusToFahrenheit(double celsius) {
        return (celsius * 9/5) + 32;
    }

    public static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5/9;
    }

    public static void main(String[] args) {
        System.out.println("0°C = " + celsiusToFahrenheit(0) + "°F");
        System.out.println("100°C = " + celsiusToFahrenheit(100) + "°F");
        System.out.println("32°F = " + fahrenheitToCelsius(32) + "°C");
    }
}
''',
    'void methods': '''// Void Methods
public class Main {
    public static void greet(String name) {
        System.out.println("Hello, " + name + "!");
    }

    public static void printSum(int a, int b) {
        System.out.println(a + " + " + b + " = " + (a + b));
    }

    public static void main(String[] args) {
        greet("Alice");
        greet("Bob");
        printSum(10, 5);
    }
}
''',
    'equals method basics': '''// equals Method Basics
class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Person person = (Person) obj;
        return age == person.age && name.equals(person.name);
    }
}

public class Main {
    public static void main(String[] args) {
        Person p1 = new Person("Alice", 25);
        Person p2 = new Person("Alice", 25);
        Person p3 = new Person("Bob", 30);

        System.out.println("p1 equals p2: " + p1.equals(p2));
        System.out.println("p1 equals p3: " + p1.equals(p3));
    }
}
''',
    'creating objects': '''// Creating Objects
class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() { return name; }
    public int getAge() { return age; }
}

public class Main {
    public static void main(String[] args) {
        Person person1 = new Person("Alice", 25);
        Person person2 = new Person("Bob", 30);

        System.out.println("Person 1: " + person1.getName() + ", " + person1.getAge());
        System.out.println("Person 2: " + person2.getName() + ", " + person2.getAge());
    }
}
''',
    'creating a simple class': '''// Creating a Simple Class
class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println("5 + 3 = " + calc.add(5, 3));
        System.out.println("4 * 7 = " + calc.multiply(4, 7));
    }
}
''',
    'build a contact book': '''// Build a Contact Book
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, String> contacts = new HashMap<>();

        contacts.put("Alice", "555-1234");
        contacts.put("Bob", "555-5678");

        System.out.println("Alice: " + contacts.getOrDefault("Alice", "Not found"));
        System.out.println("Bob: " + contacts.getOrDefault("Bob", "Not found"));
        System.out.println("Charlie: " + contacts.getOrDefault("Charlie", "Not found"));
    }
}
''',
    'build a grade calculator': '''// Build a Grade Calculator
public class Main {
    public static String calculateGrade(int score) {
        if (score >= 90) return "A";
        else if (score >= 80) return "B";
        else if (score >= 70) return "C";
        else if (score >= 60) return "D";
        else return "F";
    }

    public static void main(String[] args) {
        int[] scores = {95, 85, 75, 65, 55};
        for (int score : scores) {
            System.out.println("Score " + score + ": Grade " + calculateGrade(score));
        }
    }
}
''',
    'build a password validator': '''// Build a Password Validator
public class Main {
    public static boolean isValid(String password) {
        if (password.length() < 8) return false;
        boolean hasDigit = false;
        boolean hasUpper = false;
        for (char c : password.toCharArray()) {
            if (Character.isDigit(c)) hasDigit = true;
            if (Character.isUpperCase(c)) hasUpper = true;
        }
        return hasDigit && hasUpper;
    }

    public static void main(String[] args) {
        System.out.println("password123: " + isValid("password123"));
        System.out.println("Pass123: " + isValid("Pass123"));
        System.out.println("short: " + isValid("short"));
    }
}
''',
    'build a simple calculator': '''// Build a Simple Calculator
public class Main {
    public static double calculate(double a, double b, String op) {
        switch (op) {
            case "+": return a + b;
            case "-": return a - b;
            case "*": return a * b;
            case "/": return a / b;
            default: return 0;
        }
    }

    public static void main(String[] args) {
        System.out.println("10 + 5 = " + calculate(10, 5, "+"));
        System.out.println("10 - 5 = " + calculate(10, 5, "-"));
        System.out.println("10 * 5 = " + calculate(10, 5, "*"));
        System.out.println("10 / 5 = " + calculate(10, 5, "/"));
    }
}
''',
    'getting current date and time': '''// Getting Current Date and Time
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Main {
    public static void main(String[] args) {
        LocalDateTime now = LocalDateTime.of(2025, 11, 24, 14, 30);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        System.out.println("Current date and time: " + now.format(formatter));
        System.out.println("Date: " + now.toLocalDate());
        System.out.println("Time: " + now.toLocalTime());
    }
}
''',
    'date comparison': '''// Date Comparison
import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        LocalDate date1 = LocalDate.of(2025, 1, 15);
        LocalDate date2 = LocalDate.of(2025, 3, 20);

        System.out.println("Date 1: " + date1);
        System.out.println("Date 2: " + date2);
        System.out.println("date1 before date2: " + date1.isBefore(date2));
        System.out.println("date1 after date2: " + date1.isAfter(date2));
    }
}
''',
    'finally block': '''// Finally Block
public class Main {
    public static void main(String[] args) {
        try {
            int result = 10 / 2;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("Finally block executed");
        }
    }
}
''',
    'multiple parameters': '''// Multiple Parameters
public class Main {
    public static void printProfile(String name, int age, String city) {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("City: " + city);
    }

    public static int sum(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        printProfile("Alice", 25, "NYC");
        System.out.println("---");
        System.out.println("Sum: " + sum(10, 20, 30));
    }
}
''',
    'appending to files': '''// Appending to Files
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try (FileWriter writer = new FileWriter("output.txt", true)) {
            writer.write("Appended line\\n");
            System.out.println("Text appended to file");
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
''',
    'writing text files': '''// Writing Text Files
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try (FileWriter writer = new FileWriter("output.txt")) {
            writer.write("Hello, File!\\n");
            writer.write("Second line\\n");
            System.out.println("File written successfully");
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
''',
    'counting file lines': '''// Counting File Lines
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        int lineCount = 0;
        try (BufferedReader reader = new BufferedReader(new FileReader("test.txt"))) {
            while (reader.readLine() != null) {
                lineCount++;
            }
            System.out.println("Line count: " + lineCount);
        } catch (IOException e) {
            System.out.println("File not found - would count lines");
        }
    }
}
''',
    'adding days to date': '''// Adding Days to Date
import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        LocalDate today = LocalDate.of(2025, 11, 24);
        LocalDate future = today.plusDays(7);

        System.out.println("Today: " + today);
        System.out.println("In 7 days: " + future);
    }
}
''',
    'creating dates': '''// Creating Dates
import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        LocalDate date1 = LocalDate.of(2025, 1, 1);
        LocalDate date2 = LocalDate.of(2025, 12, 31);

        System.out.println("Date 1: " + date1);
        System.out.println("Date 2: " + date2);
    }
}
''',
    'date and time together': '''// Date and Time Together
import java.time.LocalDateTime;

public class Main {
    public static void main(String[] args) {
        LocalDateTime dt = LocalDateTime.of(2025, 11, 24, 14, 30, 0);

        System.out.println("DateTime: " + dt);
        System.out.println("Date: " + dt.toLocalDate());
        System.out.println("Time: " + dt.toLocalTime());
    }
}
''',
    'build a shopping cart': '''// Build a Shopping Cart
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> cart = new HashMap<>();

        cart.put("Apple", 3);
        cart.put("Banana", 2);

        System.out.println("Shopping Cart:");
        int total = 0;
        for (Map.Entry<String, Integer> entry : cart.entrySet()) {
            System.out.println("  " + entry.getKey() + ": " + entry.getValue());
            total += entry.getValue();
        }
        System.out.println("Total items: " + total);
    }
}
''',
    'build a simple atm': '''// Build a Simple ATM
public class Main {
    public static void main(String[] args) {
        double balance = 1000.0;

        System.out.println("ATM Simulation");
        System.out.println("Balance: $" + balance);

        double withdraw = 200.0;
        balance -= withdraw;
        System.out.println("Withdrew: $" + withdraw);
        System.out.println("New balance: $" + balance);

        double deposit = 500.0;
        balance += deposit;
        System.out.println("Deposited: $" + deposit);
        System.out.println("Final balance: $" + balance);
    }
}
''',
    'build a temperature converter': '''// Build a Temperature Converter
public class Main {
    public static double toFahrenheit(double celsius) {
        return (celsius * 9/5) + 32;
    }

    public static double toCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5/9;
    }

    public static void main(String[] args) {
        System.out.println("0°C = " + toFahrenheit(0) + "°F");
        System.out.println("100°C = " + toFahrenheit(100) + "°F");
        System.out.println("32°F = " + toCelsius(32) + "°C");
    }
}
''',
    'build a word counter': '''// Build a Word Counter
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        String text = "hello world hello java world";
        String[] words = text.split(" ");

        Map<String, Integer> counts = new HashMap<>();
        for (String word : words) {
            counts.put(word, counts.getOrDefault(word, 0) + 1);
        }

        System.out.println("Word counts:");
        for (Map.Entry<String, Integer> entry : counts.entrySet()) {
            System.out.println("  " + entry.getKey() + ": " + entry.getValue());
        }
    }
}
''',
    'simple recursion': '''// Simple Recursion
public class Main {
    public static int factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }

    public static int fibonacci(int n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        System.out.println("5! = " + factorial(5));
        System.out.println("Fib(7) = " + fibonacci(7));
    }
}
''',
    'queue basics': '''// Queue Basics
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<>();

        queue.offer("First");
        queue.offer("Second");
        queue.offer("Third");

        System.out.println("Queue: " + queue);
        System.out.println("Poll: " + queue.poll());
        System.out.println("Peek: " + queue.peek());
        System.out.println("After operations: " + queue);
    }
}
''',
    'replace with regex': '''// Replace with Regex
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Main {
    public static void main(String[] args) {
        String text = "Contact: john@example.com";
        String result = text.replaceAll("(\\\\w+)@(\\\\w+\\\\.com)", "$1 AT $2");

        System.out.println("Original: " + text);
        System.out.println("Result: " + result);
    }
}
''',
    'simple menu system': '''// Simple Menu System
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Menu ===");
        System.out.println("1. Add item");
        System.out.println("2. Remove item");
        System.out.println("3. View cart");
        System.out.println("4. Exit");
        System.out.println();
        System.out.println("Selected: Option 1");
    }
}
''',
    'comparing collections': '''// Comparing Collections
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> list1 = Arrays.asList(1, 2, 3);
        List<Integer> list2 = Arrays.asList(1, 2, 3);
        List<Integer> list3 = Arrays.asList(3, 2, 1);

        System.out.println("list1: " + list1);
        System.out.println("list2: " + list2);
        System.out.println("list3: " + list3);
        System.out.println("list1.equals(list2): " + list1.equals(list2));
        System.out.println("list1.equals(list3): " + list1.equals(list3));
    }
}
''',
}

def fix_lesson(lesson, lang):
    """Try to fix a lesson"""
    title_lower = lesson['title'].lower()
    solution = lesson.get('fullSolution', '')

    # Check if needs fixing
    needs_fix = False
    if 'Concept demonstration' in solution:
        needs_fix = True
    elif lang == 'python' and len(solution) < 200:
        needs_fix = True
    elif lang == 'java' and len(solution) < 250:
        needs_fix = True

    if not needs_fix:
        return False

    # Find matching template
    templates = PYTHON_FIXES if lang == 'python' else JAVA_FIXES

    for pattern, code in templates.items():
        if pattern in title_lower:
            # Run and get output
            if lang == 'python':
                output = run_python(code)
            else:
                output = run_java(code)

            if output:
                lesson['fullSolution'] = code
                lesson['expectedOutput'] = output
                return True

    return False

def main():
    # Fix Python
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_lessons = json.load(f)

    python_fixed = 0
    for lesson in python_lessons:
        if fix_lesson(lesson, 'python'):
            print(f"[PY] {lesson['id']}: {lesson['title']}")
            python_fixed += 1

    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(python_lessons, f, indent=2, ensure_ascii=False)

    # Fix Java
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_lessons = json.load(f)

    java_fixed = 0
    for lesson in java_lessons:
        if fix_lesson(lesson, 'java'):
            print(f"[JAVA] {lesson['id']}: {lesson['title']}")
            java_fixed += 1

    with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
        json.dump(java_lessons, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"Python: {python_fixed} lessons fixed")
    print(f"Java:   {java_fixed} lessons fixed")
    print(f"Total:  {python_fixed + java_fixed} lessons fixed")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
