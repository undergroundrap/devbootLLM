import fs from 'fs';

// Read lessons
const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

let modificationCount = 0;

// ===== PYTHON LESSON 6: For Loops =====
const lesson6 = pythonLessons.find(l => l.id === 6);
if (lesson6 && !lesson6.additionalExamples) {
  lesson6.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Loop through range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Loop from start to end
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# Loop with step
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Loop through a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Loop through a string
for char in "Python":
    print(char)  # P, y, t, h, o, n

# Loop with index using enumerate
names = ['Alice', 'Bob', 'Charlie']
for index, name in enumerate(names):
    print(f"{index}: {name}")

# Loop through dictionary keys
person = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
for key in person:
    print(f"{key}: {person[key]}")

# Loop through dictionary items
for key, value in person.items():
    print(f"{key}: {value}")

# Nested loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Break out of loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# Continue to next iteration
for i in range(5):
    if i == 2:
        continue  # Skip 2
    print(i)  # 0, 1, 3, 4
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 6: For Loops');
}

// ===== PYTHON LESSON 7: Lists Basics =====
const lesson7 = pythonLessons.find(l => l.id === 7);
if (lesson7 && !lesson7.additionalExamples) {
  lesson7.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Creating lists
numbers = [10, 20, 30, 40, 50]
names = ['Alice', 'Bob', 'Charlie']
mixed = [1, 'hello', 3.14, True]

# Accessing elements (0-indexed)
print(numbers[0])   # 10 (first element)
print(numbers[1])   # 20 (second element)
print(numbers[-1])  # 50 (last element)
print(numbers[-2])  # 40 (second to last)

# Slicing
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30] (first 3)
print(numbers[2:])    # [30, 40, 50] (from index 2 to end)
print(numbers[::2])   # [10, 30, 50] (every 2nd element)

# Modifying lists
numbers[0] = 15       # Change first element
print(numbers)        # [15, 20, 30, 40, 50]

# List methods
fruits = ['apple', 'banana']
fruits.append('cherry')         # Add to end
fruits.insert(1, 'orange')      # Insert at index
fruits.remove('banana')         # Remove by value
popped = fruits.pop()           # Remove and return last
print(fruits)

# List length and membership
print(len(numbers))             # 5
print(30 in numbers)            # True
print(100 in numbers)           # False

# List concatenation and repetition
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2        # [1, 2, 3, 4, 5, 6]
repeated = [1, 2] * 3           # [1, 2, 1, 2, 1, 2]

# Empty list
empty = []
empty.append(1)
print(empty)  # [1]
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 7: Lists Basics');
}

// ===== PYTHON LESSON 8: Functions =====
const lesson8 = pythonLessons.find(l => l.id === 8);
if (lesson8 && !lesson8.additionalExamples) {
  lesson8.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic function
def greet(name):
    print(f"Hello, {name}!")

greet('Alice')  # Hello, Alice!
greet('Bob')    # Hello, Bob!

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)  # 5 + 3 = 8

# Function with default parameter
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}")

greet_with_title("Smith")          # Hello, Mr. Smith
greet_with_title("Jones", "Ms.")   # Hello, Ms. Jones

# Function that returns a value
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)  # 20

# Function with multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Function calling another function
def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))  # 25

# Function with variable arguments
def print_all(*args):
    for arg in args:
        print(arg)

print_all(1, 2, 3, 4)  # Prints each number

# Practical example: validate email
def is_valid_email(email):
    return '@' in email and '.' in email

print(is_valid_email("user@example.com"))  # True
print(is_valid_email("invalid"))           # False
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 8: Functions');
}

// ===== PYTHON LESSON 9: Functions that Return =====
const lesson9 = pythonLessons.find(l => l.id === 9);
if (lesson9 && !lesson9.additionalExamples) {
  lesson9.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic return
def area(width, height):
    return width * height

result = area(3, 5)
print(result)  # 15

# Return with calculation
def circle_area(radius):
    pi = 3.14159
    return pi * radius ** 2

print(circle_area(5))  # 78.53975

# Early return
def is_adult(age):
    if age >= 18:
        return True
    return False

print(is_adult(25))  # True
print(is_adult(15))  # False

# Multiple return statements
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

print(get_grade(85))  # B

# Return multiple values (tuple)
def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

sum_val, avg_val = calculate_stats([1, 2, 3, 4, 5])
print(f"Sum: {sum_val}, Average: {avg_val}")  # Sum: 15, Average: 3.0

# Return list
def get_evens(numbers):
    return [n for n in numbers if n % 2 == 0]

evens = get_evens([1, 2, 3, 4, 5, 6])
print(evens)  # [2, 4, 6]

# Return dictionary
def create_person(name, age):
    return {'name': name, 'age': age}

person = create_person('Alice', 25)
print(person)  # {'name': 'Alice', 'age': 25}

# Using return value in conditions
def is_palindrome(text):
    return text == text[::-1]

if is_palindrome('racecar'):
    print("It's a palindrome!")

# Chaining function calls
def double(n):
    return n * 2

def add_ten(n):
    return n + 10

result = add_ten(double(5))  # double(5) = 10, add_ten(10) = 20
print(result)  # 20
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 9: Functions that Return');
}

// Write Python lessons back
fs.writeFileSync('public/lessons-python.json', JSON.stringify(pythonLessons, null, 2));
console.log(`\n✅ Modified ${modificationCount} Python lessons`);

// Now improve Java lessons
let javaModCount = 0;

// ===== JAVA LESSON 13: Creating Methods =====
const javaLesson13 = javaLessons.find(l => l.id === 13);
if (javaLesson13 && !javaLesson13.additionalExamples) {
  javaLesson13.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Basic method
public static void greetUser(String name) {
    System.out.println("Hello, " + name + "!");
}

public static void main(String[] args) {
    greetUser("Alice");  // Hello, Alice!
    greetUser("Bob");    // Hello, Bob!
}

// Method with multiple parameters
public static void printSum(int a, int b) {
    int sum = a + b;
    System.out.println(a + " + " + b + " = " + sum);
}

printSum(5, 3);  // 5 + 3 = 8

// Method with no parameters
public static void showMenu() {
    System.out.println("1. Start");
    System.out.println("2. Settings");
    System.out.println("3. Exit");
}

showMenu();

// Method calling another method
public static void printLine() {
    System.out.println("------------------");
}

public static void printHeader(String title) {
    printLine();
    System.out.println(title);
    printLine();
}

printHeader("Welcome");

// Multiple methods
public static void printSquare(int n) {
    System.out.println(n + " squared = " + (n * n));
}

public static void printCube(int n) {
    System.out.println(n + " cubed = " + (n * n * n));
}

printSquare(5);  // 5 squared = 25
printCube(3);    // 3 cubed = 27

// Practical example: validation
public static void validateAge(int age) {
    if (age >= 18) {
        System.out.println("Access granted");
    } else {
        System.out.println("Access denied");
    }
}

validateAge(25);  // Access granted
validateAge(15);  // Access denied
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 13: Creating Methods');
}

// ===== JAVA LESSON 14: Methods with Return Values =====
const javaLesson14 = javaLessons.find(l => l.id === 14);
if (javaLesson14 && !javaLesson14.additionalExamples) {
  javaLesson14.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Basic return
public static int add(int a, int b) {
    return a + b;
}

public static void main(String[] args) {
    int result = add(5, 3);
    System.out.println(result);  // 8
}

// Return with calculation
public static double calculateArea(double width, double height) {
    return width * height;
}

double area = calculateArea(5.0, 3.0);
System.out.println("Area: " + area);  // 15.0

// Return boolean
public static boolean isEven(int number) {
    return number % 2 == 0;
}

System.out.println(isEven(4));   // true
System.out.println(isEven(7));   // false

// Return String
public static String getGrade(int score) {
    if (score >= 90) return "A";
    else if (score >= 80) return "B";
    else if (score >= 70) return "C";
    else return "F";
}

System.out.println(getGrade(85));  // B

// Using return value in expressions
public static int multiply(int x, int y) {
    return x * y;
}

int result = multiply(3, 4) + 10;
System.out.println(result);  // 22

// Early return
public static String checkAge(int age) {
    if (age < 0) {
        return "Invalid age";
    }
    if (age < 18) {
        return "Minor";
    }
    return "Adult";
}

// Method calling method with return
public static int square(int n) {
    return n * n;
}

public static int sumOfSquares(int a, int b) {
    return square(a) + square(b);
}

System.out.println(sumOfSquares(3, 4));  // 25

// Practical example: temperature conversion
public static double celsiusToFahrenheit(double celsius) {
    return (celsius * 9.0 / 5.0) + 32;
}

double temp = celsiusToFahrenheit(25);
System.out.println("25°C = " + temp + "°F");  // 77°F
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 14: Methods with Return Values');
}

// ===== JAVA LESSON 15: Array Length & Bounds =====
const javaLesson15 = javaLessons.find(l => l.id === 15);
if (javaLesson15 && !javaLesson15.additionalExamples) {
  javaLesson15.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Array length
int[] numbers = {5, 9, 14, 27, 8};
System.out.println("Length: " + numbers.length);  // 5

// Safe array access using length
int lastIndex = numbers.length - 1;
System.out.println("Last element: " + numbers[lastIndex]);  // 8

// Loop using length
for (int i = 0; i < numbers.length; i++) {
    System.out.println("Index " + i + ": " + numbers[i]);
}

// Checking bounds before access
int index = 10;
if (index >= 0 && index < numbers.length) {
    System.out.println(numbers[index]);
} else {
    System.out.println("Index out of bounds");
}

// ArrayIndexOutOfBoundsException example
try {
    System.out.println(numbers[10]);  // Error! Index 10 doesn't exist
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Invalid index!");
}

// Dynamic array sizing
int size = 5;
int[] dynamicArray = new int[size];
System.out.println("Created array of size: " + dynamicArray.length);

// Empty array
int[] empty = new int[0];
System.out.println("Empty array length: " + empty.length);  // 0

// Finding elements safely
public static int findElement(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) {
            return i;  // Found at index i
        }
    }
    return -1;  // Not found
}

int[] data = {10, 20, 30, 40};
int position = findElement(data, 30);
System.out.println("Found at index: " + position);  // 2

// Practical: sum all elements
public static int sum(int[] array) {
    int total = 0;
    for (int i = 0; i < array.length; i++) {
        total += array[i];
    }
    return total;
}

System.out.println("Sum: " + sum(numbers));
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 15: Array Length & Bounds');
}

// ===== JAVA LESSON 16: Looping Through Arrays =====
const javaLesson16 = javaLessons.find(l => l.id === 16);
if (javaLesson16 && !javaLesson16.additionalExamples) {
  javaLesson16.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Traditional for loop with index
String[] names = {"Alice", "Bob", "Charlie", "David"};
for (int i = 0; i < names.length; i++) {
    System.out.println("Index " + i + ": " + names[i]);
}

// Enhanced for loop (for-each)
for (String name : names) {
    System.out.println("Hello, " + name);
}

// Loop through numbers array
int[] numbers = {10, 20, 30, 40, 50};
for (int num : numbers) {
    System.out.println(num * 2);  // Print each doubled
}

// Find maximum value
public static int findMax(int[] arr) {
    int max = arr[0];
    for (int i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int[] scores = {85, 92, 78, 95, 88};
System.out.println("Max score: " + findMax(scores));  // 95

// Count specific elements
public static int countEvens(int[] arr) {
    int count = 0;
    for (int num : arr) {
        if (num % 2 == 0) {
            count++;
        }
    }
    return count;
}

int[] data = {1, 2, 3, 4, 5, 6};
System.out.println("Even numbers: " + countEvens(data));  // 3

// Sum all elements
public static double average(int[] arr) {
    int sum = 0;
    for (int num : arr) {
        sum += num;
    }
    return (double) sum / arr.length;
}

System.out.println("Average: " + average(scores));

// Loop backwards
for (int i = names.length - 1; i >= 0; i--) {
    System.out.println(names[i]);
}

// Loop with step (every 2nd element)
for (int i = 0; i < numbers.length; i += 2) {
    System.out.println(numbers[i]);  // 10, 30, 50
}

// Practical: search for element
public static boolean contains(String[] arr, String target) {
    for (String element : arr) {
        if (element.equals(target)) {
            return true;
        }
    }
    return false;
}

System.out.println(contains(names, "Bob"));     // true
System.out.println(contains(names, "Eve"));     // false

// 2D array looping
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
        System.out.print(matrix[i][j] + " ");
    }
    System.out.println();
}
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 16: Looping Through Arrays');
}

// Write Java lessons back
fs.writeFileSync('public/lessons-java.json', JSON.stringify(javaLessons, null, 2));
console.log(`✅ Modified ${javaModCount} Java lessons`);

console.log(`\n📊 Total modifications: ${modificationCount + javaModCount}`);
console.log('✅ Batch 7 improvements complete!');
