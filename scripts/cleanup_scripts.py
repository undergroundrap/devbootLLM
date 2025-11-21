#!/usr/bin/env python3
"""
Clean up temporary and one-time use scripts.
Keep only the useful tools.
"""
import os
import glob

# Scripts to KEEP (useful tools that might be needed again)
KEEP_SCRIPTS = [
    'find_duplicate_solutions.py',  # Tool to detect duplicates
    'final_quality_scan.py',        # Quality checking tool
]

# Get all Python scripts in scripts/ directory
all_scripts = glob.glob('scripts/*.py')

# Categorize scripts
to_delete = []
to_keep = []

for script in all_scripts:
    script_name = os.path.basename(script)
    if script_name in KEEP_SCRIPTS or script_name == 'cleanup_scripts.py':
        to_keep.append(script_name)
    else:
        to_delete.append(script)

print("\n" + "="*80)
print("SCRIPT CLEANUP PLAN")
print("="*80)

print(f"\nScripts to KEEP ({len(to_keep)}):")
for script in to_keep:
    print(f"  [KEEP] {script}")

print(f"\nScripts to DELETE ({len(to_delete)}):")
for script in to_delete[:10]:
    print(f"  [DELETE] {os.path.basename(script)}")
if len(to_delete) > 10:
    print(f"  ... and {len(to_delete) - 10} more")

print(f"\n{'='*80}")
print(f"Total: {len(to_keep)} kept, {len(to_delete)} deleted")
print(f"{'='*80}\n")

# Delete the scripts
deleted_count = 0
for script in to_delete:
    try:
        os.remove(script)
        deleted_count += 1
    except Exception as e:
        print(f"Error deleting {script}: {e}")

print(f"Successfully deleted {deleted_count} scripts\n")
