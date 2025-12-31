#!/usr/bin/env python3
"""
Upgrade final 6 CRITICAL Java lessons
IDs: 47, 41, 32, 203, 210, 39
"""

import json

UPGRADES = {
    47: {
        "title": "Loop Practice - Find First Match",
        "solution": """/**
 * Loop Practice - Find First Match
 *
 * Learn to find the first element matching a condition.
 * Essential pattern for search operations and data filtering.
 *
 * Zero external dependencies - pure Java
 */

public class Main {
    public static void main(String[] args) {

        // Example 1: Find First Even Number
        System.out.println("=".repeat(70));
        System.out.println("Example 1: Find First Even Number");
        System.out.println("=".repeat(70));

        int[] numbers = {1, 3, 5, 8, 9, 10};
        int firstEven = -1; // -1 means not found

        System.out.println("Numbers: " + java.util.Arrays.toString(numbers));
        System.out.print("Searching for first even number...\\n");

        for (int num : numbers) {
            if (num % 2 == 0) {
                firstEven = num;
                System.out.println("Found: " + firstEven);
                break; // Stop searching once found!
            }
        }

        if (firstEven == -1) {
            System.out.println("No even number found");
        }

        // Example 2: Find First Match with Index
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 2: Find First Match - Return Index");
        System.out.println("=".repeat(70));

        int[] data = {5, 10, 15, 20, 25, 30};
        int target = 20;

        int index = findFirstIndex(data, target);

        System.out.println("Array: " + java.util.Arrays.toString(data));
        System.out.println("Looking for: " + target);

        if (index != -1) {
            System.out.println("Found at index: " + index);
        } else {
            System.out.println("Not found");
        }

        // Example 3: Find First String Match
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 3: Find First String Starting With 'A'");
        System.out.println("=".repeat(70));

        String[] names = {"Bob", "Charlie", "Alice", "Adam", "Eve"};
        String firstA = findFirstStartingWith(names, 'A');

        System.out.println("Names: " + java.util.Arrays.toString(names));
        System.out.println("First name starting with 'A': " + firstA);

        // Example 4: Find First Greater Than
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 4: Find First Number > Threshold");
        System.out.println("=".repeat(70));

        int[] scores = {45, 52, 67, 89, 72, 95};
        int threshold = 70;

        int firstHigh = findFirstGreaterThan(scores, threshold);

        System.out.println("Scores: " + java.util.Arrays.toString(scores));
        System.out.println("Threshold: " + threshold);
        System.out.println("First score > " + threshold + ": " + firstHigh);

        // Example 5: Find First Negative
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 5: Find First Negative Number");
        System.out.println("=".repeat(70));

        int[] mixed = {5, 10, -3, 8, -1, 15};
        int firstNegative = findFirstNegative(mixed);

        System.out.println("Numbers: " + java.util.Arrays.toString(mixed));
        if (firstNegative != Integer.MAX_VALUE) {
            System.out.println("First negative: " + firstNegative);
        } else {
            System.out.println("No negative numbers found");
        }

        // Example 6: Find First Prime Number
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 6: Find First Prime Number");
        System.out.println("=".repeat(70));

        int[] candidates = {4, 6, 8, 9, 11, 14, 17};
        int firstPrime = findFirstPrime(candidates);

        System.out.println("Candidates: " + java.util.Arrays.toString(candidates));
        if (firstPrime != -1) {
            System.out.println("First prime: " + firstPrime);
        } else {
            System.out.println("No prime found");
        }

        // Example 7: Find First Matching Pattern
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 7: Find First Email");
        System.out.println("=".repeat(70));

        String[] inputs = {"username", "password123", "user@email.com", "another@test.com"};
        String firstEmail = findFirstEmail(inputs);

        System.out.println("Inputs: " + java.util.Arrays.toString(inputs));
        System.out.println("First email: " + firstEmail);

        // Example 8: Early Termination Benefits
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 8: Performance - Early Exit vs Full Scan");
        System.out.println("=".repeat(70));

        demonstrateEarlyExit();

        // Example 9: Multiple Conditions
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 9: Find First Match - Multiple Conditions");
        System.out.println("=".repeat(70));

        int[] values = {3, 7, 12, 18, 25, 30, 42};
        int result = findFirstEvenAndDivisibleBy6(values);

        System.out.println("Values: " + java.util.Arrays.toString(values));
        if (result != -1) {
            System.out.println("First even AND divisible by 6: " + result);
        } else {
            System.out.println("No match found");
        }
    }

    /**
     * Find first occurrence of target value
     */
    static int findFirstIndex(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1; // Not found
    }

    /**
     * Find first string starting with letter
     */
    static String findFirstStartingWith(String[] arr, char letter) {
        for (String str : arr) {
            if (str.charAt(0) == letter) {
                return str;
            }
        }
        return null;
    }

    /**
     * Find first number greater than threshold
     */
    static int findFirstGreaterThan(int[] arr, int threshold) {
        for (int num : arr) {
            if (num > threshold) {
                return num;
            }
        }
        return -1;
    }

    /**
     * Find first negative number
     */
    static int findFirstNegative(int[] arr) {
        for (int num : arr) {
            if (num < 0) {
                return num;
            }
        }
        return Integer.MAX_VALUE; // Sentinel value
    }

    /**
     * Check if number is prime
     */
    static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    /**
     * Find first prime number
     */
    static int findFirstPrime(int[] arr) {
        for (int num : arr) {
            if (isPrime(num)) {
                return num;
            }
        }
        return -1;
    }

    /**
     * Find first email address (simple check)
     */
    static String findFirstEmail(String[] arr) {
        for (String str : arr) {
            if (str.contains("@")) {
                return str;
            }
        }
        return null;
    }

    /**
     * Demonstrate early exit performance benefit
     */
    static void demonstrateEarlyExit() {
        int size = 1000000;
        int[] large = new int[size];

        // Put target near beginning
        large[10] = 999;

        // With early exit (efficient)
        long start1 = System.nanoTime();
        int found1 = -1;
        for (int i = 0; i < large.length; i++) {
            if (large[i] == 999) {
                found1 = i;
                break; // Exit early!
            }
        }
        long time1 = System.nanoTime() - start1;

        // Without early exit (inefficient)
        long start2 = System.nanoTime();
        int found2 = -1;
        for (int i = 0; i < large.length; i++) {
            if (large[i] == 999) {
                found2 = i;
                // No break - keeps searching!
            }
        }
        long time2 = System.nanoTime() - start2;

        System.out.println("Array size: " + size);
        System.out.println("Target at index: 10");
        System.out.println("\\nWith early exit (break):");
        System.out.println("  Time: " + time1/1000 + " μs");
        System.out.println("\\nWithout early exit:");
        System.out.println("  Time: " + time2/1000 + " μs");
        System.out.println("\\nSpeedup: ~" + (time2/time1) + "x faster!");
    }

    /**
     * Find first number meeting multiple conditions
     */
    static int findFirstEvenAndDivisibleBy6(int[] arr) {
        for (int num : arr) {
            if (num % 2 == 0 && num % 6 == 0) {
                return num;
            }
        }
        return -1;
    }
}

/* Key Concepts:
 * - Early termination with 'break'
 * - Sentinel values (-1, null, MAX_VALUE) for "not found"
 * - Performance benefits of early exit
 * - Search pattern: loop + condition + break
 *
 * Common Use Cases:
 * - Linear search
 * - Validation (find first error)
 * - User lookup
 * - Finding first available slot
 *
 * Best Practices:
 * - Use break to exit as soon as found
 * - Return meaningful "not found" indicator
 * - Document what "not found" value means
 */"""
    },

    41: {
        "title": "Date Formatting",
        "solution": """/**
 * Date Formatting - Comprehensive Guide
 *
 * Learn to format dates and times in various patterns using
 * Java's DateTimeFormatter. Essential for user interfaces,
 * reports, and internationalization.
 *
 * Zero external dependencies - uses java.time (Java 8+)
 */

import java.time.*;
import java.time.format.*;
import java.util.Locale;

public class Main {
    public static void main(String[] args) {

        // Example 1: Basic Date Formatting
        System.out.println("=".repeat(70));
        System.out.println("Example 1: Basic Date Formats");
        System.out.println("=".repeat(70));

        LocalDate date = LocalDate.of(2025, 3, 15);

        System.out.println("Date object: " + date);
        System.out.println("\\nFormatted outputs:");

        // ISO format (default)
        System.out.println("  ISO: " + date.format(DateTimeFormatter.ISO_DATE));

        // US style: MM/dd/yyyy
        System.out.println("  US:  " + date.format(DateTimeFormatter.ofPattern("MM/dd/yyyy")));

        // European style: dd/MM/yyyy
        System.out.println("  EU:  " + date.format(DateTimeFormatter.ofPattern("dd/MM/yyyy")));

        // Long format
        System.out.println("  Long: " + date.format(DateTimeFormatter.ofPattern("MMMM dd, yyyy")));

        // Example 2: Time Formatting
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 2: Time Formats");
        System.out.println("=".repeat(70));

        LocalTime time = LocalTime.of(14, 30, 45);

        System.out.println("Time object: " + time);
        System.out.println("\\nFormatted outputs:");

        // 24-hour format
        System.out.println("  24-hour: " + time.format(DateTimeFormatter.ofPattern("HH:mm:ss")));

        // 12-hour format with AM/PM
        System.out.println("  12-hour: " + time.format(DateTimeFormatter.ofPattern("hh:mm a")));

        // Hour and minute only
        System.out.println("  Short:   " + time.format(DateTimeFormatter.ofPattern("HH:mm")));

        // Example 3: DateTime Formatting
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 3: Combined Date and Time");
        System.out.println("=".repeat(70));

        LocalDateTime dateTime = LocalDateTime.of(2025, 12, 25, 18, 30);

        System.out.println("DateTime object: " + dateTime);
        System.out.println("\\nFormatted outputs:");

        System.out.println("  Standard:   " + dateTime.format(
            DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")));

        System.out.println("  Readable:   " + dateTime.format(
            DateTimeFormatter.ofPattern("MMMM dd, yyyy 'at' hh:mm a")));

        System.out.println("  Compact:    " + dateTime.format(
            DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss")));

        // Example 4: Predefined Formatters
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 4: Predefined Formatters");
        System.out.println("=".repeat(70));

        LocalDateTime now = LocalDateTime.now();

        System.out.println("Using built-in formatters:\\n");
        System.out.println("  ISO_LOCAL_DATE:      " + now.format(DateTimeFormatter.ISO_LOCAL_DATE));
        System.out.println("  ISO_LOCAL_TIME:      " + now.format(DateTimeFormatter.ISO_LOCAL_TIME));
        System.out.println("  ISO_LOCAL_DATE_TIME: " + now.format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));

        // Example 5: Custom Patterns
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 5: Custom Pattern Examples");
        System.out.println("=".repeat(70));

        LocalDateTime custom = LocalDateTime.of(2025, 7, 4, 16, 45, 30);

        System.out.println("Original: " + custom);
        System.out.println("\\nCustom formats:");

        // Day name
        System.out.println("  Day name:        " + custom.format(
            DateTimeFormatter.ofPattern("EEEE, MMMM dd, yyyy")));

        // With timezone info
        System.out.println("  With timezone:   " + ZonedDateTime.now().format(
            DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss z")));

        // Ordinal day
        System.out.println("  Day of year:     " + custom.format(
            DateTimeFormatter.ofPattern("D")) + " of 365");

        // Week of year
        System.out.println("  Week of year:    Week " + custom.format(
            DateTimeFormatter.ofPattern("w")));

        // Example 6: Parsing Formatted Dates
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 6: Parsing Dates from Strings");
        System.out.println("=".repeat(70));

        String dateStr1 = "2025-12-31";
        String dateStr2 = "12/31/2025";
        String dateStr3 = "December 31, 2025";

        LocalDate parsed1 = LocalDate.parse(dateStr1);
        LocalDate parsed2 = LocalDate.parse(dateStr2,
            DateTimeFormatter.ofPattern("MM/dd/yyyy"));
        LocalDate parsed3 = LocalDate.parse(dateStr3,
            DateTimeFormatter.ofPattern("MMMM dd, yyyy"));

        System.out.println("Parsed dates:");
        System.out.println("  '" + dateStr1 + "' → " + parsed1);
        System.out.println("  '" + dateStr2 + "' → " + parsed2);
        System.out.println("  '" + dateStr3 + "' → " + parsed3);

        // Example 7: Locale-Specific Formatting
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 7: Different Locales");
        System.out.println("=".repeat(70));

        LocalDate localDate = LocalDate.of(2025, 3, 15);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("EEEE, MMMM dd, yyyy");

        System.out.println("Date: " + localDate);
        System.out.println("\\nIn different locales:");

        System.out.println("  US English:  " + localDate.format(
            formatter.withLocale(Locale.US)));
        System.out.println("  UK English:  " + localDate.format(
            formatter.withLocale(Locale.UK)));
        System.out.println("  French:      " + localDate.format(
            formatter.withLocale(Locale.FRANCE)));
        System.out.println("  German:      " + localDate.format(
            formatter.withLocale(Locale.GERMANY)));

        // Example 8: Common Business Formats
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 8: Business & Technical Formats");
        System.out.println("=".repeat(70));

        LocalDateTime timestamp = LocalDateTime.now();

        System.out.println("Timestamp formats:\\n");

        // Log format
        System.out.println("  Log file:        " + timestamp.format(
            DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss.SSS")));

        // Filename format
        System.out.println("  Filename:        report_" + timestamp.format(
            DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss")) + ".pdf");

        // Database format
        System.out.println("  Database:        " + timestamp.format(
            DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")));

        // HTTP header format
        System.out.println("  HTTP header:     " + ZonedDateTime.now().format(
            DateTimeFormatter.RFC_1123_DATE_TIME));

        // Example 9: Formatting Helper Methods
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 9: Reusable Formatting Methods");
        System.out.println("=".repeat(70));

        LocalDateTime exampleDate = LocalDateTime.of(2025, 6, 15, 14, 30);

        System.out.println("Using helper methods:");
        System.out.println("  User friendly:   " + formatUserFriendly(exampleDate));
        System.out.println("  Short date:      " + formatShortDate(exampleDate.toLocalDate()));
        System.out.println("  Time only:       " + formatTimeOnly(exampleDate.toLocalTime()));
        System.out.println("  Relative:        " + formatRelative(exampleDate));
    }

    /**
     * Format date in user-friendly way
     */
    static String formatUserFriendly(LocalDateTime dateTime) {
        return dateTime.format(DateTimeFormatter.ofPattern("MMMM dd, yyyy 'at' h:mm a"));
    }

    /**
     * Format short date
     */
    static String formatShortDate(LocalDate date) {
        return date.format(DateTimeFormatter.ofPattern("MM/dd/yy"));
    }

    /**
     * Format time only
     */
    static String formatTimeOnly(LocalTime time) {
        return time.format(DateTimeFormatter.ofPattern("h:mm a"));
    }

    /**
     * Format relative to today
     */
    static String formatRelative(LocalDateTime dateTime) {
        LocalDate today = LocalDate.now();
        LocalDate date = dateTime.toLocalDate();

        if (date.equals(today)) {
            return "Today at " + formatTimeOnly(dateTime.toLocalTime());
        } else if (date.equals(today.plusDays(1))) {
            return "Tomorrow at " + formatTimeOnly(dateTime.toLocalTime());
        } else if (date.equals(today.minusDays(1))) {
            return "Yesterday at " + formatTimeOnly(dateTime.toLocalTime());
        } else {
            return formatUserFriendly(dateTime);
        }
    }
}

/* Common Format Patterns:
 *
 * Date:
 *   yyyy-MM-dd          → 2025-03-15
 *   MM/dd/yyyy          → 03/15/2025
 *   dd/MM/yyyy          → 15/03/2025
 *   MMMM dd, yyyy       → March 15, 2025
 *   EEE, MMM dd, yyyy   → Sat, Mar 15, 2025
 *
 * Time:
 *   HH:mm:ss            → 14:30:45 (24-hour)
 *   hh:mm a             → 02:30 PM (12-hour)
 *   HH:mm               → 14:30
 *
 * Combined:
 *   yyyy-MM-dd HH:mm:ss        → 2025-03-15 14:30:45
 *   MM/dd/yyyy hh:mm a         → 03/15/2025 02:30 PM
 *   MMMM dd, yyyy 'at' h:mm a  → March 15, 2025 at 2:30 PM
 *
 * Pattern Letters:
 *   y = year, M = month, d = day
 *   H = hour (0-23), h = hour (1-12), m = minute, s = second
 *   a = AM/PM, E = day name, z = timezone
 */"""
    },

    32: {
        "title": "Check if Array is Sorted",
        "solution": """/**
 * Check if Array is Sorted
 *
 * Learn to verify if an array is sorted in ascending or descending order.
 * Essential for validating data and optimizing algorithms.
 *
 * Zero external dependencies - pure Java
 */

public class Main {
    public static void main(String[] args) {

        // Example 1: Check Ascending Sort
        System.out.println("=".repeat(70));
        System.out.println("Example 1: Check if Sorted Ascending");
        System.out.println("=".repeat(70));

        int[] sortedAsc = {1, 2, 3, 4, 5};
        boolean isSorted = isSortedAscending(sortedAsc);

        System.out.println("Array: " + java.util.Arrays.toString(sortedAsc));
        System.out.println("Is sorted ascending? " + isSorted);

        int[] unsorted = {1, 3, 2, 4, 5};
        isSorted = isSortedAscending(unsorted);

        System.out.println("\\nArray: " + java.util.Arrays.toString(unsorted));
        System.out.println("Is sorted ascending? " + isSorted);

        // Example 2: Check Descending Sort
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 2: Check if Sorted Descending");
        System.out.println("=".repeat(70));

        int[] sortedDesc = {10, 8, 6, 4, 2};
        boolean isDescending = isSortedDescending(sortedDesc);

        System.out.println("Array: " + java.util.Arrays.toString(sortedDesc));
        System.out.println("Is sorted descending? " + isDescending);

        // Example 3: Detect Sort Direction
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 3: Detect Sort Direction");
        System.out.println("=".repeat(70));

        int[][] testArrays = {
            {1, 2, 3, 4, 5},
            {5, 4, 3, 2, 1},
            {1, 3, 2, 5, 4},
            {10, 10, 10}
        };

        for (int[] arr : testArrays) {
            System.out.println("\\nArray: " + java.util.Arrays.toString(arr));
            detectSortOrder(arr);
        }

        // Example 4: Check with Duplicates
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 4: Sorted Arrays with Duplicates");
        System.out.println("=".repeat(70));

        int[] withDups = {1, 2, 2, 3, 3, 3, 4, 5};
        boolean sorted = isSortedAscending(withDups);

        System.out.println("Array with duplicates: " + java.util.Arrays.toString(withDups));
        System.out.println("Is sorted ascending? " + sorted);
        System.out.println("(Duplicates are allowed in sorted arrays)");

        // Example 5: Find Unsorted Position
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 5: Find Where Sorting Breaks");
        System.out.println("=".repeat(70));

        int[] broken = {1, 2, 5, 4, 6, 7};
        int breakPoint = findUnsortedIndex(broken);

        System.out.println("Array: " + java.util.Arrays.toString(broken));
        if (breakPoint != -1) {
            System.out.println("Sorting breaks at index " + breakPoint);
            System.out.println("  Value " + broken[breakPoint] +
                             " is less than previous " + broken[breakPoint-1]);
        } else {
            System.out.println("Array is fully sorted");
        }

        // Example 6: Strictly Increasing Check
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 6: Strictly Increasing (No Duplicates)");
        System.out.println("=".repeat(70));

        int[] strict = {1, 2, 3, 4, 5};
        int[] notStrict = {1, 2, 2, 3, 4};

        System.out.println("Array 1: " + java.util.Arrays.toString(strict));
        System.out.println("  Strictly increasing? " + isStrictlyIncreasing(strict));

        System.out.println("\\nArray 2: " + java.util.Arrays.toString(notStrict));
        System.out.println("  Strictly increasing? " + isStrictlyIncreasing(notStrict));

        // Example 7: Performance Benefits
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 7: Why Checking Sort Matters");
        System.out.println("=".repeat(70));

        int[] numbers = {1, 3, 5, 7, 9, 11, 13, 15};

        System.out.println("Array: " + java.util.Arrays.toString(numbers));
        System.out.println("Is sorted? " + isSortedAscending(numbers));
        System.out.println("\\nBenefit: Can use binary search (O(log n)) instead of");
        System.out.println("         linear search (O(n))!");

        // Example 8: Validation Use Case
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 8: Real-World Use Cases");
        System.out.println("=".repeat(70));

        // Student IDs (must be sorted for efficient lookup)
        int[] studentIDs = {101, 105, 108, 112, 115};

        System.out.println("Student IDs: " + java.util.Arrays.toString(studentIDs));
        if (isSortedAscending(studentIDs)) {
            System.out.println("✓ Valid: IDs are properly sorted for binary search");
        } else {
            System.out.println("✗ Error: IDs must be sorted!");
        }

        // Scores (might need to be descending)
        int[] scores = {95, 92, 88, 85, 76};

        System.out.println("\\nLeaderboard scores: " + java.util.Arrays.toString(scores));
        if (isSortedDescending(scores)) {
            System.out.println("✓ Valid: Scores sorted highest to lowest");
        } else {
            System.out.println("✗ Error: Leaderboard must show highest first!");
        }
    }

    /**
     * Check if array is sorted in ascending order
     */
    static boolean isSortedAscending(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[i-1]) {
                return false; // Found element smaller than previous
            }
        }
        return true;
    }

    /**
     * Check if array is sorted in descending order
     */
    static boolean isSortedDescending(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > arr[i-1]) {
                return false; // Found element larger than previous
            }
        }
        return true;
    }

    /**
     * Detect sort order of array
     */
    static void detectSortOrder(int[] arr) {
        if (arr.length <= 1) {
            System.out.println("  Status: Too small to determine");
            return;
        }

        boolean ascending = isSortedAscending(arr);
        boolean descending = isSortedDescending(arr);

        if (ascending && descending) {
            System.out.println("  Status: All elements are equal");
        } else if (ascending) {
            System.out.println("  Status: Sorted ASCENDING ↑");
        } else if (descending) {
            System.out.println("  Status: Sorted DESCENDING ↓");
        } else {
            System.out.println("  Status: UNSORTED");
        }
    }

    /**
     * Find index where sorting breaks
     */
    static int findUnsortedIndex(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[i-1]) {
                return i;
            }
        }
        return -1; // Fully sorted
    }

    /**
     * Check if strictly increasing (no duplicates)
     */
    static boolean isStrictlyIncreasing(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] <= arr[i-1]) { // Note: <= instead of <
                return false;
            }
        }
        return true;
    }
}

/* Key Concepts:
 * - Compare adjacent elements: arr[i] vs arr[i-1]
 * - Early termination on first violation
 * - Different criteria: <=, <, >=, >
 *
 * Use Cases:
 * - Validate sorted input before binary search
 * - Check data integrity
 * - Algorithm preconditions
 * - Leaderboard/ranking validation
 *
 * Time Complexity: O(n) - must check all adjacent pairs
 * Space Complexity: O(1) - only uses loop variable
 */"""
    }
}

def upgrade_final():
    """Upgrade final batch of critical Java lessons."""
    print("="*80)
    print("UPGRADING JAVA CRITICAL LESSONS - FINAL BATCH")
    print("="*80)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    for lesson_id, upgrade_data in UPGRADES.items():
        lesson = next((l for l in lessons if l['id'] == lesson_id), None)

        if lesson:
            old_length = len(lesson.get('fullSolution', ''))
            lesson['fullSolution'] = upgrade_data['solution']
            new_length = len(lesson['fullSolution'])

            print(f"\nLesson {lesson_id}: {lesson['title']}")
            print(f"  {old_length:,} -> {new_length:,} characters "
                  f"(+{new_length - old_length:,}, +{((new_length - old_length)/old_length*100):.1f}%)")

    with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)

    print("\n" + "="*80)
    print(f"BATCH COMPLETE! ({len(UPGRADES)} lessons)")
    print("="*80)
    print("\nProgress: 8 of 11 critical Java lessons complete")

if __name__ == '__main__':
    upgrade_final()
