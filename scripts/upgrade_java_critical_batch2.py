#!/usr/bin/env python3
"""
Upgrade remaining 8 CRITICAL Java lessons
IDs: 46, 30, 47, 41, 32, 203, 210, 39
"""

import json

UPGRADES = {
    46: {
        "title": "Loop Practice - Count Even Numbers",
        "solution": """/**
 * Loop Practice - Count Even Numbers
 *
 * Learn to count elements matching a condition using loops.
 * Essential pattern for filtering and analyzing data.
 *
 * Zero external dependencies - pure Java
 */

public class Main {
    public static void main(String[] args) {

        // Example 1: Count Even Numbers in Array
        System.out.println("=".repeat(70));
        System.out.println("Example 1: Basic Even Number Counting");
        System.out.println("=".repeat(70));

        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8};
        int evenCount = 0;

        System.out.println("\\nNumbers: " + java.util.Arrays.toString(numbers));
        System.out.print("Even numbers found: ");

        for (int num : numbers) {
            if (num % 2 == 0) {
                evenCount++;
                System.out.print(num + " ");
            }
        }

        System.out.println("\\nTotal even count: " + evenCount);
        System.out.println("Total odd count: " + (numbers.length - evenCount));

        // Example 2: Count with Details
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 2: Detailed Counting");
        System.out.println("=".repeat(70));

        int[] data = {10, 15, 22, 33, 44, 51, 68, 77, 82, 99};
        countWithDetails(data);

        // Example 3: Count Multiple Conditions
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 3: Count by Multiple Criteria");
        System.out.println("=".repeat(70));

        int[] values = {5, 12, 18, 25, 30, 42, 55, 60, 75, 88};
        categorizeNumbers(values);

        // Example 4: Count in Ranges
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 4: Count Numbers in Ranges");
        System.out.println("=".repeat(70));

        int[] scores = {45, 67, 89, 72, 95, 54, 88, 76, 92, 61};
        countByRange(scores);

        // Example 5: Count Consecutive Evens
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 5: Find Consecutive Even Numbers");
        System.out.println("=".repeat(70));

        int[] sequence = {1, 2, 4, 6, 3, 8, 10, 12, 5};
        findConsecutiveEvens(sequence);

        // Example 6: Count Patterns
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 6: Count Number Patterns");
        System.out.println("=".repeat(70));

        int[] pattern = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
        analyzePattern(pattern);

        // Example 7: Count with Percentage
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 7: Percentage Analysis");
        System.out.println("=".repeat(70));

        int[] survey = {2, 7, 4, 9, 6, 11, 8, 13, 10, 15};
        percentageAnalysis(survey);

        // Example 8: Count by Divisibility
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 8: Count by Divisibility Rules");
        System.out.println("=".repeat(70));

        int[] nums = {6, 12, 15, 18, 20, 25, 30, 35, 40, 45};
        countByDivisibility(nums);
    }

    static void countWithDetails(int[] arr) {
        int evenCount = 0, oddCount = 0;
        int evenSum = 0, oddSum = 0;

        System.out.println("Analyzing: " + java.util.Arrays.toString(arr));

        for (int num : arr) {
            if (num % 2 == 0) {
                evenCount++;
                evenSum += num;
            } else {
                oddCount++;
                oddSum += num;
            }
        }

        System.out.println("\\nEven Numbers:");
        System.out.println("  Count: " + evenCount);
        System.out.println("  Sum: " + evenSum);
        System.out.println("  Average: " + (evenCount > 0 ? (double)evenSum/evenCount : 0));

        System.out.println("\\nOdd Numbers:");
        System.out.println("  Count: " + oddCount);
        System.out.println("  Sum: " + oddSum);
        System.out.println("  Average: " + (oddCount > 0 ? (double)oddSum/oddCount : 0));
    }

    static void categorizeNumbers(int[] arr) {
        int evenCount = 0, oddCount = 0;
        int divisibleBy5 = 0, divisibleBy10 = 0;

        System.out.println("Numbers: " + java.util.Arrays.toString(arr));

        for (int num : arr) {
            if (num % 2 == 0) evenCount++;
            else oddCount++;

            if (num % 5 == 0) divisibleBy5++;
            if (num % 10 == 0) divisibleBy10++;
        }

        System.out.println("\\nCategories:");
        System.out.println("  Even: " + evenCount);
        System.out.println("  Odd: " + oddCount);
        System.out.println("  Divisible by 5: " + divisibleBy5);
        System.out.println("  Divisible by 10: " + divisibleBy10);
    }

    static void countByRange(int[] scores) {
        int below60 = 0, between60_80 = 0, above80 = 0;

        System.out.println("Scores: " + java.util.Arrays.toString(scores));

        for (int score : scores) {
            if (score < 60) below60++;
            else if (score <= 80) between60_80++;
            else above80++;
        }

        System.out.println("\\nGrade Distribution:");
        System.out.println("  Below 60 (F): " + below60);
        System.out.println("  60-80 (C-B): " + between60_80);
        System.out.println("  Above 80 (A): " + above80);
    }

    static void findConsecutiveEvens(int[] arr) {
        System.out.println("Sequence: " + java.util.Arrays.toString(arr));

        int maxConsecutive = 0;
        int currentConsecutive = 0;

        for (int num : arr) {
            if (num % 2 == 0) {
                currentConsecutive++;
                maxConsecutive = Math.max(maxConsecutive, currentConsecutive);
            } else {
                currentConsecutive = 0;
            }
        }

        System.out.println("\\nMax consecutive even numbers: " + maxConsecutive);
    }

    static void analyzePattern(int[] arr) {
        System.out.println("Pattern: " + java.util.Arrays.toString(arr));

        int allEven = 1;
        int allDivisibleBy2 = 1;

        for (int num : arr) {
            if (num % 2 != 0) allEven = 0;
        }

        System.out.println("\\nPattern Analysis:");
        System.out.println("  All even? " + (allEven == 1));
        System.out.println("  Count: " + arr.length);
        System.out.println("  First: " + arr[0]);
        System.out.println("  Last: " + arr[arr.length-1]);
    }

    static void percentageAnalysis(int[] arr) {
        int total = arr.length;
        int evenCount = 0;

        for (int num : arr) {
            if (num % 2 == 0) evenCount++;
        }

        double evenPercent = (evenCount * 100.0) / total;
        double oddPercent = 100.0 - evenPercent;

        System.out.println("Total numbers: " + total);
        System.out.println("\\nBreakdown:");
        System.out.printf("  Even: %d (%.1f%%)%n", evenCount, evenPercent);
        System.out.printf("  Odd: %d (%.1f%%)%n", (total - evenCount), oddPercent);
    }

    static void countByDivisibility(int[] arr) {
        int div2 = 0, div3 = 0, div5 = 0, div6 = 0;

        System.out.println("Numbers: " + java.util.Arrays.toString(arr));

        for (int num : arr) {
            if (num % 2 == 0) div2++;
            if (num % 3 == 0) div3++;
            if (num % 5 == 0) div5++;
            if (num % 6 == 0) div6++;
        }

        System.out.println("\\nDivisibility Count:");
        System.out.println("  ÷ 2: " + div2);
        System.out.println("  ÷ 3: " + div3);
        System.out.println("  ÷ 5: " + div5);
        System.out.println("  ÷ 6: " + div6);
    }
}

/* Key Concepts:
 * - Counter pattern: count++
 * - Conditional counting: if (condition) count++
 * - Multiple counters for different categories
 * - Percentage calculations
 * - Pattern detection
 */"""
    },

    30: {
        "title": "Calculating Date Differences",
        "solution": """/**
 * Calculating Date Differences
 *
 * Learn to calculate differences between dates using Java's time API.
 * Essential for scheduling, aging calculations, and time-based features.
 *
 * Zero external dependencies - uses java.time (Java 8+)
 */

import java.time.*;
import java.time.temporal.*;

public class Main {
    public static void main(String[] args) {

        // Example 1: Basic Date Difference
        System.out.println("=".repeat(70));
        System.out.println("Example 1: Days Between Dates");
        System.out.println("=".repeat(70));

        LocalDate date1 = LocalDate.of(2024, 1, 1);
        LocalDate date2 = LocalDate.of(2024, 12, 31);

        long daysBetween = ChronoUnit.DAYS.between(date1, date2);

        System.out.println("Start date: " + date1);
        System.out.println("End date: " + date2);
        System.out.println("Days between: " + daysBetween);

        // Example 2: Different Time Units
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 2: Multiple Time Units");
        System.out.println("=".repeat(70));

        LocalDate start = LocalDate.of(2024, 1, 1);
        LocalDate end = LocalDate.of(2025, 6, 15);

        long days = ChronoUnit.DAYS.between(start, end);
        long weeks = ChronoUnit.WEEKS.between(start, end);
        long months = ChronoUnit.MONTHS.between(start, end);
        long years = ChronoUnit.YEARS.between(start, end);

        System.out.println("From: " + start);
        System.out.println("To: " + end);
        System.out.println("\\nDifference:");
        System.out.println("  Days: " + days);
        System.out.println("  Weeks: " + weeks);
        System.out.println("  Months: " + months);
        System.out.println("  Years: " + years);

        // Example 3: Age Calculator
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 3: Calculate Age");
        System.out.println("=".repeat(70));

        LocalDate birthDate = LocalDate.of(1990, 5, 15);
        LocalDate today = LocalDate.now();

        Period age = Period.between(birthDate, today);

        System.out.println("Birth date: " + birthDate);
        System.out.println("Today: " + today);
        System.out.println("\\nAge: " + age.getYears() + " years, " +
                         age.getMonths() + " months, " +
                         age.getDays() + " days");

        // Example 4: Time Until Event
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 4: Days Until Future Event");
        System.out.println("=".repeat(70));

        LocalDate christmas = LocalDate.of(2025, 12, 25);
        LocalDate now = LocalDate.of(2025, 1, 1);

        long daysUntil = ChronoUnit.DAYS.between(now, christmas);

        System.out.println("Today: " + now);
        System.out.println("Christmas: " + christmas);
        System.out.println("Days until Christmas: " + daysUntil);

        // Example 5: Business Days Calculator
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 5: Business Days (excluding weekends)");
        System.out.println("=".repeat(70));

        LocalDate projectStart = LocalDate.of(2025, 1, 6); // Monday
        LocalDate projectEnd = LocalDate.of(2025, 1, 17);   // Friday

        int businessDays = calculateBusinessDays(projectStart, projectEnd);

        System.out.println("Project start: " + projectStart + " (" + projectStart.getDayOfWeek() + ")");
        System.out.println("Project end: " + projectEnd + " (" + projectEnd.getDayOfWeek() + ")");
        System.out.println("Business days: " + businessDays);

        // Example 6: DateTime Differences
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 6: Time Differences (Hours, Minutes)");
        System.out.println("=".repeat(70));

        LocalDateTime start1 = LocalDateTime.of(2025, 1, 1, 9, 0);
        LocalDateTime end1 = LocalDateTime.of(2025, 1, 1, 17, 30);

        long hours = ChronoUnit.HOURS.between(start1, end1);
        long minutes = ChronoUnit.MINUTES.between(start1, end1);

        System.out.println("Start: " + start1);
        System.out.println("End: " + end1);
        System.out.println("Hours: " + hours);
        System.out.println("Minutes: " + minutes);
        System.out.println("Formatted: " + hours + "h " + (minutes % 60) + "m");

        // Example 7: Compare Dates
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 7: Date Comparisons");
        System.out.println("=".repeat(70));

        LocalDate deadline = LocalDate.of(2025, 3, 31);
        LocalDate currentDate = LocalDate.of(2025, 3, 25);

        System.out.println("Deadline: " + deadline);
        System.out.println("Current date: " + currentDate);

        if (currentDate.isBefore(deadline)) {
            long daysLeft = ChronoUnit.DAYS.between(currentDate, deadline);
            System.out.println("Status: On time! " + daysLeft + " days remaining");
        } else if (currentDate.isAfter(deadline)) {
            long daysLate = ChronoUnit.DAYS.between(deadline, currentDate);
            System.out.println("Status: Overdue by " + daysLate + " days");
        } else {
            System.out.println("Status: Due today!");
        }

        // Example 8: Subscription/Membership Duration
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 8: Subscription Duration");
        System.out.println("=".repeat(70));

        LocalDate subscriptionStart = LocalDate.of(2024, 6, 1);
        LocalDate subscriptionEnd = LocalDate.of(2025, 6, 1);
        LocalDate checkDate = LocalDate.of(2025, 1, 15);

        calculateSubscriptionStatus(subscriptionStart, subscriptionEnd, checkDate);

        // Example 9: Rental Duration Calculator
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 9: Rental Duration & Cost");
        System.out.println("=".repeat(70));

        LocalDate rentalStart = LocalDate.of(2025, 1, 10);
        LocalDate rentalEnd = LocalDate.of(2025, 1, 15);
        double dailyRate = 75.00;

        calculateRentalCost(rentalStart, rentalEnd, dailyRate);
    }

    /**
     * Calculate business days (Monday-Friday only)
     */
    static int calculateBusinessDays(LocalDate start, LocalDate end) {
        int businessDays = 0;
        LocalDate current = start;

        while (!current.isAfter(end)) {
            DayOfWeek day = current.getDayOfWeek();
            if (day != DayOfWeek.SATURDAY && day != DayOfWeek.SUNDAY) {
                businessDays++;
            }
            current = current.plusDays(1);
        }

        return businessDays;
    }

    /**
     * Calculate subscription status
     */
    static void calculateSubscriptionStatus(LocalDate start, LocalDate end, LocalDate checkDate) {
        long totalDays = ChronoUnit.DAYS.between(start, end);
        long daysUsed = ChronoUnit.DAYS.between(start, checkDate);
        long daysRemaining = ChronoUnit.DAYS.between(checkDate, end);

        System.out.println("Subscription started: " + start);
        System.out.println("Subscription ends: " + end);
        System.out.println("Checking on: " + checkDate);
        System.out.println("\\nStatus:");
        System.out.println("  Total duration: " + totalDays + " days");
        System.out.println("  Days used: " + daysUsed);
        System.out.println("  Days remaining: " + daysRemaining);

        double percentUsed = (daysUsed * 100.0) / totalDays;
        System.out.printf("  Usage: %.1f%%%n", percentUsed);

        if (daysRemaining < 30) {
            System.out.println("  ⚠️ Renewal reminder: Less than 30 days left!");
        }
    }

    /**
     * Calculate rental cost based on duration
     */
    static void calculateRentalCost(LocalDate start, LocalDate end, double dailyRate) {
        long days = ChronoUnit.DAYS.between(start, end) + 1; // Include both days
        double totalCost = days * dailyRate;

        System.out.println("Rental period: " + start + " to " + end);
        System.out.println("Duration: " + days + " days");
        System.out.println("Daily rate: $" + String.format("%.2f", dailyRate));
        System.out.println("Total cost: $" + String.format("%.2f", totalCost));

        // Discount for longer rentals
        if (days >= 7) {
            double discount = totalCost * 0.1;
            double discountedPrice = totalCost - discount;
            System.out.println("\\n7+ day discount (10%): $" + String.format("%.2f", discount));
            System.out.println("Final price: $" + String.format("%.2f", discountedPrice));
        }
    }
}

/* Key Concepts:
 * - LocalDate for dates without time
 * - LocalDateTime for dates with time
 * - ChronoUnit for calculating differences
 * - Period for year/month/day differences
 * - isBefore(), isAfter(), isEqual() for comparisons
 *
 * Common Use Cases:
 * - Age calculators
 * - Subscription/membership duration
 * - Project timelines
 * - Rental/booking systems
 * - Deadline tracking
 */"""
    }
}

def upgrade_batch2():
    """Upgrade batch 2 of critical Java lessons."""
    print("="*80)
    print("UPGRADING JAVA CRITICAL LESSONS - BATCH 2")
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
    print(f"BATCH 2 COMPLETE! ({len(UPGRADES)} lessons)")
    print("="*80)
    print("\nProgress: 5 of 11 critical Java lessons complete")

if __name__ == '__main__':
    upgrade_batch2()
