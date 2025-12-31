"""
Upgrade pytest batch 18: Async Testing, Coverage Reports, Integration Testing, Parametrize
Upgrade 4 pytest lessons to 13,000-17,000+ characters
Zero package installation required!
"""

import json
import os

def upgrade_lessons():
    lessons_file = os.path.join('public', 'lessons-python.json')

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Lesson 808: pytest - Async Testing
    lesson_808 = next(l for l in lessons if l['id'] == 808)
    lesson_808['fullSolution'] = '''# pytest Async Testing - Complete Simulation
# In production: pip install pytest pytest-asyncio
# This lesson simulates async testing with pytest for concurrent operations

import asyncio
import time
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass
from datetime import datetime

# Example 1: Basic Async Test Pattern
print("Example 1: Basic Async Test Pattern")
print("=" * 60)

async def fetch_user(user_id: int) -> Dict[str, Any]:
    """Simulate async API call to fetch user data."""
    await asyncio.sleep(0.1)  # Simulate network delay
    return {
        'id': user_id,
        'name': f'User{user_id}',
        'email': f'user{user_id}@example.com',
        'active': True
    }

async def test_fetch_user():
    """Test async function that fetches user data."""
    print("  Running: test_fetch_user")

    # Arrange
    user_id = 1

    # Act
    result = await fetch_user(user_id)

    # Assert
    assert result['id'] == user_id
    assert result['name'] == 'User1'
    assert result['email'] == 'user1@example.com'
    assert result['active'] is True

    print("    PASS: User data fetched correctly")

# Run the test
asyncio.run(test_fetch_user())
print()

# Example 2: Testing Multiple Concurrent Operations
print("Example 2: Testing Concurrent Operations")
print("=" * 60)

async def process_item(item_id: int, delay: float = 0.05) -> Dict[str, Any]:
    """Simulate async item processing."""
    await asyncio.sleep(delay)
    return {
        'item_id': item_id,
        'processed': True,
        'timestamp': time.time()
    }

async def test_concurrent_processing():
    """Test processing multiple items concurrently."""
    print("  Running: test_concurrent_processing")

    # Arrange
    item_ids = [1, 2, 3, 4, 5]
    start_time = time.time()

    # Act - Process all items concurrently
    tasks = [process_item(item_id) for item_id in item_ids]
    results = await asyncio.gather(*tasks)

    elapsed = time.time() - start_time

    # Assert
    assert len(results) == 5
    assert all(r['processed'] for r in results)
    assert elapsed < 0.3  # Should be much faster than sequential (5 * 0.05 = 0.25s)

    print(f"    PASS: Processed {len(results)} items in {elapsed:.3f}s")
    print(f"    (Concurrent execution faster than sequential)")

asyncio.run(test_concurrent_processing())
print()

# Example 3: Async Context Managers
print("Example 3: Async Context Managers")
print("=" * 60)

class AsyncDatabaseConnection:
    """Simulates async database connection."""

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connected = False

    async def __aenter__(self):
        """Async context manager entry."""
        await asyncio.sleep(0.05)  # Simulate connection setup
        self.connected = True
        print(f"    Connected to {self.db_name}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await asyncio.sleep(0.02)  # Simulate cleanup
        self.connected = False
        print(f"    Disconnected from {self.db_name}")

    async def query(self, sql: str) -> List[Dict[str, Any]]:
        """Execute async query."""
        if not self.connected:
            raise RuntimeError("Not connected to database")
        await asyncio.sleep(0.03)
        return [{'id': 1, 'data': 'result'}]

async def test_async_context_manager():
    """Test async context manager for database connection."""
    print("  Running: test_async_context_manager")

    # Use async context manager
    async with AsyncDatabaseConnection('test_db') as db:
        # Assert connection is established
        assert db.connected is True

        # Execute query
        results = await db.query("SELECT * FROM users")
        assert len(results) == 1
        assert results[0]['id'] == 1

    # Assert connection is closed after context
    assert db.connected is False
    print("    PASS: Async context manager works correctly")

asyncio.run(test_async_context_manager())
print()

# Example 4: Exception Handling in Async Tests
print("Example 4: Exception Handling in Async Tests")
print("=" * 60)

async def risky_operation(should_fail: bool = False):
    """Async operation that may raise exception."""
    await asyncio.sleep(0.02)
    if should_fail:
        raise ValueError("Operation failed")
    return "Success"

async def test_async_exception_handling():
    """Test exception handling in async operations."""
    print("  Running: test_async_exception_handling")

    # Test successful operation
    result = await risky_operation(should_fail=False)
    assert result == "Success"
    print("    PASS: Successful operation works")

    # Test exception is raised
    exception_raised = False
    try:
        await risky_operation(should_fail=True)
    except ValueError as e:
        exception_raised = True
        assert str(e) == "Operation failed"

    assert exception_raised is True
    print("    PASS: Exception handling works correctly")

asyncio.run(test_async_exception_handling())
print()

# Example 5: Async Fixtures Simulation
print("Example 5: Async Fixtures Simulation")
print("=" * 60)

class AsyncFixture:
    """Simulates pytest-asyncio fixture."""

    def __init__(self):
        self.setup_complete = False
        self.teardown_complete = False

    async def setup(self):
        """Async setup for test."""
        print("    [FIXTURE] Setting up async resources...")
        await asyncio.sleep(0.05)
        self.setup_complete = True
        return self

    async def teardown(self):
        """Async teardown after test."""
        print("    [FIXTURE] Tearing down async resources...")
        await asyncio.sleep(0.02)
        self.teardown_complete = True

async def test_with_async_fixture():
    """Test using async fixture."""
    print("  Running: test_with_async_fixture")

    # Setup fixture
    fixture = await AsyncFixture().setup()

    try:
        # Test logic
        assert fixture.setup_complete is True
        print("    PASS: Test executed with async fixture")
    finally:
        # Teardown fixture
        await fixture.teardown()
        assert fixture.teardown_complete is True

asyncio.run(test_with_async_fixture())
print()

# Example 6: Testing Async Iterators
print("Example 6: Testing Async Iterators")
print("=" * 60)

class AsyncDataStream:
    """Simulates async data stream."""

    def __init__(self, count: int):
        self.count = count
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.count:
            raise StopAsyncIteration

        await asyncio.sleep(0.01)
        self.current += 1
        return {'index': self.current, 'data': f'item_{self.current}'}

async def test_async_iterator():
    """Test async iterator."""
    print("  Running: test_async_iterator")

    items = []
    async for item in AsyncDataStream(3):
        items.append(item)

    # Assert all items collected
    assert len(items) == 3
    assert items[0]['index'] == 1
    assert items[2]['data'] == 'item_3'

    print(f"    PASS: Collected {len(items)} items from async stream")

asyncio.run(test_async_iterator())
print()

# Example 7: Timeout Testing
print("Example 7: Timeout Testing")
print("=" * 60)

async def slow_operation(duration: float):
    """Operation that takes specific time."""
    await asyncio.sleep(duration)
    return "Completed"

async def test_operation_timeout():
    """Test operation completes within timeout."""
    print("  Running: test_operation_timeout")

    # Test operation completes in time
    try:
        result = await asyncio.wait_for(slow_operation(0.05), timeout=0.1)
        assert result == "Completed"
        print("    PASS: Operation completed within timeout")
    except asyncio.TimeoutError:
        print("    FAIL: Operation timed out")
        raise

    # Test operation times out
    timeout_occurred = False
    try:
        await asyncio.wait_for(slow_operation(0.2), timeout=0.05)
    except asyncio.TimeoutError:
        timeout_occurred = True

    assert timeout_occurred is True
    print("    PASS: Timeout detection works correctly")

asyncio.run(test_operation_timeout())
print()

# Example 8: Async Test Suite Runner
print("Example 8: Async Test Suite Runner")
print("=" * 60)

@dataclass
class AsyncTestResult:
    """Result of async test execution."""
    test_name: str
    passed: bool
    duration: float
    error: Optional[str] = None

class AsyncTestRunner:
    """Runs async tests and collects results."""

    def __init__(self):
        self.results: List[AsyncTestResult] = []

    async def run_test(self, test_func: Callable, test_name: str) -> AsyncTestResult:
        """Run a single async test."""
        start = time.time()

        try:
            await test_func()
            duration = time.time() - start
            result = AsyncTestResult(test_name, True, duration)
            print(f"  PASS: {test_name} ({duration:.3f}s)")
        except Exception as e:
            duration = time.time() - start
            result = AsyncTestResult(test_name, False, duration, str(e))
            print(f"  FAIL: {test_name} - {e}")

        self.results.append(result)
        return result

    async def run_all(self, tests: List[tuple]):
        """Run all tests."""
        for test_func, test_name in tests:
            await self.run_test(test_func, test_name)

    def print_summary(self):
        """Print test execution summary."""
        passed = sum(1 for r in self.results if r.passed)
        total = len(self.results)
        total_time = sum(r.duration for r in self.results)

        print(f"\\n{'=' * 60}")
        print(f"Test Summary: {passed}/{total} passed")
        print(f"Total time: {total_time:.3f}s")
        print(f"{'=' * 60}")

# Define test functions
async def sample_test_1():
    await asyncio.sleep(0.01)
    assert 1 + 1 == 2

async def sample_test_2():
    await asyncio.sleep(0.02)
    assert "hello".upper() == "HELLO"

async def sample_test_3():
    await asyncio.sleep(0.01)
    result = await fetch_user(1)
    assert result['id'] == 1

async def run_test_suite():
    """Run complete async test suite."""
    runner = AsyncTestRunner()

    tests = [
        (sample_test_1, "test_arithmetic"),
        (sample_test_2, "test_string_operation"),
        (sample_test_3, "test_async_fetch"),
    ]

    await runner.run_all(tests)
    runner.print_summary()

asyncio.run(run_test_suite())
print()

# Example 9: Mocking Async Dependencies
print("Example 9: Mocking Async Dependencies")
print("=" * 60)

class AsyncAPIClient:
    """Simulates external async API client."""

    async def fetch_data(self, endpoint: str) -> Dict[str, Any]:
        """Fetch data from external API."""
        await asyncio.sleep(0.5)  # Slow external API
        return {"endpoint": endpoint, "data": "real data"}

class MockAsyncAPIClient:
    """Mock version of async API client."""

    def __init__(self, mock_data: Dict[str, Any]):
        self.mock_data = mock_data
        self.call_count = 0

    async def fetch_data(self, endpoint: str) -> Dict[str, Any]:
        """Return mock data immediately."""
        self.call_count += 1
        await asyncio.sleep(0.01)  # Minimal delay
        return self.mock_data

async def process_api_data(api_client):
    """Function that uses API client."""
    data = await api_client.fetch_data("/users/1")
    return data['data'].upper()

async def test_with_mock_api():
    """Test using mocked async API client."""
    print("  Running: test_with_mock_api")

    # Create mock client
    mock_client = MockAsyncAPIClient({"data": "mocked data"})

    # Test with mock
    result = await process_api_data(mock_client)

    # Assert
    assert result == "MOCKED DATA"
    assert mock_client.call_count == 1

    print("    PASS: Mock async API works correctly")

asyncio.run(test_with_mock_api())
print()

# Example 10: Testing Async Retries
print("Example 10: Testing Async Retries")
print("=" * 60)

class RetryableAsyncOperation:
    """Async operation with retry logic."""

    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries
        self.attempt_count = 0

    async def execute(self, should_fail: bool = False) -> str:
        """Execute operation with retry logic."""
        for attempt in range(self.max_retries):
            self.attempt_count += 1
            try:
                await asyncio.sleep(0.01)

                if should_fail and attempt < 2:
                    raise RuntimeError(f"Attempt {attempt + 1} failed")

                return f"Success on attempt {attempt + 1}"
            except RuntimeError as e:
                if attempt == self.max_retries - 1:
                    raise
                print(f"    Retry {attempt + 1}: {e}")
                await asyncio.sleep(0.05)  # Backoff

async def test_retry_logic():
    """Test async retry behavior."""
    print("  Running: test_retry_logic")

    # Test successful operation
    operation = RetryableAsyncOperation(max_retries=3)
    result = await operation.execute(should_fail=False)
    assert result == "Success on attempt 1"
    assert operation.attempt_count == 1
    print("    PASS: Immediate success works")

    # Test operation that succeeds after retries
    operation2 = RetryableAsyncOperation(max_retries=3)
    result2 = await operation2.execute(should_fail=True)
    assert "Success on attempt 3" in result2
    assert operation2.attempt_count == 3
    print("    PASS: Retry logic works correctly")

asyncio.run(test_retry_logic())
print()

print("=" * 60)
print("ASYNC TESTING BEST PRACTICES")
print("=" * 60)
print("""
ASYNC TEST PATTERNS:

Basic async test:
  async def test_example():
      result = await async_function()
      assert result == expected

Concurrent testing:
  tasks = [async_op(i) for i in range(10)]
  results = await asyncio.gather(*tasks)

Timeout testing:
  result = await asyncio.wait_for(
      slow_operation(),
      timeout=5.0
  )

FIXTURES:

Async setup/teardown:
  @pytest.fixture
  async def async_db():
      db = await connect_db()
      yield db
      await db.close()

Async context manager:
  async with AsyncResource() as resource:
      await resource.do_something()

COMMON PATTERNS:

Testing exceptions:
  with pytest.raises(ValueError):
      await async_function()

Testing multiple scenarios:
  @pytest.mark.parametrize("input,expected", [...])
  async def test_async(input, expected):
      result = await process(input)
      assert result == expected

Mocking async calls:
  async def mock_api_call():
      return {"mocked": "data"}

PERFORMANCE:

Concurrent execution:
  - Use asyncio.gather() for parallel tests
  - Measure total execution time
  - Ensure proper cleanup

Timeouts:
  - Set reasonable timeouts
  - Prevent hanging tests
  - Use asyncio.wait_for()

Production note: Real pytest-asyncio provides:
  - @pytest.mark.asyncio decorator
  - Automatic event loop management
  - Async fixture support
  - Integration with pytest features
  - Async test discovery
  - Proper cleanup handling
""")
'''

    # Lesson 809: pytest - Coverage Reports
    lesson_809 = next(l for l in lessons if l['id'] == 809)
    lesson_809['fullSolution'] = '''# pytest Coverage Reports - Complete Simulation
# In production: pip install pytest pytest-cov
# This lesson simulates code coverage reporting and analysis

import os
import json
from typing import Dict, List, Set, Any, Optional
from dataclasses import dataclass, field
from pathlib import Path

# Example 1: Basic Coverage Tracking
print("Example 1: Basic Coverage Tracking")
print("=" * 60)

class CodeLine:
    """Represents a line of code."""

    def __init__(self, line_num: int, content: str):
        self.line_num = line_num
        self.content = content
        self.executed = False
        self.execution_count = 0

    def execute(self):
        """Mark line as executed."""
        self.executed = True
        self.execution_count += 1

class CoverageTracker:
    """Tracks code coverage during test execution."""

    def __init__(self, module_name: str):
        self.module_name = module_name
        self.lines: Dict[int, CodeLine] = {}
        self.total_lines = 0
        self.executed_lines = 0

    def add_line(self, line_num: int, content: str):
        """Add a line to track."""
        self.lines[line_num] = CodeLine(line_num, content)
        self.total_lines += 1

    def mark_executed(self, line_num: int):
        """Mark a line as executed."""
        if line_num in self.lines:
            if not self.lines[line_num].executed:
                self.executed_lines += 1
            self.lines[line_num].execute()

    def get_coverage_percentage(self) -> float:
        """Calculate coverage percentage."""
        if self.total_lines == 0:
            return 0.0
        return (self.executed_lines / self.total_lines) * 100

    def get_missed_lines(self) -> List[int]:
        """Get list of lines not executed."""
        return [num for num, line in self.lines.items() if not line.executed]

# Create coverage tracker
tracker = CoverageTracker("my_module.py")

# Add code lines
tracker.add_line(1, "def calculate_total(items):")
tracker.add_line(2, "    if not items:")
tracker.add_line(3, "        return 0")
tracker.add_line(4, "    return sum(item.price for item in items)")
tracker.add_line(5, "")
tracker.add_line(6, "def apply_discount(total, discount):")
tracker.add_line(7, "    if discount > 0:")
tracker.add_line(8, "        return total * (1 - discount)")
tracker.add_line(9, "    return total")

# Simulate test execution
print("Simulating test execution...")
tracker.mark_executed(1)  # Function definition
tracker.mark_executed(2)  # if not items
tracker.mark_executed(4)  # return sum - line 3 not executed
tracker.mark_executed(6)  # Function definition
tracker.mark_executed(9)  # return total - lines 7-8 not executed

coverage = tracker.get_coverage_percentage()
missed = tracker.get_missed_lines()

print(f"Coverage: {coverage:.1f}%")
print(f"Executed: {tracker.executed_lines}/{tracker.total_lines} lines")
print(f"Missed lines: {missed}")
print()

# Example 2: Branch Coverage
print("Example 2: Branch Coverage Analysis")
print("=" * 60)

@dataclass
class Branch:
    """Represents a code branch."""
    branch_id: str
    condition: str
    executed: bool = False

class BranchCoverageTracker:
    """Tracks branch coverage."""

    def __init__(self):
        self.branches: Dict[str, Branch] = {}

    def add_branch(self, branch_id: str, condition: str):
        """Add a branch to track."""
        self.branches[branch_id] = Branch(branch_id, condition)

    def mark_branch_executed(self, branch_id: str):
        """Mark a branch as executed."""
        if branch_id in self.branches:
            self.branches[branch_id].executed = True

    def get_branch_coverage(self) -> float:
        """Calculate branch coverage percentage."""
        if not self.branches:
            return 0.0
        executed = sum(1 for b in self.branches.values() if b.executed)
        return (executed / len(self.branches)) * 100

    def get_missed_branches(self) -> List[Branch]:
        """Get branches not executed."""
        return [b for b in self.branches.values() if not b.executed]

# Create branch tracker
branch_tracker = BranchCoverageTracker()

# Add branches from example code
branch_tracker.add_branch("if_items_true", "if not items: True")
branch_tracker.add_branch("if_items_false", "if not items: False")
branch_tracker.add_branch("if_discount_true", "if discount > 0: True")
branch_tracker.add_branch("if_discount_false", "if discount > 0: False")

# Simulate test execution
branch_tracker.mark_branch_executed("if_items_false")
branch_tracker.mark_branch_executed("if_discount_false")

branch_coverage = branch_tracker.get_branch_coverage()
missed_branches = branch_tracker.get_missed_branches()

print(f"Branch Coverage: {branch_coverage:.1f}%")
print(f"Missed branches:")
for branch in missed_branches:
    print(f"  - {branch.branch_id}: {branch.condition}")
print()

# Example 3: Coverage Report Generation
print("Example 3: Coverage Report Generation")
print("=" * 60)

@dataclass
class ModuleCoverage:
    """Coverage data for a module."""
    module_name: str
    total_statements: int
    covered_statements: int
    missing_lines: List[int] = field(default_factory=list)

    @property
    def coverage_percentage(self) -> float:
        """Calculate coverage percentage."""
        if self.total_statements == 0:
            return 0.0
        return (self.covered_statements / self.total_statements) * 100

class CoverageReport:
    """Generates coverage reports."""

    def __init__(self):
        self.modules: Dict[str, ModuleCoverage] = {}

    def add_module(self, module_coverage: ModuleCoverage):
        """Add module coverage data."""
        self.modules[module_coverage.module_name] = module_coverage

    def get_total_coverage(self) -> float:
        """Calculate overall coverage percentage."""
        total_statements = sum(m.total_statements for m in self.modules.values())
        covered_statements = sum(m.covered_statements for m in self.modules.values())

        if total_statements == 0:
            return 0.0
        return (covered_statements / total_statements) * 100

    def generate_terminal_report(self) -> str:
        """Generate terminal-style coverage report."""
        lines = []
        lines.append("=" * 70)
        lines.append("COVERAGE REPORT")
        lines.append("=" * 70)
        lines.append(f"{'Module':<30} {'Stmts':>8} {'Miss':>8} {'Cover':>8}")
        lines.append("-" * 70)

        for module in self.modules.values():
            miss = module.total_statements - module.covered_statements
            cover = module.coverage_percentage
            lines.append(
                f"{module.module_name:<30} {module.total_statements:>8} "
                f"{miss:>8} {cover:>7.0f}%"
            )

        lines.append("-" * 70)
        total_cover = self.get_total_coverage()
        lines.append(f"{'TOTAL':<30} {'':<8} {'':<8} {total_cover:>7.0f}%")
        lines.append("=" * 70)

        return "\\n".join(lines)

    def generate_html_snippet(self) -> str:
        """Generate HTML coverage report snippet."""
        html = '<div class="coverage-report">\\n'
        html += '  <h2>Coverage Report</h2>\\n'
        html += '  <table>\\n'
        html += '    <tr><th>Module</th><th>Coverage</th><th>Missing</th></tr>\\n'

        for module in self.modules.values():
            color = "green" if module.coverage_percentage >= 80 else "red"
            html += f'    <tr>\\n'
            html += f'      <td>{module.module_name}</td>\\n'
            html += f'      <td style="color: {color}">{module.coverage_percentage:.1f}%</td>\\n'
            html += f'      <td>{", ".join(map(str, module.missing_lines))}</td>\\n'
            html += f'    </tr>\\n'

        html += '  </table>\\n'
        html += '</div>'

        return html

# Create coverage report
report = CoverageReport()

# Add module coverage data
report.add_module(ModuleCoverage(
    module_name="auth.py",
    total_statements=50,
    covered_statements=45,
    missing_lines=[23, 24, 35, 48, 49]
))

report.add_module(ModuleCoverage(
    module_name="api.py",
    total_statements=80,
    covered_statements=72,
    missing_lines=[15, 16, 33, 55, 67, 78, 79, 80]
))

report.add_module(ModuleCoverage(
    module_name="utils.py",
    total_statements=30,
    covered_statements=30,
    missing_lines=[]
))

# Generate and print report
print(report.generate_terminal_report())
print()

# Example 4: Coverage Thresholds
print("Example 4: Coverage Thresholds")
print("=" * 60)

class CoverageThreshold:
    """Enforces coverage thresholds."""

    def __init__(self, minimum_coverage: float = 80.0):
        self.minimum_coverage = minimum_coverage

    def check_threshold(self, coverage: float) -> tuple[bool, str]:
        """Check if coverage meets threshold."""
        if coverage >= self.minimum_coverage:
            return True, f"Coverage {coverage:.1f}% meets threshold {self.minimum_coverage}%"
        else:
            diff = self.minimum_coverage - coverage
            return False, f"Coverage {coverage:.1f}% is {diff:.1f}% below threshold {self.minimum_coverage}%"

    def enforce(self, coverage: float):
        """Enforce threshold, raise exception if not met."""
        passed, message = self.check_threshold(coverage)
        print(f"  {message}")

        if not passed:
            raise ValueError(f"Coverage below threshold: {coverage:.1f}% < {self.minimum_coverage}%")

# Test threshold enforcement
threshold = CoverageThreshold(minimum_coverage=80.0)

# Test passing coverage
try:
    threshold.enforce(85.5)
    print("  Result: PASS")
except ValueError as e:
    print(f"  Result: FAIL - {e}")

print()

# Test failing coverage
try:
    threshold.enforce(72.3)
    print("  Result: PASS")
except ValueError as e:
    print(f"  Result: FAIL - {e}")

print()

# Example 5: Coverage Configuration
print("Example 5: Coverage Configuration")
print("=" * 60)

@dataclass
class CoverageConfig:
    """Coverage configuration settings."""
    source_dir: str = "src"
    omit_patterns: List[str] = field(default_factory=lambda: ["*/tests/*", "*/migrations/*"])
    fail_under: float = 80.0
    show_missing: bool = True
    skip_covered: bool = False
    report_formats: List[str] = field(default_factory=lambda: ["term", "html"])

    def to_pytest_args(self) -> List[str]:
        """Convert config to pytest arguments."""
        args = [
            f"--cov={self.source_dir}",
            f"--cov-fail-under={self.fail_under}"
        ]

        for pattern in self.omit_patterns:
            args.append(f"--cov-omit={pattern}")

        if self.show_missing:
            args.append("--cov-report=term-missing")

        if "html" in self.report_formats:
            args.append("--cov-report=html")

        if "xml" in self.report_formats:
            args.append("--cov-report=xml")

        return args

# Create coverage configuration
config = CoverageConfig(
    source_dir="myapp",
    fail_under=85.0,
    omit_patterns=["*/tests/*", "*/migrations/*", "*/__init__.py"],
    report_formats=["term", "html", "xml"]
)

print("Coverage Configuration:")
print(f"  Source directory: {config.source_dir}")
print(f"  Minimum coverage: {config.fail_under}%")
print(f"  Omit patterns: {', '.join(config.omit_patterns)}")
print(f"  Report formats: {', '.join(config.report_formats)}")
print()
print("Pytest arguments:")
for arg in config.to_pytest_args():
    print(f"  {arg}")
print()

# Example 6: Differential Coverage
print("Example 6: Differential Coverage (Changed Lines)")
print("=" * 60)

class DiffCoverageTracker:
    """Tracks coverage for changed lines only."""

    def __init__(self):
        self.changed_lines: Set[int] = set()
        self.covered_changed_lines: Set[int] = set()

    def add_changed_line(self, line_num: int):
        """Mark a line as changed."""
        self.changed_lines.add(line_num)

    def mark_covered(self, line_num: int):
        """Mark a changed line as covered."""
        if line_num in self.changed_lines:
            self.covered_changed_lines.add(line_num)

    def get_diff_coverage(self) -> float:
        """Calculate coverage for changed lines only."""
        if not self.changed_lines:
            return 100.0
        return (len(self.covered_changed_lines) / len(self.changed_lines)) * 100

    def get_uncovered_changes(self) -> Set[int]:
        """Get changed lines that are not covered."""
        return self.changed_lines - self.covered_changed_lines

# Simulate git diff
diff_tracker = DiffCoverageTracker()

# Lines changed in this PR
changed_lines = [15, 16, 17, 25, 26, 38, 39, 40]
for line in changed_lines:
    diff_tracker.add_changed_line(line)

# Lines covered by tests
covered_lines = [15, 16, 17, 25, 38, 39]
for line in covered_lines:
    diff_tracker.mark_covered(line)

diff_coverage = diff_tracker.get_diff_coverage()
uncovered = diff_tracker.get_uncovered_changes()

print(f"Changed lines: {len(diff_tracker.changed_lines)}")
print(f"Covered changed lines: {len(diff_tracker.covered_changed_lines)}")
print(f"Diff coverage: {diff_coverage:.1f}%")
print(f"Uncovered changes: {sorted(uncovered)}")
print()

print("=" * 60)
print("COVERAGE REPORTING BEST PRACTICES")
print("=" * 60)
print("""
RUNNING COVERAGE:

Basic coverage:
  pytest --cov=myapp tests/

With report:
  pytest --cov=myapp --cov-report=html tests/

Show missing lines:
  pytest --cov=myapp --cov-report=term-missing tests/

CONFIGURATION (.coveragerc or pyproject.toml):

[tool:pytest]
addopts = --cov=myapp --cov-report=html --cov-fail-under=80

[coverage:run]
source = myapp
omit =
    */tests/*
    */migrations/*
    */__init__.py

[coverage:report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:

COVERAGE METRICS:

Statement coverage:
  - Lines of code executed
  - Most common metric
  - Easy to understand

Branch coverage:
  - All decision branches covered
  - More thorough than statement coverage
  - Catches untested edge cases

Function coverage:
  - All functions called
  - Ensures no dead code

REPORT FORMATS:

Terminal (term):
  - Quick overview
  - Shows during test run
  - Good for CI/CD

HTML:
  - Detailed view
  - Line-by-line analysis
  - Browse locally

XML:
  - Machine-readable
  - CI/CD integration
  - Tool compatibility

JSON:
  - Programmatic access
  - Custom processing
  - API integration

THRESHOLDS:

Fail under threshold:
  --cov-fail-under=80

Per-file thresholds:
  [coverage:report]
  fail_under = 80

Differential coverage:
  - Cover only changed lines
  - PR coverage checks
  - Incremental improvement

Production note: Real pytest-cov provides:
  - Integration with coverage.py
  - Multiple report formats
  - Threshold enforcement
  - Parallel test support
  - Source code annotation
  - Branch coverage analysis
  - Coverage combination
  - Plugin ecosystem
""")
'''

    # Save changes
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 70)
    print("BATCH 18 PART 1 COMPLETE: pytest Async Testing and Coverage Reports")
    print("=" * 70)
    print("\nUpgraded lessons:")
    print(f"  - Lesson 808: pytest - Async Testing")
    print(f"  - Lesson 809: pytest - Coverage Reports")
    print("\nAll lessons upgraded to 13,000-17,000+ characters")
    print("Zero package installation required!")
    print("=" * 70)

if __name__ == "__main__":
    upgrade_lessons()
