#!/usr/bin/env python3
"""
Improve lesson code examples with topic-specific, compilable implementations.
Replace generic placeholders with real, educational code.
"""

import json
import re


def create_java_code_for_topic(title, description):
    """Generate realistic, compilable Java code based on lesson topic."""

    title_lower = title.lower()

    # String lessons
    if 'string' in title_lower:
        if 'length' in title_lower or 'character access' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        // TODO: Create a string and get its length
        String message = "Hello, Java!";

        // TODO: Print the length
        // System.out.println("Length: " + message.length());

        // TODO: Access first character
        // System.out.println("First char: " + message.charAt(0));
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        // Create a string and get its length
        String message = "Hello, Java!";

        // Print the length
        System.out.println("Length: " + message.length());

        // Access first character
        System.out.println("First char: " + message.charAt(0));
    }
}''',
                "Length: 12\\nFirst char: H"
            )
        elif 'concatenat' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        String firstName = "John";
        String lastName = "Doe";

        // TODO: Concatenate with + operator
        // String fullName = firstName + " " + lastName;
        // System.out.println(fullName);
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        String firstName = "John";
        String lastName = "Doe";

        // Concatenate with + operator
        String fullName = firstName + " " + lastName;
        System.out.println("Full name: " + fullName);
    }
}''',
                "Full name: John Doe"
            )
        elif 'comparison' in title_lower or 'compare' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        String str1 = "hello";
        String str2 = "hello";
        String str3 = "world";

        // TODO: Compare strings using equals()
        // System.out.println(str1.equals(str2));
        // System.out.println(str1.equals(str3));
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        String str1 = "hello";
        String str2 = "hello";
        String str3 = "world";

        // Compare strings using equals()
        System.out.println("str1 equals str2: " + str1.equals(str2));
        System.out.println("str1 equals str3: " + str1.equals(str3));
    }
}''',
                "str1 equals str2: true\\nstr1 equals str3: false"
            )
        elif 'case' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        String text = "Hello World";

        // TODO: Convert to uppercase
        // System.out.println(text.toUpperCase());

        // TODO: Convert to lowercase
        // System.out.println(text.toLowerCase());
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        String text = "Hello World";

        // Convert to uppercase
        System.out.println("Upper: " + text.toUpperCase());

        // Convert to lowercase
        System.out.println("Lower: " + text.toLowerCase());
    }
}''',
                "Upper: HELLO WORLD\\nLower: hello world"
            )
        elif 'trim' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        String text = "  Hello World  ";

        // TODO: Remove whitespace
        // System.out.println("'" + text.trim() + "'");
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        String text = "  Hello World  ";

        // Remove whitespace
        System.out.println("Before: '" + text + "'");
        System.out.println("After: '" + text.trim() + "'");
    }
}''',
                "Before: '  Hello World  '\\nAfter: 'Hello World'"
            )
        elif 'contains' in title_lower or 'indexof' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        String text = "Hello World";

        // TODO: Check if contains "World"
        // System.out.println(text.contains("World"));

        // TODO: Find index of "World"
        // System.out.println(text.indexOf("World"));
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        String text = "Hello World";

        // Check if contains "World"
        System.out.println("Contains 'World': " + text.contains("World"));

        // Find index of "World"
        System.out.println("Index of 'World': " + text.indexOf("World"));
    }
}''',
                "Contains 'World': true\\nIndex of 'World': 6"
            )
        elif 'replace' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        String text = "Hello World";

        // TODO: Replace "World" with "Java"
        // String result = text.replace("World", "Java");
        // System.out.println(result);
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        String text = "Hello World";

        // Replace "World" with "Java"
        String result = text.replace("World", "Java");
        System.out.println("Original: " + text);
        System.out.println("Modified: " + result);
    }
}''',
                "Original: Hello World\\nModified: Hello Java"
            )
        elif 'split' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        String text = "apple,banana,orange";

        // TODO: Split by comma
        // String[] fruits = text.split(",");
        // for (String fruit : fruits) {
        //     System.out.println(fruit);
        // }
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        String text = "apple,banana,orange";

        // Split by comma
        String[] fruits = text.split(",");
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}''',
                "apple\\nbanana\\norange"
            )

    # Array lessons
    elif 'array' in title_lower:
        if 'creating' in title_lower or 'create' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        // TODO: Create an array of integers
        // int[] numbers = {1, 2, 3, 4, 5};

        // TODO: Print the array
        // System.out.println("Created array with " + numbers.length + " elements");
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        // Create an array of integers
        int[] numbers = {1, 2, 3, 4, 5};

        // Print the array
        System.out.println("Created array with " + numbers.length + " elements");
        System.out.println("First element: " + numbers[0]);
    }
}''',
                "Created array with 5 elements\\nFirst element: 1"
            )
        elif 'accessing' in title_lower or 'access' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};

        // TODO: Access elements by index
        // System.out.println("First: " + numbers[0]);
        // System.out.println("Last: " + numbers[4]);
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};

        // Access elements by index
        System.out.println("First: " + numbers[0]);
        System.out.println("Third: " + numbers[2]);
        System.out.println("Last: " + numbers[4]);
    }
}''',
                "First: 10\\nThird: 30\\nLast: 50"
            )
        elif 'length' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};

        // TODO: Print array length
        // System.out.println("Length: " + numbers.length);
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};

        // Print array length
        System.out.println("Length: " + numbers.length);
    }
}''',
                "Length: 5"
            )
        elif 'iterating' in title_lower or 'iterate' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};

        // TODO: Loop through array
        // for (int num : numbers) {
        //     System.out.println(num);
        // }
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};

        // Loop through array
        for (int num : numbers) {
            System.out.println(num);
        }
    }
}''',
                "1\\n2\\n3\\n4\\n5"
            )
        elif 'sum' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};

        // TODO: Calculate sum
        // int sum = 0;
        // for (int num : numbers) {
        //     sum += num;
        // }
        // System.out.println("Sum: " + sum);
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};

        // Calculate sum
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        System.out.println("Sum: " + sum);
    }
}''',
                "Sum: 15"
            )
        elif 'max' in title_lower or 'maximum' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {3, 7, 2, 9, 1};

        // TODO: Find maximum
        // int max = numbers[0];
        // for (int num : numbers) {
        //     if (num > max) max = num;
        // }
        // System.out.println("Max: " + max);
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {3, 7, 2, 9, 1};

        // Find maximum
        int max = numbers[0];
        for (int num : numbers) {
            if (num > max) max = num;
        }
        System.out.println("Max: " + max);
    }
}''',
                "Max: 9"
            )
        elif 'min' in title_lower or 'minimum' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {3, 7, 2, 9, 1};

        // TODO: Find minimum
        // int min = numbers[0];
        // for (int num : numbers) {
        //     if (num < min) min = num;
        // }
        // System.out.println("Min: " + min);
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        int[] numbers = {3, 7, 2, 9, 1};

        // Find minimum
        int min = numbers[0];
        for (int num : numbers) {
            if (num < min) min = num;
        }
        System.out.println("Min: " + min);
    }
}''',
                "Min: 1"
            )

    # ArrayList lessons
    elif 'arraylist' in title_lower:
        if 'creating' in title_lower or 'create' in title_lower:
            return (
                '''import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // TODO: Create an ArrayList
        // ArrayList<String> fruits = new ArrayList<>();
        // System.out.println("Created ArrayList");
    }
}''',
                '''import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // Create an ArrayList
        ArrayList<String> fruits = new ArrayList<>();
        System.out.println("Created ArrayList: " + fruits);
    }
}''',
                "Created ArrayList: []"
            )
        elif 'adding' in title_lower or 'add' in title_lower:
            return (
                '''import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();

        // TODO: Add elements
        // fruits.add("Apple");
        // fruits.add("Banana");
        // System.out.println(fruits);
    }
}''',
                '''import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();

        // Add elements
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");
        System.out.println("Fruits: " + fruits);
    }
}''',
                "Fruits: [Apple, Banana, Orange]"
            )
        elif 'remov' in title_lower:
            return (
                '''import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");

        // TODO: Remove an element
        // fruits.remove("Banana");
        // System.out.println(fruits);
    }
}''',
                '''import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");

        // Remove an element
        fruits.remove("Banana");
        System.out.println("After removal: " + fruits);
    }
}''',
                "After removal: [Apple, Orange]"
            )
        elif 'size' in title_lower:
            return (
                '''import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");

        // TODO: Get size
        // System.out.println("Size: " + fruits.size());
    }
}''',
                '''import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");

        // Get size
        System.out.println("Size: " + fruits.size());
    }
}''',
                "Size: 3"
            )

    # Loop lessons
    elif 'loop' in title_lower or 'for' in title_lower:
        if 'simple for' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        // TODO: Print numbers 1 to 5
        // for (int i = 1; i <= 5; i++) {
        //     System.out.println(i);
        // }
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        // Print numbers 1 to 5
        for (int i = 1; i <= 5; i++) {
            System.out.println(i);
        }
    }
}''',
                "1\\n2\\n3\\n4\\n5"
            )
        elif 'break' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        // TODO: Loop until finding 5
        // for (int i = 1; i <= 10; i++) {
        //     System.out.println(i);
        //     if (i == 5) break;
        // }
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        // Loop until finding 5
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
            if (i == 5) {
                System.out.println("Found 5, breaking!");
                break;
            }
        }
    }
}''',
                "1\\n2\\n3\\n4\\n5\\nFound 5, breaking!"
            )
        elif 'continue' in title_lower:
            return (
                '''public class Main {
    public static void main(String[] args) {
        // TODO: Skip even numbers
        // for (int i = 1; i <= 5; i++) {
        //     if (i % 2 == 0) continue;
        //     System.out.println(i);
        // }
    }
}''',
                '''public class Main {
    public static void main(String[] args) {
        // Skip even numbers
        for (int i = 1; i <= 5; i++) {
            if (i % 2 == 0) continue;
            System.out.println(i + " is odd");
        }
    }
}''',
                "1 is odd\\n3 is odd\\n5 is odd"
            )

    # Default generic code
    return (
        f'''public class Main {{
    public static void main(String[] args) {{
        // TODO: {title}
        // {description}

        System.out.println("Complete the exercise");
    }}
}}''',
        f'''public class Main {{
    public static void main(String[] args) {{
        // {title}
        // {description}

        System.out.println("Exercise completed!");
    }}
}}''',
        "Exercise completed!"
    )


def improve_java_lessons():
    """Improve all Java beginner lesson code."""
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    improved = 0
    for lesson in lessons:
        if lesson['difficulty'] != 'Beginner':
            continue

        # Check if lesson has generic code (both patterns)
        solution = lesson.get('fullSolution', '')
        if 'Exercise completed!' in solution or 'Complete the exercise' in solution:
            base_code, full_solution, expected_output = create_java_code_for_topic(
                lesson['title'],
                lesson['description']
            )

            lesson['baseCode'] = base_code
            lesson['fullSolution'] = full_solution
            lesson['expectedOutput'] = expected_output
            improved += 1
            if improved <= 20:  # Print first 20
                print(f"Improved: {lesson['id']}: {lesson['title']}")

    with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    print(f"\nImproved {improved} Java lessons")
    return improved


if __name__ == "__main__":
    print("=" * 80)
    print("IMPROVING LESSON CODE EXAMPLES")
    print("=" * 80)
    print()

    java_count = improve_java_lessons()

    print()
    print("=" * 80)
    print(f"COMPLETE! Improved {java_count} lessons with topic-specific code")
    print("=" * 80)
