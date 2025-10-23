#!/usr/bin/env python3
"""
Add proper code blocks to lessons that are missing them.
Ensures all lessons follow the same tutorial format as lessons 1-100.
"""

import json
import re

def add_code_blocks_to_system_design(lesson_id, title, tutorial, language):
    """Add code blocks to system design lessons (601-615)"""

    # If already has code blocks, return as-is
    if '<pre class="tutorial-code-block">' in tutorial:
        return tutorial

    # System design lessons should have architecture diagrams and example code
    code_examples = {
        601: """<h4 class="font-semibold text-gray-200 mb-2">Example Implementation</h4>
<pre class="tutorial-code-block">
// URL Shortener Service
class URLShortener {{
    private final Map&lt;String, String&gt; urlMap = new ConcurrentHashMap&lt;&gt;();
    private final AtomicLong counter = new AtomicLong(1000000);

    public String shortenURL(String longURL) {{
        long id = counter.incrementAndGet();
        String shortCode = encodeBase62(id);
        urlMap.put(shortCode, longURL);
        return "bit.ly/" + shortCode;
    }}

    public String expandURL(String shortCode) {{
        return urlMap.getOrDefault(shortCode, "URL not found");
    }}

    private String encodeBase62(long num) {{
        String chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        StringBuilder sb = new StringBuilder();
        while (num > 0) {{
            sb.append(chars.charAt((int)(num % 62)));
            num /= 62;
        }}
        return sb.reverse().toString();
    }}
}}
</pre>""",
        602: """<h4 class="font-semibold text-gray-200 mb-2">Example Implementation</h4>
<pre class="tutorial-code-block">
// Pastebin Service
class PastebinService {{
    private final Map&lt;String, PasteData&gt; storage = new ConcurrentHashMap&lt;&gt;();

    public String createPaste(String content, int expiryMinutes) {{
        String pasteId = generateUniqueId();
        long expiryTime = System.currentTimeMillis() + (expiryMinutes * 60000L);
        storage.put(pasteId, new PasteData(content, expiryTime));
        return "pastebin.com/" + pasteId;
    }}

    public String getPaste(String pasteId) {{
        PasteData data = storage.get(pasteId);
        if (data == null) return "Paste not found";
        if (System.currentTimeMillis() > data.expiryTime) {{
            storage.remove(pasteId);
            return "Paste expired";
        }}
        return data.content;
    }}

    private String generateUniqueId() {{
        return UUID.randomUUID().toString().substring(0, 8);
    }}

    static class PasteData {{
        String content;
        long expiryTime;
        PasteData(String content, long expiryTime) {{
            this.content = content;
            this.expiryTime = expiryTime;
        }}
    }}
}}
</pre>""",
        604: """<h4 class="font-semibold text-gray-200 mb-2">Example Implementation</h4>
<pre class="tutorial-code-block">
// Instagram Image Service
class ImageService {{
    private final S3Client s3Client;
    private final CDN cdn;

    public String uploadImage(byte[] imageData, String userId) {{
        // 1. Generate unique image ID
        String imageId = UUID.randomUUID().toString();

        // 2. Create multiple resolutions
        byte[] thumbnail = resizeImage(imageData, 150, 150);
        byte[] medium = resizeImage(imageData, 640, 640);
        byte[] large = resizeImage(imageData, 1080, 1080);

        // 3. Upload to S3
        s3Client.upload("images/" + imageId + "/thumbnail.jpg", thumbnail);
        s3Client.upload("images/" + imageId + "/medium.jpg", medium);
        s3Client.upload("images/" + imageId + "/large.jpg", large);

        // 4. Invalidate CDN cache
        cdn.invalidate("/images/" + imageId + "/*");

        // 5. Store metadata in database
        saveImageMetadata(imageId, userId);

        return imageId;
    }}

    public String getImageURL(String imageId, String size) {{
        return cdn.getURL("images/" + imageId + "/" + size + ".jpg");
    }}

    private byte[] resizeImage(byte[] data, int width, int height) {{
        // Image processing logic
        return data; // Simplified
    }}
}}
</pre>""",
        605: """<h4 class="font-semibold text-gray-200 mb-2">Example Implementation</h4>
<pre class="tutorial-code-block">
// Twitter Feed Service
class FeedService {{
    private final Map&lt;String, List&lt;Tweet&gt;&gt; userFeeds = new ConcurrentHashMap&lt;&gt;();

    public void postTweet(String userId, String content) {{
        Tweet tweet = new Tweet(generateId(), userId, content, System.currentTimeMillis());

        // Fan-out to followers' feeds
        List&lt;String&gt; followers = getFollowers(userId);
        for (String followerId : followers) {{
            userFeeds.computeIfAbsent(followerId, k -&gt; new ArrayList&lt;&gt;()).add(tweet);
        }}
    }}

    public List&lt;Tweet&gt; getFeed(String userId, int limit) {{
        List&lt;Tweet&gt; feed = userFeeds.getOrDefault(userId, new ArrayList&lt;&gt;());
        return feed.stream()
            .sorted((a, b) -&gt; Long.compare(b.timestamp, a.timestamp))
            .limit(limit)
            .collect(Collectors.toList());
    }}

    private List&lt;String&gt; getFollowers(String userId) {{
        // Query followers from database
        return new ArrayList&lt;&gt;();
    }}

    private String generateId() {{
        return String.valueOf(System.currentTimeMillis());
    }}

    static class Tweet {{
        String id, userId, content;
        long timestamp;
        Tweet(String id, String userId, String content, long timestamp) {{
            this.id = id; this.userId = userId;
            this.content = content; this.timestamp = timestamp;
        }}
    }}
}}
</pre>""",
        617: """<h4 class="font-semibold text-gray-200 mb-2">Example Implementation</h4>
<pre class="tutorial-code-block">
// Sliding Window - Maximum Sum Subarray
public class MaxSumSubarray {{
    public static int maxSum(int[] arr, int k) {{
        if (arr == null || arr.length < k) return -1;

        // Calculate sum of first window
        int windowSum = 0;
        for (int i = 0; i < k; i++) {{
            windowSum += arr[i];
        }}

        int maxSum = windowSum;

        // Slide the window
        for (int i = k; i < arr.length; i++) {{
            windowSum = windowSum - arr[i - k] + arr[i];
            maxSum = Math.max(maxSum, windowSum);
        }}

        return maxSum;
    }}

    public static void main(String[] args) {{
        int[] arr = {{2, 1, 5, 1, 3, 2}};
        int k = 3;
        System.out.println("Max sum of subarray of size " + k + ": " + maxSum(arr, k));
        // Output: 9 (subarray [5, 1, 3])
    }}
}}
</pre>"""
    }

    # Find insertion point (before "Best Practices" or similar section)
    insertion_points = [
        '<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>',
        '<h4 class="font-semibold text-gray-200 mb-2">Real-World Applications</h4>',
        '<h4 class="font-semibold text-gray-200 mb-2">Scalability',
        '<h4 class="font-semibold text-gray-200 mb-2">Interview Tips</h4>'
    ]

    code_block = code_examples.get(lesson_id, "")
    if not code_block:
        return tutorial

    # Try to insert before any of the insertion points
    for point in insertion_points:
        if point in tutorial:
            tutorial = tutorial.replace(point, code_block + '\n\n' + point)
            break

    return tutorial


def add_code_blocks_to_security(lesson_id, title, tutorial):
    """Add code blocks to security lessons (631-640)"""

    if '<pre class="tutorial-code-block">' in tutorial:
        return tutorial

    # Security lessons should show vulnerable vs secure code examples
    code_examples = {
        631: """<h4 class="font-semibold text-gray-200 mb-2">Code Examples</h4>
<pre class="tutorial-code-block">
// VULNERABLE: SQL Injection
String query = "SELECT * FROM users WHERE username='" + userInput + "'";
// Attacker input: admin'--
// Result: SELECT * FROM users WHERE username='admin'--'

// SECURE: Prepared Statement
PreparedStatement stmt = conn.prepareStatement(
    "SELECT * FROM users WHERE username=?"
);
stmt.setString(1, userInput);
ResultSet rs = stmt.executeQuery();
</pre>""",
        632: """<h4 class="font-semibold text-gray-200 mb-2">Code Examples</h4>
<pre class="tutorial-code-block">
// VULNERABLE: XSS Attack
String userComment = request.getParameter("comment");
response.getWriter().write("&lt;div&gt;" + userComment + "&lt;/div&gt;");
// Attacker input: &lt;script&gt;alert('XSS')&lt;/script&gt;

// SECURE: HTML Escaping
import org.apache.commons.text.StringEscapeUtils;

String userComment = request.getParameter("comment");
String safeComment = StringEscapeUtils.escapeHtml4(userComment);
response.getWriter().write("&lt;div&gt;" + safeComment + "&lt;/div&gt;");
// Result: &amp;lt;script&amp;gt;alert('XSS')&amp;lt;/script&amp;gt;
</pre>"""
    }

    code_block = code_examples.get(lesson_id, "")
    if not code_block:
        return tutorial

    insertion_points = [
        '<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>',
        '<h4 class="font-semibold text-gray-200 mb-2">Implementation</h4>'
    ]

    for point in insertion_points:
        if point in tutorial:
            tutorial = tutorial.replace(point, code_block + '\n\n' + point)
            break

    return tutorial


def add_code_blocks_to_soft_skills(lesson_id, title, tutorial):
    """Add code blocks to soft skills lessons (641-650)"""

    if '<pre class="tutorial-code-block">' in tutorial:
        return tutorial

    code_examples = {
        641: """<h4 class="font-semibold text-gray-200 mb-2">Code Review Checklist</h4>
<pre class="tutorial-code-block">
# Code Review Checklist
[] Functionality: Does the code do what it's supposed to?
[] Tests: Are there unit tests? Do they cover edge cases?
[] Readability: Is the code easy to understand?
[] Performance: Any obvious performance issues?
[] Security: Any security vulnerabilities?
[] Error Handling: Are errors handled gracefully?
[] Documentation: Are complex parts documented?
[] Style: Does it follow team conventions?

# Example Good Review Comment:
"Nice work! The logic is clear. One suggestion: consider adding
a null check on line 45 before calling user.getName() to prevent
NullPointerException. Also, the function could benefit from a
doc comment explaining the expected input format."
</pre>""",
        642: """<h4 class="font-semibold text-gray-200 mb-2">Documentation Examples</h4>
<pre class="tutorial-code-block">
/**
 * Calculates the nth Fibonacci number using dynamic programming.
 *
 * @param n the position in the Fibonacci sequence (must be &gt;= 0)
 * @return the nth Fibonacci number
 * @throws IllegalArgumentException if n &lt; 0
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 *
 * Example:
 *   fibonacci(5) returns 5
 *   fibonacci(10) returns 55
 */
public static long fibonacci(int n) {{
    if (n < 0) throw new IllegalArgumentException("n must be >= 0");
    if (n <= 1) return n;

    long[] dp = new long[n + 1];
    dp[0] = 0;
    dp[1] = 1;

    for (int i = 2; i <= n; i++) {{
        dp[i] = dp[i-1] + dp[i-2];
    }}

    return dp[n];
}}
</pre>""",
        643: """<h4 class="font-semibold text-gray-200 mb-2">Debugging Example</h4>
<pre class="tutorial-code-block">
// PROBLEM: Function returns wrong result
public int calculateDiscount(int price, int percent) {{
    return price * percent / 100;  // Bug: integer division
}}

// DEBUGGING STEPS:
// 1. Add print statements
System.out.println("price: " + price + ", percent: " + percent);
System.out.println("result: " + (price * percent / 100));

// 2. Use debugger breakpoint here
int discount = price * percent / 100;  // &lt;-- breakpoint
return discount;

// 3. Test with specific values
calculateDiscount(100, 15);  // Expected: 15, Got: 15 ✓
calculateDiscount(10, 15);   // Expected: 1.5, Got: 1 ✗

// SOLUTION: Use floating point
public double calculateDiscount(int price, int percent) {{
    return price * percent / 100.0;  // Fixed: 100.0 ensures float division
}}
</pre>""",
        644: """<h4 class="font-semibold text-gray-200 mb-2">Git Workflow Examples</h4>
<pre class="tutorial-code-block">
# Feature Branch Workflow
git checkout main
git pull origin main
git checkout -b feature/add-user-auth

# Make changes and commit
git add src/auth/
git commit -m "feat: Add JWT authentication for user login"

# Push and create PR
git push origin feature/add-user-auth

# After code review, merge and cleanup
git checkout main
git pull origin main
git branch -d feature/add-user-auth

# Hotfix Workflow
git checkout main
git checkout -b hotfix/critical-security-patch
# Fix bug, commit, push
git push origin hotfix/critical-security-patch
# Emergency merge after quick review
</pre>""",
        645: """<h4 class="font-semibold text-gray-200 mb-2">Profiling Example</h4>
<pre class="tutorial-code-block">
// Slow function (before profiling)
public List&lt;User&gt; getUsersWithOrders() {{
    List&lt;User&gt; users = userRepository.findAll();
    for (User user : users) {{
        user.setOrders(orderRepository.findByUserId(user.getId())); // N+1 query!
    }}
    return users;
}}

// After profiling with JProfiler/YourKit:
// - Identified N+1 query problem
// - Database calls: 1001 (1 for users + 1000 for each user's orders)
// - Time: 5000ms

// Optimized (after profiling)
public List&lt;User&gt; getUsersWithOrders() {{
    List&lt;User&gt; users = userRepository.findAllWithOrders(); // Single JOIN query
    return users;
}}

// After optimization:
// - Database calls: 1
// - Time: 50ms
// - 100x faster!
</pre>""",
        646: """<h4 class="font-semibold text-gray-200 mb-2">Reading Stack Traces</h4>
<pre class="tutorial-code-block">
// Exception Stack Trace Example
Exception in thread "main" java.lang.NullPointerException
    at com.example.UserService.getEmail(UserService.java:42)
    at com.example.EmailSender.send(EmailSender.java:18)
    at com.example.Main.main(Main.java:12)

// How to read:
// 1. Start from TOP: NullPointerException
// 2. First line is WHERE: UserService.java line 42
// 3. Follow call chain: Main -> EmailSender -> UserService
// 4. Check line 42 in UserService.java

// Code at UserService.java:42
public String getEmail(User user) {{
    return user.getEmail();  // &lt;-- line 42: user is null!
}}

// Fix: Add null check
public String getEmail(User user) {{
    if (user == null) {{
        throw new IllegalArgumentException("User cannot be null");
    }}
    return user.getEmail();
}}
</pre>""",
        647: """<h4 class="font-semibold text-gray-200 mb-2">Story Point Estimation</h4>
<pre class="tutorial-code-block">
# Story Point Scale (Fibonacci)
1 point  = 1-2 hours   (trivial: update button text)
2 points = 2-4 hours   (simple: add form validation)
3 points = 4-8 hours   (moderate: add new API endpoint)
5 points = 1-2 days    (complex: integrate payment gateway)
8 points = 2-3 days    (very complex: build analytics dashboard)
13 points = 1 week+    (epic: redesign authentication system)

# Estimation Meeting Example
Product Owner: "As a user, I want to export my data to PDF"

Team Discussion:
- Similar to CSV export we did? (That was 3 points)
- Need PDF library (+1 complexity)
- Formatting layout (+1 complexity)
- Testing with large datasets (+1 complexity)

Consensus: 5 points

# Velocity Tracking
Sprint 1: Committed 20 points, Completed 18 points
Sprint 2: Committed 22 points, Completed 20 points
Sprint 3: Committed 20 points, Completed 21 points
Average Velocity: 20 points per sprint
</pre>""",
        648: """<h4 class="font-semibold text-gray-200 mb-2">Agile/Scrum Ceremonies</h4>
<pre class="tutorial-code-block">
# Sprint Planning (Monday 9am, 2 hours)
Goal: Plan next 2-week sprint
- Review product backlog
- Select stories for sprint
- Break down stories into tasks
- Commit to sprint goal

# Daily Standup (Every day 9:30am, 15 min)
Each team member answers:
1. What did I do yesterday?
2. What will I do today?
3. Any blockers?

Example:
"Yesterday: Finished user auth API
 Today: Starting frontend integration
 Blockers: Need design mockups from UX team"

# Sprint Review (Friday 2pm, 1 hour)
- Demo completed features
- Get stakeholder feedback
- Accept/reject stories

# Sprint Retrospective (Friday 3pm, 1 hour)
What went well?
- Good code reviews
- Fast bug fixes

What can improve?
- Better documentation
- Reduce meeting times

Action items:
[] Write setup guide in README
[] Move standup to Slack async
</pre>""",
        649: """<h4 class="font-semibold text-gray-200 mb-2">Communication Examples</h4>
<pre class="tutorial-code-block">
# Stakeholder Update Email Template

Subject: Weekly Update - User Authentication Feature

Hi [Stakeholder Name],

Progress This Week:
✓ Completed JWT token implementation
✓ Added password reset functionality
⚠ Email verification in progress (80% done)

Upcoming Next Week:
- Finish email verification
- Add two-factor authentication
- Begin security testing

Risks/Blockers:
- Waiting on security team review (requested Mon, no response yet)
- May need 2 extra days if review has feedback

Metrics:
- Sprint velocity: On track (18/20 points)
- Test coverage: 85%
- Bug count: 2 (both low priority)

Questions? Happy to discuss in tomorrow's standup.

Best,
[Your Name]

# Status Update in Standup (Clear & Concise)
"Working on payment integration. Stripe API works in test mode.
 Blocker: Need production API keys from DevOps by Thursday."
</pre>""",
        650: """<h4 class="font-semibold text-gray-200 mb-2">Portfolio Project Ideas</h4>
<pre class="tutorial-code-block">
# Strong Portfolio Projects

1. Full-Stack Social Media App
   - Tech: React, Node.js, PostgreSQL, Redis
   - Features: Auth, posts, comments, real-time chat
   - Deploy: AWS/Vercel
   - GitHub: Clean code, good README, CI/CD

2. Distributed System (Advanced)
   - Tech: Java/Go, Kafka, microservices
   - Features: Load balancing, fault tolerance
   - Show: System design diagrams, metrics

3. Open Source Contribution
   - Find issue in popular project (React, VS Code, etc.)
   - Submit quality PR with tests
   - Shows: Collaboration, code review skills

# Portfolio README Template
## Project Name
Brief description (1-2 sentences)

### Features
- User authentication with JWT
- Real-time notifications via WebSockets
- RESTful API with OpenAPI docs

### Tech Stack
Frontend: React, TypeScript, Tailwind CSS
Backend: Node.js, Express, PostgreSQL
Deploy: Docker, AWS EC2, GitHub Actions

### Demo
Live: https://myproject.com
Video: https://youtube.com/demo

### Installation
```bash
git clone https://github.com/you/project
npm install
npm run dev
```

### Screenshots
[Include 2-3 screenshots]
</pre>"""
    }

    code_block = code_examples.get(lesson_id, "")
    if not code_block:
        return tutorial

    insertion_points = [
        '<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>',
        '<h4 class="font-semibold text-gray-200 mb-2">Common Pitfalls</h4>',
        '<h4 class="font-semibold text-gray-200 mb-2">Interview Tips</h4>'
    ]

    for point in insertion_points:
        if point in tutorial:
            tutorial = tutorial.replace(point, code_block + '\n\n' + point)
            break

    return tutorial


def main():
    print("=" * 70)
    print("ADDING CODE BLOCKS TO LESSONS")
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

            # Skip if already has code blocks
            if '<pre class="tutorial-code-block">' in lesson['tutorial']:
                continue

            old_len = len(lesson['tutorial'])

            # Add code blocks based on category
            if 601 <= lesson_id <= 617:
                lesson['tutorial'] = add_code_blocks_to_system_design(
                    lesson_id, lesson['title'], lesson['tutorial'], lang_name.lower()
                )
            elif 631 <= lesson_id <= 632:
                lesson['tutorial'] = add_code_blocks_to_security(
                    lesson_id, lesson['title'], lesson['tutorial']
                )
            elif 641 <= lesson_id <= 650:
                lesson['tutorial'] = add_code_blocks_to_soft_skills(
                    lesson_id, lesson['title'], lesson['tutorial']
                )

            new_len = len(lesson['tutorial'])

            if new_len > old_len:
                print(f"  [UPDATED] Lesson {lesson_id}: {lesson['title']}")
                print(f"    Tutorial: {old_len} -> {new_len} chars (+{new_len - old_len})")
                updated_count += 1

        # Save updated file
        with open(lang_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"\n[SUCCESS] {lang_name}: Updated {updated_count} lessons")

    print()
    print("=" * 70)
    print("CODE BLOCKS ADDED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == "__main__":
    main()
