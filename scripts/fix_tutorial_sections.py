import json
import re

def add_missing_section_headers(tutorial):
    """Add missing section headers if content exists but header is missing"""

    # If tutorial has code blocks but no "Code Examples" header
    if '<pre' in tutorial or '```' in tutorial:
        if not re.search(r'<h4[^>]*>.*?(code examples?|examples?)', tutorial, re.IGNORECASE):
            # Insert Code Examples header before first code block
            tutorial = re.sub(
                r'(<pre\s|```)',
                r'<h4 class="font-semibold text-gray-200 mb-2">Code Examples</h4>\n\1',
                tutorial,
                count=1
            )

    return tutorial

def add_best_practices_section(lesson_id):
    """Generate Best Practices section for specific lessons"""

    sections = {
        691: """<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Use prepared statements to prevent SQL injection attacks</li>
<li>Hash passwords with bcrypt (never store plain text)</li>
<li>Implement proper authentication middleware on all protected routes</li>
<li>Use HTTPS in production to protect credentials in transit</li>
<li>Add rate limiting to prevent brute force attacks</li>
<li>Validate all user input on both client and server side</li>
</ul>

""",
        710: """<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Practice live coding problems daily on LeetCode, HackerRank, or CodeSignal</li>
<li>Use the STAR method (Situation, Task, Action, Result) for behavioral questions</li>
<li>Think out loud during technical interviews - interviewers want to see your process</li>
<li>Ask clarifying questions before jumping into code</li>
<li>Test your code with examples before declaring it complete</li>
<li>Prepare 3-5 strong stories showcasing your achievements and problem-solving</li>
</ul>

""",
        730: """<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Focus on code readability and maintainability, not just functionality</li>
<li>Give actionable feedback with specific examples of issues</li>
<li>Balance criticism with positive observations (praise good patterns)</li>
<li>Check for security vulnerabilities (SQL injection, XSS, etc.)</li>
<li>Verify proper error handling and edge case coverage</li>
<li>Suggest improvements rather than demanding specific solutions</li>
</ul>

"""
    }

    return sections.get(lesson_id, "")

def add_common_pitfalls_section(lesson_id):
    """Generate Common Pitfalls section for specific lessons"""

    sections = {
        730: """<h4 class="font-semibold text-gray-200 mb-2">Common Pitfalls</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Being overly critical or nitpicky about style preferences</li>
<li>Not explaining WHY a change is needed (educate, don't just criticize)</li>
<li>Focusing only on negatives without acknowledging what's done well</li>
<li>Not running the code locally to verify it actually works</li>
<li>Approving PRs without thorough review just to be nice</li>
<li>Writing vague comments like "fix this" instead of explaining the issue</li>
</ul>

""",
        734: """<h4 class="font-semibold text-gray-200 mb-2">Common Pitfalls</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Not validating user input (leads to crashes and security issues)</li>
<li>Missing error handling for database operations</li>
<li>Not implementing proper authentication/authorization checks</li>
<li>Hardcoding configuration instead of using environment variables</li>
<li>Not writing tests for critical business logic</li>
<li>Skipping input sanitization (opens door to XSS/SQL injection)</li>
</ul>

"""
    }

    return sections.get(lesson_id, "")

def add_real_world_section(lesson_id):
    """Generate Real-World Applications section for specific lessons"""

    sections = {
        690: """<h4 class="font-semibold text-gray-200 mb-2">Real-World Applications</h4>
<p class="mb-4 text-gray-300">
Todo/Task APIs are fundamental building blocks used in: (1) Project management tools like Jira, Asana, Trello (handling millions of tasks daily), (2) Productivity apps like Todoist, Microsoft To Do, Any.do, (3) E-commerce order tracking systems, (4) Bug tracking platforms like GitHub Issues, (5) Healthcare patient task management. Mastering REST API patterns through a todo app demonstrates skills directly transferable to any CRUD-based application. This is often the first portfolio project recruiters want to see.
</p>
""",
        691: """<h4 class="font-semibold text-gray-200 mb-2">Real-World Applications</h4>
<p class="mb-4 text-gray-300">
Blog platforms with authentication power: (1) Medium (60M monthly readers), (2) WordPress (455M websites), (3) Dev.to (1M+ developers), (4) Substack (publishing platform used by thousands of writers), (5) Internal company blogs and knowledge bases. Authentication patterns you implement here (JWT, session management, password hashing) apply to any application requiring user accounts. Every startup needs these skills - user authentication is table-stakes for 90%+ of web applications.
</p>
""",
        692: """<h4 class="font-semibold text-gray-200 mb-2">Real-World Applications</h4>
<p class="mb-4 text-gray-300">
Shopping cart systems are the backbone of e-commerce worth $5.7 trillion globally (2023). Your cart implementation skills apply directly to: (1) Amazon, eBay, Shopify (handling billions in transactions), (2) Food delivery (DoorDash, Uber Eats - real-time cart updates), (3) SaaS subscription management (cart = feature selection), (4) Ticketing systems (Ticketmaster, Eventbrite), (5) Marketplace apps. Companies specifically look for "shopping cart" experience on resumes - it's a concrete signal you understand complex state management and business logic.
</p>
""",
        693: """<h4 class="font-semibold text-gray-200 mb-2">Real-World Applications</h4>
<p class="mb-4 text-gray-300">
Weather API integration teaches essential skills used across industries: (1) Mobile apps (Weather Channel, Weather Underground serve 100M+ users), (2) Agriculture tech (farmers rely on accurate forecasts for $450B+ industry), (3) Logistics and delivery (UPS, FedEx optimize routes based on weather), (4) Travel and hospitality (booking sites show weather to help travelers plan), (5) IoT devices (smart home systems adjust based on weather data). Learning to consume third-party APIs is crucial - 70%+ of modern apps integrate external services.
</p>
""",
        710: """<h4 class="font-semibold text-gray-200 mb-2">Real-World Applications</h4>
<p class="mb-4 text-gray-300">
Technical interview skills directly determine career outcomes: (1) FAANG companies conduct 4-6 rounds of technical interviews, (2) Average software engineer salary jumps from $90K to $180K+ after passing FAANG interviews, (3) Startups increasingly adopt Google/Facebook interview styles, (4) Live coding platforms (HackerRank, CodeSignal) are used by 1000+ companies for screening, (5) Strong interview performance can result in competing offers and 20-40% salary increases. Interview prep is the highest ROI activity for career advancement - weeks of practice can mean hundreds of thousands in additional lifetime earnings.
</p>
""",
        734: """<h4 class="font-semibold text-gray-200 mb-2">Real-World Applications</h4>
<p class="mb-4 text-gray-300">
Full-stack task management systems demonstrate production-ready skills: (1) Startups need developers who can build complete features end-to-end, (2) Companies like Asana, Monday.com, ClickUp are billion-dollar businesses built on task management, (3) Internal tools at FAANG companies often start as simple task trackers, (4) 80%+ of mid-level developer roles require full-stack capabilities, (5) This capstone proves you can: design databases, build APIs, implement auth, create UI, handle errors, write tests. It's the ultimate portfolio piece that says "I'm ready to ship production code on day one."
</p>
"""
    }

    return sections.get(lesson_id, "")

def fix_lessons():
    """Fix missing tutorial sections in Java and Python lessons"""

    print("="*80)
    print("FIXING MISSING TUTORIAL SECTIONS")
    print("="*80)

    # Lessons needing specific fixes
    needs_best_practices = [691, 710, 730]
    needs_pitfalls = [730, 734]
    needs_real_world = [690, 691, 692, 693, 710, 734]

    for language in ['java', 'python']:
        print(f"\n\nProcessing {language.upper()} lessons...")

        filename = f'public/lessons-{language}.json'
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        modified_count = 0

        for lesson in data['lessons']:
            lid = lesson['id']
            original_tutorial = lesson.get('tutorial', '')
            modified = False

            # Add Best Practices if needed
            if lid in needs_best_practices:
                section = add_best_practices_section(lid)
                if section and section not in original_tutorial:
                    # Insert before Common Pitfalls or Real-World (whichever comes first)
                    if '<h4' in original_tutorial:
                        # Find position to insert
                        pitfalls_match = re.search(r'<h4[^>]*>.*?(common pitfalls?|pitfalls?)', original_tutorial, re.IGNORECASE)
                        real_world_match = re.search(r'<h4[^>]*>.*?(real.world|applications?)', original_tutorial, re.IGNORECASE)

                        if pitfalls_match:
                            insert_pos = pitfalls_match.start()
                        elif real_world_match:
                            insert_pos = real_world_match.start()
                        else:
                            insert_pos = len(original_tutorial)

                        lesson['tutorial'] = original_tutorial[:insert_pos] + section + original_tutorial[insert_pos:]
                        modified = True
                        print(f"  Added Best Practices to lesson {lid}")

            # Add Common Pitfalls if needed
            if lid in needs_pitfalls:
                section = add_common_pitfalls_section(lid)
                if section and section not in lesson['tutorial']:
                    # Insert before Real-World
                    real_world_match = re.search(r'<h4[^>]*>.*?(real.world|applications?)', lesson['tutorial'], re.IGNORECASE)

                    if real_world_match:
                        insert_pos = real_world_match.start()
                    else:
                        insert_pos = len(lesson['tutorial'])

                    lesson['tutorial'] = lesson['tutorial'][:insert_pos] + section + lesson['tutorial'][insert_pos:]
                    modified = True
                    print(f"  Added Common Pitfalls to lesson {lid}")

            # Add Real-World if needed
            if lid in needs_real_world:
                section = add_real_world_section(lid)
                if section and section not in lesson['tutorial']:
                    # Append to end
                    lesson['tutorial'] = lesson['tutorial'] + section
                    modified = True
                    print(f"  Added Real-World Applications to lesson {lid}")

            if modified:
                modified_count += 1

        # Save updated lessons
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"\n[SUCCESS] Modified {modified_count} {language} lessons")

    print("\n" + "="*80)
    print("TUTORIAL FIXES COMPLETE")
    print("="*80)

if __name__ == "__main__":
    fix_lessons()
