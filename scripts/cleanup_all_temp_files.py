#!/usr/bin/env python3
"""
Comprehensive cleanup of ALL temporary files and folders.
Clean up unnecessary README files too.
"""
import os
import shutil
import glob

# Temporary files to delete
TEMP_FILES = [
    'a.csv', 'a.txt', 'b.txt',
    'data.csv', 'data.txt',
    'msg.txt', 'note.txt', 'notes.txt',
    'Main.class',
    'curriculum_progress.json',
    'x.zip',
]

# Temporary directories to delete
TEMP_DIRS = [
    'd',
    'testdir',
    'scripts/__pycache__',
]

# README files to DELETE (keep only essential ones)
UNNEEDED_READMES = [
    'EXPANSION_STRATEGY.md',           # Strategy doc - not needed
    'FINAL_QUALITY_REPORT.md',         # Old report - not needed
    'GETTING_STARTED_NEW_LANGUAGE.md', # Template guide - not needed
    'LESSON_SYSTEM_SUMMARY.md',        # Summary doc - not needed
    'LESSON_TEMPLATE.md',              # Template - not needed
    'QUALITY_SUMMARY.md',              # Old report - not needed
]

# README files to KEEP
KEEP_READMES = [
    'README.md',                       # Main README - ESSENTIAL
    'DUPLICATE_SOLUTIONS_PLAN.md',    # Recent fix documentation
    'RUNTIME_ERROR_FIXES.md',         # Recent fix documentation
]

def cleanup_files():
    """Delete temporary files."""
    deleted_files = []
    for filename in TEMP_FILES:
        filepath = filename
        if os.path.exists(filepath):
            try:
                os.remove(filepath)
                deleted_files.append(filename)
                print(f"  [DELETED] {filename}")
            except Exception as e:
                print(f"  [ERROR] Could not delete {filename}: {e}")
    return deleted_files

def cleanup_directories():
    """Delete temporary directories."""
    deleted_dirs = []
    for dirname in TEMP_DIRS:
        if os.path.exists(dirname):
            try:
                shutil.rmtree(dirname)
                deleted_dirs.append(dirname)
                print(f"  [DELETED] {dirname}/ (directory)")
            except Exception as e:
                print(f"  [ERROR] Could not delete {dirname}/: {e}")
    return deleted_dirs

def cleanup_readmes():
    """Delete unnecessary README files."""
    deleted_readmes = []
    for readme in UNNEEDED_READMES:
        if os.path.exists(readme):
            try:
                os.remove(readme)
                deleted_readmes.append(readme)
                print(f"  [DELETED] {readme}")
            except Exception as e:
                print(f"  [ERROR] Could not delete {readme}: {e}")
    return deleted_readmes

def show_kept_readmes():
    """Show which READMEs are being kept."""
    print(f"\nREADME files KEPT ({len(KEEP_READMES)}):")
    for readme in KEEP_READMES:
        if os.path.exists(readme):
            print(f"  [KEEP] {readme}")

print("\n" + "="*80)
print("COMPREHENSIVE CLEANUP - TEMPORARY FILES & UNNECESSARY DOCS")
print("="*80)

print("\nDeleting temporary files:")
deleted_files = cleanup_files()

print("\nDeleting temporary directories:")
deleted_dirs = cleanup_directories()

print("\nDeleting unnecessary README/documentation files:")
deleted_readmes = cleanup_readmes()

show_kept_readmes()

print("\n" + "="*80)
print("CLEANUP SUMMARY")
print("="*80)
print(f"Temporary files deleted: {len(deleted_files)}")
print(f"Temporary directories deleted: {len(deleted_dirs)}")
print(f"Unnecessary docs deleted: {len(deleted_readmes)}")
print(f"Total items removed: {len(deleted_files) + len(deleted_dirs) + len(deleted_readmes)}")
print("="*80 + "\n")
