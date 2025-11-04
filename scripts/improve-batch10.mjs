import fs from 'fs';

// Read lessons
const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

let modificationCount = 0;

// ===== PYTHON LESSON 15: Dictionaries =====
const lesson15 = pythonLessons.find(l => l.id === 15);
if (lesson15 && !lesson15.additionalExamples) {
  lesson15.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Creating dictionaries
capital_cities = {
    'England': 'London',
    'Germany': 'Berlin',
    'France': 'Paris'
}

# Accessing values
print(capital_cities['England'])  # London

# Using get() method (safer - returns None if key doesn't exist)
print(capital_cities.get('Spain'))        # None
print(capital_cities.get('Spain', 'N/A')) # N/A (default value)

# Adding new key-value pairs
capital_cities['Spain'] = 'Madrid'
print(capital_cities)

# Updating existing values
capital_cities['France'] = 'Nice'
print(capital_cities['France'])  # Nice

# Removing items
del capital_cities['Germany']
removed = capital_cities.pop('Spain')
print(f"Removed: {removed}")

# Checking if key exists
if 'England' in capital_cities:
    print('England is in the dictionary')

# Getting all keys, values, items
print(capital_cities.keys())    # dict_keys(['England', 'France'])
print(capital_cities.values())  # dict_values(['London', 'Nice'])
print(capital_cities.items())   # dict_items([('England', 'London'), ('France', 'Nice')])

# Iterating through dictionary
for country, city in capital_cities.items():
    print(f"{country}: {city}")

# Dictionary with different value types
person = {
    'name': 'Alice',
    'age': 25,
    'hobbies': ['reading', 'coding'],
    'is_active': True
}

# Nested dictionaries
users = {
    'user1': {'name': 'Alice', 'age': 25},
    'user2': {'name': 'Bob', 'age': 30}
}
print(users['user1']['name'])  # Alice

# Dictionary methods
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
scores.update({'David': 88})  # Add new entry
scores.clear()  # Remove all items

# Dictionary from lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']
profile = dict(zip(keys, values))
print(profile)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# Default dict values
inventory = {}
inventory['apples'] = inventory.get('apples', 0) + 5
print(inventory)  # {'apples': 5}
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 15: Dictionaries');
}

// ===== PYTHON LESSON 16: Dictionary Updates =====
const lesson16 = pythonLessons.find(l => l.id === 16);
if (lesson16 && !lesson16.additionalExamples) {
  lesson16.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic dictionary update
profile = {"name": "Ada", "level": "beginner"}
profile["skills"] = ["Python"]
print(profile)

# Updating existing key
profile["level"] = "intermediate"
print(profile)

# Update multiple items at once with update()
profile.update({"age": 25, "city": "NYC"})
print(profile)

# Merge two dictionaries
defaults = {"theme": "dark", "language": "en"}
user_prefs = {"theme": "light"}
defaults.update(user_prefs)  # user_prefs overrides defaults
print(defaults)  # {"theme": "light", "language": "en"}

# Using | operator (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # dict2 values override dict1
print(merged)  # {"a": 1, "b": 3, "c": 4}

# Conditional update
inventory = {"apples": 5, "oranges": 3}
# Only add if not exists
if "bananas" not in inventory:
    inventory["bananas"] = 10

# Increment counter
stats = {"views": 100}
stats["views"] = stats.get("views", 0) + 1
print(stats)  # {"views": 101}

# Update from another dict
config = {"debug": False, "timeout": 30}
overrides = {"timeout": 60, "retries": 3}
config.update(overrides)
print(config)  # {"debug": False, "timeout": 60, "retries": 3}

# Update with keyword arguments
settings = {"theme": "light"}
settings.update(theme="dark", font_size=14)
print(settings)  # {"theme": "dark", "font_size": 14}

# Practical: shopping cart
cart = {}
# Add items
cart["apple"] = 3
cart["banana"] = 5
# Update quantity
cart["apple"] += 2
print(f"Apples: {cart['apple']}")  # 5

# Building a dictionary incrementally
word_count = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {"apple": 3, "banana": 2, "cherry": 1}

# Remove and update
data = {"a": 1, "b": 2, "c": 3}
data.pop("b")  # Remove key "b"
data.update({"d": 4})  # Add new key
print(data)  # {"a": 1, "c": 3, "d": 4}
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 16: Dictionary Updates');
}

// ===== PYTHON LESSON 19: List Methods =====
const lesson19 = pythonLessons.find(l => l.id === 19);
if (lesson19 && !lesson19.additionalExamples) {
  lesson19.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# append() - add item to end
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # ['apple', 'banana', 'cherry']

# insert() - add at specific index
fruits.insert(1, 'orange')
print(fruits)  # ['apple', 'orange', 'banana', 'cherry']

# extend() - add multiple items
fruits.extend(['mango', 'grape'])
print(fruits)  # ['apple', 'orange', 'banana', 'cherry', 'mango', 'grape']

# remove() - remove first occurrence
fruits.remove('banana')
print(fruits)  # ['apple', 'orange', 'cherry', 'mango', 'grape']

# pop() - remove and return item at index
last = fruits.pop()       # Remove last
first = fruits.pop(0)     # Remove first
print(f"Removed: {last}, {first}")

# clear() - remove all items
temp = [1, 2, 3]
temp.clear()
print(temp)  # []

# index() - find position of item
nums = [10, 20, 30, 40]
pos = nums.index(30)
print(f"30 is at index {pos}")  # 2

# count() - count occurrences
numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))  # 3

# sort() - sort in place
nums = [3, 1, 4, 1, 5]
nums.sort()
print(nums)  # [1, 1, 3, 4, 5]

# sort() with reverse
nums.sort(reverse=True)
print(nums)  # [5, 4, 3, 1, 1]

# reverse() - reverse in place
nums.reverse()
print(nums)  # [1, 1, 3, 4, 5]

# copy() - create shallow copy
original = [1, 2, 3]
copied = original.copy()
copied.append(4)
print(original)  # [1, 2, 3] (unchanged)
print(copied)    # [1, 2, 3, 4]

# Chaining methods
result = []
result.append(1)
result.append(2)
result.extend([3, 4])
result.sort(reverse=True)
print(result)  # [4, 3, 2, 1]

# Practical: managing a todo list
todos = []
todos.append("Buy groceries")
todos.append("Clean house")
todos.insert(0, "Wake up")  # Add to beginning
todos.remove("Clean house")
completed = todos.pop(0)    # Mark first as done
print(f"Completed: {completed}")
print(f"Remaining: {todos}")
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 19: List Methods');
}

// ===== PYTHON LESSON 25: Functions with Parameters =====
const lesson25 = pythonLessons.find(l => l.id === 25);
if (lesson25 && !lesson25.additionalExamples) {
  lesson25.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!

# Multiple parameters
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (uses default exponent=2)
print(power(5, 3))   # 125 (overrides default)

# Keyword arguments
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

describe_pet(animal="dog", name="Buddy")
describe_pet(name="Whiskers", animal="cat")

# Multiple return values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])
print(f"Min: {minimum}, Max: {maximum}, Avg: {average}")

# Variable number of arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# Keyword variable arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# Parameter type hints (documentation)
def multiply(x: int, y: int) -> int:
    return x * y

# Practical: calculate discount
def apply_discount(price, discount_percent=10):
    discount = price * (discount_percent / 100)
    return price - discount

print(apply_discount(100))      # 90.0 (10% off)
print(apply_discount(100, 20))  # 80.0 (20% off)

# Practical: format name
def format_name(first, last, middle=""):
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"

print(format_name("John", "Doe"))           # John Doe
print(format_name("John", "Doe", "Smith"))  # John Smith Doe

# Function calling another function
def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))  # 25

# Validation in functions
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Error: Division by zero
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 25: Functions with Parameters');
}

// Write Python lessons back
fs.writeFileSync('public/lessons-python.json', JSON.stringify(pythonLessons, null, 2));
console.log(`\n✅ Modified ${modificationCount} Python lessons`);

// Now improve Java lessons
let javaModCount = 0;

// ===== JAVA LESSON 25: Array Loop Accumulators =====
const javaLesson25 = javaLessons.find(l => l.id === 25);
if (javaLesson25 && !javaLesson25.additionalExamples) {
  javaLesson25.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Basic accumulator - sum
int[] numbers = {10, 20, 30, 40, 50};
int sum = 0;
for (int num : numbers) {
    sum += num;
}
System.out.println("Sum: " + sum);  // 150

// Accumulator - product
int[] values = {2, 3, 4, 5};
int product = 1;
for (int val : values) {
    product *= val;
}
System.out.println("Product: " + product);  // 120

// Count items matching condition
int[] scores = {85, 92, 78, 95, 88, 65};
int passing = 0;
for (int score : scores) {
    if (score >= 70) {
        passing++;
    }
}
System.out.println("Passing: " + passing);  // 5

// Build string accumulator
String[] words = {"Hello", "from", "Java"};
String sentence = "";
for (String word : words) {
    sentence += word + " ";
}
System.out.println(sentence.trim());  // Hello from Java

// Find maximum
int[] nums = {45, 23, 67, 12, 89, 34};
int max = nums[0];
for (int num : nums) {
    if (num > max) {
        max = num;
    }
}
System.out.println("Max: " + max);  // 89

// Find minimum
int min = nums[0];
for (int num : nums) {
    if (num < min) {
        min = num;
    }
}
System.out.println("Min: " + min);  // 12

// Count even and odd
int[] data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int evenCount = 0;
int oddCount = 0;
for (int n : data) {
    if (n % 2 == 0) {
        evenCount++;
    } else {
        oddCount++;
    }
}
System.out.println("Even: " + evenCount);  // 5
System.out.println("Odd: " + oddCount);    // 5

// Calculate average
double[] prices = {19.99, 29.99, 39.99, 49.99};
double total = 0;
for (double price : prices) {
    total += price;
}
double average = total / prices.length;
System.out.println("Average: " + average);

// Practical: calculate grade distribution
int[] grades = {85, 92, 78, 95, 88, 72, 65, 90};
int aCount = 0, bCount = 0, cCount = 0, fCount = 0;
for (int grade : grades) {
    if (grade >= 90) aCount++;
    else if (grade >= 80) bCount++;
    else if (grade >= 70) cCount++;
    else fCount++;
}
System.out.println("A: " + aCount);  // 3
System.out.println("B: " + bCount);  // 2
System.out.println("C: " + cCount);  // 2
System.out.println("F: " + fCount);  // 1

// Accumulate into new array
int[] source = {1, 2, 3, 4, 5};
int[] doubled = new int[source.length];
for (int i = 0; i < source.length; i++) {
    doubled[i] = source[i] * 2;
}
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 25: Array Loop Accumulators');
}

// ===== JAVA LESSON 26: Sum of Array Elements =====
const javaLesson26 = javaLessons.find(l => l.id === 26);
if (javaLesson26 && !javaLesson26.additionalExamples) {
  javaLesson26.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Basic sum with for loop
int[] numbers = {10, 20, 30, 40, 50};
int sum = 0;
for (int i = 0; i < numbers.length; i++) {
    sum += numbers[i];
}
System.out.println("Sum: " + sum);  // 150

// Sum with enhanced for loop
int total = 0;
for (int num : numbers) {
    total += num;
}
System.out.println("Total: " + total);  // 150

// Sum of doubles
double[] prices = {19.99, 29.99, 39.99};
double priceSum = 0.0;
for (double price : prices) {
    priceSum += price;
}
System.out.println("Total price: " + priceSum);

// Sum with method
public static int sumArray(int[] arr) {
    int sum = 0;
    for (int num : arr) {
        sum += num;
    }
    return sum;
}

int[] values = {5, 10, 15, 20};
System.out.println("Sum: " + sumArray(values));  // 50

// Sum only positive numbers
int[] mixed = {-5, 10, -3, 20, -8, 15};
int positiveSum = 0;
for (int num : mixed) {
    if (num > 0) {
        positiveSum += num;
    }
}
System.out.println("Positive sum: " + positiveSum);  // 45

// Sum only even numbers
int[] nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int evenSum = 0;
for (int num : nums) {
    if (num % 2 == 0) {
        evenSum += num;
    }
}
System.out.println("Even sum: " + evenSum);  // 30

// Sum with running total display
int[] scores = {85, 92, 78};
int runningSum = 0;
for (int i = 0; i < scores.length; i++) {
    runningSum += scores[i];
    System.out.println("After " + (i + 1) + " scores: " + runningSum);
}

// Using Java Streams (Java 8+)
import java.util.Arrays;
int streamSum = Arrays.stream(numbers).sum();
System.out.println("Stream sum: " + streamSum);

// Practical: calculate total bill
double[] items = {12.99, 5.50, 8.75, 15.00};
double subtotal = 0;
for (double item : items) {
    subtotal += item;
}
double tax = subtotal * 0.08;
double total_bill = subtotal + tax;
System.out.println("Subtotal: " + subtotal);
System.out.println("Tax: " + tax);
System.out.println("Total: " + total_bill);

// Sum of 2D array
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
int matrixSum = 0;
for (int[] row : matrix) {
    for (int val : row) {
        matrixSum += val;
    }
}
System.out.println("Matrix sum: " + matrixSum);  // 45
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 26: Sum of Array Elements');
}

// ===== JAVA LESSON 27: Finding the Maximum Value =====
const javaLesson27 = javaLessons.find(l => l.id === 27);
if (javaLesson27 && !javaLesson27.additionalExamples) {
  javaLesson27.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Basic find maximum
int[] numbers = {45, 23, 67, 12, 89, 34};
int max = numbers[0];
for (int i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
        max = numbers[i];
    }
}
System.out.println("Max: " + max);  // 89

// Find maximum with enhanced for loop
int maximum = numbers[0];
for (int num : numbers) {
    if (num > maximum) {
        maximum = num;
    }
}
System.out.println("Maximum: " + maximum);

// Find maximum and its index
int maxValue = numbers[0];
int maxIndex = 0;
for (int i = 0; i < numbers.length; i++) {
    if (numbers[i] > maxValue) {
        maxValue = numbers[i];
        maxIndex = i;
    }
}
System.out.println("Max value: " + maxValue + " at index " + maxIndex);

// Find max in double array
double[] prices = {19.99, 45.50, 12.75, 89.99};
double maxPrice = prices[0];
for (double price : prices) {
    if (price > maxPrice) {
        maxPrice = price;
    }
}
System.out.println("Highest price: " + maxPrice);

// Find max using method
public static int findMax(int[] arr) {
    int max = arr[0];
    for (int val : arr) {
        if (val > max) {
            max = val;
        }
    }
    return max;
}

int[] scores = {85, 92, 78, 95, 88};
System.out.println("Top score: " + findMax(scores));  // 95

// Find both min and max
int min = numbers[0];
int max2 = numbers[0];
for (int num : numbers) {
    if (num < min) min = num;
    if (num > max2) max2 = num;
}
System.out.println("Range: " + min + " to " + max2);

// Find max with condition
int[] temps = {72, 85, 90, 68, 95, 78};
int maxTemp = Integer.MIN_VALUE;
for (int temp : temps) {
    if (temp < 100 && temp > maxTemp) {  // Max below 100
        maxTemp = temp;
    }
}
System.out.println("Max temp below 100: " + maxTemp);

// Using Math.max()
int a = 10, b = 20;
int bigger = Math.max(a, b);
System.out.println("Bigger: " + bigger);  // 20

// Find max in nested arrays
int[][] matrix = {
    {3, 7, 2},
    {9, 1, 5},
    {4, 8, 6}
};
int matrixMax = matrix[0][0];
for (int[] row : matrix) {
    for (int val : row) {
        if (val > matrixMax) {
            matrixMax = val;
        }
    }
}
System.out.println("Matrix max: " + matrixMax);  // 9

// Practical: find highest grade student
String[] students = {"Alice", "Bob", "Charlie", "David"};
int[] grades = {85, 92, 78, 95};
int highestGrade = grades[0];
int topStudentIndex = 0;
for (int i = 0; i < grades.length; i++) {
    if (grades[i] > highestGrade) {
        highestGrade = grades[i];
        topStudentIndex = i;
    }
}
System.out.println("Top student: " + students[topStudentIndex]);
System.out.println("Grade: " + highestGrade);

// Using Java Streams (Java 8+)
import java.util.Arrays;
int streamMax = Arrays.stream(numbers).max().getAsInt();
System.out.println("Stream max: " + streamMax);
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 27: Finding the Maximum Value');
}

// ===== JAVA LESSON 28: Finding the Average =====
const javaLesson28 = javaLessons.find(l => l.id === 28);
if (javaLesson28 && !javaLesson28.additionalExamples) {
  javaLesson28.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Basic average calculation
int[] numbers = {10, 20, 30, 40, 50};
int sum = 0;
for (int num : numbers) {
    sum += num;
}
double average = (double) sum / numbers.length;
System.out.println("Average: " + average);  // 30.0

// Average with method
public static double calculateAverage(int[] arr) {
    int total = 0;
    for (int val : arr) {
        total += val;
    }
    return (double) total / arr.length;
}

int[] scores = {85, 92, 78, 95, 88};
System.out.println("Average score: " + calculateAverage(scores));

// Average of doubles
double[] prices = {19.99, 29.99, 39.99, 49.99};
double priceSum = 0.0;
for (double price : prices) {
    priceSum += price;
}
double avgPrice = priceSum / prices.length;
System.out.println("Average price: " + avgPrice);

// Formatted average
System.out.printf("Average: %.2f%n", average);  // 2 decimal places

// Average excluding outliers
int[] data = {10, 12, 100, 15, 13, 11};  // 100 is outlier
int count = 0;
int total = 0;
for (int val : data) {
    if (val < 50) {  // Exclude outliers > 50
        total += val;
        count++;
    }
}
double avgWithoutOutliers = (double) total / count;
System.out.println("Average (no outliers): " + avgWithoutOutliers);

// Moving average
int[] values = {10, 20, 30, 40, 50};
System.out.println("Moving averages:");
for (int i = 0; i < values.length - 1; i++) {
    double movingAvg = (values[i] + values[i + 1]) / 2.0;
    System.out.println("  " + movingAvg);
}

// Weighted average
int[] grades = {85, 90, 78};
double[] weights = {0.3, 0.5, 0.2};  // 30%, 50%, 20%
double weightedSum = 0;
for (int i = 0; i < grades.length; i++) {
    weightedSum += grades[i] * weights[i];
}
System.out.println("Weighted average: " + weightedSum);

// Average above threshold
int[] allScores = {55, 85, 92, 45, 78, 95, 60};
int qualifyingSum = 0;
int qualifyingCount = 0;
for (int score : allScores) {
    if (score >= 70) {
        qualifyingSum += score;
        qualifyingCount++;
    }
}
double qualifyingAvg = (double) qualifyingSum / qualifyingCount;
System.out.println("Average of passing scores: " + qualifyingAvg);

// Practical: class average
String[] students = {"Alice", "Bob", "Charlie", "David"};
int[] studentScores = {85, 92, 78, 95};
int classTotal = 0;
for (int score : studentScores) {
    classTotal += score;
}
double classAverage = (double) classTotal / studentScores.length;
System.out.println("Class average: " + classAverage);

// Find students above average
for (int i = 0; i < students.length; i++) {
    if (studentScores[i] > classAverage) {
        System.out.println(students[i] + " is above average");
    }
}

// Using Java Streams (Java 8+)
import java.util.Arrays;
double streamAvg = Arrays.stream(numbers).average().getAsDouble();
System.out.println("Stream average: " + streamAvg);

// Average of 2D array
int[][] matrix = {
    {10, 20, 30},
    {40, 50, 60}
};
int matrixSum = 0;
int elementCount = 0;
for (int[] row : matrix) {
    for (int val : row) {
        matrixSum += val;
        elementCount++;
    }
}
double matrixAvg = (double) matrixSum / elementCount;
System.out.println("Matrix average: " + matrixAvg);  // 35.0
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 28: Finding the Average');
}

// Write Java lessons back
fs.writeFileSync('public/lessons-java.json', JSON.stringify(javaLessons, null, 2));
console.log(`✅ Modified ${javaModCount} Java lessons`);

console.log(`\n📊 Total modifications: ${modificationCount + javaModCount}`);
console.log('✅ Batch 10 improvements complete!');
