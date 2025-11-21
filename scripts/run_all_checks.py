#!/usr/bin/env python3
"""
Master script to run all quality checks in sequence.
"""
import subprocess
import sys
from pathlib import Path
import time

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text:^80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")

def run_script(script_name, description):
    """Run a Python script and return success status"""
    print_header(description)
    print(f"{Colors.BOLD}Running: {script_name}{Colors.RESET}\n")

    script_path = Path(__file__).parent / script_name
    if not script_path.exists():
        print(f"{Colors.RED}Script not found: {script_path}{Colors.RESET}\n")
        return False

    start_time = time.time()

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=False,
            text=True
        )

        elapsed = time.time() - start_time
        print(f"\n{Colors.CYAN}Completed in {elapsed:.1f} seconds{Colors.RESET}")

        if result.returncode == 0:
            print(f"{Colors.GREEN}✓ Check passed{Colors.RESET}\n")
            return True
        else:
            print(f"{Colors.YELLOW}⚠ Check completed with warnings{Colors.RESET}\n")
            return False

    except Exception as e:
        elapsed = time.time() - start_time
        print(f"\n{Colors.RED}✗ Error running script: {e}{Colors.RESET}")
        print(f"{Colors.CYAN}Time elapsed: {elapsed:.1f} seconds{Colors.RESET}\n")
        return False

def run_node_script(script_name, description):
    """Run a Node.js script and return success status"""
    print_header(description)
    print(f"{Colors.BOLD}Running: {script_name}{Colors.RESET}\n")

    script_path = Path(__file__).parent / script_name
    if not script_path.exists():
        print(f"{Colors.RED}Script not found: {script_path}{Colors.RESET}\n")
        return False

    start_time = time.time()

    try:
        result = subprocess.run(
            ['node', str(script_path)],
            capture_output=False,
            text=True
        )

        elapsed = time.time() - start_time
        print(f"\n{Colors.CYAN}Completed in {elapsed:.1f} seconds{Colors.RESET}")

        if result.returncode == 0:
            print(f"{Colors.GREEN}✓ Check passed{Colors.RESET}\n")
            return True
        else:
            print(f"{Colors.YELLOW}⚠ Check completed with warnings{Colors.RESET}\n")
            return False

    except Exception as e:
        elapsed = time.time() - start_time
        print(f"\n{Colors.RED}✗ Error running script: {e}{Colors.RESET}")
        print(f"{Colors.CYAN}Time elapsed: {elapsed:.1f} seconds{Colors.RESET}\n")
        return False

def main():
    print_header("COMPREHENSIVE LESSON QUALITY CHECK SUITE")
    print(f"{Colors.BOLD}This will run all quality checks on your lesson files.{Colors.RESET}")
    print(f"{Colors.BOLD}This may take several minutes...{Colors.RESET}\n")

    start_time = time.time()

    checks = [
        # Basic validation (structure, fields, IDs)
        ('node', 'validate-lessons.mjs', '1. Basic Structure Validation (Node.js)'),

        # Solution execution validation
        ('python', 'validate_all_lessons.py', '2. Solution Execution Validation'),

        # Quality checks
        ('python', 'check_lesson_quality.py', '3. Lesson Quality Analysis'),

        # Tutorial quality
        ('python', 'check_tutorial_quality.py', '4. Tutorial Quality Analysis'),

        # Duplicate detection
        ('python', 'find_duplicate_solutions.py', '5. Duplicate Solution Detection'),

        # Final scan
        ('python', 'final_quality_scan.py', '6. Final Quality Scan'),
    ]

    results = []

    for i, (script_type, script_name, description) in enumerate(checks, 1):
        if script_type == 'python':
            success = run_script(script_name, description)
        else:
            success = run_node_script(script_name, description)

        results.append((description, success))

        # Brief pause between checks
        time.sleep(0.5)

    # Final summary
    total_time = time.time() - start_time

    print_header("FINAL SUMMARY")

    print(f"{Colors.BOLD}Check Results:{Colors.RESET}\n")
    passed = 0
    failed = 0

    for description, success in results:
        if success:
            print(f"  {Colors.GREEN}✓{Colors.RESET} {description}")
            passed += 1
        else:
            print(f"  {Colors.RED}✗{Colors.RESET} {description}")
            failed += 1

    print(f"\n{Colors.BOLD}Statistics:{Colors.RESET}")
    print(f"  Checks passed: {Colors.GREEN}{passed}{Colors.RESET} / {len(checks)}")
    print(f"  Checks failed: {Colors.RED}{failed}{Colors.RESET} / {len(checks)}")
    print(f"  Total time: {Colors.CYAN}{total_time:.1f} seconds{Colors.RESET}")

    # List generated reports
    report_dir = Path(__file__).parent.parent
    reports = [
        'validation_report.json',
        'quality_report.json',
        'tutorial_quality_report.json'
    ]

    print(f"\n{Colors.BOLD}Generated Reports:{Colors.RESET}")
    for report in reports:
        report_path = report_dir / report
        if report_path.exists():
            size = report_path.stat().st_size
            print(f"  {Colors.CYAN}• {report}{Colors.RESET} ({size:,} bytes)")

    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")

    if failed > 0:
        print(f"{Colors.YELLOW}Some checks failed. Review the output above for details.{Colors.RESET}\n")
        sys.exit(1)
    else:
        print(f"{Colors.GREEN}{Colors.BOLD}🎉 All checks passed!{Colors.RESET}\n")
        sys.exit(0)

if __name__ == '__main__':
    main()
