"""
Clean up temporary files and one-time upgrade scripts from the repository
Run after all batches are complete to remove clutter
"""
import os

# Temporary markdown reports (already superseded)
OLD_MD_FILES = [
    "celery_lessons_quick_reference.md",
    "celery_upgrade_report.md",
    "flask_upgrade_final_report.md",
    "FLASK_UPGRADE_SUMMARY.md",
    "FRAMEWORK_QUALITY_ISSUES.md",
    "FRAMEWORK_SIMULATION_UPGRADES.md",
    "kafka_upgrade_report.md",
    "redis_upgrade_report.md",
    "FINAL_QUALITY_REPORT.md",
    "QUALITY_IMPROVEMENTS_COMPLETE.md",
    "QUALITY_STATUS_COMPLETE.md",
    "QUALITY_VERIFICATION_COMPLETE.md",
]

# One-time upgrade scripts (already applied)
OLD_SCRIPTS = [
    "scripts/upgrade_celery_lessons.py",
    "scripts/upgrade_flask_stubs.py",
    "scripts/upgrade_redis_simulations.py",
    "scripts/upgrade_fastapi_lessons.py",
    "scripts/upgrade_pandas_batch.py",
    "scripts/upgrade_pandas_batch2.py",
    "scripts/upgrade_numpy_lessons.py",
    "scripts/upgrade_numpy_b1.py",
    "scripts/upgrade_numpy_b2.py",
    "scripts/upgrade_numpy_b3.py",
    "scripts/upgrade_django_b4a.py",
    "scripts/upgrade_django_b4b.py",
    "scripts/upgrade_sqlalchemy_b4c.py",
    "scripts/upgrade_pytest_b4d.py",
    "scripts/apply_flask_upgrades.py",
    "scripts/generate_kafka_simulations.py",
    "scripts/generate_redis_upgrade_report.py",
    "scripts/flask_simulations.py",
    "scripts/find_framework_stubs_to_upgrade.py",
    "scripts/verify_flask_syntax.py",
    "scripts/verify_redis_syntax.py",
    "scripts/verify_numpy.py",
    "scripts/view_flask_lessons.py",
    "scripts/verify_all_upgraded_lessons.py",
    "scripts/check_placeholder_issues.py",
    "scripts/detect_narrative_functions.py",
    "scripts/detect_truly_bad_lessons.py",
    "scripts/add_expected_output.py",
    "scripts/analyze_good_simulations.py",
    "scripts/check_tutorial_quality_comprehensive.py",
    "scripts/comprehensive_tutorial_improver.py",
    "scripts/find_tutorial_code_examples.py",
    "scripts/verify_tutorial_code_blocks.py",
    "scripts/SQLALCHEMY_B4C_SUMMARY.txt",
]

def cleanup():
    base_dir = r"c:\devbootLLM-app"
    removed = []

    print("=" * 80)
    print("REPOSITORY CLEANUP")
    print("=" * 80)

    # Remove old markdown files
    print("\nRemoving temporary markdown reports...")
    for md_file in OLD_MD_FILES:
        path = os.path.join(base_dir, md_file)
        if os.path.exists(path):
            os.remove(path)
            removed.append(md_file)
            print(f"  ✓ Removed: {md_file}")

    # Remove one-time scripts
    print("\nRemoving one-time upgrade scripts...")
    for script in OLD_SCRIPTS:
        path = os.path.join(base_dir, script)
        if os.path.exists(path):
            os.remove(path)
            removed.append(script)
            print(f"  ✓ Removed: {script}")

    print("\n" + "=" * 80)
    print(f"CLEANUP COMPLETE: Removed {len(removed)} files")
    print("=" * 80)

    print("\nKept important files:")
    print("  📄 README.md, FRAMEWORK_VALIDATION.md, CHANGELOG.md")
    print("  📄 CONTRIBUTING.md, FAQ.md, COMPETITIVE_ANALYSIS.md")
    print("  🔧 comprehensive_quality_check.py")
    print("  🔧 comprehensive_validation.py")
    print("  🔧 job_readiness_analysis.py")
    print("  🔧 final_framework_status.py")
    print("  🔧 verify_framework_lessons.py")
    print("  🔧 verify_batch4.py")

if __name__ == "__main__":
    cleanup()
