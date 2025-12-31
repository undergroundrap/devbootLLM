#!/usr/bin/env python3
"""
Upgrade FINAL 3 CRITICAL Java lessons
IDs: 203 (Email Validation), 210 (Phone Number Validation), 39 (Switch Statement)
"""

import json

UPGRADES = {
    203: {
        "title": "Email Validation",
        "solution": """/**
 * Email Validation - Comprehensive Guide
 *
 * Learn to validate email addresses using pattern matching.
 * Essential for user registration, forms, and data validation.
 *
 * Zero external dependencies - pure Java
 */

public class Main {
    public static void main(String[] args) {

        // Example 1: Basic Email Validation
        System.out.println("=".repeat(70));
        System.out.println("Example 1: Basic Email Validation");
        System.out.println("=".repeat(70));

        String[] emails = {
            "user@example.com",
            "invalid.email",
            "test@test",
            "user@domain.co.uk",
            "user.name@example.com"
        };

        System.out.println("Validating email addresses:\\n");
        for (String email : emails) {
            boolean valid = isValidEmail(email);
            String status = valid ? "✓ Valid" : "✗ Invalid";
            System.out.printf("  %-30s %s%n", email, status);
        }

        // Example 2: Detailed Validation with Reasons
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 2: Validation with Error Messages");
        System.out.println("=".repeat(70));

        String[] testEmails = {
            "valid@email.com",
            "no-at-sign.com",
            "@nodomain.com",
            "user@",
            "user name@example.com",
            "user@@example.com"
        };

        System.out.println("\\nDetailed validation:\\n");
        for (String email : testEmails) {
            EmailValidationResult result = validateEmailDetailed(email);
            System.out.println("Email: " + email);
            System.out.println("  Valid: " + result.isValid);
            if (!result.isValid) {
                System.out.println("  Reason: " + result.errorMessage);
            }
            System.out.println();
        }

        // Example 3: Extract Email Components
        System.out.println("=".repeat(70));
        System.out.println("Example 3: Extract Email Parts");
        System.out.println("=".repeat(70));

        String email = "john.doe@company.com";
        EmailParts parts = extractEmailParts(email);

        System.out.println("\\nEmail: " + email);
        System.out.println("  Username: " + parts.username);
        System.out.println("  Domain: " + parts.domain);

        // Example 4: Business Rules Validation
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 4: Business-Specific Validation");
        System.out.println("=".repeat(70));

        String[] workEmails = {
            "employee@company.com",
            "contractor@company.com",
            "external@gmail.com",
            "user@competitor.com"
        };

        System.out.println("\\nChecking corporate email policy:\\n");
        for (String e : workEmails) {
            boolean isCorp = isCorporateEmail(e, "company.com");
            String status = isCorp ? "✓ Allowed" : "✗ Blocked";
            System.out.printf("  %-30s %s%n", e, status);
        }

        // Example 5: Batch Email Validation
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 5: Batch Validation");
        System.out.println("=".repeat(70));

        String[] batch = {
            "alice@example.com",
            "bob@test.org",
            "invalid@",
            "charlie@domain.co",
            "not-an-email"
        };

        ValidationStats stats = validateBatch(batch);

        System.out.println("\\nBatch Results:");
        System.out.println("  Total: " + stats.total);
        System.out.println("  Valid: " + stats.valid);
        System.out.println("  Invalid: " + stats.invalid);
        System.out.println("  Success rate: " + String.format("%.1f%%",
            (stats.valid * 100.0 / stats.total)));

        // Example 6: Common Email Patterns
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 6: Check Common Patterns");
        System.out.println("=".repeat(70));

        String[] commonPatterns = {
            "support@company.com",
            "info@company.com",
            "noreply@company.com",
            "admin@company.com"
        };

        System.out.println("\\nCommon service emails:");
        for (String e : commonPatterns) {
            System.out.println("  " + e + " - " + detectEmailType(e));
        }

        // Example 7: Normalize Email
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 7: Email Normalization");
        System.out.println("=".repeat(70));

        String[] toNormalize = {
            "  USER@EXAMPLE.COM  ",
            "User@Example.Com",
            "user@EXAMPLE.com"
        };

        System.out.println("\\nNormalizing emails:");
        for (String e : toNormalize) {
            String normalized = normalizeEmail(e);
            System.out.printf("  '%s' → '%s'%n", e, normalized);
        }
    }

    /**
     * Basic email validation
     */
    static boolean isValidEmail(String email) {
        if (email == null || email.trim().isEmpty()) {
            return false;
        }

        // Must contain exactly one @
        int atCount = 0;
        int atPos = -1;
        for (int i = 0; i < email.length(); i++) {
            if (email.charAt(i) == '@') {
                atCount++;
                atPos = i;
            }
        }

        if (atCount != 1) return false;

        // Must have content before and after @
        if (atPos == 0 || atPos == email.length() - 1) {
            return false;
        }

        // Domain must have at least one dot after @
        String domain = email.substring(atPos + 1);
        if (!domain.contains(".")) {
            return false;
        }

        // No spaces allowed
        if (email.contains(" ")) {
            return false;
        }

        return true;
    }

    /**
     * Validation result with error message
     */
    static class EmailValidationResult {
        boolean isValid;
        String errorMessage;

        EmailValidationResult(boolean valid, String error) {
            this.isValid = valid;
            this.errorMessage = error;
        }
    }

    /**
     * Detailed email validation
     */
    static EmailValidationResult validateEmailDetailed(String email) {
        if (email == null || email.trim().isEmpty()) {
            return new EmailValidationResult(false, "Email is empty");
        }

        if (email.contains(" ")) {
            return new EmailValidationResult(false, "Email contains spaces");
        }

        int atCount = 0;
        int atPos = -1;
        for (int i = 0; i < email.length(); i++) {
            if (email.charAt(i) == '@') {
                atCount++;
                atPos = i;
            }
        }

        if (atCount == 0) {
            return new EmailValidationResult(false, "Missing @ symbol");
        }

        if (atCount > 1) {
            return new EmailValidationResult(false, "Multiple @ symbols");
        }

        if (atPos == 0) {
            return new EmailValidationResult(false, "Missing username");
        }

        if (atPos == email.length() - 1) {
            return new EmailValidationResult(false, "Missing domain");
        }

        String domain = email.substring(atPos + 1);
        if (!domain.contains(".")) {
            return new EmailValidationResult(false, "Domain missing extension");
        }

        return new EmailValidationResult(true, null);
    }

    /**
     * Email parts container
     */
    static class EmailParts {
        String username;
        String domain;

        EmailParts(String user, String dom) {
            this.username = user;
            this.domain = dom;
        }
    }

    /**
     * Extract email components
     */
    static EmailParts extractEmailParts(String email) {
        int atPos = email.indexOf('@');
        if (atPos == -1) {
            return new EmailParts(email, "");
        }

        String username = email.substring(0, atPos);
        String domain = email.substring(atPos + 1);

        return new EmailParts(username, domain);
    }

    /**
     * Check if email is from corporate domain
     */
    static boolean isCorporateEmail(String email, String corporateDomain) {
        if (!isValidEmail(email)) return false;

        EmailParts parts = extractEmailParts(email);
        return parts.domain.equals(corporateDomain);
    }

    /**
     * Validation statistics
     */
    static class ValidationStats {
        int total;
        int valid;
        int invalid;
    }

    /**
     * Validate batch of emails
     */
    static ValidationStats validateBatch(String[] emails) {
        ValidationStats stats = new ValidationStats();
        stats.total = emails.length;

        for (String email : emails) {
            if (isValidEmail(email)) {
                stats.valid++;
            } else {
                stats.invalid++;
            }
        }

        return stats;
    }

    /**
     * Detect type of email
     */
    static String detectEmailType(String email) {
        EmailParts parts = extractEmailParts(email);
        String username = parts.username.toLowerCase();

        if (username.equals("support")) return "Support Email";
        if (username.equals("info")) return "Information Email";
        if (username.equals("noreply")) return "No-Reply Email";
        if (username.equals("admin")) return "Admin Email";

        return "Regular Email";
    }

    /**
     * Normalize email (lowercase, trim)
     */
    static String normalizeEmail(String email) {
        return email.trim().toLowerCase();
    }
}

/* Common Email Validation Rules:
 *
 * Required:
 * ✓ Must contain exactly one @
 * ✓ Must have username before @
 * ✓ Must have domain after @
 * ✓ Domain must contain at least one dot
 * ✓ No whitespace allowed
 *
 * Optional Business Rules:
 * - Minimum/maximum length
 * - Allowed/blocked domains
 * - Required domain patterns
 * - Username restrictions
 *
 * Real-World Considerations:
 * - Always validate on both client and server
 * - Send verification email to confirm
 * - Consider internationalized emails
 * - Allow + and . in usernames
 */"""
    },

    210: {
        "title": "Phone Number Validation",
        "solution": """/**
 * Phone Number Validation - Comprehensive Guide
 *
 * Learn to validate and format phone numbers in various formats.
 * Essential for contact forms, user profiles, and communication features.
 *
 * Zero external dependencies - pure Java
 */

public class Main {
    public static void main(String[] args) {

        // Example 1: Basic US Phone Validation
        System.out.println("=".repeat(70));
        System.out.println("Example 1: Validate US Phone Numbers");
        System.out.println("=".repeat(70));

        String[] phones = {
            "555-123-4567",
            "(555) 123-4567",
            "5551234567",
            "555.123.4567",
            "123-456",  // Too short
            "555-12-34567"  // Wrong format
        };

        System.out.println("Validating US phone numbers:\\n");
        for (String phone : phones) {
            boolean valid = isValidUSPhone(phone);
            String status = valid ? "✓ Valid" : "✗ Invalid";
            System.out.printf("  %-20s %s%n", phone, status);
        }

        // Example 2: Extract Digits Only
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 2: Extract Digits from Phone Numbers");
        System.out.println("=".repeat(70));

        String[] formatted = {
            "(555) 123-4567",
            "555-123-4567",
            "555.123.4567",
            "+1 (555) 123-4567"
        };

        System.out.println("\\nExtracting digits:");
        for (String phone : formatted) {
            String digits = extractDigits(phone);
            System.out.printf("  %-22s → %s%n", phone, digits);
        }

        // Example 3: Format Phone Numbers
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 3: Format Phone Numbers");
        System.out.println("=".repeat(70));

        String[] raw = {
            "5551234567",
            "15551234567",  // With country code
            "5559876543"
        };

        System.out.println("\\nFormatting phone numbers:");
        for (String phone : raw) {
            String formatted1 = formatUSPhone(phone);
            System.out.printf("  %s → %s%n", phone, formatted1);
        }

        // Example 4: Phone Number Components
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 4: Extract Phone Components");
        System.out.println("=".repeat(70));

        String phone = "555-123-4567";
        PhoneParts parts = parseUSPhone(phone);

        System.out.println("\\nPhone: " + phone);
        System.out.println("  Area code: " + parts.areaCode);
        System.out.println("  Prefix: " + parts.prefix);
        System.out.println("  Line number: " + parts.lineNumber);

        // Example 5: Different Phone Formats
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 5: Support Multiple Formats");
        System.out.println("=".repeat(70));

        String[] multiFormat = {
            "555-123-4567",      // Dashes
            "(555) 123-4567",    // Parentheses
            "555.123.4567",      // Dots
            "5551234567",        // No formatting
            "+1-555-123-4567",   // With country code
            "1 (555) 123-4567"   // Country code + parens
        };

        System.out.println("\\nNormalizing to standard format:");
        for (String p : multiFormat) {
            String normalized = normalizePhone(p);
            System.out.printf("  %-22s → %s%n", p, normalized);
        }

        // Example 6: Validation with Error Messages
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 6: Detailed Validation");
        System.out.println("=".repeat(70));

        String[] testPhones = {
            "555-123-4567",
            "123-456",
            "(555) 12-4567",
            "abcd-efg-hijk"
        };

        System.out.println("\\nDetailed validation:\\n");
        for (String p : testPhones) {
            PhoneValidationResult result = validatePhoneDetailed(p);
            System.out.println("Phone: " + p);
            System.out.println("  Valid: " + result.isValid);
            if (!result.isValid) {
                System.out.println("  Error: " + result.errorMessage);
            }
            System.out.println();
        }

        // Example 7: International Phone Numbers
        System.out.println("=".repeat(70));
        System.out.println("Example 7: International Format");
        System.out.println("=".repeat(70));

        String[] international = {
            "+1-555-123-4567",     // US
            "+44-20-1234-5678",    // UK
            "+81-3-1234-5678",     // Japan
            "+33-1-23-45-67-89"    // France
        };

        System.out.println("\\nInternational phone numbers:");
        for (String p : international) {
            String country = detectCountryCode(p);
            System.out.printf("  %-25s Country code: %s%n", p, country);
        }

        // Example 8: Phone Type Detection
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 8: Detect Phone Type");
        System.out.println("=".repeat(70));

        String[] typeTest = {
            "800-555-1234",  // Toll-free
            "900-555-1234",  // Premium
            "555-555-1234"   // Regular
        };

        System.out.println("\\nDetecting phone type:");
        for (String p : typeTest) {
            String type = detectPhoneType(p);
            System.out.printf("  %-20s → %s%n", p, type);
        }
    }

    /**
     * Validate US phone number (10 digits)
     */
    static boolean isValidUSPhone(String phone) {
        String digits = extractDigits(phone);
        return digits.length() == 10 || digits.length() == 11;
    }

    /**
     * Extract only digits from phone number
     */
    static String extractDigits(String phone) {
        StringBuilder digits = new StringBuilder();

        for (char c : phone.toCharArray()) {
            if (Character.isDigit(c)) {
                digits.append(c);
            }
        }

        return digits.toString();
    }

    /**
     * Format US phone number as (XXX) XXX-XXXX
     */
    static String formatUSPhone(String phone) {
        String digits = extractDigits(phone);

        // Remove country code if present
        if (digits.length() == 11 && digits.charAt(0) == '1') {
            digits = digits.substring(1);
        }

        if (digits.length() != 10) {
            return phone; // Return as-is if invalid
        }

        String areaCode = digits.substring(0, 3);
        String prefix = digits.substring(3, 6);
        String lineNum = digits.substring(6);

        return "(" + areaCode + ") " + prefix + "-" + lineNum;
    }

    /**
     * Phone number parts
     */
    static class PhoneParts {
        String areaCode;
        String prefix;
        String lineNumber;

        PhoneParts(String area, String pre, String line) {
            this.areaCode = area;
            this.prefix = pre;
            this.lineNumber = line;
        }
    }

    /**
     * Parse US phone into components
     */
    static PhoneParts parseUSPhone(String phone) {
        String digits = extractDigits(phone);

        if (digits.length() == 11 && digits.charAt(0) == '1') {
            digits = digits.substring(1);
        }

        if (digits.length() != 10) {
            return new PhoneParts("", "", "");
        }

        return new PhoneParts(
            digits.substring(0, 3),  // Area code
            digits.substring(3, 6),  // Prefix
            digits.substring(6)      // Line number
        );
    }

    /**
     * Normalize to standard format
     */
    static String normalizePhone(String phone) {
        return formatUSPhone(phone);
    }

    /**
     * Validation result
     */
    static class PhoneValidationResult {
        boolean isValid;
        String errorMessage;

        PhoneValidationResult(boolean valid, String error) {
            this.isValid = valid;
            this.errorMessage = error;
        }
    }

    /**
     * Detailed phone validation
     */
    static PhoneValidationResult validatePhoneDetailed(String phone) {
        String digits = extractDigits(phone);

        if (digits.isEmpty()) {
            return new PhoneValidationResult(false, "No digits found");
        }

        if (digits.length() < 10) {
            return new PhoneValidationResult(false,
                "Too few digits (expected 10 or 11)");
        }

        if (digits.length() > 11) {
            return new PhoneValidationResult(false,
                "Too many digits (expected 10 or 11)");
        }

        if (digits.length() == 11 && digits.charAt(0) != '1') {
            return new PhoneValidationResult(false,
                "11-digit number must start with 1");
        }

        return new PhoneValidationResult(true, null);
    }

    /**
     * Detect country code
     */
    static String detectCountryCode(String phone) {
        if (phone.startsWith("+")) {
            if (phone.startsWith("+1")) return "+1 (US/Canada)";
            if (phone.startsWith("+44")) return "+44 (UK)";
            if (phone.startsWith("+81")) return "+81 (Japan)";
            if (phone.startsWith("+33")) return "+33 (France)";
        }

        return "Unknown";
    }

    /**
     * Detect phone type by area code
     */
    static String detectPhoneType(String phone) {
        String digits = extractDigits(phone);

        if (digits.length() >= 3) {
            String areaCode = digits.substring(0, 3);

            if (areaCode.equals("800") || areaCode.equals("888") ||
                areaCode.equals("877") || areaCode.equals("866")) {
                return "Toll-Free";
            }

            if (areaCode.equals("900")) {
                return "Premium Rate";
            }
        }

        return "Regular";
    }
}

/* Phone Number Validation Best Practices:
 *
 * Basic Rules (US):
 * ✓ 10 digits for local (XXX-XXX-XXXX)
 * ✓ 11 digits with country code (1-XXX-XXX-XXXX)
 * ✓ Area code cannot be 0 or 1
 * ✓ Prefix cannot be 0 or 1
 *
 * Common Formats:
 * - (555) 123-4567
 * - 555-123-4567
 * - 555.123.4567
 * - 5551234567
 * - +1-555-123-4567
 *
 * Real-World Considerations:
 * - Always store normalized format
 * - Support international numbers if needed
 * - Validate but allow flexible input
 * - Send SMS verification to confirm
 */"""
    },

    39: {
        "title": "Switch Statement Deep Dive",
        "solution": """/**
 * Switch Statement Deep Dive - Comprehensive Guide
 *
 * Master switch statements for multi-way branching.
 * Essential control flow structure for readable conditional logic.
 *
 * Zero external dependencies - pure Java
 */

public class Main {
    public static void main(String[] args) {

        // Example 1: Basic Switch Statement
        System.out.println("=".repeat(70));
        System.out.println("Example 1: Basic Day of Week");
        System.out.println("=".repeat(70));

        int day = 3;

        System.out.println("\\nDay number: " + day);
        System.out.print("Day name: ");

        switch (day) {
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
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Invalid day");
        }

        // Example 2: Switch with Fall-Through
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 2: Fall-Through for Grouping");
        System.out.println("=".repeat(70));

        int month = 2;

        System.out.println("\\nMonth: " + month);
        System.out.print("Season: ");

        switch (month) {
            case 12:
            case 1:
            case 2:
                System.out.println("Winter");
                break;
            case 3:
            case 4:
            case 5:
                System.out.println("Spring");
                break;
            case 6:
            case 7:
            case 8:
                System.out.println("Summer");
                break;
            case 9:
            case 10:
            case 11:
                System.out.println("Fall");
                break;
            default:
                System.out.println("Invalid month");
        }

        // Example 3: Switch with Return Values
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 3: Switch in Methods");
        System.out.println("=".repeat(70));

        System.out.println("\\nGrade conversions:");
        for (char grade = 'A'; grade <= 'F'; grade++) {
            String description = getGradeDescription(grade);
            System.out.printf("  Grade %c: %s%n", grade, description);
        }

        // Example 4: Calculator with Switch
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 4: Simple Calculator");
        System.out.println("=".repeat(70));

        int a = 10, b = 5;
        char[] operations = {'+', '-', '*', '/', '%'};

        System.out.println("\\nCalculating " + a + " op " + b + ":");
        for (char op : operations) {
            double result = calculate(a, b, op);
            System.out.printf("  %d %c %d = %.2f%n", a, op, b, result);
        }

        // Example 5: Menu Selection
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 5: Menu System");
        System.out.println("=".repeat(70));

        int[] menuChoices = {1, 2, 3, 4, 5};

        System.out.println("\\nMenu selections:");
        for (int choice : menuChoices) {
            processMenuChoice(choice);
        }

        // Example 6: String Switch (Java 7+)
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 6: Switch on Strings");
        System.out.println("=".repeat(70));

        String[] commands = {"start", "stop", "pause", "resume", "unknown"};

        System.out.println("\\nProcessing commands:");
        for (String cmd : commands) {
            System.out.print("  Command '" + cmd + "': ");
            processCommand(cmd);
        }

        // Example 7: Switch vs If-Else Performance
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 7: When to Use Switch");
        System.out.println("=".repeat(70));

        System.out.println("\\nUse switch when:");
        System.out.println("  ✓ Comparing one variable to multiple constant values");
        System.out.println("  ✓ You have 3+ conditions to check");
        System.out.println("  ✓ Values are integers, chars, or strings (Java 7+)");
        System.out.println("\\nUse if-else when:");
        System.out.println("  ✓ Complex conditions (&&, ||)");
        System.out.println("  ✓ Range checks (x > 10 && x < 20)");
        System.out.println("  ✓ Different variables in each condition");

        // Example 8: Nested Switch
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 8: Nested Switch Statements");
        System.out.println("=".repeat(70));

        int category = 1;
        int subcategory = 2;

        System.out.println("\\nCategory: " + category + ", Subcategory: " + subcategory);
        System.out.print("Item type: ");

        switch (category) {
            case 1: // Electronics
                switch (subcategory) {
                    case 1:
                        System.out.println("Computer");
                        break;
                    case 2:
                        System.out.println("Phone");
                        break;
                    default:
                        System.out.println("Other Electronics");
                }
                break;
            case 2: // Clothing
                switch (subcategory) {
                    case 1:
                        System.out.println("Shirt");
                        break;
                    case 2:
                        System.out.println("Pants");
                        break;
                    default:
                        System.out.println("Other Clothing");
                }
                break;
            default:
                System.out.println("Unknown category");
        }

        // Example 9: Enhanced Switch (Java 14+) - Traditional Alternative
        System.out.println("\\n" + "=".repeat(70));
        System.out.println("Example 9: Multiple Cases, One Action");
        System.out.println("=".repeat(70));

        int dayOfWeek = 6;
        String dayType = getDayType(dayOfWeek);

        System.out.println("\\nDay " + dayOfWeek + " is a " + dayType);
    }

    /**
     * Get grade description
     */
    static String getGradeDescription(char grade) {
        switch (grade) {
            case 'A':
                return "Excellent";
            case 'B':
                return "Good";
            case 'C':
                return "Average";
            case 'D':
                return "Below Average";
            case 'F':
                return "Failing";
            default:
                return "Invalid grade";
        }
    }

    /**
     * Simple calculator
     */
    static double calculate(int a, int b, char operator) {
        switch (operator) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                return (double) a / b;
            case '%':
                return a % b;
            default:
                return 0;
        }
    }

    /**
     * Process menu choice
     */
    static void processMenuChoice(int choice) {
        System.out.print("  Option " + choice + ": ");

        switch (choice) {
            case 1:
                System.out.println("New File created");
                break;
            case 2:
                System.out.println("File opened");
                break;
            case 3:
                System.out.println("File saved");
                break;
            case 4:
                System.out.println("Settings displayed");
                break;
            case 5:
                System.out.println("Application exited");
                break;
            default:
                System.out.println("Invalid option");
        }
    }

    /**
     * Process string command
     */
    static void processCommand(String command) {
        switch (command) {
            case "start":
                System.out.println("Starting...");
                break;
            case "stop":
                System.out.println("Stopping...");
                break;
            case "pause":
                System.out.println("Paused");
                break;
            case "resume":
                System.out.println("Resuming...");
                break;
            default:
                System.out.println("Unknown command");
        }
    }

    /**
     * Determine if weekday or weekend
     */
    static String getDayType(int day) {
        switch (day) {
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                return "Weekday";
            case 6:
            case 7:
                return "Weekend";
            default:
                return "Invalid";
        }
    }
}

/* Switch Statement Best Practices:
 *
 * DO:
 * ✓ Always include 'break' to prevent fall-through (unless intentional)
 * ✓ Always include 'default' case
 * ✓ Keep case blocks simple
 * ✓ Group similar cases together
 * ✓ Use for equality checks on single variable
 *
 * DON'T:
 * ✗ Use for complex conditions (use if-else)
 * ✗ Use for range checks (use if-else)
 * ✗ Forget break statements
 * ✗ Make case blocks too long (extract to methods)
 *
 * Switch Works With:
 * - byte, short, int, char
 * - String (Java 7+)
 * - Enum types
 * - Wrapper classes (Integer, Character, etc.)
 *
 * Doesn't Work With:
 * - long, float, double
 * - boolean
 * - Custom objects
 */"""
    }
}

def upgrade_last3():
    """Upgrade last 3 critical Java lessons."""
    print("="*80)
    print("COMPLETING JAVA CRITICAL LESSONS - FINAL 3!")
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
    print("🎉 ALL 11 JAVA CRITICAL LESSONS COMPLETE! 🎉")
    print("="*80)
    print("\nEvery critical lesson now comprehensive with:")
    print("  • 7,000-10,000+ characters")
    print("  • Multiple examples (7-9 per lesson)")
    print("  • Real-world use cases")
    print("  • Best practices and key takeaways")
    print("  • Zero dependencies!")

if __name__ == '__main__':
    upgrade_last3()
