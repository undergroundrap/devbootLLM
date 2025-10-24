import json

# Load existing lessons
with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

lessons = data['lessons']
new_lessons = []

#========== LESSON 661: Career Prep Guide ==========
new_lessons.append({
    "id": 661,
    "title": "Career Prep: Resume, LinkedIn & GitHub Portfolio",
    "description": "Master the job search essentials: craft a developer resume that gets past ATS systems, optimize your LinkedIn for recruiters, and build a GitHub portfolio that showcases your best work - critical for landing interviews.",
    "initialCode": """// This lesson focuses on career preparation
// Complete the checklist below to maximize your job search success

public class CareerPrep {
    public static void main(String[] args) {
        System.out.println("=== CAREER PREPARATION CHECKLIST ===\\n");

        // TODO: Complete each section below

        System.out.println("[] RESUME");
        System.out.println("  [] Use ATS-friendly format (no fancy graphics)");
        System.out.println("  [] Include technical skills section");
        System.out.println("  [] List projects with quantifiable impact");
        System.out.println("  [] Add relevant keywords for target role\\n");

        System.out.println("[] LINKEDIN");
        System.out.println("  [] Professional headshot photo");
        System.out.println("  [] Compelling headline (not just 'Software Engineer')");
        System.out.println("  [] Detailed experience with accomplishments");
        System.out.println("  [] Skills section with endorsements\\n");

        System.out.println("[] GITHUB");
        System.out.println("  [] 3-5 pinned repositories showcasing best work");
        System.out.println("  [] README files explaining each project");
        System.out.println("  [] Clean, well-documented code");
        System.out.println("  [] Contribution graph showing consistent activity\\n");

        System.out.println("WHEN COMPLETE: Update all checkmarks to [X]");
    }
}""",
    "fullSolution": """// Career Preparation - Complete Guide
// This is not a coding exercise, but a comprehensive career prep guide

public class CareerPrep {
    public static void main(String[] args) {
        System.out.println("=== CAREER PREPARATION COMPLETE ===\\n");

        System.out.println("[X] RESUME");
        System.out.println("  [X] ATS-friendly single-column format");
        System.out.println("  [X] Technical skills: Java, Python, Spring Boot, REST APIs, SQL");
        System.out.println("  [X] Projects: Todo API, Blog Platform, E-Commerce Cart");
        System.out.println("  [X] Keywords: Full-Stack, Backend, Microservices, Agile\\n");

        System.out.println("[X] LINKEDIN");
        System.out.println("  [X] Professional headshot with solid background");
        System.out.println("  [X] Headline: 'Full-Stack Developer | Java & Python | Building Scalable Web Apps'");
        System.out.println("  [X] 3+ detailed project experiences with tech stack");
        System.out.println("  [X] 15+ skills added and endorsed\\n");

        System.out.println("[X] GITHUB");
        System.out.println("  [X] Pinned: Todo REST API, Blog Auth System, Shopping Cart, Weather API, URL Shortener");
        System.out.println("  [X] Each project has comprehensive README with screenshots");
        System.out.println("  [X] Code follows best practices with comments");
        System.out.println("  [X] Green contribution graph for past 6 months\\n");

        System.out.println("\\nREADY TO APPLY FOR JOBS!");
        System.out.println("Target: Junior/Mid-Level Full-Stack Developer positions");
        System.out.println("Application goal: 10-15 quality applications per week");
    }
}""",
    "expectedOutput": """=== CAREER PREPARATION COMPLETE ===

[X] RESUME
  [X] ATS-friendly single-column format
  [X] Technical skills: Java, Python, Spring Boot, REST APIs, SQL
  [X] Projects: Todo API, Blog Platform, E-Commerce Cart
  [X] Keywords: Full-Stack, Backend, Microservices, Agile

[X] LINKEDIN
  [X] Professional headshot with solid background
  [X] Headline: 'Full-Stack Developer | Java & Python | Building Scalable Web Apps'
  [X] 3+ detailed project experiences with tech stack
  [X] 15+ skills added and endorsed

[X] GITHUB
  [X] Pinned: Todo REST API, Blog Auth System, Shopping Cart, Weather API, URL Shortener
  [X] Each project has comprehensive README with screenshots
  [X] Code follows best practices with comments
  [X] Green contribution graph for past 6 months

READY TO APPLY FOR JOBS!
Target: Junior/Mid-Level Full-Stack Developer positions
Application goal: 10-15 quality applications per week""",
    "tutorial": """<h4 class="font-semibold text-gray-200 mb-2">Overview</h4>
<p class="mb-4 text-gray-300">
You've built the technical skills - now it's time to market yourself. This lesson covers the three pillars of job search success: a resume that gets past Applicant Tracking Systems (ATS), a LinkedIn profile that attracts recruiters, and a GitHub portfolio that proves your abilities. These are non-negotiable for landing developer interviews.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Resume Best Practices</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li><strong>Format:</strong> Single-column, no tables or text boxes (ATS can't parse them). Use standard fonts (Arial, Calibri). PDF format only.</li>
<li><strong>Structure:</strong> Contact info, Technical Skills, Projects, Experience, Education. Lead with skills and projects for new developers.</li>
<li><strong>Technical Skills Section:</strong> List languages (Java, Python), frameworks (Spring Boot, React), databases (PostgreSQL, MongoDB), tools (Git, Docker, AWS). Group by category.</li>
<li><strong>Projects Section:</strong> For each project include: name, 1-line description, tech stack, and 2-3 bullet points with measurable impact. Example: "Built e-commerce shopping cart with discount system using Java, HashMap data structures, and OOP principles. Implemented inventory management preventing overselling via atomic operations."</li>
<li><strong>Keywords:</strong> Match job descriptions. If they want "RESTful APIs", use that exact phrase. If they say "Spring Framework", don't just say "Spring Boot".</li>
<li><strong>Avoid:</strong> Objective statements (waste of space), "proficient in" (just list the skills), graphics/icons, rating your skills with bars.</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">LinkedIn Optimization</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li><strong>Photo:</strong> Professional headshot, solid background, facing camera, smiling. No selfies, no group photos, no sunglasses.</li>
<li><strong>Headline:</strong> Don't just say "Software Engineer". Use: "Full-Stack Developer | Java & Python | Building Scalable Web Applications". Include your stack and what you build.</li>
<li><strong>About Section:</strong> 3-4 paragraphs. Paragraph 1: What you do. Paragraph 2: Your technical strengths. Paragraph 3: Projects you've built. Paragraph 4: What you're looking for. Write in first person, be conversational.</li>
<li><strong>Experience:</strong> Add your portfolio projects as experience. Title: "Full-Stack Developer - Personal Projects". List each project with tech stack and what it demonstrates.</li>
<li><strong>Skills:</strong> Add 15-20 skills. Prioritize: Java, Python, JavaScript, React, Spring Boot, REST APIs, SQL, Git, Docker. Get endorsements by endorsing others first.</li>
<li><strong>Activity:</strong> Share articles, comment on posts, engage with tech community. Recruiters check your activity feed.</li>
<li><strong>Set to "Open to Work":</strong> Enable this - recruiters search for it.</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">GitHub Portfolio Strategy</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li><strong>Pin Your Best Work:</strong> GitHub allows 6 pinned repos. Choose: Todo REST API, Blog Authentication System, Shopping Cart, Weather API Client, URL Shortener, and your capstone project. These showcase different skills.</li>
<li><strong>README Files:</strong> Every pinned project needs a comprehensive README with: project description, features list, tech stack, installation instructions, screenshots/GIFs, what you learned, future enhancements. Use markdown formatting.</li>
<li><strong>Code Quality:</strong> Clean, well-commented code. Follow naming conventions. Organize files logically. Remove TODO comments and console.logs before committing.</li>
<li><strong>Contribution Graph:</strong> Commit regularly (even small changes). A green graph shows you're actively coding. Aim for 4-5 commits per week minimum.</li>
<li><strong>Profile README:</strong> Create a special repo named your-username/your-username to add a profile README. Include: your tech stack, current projects, how to reach you.</li>
<li><strong>Avoid:</strong> Forked repos without modifications (doesn't show your work), half-finished projects, code with no commits in 6+ months.</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Application Strategy</h4>
<p class="mb-4 text-gray-300">
<strong>Quality over quantity.</strong> Don't spray-and-pray 100 applications. Instead: (1) Find 10-15 roles per week that match your skills, (2) Customize resume for each (add their keywords), (3) Write custom cover letter mentioning specific tech stack they use, (4) Apply directly on company website (better than job boards), (5) Follow up after 1 week via LinkedIn message to hiring manager or recruiter. Track applications in a spreadsheet: company, role, date applied, contact, status, next steps.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Common Pitfalls</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Resume over 1 page for junior roles - recruiters spend 6 seconds scanning</li>
<li>No quantifiable achievements - "built a todo app" vs "built todo REST API handling CRUD operations with authentication"</li>
<li>LinkedIn with no activity - looks like you're not serious about tech</li>
<li>GitHub with no pinned repos - recruiters won't dig through all your repos</li>
<li>Applying without customizing resume - ATS will reject you</li>
<li>Not using LinkedIn recruiter search - set "Open to Work" and add keywords</li>
<li>Waiting for perfect - ship your portfolio and iterate based on feedback</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Interview Prep Checklist</h4>
<p class="mb-4 text-gray-300">
Before applying, ensure you can: (1) Explain each portfolio project in detail - why you built it, challenges faced, how you solved them, what you'd do differently, (2) Walk through your code and explain design decisions, (3) Discuss trade-offs between different approaches, (4) Answer "Why this tech stack?" for each project, (5) Describe your development process (Git workflow, testing, deployment). Rehearse these out loud - awkward now saves embarrassment in interviews.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Timeline and Goals</h4>
<p class="mb-4 text-gray-300">
<strong>Week 1:</strong> Complete resume, get 2-3 people to review. <strong>Week 2:</strong> Optimize LinkedIn, request 20+ connections, get endorsements. <strong>Week 3:</strong> Polish GitHub README files, ensure contribution graph is green. <strong>Week 4:</strong> Start applications, 10-15 per week. <strong>Ongoing:</strong> Post on LinkedIn 2x/week, contribute to GitHub daily, respond to recruiters within 24 hours. Goal: 5-10 recruiter conversations within first month, 2-3 first-round interviews by month two.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Resources</h4>
<pre class="tutorial-code-block">
Resume Templates:
- Jake's Resume (LaTeX): github.com/jakegut/resume
- Standard Resume: standardresume.co

LinkedIn Resources:
- LinkedIn Profile Checklist: bit.ly/linkedin-dev-checklist
- Austin Belcak's LinkedIn Guide: cultivatedculture.com/linkedin-profile

GitHub Resources:
- Awesome README: github.com/matiassingers/awesome-readme
- Profile README Examples: github.com/abhisheknaiidu/awesome-github-profile-readme

Job Boards for Developers:
- LinkedIn Jobs (best for junior roles)
- Indeed (volume)
- AngelList/Wellfound (startups)
- Built In (tech hubs: SF, NY, Austin, etc.)
- Company career pages directly
</pre>

<h4 class="font-semibold text-gray-200 mb-2">Action Items</h4>
<p class="mb-4 text-gray-300">
Complete these NOW before moving to the next lesson: (1) Draft your resume using the guidelines above, (2) Update LinkedIn headline and About section, (3) Add top 3 portfolio projects to GitHub with READMEs, (4) Get at least one person to review your materials, (5) Set "Open to Work" on LinkedIn, (6) Apply to your first 5 jobs. Don't wait for perfect - launch and iterate based on feedback. The best time to start was yesterday, the second best time is now.
</p>""",
    "language": "java",
    "tags": ["Career", "Job Search", "Resume", "LinkedIn", "GitHub", "Portfolio", "Interview Prep", "Professional Development", "Job Ready"]
})

#========== LESSON 671: Interview Prep ==========
new_lessons.append({
    "id": 671,
    "title": "Interview Prep: Technical Interviews & Coding Challenges",
    "description": "Master technical interviews with the STAR method for behavioral questions, live coding strategies, whiteboard problem-solving, and how to handle questions you don't know - turn interviews into job offers.",
    "initialCode": """// Interview Preparation - Practice Template

import java.util.*;

public class InterviewPrep {
    // STEP 1: Understand the problem
    // - Restate the problem in your own words
    // - Ask clarifying questions
    // - Identify inputs, outputs, constraints

    // STEP 2: Plan your approach
    // - Think out loud
    // - Discuss brute force vs optimal solution
    // - Explain time/space complexity

    // STEP 3: Code the solution
    // - Write clean, readable code
    // - Use meaningful variable names
    // - Add comments for complex logic

    // STEP 4: Test your solution
    // - Walk through with example inputs
    // - Consider edge cases
    // - Fix bugs if found

    public static void main(String[] args) {
        // TODO: Practice with sample problem
        System.out.println("Interview Prep Template Ready");
    }
}""",
    "fullSolution": """// Interview Preparation - Complete Guide with Examples

import java.util.*;

public class InterviewPrep {
    // Example Problem: Two Sum
    // Given array of integers and target, return indices of two numbers that add to target

    public static int[] twoSum(int[] nums, int target) {
        // STEP 1: Clarifying questions asked:
        // - Can we assume exactly one solution exists? Yes
        // - Can we use the same element twice? No
        // - What if array is empty? Won't happen (given constraints)

        // STEP 2: Approach explained:
        // Brute force: Nested loops O(n^2) - check every pair
        // Optimal: HashMap O(n) - store complements as we iterate

        // STEP 3: Implementation with clear variable names
        Map<Integer, Integer> complementMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            // Check if complement exists in our map
            if (complementMap.containsKey(complement)) {
                return new int[] {complementMap.get(complement), i};
            }

            // Store current number and its index
            complementMap.put(nums[i], i);
        }

        return new int[] {}; // No solution found
    }

    // STEP 4: Test cases demonstrated
    public static void main(String[] args) {
        System.out.println("=== INTERVIEW CODING EXAMPLE ===\\n");

        // Test case 1: Normal case
        int[] nums1 = {2, 7, 11, 15};
        int target1 = 9;
        int[] result1 = twoSum(nums1, target1);
        System.out.printf("Input: %s, Target: %d\\n", Arrays.toString(nums1), target1);
        System.out.printf("Output: %s (indices of 2 and 7)\\n\\n", Arrays.toString(result1));

        // Test case 2: Edge case - first and last elements
        int[] nums2 = {3, 2, 4};
        int target2 = 6;
        int[] result2 = twoSum(nums2, target2);
        System.out.printf("Input: %s, Target: %d\\n", Arrays.toString(nums2), target2);
        System.out.printf("Output: %s (indices of 2 and 4)\\n\\n", Arrays.toString(result2));

        // Complexity analysis explained:
        System.out.println("Time Complexity: O(n) - single pass through array");
        System.out.println("Space Complexity: O(n) - HashMap stores up to n elements");

        System.out.println("\\n=== READY FOR TECHNICAL INTERVIEWS ===");
    }
}""",
    "expectedOutput": """=== INTERVIEW CODING EXAMPLE ===

Input: [2, 7, 11, 15], Target: 9
Output: [0, 1] (indices of 2 and 7)

Input: [3, 2, 4], Target: 6
Output: [1, 2] (indices of 2 and 4)

Time Complexity: O(n) - single pass through array
Space Complexity: O(n) - HashMap stores up to n elements

=== READY FOR TECHNICAL INTERVIEWS ===""",
    "tutorial": """<h4 class="font-semibold text-gray-200 mb-2">Overview</h4>
<p class="mb-4 text-gray-300">
Technical interviews test both your coding ability and communication skills. This lesson covers the complete interview process: behavioral questions using STAR method, live coding strategies, whiteboard problem-solving, handling questions you don't know, and what interviewers actually look for. Master these and you'll turn interviews into offers.
</p>

<h4 class="font-semibold text-gray-200 mb-2">The STAR Method (Behavioral Questions)</h4>
<p class="mb-4 text-gray-300">
Every behavioral question follows this format: <strong>Situation</strong> (context), <strong>Task</strong> (your responsibility), <strong>Action</strong> (what you did), <strong>Result</strong> (outcome with numbers). Common questions: "Tell me about a challenging bug you fixed", "Describe a time you disagreed with a teammate", "What's your proudest project?". Prepare 3-5 stories from your portfolio projects that demonstrate: problem-solving, learning new tech, overcoming obstacles, collaboration, making trade-off decisions.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Live Coding: The 4-Step Process</h4>
<pre class="tutorial-code-block">
STEP 1: UNDERSTAND (2-3 minutes)
- Restate problem in your own words
- Ask clarifying questions:
  * What are the inputs/outputs?
  * Any constraints (time, memory)?
  * Edge cases to consider?
  * Can I assume inputs are valid?
- Write down examples on whiteboard

STEP 2: PLAN (3-5 minutes)
- Think out loud - they're evaluating your thought process
- Discuss brute force approach first
- Then optimize: "This is O(n^2), can we do better with a HashMap?"
- Explain time/space complexity before coding
- Ask: "Does this approach sound good?"

STEP 3: CODE (15-20 minutes)
- Start coding only after interviewer approves approach
- Write clean, readable code (not competition-style shortcuts)
- Use meaningful variable names (not a, b, c)
- Add comments for complex logic
- Talk through what you're doing as you code
- Don't go silent for 10 minutes - communicate constantly

STEP 4: TEST (5 minutes)
- Walk through code with example input
- Test edge cases: empty array, single element, duplicates, negatives
- If you find a bug, don't panic - fix it calmly
- Mention additional test cases you'd add in production
- Discuss how you'd handle the bug in real codebase
</pre>

<h4 class="font-semibold text-gray-200 mb-2">Common Coding Patterns</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li><strong>Two Pointers:</strong> Used for sorted arrays, finding pairs. Example: Two Sum in sorted array.</li>
<li><strong>HashMap/HashSet:</strong> Fast lookups, counting occurrences, finding complements. Example: Two Sum, First Unique Character.</li>
<li><strong>Sliding Window:</strong> Subarray/substring problems. Example: Longest substring without repeating characters.</li>
<li><strong>BFS/DFS:</strong> Tree and graph traversal. Example: Level order traversal, finding connected components.</li>
<li><strong>Dynamic Programming:</strong> Optimization problems with overlapping subproblems. Example: Fibonacci, Longest Common Subsequence.</li>
<li><strong>Binary Search:</strong> Finding elements in sorted data. Example: Search in rotated sorted array.</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Handling Unknown Questions</h4>
<p class="mb-4 text-gray-300">
<strong>When stuck, don't freeze.</strong> Interviewers care more about problem-solving process than perfect solutions. If you don't know: (1) Say what you DO know - "I haven't solved this exact problem, but it reminds me of X which uses Y approach", (2) Start with brute force - "I can solve this in O(n^2) with nested loops, let me code that first", (3) Ask for hints - "I'm thinking a HashMap might help here, am I on the right track?", (4) Think out loud - show your debugging process, (5) Never lie or pretend to know something you don't - honesty > ego. Remember: they're looking for how you approach unfamiliar problems, not memorized solutions.
</p>

<h4 class="font-semibold text-gray-200 mb-2">What Interviewers Evaluate</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li><strong>Problem-Solving:</strong> Can you break down complex problems into manageable steps?</li>
<li><strong>Communication:</strong> Do you explain your thinking clearly? Ask good questions?</li>
<li><strong>Coding Skills:</strong> Clean, readable code with meaningful names and proper structure.</li>
<li><strong>Debugging:</strong> When you find a bug, can you systematically fix it?</li>
<li><strong>Trade-offs:</strong> Do you understand when to optimize vs when "good enough" is fine?</li>
<li><strong>Collaboration:</strong> Are you pleasant to work with? Do you take feedback well?</li>
<li><strong>Growth Mindset:</strong> Do you learn from hints? Admit when you don't know something?</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">System Design Questions (Mid/Senior)</h4>
<p class="mb-4 text-gray-300">
For mid-level roles, expect 1-2 system design questions: "Design Twitter", "Design URL Shortener", "Design Rate Limiter". Framework: (1) <strong>Requirements:</strong> Clarify functional vs non-functional requirements, scale (users, requests/sec), (2) <strong>High-Level Design:</strong> Draw boxes for major components (API, database, cache), (3) <strong>Deep Dive:</strong> Pick 2-3 components to detail (database schema, API endpoints, caching strategy), (4) <strong>Scalability:</strong> Discuss bottlenecks and how to scale (load balancing, database sharding, caching layers). Leverage your portfolio projects - "In my URL Shortener project, I used X approach for Y reason."
</p>

<h4 class="font-semibold text-gray-200 mb-2">Common Pitfalls</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Starting to code immediately without understanding problem - slow down, ask questions first</li>
<li>Going silent while coding - interviewers can't read your mind, narrate your thinking</li>
<li>Not testing your code - always walk through with examples, even if time is tight</li>
<li>Giving up when stuck - show your problem-solving process, ask for hints</li>
<li>Memorizing LeetCode solutions - interviewers can tell, focus on understanding patterns</li>
<li>Not asking clarifying questions - shows poor communication and assumptions</li>
<li>Optimizing too early - get a working solution first, then optimize</li>
<li>Bad-mouthing previous employers/teams in behavioral questions - stay professional</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Practice Resources</h4>
<pre class="tutorial-code-block">
Coding Practice:
- LeetCode: Start with Easy, move to Medium (focus on Top 150 Interview Questions)
- HackerRank: Good for beginners, has tutorials
- AlgoExpert: Paid but excellent video explanations
- Pramp: Free mock interviews with peers

Study Guides:
- "Cracking the Coding Interview" by Gayle McDowell (bible for interviews)
- "Grokking the Coding Interview" course (pattern-based learning)
- NeetCode 150 (curated LeetCode list with video solutions)

System Design:
- "Designing Data-Intensive Applications" by Martin Kleppmann
- "System Design Interview" by Alex Xu
- YouTube: System Design Interview channel

Behavioral Prep:
- Write out 5 STAR stories from your portfolio projects
- Practice speaking them out loud (sounds different than writing)
- Record yourself - check for filler words, pace, clarity
</pre>

<h4 class="font-semibold text-gray-200 mb-2">Interview Day Tips</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li><strong>Before:</strong> Get 8 hours sleep, eat a good meal, test your webcam/mic, have water nearby, use bathroom right before.</li>
<li><strong>During:</strong> Smile, make eye contact (camera), speak clearly, if you need a moment to think say "Let me think through this for 30 seconds", ask if you can take notes.</li>
<li><strong>After:</strong> Send thank-you email within 24 hours mentioning something specific from the conversation, ask about next steps and timeline.</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Action Items</h4>
<p class="mb-4 text-gray-300">
Complete these before your first interview: (1) Solve 20 Easy and 10 Medium LeetCode problems covering different patterns, (2) Write out 5 STAR stories from your portfolio projects, (3) Do 3 mock interviews with friends or Pramp, (4) Practice explaining your portfolio projects out loud for 5 minutes each, (5) Review your resume and be ready to discuss every bullet point in detail. The difference between a good candidate and a great one is preparation - put in the work.
</p>""",
    "language": "java",
    "tags": ["Interview Prep", "Coding Challenges", "STAR Method", "Live Coding", "Behavioral Questions", "Technical Interviews", "Career", "Job Ready", "FAANG"]
})

#========== LESSON 681: Debugging Challenge ==========
new_lessons.append({
    "id": 681,
    "title": "Debug Challenge: Fix Production Bugs",
    "description": "Practice real-world debugging skills by fixing 5 production-like bugs: null pointer exceptions, off-by-one errors, race conditions, memory leaks, and logic errors - essential for passing take-home assignments.",
    "initialCode": """import java.util.*;

// DEBUGGING CHALLENGE: Fix all 5 bugs below

public class DebugChallenge {
    // BUG 1: Null Pointer Exception
    public static int getListSize(List<String> items) {
        return items.size();  // What if items is null?
    }

    // BUG 2: Off-by-One Error
    public static int[] getFirstThree(int[] arr) {
        int[] result = new int[3];
        for (int i = 0; i <= 3; i++) {  // ArrayIndexOutOfBounds
            result[i] = arr[i];
        }
        return result;
    }

    // BUG 3: Logic Error
    public static boolean isPalindrome(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != s.charAt(s.length() - i)) {  // Wrong index
                return false;
            }
        }
        return true;
    }

    // BUG 4: Resource Leak
    public static String readFile(String filename) {
        Scanner scanner = new Scanner(System.in);
        // File is never closed - memory leak
        return scanner.nextLine();
    }

    // BUG 5: Integer Overflow
    public static int multiply(int a, int b) {
        return a * b;  // Can overflow for large values
    }

    public static void main(String[] args) {
        // TODO: Test each method and fix the bugs
        System.out.println("Debug Challenge - Fix all bugs!");
    }
}""",
    "fullSolution": """import java.util.*;

// DEBUGGING CHALLENGE: All bugs fixed with explanations

public class DebugChallenge {
    // BUG 1 FIXED: Null Pointer Exception
    public static int getListSize(List<String> items) {
        if (items == null) {  // Defensive programming
            return 0;
        }
        return items.size();
    }

    // BUG 2 FIXED: Off-by-One Error
    public static int[] getFirstThree(int[] arr) {
        if (arr == null || arr.length < 3) {
            throw new IllegalArgumentException("Array must have at least 3 elements");
        }
        int[] result = new int[3];
        for (int i = 0; i < 3; i++) {  // Changed <= to <
            result[i] = arr[i];
        }
        return result;
    }

    // BUG 3 FIXED: Logic Error
    public static boolean isPalindrome(String s) {
        if (s == null || s.isEmpty()) return true;

        for (int i = 0; i < s.length() / 2; i++) {
            // Fixed: s.length() - 1 - i (not s.length() - i)
            if (s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }

    // BUG 4 FIXED: Resource Leak
    public static String readFile(String filename) {
        try (Scanner scanner = new Scanner(System.in)) {  // Try-with-resources
            if (scanner.hasNextLine()) {
                return scanner.nextLine();
            }
        } // Scanner automatically closed
        return "";
    }

    // BUG 5 FIXED: Integer Overflow
    public static long multiply(int a, int b) {
        return (long) a * b;  // Cast to long to prevent overflow
    }

    public static void main(String[] args) {
        System.out.println("=== DEBUGGING CHALLENGE - ALL BUGS FIXED ===\\n");

        // Test 1: Null check
        System.out.println("Test 1 - Null list size: " + getListSize(null));
        System.out.println("Test 1 - Normal list: " + getListSize(Arrays.asList("a", "b", "c")));

        // Test 2: Off-by-one
        int[] arr = {1, 2, 3, 4, 5};
        int[] first3 = getFirstThree(arr);
        System.out.println("\\nTest 2 - First three: " + Arrays.toString(first3));

        // Test 3: Palindrome
        System.out.println("\\nTest 3 - 'racecar' is palindrome: " + isPalindrome("racecar"));
        System.out.println("Test 3 - 'hello' is palindrome: " + isPalindrome("hello"));

        // Test 4: Resource management (no visible output, but fixed leak)
        System.out.println("\\nTest 4 - Resource management fixed (no memory leak)");

        // Test 5: Overflow
        long result = multiply(100000, 100000);
        System.out.println("\\nTest 5 - 100000 * 100000 = " + result);
        System.out.println("(Would overflow as int: " + (100000 * 100000) + ")");

        System.out.println("\\n=== ALL TESTS PASSED ===");
    }
}""",
    "expectedOutput": """=== DEBUGGING CHALLENGE - ALL BUGS FIXED ===

Test 1 - Null list size: 0
Test 1 - Normal list: 3

Test 2 - First three: [1, 2, 3]

Test 3 - 'racecar' is palindrome: true
Test 3 - 'hello' is palindrome: false

Test 4 - Resource management fixed (no memory leak)

Test 5 - 100000 * 100000 = 10000000000
(Would overflow as int: 1410065408)

=== ALL TESTS PASSED ===""",
    "tutorial": """<h4 class="font-semibold text-gray-200 mb-2">Overview</h4>
<p class="mb-4 text-gray-300">
Debugging is 50% of a developer's job, yet most coding bootcamps don't teach it systematically. This challenge covers the 5 most common production bugs: null pointers, off-by-one errors, logic mistakes, resource leaks, and integer overflow. Master these patterns and you'll debug faster than 80% of developers.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Bug Patterns Explained</h4>
<pre class="tutorial-code-block">
1. NULL POINTER EXCEPTIONS
- Most common bug in production
- Always validate inputs: if (obj == null) return default
- Use Optional<T> in Java to make nullability explicit
- Null checks cost nothing compared to crashed servers

2. OFF-BY-ONE ERRORS
- Loop bounds: use < length (not <= length)
- Array indexing: valid range is 0 to length-1
- String indexing: s.charAt(s.length() - 1) for last char
- Test with: empty arrays, single element, boundaries

3. LOGIC ERRORS
- Most subtle bug type - code runs but gives wrong results
- Debugging strategy: add print statements to trace execution
- Verify assumptions: "I think X happens here" -> prove it
- Use debugger breakpoints to step through code

4. RESOURCE LEAKS
- Files, database connections, network sockets must be closed
- Use try-with-resources in Java (auto-closes)
- Python: use 'with' statement
- Memory leaks crash servers over time - hard to debug

5. INTEGER OVERFLOW
- int max value: 2,147,483,647
- Multiplying two ints can exceed this
- Solution: cast to long before operation
- In production: use BigInteger for money calculations
</pre>

<h4 class="font-semibold text-gray-200 mb-2">Debugging Process</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li><strong>Step 1 - Reproduce:</strong> Can you make the bug happen consistently? If not, it's a race condition or environment-specific.</li>
<li><strong>Step 2 - Isolate:</strong> Binary search the code - comment out half, see if bug persists. Narrow down to specific function.</li>
<li><strong>Step 3 - Hypothesize:</strong> What do you think is wrong? State it explicitly: "I think the loop index is wrong because..."</li>
<li><strong>Step 4 - Test:</strong> Add logging/print statements to verify hypothesis. Use debugger to step through line-by-line.</li>
<li><strong>Step 5 - Fix:</strong> Make smallest change possible. Don't rewrite everything.</li>
<li><strong>Step 6 - Verify:</strong> Test the fix with original failing case PLUS edge cases. Make sure you didn't introduce new bugs.</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Debugging Tools</h4>
<pre class="tutorial-code-block">
Print Statements (Universal):
System.out.println("DEBUG: value = " + value);
- Quick and dirty, works everywhere
- Use unique prefixes like "DEBUG:" to find/remove later

IDE Debugger (Professional):
- Set breakpoints on suspicious lines
- Step through code line-by-line (F10 in most IDEs)
- Inspect variable values at each step
- Watch expressions to track specific values

Stack Traces (Exception Handling):
- Read from bottom to top (shows call chain)
- Line numbers tell you exactly where crash happened
- Google the exception type + language for solutions

Logging Frameworks:
- log.debug(), log.info(), log.error()
- Can enable/disable by severity level
- Stays in code permanently (unlike print statements)
</pre>

<h4 class="font-semibold text-gray-200 mb-2">Common Pitfalls</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Assuming code works without testing edge cases</li>
<li>Not reading error messages carefully - they often tell you exactly what's wrong</li>
<li>Changing multiple things at once - then you don't know what fixed it</li>
<li>Not using version control - can't roll back bad changes</li>
<li>Debugging by random code changes hoping something works</li>
<li>Not taking breaks - fresh eyes spot bugs immediately</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Interview Relevance</h4>
<p class="mb-4 text-gray-300">
Many take-home assignments intentionally include bugs to test your debugging skills. When you find a bug: (1) Document it clearly in comments, (2) Explain WHY it was a bug, (3) Show the fix, (4) Add a test case that would have caught it. This proves you think like a senior developer. In live interviews, if your code doesn't work, methodically debug it - interviewers are watching your process, not expecting perfect code on first try.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Action Items</h4>
<p class="mb-4 text-gray-300">
Practice debugging daily: (1) Solve LeetCode problems then intentionally break them and fix, (2) Review your portfolio projects for potential bugs, (3) Add defensive checks to all methods (null validation, bounds checking), (4) Learn your IDE's debugger (spend 30 min watching tutorial), (5) Read stack traces from your old projects and understand them fully.
</p>""",
    "language": "java",
    "tags": ["Debugging", "Bug Fixing", "Error Handling", "Best Practices", "Production Code", "Testing", "Career", "Job Ready"]
})

#========== LESSON 691: Code Review ==========
new_lessons.append({
    "id": 691,
    "title": "Code Review: Professional Standards & Best Practices",
    "description": "Learn how to review code like a senior developer: identify code smells, suggest improvements, give constructive feedback, and write review-ready code - critical for team collaboration and passing code reviews.",
    "initialCode": """// CODE REVIEW EXERCISE
// Review the code below and identify issues

import java.util.*;

public class UserService {
    public static ArrayList GetUsers() {  // Issues?
        ArrayList users = new ArrayList();  // Issues?
        users.add("john");
        users.add("jane");
        return users;
    }

    public static void ProcessUser(String u) {  // Issues?
        if(u!=null){  // Issues?
            System.out.println(u);
        }
    }

    public static void main(String[] args) {
        ArrayList users=GetUsers();  // Issues?
        for(int i=0;i<users.size();i++){  // Issues?
            ProcessUser((String)users.get(i));
        }
    }
}

// TODO: List all code review comments
// TODO: Refactor to professional standards""",
    "fullSolution": r"""// CODE REVIEW: Professional refactored version

import java.util.*;

/**
 * Service class for managing user operations.
 * Demonstrates professional coding standards and best practices.
 */
public class UserService {
    /**
     * Retrieves all users from the system.
     * @return List of usernames
     */
    public static List<String> getUsers() {
        // Use List interface, not ArrayList implementation
        // Use diamond operator for type inference
        List<String> users = new ArrayList<>();
        users.add("john");
        users.add("jane");
        return users;
    }

    /**
     * Processes a single user by printing their username.
     * @param username the username to process (must not be null)
     */
    public static void processUser(String username) {
        // Validate input with meaningful error
        if (username == null || username.trim().isEmpty()) {
            throw new IllegalArgumentException("Username cannot be null or empty");
        }

        // In production, this would do actual processing
        System.out.println("Processing user: " + username);
    }

    public static void main(String[] args) {
        // Retrieve users
        List<String> users = getUsers();

        // Use enhanced for loop (cleaner than index loop)
        for (String user : users) {
            processUser(user);
        }
    }
}

/*
CODE REVIEW COMMENTS:

1. Method naming: GetUsers() -> getUsers()
   - Java convention: camelCase for methods
   - Uppercase reserved for class names

2. Return type: ArrayList -> List<String>
   - Return interface, not implementation
   - Allows swapping ArrayList for LinkedList later
   - Always use generics (List<String>, not raw List)

3. Variable naming: u -> username
   - Use descriptive names, not abbreviations
   - Code is read 10x more than written

4. Spacing: if(u!=null) -> if (username == null)
   - Add spaces around operators for readability
   - Use positive conditions when possible

5. Type safety: Remove (String) cast
   - Use generics to avoid runtime casts
   - Casts are code smells indicating poor type design

6. Loop style: for(int i...) -> for (String user : users)
   - Enhanced for loop is cleaner and less error-prone
   - No index management, no get() calls

7. Documentation: Add Javadoc comments
   - Every public method needs /** comment explaining purpose
   - Include @param and @return tags

8. Error handling: Validate inputs properly
   - Don't just check null - also check empty strings
   - Throw meaningful exceptions with context
*/""",
    "expectedOutput": """Processing user: john
Processing user: jane""",
    "tutorial": """<h4 class="font-semibold text-gray-200 mb-2">Overview</h4>
<p class="mb-4 text-gray-300">
Code reviews are where junior developers become senior developers. This lesson teaches you how to review code professionally: spot code smells, suggest improvements diplomatically, understand what reviewers look for, and write review-ready code that gets approved quickly. Essential for team environments and open-source contributions.
</p>

<h4 class="font-semibold text-gray-200 mb-2">What to Look For in Code Reviews</h4>
<pre class="tutorial-code-block">
READABILITY (30% of review time):
- Meaningful variable/method names (username vs u, calculateTotal vs ct)
- Consistent formatting (spaces, indentation, brace style)
- Comments explaining WHY, not WHAT
- Reasonable method/class length (< 50 lines per method)

CORRECTNESS (40% of review time):
- Does it solve the actual problem?
- Edge cases handled (null, empty, boundary values)?
- No obvious bugs (off-by-one, null pointers, race conditions)?
- Error handling present and meaningful?

DESIGN (20% of review time):
- Using right data structures (HashMap vs List)?
- Code reuse vs duplication?
- Separation of concerns (logic separate from presentation)?
- Return interfaces, not implementations (List vs ArrayList)?

PERFORMANCE (10% of review time):
- O(n) vs O(n^2) algorithm choices?
- Unnecessary loops or database calls?
- Memory leaks (resources not closed)?
- Only optimize if profiling shows it matters
</pre>

<h4 class="font-semibold text-gray-200 mb-2">Code Smells to Watch For</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li><strong>Magic Numbers:</strong> Use constants. Bad: if (status == 200), Good: if (status == HTTP_OK)</li>
<li><strong>God Classes:</strong> Classes doing too much. UserService shouldn't also handle email, database, and logging.</li>
<li><strong>Deep Nesting:</strong> More than 3 levels of if/for statements. Extract methods or use early returns.</li>
<li><strong>Commented Code:</strong> Delete it. Version control remembers everything.</li>
<li><strong>Long Parameter Lists:</strong> More than 3-4 params? Create a parameter object.</li>
<li><strong>Primitive Obsession:</strong> Using String for everything. Create Email, Phone, Address classes.</li>
<li><strong>Inconsistent Naming:</strong> getUser() in one place, FetchUser() in another. Pick one convention.</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">How to Give Feedback</h4>
<p class="mb-4 text-gray-300">
<strong>Be kind and constructive.</strong> Your goal is to improve code, not demoralize teammates. Framework: (1) <strong>Start positive:</strong> "Nice use of HashMap for O(1) lookups", (2) <strong>Ask questions:</strong> "Could we use Stream API here for readability?" vs "This loop is wrong", (3) <strong>Explain WHY:</strong> "Let's return List<T> instead of ArrayList<T> so we can swap implementations later", (4) <strong>Suggest, don't demand:</strong> "Consider extracting this to a helper method" vs "Extract this now", (5) <strong>Link to resources:</strong> "Here's a great article on why X pattern is preferred". Remember: you're reviewing code, not people.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Writing Review-Ready Code</h4>
<pre class="tutorial-code-block">
BEFORE SUBMITTING PR:
[] Run linter/formatter (Checkstyle for Java, Black for Python)
[] All tests pass locally
[] No commented-out code
[] No console.log() or System.out.println() debug statements
[] Javadoc/docstrings on all public methods
[] Descriptive commit messages ("Fix null pointer in user lookup")
[] PR description explains WHAT changed and WHY

SELF-REVIEW CHECKLIST:
[] Would I approve this if someone else wrote it?
[] Is every variable/method name clear?
[] Are edge cases tested?
[] Is there duplicated code I could extract?
[] Did I follow team conventions?
[] Would I be proud to have this in production?
</pre>

<h4 class="font-semibold text-gray-200 mb-2">Common Review Comments Explained</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li><strong>"LGTM" (Looks Good To Me):</strong> Approval to merge</li>
<li><strong>"Nit: ...":</strong> Minor issue, not blocking merge</li>
<li><strong>"Blocking: ...":</strong> Must fix before approval</li>
<li><strong>"Consider: ...":</strong> Suggestion, not requirement</li>
<li><strong>"DRY violation":</strong> Don't Repeat Yourself - duplicated code</li>
<li><strong>"YAGNI":</strong> You Aren't Gonna Need It - over-engineering</li>
<li><strong>"KISS":</strong> Keep It Simple, Stupid - unnecessarily complex</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Handling Feedback</h4>
<p class="mb-4 text-gray-300">
When your code is reviewed: (1) Don't take it personally - everyone's code gets reviewed, (2) Ask questions if feedback unclear - "Can you explain what you mean by X?", (3) Push back respectfully if you disagree - "I chose ArrayList here because we need index access performance", (4) Thank reviewers - "Great catch on that edge case!", (5) Learn from patterns - if 3 people mention naming, improve your naming game. Senior developers WANT their code reviewed - fresh eyes catch bugs and suggest better approaches.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Interview Relevance</h4>
<p class="mb-4 text-gray-300">
In pair programming interviews, interviewers are evaluating: (1) How you react to feedback - defensive or collaborative?, (2) Your code quality before they even mention it, (3) Whether you ask for review at appropriate times, (4) If you give feedback respectfully when reviewing their suggested changes. Many companies have dedicated "code review" rounds where you review sample code - use the frameworks from this lesson.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Action Items</h4>
<p class="mb-4 text-gray-300">
Practice code review skills: (1) Review your own portfolio projects with the checklist above, (2) Contribute to open source and study how maintainers give feedback, (3) Practice giving code review comments on sample code (CodeMentor, Exercism), (4) Set up a linter/formatter in your IDE and use it religiously, (5) Read "Clean Code" by Robert Martin - the code review bible.
</p>""",
    "language": "java",
    "tags": ["Code Review", "Best Practices", "Clean Code", "Professional Development", "Team Collaboration", "Code Quality", "Career", "Job Ready"]
})

#========== LESSON 695: Final Capstone ==========
new_lessons.append({
    "id": 695,
    "title": "Final Capstone: Task Management System",
    "description": "Build a complete task management system combining all skills learned: user authentication, CRUD operations, priority sorting, deadline tracking, and search - your ultimate portfolio showcase piece.",
    "initialCode": """import java.util.*;
import java.time.*;

// FINAL CAPSTONE: Task Management System
// Combines: Authentication, CRUD, Search, Sorting, Date handling

// TODO: Implement User class with authentication
// TODO: Implement Task class with title, description, priority, deadline
// TODO: Implement TaskManager with CRUD operations
// TODO: Add search by keyword and filter by priority
// TODO: Add deadline reminders (tasks due soon)

public class Main {
    public static void main(String[] args) {
        System.out.println("Final Capstone: Task Management System");
        // TODO: Build complete system
    }
}""",
    "fullSolution": r"""import java.util.*;
import java.time.*;
import java.time.format.*;

class User {
    private final String username;
    private final String passwordHash;

    public User(String username, String password) {
        this.username = username;
        this.passwordHash = hashPassword(password);
    }

    private String hashPassword(String password) {
        return Integer.toHexString(password.hashCode());
    }

    public boolean authenticate(String password) {
        return this.passwordHash.equals(hashPassword(password));
    }

    public String getUsername() { return username; }
}

class Task {
    private static int nextId = 1;
    private final int id;
    private String title;
    private String description;
    private String priority;  // HIGH, MEDIUM, LOW
    private LocalDate deadline;
    private boolean completed;
    private final LocalDateTime createdAt;

    public Task(String title, String description, String priority, LocalDate deadline) {
        this.id = nextId++;
        this.title = title;
        this.description = description;
        this.priority = priority;
        this.deadline = deadline;
        this.completed = false;
        this.createdAt = LocalDateTime.now();
    }

    // Getters and setters
    public int getId() { return id; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getPriority() { return priority; }
    public void setPriority(String priority) { this.priority = priority; }
    public LocalDate getDeadline() { return deadline; }
    public void setDeadline(LocalDate deadline) { this.deadline = deadline; }
    public boolean isCompleted() { return completed; }
    public void setCompleted(boolean completed) { this.completed = completed; }

    public long getDaysUntilDeadline() {
        return LocalDate.now().until(deadline).getDays();
    }

    public boolean isDueSoon() {
        long days = getDaysUntilDeadline();
        return days >= 0 && days <= 3;
    }

    @Override
    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MMM dd, yyyy");
        String status = completed ? "[DONE]" : "[TODO]";
        String urgent = isDueSoon() && !completed ? " !!!" : "";
        return String.format("#%d %s [%s] %s - Due: %s%s",
            id, status, priority, title, deadline.format(formatter), urgent);
    }
}

class TaskManager {
    private final Map<Integer, Task> tasks;
    private final User currentUser;

    public TaskManager(User user) {
        this.tasks = new HashMap<>();
        this.currentUser = user;
    }

    public Task createTask(String title, String desc, String priority, LocalDate deadline) {
        Task task = new Task(title, desc, priority, deadline);
        tasks.put(task.getId(), task);
        System.out.println("Created task #" + task.getId());
        return task;
    }

    public Task getTask(int id) {
        return tasks.get(id);
    }

    public void updateTask(int id, String title, String desc, String priority, LocalDate deadline) {
        Task task = tasks.get(id);
        if (task != null) {
            task.setTitle(title);
            task.setDescription(desc);
            task.setPriority(priority);
            task.setDeadline(deadline);
            System.out.println("Updated task #" + id);
        }
    }

    public void deleteTask(int id) {
        tasks.remove(id);
        System.out.println("Deleted task #" + id);
    }

    public void completeTask(int id) {
        Task task = tasks.get(id);
        if (task != null) {
            task.setCompleted(true);
            System.out.println("Completed task #" + id);
        }
    }

    public List<Task> search(String keyword) {
        return tasks.values().stream()
            .filter(t -> t.getTitle().toLowerCase().contains(keyword.toLowerCase()) ||
                        t.getDescription().toLowerCase().contains(keyword.toLowerCase()))
            .toList();
    }

    public List<Task> filterByPriority(String priority) {
        return tasks.values().stream()
            .filter(t -> t.getPriority().equals(priority))
            .toList();
    }

    public List<Task> getUpcomingDeadlines() {
        return tasks.values().stream()
            .filter(t -> !t.isCompleted() && t.getDaysUntilDeadline() <= 7)
            .sorted(Comparator.comparing(Task::getDeadline))
            .toList();
    }

    public void listAllTasks() {
        System.out.println("\n=== ALL TASKS ===");
        if (tasks.isEmpty()) {
            System.out.println("No tasks yet");
        } else {
            tasks.values().stream()
                .sorted(Comparator.comparing(Task::getDeadline))
                .forEach(System.out::println);
        }
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== TASK MANAGEMENT SYSTEM ===\n");

        // Authentication
        User user = new User("john", "password123");
        System.out.println("User created: " + user.getUsername());
        System.out.println("Auth test: " + user.authenticate("password123") + "\n");

        // Create task manager
        TaskManager manager = new TaskManager(user);

        // Create tasks
        System.out.println("--- Creating Tasks ---");
        manager.createTask("Complete capstone project", "Finish final lesson", "HIGH",
            LocalDate.now().plusDays(2));
        manager.createTask("Review Java concepts", "Go through all 650 lessons", "MEDIUM",
            LocalDate.now().plusDays(7));
        manager.createTask("Apply to jobs", "Send 10 applications", "HIGH",
            LocalDate.now().plusDays(1));
        manager.createTask("Learn Docker", "Complete Docker tutorial", "LOW",
            LocalDate.now().plusDays(14));

        // List all tasks
        manager.listAllTasks();

        // Search
        System.out.println("--- Search Results for 'java' ---");
        manager.search("java").forEach(System.out::println);

        // Filter by priority
        System.out.println("\n--- HIGH Priority Tasks ---");
        manager.filterByPriority("HIGH").forEach(System.out::println);

        // Upcoming deadlines
        System.out.println("\n--- Upcoming Deadlines (next 7 days) ---");
        manager.getUpcomingDeadlines().forEach(System.out::println);

        // Complete a task
        System.out.println("\n--- Completing Task #1 ---");
        manager.completeTask(1);
        manager.listAllTasks();

        // Update a task
        System.out.println("--- Updating Task #2 ---");
        manager.updateTask(2, "Review Java & Python", "Review all concepts", "HIGH",
            LocalDate.now().plusDays(5));
        manager.listAllTasks();

        // Statistics
        long total = manager.tasks.size();
        long completed = manager.tasks.values().stream().filter(Task::isCompleted).count();
        System.out.println("=== STATISTICS ===");
        System.out.println("Total tasks: " + total);
        System.out.println("Completed: " + completed);
        System.out.println("Remaining: " + (total - completed));
    }
}""",
    "expectedOutput": """=== TASK MANAGEMENT SYSTEM ===

User created: john
Auth test: true

--- Creating Tasks ---
Created task #1
Created task #2
Created task #3
Created task #4

=== ALL TASKS ===
#3 [TODO] [HIGH] Apply to jobs - Due: Oct 24, 2025 !!!
#1 [TODO] [HIGH] Complete capstone project - Due: Oct 25, 2025 !!!
#2 [TODO] [MEDIUM] Review Java concepts - Due: Oct 30, 2025
#4 [TODO] [LOW] Learn Docker - Due: Nov 06, 2025

--- Search Results for 'java' ---
#2 [TODO] [MEDIUM] Review Java concepts - Due: Oct 30, 2025

--- HIGH Priority Tasks ---
#3 [TODO] [HIGH] Apply to jobs - Due: Oct 24, 2025 !!!
#1 [TODO] [HIGH] Complete capstone project - Due: Oct 25, 2025 !!!

--- Upcoming Deadlines (next 7 days) ---
#3 [TODO] [HIGH] Apply to jobs - Due: Oct 24, 2025 !!!
#1 [TODO] [HIGH] Complete capstone project - Due: Oct 25, 2025 !!!
#2 [TODO] [MEDIUM] Review Java concepts - Due: Oct 30, 2025

--- Completing Task #1 ---
Completed task #1

=== ALL TASKS ===
#3 [TODO] [HIGH] Apply to jobs - Due: Oct 24, 2025 !!!
#1 [DONE] [HIGH] Complete capstone project - Due: Oct 25, 2025
#2 [TODO] [MEDIUM] Review Java concepts - Due: Oct 30, 2025
#4 [TODO] [LOW] Learn Docker - Due: Nov 06, 2025

--- Updating Task #2 ---
Updated task #2

=== ALL TASKS ===
#3 [TODO] [HIGH] Apply to jobs - Due: Oct 24, 2025 !!!
#1 [DONE] [HIGH] Complete capstone project - Due: Oct 25, 2025
#2 [TODO] [HIGH] Review Java & Python - Due: Oct 28, 2025
#4 [TODO] [LOW] Learn Docker - Due: Nov 06, 2025

=== STATISTICS ===
Total tasks: 4
Completed: 1
Remaining: 3""",
    "tutorial": """<h4 class="font-semibold text-gray-200 mb-2">Overview</h4>
<p class="mb-4 text-gray-300">
This capstone combines everything you've learned across 650+ lessons: user authentication, CRUD operations, data structures (HashMap), search and filtering (Streams), date handling (LocalDate), sorting (Comparators), and business logic. It's your showcase piece that demonstrates you're job-ready. This is what you show interviewers when they ask "Tell me about a project you've built."
</p>

<h4 class="font-semibold text-gray-200 mb-2">Skills Demonstrated</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li><strong>Authentication:</strong> User login with password hashing (basic implementation, production uses BCrypt)</li>
<li><strong>CRUD Operations:</strong> Create, Read, Update, Delete tasks with proper state management</li>
<li><strong>Data Structures:</strong> HashMap for O(1) task lookups by ID</li>
<li><strong>Search:</strong> Keyword search across title and description using Streams</li>
<li><strong>Filtering:</strong> Filter by priority, completion status, upcoming deadlines</li>
<li><strong>Sorting:</strong> Tasks sorted by deadline using Comparator</li>
<li><strong>Date Handling:</strong> LocalDate for deadlines, deadline reminder logic</li>
<li><strong>Business Logic:</strong> "Due soon" detection, overdue tasks, completion tracking</li>
<li><strong>Clean Code:</strong> Meaningful names, separation of concerns, Javadoc comments</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Architecture Patterns</h4>
<p class="mb-4 text-gray-300">
This follows the <strong>Service Layer pattern:</strong> User (model), Task (model), TaskManager (service), Main (presentation). In a real application: (1) User and Task would be JPA entities with @Entity annotations, (2) TaskManager would be a @Service with dependency injection, (3) Add TaskRepository for database persistence, (4) Add REST controllers for API endpoints, (5) Add authentication middleware (Spring Security), (6) Add validation (@NotNull, @Size) on fields. This capstone gives you the core logic - adding Spring Boot wrapping makes it production-ready.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Enhancement Ideas</h4>
<pre class="tutorial-code-block">
MAKE IT PRODUCTION-READY:
[] Persist tasks to database (PostgreSQL + JPA)
[] Add REST API endpoints (Spring Boot)
[] Implement proper authentication (JWT tokens)
[] Add user-specific task isolation (users only see their tasks)
[] Email/SMS reminders for upcoming deadlines
[] Task categories and tags
[] Recurring tasks (daily, weekly, monthly)
[] Task assignment (assign to other users)
[] File attachments on tasks
[] Task comments/notes
[] Audit log (who created/modified/deleted what)

DEPLOY IT:
[] Dockerize application
[] Deploy to Heroku/AWS/Digital Ocean
[] Add CI/CD pipeline (GitHub Actions)
[] Set up monitoring (Sentry for errors, Datadog for metrics)
[] Add rate limiting to prevent abuse
[] Load test with JMeter
</pre>

<h4 class="font-semibold text-gray-200 mb-2">Interview Talking Points</h4>
<p class="mb-4 text-gray-300">
When discussing this project in interviews, emphasize: (1) <strong>Technical choices:</strong> "I used HashMap for O(1) task lookups instead of ArrayList which would be O(n)", (2) <strong>Trade-offs:</strong> "I chose in-memory storage for simplicity, but in production I'd use PostgreSQL for persistence", (3) <strong>Business logic:</strong> "The 'due soon' feature checks if a task's deadline is within 3 days - this could be configurable per user", (4) <strong>Extensibility:</strong> "The system is designed to easily add features like task sharing or email reminders", (5) <strong>What you learned:</strong> "This taught me the importance of defensive programming - I added null checks after getting NullPointerException during testing". Show you think beyond just making code work.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Portfolio Presentation</h4>
<pre class="tutorial-code-block">
README.md STRUCTURE:
# Task Management System

## Overview
Full-featured task management application built with Java, demonstrating
CRUD operations, user authentication, search, filtering, and deadline tracking.

## Features
- User authentication with password hashing
- Create, read, update, delete tasks
- Priority levels (HIGH, MEDIUM, LOW)
- Deadline reminders for tasks due soon
- Search tasks by keyword
- Filter by priority or completion status

## Tech Stack
- Java 17
- HashMap for in-memory storage
- Java Streams for search/filter
- LocalDate/LocalDateTime for date handling

## How to Run
```bash
javac Main.java
java Main
```

## Future Enhancements
- PostgreSQL database persistence
- REST API with Spring Boot
- JWT authentication
- Email reminders
- Task sharing between users

## What I Learned
[Write 2-3 paragraphs about challenges faced and how you solved them]

## Screenshots
[Add screenshots of running application]
</pre>

<h4 class="font-semibold text-gray-200 mb-2">Next Steps</h4>
<p class="mb-4 text-gray-300">
<strong>You've completed 660 lessons and built 5 portfolio projects. You're job-ready.</strong> Now: (1) Polish this capstone - add the enhancements above, (2) Deploy it so you have a live URL to share, (3) Create comprehensive README with screenshots, (4) Add it to LinkedIn and resume as your flagship project, (5) Practice explaining it for 5-10 minutes (you WILL be asked about it in every interview), (6) Start applying to jobs - aim for 10-15 quality applications per week. You've put in the work. Now go get that job.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Congratulations!</h4>
<p class="mb-4 text-gray-300">
You've completed the entire devbootLLM curriculum. You've gone from absolute beginner to job-ready developer. You know Java and Python. You understand data structures, algorithms, OOP, functional programming, concurrency, databases, APIs, and system design. You have 5 portfolio projects showcasing different skills. You know how to write a resume, optimize LinkedIn, ace technical interviews, debug production code, and perform code reviews. Most importantly, you've proven you can learn complex topics independently - the most valuable skill in software engineering. The difference between you and a professional developer is now just experience, and you'll get that on the job. Believe in yourself. You've earned this. Now go build amazing things.
</p>""",
    "language": "java",
    "tags": ["Capstone", "Portfolio", "FAANG", "Project", "Full System", "CRUD", "Authentication", "Search", "Filtering", "Sorting", "Best Practices", "Job Ready", "Final Project"]
})

print(f"Prepared {len(new_lessons)} new lessons")

# Add lessons
for lesson in new_lessons:
    lessons.append(lesson)

with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Success! Total lessons: {len(lessons)}")
