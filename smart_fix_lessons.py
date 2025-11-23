#!/usr/bin/env python3
"""
Smart lesson fixer that generates implementations based on title analysis.
"""

import json
import re

# Lesson templates organized by topic
LESSON_TEMPLATES = {
    # Core concepts
    "variables": {
        "baseCode": "# {title}\n# TODO: Create and use variables\n\n",
        "fullSolution": "# {title}\nname = \"Alice\"\nage = 25\nheight = 5.6\nis_student = True\n\nprint(f\"Name: {name}\")\nprint(f\"Age: {age}\")\nprint(f\"Height: {height}\")\nprint(f\"Student: {is_student}\")\n",
        "expectedOutput": "Name: Alice\nAge: 25\nHeight: 5.6\nStudent: True\n"
    },

    # List operations
    "list_basics": {
        "baseCode": "# {title}\n# TODO: Work with lists\n\n",
        "fullSolution": "# {title}\nmy_list = [1, 2, 3, 4, 5]\nprint(f\"List: {my_list}\")\nprint(f\"Length: {len(my_list)}\")\nprint(f\"First: {my_list[0]}\")\nprint(f\"Last: {my_list[-1]}\")\n",
        "expectedOutput": "List: [1, 2, 3, 4, 5]\nLength: 5\nFirst: 1\nLast: 5\n"
    },

    "list_methods": {
        "baseCode": "# {title}\n# TODO: Use list methods\n\n",
        "fullSolution": "# {title}\nmy_list = [1, 2, 3]\nprint(f\"Original: {my_list}\")\n\nmy_list.append(4)\nprint(f\"After append(4): {my_list}\")\n\nmy_list.insert(0, 0)\nprint(f\"After insert(0, 0): {my_list}\")\n\nmy_list.remove(2)\nprint(f\"After remove(2): {my_list}\")\n",
        "expectedOutput": "Original: [1, 2, 3]\nAfter append(4): [1, 2, 3, 4]\nAfter insert(0, 0): [0, 1, 2, 3, 4]\nAfter remove(2): [0, 1, 3, 4]\n"
    },

    # Dictionary operations
    "dict_basics": {
        "baseCode": "# {title}\n# TODO: Work with dictionaries\n\n",
        "fullSolution": "# {title}\nmy_dict = {'name': 'Alice', 'age': 25}\nprint(f\"Dictionary: {my_dict}\")\nprint(f\"Name: {my_dict['name']}\")\nprint(f\"Keys: {list(my_dict.keys())}\")\n",
        "expectedOutput": "Dictionary: {'name': 'Alice', 'age': 25}\nName: Alice\nKeys: ['name', 'age']\n"
    },

    # String operations
    "string_methods": {
        "baseCode": "# {title}\n# TODO: Use string methods\n\n",
        "fullSolution": "# {title}\ntext = \"Hello World\"\nprint(f\"Original: {text}\")\nprint(f\"Lower: {text.lower()}\")\nprint(f\"Upper: {text.upper()}\")\nprint(f\"Replace: {text.replace('World', 'Python')}\")\nprint(f\"Split: {text.split()}\")\n",
        "expectedOutput": "Original: Hello World\nLower: hello world\nUpper: HELLO WORLD\nReplace: Hello Python\nSplit: ['Hello', 'World']\n"
    },

    # Functions
    "function_basics": {
        "baseCode": "# {title}\n# TODO: Define and call a function\n\n",
        "fullSolution": "# {title}\ndef greet(name):\n    return f\"Hello, {name}!\"\n\nresult1 = greet(\"Alice\")\nresult2 = greet(\"Bob\")\n\nprint(result1)\nprint(result2)\n",
        "expectedOutput": "Hello, Alice!\nHello, Bob!\n"
    },

    # Classes/OOP
    "class_basics": {
        "baseCode": "# {title}\n# TODO: Create a class\n\n",
        "fullSolution": "# {title}\nclass Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    \n    def greet(self):\n        return f\"Hi, I'm {self.name}!\"\n\nperson = Person(\"Alice\", 25)\nprint(person.greet())\nprint(f\"Age: {person.age}\")\n",
        "expectedOutput": "Hi, I'm Alice!\nAge: 25\n"
    },

    # File operations
    "file_operations": {
        "baseCode": "# {title}\n# TODO: Work with files\nimport os\n\n",
        "fullSolution": "# {title}\nimport os\n\n# Write\nwith open('test.txt', 'w') as f:\n    f.write('Hello\\nWorld\\n')\n\n# Read\nwith open('test.txt', 'r') as f:\n    content = f.read()\n    print(content)\n\n# Cleanup\nos.remove('test.txt')\n",
        "expectedOutput": "Hello\nWorld\n\n"
    },

    # Loops
    "for_loop": {
        "baseCode": "# {title}\n# TODO: Use a for loop\n\n",
        "fullSolution": "# {title}\nfor i in range(1, 6):\n    print(f\"Number: {i}\")\n",
        "expectedOutput": "Number: 1\nNumber: 2\nNumber: 3\nNumber: 4\nNumber: 5\n"
    },

    # Exception handling
    "exceptions": {
        "baseCode": "# {title}\n# TODO: Handle exceptions\n\n",
        "fullSolution": "# {title}\ntry:\n    result = 10 / 2\n    print(f\"Result: {result}\")\nexcept ZeroDivisionError:\n    print(\"Cannot divide by zero\")\n\ntry:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print(\"Caught division by zero\")\n",
        "expectedOutput": "Result: 5.0\nCaught division by zero\n"
    },

    # Algorithms
    "sorting": {
        "baseCode": "# {title}\n# TODO: Sort data\n\n",
        "fullSolution": "# {title}\nnumbers = [5, 2, 8, 1, 9, 3]\nprint(f\"Original: {numbers}\")\nprint(f\"Sorted: {sorted(numbers)}\")\nprint(f\"Descending: {sorted(numbers, reverse=True)}\")\n",
        "expectedOutput": "Original: [5, 2, 8, 1, 9, 3]\nSorted: [1, 2, 3, 5, 8, 9]\nDescending: [9, 8, 5, 3, 2, 1]\n"
    },

    # Advanced topics
    "fastapi": {
        "baseCode": "# {title}\nfrom fastapi import FastAPI\n\napp = FastAPI()\n\n",
        "fullSolution": "# {title}\nfrom fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get(\"/\")\nasync def root():\n    return {\"message\": \"Hello World\"}\n\nprint(\"FastAPI app created\")\nprint(\"Route '/' registered\")\n",
        "expectedOutput": "FastAPI app created\nRoute '/' registered\n"
    },

    "redis": {
        "baseCode": "# {title}\n# TODO: Demonstrate Redis concepts (simulated)\n\n",
        "fullSolution": "# {title}\nprint(\"=== {title} ===\")\n\n# Simulated Redis\nclass RedisClient:\n    def __init__(self):\n        self.store = {}\n    def set(self, k, v):\n        self.store[k] = v\n        return True\n    def get(self, k):\n        return self.store.get(k)\n\nredis = RedisClient()\nredis.set('user:1', 'Alice')\nprint(f\"Stored: user:1 = Alice\")\nprint(f\"Retrieved: {redis.get('user:1')}\")\n",
        "expectedOutput": "=== {title} ===\nStored: user:1 = Alice\nRetrieved: Alice\n"
    },

    "docker": {
        "baseCode": "# {title}\n# TODO: Demonstrate Docker concepts\n\n",
        "fullSolution": "# {title}\nprint(\"=== {title} ===\")\nprint(\"Docker: Containerization platform\")\nprint(\"Key concepts:\")\nprint(\"  - Containers: Isolated app environments\")\nprint(\"  - Images: Container templates\")\nprint(\"  - Dockerfiles: Build instructions\")\n",
        "expectedOutput": "=== {title} ===\nDocker: Containerization platform\nKey concepts:\n  - Containers: Isolated app environments\n  - Images: Container templates\n  - Dockerfiles: Build instructions\n"
    },

    "aws": {
        "baseCode": "# {title}\n# TODO: Demonstrate AWS concepts\n\n",
        "fullSolution": "# {title}\nprint(\"=== {title} ===\")\nprint(\"AWS cloud service\")\nprint(\"Key features:\")\nprint(\"  - Scalable infrastructure\")\nprint(\"  - Pay-as-you-go pricing\")\nprint(\"  - Global availability\")\n",
        "expectedOutput": "=== {title} ===\nAWS cloud service\nKey features:\n  - Scalable infrastructure\n  - Pay-as-you-go pricing\n  - Global availability\n"
    },

    # Generic fallback
    "generic": {
        "baseCode": "# {title}\n# TODO: Implement {title}\n\n",
        "fullSolution": "# {title}\nprint(\"{title}\")\nprint(\"Concept demonstration\")\n",
        "expectedOutput": "{title}\nConcept demonstration\n"
    }
}


def select_template(title, description, category):
    """Select the best template for a lesson based on title and category."""
    title_lower = title.lower()

    # Keyword mapping to templates
    keywords = {
        "variable": "variables",
        "data type": "variables",

        "list": "list_basics",
        "append": "list_methods",
        "remove": "list_methods",
        "insert": "list_methods",

        "dictionary": "dict_basics",
        "dict": "dict_basics",

        "string": "string_methods",

        "function": "function_basics",
        "parameter": "function_basics",
        "return": "function_basics",

        "class": "class_basics",
        "object": "class_basics",
        "method": "class_basics",
        "inheritance": "class_basics",

        "file": "file_operations",
        "read": "file_operations",
        "write": "file_operations",

        "for": "for_loop",
        "loop": "for_loop",
        "iterate": "for_loop",

        "exception": "exceptions",
        "error": "exceptions",
        "try": "exceptions",

        "sort": "sorting",
        "search": "sorting",

        "fastapi": "fastapi",
        "redis": "redis",
        "docker": "docker",
        "aws": "aws",
        "s3": "aws",
        "ec2": "aws",
        "lambda": "aws",
    }

    # Check keywords in title
    for keyword, template_name in keywords.items():
        if keyword in title_lower:
            return LESSON_TEMPLATES[template_name]

    # Fallback to generic
    return LESSON_TEMPLATES["generic"]


def generate_lesson(lesson_id, title, description, difficulty, category):
    """Generate lesson implementation."""

    # Select template
    template = select_template(title, description, category)

    # Replace {title} with actual title (simple string replacement)
    return {
        "baseCode": template["baseCode"].replace("{title}", title),
        "fullSolution": template["fullSolution"].replace("{title}", title),
        "expectedOutput": template["expectedOutput"].replace("{title}", title)
    }


def is_placeholder(solution, title):
    """Check if a solution is a placeholder."""
    lines = [l.strip() for l in solution.strip().split('\n')
             if l.strip() and not l.strip().startswith('#')]

    # Check for double braces in f-strings (sign of incorrectly formatted templates)
    has_double_braces_in_fstring = 'f"' in solution and '{{' in solution and '}}' in solution

    return (
        len(lines) <= 2 or
        'TODO: Implement' in solution or
        'Implementation placeholder' in solution or
        (len(lines) == 1 and f'print("{title}")' in solution) or
        (len(lines) == 1 and 'print(' in lines[0] and title.lower() in lines[0].lower()) or
        has_double_braces_in_fstring
    )


def fix_lessons(input_file, output_file):
    """Fix all placeholder lessons."""

    with open(input_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    fixed_count = 0

    for lesson in lessons:
        lesson_id = lesson['id']
        title = lesson['title']
        solution = lesson.get('fullSolution', '')

        if is_placeholder(solution, title):
            print(f"Fixing {lesson_id}: {title}")

            new_content = generate_lesson(
                lesson_id,
                title,
                lesson.get('description', ''),
                lesson.get('difficulty', 'Beginner'),
                lesson.get('category', 'Core Python')
            )

            lesson['baseCode'] = new_content['baseCode']
            lesson['fullSolution'] = new_content['fullSolution']
            lesson['expectedOutput'] = new_content['expectedOutput']

            fixed_count += 1

    # Save
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    print(f"\n[DONE] Fixed {fixed_count} lessons")
    print(f"[SAVE] Saved to {output_file}")

    return fixed_count


if __name__ == '__main__':
    fix_lessons('public/lessons-python.json', 'public/lessons-python.json')
