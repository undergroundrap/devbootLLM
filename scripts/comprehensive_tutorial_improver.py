"""
Comprehensive Tutorial Improvement System
Improves all 222 remaining lessons to college-level quality
"""
import json
import re

def clean_generic_content(tutorial):
    """Remove generic template language from tutorials"""
    # Patterns to remove/replace
    generic_patterns = [
        (r'Flask is a critical technology for modern applications\.', ''),
        (r'Django is a critical technology for modern applications\.', ''),
        (r'Spring Boot is a critical technology for modern applications\.', ''),
        (r'Java is a critical technology for modern applications\.', ''),
        (r'Python is a critical technology for modern applications\.', ''),
        (r'\*Practice these concepts in real projects to build expertise\.\*', ''),
        (r'Practice these concepts in real projects to build expertise\.', ''),
        (r'Understanding .+ is essential for web development development',
         lambda m: m.group(0).replace(' development development', ' development')),
        # Fix double "development development"
        (r'development development', 'development'),
    ]

    cleaned = tutorial
    for pattern, replacement in generic_patterns:
        if callable(replacement):
            cleaned = re.sub(pattern, replacement, cleaned, flags=re.IGNORECASE)
        else:
            cleaned = re.sub(pattern, replacement, cleaned, flags=re.IGNORECASE)

    return cleaned

def add_technical_depth_advanced(lesson):
    """
    Expand Advanced/Expert tutorials that are too short
    Add framework-specific technical content
    """
    title = lesson['title']
    category = lesson.get('category', '')
    current_tutorial = lesson['tutorial']

    # Only process if too short
    if len(current_tutorial) >= 1500:
        return None  # No change needed

    # Add depth based on topic area
    additions = []

    # Web framework lessons
    if 'Flask' in title or 'Django' in title or 'FastAPI' in title:
        additions.append("""
<div style="background: rgba(59, 130, 246, 0.1); border-left: 4px solid #3b82f6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">🏗️ Architecture Considerations</h4>
  <p class="mb-4 text-gray-300">When implementing this pattern in production:</p>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li><strong class="text-blue-400">Scalability:</strong> Design for horizontal scaling with stateless servers</li>
    <li><strong class="text-blue-400">Performance:</strong> Use caching (Redis) and database query optimization</li>
    <li><strong class="text-blue-400">Security:</strong> Implement input validation, CSRF protection, and SQL injection prevention</li>
    <li><strong class="text-blue-400">Monitoring:</strong> Add logging, error tracking (Sentry), and performance monitoring (New Relic)</li>
  </ul>
</div>""")

    # Spring Boot lessons
    if 'Spring' in title:
        additions.append("""
<div style="background: rgba(139, 92, 246, 0.1); border-left: 4px solid #8b5cf6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">🔧 Spring Boot Best Practices</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li><strong class="text-purple-400">Dependency Injection:</strong> Use constructor injection for required dependencies (better testability)</li>
    <li><strong class="text-purple-400">Configuration:</strong> Externalize configuration with application.yml and environment variables</li>
    <li><strong class="text-purple-400">Exception Handling:</strong> Use @ControllerAdvice for global exception handling</li>
    <li><strong class="text-purple-400">Testing:</strong> Write integration tests with @SpringBootTest and unit tests with @WebMvcTest</li>
  </ul>
</div>""")

    # Database/ORM lessons
    if any(term in title.lower() for term in ['database', 'sql', 'orm', 'hibernate', 'jpa', 'sqlalchemy']):
        additions.append("""
<div style="background: rgba(16, 185, 129, 0.1); border-left: 4px solid #10b981; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">📊 Database Performance</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li><strong class="text-green-400">Indexing:</strong> Add indexes on frequently queried columns (WHERE, JOIN, ORDER BY)</li>
    <li><strong class="text-green-400">N+1 Queries:</strong> Use eager loading or JOIN FETCH to avoid multiple queries</li>
    <li><strong class="text-green-400">Connection Pooling:</strong> Configure pool size based on concurrent users (formula: connections = ((core_count * 2) + effective_spindle_count))</li>
    <li><strong class="text-green-400">Query Optimization:</strong> Use EXPLAIN to analyze query plans and optimize slow queries</li>
  </ul>
</div>""")

    # Add common production section for all Advanced lessons
    additions.append("""
<div style="background: rgba(245, 158, 11, 0.1); border-left: 4px solid #f59e0b; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">⚡ Common Pitfalls to Avoid</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li>Not handling edge cases and error conditions properly</li>
    <li>Ignoring performance implications at scale (test with realistic data volumes)</li>
    <li>Insufficient logging and monitoring in production</li>
    <li>Not writing comprehensive tests (aim for >80% code coverage)</li>
    <li>Hardcoding configuration values instead of using environment variables</li>
  </ul>
</div>""")

    # If we have additions, insert them before the closing tags
    if additions:
        # Find good insertion point (before final closing divs)
        insertion_point = current_tutorial.rfind('</div>')
        if insertion_point > 0:
            enhanced = (current_tutorial[:insertion_point] +
                       '\n'.join(additions) +
                       current_tutorial[insertion_point:])
            return enhanced

    return None

def add_code_example(lesson):
    """
    Add code examples to tutorials that are missing them
    """
    title = lesson['title']
    tutorial = lesson['tutorial']

    # Check if already has code examples
    if '<pre' in tutorial or 'Example:' in tutorial:
        return None  # Already has examples

    # Extract a meaningful snippet from the solution
    solution = lesson.get('fullSolution', '')

    # Get first 10-15 lines of solution as example
    lines = solution.split('\n')
    # Skip comments and empty lines at start
    start_idx = 0
    for i, line in enumerate(lines):
        if line.strip() and not line.strip().startswith('#') and not line.strip().startswith('//'):
            start_idx = i
            break

    # Take next 12 lines for example
    example_lines = lines[start_idx:start_idx + 12]
    example_code = '\n'.join(example_lines)

    if not example_code.strip():
        return None

    # Create code example section
    code_example = f"""
<div style="background: rgba(16, 185, 129, 0.1); border-left: 4px solid #10b981; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">💡 Code Example</h4>
  <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto"><code>{example_code}</code></pre>
  <p class="mt-4 text-gray-300">This example demonstrates the core concept. Study the full solution to see the complete implementation with additional details.</p>
</div>"""

    # Insert before last closing div
    insertion_point = tutorial.rfind('</div>')
    if insertion_point > 0:
        enhanced = tutorial[:insertion_point] + code_example + tutorial[insertion_point:]
        return enhanced

    return None

def improve_lesson(lesson):
    """
    Apply all improvements to a single lesson
    Returns: (modified, changes_made)
    """
    changes = []
    modified = False

    # 1. Clean generic content
    old_tutorial = lesson['tutorial']
    cleaned = clean_generic_content(old_tutorial)
    if cleaned != old_tutorial:
        lesson['tutorial'] = cleaned
        changes.append('removed_generic_content')
        modified = True

    # 2. Add depth to Advanced/Expert tutorials
    if lesson.get('difficulty') in ['Advanced', 'Expert']:
        enhanced = add_technical_depth_advanced(lesson)
        if enhanced:
            lesson['tutorial'] = enhanced
            changes.append(f'added_depth({len(enhanced) - len(lesson["tutorial"])}chars)')
            modified = True

    # 3. Add code examples if missing
    with_example = add_code_example(lesson)
    if with_example:
        lesson['tutorial'] = with_example
        changes.append('added_code_example')
        modified = True

    return modified, changes

def improve_all_lessons(lessons_to_improve_file, lessons_file, language):
    """
    Improve all lessons that need work
    """
    # Load lessons needing improvement
    with open(lessons_to_improve_file, 'r', encoding='utf-8') as f:
        improvement_data = json.load(f)

    lessons_to_fix = improvement_data[language]

    # Load actual lessons
    with open(lessons_file, 'r', encoding='utf-8') as f:
        all_lessons = json.load(f)

    # Create lookup for faster access
    lesson_lookup = {l['id']: i for i, l in enumerate(all_lessons)}

    improved_count = 0
    total_to_improve = len(lessons_to_fix)

    print(f"\n=== Improving {language.upper()} Lessons ===")
    print(f"Total lessons to improve: {total_to_improve}\n")

    for i, lesson_info in enumerate(lessons_to_fix, 1):
        lesson_id = lesson_info['id']

        if lesson_id not in lesson_lookup:
            print(f"[WARN] Lesson {lesson_id} not found in lessons file")
            continue

        lesson_idx = lesson_lookup[lesson_id]
        lesson = all_lessons[lesson_idx]

        # Skip already improved lessons (from batch 1)
        if lesson_id in [714, 715]:
            print(f"[SKIP] Lesson {lesson_id}: {lesson['title']} (already improved)")
            continue

        old_len = len(lesson['tutorial'])
        modified, changes = improve_lesson(lesson)

        if modified:
            new_len = len(lesson['tutorial'])
            improved_count += 1
            print(f"[{improved_count}/{total_to_improve}] Lesson {lesson_id}: {lesson['title']}")
            print(f"  Tutorial: {old_len} -> {new_len} chars (+{new_len - old_len})")
            print(f"  Changes: {', '.join(changes)}")
        else:
            print(f"[SKIP] Lesson {lesson_id}: {lesson['title']} (no improvements needed)")

    # Save improved lessons
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(all_lessons, f, indent=2, ensure_ascii=False)

    print(f"\n[DONE] Improved {improved_count} {language} lessons")
    return improved_count

if __name__ == '__main__':
    print("=== Comprehensive Tutorial Improvement System ===\n")

    # Improve Python lessons
    python_count = improve_all_lessons(
        'lessons_needing_improvement.json',
        'public/lessons-python.json',
        'python'
    )

    # Improve Java lessons
    java_count = improve_all_lessons(
        'lessons_needing_improvement.json',
        'public/lessons-java.json',
        'java'
    )

    print(f"\n{'='*60}")
    print(f"TOTAL IMPROVEMENTS: {python_count + java_count} lessons")
    print(f"  Python: {python_count}")
    print(f"  Java: {java_count}")
    print(f"{'='*60}")
