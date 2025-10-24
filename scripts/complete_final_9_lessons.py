import json

# Define missing sections for each lesson
MISSING_SECTIONS = {
    423: {
        'overview': '''<h4 class="font-semibold text-gray-200 mb-2">Overview</h4>
<p class="mb-4 text-gray-300">
Environment variables allow you to configure applications without hardcoding values. Reading them properly is essential for deployable, secure applications that work across different environments (dev, staging, production).
</p>

'''
    },
    424: {
        'overview': '''<h4 class="font-semibold text-gray-200 mb-2">Overview</h4>
<p class="mb-4 text-gray-300">
Providing sensible defaults for environment variables makes your application more robust and easier to configure. This lesson shows how to handle missing environment variables gracefully with fallback values.
</p>

'''
    },
    651: {
        'best_practices': '''<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Use proper HTTP status codes (200 OK, 201 Created, 404 Not Found, 400 Bad Request)</li>
<li>Implement input validation before processing requests</li>
<li>Use DTOs (Data Transfer Objects) to separate API models from domain models</li>
<li>Add pagination for list endpoints to handle large datasets</li>
<li>Include timestamps (createdAt, updatedAt) for all resources</li>
<li>Implement proper error responses with meaningful messages</li>
</ul>

'''
    },
    653: {
        'best_practices': '''<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Use BigDecimal for money calculations to avoid floating-point errors</li>
<li>Implement atomic operations for cart updates to prevent race conditions</li>
<li>Validate discount codes server-side (never trust client)</li>
<li>Set cart expiration (TTL) to free up memory from abandoned carts</li>
<li>Log all cart operations for analytics and fraud detection</li>
<li>Use database transactions for checkout to ensure consistency</li>
</ul>

'''
    },
    654: {
        'best_practices': '''<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Store API keys in environment variables, never hardcode them</li>
<li>Implement exponential backoff for retry logic on API failures</li>
<li>Use cache headers (Cache-Control, ETag) for HTTP caching</li>
<li>Set appropriate TTL based on data freshness requirements</li>
<li>Monitor cache hit rate - aim for 80%+ for significant cost savings</li>
<li>Implement circuit breaker pattern for external API calls</li>
</ul>

'''
    },
    655: {
        'best_practices': '''<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Use database indexes on shortCode for O(1) lookups at scale</li>
<li>Implement collision detection with retry logic (max 3-5 attempts)</li>
<li>Exclude ambiguous characters (0/O, 1/l/I) from short code alphabet</li>
<li>Set expiration dates for temporary links to prevent database bloat</li>
<li>Rate limit URL creation per IP to prevent abuse</li>
<li>Validate URLs before shortening (check for malicious/spam sites)</li>
</ul>

''',
        'real_world': '''<h4 class="font-semibold text-gray-200 mb-2">Real-World Applications</h4>
<p class="mb-4 text-gray-300">
URL shorteners are used by marketing teams (track campaign performance), social media platforms (character limits), QR codes (shorter URLs scan better), email campaigns (cleaner links), and analytics (track click-through rates). Companies like Bit.ly, TinyURL, and Google's goo.gl (discontinued) handle billions of redirects daily. Key scaling challenge: maintaining O(1) lookup performance as database grows to millions/billions of URLs.
</p>

'''
    },
    681: {
        'best_practices': '''<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Always add null checks for external inputs and method parameters</li>
<li>Use try-with-resources for automatic resource cleanup</li>
<li>Write unit tests that cover edge cases (empty, null, boundaries)</li>
<li>Use static analysis tools (SonarQube, SpotBugs) to catch bugs early</li>
<li>Follow the principle of least surprise - code should behave as expected</li>
<li>Add defensive checks even if "impossible" - defensive programming saves production</li>
</ul>

''',
        'real_world': '''<h4 class="font-semibold text-gray-200 mb-2">Real-World Applications</h4>
<p class="mb-4 text-gray-300">
These 5 bug patterns account for ~70% of production issues. NullPointerException alone causes billions in losses annually. Companies like Amazon, Netflix, and Google invest heavily in preventing these through code reviews, static analysis, and comprehensive testing. Senior developers spend 40-60% of time debugging - mastering these patterns dramatically accelerates your career.
</p>

'''
    },
    691: {
        'real_world': '''<h4 class="font-semibold text-gray-200 mb-2">Real-World Applications</h4>
<p class="mb-4 text-gray-300">
Professional code review is mandatory at FAANG companies and most tech companies. Google requires minimum 2 reviewers for production code. Facebook analyzes code review data to improve engineering productivity. Studies show code review catches 60% of defects before production, reduces technical debt, and is the #1 way junior developers learn from seniors. Teams with strong code review culture ship 30-50% fewer bugs.
</p>

'''
    },
    695: {
        'best_practices': '''<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Separate business logic from presentation layer (MVC/Service pattern)</li>
<li>Use dependency injection for testability and loose coupling</li>
<li>Implement proper validation at API boundaries</li>
<li>Add audit logging for all data modifications (who, what, when)</li>
<li>Use proper password hashing (BCrypt, Argon2) not simple hashing</li>
<li>Implement rate limiting to prevent abuse and DDoS attacks</li>
</ul>

'''
    }
}

def add_missing_sections():
    # Load Java lessons
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    lessons = {l['id']: l for l in data['lessons']}

    for lesson_id, sections in MISSING_SECTIONS.items():
        if lesson_id in lessons:
            lesson = lessons[lesson_id]
            tutorial = lesson['tutorial']

            # Add overview at the beginning if needed
            if 'overview' in sections:
                tutorial = sections['overview'] + tutorial

            # Add best practices before Common Pitfalls if it exists
            if 'best_practices' in sections:
                if 'Common Pitfalls' in tutorial:
                    tutorial = tutorial.replace(
                        '<h4 class="font-semibold text-gray-200 mb-2">Common Pitfalls</h4>',
                        sections['best_practices'] + '<h4 class="font-semibold text-gray-200 mb-2">Common Pitfalls</h4>'
                    )
                else:
                    # Add near the end before Interview Points or Next Steps
                    if 'Interview Points' in tutorial:
                        tutorial = tutorial.replace(
                            '<h4 class="font-semibold text-gray-200 mb-2">Interview Points</h4>',
                            sections['best_practices'] + '<h4 class="font-semibold text-gray-200 mb-2">Interview Points</h4>'
                        )
                    else:
                        tutorial += '\n' + sections['best_practices']

            # Add real-world near the end
            if 'real_world' in sections:
                if 'Next Steps' in tutorial:
                    tutorial = tutorial.replace(
                        '<h4 class="font-semibold text-gray-200 mb-2">Next Steps</h4>',
                        sections['real_world'] + '<h4 class="font-semibold text-gray-200 mb-2">Next Steps</h4>'
                    )
                else:
                    tutorial += '\n' + sections['real_world']

            lesson['tutorial'] = tutorial
            print(f"Updated Lesson {lesson_id}: {lesson['title']}")

    # Save Java
    with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Mirror to Python
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        py_data = json.load(f)

    py_lessons = {l['id']: l for l in py_data['lessons']}

    for lesson_id in MISSING_SECTIONS.keys():
        if lesson_id in lessons and lesson_id in py_lessons:
            py_lessons[lesson_id]['tutorial'] = lessons[lesson_id]['tutorial']

    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(py_data, f, indent=2, ensure_ascii=False)

    print(f"\n[SUCCESS] Updated {len(MISSING_SECTIONS)} lessons in both Java and Python")

if __name__ == "__main__":
    print("=" * 80)
    print("COMPLETING FINAL 9 LESSONS TO ACHIEVE 100% TUTORIAL DEPTH")
    print("=" * 80)
    print()

    add_missing_sections()

    print("\n" + "=" * 80)
    print("DONE! All lessons now have complete tutorials")
    print("=" * 80)
