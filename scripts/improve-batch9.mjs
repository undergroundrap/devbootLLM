import fs from 'fs';

// Read lessons
const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

let modificationCount = 0;

// ===== PYTHON LESSON 11: Compound Conditions =====
const lesson11 = pythonLessons.find(l => l.id === 11);
if (lesson11 && !lesson11.additionalExamples) {
  lesson11.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# AND operator - both must be True
temperature = 72
is_raining = False

if temperature >= 70 and not is_raining:
    print('Nice day!')

# OR operator - at least one must be True
has_umbrella = True
is_indoors = False

if has_umbrella or is_indoors:
    print('You are protected')

# Combining AND and OR
age = 25
has_license = True
has_car = False

if age >= 18 and (has_license or has_car):
    print('Can drive')

# NOT operator - inverts boolean
is_weekend = False
if not is_weekend:
    print('It is a weekday')

# Multiple AND conditions
score = 85
attendance = 95
participation = 90

if score >= 80 and attendance >= 90 and participation >= 85:
    print('Excellent student!')

# Chaining comparisons (Pythonic way)
age = 25
if 18 <= age < 65:
    print('Working age')

# Using parentheses for clarity
x = 10
y = 20
z = 30

if (x < y) and (y < z):
    print('Ascending order')

# Practical: login validation
username = 'admin'
password = 'secret'
is_active = True

if username == 'admin' and password == 'secret' and is_active:
    print('Login successful')
else:
    print('Login failed')

# Complex condition
temperature = 75
humidity = 60
is_sunny = True

if (temperature >= 70 and temperature <= 85) and humidity < 70 and is_sunny:
    print('Perfect weather!')

# Short-circuit evaluation
x = 5
if x > 0 and 10 / x > 1:  # Second condition only checked if first is True
    print('Valid')
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 11: Compound Conditions');
}

// ===== PYTHON LESSON 12: Sum with range() =====
const lesson12 = pythonLessons.find(l => l.id === 12);
if (lesson12 && !lesson12.additionalExamples) {
  lesson12.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Sum of first N numbers
print(sum(range(1, 11)))  # 1+2+3+...+10 = 55

# Sum with different start
print(sum(range(5, 11)))  # 5+6+7+8+9+10 = 45

# Sum even numbers
print(sum(range(0, 11, 2)))  # 0+2+4+6+8+10 = 30

# Sum odd numbers
print(sum(range(1, 11, 2)))  # 1+3+5+7+9 = 25

# Using list comprehension
total = sum([i for i in range(1, 6)])
print(total)  # 15

# Sum of squares
squares_sum = sum([i**2 for i in range(1, 6)])
print(squares_sum)  # 1+4+9+16+25 = 55

# Sum with condition
evens_sum = sum([i for i in range(1, 11) if i % 2 == 0])
print(evens_sum)  # 2+4+6+8+10 = 30

# Sum of list
numbers = [10, 20, 30, 40, 50]
print(sum(numbers))  # 150

# Sum with initial value
print(sum([1, 2, 3], 10))  # 1+2+3+10 = 16

# Practical: calculate total price
prices = [9.99, 14.99, 24.99, 5.99]
total = sum(prices)
print(f"Total: {total:.2f}")  # Total: 55.96

# Average using sum
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"Average: {average}")  # Average: 30.0

# Sum multiples of 3
multiples = sum(range(0, 31, 3))
print(multiples)  # 0+3+6+9+12+15+18+21+24+27+30 = 165
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 12: Sum with range()');
}

// ===== PYTHON LESSON 13: Strings & f-Strings =====
const lesson13 = pythonLessons.find(l => l.id === 13);
if (lesson13 && !lesson13.additionalExamples) {
  lesson13.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic f-string
name = 'Alice'
print(f'Hello, {name}!')  # Hello, Alice!

# Multiple variables
age = 25
city = 'NYC'
print(f'{name} is {age} years old and lives in {city}')

# Expressions in f-strings
x = 10
y = 20
print(f'{x} + {y} = {x + y}')  # 10 + 20 = 30

# Calling functions in f-strings
text = 'python'
print(f'Uppercase: {text.upper()}')  # Uppercase: PYTHON

# Formatting numbers
pi = 3.14159
print(f'Pi: {pi:.2f}')  # Pi: 3.14 (2 decimal places)

# Formatting with width
num = 42
print(f'Number: {num:5}')   # 'Number:    42' (5 chars wide)
print(f'Number: {num:05}')  # 'Number: 00042' (zero-padded)

# Percentage formatting
score = 0.856
print(f'Score: {score:.1%}')  # Score: 85.6%

# String concatenation vs f-strings
# Old way
greeting = 'Hello, ' + name + '!'
# New way (f-string)
greeting = f'Hello, {name}!'

# Multi-line f-strings
message = f"""
Name: {name}
Age: {age}
City: {city}
"""
print(message)

# Dictionary values in f-strings
person = {'name': 'Bob', 'age': 30}
print(f"{person['name']} is {person['age']}")

# Using expressions
items = ['apple', 'banana', 'cherry']
print(f'First item: {items[0]}')
print(f'Number of items: {len(items)}')

# Escaping braces
print(f'Use {{double braces}} to show literal braces')

# Practical: receipt
item = 'Book'
price = 19.99
quantity = 3
total = price * quantity
print(f'Item: {item}')
print(f'Price: {price:.2f}')
print(f'Qty: {quantity}')
print(f'Total: {total:.2f}')
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 13: Strings & f-Strings');
}

// ===== PYTHON LESSON 14: List Indexing & len() =====
const lesson14 = pythonLessons.find(l => l.id === 14);
if (lesson14 && !lesson14.additionalExamples) {
  lesson14.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic indexing
numbers = [4, 8, 15, 16, 23, 42]
print(numbers[0])   # 4 (first element)
print(numbers[3])   # 16 (fourth element)

# Negative indexing (from end)
print(numbers[-1])  # 42 (last element)
print(numbers[-2])  # 23 (second to last)

# Length
print(len(numbers))  # 6

# Last element using len
last = numbers[len(numbers) - 1]
print(last)  # 42

# Checking if list is empty
empty_list = []
if len(empty_list) == 0:
    print('List is empty')

# Iterating with index
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(f'Index {i}: {fruits[i]}')

# Getting middle element
middle_index = len(numbers) // 2
print(numbers[middle_index])  # 15

# Slicing with indices
print(numbers[1:4])   # [8, 15, 16] (index 1 to 3)
print(numbers[:3])    # [4, 8, 15] (first 3)
print(numbers[3:])    # [16, 23, 42] (from index 3)

# Copy entire list
copy = numbers[:]
print(copy)

# Reverse with slicing
reversed_list = numbers[::-1]
print(reversed_list)  # [42, 23, 16, 15, 8, 4]

# Finding index of element
fruits = ['apple', 'banana', 'cherry', 'banana']
index = fruits.index('banana')
print(f'First banana at index: {index}')  # 1

# Checking if element exists
if 'cherry' in fruits:
    print('Cherry found!')

# Counting occurrences
count = fruits.count('banana')
print(f'Banana appears {count} times')  # 2

# Practical: accessing student scores
scores = [85, 92, 78, 95, 88]
print(f'Total students: {len(scores)}')
print(f'First score: {scores[0]}')
print(f'Last score: {scores[-1]}')
print(f'Average: {sum(scores) / len(scores)}')

# Safe indexing with bounds check
index = 10
if 0 <= index < len(numbers):
    print(numbers[index])
else:
    print('Index out of range')
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 14: List Indexing & len()');
}

// Write Python lessons back
fs.writeFileSync('public/lessons-python.json', JSON.stringify(pythonLessons, null, 2));
console.log(`\n✅ Modified ${modificationCount} Python lessons`);

// Now improve Java lessons
let javaModCount = 0;

// ===== JAVA LESSON 21: Enhanced For Loop =====
const javaLesson21 = javaLessons.find(l => l.id === 21);
if (javaLesson21 && !javaLesson21.additionalExamples) {
  javaLesson21.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Basic enhanced for loop (for-each)
String[] fruits = {"apple", "banana", "cherry"};
for (String fruit : fruits) {
    System.out.println(fruit);
}

// With integers
int[] numbers = {10, 20, 30, 40, 50};
for (int num : numbers) {
    System.out.println(num);
}

// Calculating sum
int sum = 0;
for (int num : numbers) {
    sum += num;
}
System.out.println("Sum: " + sum);  // 150

// Finding maximum
int max = numbers[0];
for (int num : numbers) {
    if (num > max) {
        max = num;
    }
}
System.out.println("Max: " + max);

// With ArrayList
import java.util.ArrayList;
ArrayList&lt;String&gt; names = new ArrayList&lt;&gt;();
names.add("Alice");
names.add("Bob");
names.add("Charlie");

for (String name : names) {
    System.out.println("Hello, " + name);
}

// Cannot modify array during enhanced for loop
// This only modifies the loop variable, not the array
int[] nums = {1, 2, 3};
for (int n : nums) {
    n = n * 2;  // This does NOT change the array
}
// nums is still {1, 2, 3}

// Use traditional for loop to modify
for (int i = 0; i < nums.length; i++) {
    nums[i] = nums[i] * 2;  // This DOES change the array
}

// Practical: processing grades
double[] grades = {85.5, 92.0, 78.5, 95.0, 88.0};
double total = 0;
for (double grade : grades) {
    total += grade;
}
double average = total / grades.length;
System.out.println("Average: " + average);

// Counting elements
String[] words = {"cat", "elephant", "dog", "bear"};
int longWords = 0;
for (String word : words) {
    if (word.length() > 3) {
        longWords++;
    }
}
System.out.println("Words longer than 3 chars: " + longWords);

// Nested enhanced for loops
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

for (int[] row : matrix) {
    for (int value : row) {
        System.out.print(value + " ");
    }
    System.out.println();
}

// When to use enhanced for loop:
// - Reading/processing all elements
// - No need for index
// - Cleaner, more readable code

// When to use traditional for loop:
// - Need the index
// - Modifying array elements
// - Not processing all elements
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 21: Enhanced For Loop');
}

// ===== JAVA LESSON 22: User Input (Scanner) =====
const javaLesson22 = javaLessons.find(l => l.id === 22);
if (javaLesson22 && !javaLesson22.additionalExamples) {
  javaLesson22.additionalExamples = `
<h5>More Examples:</h5>
<pre>
import java.util.Scanner;

// Basic Scanner usage
Scanner scanner = new Scanner(System.in);

System.out.print("Enter your name: ");
String name = scanner.nextLine();
System.out.println("Hello, " + name);

// Reading integers
System.out.print("Enter your age: ");
int age = scanner.nextInt();
System.out.println("You are " + age + " years old");

// Reading doubles
System.out.print("Enter price: ");
double price = scanner.nextDouble();
System.out.println("Price: $" + price);

// Reading multiple values
System.out.print("Enter two numbers: ");
int num1 = scanner.nextInt();
int num2 = scanner.nextInt();
System.out.println("Sum: " + (num1 + num2));

// Important: nextLine() after next() or nextInt()
scanner.nextInt();  // Reads number but leaves newline
scanner.nextLine(); // Consume the leftover newline
String text = scanner.nextLine();  // Now reads full line

// Practical: calculator
System.out.print("Enter first number: ");
double a = scanner.nextDouble();
System.out.print("Enter operator (+, -, *, /): ");
String op = scanner.next();
System.out.print("Enter second number: ");
double b = scanner.nextDouble();

double result = 0;
switch(op) {
    case "+": result = a + b; break;
    case "-": result = a - b; break;
    case "*": result = a * b; break;
    case "/": result = a / b; break;
}
System.out.println("Result: " + result);

// Reading yes/no
System.out.print("Continue? (yes/no): ");
String answer = scanner.next().toLowerCase();
if (answer.equals("yes")) {
    System.out.println("Continuing...");
}

// Input validation
int validAge = -1;
while (validAge < 0 || validAge > 120) {
    System.out.print("Enter valid age (0-120): ");
    if (scanner.hasNextInt()) {
        validAge = scanner.nextInt();
    } else {
        System.out.println("Invalid input!");
        scanner.next(); // Clear invalid input
    }
}

// Checking if input is available
if (scanner.hasNextInt()) {
    int number = scanner.nextInt();
} else {
    System.out.println("Not a number!");
}

// Reading entire line with spaces
System.out.print("Enter full name: ");
scanner.nextLine(); // Clear buffer
String fullName = scanner.nextLine();

// Always close scanner when done
scanner.close();

// Practical: user registration
Scanner input = new Scanner(System.in);

System.out.print("Username: ");
String username = input.nextLine();

System.out.print("Age: ");
int userAge = input.nextInt();

System.out.print("Email: ");
input.nextLine(); // Clear buffer
String email = input.nextLine();

System.out.println("\\nRegistration Complete!");
System.out.println("User: " + username);
System.out.println("Age: " + userAge);
System.out.println("Email: " + email);

input.close();
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 22: User Input (Scanner)');
}

// ===== JAVA LESSON 23: Switch Statement =====
const javaLesson23 = javaLessons.find(l => l.id === 23);
if (javaLesson23 && !javaLesson23.additionalExamples) {
  javaLesson23.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Basic switch statement
int day = 3;
switch(day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    case 3:
        System.out.println("Wednesday");
        break;
    case 4:
        System.out.println("Thursday");
        break;
    case 5:
        System.out.println("Friday");
        break;
    default:
        System.out.println("Weekend");
}

// Switch with strings
String fruit = "apple";
switch(fruit) {
    case "apple":
        System.out.println("Red or green");
        break;
    case "banana":
        System.out.println("Yellow");
        break;
    case "orange":
        System.out.println("Orange");
        break;
    default:
        System.out.println("Unknown fruit");
}

// Multiple cases with same action
char grade = 'B';
switch(grade) {
    case 'A':
    case 'B':
        System.out.println("Excellent!");
        break;
    case 'C':
        System.out.println("Good");
        break;
    case 'D':
        System.out.println("Passed");
        break;
    case 'F':
        System.out.println("Failed");
        break;
    default:
        System.out.println("Invalid grade");
}

// Calculator with switch
char operator = '+';
int a = 10, b = 5;
int result = 0;

switch(operator) {
    case '+':
        result = a + b;
        break;
    case '-':
        result = a - b;
        break;
    case '*':
        result = a * b;
        break;
    case '/':
        result = a / b;
        break;
    default:
        System.out.println("Invalid operator");
        return;
}
System.out.println("Result: " + result);

// Month days calculator
int month = 2;
int year = 2024;
int days;

switch(month) {
    case 1: case 3: case 5: case 7: case 8: case 10: case 12:
        days = 31;
        break;
    case 4: case 6: case 9: case 11:
        days = 30;
        break;
    case 2:
        // Check leap year
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            days = 29;
        } else {
            days = 28;
        }
        break;
    default:
        days = 0;
        System.out.println("Invalid month");
}
System.out.println("Days: " + days);

// Switch expressions (Java 14+)
// Modern syntax - no break needed
String dayType = switch(day) {
    case 1, 2, 3, 4, 5 -> "Weekday";
    case 6, 7 -> "Weekend";
    default -> "Invalid";
};

// Fall-through behavior (when break is omitted)
int score = 85;
switch(score / 10) {
    case 10:
    case 9:
        System.out.println("A");
        break;
    case 8:
        System.out.println("B");
        break;
    case 7:
        System.out.println("C");
        break;
    default:
        System.out.println("F");
}

// Practical: menu system
int choice = 2;
switch(choice) {
    case 1:
        System.out.println("Starting new game...");
        break;
    case 2:
        System.out.println("Loading saved game...");
        break;
    case 3:
        System.out.println("Opening settings...");
        break;
    case 4:
        System.out.println("Exiting...");
        break;
    default:
        System.out.println("Invalid choice");
}
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 23: Switch Statement');
}

// ===== JAVA LESSON 24: Modifying Array Elements =====
const javaLesson24 = javaLessons.find(l => l.id === 24);
if (javaLesson24 && !javaLesson24.additionalExamples) {
  javaLesson24.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Basic array modification
int[] numbers = {10, 20, 30, 40, 50};
numbers[0] = 15;  // Change first element
numbers[2] = 35;  // Change third element
System.out.println(numbers[0]);  // 15

// Modify in a loop
for (int i = 0; i < numbers.length; i++) {
    numbers[i] = numbers[i] * 2;  // Double each element
}
// numbers is now {30, 40, 70, 80, 100}

// Add value to all elements
int[] scores = {85, 92, 78, 95};
for (int i = 0; i < scores.length; i++) {
    scores[i] += 5;  // Add 5 bonus points to each
}

// Set all elements to same value
int[] arr = new int[5];
for (int i = 0; i < arr.length; i++) {
    arr[i] = 10;  // All elements now 10
}

// Modify based on condition
int[] values = {1, 2, 3, 4, 5, 6, 7, 8};
for (int i = 0; i < values.length; i++) {
    if (values[i] % 2 == 0) {
        values[i] = 0;  // Set even numbers to 0
    }
}

// Swap elements
int[] nums = {1, 2, 3, 4, 5};
// Swap first and last
int temp = nums[0];
nums[0] = nums[nums.length - 1];
nums[nums.length - 1] = temp;
// nums is now {5, 2, 3, 4, 1}

// Reverse array in place
int[] data = {1, 2, 3, 4, 5};
for (int i = 0; i < data.length / 2; i++) {
    int temp2 = data[i];
    data[i] = data[data.length - 1 - i];
    data[data.length - 1 - i] = temp2;
}
// data is now {5, 4, 3, 2, 1}

// Fill array with pattern
int[] pattern = new int[10];
for (int i = 0; i < pattern.length; i++) {
    pattern[i] = i * 2;  // 0, 2, 4, 6, 8, 10...
}

// Modify specific range
int[] range = {1, 2, 3, 4, 5, 6, 7, 8};
for (int i = 2; i < 5; i++) {
    range[i] = -1;  // Set elements 2-4 to -1
}

// Increment each element
int[] counters = {0, 0, 0, 0};
for (int i = 0; i < counters.length; i++) {
    counters[i]++;
}

// Practical: apply discount
double[] prices = {19.99, 29.99, 39.99};
double discount = 0.10;  // 10% off
for (int i = 0; i < prices.length; i++) {
    prices[i] = prices[i] * (1 - discount);
}

// Normalize scores to 0-100 range
int[] rawScores = {45, 50, 40, 48};
int maxScore = 50;
for (int i = 0; i < rawScores.length; i++) {
    rawScores[i] = (rawScores[i] * 100) / maxScore;
}

// Cap values at maximum
int[] values2 = {10, 150, 200, 50, 300};
int max = 100;
for (int i = 0; i < values2.length; i++) {
    if (values2[i] > max) {
        values2[i] = max;  // Cap at 100
    }
}

// Using Arrays.fill()
import java.util.Arrays;
int[] zeros = new int[5];
Arrays.fill(zeros, 0);  // All elements set to 0

int[] tens = new int[5];
Arrays.fill(tens, 10);  // All elements set to 10
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 24: Modifying Array Elements');
}

// Write Java lessons back
fs.writeFileSync('public/lessons-java.json', JSON.stringify(javaLessons, null, 2));
console.log(`✅ Modified ${javaModCount} Java lessons`);

console.log(`\n📊 Total modifications: ${modificationCount + javaModCount}`);
console.log('✅ Batch 9 improvements complete!');
