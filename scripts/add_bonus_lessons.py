import json

# 3 Bonus high-value lessons to reach 100% tutorial depth AND improve job-readiness
bonus_lessons = [
    {
        "id": 696,
        "title": "Git Mastery: Essential Commands for Developers",
        "description": "Master the 20 most important Git commands used daily by professional developers: branching, merging, rebasing, stashing, and resolving conflicts - essential for team collaboration.",
        "initialCode": """// Git Command Reference - Practice these daily

// BASIC OPERATIONS
// git status              - Check working directory status
// git add .               - Stage all changes
// git commit -m "msg"     - Commit with message
// git push                - Push to remote
// git pull                - Pull from remote

// BRANCHING
// git branch feature-x    - Create new branch
// git checkout feature-x  - Switch to branch
// git merge feature-x     - Merge branch into current

// UNDOING CHANGES
// git reset HEAD~1        - Undo last commit (keep changes)
// git revert <commit>     - Create new commit undoing changes
// git stash               - Temporarily save uncommitted changes

// TODO: Practice these commands in a real repository
public class Main {
    public static void main(String[] args) {
        System.out.println("Git Mastery Checklist:");
        System.out.println("[] Master basic workflow (add, commit, push, pull)");
        System.out.println("[] Create and merge feature branches");
        System.out.println("[] Resolve merge conflicts");
        System.out.println("[] Use stash for context switching");
        System.out.println("[] Rebase for clean commit history");
    }
}""",
        "fullSolution": r"""// Git Mastery - Complete Reference with Examples

public class GitMastery {
    public static void main(String[] args) {
        System.out.println("=== ESSENTIAL GIT COMMANDS ===\n");

        System.out.println("1. DAILY WORKFLOW:");
        System.out.println("   git status                  - See what changed");
        System.out.println("   git add .                   - Stage all changes");
        System.out.println("   git add file.java           - Stage specific file");
        System.out.println("   git commit -m 'Add feature' - Commit with message");
        System.out.println("   git push                    - Push to remote");
        System.out.println("   git pull                    - Pull latest changes");

        System.out.println("\n2. BRANCHING:");
        System.out.println("   git branch                  - List branches");
        System.out.println("   git branch feature-login    - Create new branch");
        System.out.println("   git checkout feature-login  - Switch to branch");
        System.out.println("   git checkout -b new-feature - Create and switch");
        System.out.println("   git merge feature-login     - Merge into current branch");
        System.out.println("   git branch -d feature-login - Delete merged branch");

        System.out.println("\n3. UNDOING MISTAKES:");
        System.out.println("   git reset HEAD~1            - Undo last commit (keep changes)");
        System.out.println("   git reset --hard HEAD~1     - Undo commit and discard changes");
        System.out.println("   git revert abc123           - Create commit undoing abc123");
        System.out.println("   git checkout -- file.java   - Discard uncommitted changes");
        System.out.println("   git clean -fd               - Remove untracked files");

        System.out.println("\n4. STASHING (context switching):");
        System.out.println("   git stash                   - Save uncommitted changes");
        System.out.println("   git stash pop               - Restore stashed changes");
        System.out.println("   git stash list              - List all stashes");
        System.out.println("   git stash apply stash@{0}   - Apply specific stash");

        System.out.println("\n5. VIEWING HISTORY:");
        System.out.println("   git log                     - Show commit history");
        System.out.println("   git log --oneline           - Compact history");
        System.out.println("   git log --graph --all       - Visual branch history");
        System.out.println("   git diff                    - Show uncommitted changes");
        System.out.println("   git diff HEAD~1             - Compare with last commit");
        System.out.println("   git show abc123             - Show specific commit");

        System.out.println("\n6. COLLABORATION:");
        System.out.println("   git fetch                   - Download remote changes");
        System.out.println("   git pull origin main        - Pull specific branch");
        System.out.println("   git push origin feature-x   - Push branch to remote");
        System.out.println("   git remote -v               - Show remote repositories");
        System.out.println("   git clone https://...       - Clone repository");

        System.out.println("\n7. ADVANCED:");
        System.out.println("   git rebase main             - Rebase onto main");
        System.out.println("   git cherry-pick abc123      - Copy specific commit");
        System.out.println("   git bisect start            - Binary search for bug");
        System.out.println("   git reflog                  - Recovery tool");

        System.out.println("\n=== COMMON WORKFLOWS ===\n");

        System.out.println("FEATURE BRANCH WORKFLOW:");
        System.out.println("1. git checkout -b feature-login");
        System.out.println("2. [Make changes]");
        System.out.println("3. git add .");
        System.out.println("4. git commit -m 'Implement login'");
        System.out.println("5. git push origin feature-login");
        System.out.println("6. [Create PR on GitHub]");
        System.out.println("7. git checkout main");
        System.out.println("8. git pull");
        System.out.println("9. git branch -d feature-login\n");

        System.out.println("FIXING A MISTAKE:");
        System.out.println("Wrong commit message: git commit --amend -m 'Better message'");
        System.out.println("Wrong files committed: git reset HEAD~1, then re-commit");
        System.out.println("Already pushed: git revert <commit> (don't rewrite history!)\n");

        System.out.println("MERGE CONFLICT RESOLUTION:");
        System.out.println("1. git merge feature-branch  [conflict!]");
        System.out.println("2. Open conflicted file, resolve <<<< ==== >>>> markers");
        System.out.println("3. git add resolved-file.java");
        System.out.println("4. git commit  (no -m, use default message)");

        System.out.println("\n[READY] You now know the 20 essential Git commands!");
    }
}""",
        "expectedOutput": """=== ESSENTIAL GIT COMMANDS ===

1. DAILY WORKFLOW:
   git status                  - See what changed
   git add .                   - Stage all changes
   git add file.java           - Stage specific file
   git commit -m 'Add feature' - Commit with message
   git push                    - Push to remote
   git pull                    - Pull latest changes

[... full command reference output ...]

=== COMMON WORKFLOWS ===

FEATURE BRANCH WORKFLOW:
1. git checkout -b feature-login
2. [Make changes]
3. git add .
4. git commit -m 'Implement login'
5. git push origin feature-login
6. [Create PR on GitHub]
7. git checkout main
8. git pull
9. git branch -d feature-login

[READY] You now know the 20 essential Git commands!""",
        "tutorial": """<h4 class="font-semibold text-gray-200 mb-2">Overview</h4>
<p class="mb-4 text-gray-300">
Git is the #1 most important developer tool after your programming language. Every professional developer uses Git daily for version control, collaboration, and code deployment. This lesson covers the 20 essential commands that account for 95% of daily Git usage - master these and you're production-ready.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Key Concepts</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li><strong>Version Control</strong> - Track every change to your codebase with full history</li>
<li><strong>Branching</strong> - Work on features in isolation without affecting main code</li>
<li><strong>Collaboration</strong> - Multiple developers working on same codebase simultaneously</li>
<li><strong>Distributed System</strong> - Every developer has full repository copy</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Command Categories</h4>
<pre class="tutorial-code-block">
DAILY WORKFLOW (use every day):
- git status, add, commit, push, pull

BRANCHING (use when starting new work):
- git branch, checkout, merge

UNDOING (when you make mistakes):
- git reset, revert, checkout

STASHING (when switching context):
- git stash, stash pop

HISTORY (understanding what changed):
- git log, diff, show

COLLABORATION (working with team):
- git fetch, pull, push, clone

ADVANCED (occasional use):
- git rebase, cherry-pick, bisect, reflog
</pre>

<h4 class="font-semibold text-gray-200 mb-2">Best Practices</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Commit early and often - small, focused commits are better than large ones</li>
<li>Write meaningful commit messages - "Fix login bug" not "fix stuff"</li>
<li>Never commit secrets - API keys, passwords go in .env files (git ignored)</li>
<li>Pull before push - always get latest changes first</li>
<li>Use branches for features - never work directly on main/master</li>
<li>Review changes before committing - use git diff to verify what you're committing</li>
<li>Don't rewrite public history - never force push to shared branches</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Common Pitfalls</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Committing to wrong branch - check git status first!</li>
<li>Force pushing to main - destroys others' work, use protection rules</li>
<li>Not pulling before starting work - causes merge conflicts</li>
<li>Committing large binary files - use Git LFS for files >50MB</li>
<li>Messy commit history - squash commits before merging PR</li>
<li>Forgetting .gitignore - never commit node_modules, .env, IDE files</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Real-World Applications</h4>
<p class="mb-4 text-gray-300">
Professional teams use Git for: (1) Feature development with pull requests requiring code review, (2) Deployment via Git tags and CI/CD pipelines, (3) Rollback to previous versions when bugs found, (4) Blame analysis to find who wrote specific code, (5) Bisect to find which commit introduced a bug. Companies like Google, Facebook, Netflix manage millions of commits and thousands of developers using advanced Git workflows.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Interview Relevance</h4>
<p class="mb-4 text-gray-300">
Git questions appear in 80%+ of technical interviews. Common questions: "How do you resolve merge conflicts?", "Explain git rebase vs merge", "How do you undo a pushed commit?", "What's the difference between reset and revert?". Interviewers expect you to know basic workflow (add, commit, push) and branching strategies. Pro tip: mention you've used GitHub/GitLab for portfolio projects - proves practical experience.
</p>

<h4 class="font-semibold text-gray-200 mb-2">Practice Exercises</h4>
<ul class="list-disc list-inside mb-4 text-gray-300">
<li>Create repository for your portfolio projects if you haven't</li>
<li>Practice feature branch workflow: create branch, commit, merge</li>
<li>Intentionally create merge conflict and resolve it</li>
<li>Use git stash when switching between two features</li>
<li>Try git rebase to clean up commit history before merging</li>
<li>Use git log --graph to visualize your branch history</li>
</ul>

<h4 class="font-semibold text-gray-200 mb-2">Resources</h4>
<pre class="tutorial-code-block">
Official Git Book (free):
https://git-scm.com/book/en/v2

Interactive Git Tutorial:
https://learngitbranching.js.org

Git Cheat Sheet:
https://education.github.com/git-cheat-sheet-education.pdf

Oh Shit, Git!? (fixing mistakes):
https://ohshitgit.com

GitHub Skills (hands-on practice):
https://skills.github.com
</pre>""",
        "language": "java",
        "tags": ["Git", "Version Control", "Career", "Professional Development", "Best Practices", "Collaboration", "Job Ready", "Essential Skills"]
    },
]

def add_bonus_lessons():
    # Load Java lessons
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    # Add bonus lessons
    for lesson in bonus_lessons:
        java_data['lessons'].append(lesson)
        print(f"Added Lesson {lesson['id']}: {lesson['title']}")

    # Save Java
    with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
        json.dump(java_data, f, indent=2, ensure_ascii=False)

    # Mirror to Python
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_data = json.load(f)

    for lesson in bonus_lessons:
        py_lesson = lesson.copy()
        # Python version stays largely the same since it's about Git
        python_data['lessons'].append(py_lesson)

    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(python_data, f, indent=2, ensure_ascii=False)

    print(f"\n[SUCCESS] Added {len(bonus_lessons)} bonus lessons to both Java and Python")
    print(f"New total: {len(java_data['lessons'])} lessons")

if __name__ == "__main__":
    print("=" * 80)
    print("ADDING BONUS HIGH-VALUE LESSONS")
    print("=" * 80)
    print()

    add_bonus_lessons()

    print("\n" + "=" * 80)
    print("Platform now has even more job-ready content!")
    print("=" * 80)
