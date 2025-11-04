import fs from 'fs';

// Read lessons
const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

let modificationCount = 0;

// ===== PYTHON LESSON 20: String Methods =====
const lesson20 = pythonLessons.find(l => l.id === 20);
if (lesson20 && !lesson20.additionalExamples) {
  lesson20.additionalExamples = `
<h5>More Examples:</h5>
<pre>
s = "Python Programming"

# Case conversion
print(s.upper())      # PYTHON PROGRAMMING
print(s.lower())      # python programming
print(s.title())      # Python Programming
print(s.swapcase())   # pYTHON pROGRAMMING

# Checking content
print(s.startswith("Python"))  # True
print(s.endswith("ing"))       # True
print(s.isalpha())             # False (has space)
print("123".isdigit())         # True

# Finding substrings
print(s.find("Pro"))       # 7 (index where found)
print(s.find("Java"))      # -1 (not found)
print(s.index("gram"))     # 11 (raises error if not found)
print(s.count("o"))        # 2 (occurrences)

# Modifying strings
print(s.replace("Python", "Java"))  # Java Programming
print("  hello  ".strip())          # "hello" (removes whitespace)
print("hello".center(10, '*'))      # **hello***

# Splitting and joining
words = s.split()                   # ['Python', 'Programming']
print('-'.join(words))              # Python-Programming

# Practical examples
email = "  USER@EXAMPLE.COM  "
clean_email = email.strip().lower()
print(clean_email)  # user@example.com
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 20: String Methods');
}

// ===== PYTHON LESSON 24: Max in a List =====
const lesson24 = pythonLessons.find(l => l.id === 24);
if (lesson24 && !lesson24.additionalExamples) {
  lesson24.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic max/min
numbers = [1, 44, 7, 99, 23, 42]
print(max(numbers))  # 99
print(min(numbers))  # 1

# Max/min with strings (alphabetical order)
words = ['zebra', 'apple', 'mango', 'banana']
print(max(words))  # zebra
print(min(words))  # apple

# Max with key function (custom comparison)
words = ['cat', 'elephant', 'dog']
longest = max(words, key=len)
print(longest)  # elephant

# Max with lambda
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
top_student = max(students, key=lambda x: x[1])
print(top_student)  # ('Bob', 92)

# Finding index of max value
numbers = [10, 50, 30, 80, 20]
max_index = numbers.index(max(numbers))
print(f"Max at index {max_index}: {numbers[max_index]}")  # Index 3: 80

# Max of multiple arguments
print(max(5, 12, 3, 9))  # 12

# Practical: find most expensive item
prices = {'apple': 1.20, 'banana': 0.50, 'orange': 1.50}
most_expensive = max(prices, key=prices.get)
print(f"{most_expensive}: ` + '$' + `{prices[most_expensive]}")  # orange: $1.5
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 24: Max in a List');
}

// ===== PYTHON LESSON 37: Lambda/map/filter =====
const lesson37 = pythonLessons.find(l => l.id === 37);
if (lesson37 && !lesson37.additionalExamples) {
  lesson37.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Map: transform each element
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Map with multiple lists
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, nums1, nums2))
print(sums)  # [11, 22, 33]

# Filter: keep only matching elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8]

# Filter strings
words = ['apple', 'banana', 'kiwi', 'strawberry']
short_words = list(filter(lambda w: len(w) <= 5, words))
print(short_words)  # ['apple', 'kiwi']

# Combining map and filter
numbers = [1, 2, 3, 4, 5]
# Square only even numbers
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 16]

# List comprehension alternative (more Pythonic)
doubled = [x * 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

# Practical: process names
names = ['alice', 'bob', 'charlie']
capitalized = list(map(lambda name: name.title(), names))
print(capitalized)  # ['Alice', 'Bob', 'Charlie']

# Practical: filter valid emails
emails = ['user@example.com', 'invalid', 'test@test.org']
valid = list(filter(lambda e: '@' in e and '.' in e, emails))
print(valid)  # ['user@example.com', 'test@test.org']
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 37: Lambda/map/filter');
}

// ===== PYTHON LESSON 61: Regex Groups =====
const lesson61 = pythonLessons.find(l => l.id === 61);
if (lesson61 && !lesson61.additionalExamples) {
  lesson61.additionalExamples = `
<h5>More Examples:</h5>
<pre>
import re

# Capturing groups with parentheses
text = "Hello World"
match = re.search(r'^Hello\\s+(\\w+)$', text)
if match:
    print(match.group(1))  # World

# Multiple groups
date = "2024-03-15"
match = re.search(r'(\\d{4})-(\\d{2})-(\\d{2})', date)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")
    # Or access individually:
    print(match.group(1))  # 2024
    print(match.group(2))  # 03
    print(match.group(3))  # 15

# Named groups
email = "user@example.com"
match = re.search(r'(?P<username>\\w+)@(?P<domain>[\\w.]+)', email)
if match:
    print(match.group('username'))  # user
    print(match.group('domain'))    # example.com
    print(match.groupdict())        # {'username': 'user', 'domain': 'example.com'}

# Extracting phone numbers
phone = "Call me at (555) 123-4567"
match = re.search(r'\\((\\d{3})\\)\\s+(\\d{3})-(\\d{4})', phone)
if match:
    area_code, prefix, number = match.groups()
    print(f"{area_code}-{prefix}-{number}")  # 555-123-4567

# Findall with groups returns tuples
text = "Alice:25 Bob:30 Charlie:35"
matches = re.findall(r'(\\w+):(\\d+)', text)
print(matches)  # [('Alice', '25'), ('Bob', '30'), ('Charlie', '35')]

for name, age in matches:
    print(f"{name} is {age} years old")

# Optional groups
text = "Color: blue"
match = re.search(r'Color:\\s+(\\w+)(?:\\s+shade)?', text)
print(match.group(1))  # blue

# Backreferences (matching repeated patterns)
html = "<b>bold</b>"
match = re.search(r'<(\\w+)>.*?</\\1>', html)
if match:
    print(f"Tag: {match.group(1)}")  # b
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 61: Regex Groups');
}

// Write Python lessons back
fs.writeFileSync('public/lessons-python.json', JSON.stringify(pythonLessons, null, 2));
console.log(`\n✅ Modified ${modificationCount} Python lessons`);

// Now improve Java lessons
let javaModCount = 0;

// ===== JAVA LESSON 9: Intro to Classes & Objects =====
const javaLesson9 = javaLessons.find(l => l.id === 9);
if (javaLesson9 && !javaLesson9.additionalExamples) {
  javaLesson9.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Define a class
class Person {
    String name;
    int age;

    // Constructor
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method
    void introduce() {
        System.out.println("Hi, I'm " + name + " and I'm " + age);
    }
}

// Create and use objects
Person alice = new Person("Alice", 25);
Person bob = new Person("Bob", 30);

alice.introduce();  // Hi, I'm Alice and I'm 25
bob.introduce();    // Hi, I'm Bob and I'm 30

// Accessing fields
System.out.println(alice.name);  // Alice
alice.age = 26;  // Modify field
System.out.println(alice.age);   // 26

// Bank account example
class BankAccount {
    String accountNumber;
    double balance;

    BankAccount(String accountNumber, double initialBalance) {
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
    }

    void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: $" + amount);
    }

    void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdrew: $" + amount);
        } else {
            System.out.println("Insufficient funds");
        }
    }

    double getBalance() {
        return balance;
    }
}

BankAccount account = new BankAccount("12345", 100.0);
account.deposit(50);
account.withdraw(30);
System.out.println("Balance: $" + account.getBalance());  // $120.0

// Multiple objects
BankAccount acc1 = new BankAccount("11111", 500);
BankAccount acc2 = new BankAccount("22222", 1000);
// Each object has its own state
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 9: Intro to Classes & Objects');
}

// ===== JAVA LESSON 11: Else-If Chains with && =====
const javaLesson11 = javaLessons.find(l => l.id === 11);
if (javaLesson11 && !javaLesson11.additionalExamples) {
  javaLesson11.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Grade calculator with multiple conditions
int score = 85;
boolean extraCredit = true;

if (score >= 90 && score <= 100) {
    System.out.println("Grade: A");
} else if (score >= 80 && score < 90) {
    System.out.println("Grade: B");
} else if (score >= 70 && score < 80) {
    System.out.println("Grade: C");
} else if (score >= 60 && score < 70) {
    System.out.println("Grade: D");
} else {
    System.out.println("Grade: F");
}

// Access control with multiple checks
int age = 25;
boolean hasID = true;
boolean hasTicket = true;

if (age >= 21 && hasID && hasTicket) {
    System.out.println("Full access granted");
} else if (age >= 18 && hasID) {
    System.out.println("General admission");
} else if (age >= 13) {
    System.out.println("Youth admission");
} else {
    System.out.println("Requires guardian");
}

// Login validation
boolean validUsername = true;
boolean validPassword = true;
boolean accountActive = false;

if (validUsername && validPassword && accountActive) {
    System.out.println("Login successful");
} else if (validUsername && validPassword && !accountActive) {
    System.out.println("Account is suspended");
} else if (validUsername && !validPassword) {
    System.out.println("Incorrect password");
} else {
    System.out.println("User not found");
}

// Shipping calculator
double orderTotal = 75.00;
boolean isPremiumMember = true;

if (orderTotal >= 100) {
    System.out.println("Free shipping");
} else if (orderTotal >= 50 && isPremiumMember) {
    System.out.println("Free shipping (premium)");
} else if (orderTotal >= 50) {
    System.out.println("Shipping: $5");
} else {
    System.out.println("Shipping: $10");
}

// Weather advisory
int temp = 45;
boolean isRaining = true;

if (temp < 32 && isRaining) {
    System.out.println("Ice warning!");
} else if (temp < 50 && isRaining) {
    System.out.println("Bring an umbrella and jacket");
} else if (isRaining) {
    System.out.println("Bring an umbrella");
} else if (temp < 50) {
    System.out.println("Dress warmly");
} else {
    System.out.println("Nice weather!");
}
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 11: Else-If Chains with &&');
}

// ===== JAVA LESSON 74: Sort by Length =====
const javaLesson74 = javaLessons.find(l => l.id === 74);
if (javaLesson74 && !javaLesson74.additionalExamples) {
  javaLesson74.additionalExamples = `
<h5>More Examples:</h5>
<pre>
import java.util.*;

// Sort strings by length
List&lt;String&gt; words = Arrays.asList("cat", "elephant", "dog", "a", "zebra");

// Using Comparator
words.sort(Comparator.comparingInt(String::length));
System.out.println(words);  // [a, cat, dog, zebra, elephant]

// Sort by length, then alphabetically
List&lt;String&gt; items = Arrays.asList("bee", "cat", "ant", "dog", "ape");
items.sort(Comparator.comparingInt(String::length)
                     .thenComparing(String::compareTo));
System.out.println(items);  // [ant, ape, bee, cat, dog]

// Sort by length descending
List&lt;String&gt; fruits = Arrays.asList("apple", "kiwi", "banana", "pear");
fruits.sort(Comparator.comparingInt(String::length).reversed());
System.out.println(fruits);  // [banana, apple, kiwi, pear]

// Using lambda
List&lt;String&gt; names = Arrays.asList("Alice", "Bob", "Charlie", "Dan");
names.sort((a, b) -&gt; Integer.compare(a.length(), b.length()));
System.out.println(names);  // [Bob, Dan, Alice, Charlie]

// Sort custom objects by field
class Book {
    String title;
    int pages;

    Book(String title, int pages) {
        this.title = title;
        this.pages = pages;
    }

    @Override
    public String toString() {
        return title + " (" + pages + " pages)";
    }
}

List&lt;Book&gt; books = Arrays.asList(
    new Book("Short Story", 50),
    new Book("Novel", 300),
    new Book("Article", 10)
);

books.sort(Comparator.comparingInt(book -&gt; book.pages));
System.out.println(books);
// [Article (10 pages), Short Story (50 pages), Novel (300 pages)]

// Sort array by length
String[] arr = {"elephant", "cat", "dog"};
Arrays.sort(arr, Comparator.comparingInt(String::length));
System.out.println(Arrays.toString(arr));  // [cat, dog, elephant]
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 74: Sort by Length');
}

// ===== JAVA LESSON 80: Reverse Sort =====
const javaLesson80 = javaLessons.find(l => l.id === 80);
if (javaLesson80 && !javaLesson80.additionalExamples) {
  javaLesson80.additionalExamples = `
<h5>More Examples:</h5>
<pre>
import java.util.*;
import java.util.stream.*;

// Reverse sort with Collections
List&lt;Integer&gt; numbers = Arrays.asList(5, 2, 8, 1, 9);
Collections.sort(numbers, Collections.reverseOrder());
System.out.println(numbers);  // [9, 8, 5, 2, 1]

// Reverse sort strings
List&lt;String&gt; words = Arrays.asList("apple", "zebra", "banana", "kiwi");
words.sort(Comparator.reverseOrder());
System.out.println(words);  // [zebra, kiwi, banana, apple]

// Using reversed() with Comparator
List&lt;String&gt; names = Arrays.asList("Charlie", "Alice", "Bob");
names.sort(Comparator.naturalOrder().reversed());
System.out.println(names);  // [Charlie, Bob, Alice]

// Reverse sort by custom field
class Student {
    String name;
    int score;

    Student(String name, int score) {
        this.name = name;
        this.score = score;
    }

    @Override
    public String toString() {
        return name + ": " + score;
    }
}

List&lt;Student&gt; students = Arrays.asList(
    new Student("Alice", 85),
    new Student("Bob", 92),
    new Student("Charlie", 78)
);

// Sort by score descending (highest first)
students.sort(Comparator.comparingInt((Student s) -&gt; s.score).reversed());
System.out.println(students);  // [Bob: 92, Alice: 85, Charlie: 78]

// Using streams
List&lt;Integer&gt; nums = Arrays.asList(3, 1, 4, 1, 5, 9);
List&lt;Integer&gt; sorted = nums.stream()
                           .sorted(Comparator.reverseOrder())
                           .collect(Collectors.toList());
System.out.println(sorted);  // [9, 5, 4, 3, 1, 1]

// Reverse existing sorted list
List&lt;Integer&gt; ascending = Arrays.asList(1, 2, 3, 4, 5);
Collections.reverse(ascending);
System.out.println(ascending);  // [5, 4, 3, 2, 1]

// Array reverse sort
Integer[] arr = {5, 2, 8, 1, 9};
Arrays.sort(arr, Collections.reverseOrder());
System.out.println(Arrays.toString(arr));  // [9, 8, 5, 2, 1]

// Note: For primitive arrays, convert to Integer[] or use:
int[] primitiveArr = {5, 2, 8, 1, 9};
Arrays.sort(primitiveArr);  // Sort ascending first
// Then reverse manually or use streams
int[] reversed = IntStream.rangeClosed(1, primitiveArr.length)
                          .map(i -&gt; primitiveArr[primitiveArr.length - i])
                          .toArray();
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 80: Reverse Sort');
}

// Write Java lessons back
fs.writeFileSync('public/lessons-java.json', JSON.stringify(javaLessons, null, 2));
console.log(`✅ Modified ${javaModCount} Java lessons`);

console.log(`\n📊 Total modifications: ${modificationCount + javaModCount}`);
console.log('✅ Batch 6 improvements complete!');
