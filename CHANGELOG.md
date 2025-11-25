# Changelog

All notable changes to DevBoot LLM will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- **License**: Updated from proprietary license to Apache License 2.0
  - Added explicit patent grant protection for contributors and users
  - Enables commercial use, modification, and distribution
  - Requires attribution and license notice in distributions
  - Provides legal clarity and protection for open-source community

## [1.0.0] - 2025-11-24

### 🎉 Initial Release

A comprehensive coding education platform with **2,107 verified lessons** achieving **100% compilation and validation rates**.

### Added

#### Core Platform
- **2,107 total lessons** (1,030 Python + 1,077 Java)
- **100% compilation rate** - Every lesson runs without errors
- **100% validation rate** - All tests pass
- Interactive code editor with syntax highlighting
- Real-time code execution for Python and Java
- Docker containerization for easy deployment
- SQLite database with JSON file fallback
- Responsive web interface

#### Python Lessons (1,030 total)
- **Core fundamentals**: Variables, data types, control flow, functions
- **Object-oriented programming**: Classes, inheritance, polymorphism
- **Web development**: Flask, Django, FastAPI
- **Asynchronous programming**: asyncio, concurrent.futures
- **Data science**: pandas, NumPy, scikit-learn
- **Database**: SQLAlchemy, database operations
- **Testing**: pytest, unit testing, mocking
- **DevOps**: Docker, deployment, CI/CD

#### Java Lessons (1,077 total)
- **Core fundamentals**: Variables, data types, control flow, methods
- **Object-oriented programming**: Classes, interfaces, inheritance
- **Spring Boot**: REST APIs, dependency injection, MVC
- **Spring Security**: Authentication, authorization, JWT
- **Spring Data**: JPA, Hibernate, repositories
- **Spring Cloud**: Microservices, service discovery
- **Reactive programming**: Project Reactor, WebFlux
- **Testing**: JUnit, Mockito, integration testing
- **Advanced**: Reflection, annotations, generics, streams

#### Features
- **Difficulty progression**: Beginner → Intermediate → Advanced → Expert
- **10+ categories**: Core, OOP, Web, Async, Database, Testing, DevOps, AI/ML
- **Comprehensive tutorials**: Every lesson includes detailed explanations
- **Code examples**: Working examples demonstrate concepts
- **Best practices**: Guidance on professional coding standards
- **Tag system**: Searchable lesson organization

#### AI Integration
- **Ollama support**: Local AI assistance
- **LM Studio support**: Alternative AI provider
- **AI code hints**: Get help when stuck (optional)

#### Developer Experience
- **Easy deployment**: Docker one-command setup
- **Self-hostable**: Run locally or deploy anywhere
- **No account required**: Privacy-friendly, offline-capable
- **Open source**: Auditable, modifiable, community-driven

### Fixed

#### Quality Improvements (223 lessons improved)
- Fixed all lessons with placeholder or trivial implementations
- Resolved HTML structure issues in tutorials
- Added proper expected output for all lessons
- Fixed edge cases in code execution
- Improved tutorial clarity and completeness

#### Specific Fixes
- **Python lesson 148**: Expanded CSV writing example
- **Python lesson 305**: Comprehensive *args demonstration
- **Java lesson 424**: Fixed reflection deprecated audit
- **Java lesson 460**: Custom log formatter implementation
- **Java lesson 532**: Fixed annotation runtime retention
- **Java lessons 841, 1007**: Educational simulations for complex dependencies

### Documentation
- Comprehensive README with quick start guide
- Architecture documentation
- Lesson structure specifications
- Development setup instructions
- Docker deployment guide
- CONTRIBUTING.md with contribution guidelines
- FAQ for common questions

### Testing
- Validation scripts for all lessons
- Automated compilation testing
- Output verification
- HTML structure validation
- Quality assurance checks

### Technical Stack
- **Backend**: Node.js, Express.js
- **Database**: SQLite with JSON fallback
- **Frontend**: Vanilla JavaScript, Tailwind CSS
- **Code Execution**: Python 3.12, Java 17
- **Containerization**: Docker
- **AI Integration**: Ollama, LM Studio

---

## [Unreleased]

### Planned Features

#### High Priority
- **Progress tracking**: Mark lessons complete, track learning progress
- **Lesson metadata**: Estimated time, prerequisites, related lessons
- **Search and filtering**: Find lessons by keywords, difficulty, category
- **Learning paths**: Structured courses combining related lessons

#### Medium Priority
- **Better code editor**: CodeMirror or Monaco editor integration
- **Keyboard shortcuts**: Power user navigation
- **Mobile responsive**: Improved phone/tablet experience
- **API endpoints**: REST API for progress tracking

#### Future Considerations
- **Code execution improvements**: Faster execution, better error handling
- **Community features**: Lesson ratings, comments
- **Gamification**: Achievements, streaks, leaderboards (if requested)
- **More languages**: JavaScript, Rust, Go (community contributions welcome)

---

## Version History

### What Changed Between Versions

**1.0.0** (2025-11-24)
- Initial public release
- 2,107 verified lessons
- 100% compilation and validation
- Full Docker support
- Comprehensive documentation

---

## Migration Guide

### Upgrading to 1.0.0

This is the initial release. If you're using a development version:

1. **Pull latest changes**
   ```bash
   git pull origin main
   ```

2. **Reinstall dependencies**
   ```bash
   npm install
   ```

3. **Rebuild Docker image** (if using Docker)
   ```bash
   docker build -t devboot-llm .
   docker run -p 3000:3000 devboot-llm
   ```

4. **Verify lessons**
   ```bash
   node scripts/validate-lessons.mjs
   ```

---

## Breaking Changes

None - this is the initial release.

---

## Contributors

Thanks to everyone who contributed to making this release possible!

- Quality assurance and lesson validation
- Docker containerization
- Documentation improvements
- Bug fixes and testing

Want to contribute? See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Support

- **Issues**: [GitHub Issues](https://github.com/undergroundrap/devbootLLM-app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/undergroundrap/devbootLLM-app/discussions)
- **Documentation**: [README.md](README.md)

---

[1.0.0]: https://github.com/undergroundrap/devbootLLM-app/releases/tag/v1.0.0
[Unreleased]: https://github.com/undergroundrap/devbootLLM-app/compare/v1.0.0...HEAD
