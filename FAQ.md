# Frequently Asked Questions (FAQ)

Common questions about DevBoot LLM - a coding education platform with 2,107 verified lessons.

## Table of Contents

- [Getting Started](#getting-started)
- [Deployment](#deployment)
- [Using the Platform](#using-the-platform)
- [Lessons and Content](#lessons-and-content)
- [Code Execution](#code-execution)
- [AI Features](#ai-features)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [Technical Questions](#technical-questions)

---

## Getting Started

### What is DevBoot LLM?

DevBoot LLM is an open-source coding education platform with **2,107 verified lessons** covering Python and Java. Every lesson includes:
- Interactive code editor
- Detailed tutorials
- Working code examples
- Real-time code execution
- Optional AI assistance

### Who is this for?

- **Self-learners**: Learn programming fundamentals at your own pace
- **Bootcamp students**: Supplement your curriculum with hands-on practice
- **Teachers**: Deploy for your students in a controlled environment
- **Companies**: Use for employee training and onboarding

### How much does it cost?

**It's completely free!** This is an open-source project. You can:
- Use it for free online (when available)
- Self-host it for free
- Modify it for your needs
- Deploy it in your organization

No subscriptions, no hidden costs, no account required.

### What do I need to get started?

**To use the platform:**
- Web browser (Chrome, Firefox, Safari, Edge)
- Internet connection (or local deployment)

**To self-host:**
- Docker (recommended) OR
- Node.js 18+ and Python 3.12+ and Java 17+

---

## Deployment

### How do I deploy this?

**Option 1: Docker (Recommended)**
```bash
git clone https://github.com/anthropics/devbootLLM-app.git
cd devbootLLM-app
docker build -t devboot-llm .
docker run -p 3000:3000 devboot-llm
```

Visit `http://localhost:3000`

**Option 2: Manual Setup**
```bash
git clone https://github.com/anthropics/devbootLLM-app.git
cd devbootLLM-app
npm install
npm start
```

**Requirements:**
- Node.js 18+
- Python 3.12+
- Java 17+

### Can I deploy this on my company's servers?

**Yes!** The platform is designed to be self-hosted. You can:
- Deploy on internal servers
- Use behind a firewall
- Run completely offline
- Customize for your needs

No external services required (except optional AI features).

### Can I use this offline?

**Yes!** Once deployed, the platform works completely offline:
- All lessons are local
- Code execution is local
- No external API calls (except optional AI)

Perfect for:
- Corporate environments with restricted internet
- Classroom settings
- Areas with limited connectivity
- Privacy-conscious deployments

### How do I update to the latest version?

```bash
git pull origin main
npm install
docker build -t devboot-llm .  # If using Docker
npm start  # Or restart Docker container
```

---

## Using the Platform

### How do I start learning?

1. Visit the platform (local or online)
2. Select Python or Java
3. Choose a lesson category
4. Pick a lesson based on difficulty
5. Read the tutorial
6. Write code in the editor
7. Click "Run Code" to test
8. Submit when your output matches expected output

### How do I track my progress?

**Currently:** Progress tracking is manual - you remember which lessons you've completed.

**Coming soon:**
- Mark lessons as complete
- Track completion percentage
- "Continue where you left off"
- Learning streaks
- Category completion stats

See [CHANGELOG.md](CHANGELOG.md) for planned features.

### Can I save my code?

**Currently:** Code is saved in your browser's local storage temporarily. Refreshing the page clears it.

**Workaround:** Copy your code to a text editor or IDE to save it permanently.

**Coming soon:** User accounts with code persistence (optional feature).

### How do I search for lessons?

**Currently:** Browse by category and difficulty.

**Coming soon:**
- Full-text search
- Filter by keywords, tags, difficulty
- Search suggestions
- "Most popular" and "Recommended for you"

### Can I use this on mobile?

**Partially.** The platform works on mobile browsers but the experience is optimized for desktop.

**Limitations:**
- Code editor is small on phones
- Keyboard typing can be awkward
- Layout not fully responsive

**Coming soon:** Mobile-optimized experience with touch-friendly controls.

---

## Lessons and Content

### How many lessons are there?

**2,107 verified lessons:**
- 1,030 Python lessons
- 1,077 Java lessons

**100% working** - Every lesson compiles and runs correctly.

### What topics are covered?

**Python (1,030 lessons):**
- Core fundamentals
- Object-oriented programming
- Web development (Flask, Django, FastAPI)
- Asynchronous programming
- Data science (pandas, NumPy, scikit-learn)
- Database (SQLAlchemy)
- Testing (pytest)
- DevOps and deployment

**Java (1,077 lessons):**
- Core fundamentals
- Object-oriented programming
- Spring Boot (REST APIs, MVC)
- Spring Security (authentication, JWT)
- Spring Data (JPA, Hibernate)
- Spring Cloud (microservices)
- Reactive programming (WebFlux)
- Testing (JUnit, Mockito)
- Advanced features (reflection, streams, generics)

### What difficulty levels are available?

- **Beginner**: First steps, basic syntax
- **Intermediate**: Combining concepts, frameworks
- **Advanced**: Complex patterns, architecture
- **Expert**: Optimization, advanced topics

### Are the lessons up-to-date?

Yes! Lessons use:
- Python 3.12+
- Java 17+
- Current framework versions (Spring Boot 3.x, etc.)

### Can I suggest new lessons?

**Yes!** See [CONTRIBUTING.md](CONTRIBUTING.md) for how to:
- Propose new lesson topics
- Submit lesson contributions
- Improve existing lessons

---

## Code Execution

### How does code execution work?

**Python:**
- Runs in a containerized Python 3.12 environment
- Uses `exec()` to execute your code
- Captures stdout and stderr
- 30-second timeout per execution

**Java:**
- Compiles with `javac` (Java 17)
- Runs with `java` command
- Captures output
- 30-second timeout per execution

### Why isn't my code executing?

**Common reasons:**

1. **Syntax errors**: Check for typos, missing colons, unmatched brackets
2. **Runtime errors**: Division by zero, null pointers, etc.
3. **Infinite loops**: Code times out after 30 seconds
4. **Wrong output**: Output must match expected output EXACTLY
5. **Docker not running**: If self-hosting, ensure Docker is running

**Debugging tips:**
- Read error messages carefully
- Use print statements to debug
- Compare with tutorial examples
- Check expected output format (including newlines)

### Why does my output not match?

**Output must match EXACTLY**, including:
- Case sensitivity ("hello" ≠ "Hello")
- Spacing
- Newlines (`\n`)
- Punctuation

**Example:**
```
Expected: "Hello, World!\n"
Your output: "Hello World"  ❌ Missing comma and newline

Your output: "Hello, World!\n"  ✅ Exact match
```

### Can I use external libraries?

**Standard libraries**: Yes, all standard library modules/packages work.

**External packages**: Limited to pre-installed packages:

**Python:**
- Flask, Django, FastAPI
- pandas, NumPy, scikit-learn
- SQLAlchemy, psycopg2
- pytest, requests
- boto3 (AWS SDK)

**Java:**
- Spring Boot ecosystem
- JUnit, Mockito
- Jackson, Lombok
- Common Apache libraries

**Want to add a package?** See [CONTRIBUTING.md](CONTRIBUTING.md) or open an issue.

### Is my code executed securely?

**Yes.** Code runs in:
- Docker containers (isolated from host)
- Limited resource allocation
- 30-second timeout
- No file system access outside container
- No network access (except for web framework lessons)

**However:** This is a learning platform, not a production environment. Don't use it to run untrusted code from others.

---

## AI Features

### How do I enable AI features?

AI features are **optional** and require either:

1. **Ollama** (local AI)
   ```bash
   # Install Ollama
   curl -fsSL https://ollama.ai/install.sh | sh

   # Pull a model
   ollama pull codellama

   # Configure in platform
   Set OLLAMA_URL environment variable
   ```

2. **LM Studio** (local AI)
   - Install LM Studio
   - Load a coding model
   - Start API server
   - Configure platform endpoint

### Do I need AI to use the platform?

**No!** AI is completely optional. The platform works perfectly without it:
- All lessons are complete
- Tutorials explain everything
- Code examples are provided
- Solutions are available

AI just provides additional hints if you get stuck.

### What can AI help with?

- Explain error messages
- Suggest debugging steps
- Provide alternative approaches
- Answer questions about concepts

**AI does NOT:**
- Give you the complete solution
- Do the lesson for you
- Track your progress

### Is my code sent to external servers?

**No!** If you use local AI (Ollama/LM Studio), everything stays on your machine.

**No external API calls** means:
- Your code stays private
- Works offline
- No API costs
- Complete privacy

---

## Contributing

### How can I contribute?

Many ways to help:

1. **Add lessons**: Create new Python or Java lessons
2. **Improve content**: Fix typos, clarify tutorials
3. **Fix bugs**: Report or fix issues
4. **Add features**: Progress tracking, search, etc.
5. **Improve documentation**: Help others understand the project

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Do I need permission to contribute?

**No!** Just:
1. Fork the repository
2. Make your changes
3. Test thoroughly
4. Submit a pull request

All contributions are reviewed and welcomed.

### How do I add a new lesson?

See the [Adding New Lessons](CONTRIBUTING.md#adding-new-lessons) section in CONTRIBUTING.md.

**Quick summary:**
1. Add lesson JSON to `public/lessons-python.json` or `public/lessons-java.json`
2. Ensure code compiles and runs
3. Verify expected output
4. Write clear tutorial
5. Test in the app
6. Submit PR

### What if I find a bug in a lesson?

**Please report it!**

1. Open a [GitHub Issue](https://github.com/anthropics/devbootLLM-app/issues)
2. Include:
   - Lesson ID and title
   - What's wrong
   - Expected vs actual behavior
   - Screenshots if helpful

Or fix it yourself and submit a PR!

---

## Troubleshooting

### Platform won't start

**Docker:**
```bash
# Check if Docker is running
docker ps

# Check logs
docker logs <container_id>

# Rebuild
docker build -t devboot-llm .
```

**Manual setup:**
```bash
# Check Node.js version
node --version  # Should be 18+

# Check Python version
python --version  # Should be 3.12+

# Check Java version
java -version  # Should be 17+

# Reinstall dependencies
rm -rf node_modules
npm install
```

### Code editor not loading

**Check:**
- Browser console for errors (F12 → Console)
- Network tab for failed requests
- Ad blocker isn't blocking resources
- Try different browser

### Code execution fails

**Check:**
1. Code compiles locally first
   ```bash
   # Python
   python -c "exec('''your code here''')"

   # Java
   javac Main.java && java Main
   ```

2. Expected output is correct
3. No infinite loops
4. Syntax is valid

### Docker build fails

**Common issues:**

1. **Insufficient disk space**: Free up space
2. **Docker daemon not running**: Start Docker
3. **Port 3000 in use**: Change port or stop other service
4. **Network issues**: Check internet connection

```bash
# Use different port
docker run -p 8080:3000 devboot-llm
```

### Lesson not displaying correctly

**Check:**
1. Browser cache - try hard refresh (Ctrl+F5)
2. JSON syntax - ensure lessons file is valid JSON
3. Browser console for errors
4. Try different lesson to isolate issue

---

## Technical Questions

### What's the tech stack?

**Backend:**
- Node.js + Express.js
- SQLite database (JSON fallback)
- Child process for code execution

**Frontend:**
- Vanilla JavaScript
- Tailwind CSS
- No framework (lightweight, fast)

**Code Execution:**
- Python 3.12
- Java 17
- Docker containerization

### Can I integrate this with my LMS?

**Possible, but requires development.** You could:
- Embed in iframe (limited)
- Use as content source
- Fork and customize
- Build API integration

No built-in LTI or LMS support currently. See [CHANGELOG.md](CHANGELOG.md) for planned API features.

### How does the validation work?

```javascript
// Simplified validation flow
1. User submits code
2. Server executes code in container
3. Captures output
4. Compares to expectedOutput
5. Returns success/failure + actual output
```

### Can I customize the UI?

**Yes!** Fork the project and modify:
- `public/index.html` - Main UI
- `public/styles.css` - Custom styles (in addition to Tailwind)
- Frontend JavaScript files

### Where is data stored?

**Lessons:** `public/lessons-python.json`, `public/lessons-java.json`

**User progress:** Currently browser localStorage (temporary)

**Database:** SQLite at `coding-platform.db` (created on first run)

### How do I backup my data?

**Lessons:**
```bash
cp public/lessons-python.json backup/
cp public/lessons-java.json backup/
```

**Database:**
```bash
cp coding-platform.db backup/
```

**Docker volumes:**
```bash
docker cp <container_id>:/app/coding-platform.db backup/
```

### Can I add support for other languages?

**Yes!** You'll need to:

1. Create `lessons-<language>.json`
2. Add execution logic in `server.js`
3. Update frontend language selector
4. Test thoroughly

Pull requests welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Still Have Questions?

- **General questions**: [GitHub Discussions](https://github.com/anthropics/devbootLLM-app/discussions)
- **Bug reports**: [GitHub Issues](https://github.com/anthropics/devbootLLM-app/issues)
- **Documentation**: [README.md](README.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Happy learning! 🚀**
