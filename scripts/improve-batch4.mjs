import fs from 'fs';

// Read lessons
const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

let modificationCount = 0;

// ===== PYTHON LESSON 38: Math Module =====
const lesson38 = pythonLessons.find(l => l.id === 38);
if (lesson38 && !lesson38.additionalExamples) {
  lesson38.additionalExamples = `
<h5>More Examples:</h5>
<pre>
import math

# Rounding functions
print(math.ceil(4.3))   # 5: round up
print(math.floor(4.7))  # 4: round down
print(round(4.5))       # 4: round to nearest (built-in)

# Trigonometric functions
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))            # 1.0

# Constants
print(math.pi)    # 3.141592653589793
print(math.e)     # 2.718281828459045

# Power and logarithm
print(math.pow(2, 3))   # 8.0: 2^3
print(math.log(math.e)) # 1.0: natural log
print(math.log10(100))  # 2.0: log base 10

# Practical example: distance formula
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"Distance: {distance}")  # 5.0
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 38: Math Module');
}

// ===== PYTHON LESSON 39: String Join =====
const lesson39 = pythonLessons.find(l => l.id === 39);
if (lesson39 && !lesson39.additionalExamples) {
  lesson39.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Join with different separators
words = ['Python', 'is', 'awesome']
print(' '.join(words))    # Python is awesome
print('-'.join(words))    # Python-is-awesome
print(''.join(words))     # Pythonisawesome

# Join numbers (need to convert to strings)
numbers = [1, 2, 3, 4, 5]
print(', '.join(str(n) for n in numbers))  # 1, 2, 3, 4, 5

# Creating CSV format
data = ['Alice', '25', 'Engineer']
csv_line = ','.join(data)
print(csv_line)  # Alice,25,Engineer

# Join with newline
lines = ['First line', 'Second line', 'Third line']
text = '\\n'.join(lines)
print(text)
# Output:
# First line
# Second line
# Third line

# Practical example: building a path
path_parts = ['home', 'user', 'documents', 'file.txt']
path = '/'.join(path_parts)
print(path)  # home/user/documents/file.txt
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 39: String Join');
}

// ===== PYTHON LESSON 44: Tuple Unpacking =====
const lesson44 = pythonLessons.find(l => l.id === 44);
if (lesson44 && !lesson44.additionalExamples) {
  lesson44.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Unpacking different numbers of values
x, y = (10, 20)
print(x, y)  # 10 20

# Swapping variables
a, b = 5, 10
a, b = b, a  # Swap
print(a, b)  # 10 5

# Unpacking with * (rest operator)
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Unpacking in loops
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
for num, word in pairs:
    print(f"{num}: {word}")

# Unpacking from functions
def get_coordinates():
    return (10, 20, 30)

x, y, z = get_coordinates()
print(x, y, z)  # 10 20 30

# Ignoring values with _
name, _, age = ('Alice', 'unused', 25)
print(name, age)  # Alice 25
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 44: Tuple Unpacking');
}

// ===== PYTHON LESSON 53: Sorting =====
const lesson53 = pythonLessons.find(l => l.id === 53);
if (lesson53 && !lesson53.additionalExamples) {
  lesson53.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Sort in-place vs. sorted()
nums = [3, 1, 4, 1, 5]
nums.sort()  # Modifies list in-place
print(nums)  # [1, 1, 3, 4, 5]

original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)  # Returns new sorted list
print(original)     # [3, 1, 4, 1, 5] - unchanged
print(sorted_copy)  # [1, 1, 3, 4, 5]

# Reverse sort
nums = [3, 1, 4, 1, 5]
nums.sort(reverse=True)
print(nums)  # [5, 4, 3, 1, 1]

# Sort strings
words = ['banana', 'apple', 'cherry']
words.sort()
print(words)  # ['apple', 'banana', 'cherry']

# Sort by key (custom sorting)
words = ['banana', 'pie', 'Washington', 'book']
words.sort(key=len)  # Sort by length
print(words)  # ['pie', 'book', 'banana', 'Washington']

# Sort case-insensitive
words = ['banana', 'Apple', 'cherry']
words.sort(key=str.lower)
print(words)  # ['Apple', 'banana', 'cherry']

# Sort complex objects
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
students.sort(key=lambda x: x[1], reverse=True)  # Sort by grade
print(students)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 53: Sorting');
}

// Write Python lessons back
fs.writeFileSync('public/lessons-python.json', JSON.stringify(pythonLessons, null, 2));
console.log(`\n✅ Modified ${modificationCount} Python lessons`);

// Now improve Java lessons
let javaModCount = 0;

// ===== JAVA LESSON 3: Arithmetic & Assignment =====
const javaLesson3 = javaLessons.find(l => l.id === 3);
if (javaLesson3 && !javaLesson3.additionalExamples) {
  javaLesson3.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// All compound assignment operators
int x = 10;
x += 5;   // x = x + 5  → 15
x -= 3;   // x = x - 3  → 12
x *= 2;   // x = x * 2  → 24
x /= 4;   // x = x / 4  → 6
x %= 4;   // x = x % 4  → 2 (remainder)

// String concatenation with +=
String message = "Hello";
message += " ";
message += "World";
System.out.println(message);  // Hello World

// Practical example: calculating total
int subtotal = 100;
int tax = 10;
int shipping = 15;

int total = 0;
total += subtotal;
total += tax;
total += shipping;
System.out.println("Total: " + total);  // 125

// Accumulator pattern
int sum = 0;
sum += 10;
sum += 20;
sum += 30;
System.out.println("Sum: " + sum);  // 60
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 3: Arithmetic & Assignment');
}

// ===== JAVA LESSON 4: Increment & Decrement =====
const javaLesson4 = javaLessons.find(l => l.id === 4);
if (javaLesson4 && !javaLesson4.additionalExamples) {
  javaLesson4.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Post-increment vs pre-increment
int a = 5;
int b = a++;  // b gets 5, then a becomes 6
System.out.println("b: " + b + ", a: " + a);  // b: 5, a: 6

int x = 5;
int y = ++x;  // x becomes 6, then y gets 6
System.out.println("y: " + y + ", x: " + x);  // y: 6, x: 6

// Post-decrement vs pre-decrement
int c = 10;
int d = c--;  // d gets 10, then c becomes 9
System.out.println("d: " + d + ", c: " + c);  // d: 10, c: 9

int m = 10;
int n = --m;  // m becomes 9, then n gets 9
System.out.println("n: " + n + ", m: " + m);  // n: 9, m: 9

// Common use in loops
int count = 0;
while (count < 5) {
    System.out.println(count);
    count++;  // Increment after each iteration
}

// Countdown
int timer = 3;
while (timer > 0) {
    System.out.println(timer);
    timer--;  // Decrement
}
System.out.println("Blast off!");
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 4: Increment & Decrement');
}

// ===== JAVA LESSON 5: Comparison Operators =====
const javaLesson5 = javaLessons.find(l => l.id === 5);
if (javaLesson5 && !javaLesson5.additionalExamples) {
  javaLesson5.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// All comparison operators
System.out.println(10 > 5);    // true
System.out.println(10 < 5);    // false
System.out.println(10 >= 10);  // true
System.out.println(5 <= 10);   // true
System.out.println(5 == 5);    // true
System.out.println(5 != 10);   // true

// Comparing strings (reference vs content)
String s1 = "hello";
String s2 = "hello";
String s3 = new String("hello");

System.out.println(s1 == s2);         // true (same reference)
System.out.println(s1 == s3);         // false (different references)
System.out.println(s1.equals(s3));    // true (same content)

// Practical examples
int age = 25;
boolean isAdult = age >= 18;
System.out.println("Is adult: " + isAdult);  // true

int price = 50;
int budget = 45;
boolean canAfford = price <= budget;
System.out.println("Can afford: " + canAfford);  // false

// Combining comparisons with logical operators
int score = 75;
boolean passed = score >= 70 && score <= 100;
System.out.println("Passed: " + passed);  // true
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 5: Comparison Operators');
}

// ===== JAVA LESSON 6: While Loops =====
const javaLesson6 = javaLessons.find(l => l.id === 6);
if (javaLesson6 && !javaLesson6.additionalExamples) {
  javaLesson6.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Count to 5
int i = 1;
while (i <= 5) {
    System.out.println(i);
    i++;
}
// Output: 1 2 3 4 5

// Countdown
int count = 5;
while (count > 0) {
    System.out.println(count);
    count--;
}
System.out.println("Liftoff!");

// Accumulator pattern
int sum = 0;
int n = 1;
while (n <= 10) {
    sum += n;
    n++;
}
System.out.println("Sum: " + sum);  // 55

// While with condition
int balance = 100;
while (balance > 0) {
    System.out.println("Balance: " + balance);
    balance -= 25;
}
System.out.println("Account empty");

// Do-while (runs at least once)
int x = 0;
do {
    System.out.println("Runs once: " + x);
    x++;
} while (x < 0);  // Condition is false, but body ran once

// Infinite loop prevention
int safety = 0;
while (true) {
    System.out.println("Loop: " + safety);
    safety++;
    if (safety >= 3) break;  // Exit condition
}
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 6: While Loops');
}

// Write Java lessons back
fs.writeFileSync('public/lessons-java.json', JSON.stringify(javaLessons, null, 2));
console.log(`✅ Modified ${javaModCount} Java lessons`);

console.log(`\n📊 Total modifications: ${modificationCount + javaModCount}`);
console.log('✅ Batch 4 improvements complete!');
