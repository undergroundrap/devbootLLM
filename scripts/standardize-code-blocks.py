#!/usr/bin/env python3
"""
Standardize all code blocks to use class="tutorial-code-block"
"""

import json
import re

def standardize_code_blocks(tutorial):
    """
    Replace various <pre> tag formats with standardized class="tutorial-code-block"
    """
    # Pattern 1: <pre><code>...</code></pre> -> <pre class="tutorial-code-block">...</pre>
    tutorial = re.sub(
        r'<pre>\s*<code>(.*?)</code>\s*</pre>',
        r'<pre class="tutorial-code-block">\1</pre>',
        tutorial,
        flags=re.DOTALL
    )

    # Pattern 2: <pre> without class -> <pre class="tutorial-code-block">
    tutorial = re.sub(
        r'<pre>(?!.*class=)',
        r'<pre class="tutorial-code-block">',
        tutorial
    )

    # Pattern 3: <pre class="..."> replace with tutorial-code-block
    tutorial = re.sub(
        r'<pre class="[^"]*">',
        r'<pre class="tutorial-code-block">',
        tutorial
    )

    return tutorial

def main():
    print("=" * 70)
    print("STANDARDIZING CODE BLOCK FORMATTING")
    print("=" * 70)
    print()

    for lang_file, lang_name in [('public/lessons-java.json', 'Java'),
                                   ('public/lessons-python.json', 'Python')]:
        print(f"\nProcessing {lang_name} lessons...")

        with open(lang_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        updated_count = 0

        for lesson in data['lessons']:
            lesson_id = lesson['id']

            # Only process lessons 601-650
            if not (601 <= lesson_id <= 650):
                continue

            old_tutorial = lesson['tutorial']
            new_tutorial = standardize_code_blocks(old_tutorial)

            if new_tutorial != old_tutorial:
                lesson['tutorial'] = new_tutorial
                print(f"  [STANDARDIZED] Lesson {lesson_id}: {lesson['title']}")
                updated_count += 1

        # Save updated file
        with open(lang_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"\n[SUCCESS] {lang_name}: Standardized {updated_count} lessons")

    print()
    print("=" * 70)
    print("CODE BLOCKS STANDARDIZED!")
    print("=" * 70)

if __name__ == "__main__":
    main()
