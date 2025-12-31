#!/usr/bin/env python3
"""
Upgrade 11 CRITICAL Java lessons with comprehensive content
Zero dependencies, multiple examples, real-world use cases
"""

import json

# Critical Java lesson upgrades
UPGRADES = {
    48: {
        "title": "Loop Practice - Multiplication Table",
        "solution": """/**
 * Loop Practice - Multiplication Table
 *
 * Master loops by building multiplication tables with various techniques.
 * Covers nested loops, formatting, and pattern generation.
 *
 * Zero external dependencies - pure Java
 */

public class Main {
    public static void main(String[] args) {

        // Example 1: Basic Multiplication Table
        System.out.println("=".repeat(70));
        System.out.println("Example 1: Basic Multiplication Table for 5");
        System.out.println("=".repeat(70));

        int number = 5;
        System.out.println("\\nMultiplication table for " + number + ":");

        for (int i = 1; i <= 10; i++) {
            int result = number * i;
            System.out.println(number + " x " + i + " = " + result);
        }

        // Example 2: Complete Multiplication Table (1-10)
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 2: Complete Multiplication Table (1-10)");
        System.out.println("=".repeat(70));

        System.out.println();
        // Print header
        System.out.print("   |");
        for (int i = 1; i <= 10; i++) {
            System.out.printf("%4d", i);
        }
        System.out.println();
        System.out.println("---+" + "-".repeat(40));

        // Print table
        for (int i = 1; i <= 10; i++) {
            System.out.printf("%2d |", i);
            for (int j = 1; j <= 10; j++) {
                System.out.printf("%4d", i * j);
            }
            System.out.println();
        }

        // Example 3: Formatted Table with Alignment
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 3: Beautifully Formatted Table");
        System.out.println("=".repeat(70));

        printMultiplicationTable(7, 12);

        // Example 4: Reverse Multiplication Table
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 4: Reverse Order (10 down to 1)");
        System.out.println("=".repeat(70));

        int num = 8;
        System.out.println("\\nReverse table for " + num + ":");
        for (int i = 10; i >= 1; i--) {
            System.out.printf("%d x %2d = %3d%n", num, i, num * i);
        }

        // Example 5: Range-based Multiplication
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 5: Custom Range (5 to 15)");
        System.out.println("=".repeat(70));

        printRangeTable(6, 5, 15);

        // Example 6: Multiple Tables Side by Side
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 6: Compare Two Tables Side by Side");
        System.out.println("=".repeat(70));

        printSideBySideTables(3, 7);

        // Example 7: Pattern Detection
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 7: Finding Patterns in Multiplication");
        System.out.println("=".repeat(70));

        analyzeMultiplicationPatterns(9);

        // Example 8: Practice Quiz Generator
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 8: Generate Practice Problems");
        System.out.println("=".repeat(70));

        generatePracticeProblems(5, 5);
    }

    /**
     * Print a formatted multiplication table for a number
     */
    static void printMultiplicationTable(int number, int upTo) {
        System.out.println("\\nMultiplication Table for " + number + " (1 to " + upTo + "):");
        System.out.println("-".repeat(40));

        for (int i = 1; i <= upTo; i++) {
            int result = number * i;
            String arrow = (i == 1 || i == upTo) ? " <-- " : "     ";
            System.out.printf("%2d × %2d = %4d%s%n", number, i, result,
                            i == 1 ? arrow + "Start" : (i == upTo ? arrow + "End" : ""));
        }
    }

    /**
     * Print multiplication table for a custom range
     */
    static void printRangeTable(int number, int start, int end) {
        System.out.println("\\nTable for " + number + " from " + start + " to " + end + ":");

        for (int i = start; i <= end; i++) {
            int result = number * i;
            System.out.printf("%d × %2d = %4d%n", number, i, result);
        }
    }

    /**
     * Print two multiplication tables side by side
     */
    static void printSideBySideTables(int num1, int num2) {
        System.out.printf("%n%-20s | %-20s%n",
                         "Table for " + num1, "Table for " + num2);
        System.out.println("-".repeat(44));

        for (int i = 1; i <= 10; i++) {
            System.out.printf("%d × %2d = %3d         | %d × %2d = %3d%n",
                            num1, i, num1 * i, num2, i, num2 * i);
        }
    }

    /**
     * Analyze patterns in multiplication
     */
    static void analyzeMultiplicationPatterns(int number) {
        System.out.println("\\nPattern Analysis for " + number + ":");

        int sumOfResults = 0;
        int[] results = new int[10];

        for (int i = 1; i <= 10; i++) {
            results[i-1] = number * i;
            sumOfResults += results[i-1];
        }

        System.out.println("  All results: " + java.util.Arrays.toString(results));
        System.out.println("  Sum of all: " + sumOfResults);
        System.out.println("  Average: " + (sumOfResults / 10.0));

        // Find even and odd results
        int evenCount = 0, oddCount = 0;
        for (int result : results) {
            if (result % 2 == 0) evenCount++;
            else oddCount++;
        }
        System.out.println("  Even results: " + evenCount);
        System.out.println("  Odd results: " + oddCount);
    }

    /**
     * Generate practice problems
     */
    static void generatePracticeProblems(int number, int count) {
        System.out.println("\\nPractice Problems for " + number + ":");
        System.out.println("(Try to solve before looking at answers!)\\n");

        for (int i = 1; i <= count; i++) {
            int multiplier = (int)(Math.random() * 12) + 1;
            System.out.printf("Problem %d: %d × %d = ?%n", i, number, multiplier);
        }

        System.out.println("\\n(Answers would be at the bottom in a real quiz)");
    }
}

/* Expected Output:
======================================================================
Example 1: Basic Multiplication Table for 5
======================================================================

Multiplication table for 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

======================================================================
Example 2: Complete Multiplication Table (1-10)
======================================================================

   |   1   2   3   4   5   6   7   8   9  10
---+----------------------------------------
 1 |   1   2   3   4   5   6   7   8   9  10
 2 |   2   4   6   8  10  12  14  16  18  20
...
10 |  10  20  30  40  50  60  70  80  90 100

Key Concepts:
- Nested loops for 2D patterns
- String formatting with printf
- Loop control and ranges
- Pattern recognition
*/"""
    },

    11: {
        "title": "StringBuilder Basics",
        "solution": """/**
 * StringBuilder Basics - Comprehensive Guide
 *
 * StringBuilder provides efficient string manipulation in Java.
 * Unlike String, StringBuilder is mutable and performs better
 * for multiple concatenation operations.
 *
 * Zero external dependencies - pure Java
 */

public class Main {
    public static void main(String[] args) {

        // Example 1: Basic StringBuilder Operations
        System.out.println("=".repeat(70));
        System.out.println("Example 1: Creating and Appending");
        System.out.println("=".repeat(70));

        StringBuilder sb = new StringBuilder();
        sb.append("Hello");
        sb.append(" ");
        sb.append("World");
        sb.append("!");

        System.out.println("Result: " + sb.toString());
        System.out.println("Length: " + sb.length());
        System.out.println("Capacity: " + sb.capacity());

        // Example 2: Method Chaining
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 2: Method Chaining");
        System.out.println("=".repeat(70));

        StringBuilder chain = new StringBuilder()
            .append("Java")
            .append(" is")
            .append(" awesome")
            .append("!");

        System.out.println("Chained result: " + chain);

        // Example 3: Insert Operations
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 3: Inserting Text");
        System.out.println("=".repeat(70));

        StringBuilder insert = new StringBuilder("Hello World");
        System.out.println("Original: " + insert);

        insert.insert(6, "Beautiful ");
        System.out.println("After insert at index 6: " + insert);

        insert.insert(0, ">>> ");
        System.out.println("After insert at start: " + insert);

        // Example 4: Delete and DeleteCharAt
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 4: Deleting Content");
        System.out.println("=".repeat(70));

        StringBuilder delete = new StringBuilder("Hello Beautiful World");
        System.out.println("Original: " + delete);

        delete.delete(6, 16); // Remove "Beautiful "
        System.out.println("After delete(6, 16): " + delete);

        delete.deleteCharAt(5); // Remove space
        System.out.println("After deleteCharAt(5): " + delete);

        // Example 5: Reverse
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 5: Reversing Strings");
        System.out.println("=".repeat(70));

        StringBuilder reverse = new StringBuilder("Hello");
        System.out.println("Original: " + reverse);

        reverse.reverse();
        System.out.println("Reversed: " + reverse);

        // Palindrome check
        String word = "racecar";
        StringBuilder palin = new StringBuilder(word);
        boolean isPalindrome = word.equals(palin.reverse().toString());
        System.out.println("\\n'" + word + "' is palindrome? " + isPalindrome);

        // Example 6: Replace
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 6: Replacing Content");
        System.out.println("=".repeat(70));

        StringBuilder replace = new StringBuilder("Java is good");
        System.out.println("Original: " + replace);

        replace.replace(8, 12, "great");
        System.out.println("After replace: " + replace);

        // Example 7: StringBuilder vs String Performance
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 7: Performance Comparison");
        System.out.println("=".repeat(70));

        demonstratePerformance();

        // Example 8: Building Complex Strings
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 8: Building HTML");
        System.out.println("=".repeat(70));

        String html = buildHTML();
        System.out.println(html);

        // Example 9: CSV Builder
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 9: Building CSV Data");
        System.out.println("=".repeat(70));

        String csv = buildCSV();
        System.out.println(csv);

        // Example 10: SQL Query Builder
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 10: Dynamic SQL Query");
        System.out.println("=".repeat(70));

        String sql = buildSQLQuery("users", new String[]{"name", "email", "age"}, "age > 18");
        System.out.println(sql);
    }

    /**
     * Demonstrate performance difference between String and StringBuilder
     */
    static void demonstratePerformance() {
        int iterations = 1000;

        // Using String concatenation (slow)
        long start1 = System.nanoTime();
        String str = "";
        for (int i = 0; i < iterations; i++) {
            str += "a";  // Creates new String object each time!
        }
        long end1 = System.nanoTime();

        // Using StringBuilder (fast)
        long start2 = System.nanoTime();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < iterations; i++) {
            sb.append("a");  // Modifies existing object
        }
        long end2 = System.nanoTime();

        System.out.println("String concatenation: " + (end1 - start1) / 1000 + " μs");
        System.out.println("StringBuilder append:  " + (end2 - start2) / 1000 + " μs");
        System.out.println("StringBuilder is ~" + ((end1 - start1) / (end2 - start2)) + "x faster!");
    }

    /**
     * Build HTML using StringBuilder
     */
    static String buildHTML() {
        StringBuilder html = new StringBuilder();

        html.append("<html>\\n");
        html.append("  <head>\\n");
        html.append("    <title>My Page</title>\\n");
        html.append("  </head>\\n");
        html.append("  <body>\\n");
        html.append("    <h1>Welcome</h1>\\n");
        html.append("    <p>This HTML was built with StringBuilder!</p>\\n");
        html.append("  </body>\\n");
        html.append("</html>");

        return html.toString();
    }

    /**
     * Build CSV data
     */
    static String buildCSV() {
        StringBuilder csv = new StringBuilder();

        // Header
        csv.append("Name,Age,City\\n");

        // Data rows
        String[][] data = {
            {"Alice", "25", "NYC"},
            {"Bob", "30", "LA"},
            {"Charlie", "35", "Chicago"}
        };

        for (String[] row : data) {
            csv.append(String.join(",", row)).append("\\n");
        }

        return csv.toString();
    }

    /**
     * Build SQL query dynamically
     */
    static String buildSQLQuery(String table, String[] columns, String condition) {
        StringBuilder sql = new StringBuilder();

        sql.append("SELECT ");
        sql.append(String.join(", ", columns));
        sql.append(" FROM ");
        sql.append(table);

        if (condition != null && !condition.isEmpty()) {
            sql.append(" WHERE ");
            sql.append(condition);
        }

        sql.append(";");

        return sql.toString();
    }
}

/* Key Takeaways:
 *
 * 1. StringBuilder is MUTABLE - can be modified without creating new objects
 * 2. Use StringBuilder when concatenating in loops - much faster!
 * 3. Methods: append(), insert(), delete(), reverse(), replace()
 * 4. Method chaining: sb.append("a").append("b").append("c")
 * 5. Convert to String: sb.toString()
 *
 * When to use:
 * ✓ Multiple concatenations in loops
 * ✓ Building complex strings (HTML, JSON, SQL)
 * ✓ String manipulation operations
 *
 * When NOT to use:
 * ✗ Single concatenation (just use +)
 * ✗ Thread-safe scenarios (use StringBuffer instead)
 */"""
    },

    49: {
        "title": "Loop Practice - Sum Numbers",
        "solution": """/**
 * Loop Practice - Sum Numbers
 *
 * Master different ways to sum numbers using loops.
 * Essential pattern for data processing and calculations.
 *
 * Zero external dependencies - pure Java
 */

public class Main {
    public static void main(String[] args) {

        // Example 1: Sum Array Elements
        System.out.println("=".repeat(70));
        System.out.println("Example 1: Sum Array Elements");
        System.out.println("=".repeat(70));

        int[] numbers = {1, 2, 3, 4, 5};
        int sum = 0;

        System.out.println("Numbers: " + java.util.Arrays.toString(numbers));

        for (int num : numbers) {
            sum += num;
            System.out.println("  Adding " + num + ", running sum: " + sum);
        }

        System.out.println("Total sum: " + sum);

        // Example 2: Sum with Index
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 2: Sum Using Index");
        System.out.println("=".repeat(70));

        int[] values = {10, 20, 30, 40, 50};
        int total = 0;

        for (int i = 0; i < values.length; i++) {
            total += values[i];
            System.out.printf("Index %d: value=%d, sum=%d%n", i, values[i], total);
        }

        System.out.println("Final total: " + total);

        // Example 3: Sum Range of Numbers
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 3: Sum Numbers 1 to 100");
        System.out.println("=".repeat(70));

        int sumRange = sumRange(1, 100);
        System.out.println("Sum of 1 to 100: " + sumRange);

        // Verify with formula: n(n+1)/2
        int formula = 100 * 101 / 2;
        System.out.println("Verified with formula: " + formula);

        // Example 4: Sum Even Numbers
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 4: Sum Only Even Numbers");
        System.out.println("=".repeat(70));

        int[] mixed = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int evenSum = 0;
        int evenCount = 0;

        System.out.println("Numbers: " + java.util.Arrays.toString(mixed));
        System.out.print("Even numbers: ");

        for (int num : mixed) {
            if (num % 2 == 0) {
                evenSum += num;
                evenCount++;
                System.out.print(num + " ");
            }
        }

        System.out.println("\\nSum of even numbers: " + evenSum);
        System.out.println("Count of even numbers: " + evenCount);
        System.out.println("Average: " + (double)evenSum / evenCount);

        // Example 5: Sum Positive Numbers Only
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 5: Sum Positive Numbers");
        System.out.println("=".repeat(70));

        int[] withNegatives = {-5, 10, -3, 8, -1, 15, 20};
        int positiveSum = sumPositive(withNegatives);

        System.out.println("Numbers: " + java.util.Arrays.toString(withNegatives));
        System.out.println("Sum of positive: " + positiveSum);

        // Example 6: Running Sum (Cumulative)
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 6: Running Sum (Cumulative)");
        System.out.println("=".repeat(70));

        int[] data = {5, 10, 15, 20, 25};
        int[] runningSum = calculateRunningSum(data);

        System.out.println("Original:    " + java.util.Arrays.toString(data));
        System.out.println("Running sum: " + java.util.Arrays.toString(runningSum));

        // Example 7: Sum with Condition
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 7: Sum Numbers Greater Than 10");
        System.out.println("=".repeat(70));

        int[] allNumbers = {5, 12, 8, 20, 3, 15, 25, 7};
        int conditionalSum = 0;

        System.out.println("All numbers: " + java.util.Arrays.toString(allNumbers));
        System.out.print("Numbers > 10: ");

        for (int num : allNumbers) {
            if (num > 10) {
                conditionalSum += num;
                System.out.print(num + " ");
            }
        }

        System.out.println("\\nSum: " + conditionalSum);

        // Example 8: Sum Multiple Arrays
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 8: Sum Multiple Arrays");
        System.out.println("=".repeat(70));

        int[] array1 = {1, 2, 3};
        int[] array2 = {4, 5, 6};
        int[] array3 = {7, 8, 9};

        int grandTotal = sumArrays(array1, array2, array3);
        System.out.println("Array 1: " + java.util.Arrays.toString(array1));
        System.out.println("Array 2: " + java.util.Arrays.toString(array2));
        System.out.println("Array 3: " + java.util.Arrays.toString(array3));
        System.out.println("Grand total: " + grandTotal);

        // Example 9: Sum Digits of a Number
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 9: Sum Digits of Number");
        System.out.println("=".repeat(70));

        int number = 12345;
        int digitSum = sumDigits(number);

        System.out.println("Number: " + number);
        System.out.println("Sum of digits: " + digitSum);
        System.out.println("Example: 1 + 2 + 3 + 4 + 5 = " + digitSum);

        // Example 10: Statistics
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 10: Calculate Statistics");
        System.out.println("=".repeat(70));

        int[] scores = {85, 92, 78, 95, 88, 76, 91};
        printStatistics(scores);
    }

    /**
     * Sum numbers in a range
     */
    static int sumRange(int start, int end) {
        int sum = 0;
        for (int i = start; i <= end; i++) {
            sum += i;
        }
        return sum;
    }

    /**
     * Sum only positive numbers
     */
    static int sumPositive(int[] arr) {
        int sum = 0;
        for (int num : arr) {
            if (num > 0) {
                sum += num;
            }
        }
        return sum;
    }

    /**
     * Calculate running sum
     */
    static int[] calculateRunningSum(int[] arr) {
        int[] result = new int[arr.length];
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
            result[i] = sum;
        }

        return result;
    }

    /**
     * Sum multiple arrays
     */
    static int sumArrays(int[]... arrays) {
        int total = 0;
        for (int[] arr : arrays) {
            for (int num : arr) {
                total += num;
            }
        }
        return total;
    }

    /**
     * Sum digits of a number
     */
    static int sumDigits(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    /**
     * Print statistics for an array
     */
    static void printStatistics(int[] arr) {
        int sum = 0;
        int min = arr[0];
        int max = arr[0];

        System.out.println("Scores: " + java.util.Arrays.toString(arr));

        for (int score : arr) {
            sum += score;
            if (score < min) min = score;
            if (score > max) max = score;
        }

        double average = (double) sum / arr.length;

        System.out.println("\\nStatistics:");
        System.out.println("  Sum: " + sum);
        System.out.println("  Count: " + arr.length);
        System.out.println("  Average: " + String.format("%.2f", average));
        System.out.println("  Min: " + min);
        System.out.println("  Max: " + max);
        System.out.println("  Range: " + (max - min));
    }
}

/* Key Concepts:
 * - Enhanced for loop: for (int num : array)
 * - Traditional for loop: for (int i = 0; i < length; i++)
 * - Accumulator pattern: sum += value
 * - Conditional summing
 * - Running/cumulative sums
 *
 * Common Use Cases:
 * - Calculate totals (shopping cart, invoices)
 * - Find averages (grades, scores)
 * - Data aggregation
 * - Financial calculations
 */"""
    }
}

def upgrade_lessons():
    """Upgrade critical Java lessons."""
    print("="*80)
    print("UPGRADING 11 CRITICAL JAVA LESSONS")
    print("="*80)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    upgraded_count = 0

    for lesson_id, upgrade_data in UPGRADES.items():
        lesson = next((l for l in lessons if l['id'] == lesson_id), None)

        if lesson:
            old_length = len(lesson.get('fullSolution', ''))
            lesson['fullSolution'] = upgrade_data['solution']
            new_length = len(lesson['fullSolution'])

            print(f"\nLesson {lesson_id}: {lesson['title']}")
            print(f"  {old_length:,} -> {new_length:,} characters "
                  f"(+{new_length - old_length:,}, +{((new_length - old_length)/old_length*100):.1f}%)")

            upgraded_count += 1

    with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)

    print("\n" + "="*80)
    print(f"UPGRADED {upgraded_count} CRITICAL JAVA LESSONS!")
    print("="*80)
    print("\nPhase 1 Progress: 3 of 11 critical lessons complete")
    print("Next batch coming...")

if __name__ == '__main__':
    upgrade_lessons()
