import fs from 'fs';

// Read lessons
const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

let modificationCount = 0;

// ===== PYTHON LESSON 10: If / Else =====
const lesson10 = pythonLessons.find(l => l.id === 10);
if (lesson10 && !lesson10.additionalExamples) {
  lesson10.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic if/else
x = 7
if x % 2 == 0:
    print('Even')
else:
    print('Odd')

# Temperature check
temp = 72
if temp > 75:
    print('It is hot')
else:
    print('It is not hot')

# Age verification
age = 25
if age >= 18:
    print('Adult')
else:
    print('Minor')

# Comparison with strings
password = "secret"
if password == "secret":
    print('Access granted')
else:
    print('Access denied')

# Nested if/else
score = 85
if score >= 90:
    print('A')
else:
    if score >= 80:
        print('B')
    else:
        print('C or lower')

# Using elif (better than nested)
score = 85
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')

# Practical: login check
username = "admin"
password = "pass123"

if username == "admin" and password == "pass123":
    print('Login successful')
else:
    print('Invalid credentials')

# Ternary operator (one-line if/else)
age = 20
status = 'Adult' if age >= 18 else 'Minor'
print(status)  # Adult

# Checking multiple conditions
num = 15
if num > 0:
    print('Positive')
else:
    print('Zero or negative')
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 10: If / Else');
}

// ===== PYTHON LESSON 54: Dict Comprehensions =====
const lesson54 = pythonLessons.find(l => l.id === 54);
if (lesson54 && !lesson54.additionalExamples) {
  lesson54.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic dict comprehension
squares = {i: i*i for i in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From list to dict
names = ['Alice', 'Bob', 'Charlie']
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# With condition
numbers = range(10)
even_squares = {n: n**2 for n in numbers if n % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Transform existing dict
prices = {'apple': 1.20, 'banana': 0.50, 'orange': 1.50}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)  # {'apple': 1.08, 'banana': 0.45, 'orange': 1.35}

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# Conditional value
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
passed = {name: 'Pass' if score >= 80 else 'Fail'
          for name, score in grades.items()}
print(passed)  # {'Alice': 'Pass', 'Bob': 'Pass', 'Charlie': 'Fail'}

# From two lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']
person = {k: v for k, v in zip(keys, values)}
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# Filter dict by value
scores = {'math': 85, 'english': 92, 'science': 78, 'history': 88}
high_scores = {subject: score for subject, score in scores.items()
               if score >= 85}
print(high_scores)  # {'math': 85, 'english': 92, 'history': 88}

# String manipulation
words = ['Hello', 'World', 'Python']
upper_dict = {word: word.upper() for word in words}
print(upper_dict)  # {'Hello': 'HELLO', 'World': 'WORLD', 'Python': 'PYTHON'}
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 54: Dict Comprehensions');
}

// ===== PYTHON LESSON 65: Lambda + map =====
const lesson65 = pythonLessons.find(l => l.id === 65);
if (lesson65 && !lesson65.additionalExamples) {
  lesson65.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic lambda with map
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6, 8, 10]

# Square numbers
squares = list(map(lambda x: x**2, [1, 2, 3, 4]))
print(squares)  # [1, 4, 9, 16]

# String manipulation
words = ['hello', 'world', 'python']
upper_words = list(map(lambda s: s.upper(), words))
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# Map with multiple arguments
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, nums1, nums2))
print(sums)  # [11, 22, 33]

# Convert to different type
str_nums = ['1', '2', '3', '4']
integers = list(map(int, str_nums))  # Can use built-in function
print(integers)  # [1, 2, 3, 4]

# Format strings
prices = [10.5, 20.75, 15.0]
formatted = list(map(lambda p: f"Price: ` + '$' + `{p:.2f}", prices))
print(formatted)  # ['Price: $10.50', 'Price: $20.75', 'Price: $15.00']

# Get lengths
words = ['cat', 'elephant', 'dog']
lengths = list(map(len, words))
print(lengths)  # [3, 8, 3]

# Practical: add tax
prices = [100, 200, 300]
with_tax = list(map(lambda p: p * 1.08, prices))
print(with_tax)  # [108.0, 216.0, 324.0]

# Chaining operations
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, map(lambda x: x + 1, nums)))
print(result)  # [4, 6, 8, 10, 12]

# Extract from dict
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30}
]
names = list(map(lambda p: p['name'], people))
print(names)  # ['Alice', 'Bob']
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 65: Lambda + map');
}

// ===== PYTHON LESSON 66: Filter Evens =====
const lesson66 = pythonLessons.find(l => l.id === 66);
if (lesson66 && !lesson66.additionalExamples) {
  lesson66.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Basic filter for evens
nums = range(10)
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)  # [0, 2, 4, 6, 8]

# Filter odds
odds = list(filter(lambda n: n % 2 != 0, range(10)))
print(odds)  # [1, 3, 5, 7, 9]

# Filter positive numbers
numbers = [-5, 3, -1, 7, -2, 8]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)  # [3, 7, 8]

# Filter strings by length
words = ['cat', 'elephant', 'dog', 'bird']
short_words = list(filter(lambda w: len(w) <= 3, words))
print(short_words)  # ['cat', 'dog']

# Filter by starting letter
names = ['Alice', 'Bob', 'Anna', 'Charlie', 'Amy']
a_names = list(filter(lambda n: n.startswith('A'), names))
print(a_names)  # ['Alice', 'Anna', 'Amy']

# Filter None and empty values
data = [1, None, 2, '', 3, 0, 4]
clean = list(filter(None, data))  # Removes falsy values
print(clean)  # [1, 2, 3, 4]

# Filter by range
numbers = [5, 15, 25, 35, 45]
in_range = list(filter(lambda x: 10 <= x <= 30, numbers))
print(in_range)  # [15, 25]

# Filter dict values
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 88}
high_scorers = dict(filter(lambda item: item[1] >= 85, scores.items()))
print(high_scorers)  # {'Alice': 85, 'Bob': 92, 'David': 88}

# Combining filter and map
nums = [1, 2, 3, 4, 5, 6, 7, 8]
# Square only even numbers
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(result)  # [4, 16, 36, 64]

# Practical: valid emails
emails = ['user@example.com', 'invalid', 'test@test.org', 'bad']
valid = list(filter(lambda e: '@' in e and '.' in e, emails))
print(valid)  # ['user@example.com', 'test@test.org']

# Filter by multiple conditions
ages = [15, 25, 35, 45, 55]
target_ages = list(filter(lambda age: age >= 18 and age <= 40, ages))
print(target_ages)  # [25, 35]
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 66: Filter Evens');
}

// Write Python lessons back
fs.writeFileSync('public/lessons-python.json', JSON.stringify(pythonLessons, null, 2));
console.log(`\n✅ Modified ${modificationCount} Python lessons`);

// Now improve Java lessons
let javaModCount = 0;

// ===== JAVA LESSON 17: String Concatenation =====
const javaLesson17 = javaLessons.find(l => l.id === 17);
if (javaLesson17 && !javaLesson17.additionalExamples) {
  javaLesson17.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Basic concatenation with +
String firstName = "John";
String lastName = "Doe";
String fullName = firstName + " " + lastName;
System.out.println(fullName);  // John Doe

// Concatenating multiple strings
String greeting = "Hello" + ", " + "World" + "!";
System.out.println(greeting);  // Hello, World!

// Concatenating strings and numbers
int age = 25;
String message = "I am " + age + " years old";
System.out.println(message);  // I am 25 years old

// Building a sentence
String subject = "Java";
String verb = "is";
String adjective = "awesome";
String sentence = subject + " " + verb + " " + adjective + "!";
System.out.println(sentence);  // Java is awesome!

// Concatenation with += operator
String result = "Hello";
result += " ";
result += "World";
System.out.println(result);  // Hello World

// Using String.format() for better readability
String name = "Alice";
int score = 95;
String formatted = String.format("%s scored %d points", name, score);
System.out.println(formatted);  // Alice scored 95 points

// Using StringBuilder (more efficient for multiple concatenations)
StringBuilder sb = new StringBuilder();
sb.append("Java");
sb.append(" ");
sb.append("Programming");
System.out.println(sb.toString());  // Java Programming

// StringBuilder in a loop (efficient)
StringBuilder numbers = new StringBuilder();
for (int i = 1; i <= 5; i++) {
    numbers.append(i);
    if (i < 5) numbers.append(", ");
}
System.out.println(numbers.toString());  // 1, 2, 3, 4, 5

// String.join() for arrays
String[] words = {"Hello", "from", "Java"};
String joined = String.join(" ", words);
System.out.println(joined);  // Hello from Java

// Practical: building a URL
String protocol = "https";
String domain = "example.com";
String path = "/api/users";
String url = protocol + "://" + domain + path;
System.out.println(url);  // https://example.com/api/users

// Text formatting with concatenation
double price = 19.99;
String priceTag = "Price: $" + price;
System.out.println(priceTag);  // Price: $19.99
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 17: String Concatenation');
}

// ===== JAVA LESSON 18: Constructors =====
const javaLesson18 = javaLessons.find(l => l.id === 18);
if (javaLesson18 && !javaLesson18.additionalExamples) {
  javaLesson18.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Basic constructor
class Car {
    String color;
    String model;

    // Constructor
    Car(String c, String m) {
        color = c;
        model = m;
    }

    void display() {
        System.out.println(model + " - " + color);
    }
}

Car myCar = new Car("Red", "Tesla");
myCar.display();  // Tesla - Red

// Constructor with default values
class Book {
    String title;
    int pages;

    // Constructor with parameters
    Book(String t, int p) {
        title = t;
        pages = p;
    }

    void info() {
        System.out.println(title + ": " + pages + " pages");
    }
}

Book book1 = new Book("Java Guide", 500);
book1.info();  // Java Guide: 500 pages

// Multiple constructors (overloading)
class Person {
    String name;
    int age;

    // Constructor with both parameters
    Person(String n, int a) {
        name = n;
        age = a;
    }

    // Constructor with only name
    Person(String n) {
        name = n;
        age = 0;  // Default age
    }

    // Default constructor
    Person() {
        name = "Unknown";
        age = 0;
    }
}

Person p1 = new Person("Alice", 25);
Person p2 = new Person("Bob");
Person p3 = new Person();

// Constructor with validation
class BankAccount {
    String accountNumber;
    double balance;

    BankAccount(String num, double bal) {
        accountNumber = num;
        if (bal >= 0) {
            balance = bal;
        } else {
            balance = 0;  // No negative balance
            System.out.println("Invalid balance, set to 0");
        }
    }
}

// Calling another constructor (constructor chaining)
class Rectangle {
    int width;
    int height;

    // Main constructor
    Rectangle(int w, int h) {
        width = w;
        height = h;
    }

    // Square constructor (calls main constructor)
    Rectangle(int side) {
        this(side, side);  // Call other constructor
    }
}

Rectangle rect = new Rectangle(5, 10);
Rectangle square = new Rectangle(5);  // 5x5 square

// Practical: initializing object state
class Student {
    String name;
    int id;
    double gpa;

    Student(String n, int i, double g) {
        name = n;
        id = i;
        gpa = g;
        System.out.println("Student created: " + name);
    }
}

Student s = new Student("Alice", 12345, 3.8);
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 18: Constructors');
}

// ===== JAVA LESSON 19: this for Fields in Constructors =====
const javaLesson19 = javaLessons.find(l => l.id === 19);
if (javaLesson19 && !javaLesson19.additionalExamples) {
  javaLesson19.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Using 'this' to distinguish field from parameter
class Person {
    private String name;
    private int age;

    Person(String name, int age) {
        this.name = name;  // this.name = field, name = parameter
        this.age = age;
    }

    void display() {
        System.out.println(this.name + " is " + this.age);
    }
}

Person p = new Person("Alice", 25);
p.display();  // Alice is 25

// Without 'this' - parameter names must differ
class Book {
    private String title;

    Book(String t) {  // Different name required
        title = t;    // No 'this' needed
    }
}

// With 'this' - clearer parameter names
class Book2 {
    private String title;

    Book2(String title) {  // Same name as field
        this.title = title;  // 'this' required
    }
}

// 'this' for calling another constructor
class Rectangle {
    private int width;
    private int height;

    Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    Rectangle(int size) {
        this(size, size);  // Call other constructor
    }
}

// Practical example: Student class
class Student {
    private String name;
    private int id;
    private double gpa;

    Student(String name, int id, double gpa) {
        this.name = name;
        this.id = id;
        this.gpa = gpa;
    }

    void printInfo() {
        System.out.println("Name: " + this.name);
        System.out.println("ID: " + this.id);
        System.out.println("GPA: " + this.gpa);
    }
}

Student student = new Student("Bob", 12345, 3.8);
student.printInfo();

// Using 'this' in methods
class Counter {
    private int value;

    Counter(int value) {
        this.value = value;
    }

    void increment() {
        this.value++;  // 'this' optional here but makes it clear
    }

    int getValue() {
        return this.value;
    }
}

// Returning 'this' for method chaining
class Builder {
    private String name;
    private int age;

    Builder setName(String name) {
        this.name = name;
        return this;  // Return current object
    }

    Builder setAge(int age) {
        this.age = age;
        return this;
    }

    void print() {
        System.out.println(this.name + ", " + this.age);
    }
}

Builder b = new Builder()
    .setName("Alice")
    .setAge(25);
b.print();  // Alice, 25

// 'this' with same-named local variables
class Account {
    private double balance;

    void deposit(double balance) {
        this.balance += balance;  // field += parameter
    }

    double getBalance() {
        return this.balance;
    }
}
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 19: this for Fields in Constructors');
}

// ===== JAVA LESSON 20: Static vs Instance Fields =====
const javaLesson20 = javaLessons.find(l => l.id === 20);
if (javaLesson20 && !javaLesson20.additionalExamples) {
  javaLesson20.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Instance fields - unique per object
class Car {
    String model;  // Instance field - each Car has its own model
    String color;  // Instance field - each Car has its own color

    Car(String m, String c) {
        model = m;
        color = c;
    }
}

Car car1 = new Car("Tesla", "Red");
Car car2 = new Car("BMW", "Blue");
System.out.println(car1.model);  // Tesla
System.out.println(car2.model);  // BMW

// Static fields - shared across all objects
class Counter {
    static int totalCount = 0;  // Static - shared by all Counter objects
    int instanceCount;          // Instance - unique per object

    Counter() {
        totalCount++;      // Increment shared counter
        instanceCount++;   // Increment instance counter
    }
}

Counter c1 = new Counter();
Counter c2 = new Counter();
Counter c3 = new Counter();

System.out.println(Counter.totalCount);  // 3 (shared)
System.out.println(c1.instanceCount);    // 1 (unique per object)
System.out.println(c2.instanceCount);    // 1

// Static vs Instance comparison
class Student {
    static String school = "MIT";  // Static - same for all students
    String name;                    // Instance - unique per student

    Student(String name) {
        this.name = name;
    }

    void display() {
        System.out.println(name + " attends " + school);
    }
}

Student s1 = new Student("Alice");
Student s2 = new Student("Bob");

s1.display();  // Alice attends MIT
s2.display();  // Bob attends MIT

Student.school = "Harvard";  // Change static field
s1.display();  // Alice attends Harvard
s2.display();  // Bob attends Harvard

// Practical: tracking instances
class Database {
    static int activeConnections = 0;  // Static - total connections
    String connectionId;                // Instance - unique ID

    Database(String id) {
        this.connectionId = id;
        activeConnections++;
    }

    void close() {
        activeConnections--;
    }

    static void printActiveConnections() {
        System.out.println("Active: " + activeConnections);
    }
}

Database db1 = new Database("DB-1");
Database db2 = new Database("DB-2");
Database.printActiveConnections();  // Active: 2

db1.close();
Database.printActiveConnections();  // Active: 1

// Static constants
class MathConstants {
    static final double PI = 3.14159;      // Static final - constant
    static final int MAX_VALUE = 100;

    static double calculateCircleArea(double radius) {
        return PI * radius * radius;
    }
}

System.out.println(MathConstants.PI);  // 3.14159
double area = MathConstants.calculateCircleArea(5);

// When to use static vs instance
class BankAccount {
    static double interestRate = 0.05;  // Static - same for all accounts
    double balance;                      // Instance - unique per account

    BankAccount(double balance) {
        this.balance = balance;
    }

    double calculateInterest() {
        return balance * interestRate;  // Uses both static and instance
    }
}

BankAccount acc1 = new BankAccount(1000);
BankAccount acc2 = new BankAccount(2000);

System.out.println(acc1.calculateInterest());  // 50.0
System.out.println(acc2.calculateInterest());  // 100.0

BankAccount.interestRate = 0.06;  // Change for all accounts
System.out.println(acc1.calculateInterest());  // 60.0
System.out.println(acc2.calculateInterest());  // 120.0
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 20: Static vs Instance Fields');
}

// Write Java lessons back
fs.writeFileSync('public/lessons-java.json', JSON.stringify(javaLessons, null, 2));
console.log(`✅ Modified ${javaModCount} Java lessons`);

console.log(`\n📊 Total modifications: ${modificationCount + javaModCount}`);
console.log('✅ Batch 8 improvements complete!');
