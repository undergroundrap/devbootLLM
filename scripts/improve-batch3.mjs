import fs from 'fs';

// Read lessons
const pythonLessons = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const javaLessons = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));

let modificationCount = 0;

// ===== PYTHON LESSON 4: Comparison Operators =====
const lesson4 = pythonLessons.find(l => l.id === 4);
if (lesson4 && !lesson4.additionalExamples) {
  lesson4.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# All comparison operators
print(10 > 5)   # True: greater than
print(10 < 5)   # False: less than
print(10 >= 10) # True: greater than or equal
print(5 <= 10)  # True: less than or equal
print(5 == 5)   # True: equal to
print(5 != 10)  # True: not equal to

# String comparisons (alphabetical order)
print("apple" < "banana")  # True
print("zebra" > "apple")   # True

# Chained comparisons
age = 25
print(18 <= age < 65)  # True: age is between 18 and 65

# Practical example
price = 49.99
budget = 50.00
can_afford = price <= budget
print(can_afford)  # True
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 4: Comparison Operators');
}

// ===== PYTHON LESSON 414: Title case conversion =====
const lesson414 = pythonLessons.find(l => l.id === 414);
if (lesson414 && !lesson414.additionalExamples) {
  lesson414.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Title case with different inputs
print("HELLO WORLD".title())          # Hello World
print("python programming".title())   # Python Programming

# Preserving apostrophes
print("don't stop believing".title()) # Don'T Stop Believing

# Better handling for contractions - use split/join
text = "don't stop believing"
words = text.split()
result = ' '.join(word.capitalize() for word in words)
print(result)  # Don't Stop Believing

# Mixed case input
print("mIxEd CaSe TeXt".title())      # Mixed Case Text

# Real-world use case: formatting names
name = "john doe"
formatted = name.title()
print(formatted)  # John Doe
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 414: Title case conversion');
}

// ===== PYTHON LESSON 420: Or operator for default values =====
const lesson420 = pythonLessons.find(l => l.id === 420);
if (lesson420 && !lesson420.additionalExamples) {
  lesson420.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Using or for default values
username = None
display = username or "Anonymous"
print(display)  # Anonymous

# With empty string (considered falsy)
email = ""
contact = email or "no-email@example.com"
print(contact)  # no-email@example.com

# With actual value
user = "Alice"
name = user or "Guest"
print(name)  # Alice

# Chaining multiple or operators
config = None
backup = None
default = "default_value"
result = config or backup or default
print(result)  # default_value

# Practical example: getting environment variable with fallback
import os
port = os.environ.get('PORT') or 8080
print(port)  # 8080 (if PORT not set)
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 420: Or operator for default values');
}

// ===== PYTHON LESSON 430: Supplier for Lazy Evaluation =====
const lesson430 = pythonLessons.find(l => l.id === 430);
if (lesson430 && !lesson430.additionalExamples) {
  lesson430.additionalExamples = `
<h5>More Examples:</h5>
<pre>
# Lazy evaluation with lambda
def expensive_operation():
    print("Computing...")
    return 42

# Without lazy evaluation - always computes
value = expensive_operation() or 10  # Prints "Computing..." even if not needed

# With lazy evaluation - only computes when needed
def get_value(supplier):
    return supplier() or 10

# Only calls if first value is falsy
result = get_value(lambda: None or expensive_operation())
print(result)  # Prints "Computing..." then 42

# Deferring computation example
def create_supplier(x):
    return lambda: x * 2

supplier = create_supplier(5)
print("Supplier created, but not executed yet")
print(supplier())  # 10 - computed when called

# Real-world: expensive database call
def get_default_config():
    print("Fetching from database...")
    return {"theme": "dark"}

# Only fetch if config is missing
user_config = None
config = user_config or (lambda: get_default_config())()
print(config)  # Fetches from database
</pre>`;
  modificationCount++;
  console.log('✓ Added examples to Lesson 430: Supplier for Lazy Evaluation');
}

// Write Python lessons back
fs.writeFileSync('public/lessons-python.json', JSON.stringify(pythonLessons, null, 2));
console.log(`\n✅ Modified ${modificationCount} Python lessons`);

// Now improve some Java lessons
let javaModCount = 0;

// ===== JAVA LESSON 37: Read Env Default =====
const javaLesson37 = javaLessons.find(l => l.id === 37);
if (javaLesson37 && !javaLesson37.additionalExamples) {
  javaLesson37.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Reading environment variables with defaults
String dbHost = System.getenv().getOrDefault("DB_HOST", "localhost");
String dbPort = System.getenv().getOrDefault("DB_PORT", "5432");
System.out.println("Database: " + dbHost + ":" + dbPort);

// Using for configuration
Map&lt;String, String&gt; config = System.getenv();
String logLevel = config.getOrDefault("LOG_LEVEL", "INFO");
String appEnv = config.getOrDefault("APP_ENV", "development");

// Multiple fallbacks pattern
String apiKey = System.getenv().getOrDefault("API_KEY",
                System.getenv().getOrDefault("BACKUP_API_KEY", "default-key"));

// Checking if variable exists
if (System.getenv("SECRET_KEY") != null) {
    // Use the secret
} else {
    System.out.println("Using default configuration");
}
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 37: Read Env Default');
}

// ===== JAVA LESSON 54: Access Modifiers (private) =====
const javaLesson54 = javaLessons.find(l => l.id === 54);
if (javaLesson54 && !javaLesson54.additionalExamples) {
  javaLesson54.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Encapsulation with private fields and public getters/setters
class BankAccount {
    private double balance;  // Private - can't access directly
    private String accountNumber;

    public BankAccount(String accountNumber) {
        this.accountNumber = accountNumber;
        this.balance = 0.0;
    }

    // Public methods to interact with private data
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public double getBalance() {
        return balance;  // Controlled access
    }
}

// Private helper methods
class Calculator {
    public int fibonacci(int n) {
        return fibHelper(n);
    }

    private int fibHelper(int n) {  // Internal implementation detail
        if (n <= 1) return n;
        return fibHelper(n - 1) + fibHelper(n - 2);
    }
}

// Usage
BankAccount account = new BankAccount("12345");
// account.balance = 1000;  // ERROR: balance is private
account.deposit(1000);      // OK: using public method
System.out.println(account.getBalance());  // 1000.0
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 54: Access Modifiers (private)');
}

// ===== JAVA LESSON 1 (assuming it's a beginner lesson needing examples) =====
const javaLesson1 = javaLessons.find(l => l.id === 1);
if (javaLesson1 && !javaLesson1.additionalExamples) {
  javaLesson1.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Printing different types
System.out.println("Hello, Java!");
System.out.println(42);
System.out.println(3.14);
System.out.println(true);

// Concatenating strings
System.out.println("Hello" + " " + "World");

// Printing with variables
String message = "Welcome to Java!";
System.out.println(message);

// Empty println adds a blank line
System.out.println("First line");
System.out.println();
System.out.println("After blank line");

// Using print (no newline) vs println
System.out.print("Same ");
System.out.print("line");
System.out.println();  // Now move to next line
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 1: Hello World');
}

// ===== JAVA LESSON 2 (Variables) =====
const javaLesson2 = javaLessons.find(l => l.id === 2);
if (javaLesson2 && !javaLesson2.additionalExamples) {
  javaLesson2.additionalExamples = `
<h5>More Examples:</h5>
<pre>
// Different data types
int age = 25;
double price = 19.99;
String name = "Alice";
boolean isActive = true;

// Multiple declarations
int x = 10, y = 20, z = 30;
System.out.println(x + y + z);  // 60

// Constants (final variables)
final double PI = 3.14159;
final int MAX_USERS = 100;
// PI = 3.14;  // ERROR: cannot reassign final variable

// Type inference with var (Java 10+)
var count = 42;        // int
var message = "Hello"; // String
var score = 98.5;      // double

// Variable naming conventions
int userCount;         // camelCase for variables
final int MAX_SIZE = 100;  // UPPER_SNAKE_CASE for constants
</pre>`;
  javaModCount++;
  console.log('✓ Added examples to Java Lesson 2: Variables');
}

// Write Java lessons back
fs.writeFileSync('public/lessons-java.json', JSON.stringify(javaLessons, null, 2));
console.log(`✅ Modified ${javaModCount} Java lessons`);

console.log(`\n📊 Total modifications: ${modificationCount + javaModCount}`);
console.log('✅ Batch 3 improvements complete!');
