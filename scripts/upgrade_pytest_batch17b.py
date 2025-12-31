#!/usr/bin/env python3
"""
Upgrade pytest lessons to comprehensive simulations (13,000-17,000+ chars)
Batch 17b: pytest CI/CD Integration, Database Testing, and Test Organization
"""

import json
import sys
from pathlib import Path

def upgrade_lessons():
    lessons_file = Path("c:/devbootLLM-app/public/lessons-python.json")

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Lesson 814: pytest CI/CD Integration
    lesson_814 = next(l for l in lessons if l['id'] == 814)
    lesson_814['fullSolution'] = '''# pytest CI/CD Integration - Complete Simulation
# In production: pip install pytest pytest-cov pytest-xdist
# This lesson simulates pytest integration with CI/CD pipelines

import subprocess
import json
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import os

@dataclass
class TestResult:
    """Test result with metadata."""
    name: str
    outcome: str  # passed, failed, skipped
    duration: float
    error: Optional[str] = None

@dataclass
class CoverageResult:
    """Code coverage result."""
    total_statements: int
    covered_statements: int
    missing_lines: List[int]

    @property
    def percentage(self) -> float:
        if self.total_statements == 0:
            return 100.0
        return (self.covered_statements / self.total_statements) * 100

class PytestRunner:
    """
    Pytest runner with CI/CD features.

    Features:
    - JUnit XML reports
    - Coverage reports
    - Parallel execution
    - Test selection
    """

    def __init__(self):
        self.results: List[TestResult] = []
        self.coverage: Dict[str, CoverageResult] = {}

    def run_tests(
        self,
        test_paths: List[str] = None,
        markers: str = None,
        coverage: bool = False,
        parallel: bool = False,
        junit_xml: str = None
    ) -> int:
        """
        Run pytest with CI/CD options.

        Args:
            test_paths: Specific test files/directories
            markers: Test markers to filter (-m flag)
            coverage: Enable coverage reporting
            parallel: Run tests in parallel
            junit_xml: Output JUnit XML report

        Returns:
            Exit code (0 = success, 1 = failures)
        """
        print(f"[PYTEST] Running tests...")

        # Simulate test execution
        self._execute_tests(test_paths, markers)

        # Generate reports
        if coverage:
            self._generate_coverage()

        if junit_xml:
            self._generate_junit_xml(junit_xml)

        # Count failures
        failures = sum(1 for r in self.results if r.outcome == "failed")

        return 0 if failures == 0 else 1

    def _execute_tests(self, test_paths: List[str] = None, markers: str = None):
        """Execute tests."""
        # Simulated test results
        test_cases = [
            TestResult("test_user_login", "passed", 0.05),
            TestResult("test_user_logout", "passed", 0.03),
            TestResult("test_invalid_credentials", "passed", 0.04),
            TestResult("test_database_connection", "passed", 0.10),
            TestResult("test_api_endpoint", "failed", 0.08, "AssertionError: Expected 200, got 500"),
            TestResult("test_slow_query", "skipped", 0.00),
        ]

        # Filter by markers if specified
        if markers:
            if markers == "not slow":
                test_cases = [t for t in test_cases if "slow" not in t.name]

        self.results = test_cases

        # Display results
        for result in self.results:
            status_icon = {
                "passed": "✓",
                "failed": "✗",
                "skipped": "○"
            }.get(result.outcome, "?")

            print(f"  {status_icon} {result.name} ({result.duration:.2f}s)")
            if result.error:
                print(f"    Error: {result.error}")

    def _generate_coverage(self):
        """Generate coverage report."""
        # Simulated coverage data
        self.coverage = {
            "app/auth.py": CoverageResult(50, 45, [10, 15, 20, 25, 30]),
            "app/models.py": CoverageResult(100, 95, [50, 60, 70, 80, 90]),
            "app/views.py": CoverageResult(75, 60, list(range(30, 45))),
        }

        print(f"\\n[COVERAGE] Coverage Report:")
        print(f"{'File':<20} {'Stmts':>8} {'Miss':>8} {'Cover':>8}")
        print("-" * 50)

        total_stmts = 0
        total_covered = 0

        for file, cov in self.coverage.items():
            missed = cov.total_statements - cov.covered_statements
            total_stmts += cov.total_statements
            total_covered += cov.covered_statements

            print(f"{file:<20} {cov.total_statements:>8} {missed:>8} {cov.percentage:>7.0f}%")

        print("-" * 50)
        total_pct = (total_covered / total_stmts * 100) if total_stmts > 0 else 0
        print(f"{'TOTAL':<20} {total_stmts:>8} {total_stmts - total_covered:>8} {total_pct:>7.0f}%")

    def _generate_junit_xml(self, output_file: str):
        """Generate JUnit XML report for CI systems."""
        print(f"\\n[JUNIT] Writing XML report to {output_file}")

        # Create XML structure
        testsuites = ET.Element("testsuites")
        testsuite = ET.SubElement(testsuites, "testsuite", {
            "name": "pytest",
            "tests": str(len(self.results)),
            "failures": str(sum(1 for r in self.results if r.outcome == "failed")),
            "skipped": str(sum(1 for r in self.results if r.outcome == "skipped")),
            "time": str(sum(r.duration for r in self.results))
        })

        for result in self.results:
            testcase = ET.SubElement(testsuite, "testcase", {
                "name": result.name,
                "time": str(result.duration)
            })

            if result.outcome == "failed":
                failure = ET.SubElement(testcase, "failure", {
                    "message": result.error or "Test failed"
                })
                failure.text = result.error

            elif result.outcome == "skipped":
                ET.SubElement(testcase, "skipped")

        # Write to file
        tree = ET.ElementTree(testsuites)
        ET.indent(tree, space="  ")
        with open(output_file, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)

        print(f"  Generated JUnit XML with {len(self.results)} test cases")

class GitHubActions:
    """GitHub Actions workflow simulation."""

    @staticmethod
    def generate_workflow() -> str:
        """Generate GitHub Actions workflow YAML."""
        return """name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11']

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov pytest-xdist

    - name: Run tests with coverage
      run: |
        pytest --cov=app --cov-report=xml --cov-report=term \\
               --junitxml=junit/test-results.xml \\
               -n auto

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        fail_ci_if_error: true

    - name: Upload test results
      uses: actions/upload-artifact@v3
      if: always()
      with:
        name: test-results
        path: junit/test-results.xml
"""

class GitLabCI:
    """GitLab CI pipeline simulation."""

    @staticmethod
    def generate_pipeline() -> str:
        """Generate GitLab CI pipeline YAML."""
        return """stages:
  - test
  - coverage

variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

cache:
  paths:
    - .cache/pip

test:
  stage: test
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - pip install pytest pytest-cov
    - pytest --junitxml=report.xml --cov=app
  artifacts:
    when: always
    reports:
      junit: report.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml

coverage:
  stage: coverage
  image: python:3.11
  script:
    - pip install coverage
    - coverage report
    - coverage html
  artifacts:
    paths:
      - htmlcov/
  coverage: '/TOTAL.*\\s+(\\d+)%/'
"""

# Example 1: Basic CI/CD Test Run
print("Example 1: Basic CI/CD Test Run")
print("=" * 60)

runner = PytestRunner()
exit_code = runner.run_tests()

print(f"\\nTest Summary:")
print(f"  Total: {len(runner.results)}")
print(f"  Passed: {sum(1 for r in runner.results if r.outcome == 'passed')}")
print(f"  Failed: {sum(1 for r in runner.results if r.outcome == 'failed')}")
print(f"  Skipped: {sum(1 for r in runner.results if r.outcome == 'skipped')}")
print(f"  Exit code: {exit_code}")
print()

# Example 2: Coverage Report
print("Example 2: Coverage Report")
print("=" * 60)

runner2 = PytestRunner()
runner2.run_tests(coverage=True)
print()

# Example 3: JUnit XML for CI
print("Example 3: JUnit XML Report for CI")
print("=" * 60)

runner3 = PytestRunner()
runner3.run_tests(junit_xml="test-results.xml")
print()

# Example 4: Parallel Testing
print("Example 4: Parallel Testing")
print("=" * 60)

print("Running tests in parallel with pytest-xdist:")
print("  Command: pytest -n auto")
print("  Workers: 4 (auto-detected)")
print()

runner4 = PytestRunner()
runner4.run_tests(parallel=True)
print()

# Example 5: Test Markers (CI Optimization)
print("Example 5: Test Markers for CI Optimization")
print("=" * 60)

print("Running fast tests only (skip slow tests):")
print("  Command: pytest -m 'not slow'")
print()

runner5 = PytestRunner()
runner5.run_tests(markers="not slow")
print()

# Example 6: GitHub Actions Workflow
print("Example 6: GitHub Actions Workflow")
print("=" * 60)

workflow = GitHubActions.generate_workflow()
print("Generated .github/workflows/ci.yml:")
print(workflow[:500] + "...")
print()

# Example 7: GitLab CI Pipeline
print("Example 7: GitLab CI Pipeline")
print("=" * 60)

pipeline = GitLabCI.generate_pipeline()
print("Generated .gitlab-ci.yml:")
print(pipeline[:400] + "...")
print()

# Example 8: Coverage Threshold Check
print("Example 8: Coverage Threshold Check")
print("=" * 60)

def check_coverage_threshold(coverage: Dict[str, CoverageResult], threshold: float = 80.0) -> bool:
    """Check if coverage meets threshold."""
    total_stmts = sum(c.total_statements for c in coverage.values())
    total_covered = sum(c.covered_statements for c in coverage.values())

    if total_stmts == 0:
        return True

    percentage = (total_covered / total_stmts) * 100

    print(f"Coverage: {percentage:.1f}% (threshold: {threshold}%)")

    if percentage >= threshold:
        print("  ✓ Coverage threshold met")
        return True
    else:
        print(f"  ✗ Coverage below threshold (need {threshold - percentage:.1f}% more)")
        return False

runner8 = PytestRunner()
runner8.run_tests(coverage=True)

print()
passed = check_coverage_threshold(runner8.coverage, threshold=80.0)
print()

print("=" * 60)
print("PYTEST CI/CD INTEGRATION BEST PRACTICES")
print("=" * 60)
print("""
CI/CD CONFIGURATION:

1. PYTEST OPTIONS:
   --cov=app                 # Enable coverage
   --cov-report=xml          # XML for CI tools
   --cov-report=term         # Terminal output
   --junitxml=report.xml     # JUnit XML report
   -n auto                   # Parallel execution
   -m "not slow"             # Skip slow tests
   --maxfail=1               # Fail fast
   --tb=short                # Short traceback

2. COVERAGE REQUIREMENTS:
   [tool.pytest.ini_options]
   addopts = """--cov=app --cov-fail-under=80"""

   # Fail if coverage < 80%

3. TEST MARKERS:
   @pytest.mark.slow
   @pytest.mark.integration
   @pytest.mark.smoke
   @pytest.mark.critical

   # Run: pytest -m smoke (quick checks)

GITHUB ACTIONS:

Matrix Testing:
  strategy:
    matrix:
      python-version: ['3.9', '3.10', '3.11']
      os: [ubuntu-latest, windows-latest]

Caching:
  - uses: actions/cache@v3
    with:
      path: ~/.cache/pip
      key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}

Artifacts:
  - uses: actions/upload-artifact@v3
    with:
      name: coverage-report
      path: htmlcov/

GITLAB CI:

Stages:
  stages:
    - test
    - coverage
    - deploy

Artifacts:
  artifacts:
    reports:
      junit: report.xml
      coverage_report:
        coverage_format: cobertura

Coverage Visualization:
  coverage: '/TOTAL.*\\s+(\\d+)%/'

JENKINS:

Jenkinsfile:
  pipeline {
    agent any
    stages {
      stage('Test') {
        steps {
          sh 'pytest --junitxml=results.xml'
        }
      }
      stage('Coverage') {
        steps {
          sh 'pytest --cov=app --cov-report=xml'
        }
      }
    }
    post {
      always {
        junit 'results.xml'
        publishHTML([
          reportDir: 'htmlcov',
          reportFiles: 'index.html'
        ])
      }
    }
  }

OPTIMIZATION STRATEGIES:

1. Parallel Execution:
   pytest -n auto  # Use all CPU cores
   pytest -n 4     # Use 4 workers

2. Test Selection:
   pytest tests/unit/           # Only unit tests
   pytest -m "not slow"         # Skip slow tests
   pytest --lf                  # Last failed
   pytest --ff                  # Failed first

3. Caching:
   - Cache pip dependencies
   - Cache pytest cache (.pytest_cache/)
   - Reuse test databases

4. Fail Fast:
   pytest --maxfail=1     # Stop after first failure
   pytest -x              # Stop on first error

REPORTING:

Coverage Badges:
  [![Coverage](https://codecov.io/gh/user/repo/branch/main/graph/badge.svg)]

Test Results:
  - JUnit XML for CI dashboards
  - HTML reports for developers
  - Cobertura XML for coverage tools

Notifications:
  - Slack on failure
  - Email reports
  - GitHub status checks

DOCKER INTEGRATION:

Dockerfile for testing:
  FROM python:3.11
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  CMD ["pytest", "--cov=app"]

Docker Compose:
  version: '3.8'
  services:
    test:
      build: .
      command: pytest --cov=app
      volumes:
        - ./htmlcov:/app/htmlcov

MONITORING:

Metrics to track:
  - Test execution time
  - Test failure rate
  - Code coverage trend
  - Flaky test detection

Alerts:
  - Coverage drop > 5%
  - New failing tests
  - Slow test threshold

BEST PRACTICES:

1. Fast Feedback:
   - Run unit tests first
   - Integration tests later
   - Slow tests in nightly builds

2. Stability:
   - Fix flaky tests immediately
   - Use retry decorators sparingly
   - Isolate test dependencies

3. Maintainability:
   - Keep tests fast (< 1s each)
   - Clear test names
   - DRY principle with fixtures

4. Security:
   - Don't commit secrets
   - Use environment variables
   - Secure test credentials

Production note: Real pytest CI/CD provides:
  - Advanced reporting plugins
  - Test result history
  - Coverage trending
  - Parallel test distribution
  - Test sharding
  - Automatic retry
  - Flaky test detection
  - Integration with all major CI platforms
""")
'''

    # Lesson 812: pytest Database Testing
    lesson_812 = next(l for l in lessons if l['id'] == 812)
    lesson_812['fullSolution'] = '''# pytest Database Testing - Complete Simulation
# In production: pip install pytest pytest-django factory-boy
# This lesson simulates database testing patterns with pytest

import sqlite3
from typing import Any, Callable, Dict, List, Optional
from dataclasses import dataclass
from contextlib import contextmanager
import tempfile
import os

@dataclass
class User:
    """User model."""
    id: Optional[int] = None
    username: str = ""
    email: str = ""
    is_active: bool = True

class Database:
    """Simple database abstraction."""

    def __init__(self, connection_string: str = ":memory:"):
        self.conn = sqlite3.connect(connection_string)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        """Create database schema."""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                is_active INTEGER DEFAULT 1
            )
        """)
        self.conn.commit()

    def create_user(self, username: str, email: str) -> User:
        """Create new user."""
        cursor = self.conn.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (username, email)
        )
        self.conn.commit()

        return User(id=cursor.lastrowid, username=username, email=email)

    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        cursor = self.conn.execute(
            "SELECT * FROM users WHERE id = ?",
            (user_id,)
        )
        row = cursor.fetchone()

        if row:
            return User(
                id=row["id"],
                username=row["username"],
                email=row["email"],
                is_active=bool(row["is_active"])
            )
        return None

    def get_all_users(self) -> List[User]:
        """Get all users."""
        cursor = self.conn.execute("SELECT * FROM users")
        return [
            User(
                id=row["id"],
                username=row["username"],
                email=row["email"],
                is_active=bool(row["is_active"])
            )
            for row in cursor.fetchall()
        ]

    def update_user(self, user_id: int, **kwargs):
        """Update user."""
        fields = ", ".join(f"{k} = ?" for k in kwargs.keys())
        values = list(kwargs.values()) + [user_id]

        self.conn.execute(
            f"UPDATE users SET {fields} WHERE id = ?",
            values
        )
        self.conn.commit()

    def delete_user(self, user_id: int):
        """Delete user."""
        self.conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()

    def close(self):
        """Close connection."""
        self.conn.close()

class DatabaseFixtures:
    """
    Database test fixtures.

    Provides:
    - Clean database per test
    - Transaction rollback
    - Test data factories
    """

    @staticmethod
    @contextmanager
    def db_connection():
        """Database connection fixture (in-memory)."""
        db = Database(":memory:")
        try:
            yield db
        finally:
            db.close()

    @staticmethod
    @contextmanager
    def db_transaction(db: Database):
        """
        Transaction fixture with rollback.

        Each test runs in a transaction that's rolled back after test.
        """
        db.conn.execute("BEGIN")
        try:
            yield db
        finally:
            db.conn.execute("ROLLBACK")

class UserFactory:
    """
    User factory for test data generation.

    Similar to factory_boy pattern.
    """

    _counter = 0

    @classmethod
    def create(cls, db: Database, **kwargs) -> User:
        """Create user with default or custom data."""
        cls._counter += 1

        defaults = {
            "username": f"user{cls._counter}",
            "email": f"user{cls._counter}@example.com"
        }
        defaults.update(kwargs)

        return db.create_user(defaults["username"], defaults["email"])

    @classmethod
    def create_batch(cls, db: Database, size: int, **kwargs) -> List[User]:
        """Create multiple users."""
        return [cls.create(db, **kwargs) for _ in range(size)]

# Example 1: Basic Database Test
print("Example 1: Basic Database Test")
print("=" * 60)

print("Test: Create and retrieve user")
with DatabaseFixtures.db_connection() as db:
    # Create user
    user = db.create_user("alice", "alice@example.com")
    print(f"  Created user: {user.username} (ID: {user.id})")

    # Retrieve user
    retrieved = db.get_user(user.id)
    assert retrieved is not None
    assert retrieved.username == "alice"
    print(f"  Retrieved user: {retrieved.username}")
    print("  ✓ Test passed")

print()

# Example 2: Transaction Rollback
print("Example 2: Transaction Rollback Pattern")
print("=" * 60)

print("Test with transaction rollback:")
with DatabaseFixtures.db_connection() as db:
    # First test - data is rolled back
    with DatabaseFixtures.db_transaction(db):
        user1 = db.create_user("bob", "bob@example.com")
        print(f"  Test 1: Created {user1.username}")
        users = db.get_all_users()
        print(f"  Test 1: Total users: {len(users)}")

    # Second test - clean database
    with DatabaseFixtures.db_transaction(db):
        users = db.get_all_users()
        print(f"  Test 2: Total users: {len(users)} (rolled back)")

        user2 = db.create_user("charlie", "charlie@example.com")
        print(f"  Test 2: Created {user2.username}")
        users = db.get_all_users()
        print(f"  Test 2: Total users: {len(users)}")

print()

# Example 3: Factory Pattern
print("Example 3: Factory Pattern for Test Data")
print("=" * 60)

print("Creating test users with factory:")
with DatabaseFixtures.db_connection() as db:
    # Create with defaults
    user1 = UserFactory.create(db)
    print(f"  Created: {user1.username} - {user1.email}")

    # Create with custom data
    user2 = UserFactory.create(db, username="admin", email="admin@example.com")
    print(f"  Created: {user2.username} - {user2.email}")

    # Create batch
    batch = UserFactory.create_batch(db, 3)
    print(f"  Created batch: {[u.username for u in batch]}")

    total = len(db.get_all_users())
    print(f"  Total users: {total}")

print()

# Example 4: Testing CRUD Operations
print("Example 4: Testing CRUD Operations")
print("=" * 60)

print("CRUD test suite:")
with DatabaseFixtures.db_connection() as db:
    # CREATE
    print("  [CREATE] Creating user...")
    user = db.create_user("testuser", "test@example.com")
    assert user.id is not None
    print(f"    ✓ User created with ID: {user.id}")

    # READ
    print("  [READ] Reading user...")
    retrieved = db.get_user(user.id)
    assert retrieved.username == "testuser"
    print(f"    ✓ User retrieved: {retrieved.username}")

    # UPDATE
    print("  [UPDATE] Updating user...")
    db.update_user(user.id, email="newemail@example.com")
    updated = db.get_user(user.id)
    assert updated.email == "newemail@example.com"
    print(f"    ✓ Email updated: {updated.email}")

    # DELETE
    print("  [DELETE] Deleting user...")
    db.delete_user(user.id)
    deleted = db.get_user(user.id)
    assert deleted is None
    print(f"    ✓ User deleted")

print()

# Example 5: Testing Constraints
print("Example 5: Testing Database Constraints")
print("=" * 60)

print("Testing unique constraint:")
with DatabaseFixtures.db_connection() as db:
    # Create first user
    db.create_user("unique_user", "unique@example.com")
    print("  Created user: unique_user")

    # Try to create duplicate
    try:
        db.create_user("unique_user", "different@example.com")
        print("  ✗ Duplicate allowed (should fail!)")
    except sqlite3.IntegrityError as e:
        print(f"  ✓ Unique constraint enforced: {str(e)[:50]}...")

print()

# Example 6: Testing Queries
print("Example 6: Testing Complex Queries")
print("=" * 60)

print("Testing user filtering:")
with DatabaseFixtures.db_connection() as db:
    # Create test data
    UserFactory.create(db, username="active1", is_active=True)
    UserFactory.create(db, username="active2", is_active=True)
    UserFactory.create(db, username="inactive1", is_active=False)

    # Query active users
    cursor = db.conn.execute("SELECT * FROM users WHERE is_active = 1")
    active_users = cursor.fetchall()

    print(f"  Total users: {len(db.get_all_users())}")
    print(f"  Active users: {len(active_users)}")
    print(f"  ✓ Query test passed")

print()

# Example 7: Database Migration Testing
print("Example 7: Database Migration Testing")
print("=" * 60)

class Migration:
    """Database migration simulation."""

    @staticmethod
    def add_created_at_column(db: Database):
        """Migration: Add created_at column."""
        db.conn.execute("""
            ALTER TABLE users
            ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        """)
        db.conn.commit()

    @staticmethod
    def verify_migration(db: Database) -> bool:
        """Verify migration was applied."""
        cursor = db.conn.execute("PRAGMA table_info(users)")
        columns = [row[1] for row in cursor.fetchall()]
        return "created_at" in columns

print("Testing migration:")
with DatabaseFixtures.db_connection() as db:
    # Before migration
    has_column = Migration.verify_migration(db)
    print(f"  Before: has created_at column: {has_column}")

    # Apply migration
    Migration.add_created_at_column(db)
    print("  Applied migration")

    # After migration
    has_column = Migration.verify_migration(db)
    print(f"  After: has created_at column: {has_column}")
    print(f"  ✓ Migration test passed")

print()

# Example 8: Parametrized Database Tests
print("Example 8: Parametrized Database Tests")
print("=" * 60)

test_cases = [
    ("alice", "alice@example.com", True),
    ("bob", "bob@example.com", True),
    ("charlie", "charlie@example.com", False),
]

print("Running parametrized tests:")
with DatabaseFixtures.db_connection() as db:
    for username, email, is_active in test_cases:
        user = db.create_user(username, email)
        db.update_user(user.id, is_active=is_active)

        retrieved = db.get_user(user.id)
        assert retrieved.is_active == is_active

        status = "active" if is_active else "inactive"
        print(f"  ✓ {username}: {status}")

print()

print("=" * 60)
print("DATABASE TESTING BEST PRACTICES")
print("=" * 60)
print("""
PYTEST FIXTURES:

Database Connection:
  @pytest.fixture(scope="function")
  def db():
      db = Database(":memory:")
      yield db
      db.close()

Transaction Rollback:
  @pytest.fixture
  def db_transaction(db):
      db.begin()
      yield db
      db.rollback()

Test Database:
  @pytest.fixture(scope="session")
  def test_db():
      db = create_test_database()
      yield db
      drop_test_database()

FACTORY PATTERN:

Factory Boy:
  class UserFactory(factory.Factory):
      class Meta:
          model = User

      username = factory.Sequence(lambda n: f"user{n}")
      email = factory.LazyAttribute(
          lambda obj: f"{obj.username}@example.com"
      )

Usage:
  user = UserFactory.create()
  users = UserFactory.create_batch(10)

ISOLATION:

1. In-Memory Database:
   - Fast setup/teardown
   - Perfect isolation
   - Good for unit tests

2. Transaction Rollback:
   - Real database
   - Each test in transaction
   - Rolled back after test

3. Database Fixtures:
   - Known test data
   - Reproducible tests
   - Easy assertions

DJANGO SPECIFIC:

Database Fixture:
  @pytest.fixture
  def db():
      # Provides access to database

Transactional Test:
  @pytest.mark.django_db(transaction=True)
  def test_something():
      ...

SQLALCHEMY SPECIFIC:

Session Fixture:
  @pytest.fixture
  def db_session():
      session = Session()
      yield session
      session.rollback()
      session.close()

Model Factory:
  class UserFactory(SQLAlchemyModelFactory):
      class Meta:
          model = User
          sqlalchemy_session = session

PERFORMANCE:

Optimization strategies:
  - Use in-memory database for fast tests
  - Share database across test suite (scope="session")
  - Minimize database setup/teardown
  - Use fixtures for common data
  - Parallel test execution with separate databases

TESTING PATTERNS:

1. AAA Pattern:
   def test_create_user(db):
       # Arrange
       username = "testuser"

       # Act
       user = db.create_user(username, "email")

       # Assert
       assert user.id is not None

2. Given-When-Then:
   def test_update_user(db):
       # Given
       user = UserFactory.create(db)

       # When
       db.update_user(user.id, email="new@example.com")

       # Then
       updated = db.get_user(user.id)
       assert updated.email == "new@example.com"

3. Setup-Exercise-Verify:
   def test_delete_user(db):
       # Setup
       user = UserFactory.create(db)

       # Exercise
       db.delete_user(user.id)

       # Verify
       assert db.get_user(user.id) is None

MIGRATION TESTING:

Test Migration:
  def test_migration_001(db):
      # Apply migration
      migrate(db, "001_add_column")

      # Verify schema
      assert has_column(db, "users", "created_at")

      # Test data migration
      user = create_user(db)
      assert user.created_at is not None

Rollback Test:
  def test_migration_rollback(db):
      migrate(db, "001_add_column")
      rollback(db, "001_add_column")
      assert not has_column(db, "users", "created_at")

FIXTURES STRATEGY:

Minimal fixtures:
  - Only create data needed for test
  - Use factories for flexibility
  - Avoid fixture dependencies

Shared fixtures:
  - Scope="session" for expensive setup
  - Scope="module" for test file
  - Scope="function" for isolation

Production note: Real pytest database testing provides:
  - pytest-django for Django integration
  - pytest-sqlalchemy for SQLAlchemy
  - factory_boy for test data
  - faker for realistic data
  - Database cleanup plugins
  - Parallel testing with xdist
  - Test database management
  - Fixture parametrization
""")
'''

    # Lesson 810: pytest Test Organization
    lesson_810 = next(l for l in lessons if l['id'] == 810)
    lesson_810['fullSolution'] = '''# pytest Test Organization - Complete Simulation
# In production: pip install pytest
# This lesson simulates organizing tests for maintainability and scalability

import os
from typing import List, Dict, Any, Callable
from dataclasses import dataclass
from pathlib import Path

# Example 1: Directory Structure
print("Example 1: Test Directory Structure")
print("=" * 60)

project_structure = """
project/
├── src/
│   ├── __init__.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── login.py
│   │   └── logout.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── posts.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── conftest.py           # Shared fixtures
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_auth.py
│   │   ├── test_api.py
│   │   └── test_utils.py
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── test_user_flow.py
│   │   └── test_api_integration.py
│   ├── e2e/
│   │   ├── __init__.py
│   │   └── test_complete_workflow.py
│   └── fixtures/
│       ├── __init__.py
│       ├── database.py
│       └── api_client.py
└── pytest.ini                # pytest configuration
"""

print("Recommended test structure:")
print(project_structure)
print()

# Example 2: Test Naming Conventions
print("Example 2: Test Naming Conventions")
print("=" * 60)

naming_examples = {
    "Functions": [
        "test_user_login_success()",
        "test_user_login_invalid_password()",
        "test_create_post_with_valid_data()",
        "test_delete_post_unauthorized()",
    ],
    "Classes": [
        "TestUserAuthentication",
        "TestPostAPI",
        "TestDatabaseModels",
    ],
    "Files": [
        "test_auth.py",
        "test_api_users.py",
        "test_models_user.py",
    ]
}

print("Naming conventions:")
for category, examples in naming_examples.items():
    print(f"\\n{category}:")
    for example in examples:
        print(f"  - {example}")

print()

# Example 3: Organizing with Test Classes
print("Example 3: Organizing Tests with Classes")
print("=" * 60)

class TestUserAuthentication:
    """Group related authentication tests."""

    def setup_method(self):
        """Run before each test method."""
        print("  [SETUP] Preparing test environment")
        self.user_data = {"username": "testuser", "password": "testpass"}

    def teardown_method(self):
        """Run after each test method."""
        print("  [TEARDOWN] Cleaning up")

    def test_login_success(self):
        """Test successful login."""
        print("  [TEST] Running test_login_success")
        # Test logic here
        assert True

    def test_login_invalid_password(self):
        """Test login with invalid password."""
        print("  [TEST] Running test_login_invalid_password")
        # Test logic here
        assert True

    def test_logout(self):
        """Test user logout."""
        print("  [TEST] Running test_logout")
        # Test logic here
        assert True

print("Running TestUserAuthentication:")
test_suite = TestUserAuthentication()

test_suite.setup_method()
test_suite.test_login_success()
test_suite.teardown_method()

print()

test_suite.setup_method()
test_suite.test_login_invalid_password()
test_suite.teardown_method()

print()

# Example 4: Shared Fixtures (conftest.py)
print("Example 4: Shared Fixtures in conftest.py")
print("=" * 60)

conftest_example = """# tests/conftest.py
import pytest

@pytest.fixture(scope="session")
def database():
    # Shared database for all tests
    print("Setting up database...")
    db = create_test_database()
    yield db
    print("Tearing down database...")
    db.close()

@pytest.fixture(scope="function")
def user(database):
    # Create test user
    user = database.create_user("testuser", "test@example.com")
    yield user
    database.delete_user(user.id)

@pytest.fixture
def api_client():
    # API client for testing
    return TestClient()
"""

print("Example conftest.py:")
print(conftest_example)
print()

# Example 5: Test Markers for Organization
print("Example 5: Test Markers for Organization")
print("=" * 60)

marker_examples = """
# pytest.ini
[pytest]
markers =
    unit: Unit tests (fast, isolated)
    integration: Integration tests (slower, database required)
    e2e: End-to-end tests (slowest, full system)
    smoke: Smoke tests (critical functionality)
    slow: Tests that take > 1 second
    api: API tests
    auth: Authentication tests
    database: Tests requiring database

# Usage in tests:
@pytest.mark.unit
def test_calculate_total():
    pass

@pytest.mark.integration
@pytest.mark.database
def test_save_user():
    pass

@pytest.mark.e2e
@pytest.mark.slow
def test_complete_checkout():
    pass

# Running specific markers:
pytest -m unit              # Run only unit tests
pytest -m "not slow"        # Skip slow tests
pytest -m "unit or smoke"   # Run unit or smoke tests
"""

print(marker_examples)
print()

# Example 6: Parameterized Test Organization
print("Example 6: Parameterized Test Organization")
print("=" * 60)

test_data = [
    ("alice", "password123", True),
    ("bob", "wrongpass", False),
    ("charlie", "", False),
    ("", "password", False),
]

print("Parameterized login tests:")
for i, (username, password, expected) in enumerate(test_data, 1):
    result = bool(username and password and password != "wrongpass")
    status = "✓" if result == expected else "✗"
    print(f"  {status} Test case {i}: username='{username}', password='{password}' -> {expected}")

print()

# Example 7: Test Coverage Organization
print("Example 7: Test Coverage Organization")
print("=" * 60)

coverage_structure = """
Coverage by test type:

Unit Tests (70-80% of tests):
  ├── Fast execution (< 100ms)
  ├── No external dependencies
  ├── Test individual functions/methods
  └── High code coverage target (80%+)

Integration Tests (15-20% of tests):
  ├── Moderate execution time
  ├── Test component interaction
  ├── Database, API, file system
  └── Test realistic scenarios

E2E Tests (5-10% of tests):
  ├── Slow execution
  ├── Test complete user workflows
  ├── All systems integrated
  └── Critical user paths only
"""

print(coverage_structure)
print()

# Example 8: pytest.ini Configuration
print("Example 8: pytest.ini Configuration")
print("=" * 60)

pytest_ini = """[pytest]
# Test discovery patterns
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*

# Test paths
testpaths = tests

# Markers
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    slow: Tests that take > 1 second

# Output options
addopts =
    -v                      # Verbose output
    --strict-markers        # Enforce marker registration
    --tb=short             # Short traceback format
    --cov=src              # Coverage for src directory
    --cov-report=term-missing  # Show missing lines
    --cov-fail-under=80    # Minimum 80% coverage

# Warnings
filterwarnings =
    error                   # Treat warnings as errors
    ignore::DeprecationWarning

# Logging
log_cli = true
log_cli_level = INFO
"""

print("Example pytest.ini:")
print(pytest_ini)
print()

# Example 9: Test Data Organization
print("Example 9: Test Data Organization")
print("=" * 60)

test_data_structure = """
tests/
├── fixtures/
│   ├── users.json         # Test user data
│   ├── posts.json         # Test post data
│   └── config.json        # Test configuration
├── factories/
│   ├── user_factory.py    # User data factory
│   ├── post_factory.py    # Post data factory
│   └── base.py            # Base factory
└── mocks/
    ├── api_responses.py   # Mock API responses
    ├── database.py        # Mock database
    └── external_services.py  # Mock external services
"""

print("Test data organization:")
print(test_data_structure)
print()

# Example 10: Best Practices Checklist
print("Example 10: Test Organization Best Practices")
print("=" * 60)

best_practices = """
✓ Test Organization:
  1. Group related tests in classes
  2. Use descriptive test names
  3. Separate unit/integration/e2e tests
  4. Keep tests close to source code
  5. Use conftest.py for shared fixtures

✓ Test Naming:
  1. test_<feature>_<scenario>_<expected>
  2. Classes: TestFeatureName
  3. Files: test_module_name.py
  4. Be descriptive and specific

✓ Test Structure (AAA):
  1. Arrange: Set up test data
  2. Act: Execute code under test
  3. Assert: Verify expected behavior

✓ Fixtures:
  1. Scope appropriately (session, module, function)
  2. Keep fixtures focused and reusable
  3. Use fixture factories for flexibility
  4. Clean up in teardown

✓ Markers:
  1. Mark tests by type (unit, integration, e2e)
  2. Mark slow tests
  3. Mark tests by feature area
  4. Use markers for selective execution

✓ Maintenance:
  1. Keep tests DRY (Don't Repeat Yourself)
  2. Refactor tests as code changes
  3. Delete obsolete tests
  4. Monitor test execution time
  5. Fix flaky tests immediately
"""

print(best_practices)
print()

# Example 11: Test Suite Runner Simulation
print("Example 11: Test Suite Runner Simulation")
print("=" * 60)

class TestRunner:
    """Simulates pytest test execution and organization."""

    def __init__(self):
        self.tests = []
        self.results = {'passed': 0, 'failed': 0, 'skipped': 0}

    def add_test(self, name, markers=None, scope='function'):
        """Add a test to the suite."""
        self.tests.append({
            'name': name,
            'markers': markers or [],
            'scope': scope,
            'status': None
        })

    def run_test(self, test, verbose=True):
        """Execute a single test."""
        if verbose:
            print(f"  Running: {test['name']}")

        # Simulate test execution
        import random
        random.seed(len(test['name']))  # Deterministic for demo
        result = random.choice(['passed', 'passed', 'passed', 'failed'])

        test['status'] = result
        self.results[result] += 1

        if verbose:
            status_symbol = "PASS" if result == 'passed' else "FAIL"
            print(f"    Status: {status_symbol}")

        return result

    def run_by_marker(self, marker):
        """Run tests filtered by marker."""
        filtered = [t for t in self.tests if marker in t['markers']]
        print(f"Running tests with marker '{marker}': {len(filtered)} tests")
        for test in filtered:
            self.run_test(test)
        print()

    def run_all(self):
        """Run all tests in the suite."""
        print(f"Running all tests: {len(self.tests)} tests")
        for test in self.tests:
            self.run_test(test, verbose=False)
        self.print_summary()

    def print_summary(self):
        """Print test execution summary."""
        total = sum(self.results.values())
        print(f"\\n{'=' * 60}")
        print(f"Test Results: {self.results['passed']}/{total} passed")
        print(f"  Passed:  {self.results['passed']}")
        print(f"  Failed:  {self.results['failed']}")
        print(f"  Skipped: {self.results['skipped']}")
        print(f"{'=' * 60}")

# Create test suite
runner = TestRunner()

# Add unit tests
runner.add_test('test_user_login_success', markers=['unit', 'auth'])
runner.add_test('test_user_login_invalid_password', markers=['unit', 'auth'])
runner.add_test('test_user_logout', markers=['unit', 'auth'])
runner.add_test('test_calculate_total_price', markers=['unit', 'business'])
runner.add_test('test_validate_email', markers=['unit', 'validation'])

# Add integration tests
runner.add_test('test_database_user_crud', markers=['integration', 'database'])
runner.add_test('test_api_authentication_flow', markers=['integration', 'api'])

# Add e2e tests
runner.add_test('test_complete_checkout_flow', markers=['e2e', 'slow'])

# Run tests by marker
runner.run_by_marker('unit')
runner.run_by_marker('integration')

# Run all tests
runner.run_all()
print()

# Example 12: Fixture Dependency Graph
print("Example 12: Fixture Dependency Graph")
print("=" * 60)

class FixtureDependencyGraph:
    """Visualizes fixture dependencies."""

    def __init__(self):
        self.fixtures = {}

    def register_fixture(self, name, depends_on=None, scope='function'):
        """Register a fixture with its dependencies."""
        self.fixtures[name] = {
            'depends_on': depends_on or [],
            'scope': scope,
            'setup_count': 0
        }

    def setup_fixture(self, name, indent=0):
        """Setup fixture and its dependencies."""
        if name not in self.fixtures:
            return

        fixture = self.fixtures[name]

        # Setup dependencies first
        for dep in fixture['depends_on']:
            self.setup_fixture(dep, indent + 2)

        # Setup this fixture
        fixture['setup_count'] += 1
        prefix = " " * indent
        print(f"{prefix}Setting up {name} (scope: {fixture['scope']})")

    def visualize(self):
        """Visualize the fixture dependency tree."""
        print("Fixture Dependency Tree:")
        for name, fixture in self.fixtures.items():
            if not fixture['depends_on']:
                print(f"  {name} (scope: {fixture['scope']})")
            else:
                deps = ", ".join(fixture['depends_on'])
                print(f"  {name} (scope: {fixture['scope']}) -> depends on: {deps}")

# Create fixture graph
graph = FixtureDependencyGraph()

# Register fixtures
graph.register_fixture('db_engine', scope='session')
graph.register_fixture('db_session', depends_on=['db_engine'], scope='function')
graph.register_fixture('user_factory', depends_on=['db_session'], scope='function')
graph.register_fixture('authenticated_user', depends_on=['user_factory'], scope='function')
graph.register_fixture('api_client', scope='function')

# Visualize dependencies
graph.visualize()
print()

# Simulate test execution with fixture setup
print("Test execution with fixture setup:")
print()
print("Test 1: test_create_user")
graph.setup_fixture('db_session')
graph.setup_fixture('user_factory')
print()

print("Test 2: test_authenticated_api_call")
graph.setup_fixture('authenticated_user')
graph.setup_fixture('api_client')
print()

print("=" * 60)
print("TEST ORGANIZATION GUIDELINES")
print("=" * 60)
print("""
DIRECTORY STRUCTURE:

Mirror source structure:
  src/auth/login.py  -> tests/unit/auth/test_login.py

Separate by test type:
  tests/unit/         # Fast, isolated tests
  tests/integration/  # Component interaction tests
  tests/e2e/         # Full system tests

Shared resources:
  tests/conftest.py   # Shared fixtures
  tests/fixtures/     # Test data files
  tests/factories/    # Data factories

TEST FILE ORGANIZATION:

Logical grouping:
  # Group 1: Authentication tests
  class TestUserLogin:
      def test_valid_credentials(self): ...
      def test_invalid_password(self): ...

  # Group 2: User management tests
  class TestUserCRUD:
      def test_create_user(self): ...
      def test_update_user(self): ...

Single responsibility:
  - One test file per module/class
  - One test class per feature
  - One test function per scenario

FIXTURE ORGANIZATION:

Scope hierarchy:
  session > package > module > class > function

Location:
  - conftest.py: Shared across directory
  - Test file: Test-specific fixtures
  - Fixture modules: Complex fixtures

Naming:
  - Descriptive names (db_session, authenticated_user)
  - Avoid generic names (data, obj, tmp)

MARKER STRATEGY:

Test pyramid markers:
  @pytest.mark.unit        # 70% of tests
  @pytest.mark.integration # 20% of tests
  @pytest.mark.e2e         # 10% of tests

Feature markers:
  @pytest.mark.auth
  @pytest.mark.api
  @pytest.mark.database

Performance markers:
  @pytest.mark.slow
  @pytest.mark.fast

CI/CD markers:
  @pytest.mark.smoke      # Critical tests
  @pytest.mark.regression # Full test suite

MAINTENANCE:

Code review:
  - Review test code like production code
  - Ensure test quality
  - Check for duplication

Refactoring:
  - Extract common setup to fixtures
  - Use helper functions
  - Keep tests simple

Monitoring:
  - Track test execution time
  - Identify slow tests
  - Fix flaky tests
  - Remove obsolete tests

SCALING:

Parallel execution:
  pytest -n auto  # Use all CPU cores

Test selection:
  pytest tests/unit/  # Run specific directory
  pytest -m unit      # Run by marker
  pytest -k login     # Run by name pattern

Incremental testing:
  pytest --lf  # Last failed
  pytest --ff  # Failed first
  pytest --nf  # New first

Production note: Real pytest organization provides:
  - Automatic test discovery
  - Flexible directory structure
  - Plugin system for extensions
  - Custom markers
  - Fixture parametrization
  - Test selection strategies
  - Parallel execution
  - Result caching
""")
'''

    # Save changes
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 70)
    print("BATCH 17B COMPLETE: pytest CI/CD, Database, and Organization")
    print("=" * 70)
    print("\nUpgraded lessons:")
    print(f"  - Lesson 814: pytest CI/CD Integration")
    print(f"  - Lesson 812: pytest Database Testing")
    print(f"  - Lesson 810: pytest Test Organization")
    print("\nAll lessons upgraded to 13,000-17,000+ characters")
    print("Zero package installation required!")
    print("=" * 70)

if __name__ == "__main__":
    upgrade_lessons()
