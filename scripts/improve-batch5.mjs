import fs from 'fs';

// Read lessons
const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

let modificationCount = 0;

// ===== PYTHON LESSON 5: While Loops =====
const lesson5 = pythonLessons.find(l => l.id === 5);
if (lesson5 && !lesson5.additionalExamples) {
  lesson5.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Count to 10
count = 1
while count <= 10:
    print(count)
    count += 1

# Countdown
timer = 5
while timer > 0:
    print(f"T-minus {timer}")
    timer -= 1
print("Blast off!")

# Accumulator pattern
total = 0
num = 1
while num <= 5:
    total += num
    num += 1
print(f"Sum: {total}")  # 15

# While with condition
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted")

# Break out of while loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 3:
        break  # Exit the loop

# Continue to skip iteration
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip 3
    print(i)  # Prints: 1, 2, 4, 5
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 5: While Loops');
}

// ===== PYTHON LESSON 58: Regular Expressions =====
const lesson58 = pythonLessons.find(l => l.id === 58);
if (lesson58 && !lesson58.additionalExamples) {
  lesson58.additionalExamples = `
<h5>More Examples:</h5>
<pre>
import re

# Find all digits
text = "I have 3 cats and 2 dogs"
digits = re.findall(r'\\d', text)
print(digits)  # ['3', '2']

# Find all words
words = re.findall(r'\\w+', "Hello, World!")
print(words)  # ['Hello', 'World']

# Match email pattern
email = "user@example.com"
if re.match(r'\\w+@\\w+\\.\\w+', email):
    print("Valid email")

# Search for pattern anywhere in string
text = "The price is $50"
match = re.search(r'\\$(\\d+)', text)
if match:
    print(f"Price: {match.group(1)}")  # 50

# Replace pattern
text = "Phone: 123-456-7890"
cleaned = re.sub(r'[^\\d]', '', text)
print(cleaned)  # 1234567890

# Split by pattern
data = "apple,banana;cherry:date"
items = re.split(r'[,;:]', data)
print(items)  # ['apple', 'banana', 'cherry', 'date']

# Check if string starts with pattern
if re.match(r'^Hello', "Hello World"):
    print("Starts with Hello")
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 58: Regular Expressions');
}

// ===== PYTHON LESSON 59: enumerate() =====
const lesson59 = pythonLessons.find(l => l.id === 59);
if (lesson59 && !lesson59.additionalExamples) {
  lesson59.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic enumerate
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start counting from 1 instead of 0
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. cherry

# Enumerate with strings
for i, char in enumerate("Python"):
    print(f"Index {i}: {char}")

# Using enumerate for position tracking
numbers = [10, 20, 30, 40, 50]
for i, num in enumerate(numbers):
    if num == 30:
        print(f"Found 30 at index {i}")

# Enumerate with list comprehension
indexed = [(i, val) for i, val in enumerate(['a', 'b', 'c'])]
print(indexed)  # [(0, 'a'), (1, 'b'), (2, 'c')]

# Practical: modify list based on index
scores = [85, 92, 78, 95]
for i, score in enumerate(scores):
    if score < 80:
        print(f"Student {i+1} needs improvement")
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 59: enumerate()');
}

// ===== PYTHON LESSON 60: Set Comprehension =====
const lesson60 = pythonLessons.find(l => l.id === 60);
if (lesson60 && !lesson60.additionalExamples) {
  lesson60.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic set comprehension
squares = {x**2 for x in range(6)}
print(squares)  # {0, 1, 4, 9, 16, 25}

# Set comprehension with condition
evens = {n for n in range(10) if n % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}

# Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {n for n in numbers}
print(unique)  # {1, 2, 3, 4}

# String manipulation
words = ['hello', 'world', 'hello', 'python']
unique_words = {word.upper() for word in words}
print(unique_words)  # {'HELLO', 'WORLD', 'PYTHON'}

# Set of lengths
words = ['cat', 'dog', 'bird', 'fish']
lengths = {len(word) for word in words}
print(lengths)  # {3, 4} - only unique lengths

# Filtering with multiple conditions
numbers = {n for n in range(20) if n % 2 == 0 and n > 10}
print(numbers)  # {12, 14, 16, 18}

# Practical: extract unique first letters
names = ['Alice', 'Bob', 'Charlie', 'Anna']
first_letters = {name[0] for name in names}
print(first_letters)  # {'A', 'B', 'C'}
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 60: Set Comprehension');
}

// Write Python lessons back
fs.writeFileSync('public/lessons-python.json', JSON.stringify(pythonLessons, null, 2));
console.log(`\n✅ Modified ${modificationCount} Python lessons`);

// Now improve Java lessons
let javaModCount = 0;

// ===== JAVA LESSON 7: For Loops =====
const javaLesson7 = javaLessons.find(l => l.id === 7);
if (javaLesson7 && !javaLesson7.additionalExamples) {
  javaLesson7.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Count from 1 to 10
for (int i = 1; i <= 10; i++) {
    System.out.println(i);
}

// Countdown
for (int i = 5; i > 0; i--) {
    System.out.println("T-minus " + i);
}
System.out.println("Blast off!");

// Count by 2s
for (int i = 0; i <= 10; i += 2) {
    System.out.println(i);  // 0, 2, 4, 6, 8, 10
}

// Accumulator pattern
int sum = 0;
for (int i = 1; i <= 5; i++) {
    sum += i;
}
System.out.println("Sum: " + sum);  // 15

// Iterate through array
int[] numbers = {10, 20, 30, 40};
for (int i = 0; i < numbers.length; i++) {
    System.out.println("Index " + i + ": " + numbers[i]);
}

// Enhanced for loop (for-each)
String[] fruits = {"apple", "banana", "cherry"};
for (String fruit : fruits) {
    System.out.println(fruit);
}

// Nested loops (multiplication table)
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        System.out.print(i * j + " ");
    }
    System.out.println();
}
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 7: For Loops');
}

// ===== JAVA LESSON 8: Introduction to Arrays =====
const javaLesson8 = javaLessons.find(l => l.id === 8);
if (javaLesson8 && !javaLesson8.additionalExamples) {
  javaLesson8.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Declare and initialize array
int[] numbers = {10, 20, 30, 40, 50};
System.out.println(numbers[0]);  // 10
System.out.println(numbers[4]);  // 50

// Declare array with size, then assign values
String[] names = new String[3];
names[0] = "Alice";
names[1] = "Bob";
names[2] = "Charlie";

// Array length
System.out.println("Length: " + names.length);  // 3

// Loop through array
int[] scores = {85, 92, 78, 95, 88};
for (int i = 0; i < scores.length; i++) {
    System.out.println("Score " + i + ": " + scores[i]);
}

// Enhanced for loop
for (int score : scores) {
    System.out.println(score);
}

// Find max value
int max = scores[0];
for (int score : scores) {
    if (score > max) {
        max = score;
    }
}
System.out.println("Max: " + max);

// Sum all elements
int sum = 0;
for (int num : numbers) {
    sum += num;
}
System.out.println("Sum: " + sum);

// 2D array
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
System.out.println(matrix[1][2]);  // 6
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 8: Introduction to Arrays');
}

// ===== JAVA LESSON 10: Advanced Conditionals (Else If) =====
const javaLesson10 = javaLessons.find(l => l.id === 10);
if (javaLesson10 && !javaLesson10.additionalExamples) {
  javaLesson10.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Grade calculator
int score = 85;
if (score >= 90) {
    System.out.println("Grade: A");
} else if (score >= 80) {
    System.out.println("Grade: B");
} else if (score >= 70) {
    System.out.println("Grade: C");
} else if (score >= 60) {
    System.out.println("Grade: D");
} else {
    System.out.println("Grade: F");
}

// Temperature ranges
int temp = 75;
if (temp > 85) {
    System.out.println("Hot");
} else if (temp > 65) {
    System.out.println("Warm");
} else if (temp > 45) {
    System.out.println("Cool");
} else {
    System.out.println("Cold");
}

// Age categories
int age = 25;
if (age < 13) {
    System.out.println("Child");
} else if (age < 20) {
    System.out.println("Teenager");
} else if (age < 65) {
    System.out.println("Adult");
} else {
    System.out.println("Senior");
}

// Multiple conditions
int hour = 14;
boolean isWeekend = false;
if (hour < 12) {
    System.out.println("Morning");
} else if (hour < 17) {
    System.out.println("Afternoon");
} else if (hour < 21) {
    System.out.println("Evening");
} else {
    System.out.println("Night");
}
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 10: Advanced Conditionals (Else If)');
}

// ===== JAVA LESSON 12: Logical Operators =====
const javaLesson12 = javaLessons.find(l => l.id === 12);
if (javaLesson12 && !javaLesson12.additionalExamples) {
  javaLesson12.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// AND operator (&&) - both must be true
boolean loggedIn = true;
boolean isAdmin = false;
if (loggedIn && isAdmin) {
    System.out.println("Admin panel");  // Won't print
}

// OR operator (||) - at least one must be true
boolean hasTicket = false;
boolean isVIP = true;
if (hasTicket || isVIP) {
    System.out.println("Entry granted");  // Prints
}

// NOT operator (!) - inverts boolean
boolean isDarkMode = false;
if (!isDarkMode) {
    System.out.println("Light mode active");  // Prints
}

// Combining operators
int age = 25;
boolean hasLicense = true;
if (age >= 18 && hasLicense) {
    System.out.println("Can drive");
}

// Complex conditions
int score = 75;
boolean extraCredit = true;
if ((score >= 70 && score < 80) || extraCredit) {
    System.out.println("Passed with distinction");
}

// Range checking with AND
int temperature = 72;
if (temperature >= 65 && temperature <= 75) {
    System.out.println("Perfect weather");
}

// Multiple OR conditions
String day = "Saturday";
if (day.equals("Saturday") || day.equals("Sunday")) {
    System.out.println("Weekend!");
}

// NOT with comparisons
int inventory = 5;
if (!(inventory > 10)) {
    System.out.println("Low stock alert");
}
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 12: Logical Operators');
}

// Write Java lessons back
fs.writeFileSync('public/lessons-java.json', JSON.stringify(javaLessons, null, 2));
console.log(`✅ Modified ${javaModCount} Java lessons`);

console.log(`\n📊 Total modifications: ${modificationCount + javaModCount}`);
console.log('✅ Batch 5 improvements complete!');
