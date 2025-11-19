#!/usr/bin/env python3
"""
Curriculum Improvement Progress Tracker

Tracks progress through the implementation roadmap and measures improvement metrics.

Usage:
    python scripts/track_progress.py init        # Initialize tracking
    python scripts/track_progress.py update      # Update current metrics
    python scripts/track_progress.py report      # Generate progress report
    python scripts/track_progress.py milestone   # Check milestone achievements
"""

import json
import sys
from datetime import datetime
from collections import Counter
import os

PROGRESS_FILE = 'curriculum_progress.json'

# Target metrics
TARGETS = {
    'difficulty': {
        'Beginner': (25, 30),
        'Intermediate': (30, 35),
        'Advanced': (25, 30),
        'Expert': (10, 15)
    },
    'professional_skills': {
        'Git/Version Control': 25,
        'Agile/Scrum': 20,
        'Documentation': 15,
        'Code Review/Testing': 20
    },
    'fullstack_projects': {
        'Java': 5,
        'Python': 5
    }
}

def load_lessons(filepath):
    """Load lessons from JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filepath} not found")
        return []

def load_progress():
    """Load progress tracking data."""
    if not os.path.exists(PROGRESS_FILE):
        return None

    with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_progress(data):
    """Save progress tracking data."""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def calculate_metrics():
    """Calculate current curriculum metrics."""
    java = load_lessons('public/lessons-java.json')
    python = load_lessons('public/lessons-python.json')

    metrics = {
        'timestamp': datetime.now().isoformat(),
        'java': analyze_language(java, 'Java'),
        'python': analyze_language(python, 'Python'),
        'overall': {}
    }

    # Overall totals
    metrics['overall']['total_lessons'] = len(java) + len(python)

    # Overall difficulty distribution
    all_difficulties = ([l['difficulty'] for l in java] +
                       [l['difficulty'] for l in python])
    total = len(all_difficulties)
    diff_counts = Counter(all_difficulties)

    metrics['overall']['difficulty'] = {
        d: {
            'count': diff_counts.get(d, 0),
            'percentage': (diff_counts.get(d, 0) / total * 100) if total > 0 else 0
        }
        for d in ['Beginner', 'Intermediate', 'Advanced', 'Expert']
    }

    return metrics

def analyze_language(lessons, lang):
    """Analyze metrics for a single language."""
    total = len(lessons)

    # Difficulty distribution
    difficulty_counts = Counter(l['difficulty'] for l in lessons)

    # All tags
    all_tags = []
    for lesson in lessons:
        all_tags.extend([tag.lower() for tag in lesson['tags']])
    tag_counts = Counter(all_tags)

    # Professional skills count
    prof_skills = {
        'Git/Version Control': sum(tag_counts.get(kw, 0) for kw in ['git', 'github', 'version control']),
        'Agile/Scrum': sum(tag_counts.get(kw, 0) for kw in ['agile', 'scrum', 'sprint']),
        'Documentation': sum(tag_counts.get(kw, 0) for kw in ['documentation', 'javadoc', 'docstring']),
        'Code Review/Testing': sum(tag_counts.get(kw, 0) for kw in ['code review', 'tdd', 'test-driven'])
    }

    # Full-stack projects
    fullstack = len([l for l in lessons if 'full-stack' in [t.lower() for t in l['tags']] or
                     'fullstack' in [t.lower() for t in l['tags']]])

    # Capstone projects
    capstone = len([l for l in lessons if 'capstone' in l['title'].lower()])

    return {
        'total': total,
        'difficulty': {
            d: {
                'count': difficulty_counts.get(d, 0),
                'percentage': (difficulty_counts.get(d, 0) / total * 100) if total > 0 else 0
            }
            for d in ['Beginner', 'Intermediate', 'Advanced', 'Expert']
        },
        'professional_skills': prof_skills,
        'fullstack_projects': fullstack,
        'capstone_projects': capstone
    }

def init_tracking():
    """Initialize progress tracking."""
    print("Initializing curriculum progress tracking...")

    # Get baseline metrics
    baseline = calculate_metrics()

    progress_data = {
        'initialized': datetime.now().isoformat(),
        'baseline': baseline,
        'snapshots': [baseline],
        'milestones': {
            'phase1_complete': False,
            'phase2_complete': False,
            'phase3_complete': False,
            'phase4_complete': False
        }
    }

    save_progress(progress_data)

    print("\n[OK] Progress tracking initialized!")
    print(f"Baseline snapshot created: {baseline['timestamp']}")
    print(f"Progress file: {PROGRESS_FILE}")
    print("\nNext steps:")
    print("  1. Make curriculum improvements")
    print("  2. Run: python scripts/track_progress.py update")
    print("  3. Run: python scripts/track_progress.py report")

def update_tracking():
    """Update progress with current metrics."""
    progress_data = load_progress()

    if not progress_data:
        print("Error: Progress tracking not initialized.")
        print("Run: python scripts/track_progress.py init")
        return

    print("Updating progress metrics...")

    # Get current metrics
    current = calculate_metrics()

    # Add to snapshots
    progress_data['snapshots'].append(current)

    # Check for milestone achievements
    check_milestones(progress_data, current)

    save_progress(progress_data)

    print("\n[OK] Progress updated!")
    print(f"Snapshot created: {current['timestamp']}")
    print(f"Total snapshots: {len(progress_data['snapshots'])}")
    print("\nRun 'python scripts/track_progress.py report' to see detailed progress.")

def check_milestones(progress_data, current):
    """Check if any milestones have been achieved."""
    milestones = progress_data['milestones']

    # Phase 1: Difficulty rebalancing
    java_expert_pct = current['java']['difficulty']['Expert']['percentage']
    python_expert_pct = current['python']['difficulty']['Expert']['percentage']

    if (java_expert_pct <= 15 and python_expert_pct <= 15 and
        not milestones['phase1_complete']):
        milestones['phase1_complete'] = True
        print("\n*** MILESTONE ACHIEVED: Phase 1 Complete - Difficulty Rebalanced! ***")

    # Phase 2: Professional skills
    prof_skills_met = True
    for skill, target in TARGETS['professional_skills'].items():
        java_count = current['java']['professional_skills'].get(skill, 0)
        python_count = current['python']['professional_skills'].get(skill, 0)
        if java_count < target or python_count < target:
            prof_skills_met = False

    if prof_skills_met and not milestones['phase2_complete']:
        milestones['phase2_complete'] = True
        print("\n*** MILESTONE ACHIEVED: Phase 2 Complete - Professional Skills Added! ***")

    # Phase 3: Full-stack projects
    java_fullstack = current['java']['fullstack_projects']
    python_fullstack = current['python']['fullstack_projects']

    if (java_fullstack >= 5 and python_fullstack >= 5 and
        not milestones['phase3_complete']):
        milestones['phase3_complete'] = True
        print("\n*** MILESTONE ACHIEVED: Phase 3 Complete - Full-Stack Projects Done! ***")

def generate_report():
    """Generate detailed progress report."""
    progress_data = load_progress()

    if not progress_data:
        print("Error: Progress tracking not initialized.")
        print("Run: python scripts/track_progress.py init")
        return

    baseline = progress_data['baseline']
    current = progress_data['snapshots'][-1]

    print("\n" + "="*80)
    print("CURRICULUM IMPROVEMENT PROGRESS REPORT")
    print("="*80)

    print(f"\nInitialized: {progress_data['initialized']}")
    print(f"Last Updated: {current['timestamp']}")
    print(f"Snapshots Taken: {len(progress_data['snapshots'])}")

    print("\n" + "="*80)
    print("OVERALL PROGRESS")
    print("="*80)

    # Total lessons
    baseline_total = baseline['overall']['total_lessons']
    current_total = current['overall']['total_lessons']
    lessons_added = current_total - baseline_total

    print(f"\nTotal Lessons:")
    print(f"  Baseline: {baseline_total}")
    print(f"  Current:  {current_total}")
    print(f"  Added:    {lessons_added:+d}")

    # Difficulty distribution
    print("\nDifficulty Distribution (Overall):")
    print("-" * 80)
    for difficulty in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
        baseline_pct = baseline['overall']['difficulty'][difficulty]['percentage']
        current_pct = current['overall']['difficulty'][difficulty]['percentage']
        change = current_pct - baseline_pct
        target_min, target_max = TARGETS['difficulty'][difficulty]

        status = "[OK]" if target_min <= current_pct <= target_max else "[IN PROGRESS]"

        print(f"  {difficulty:15s}: {baseline_pct:5.1f}% → {current_pct:5.1f}% "
              f"({change:+5.1f}%) | Target: {target_min}-{target_max}% {status}")

    # Language-specific progress
    for lang in ['java', 'python']:
        lang_name = lang.capitalize()
        print(f"\n{'='*80}")
        print(f"{lang_name.upper()} PROGRESS")
        print('='*80)

        baseline_lang = baseline[lang]
        current_lang = current[lang]

        lessons_added = current_lang['total'] - baseline_lang['total']
        print(f"\nLessons: {baseline_lang['total']} → {current_lang['total']} ({lessons_added:+d})")

        print("\nDifficulty Distribution:")
        for difficulty in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
            baseline_pct = baseline_lang['difficulty'][difficulty]['percentage']
            current_pct = current_lang['difficulty'][difficulty]['percentage']
            change = current_pct - baseline_pct

            print(f"  {difficulty:15s}: {baseline_pct:5.1f}% → {current_pct:5.1f}% ({change:+5.1f}%)")

        print("\nProfessional Skills:")
        for skill, target in TARGETS['professional_skills'].items():
            baseline_count = baseline_lang['professional_skills'].get(skill, 0)
            current_count = current_lang['professional_skills'].get(skill, 0)
            change = current_count - baseline_count
            status = "[OK]" if current_count >= target else "[NEED MORE]"

            print(f"  {skill:25s}: {baseline_count:3d} → {current_count:3d} ({change:+3d}) | "
                  f"Target: {target} {status}")

        print(f"\nFull-Stack Projects:")
        baseline_fs = baseline_lang['fullstack_projects']
        current_fs = current_lang['fullstack_projects']
        target_fs = TARGETS['fullstack_projects'][lang_name]
        status = "[OK]" if current_fs >= target_fs else "[NEED MORE]"

        print(f"  {baseline_fs} → {current_fs} ({current_fs - baseline_fs:+d}) | "
              f"Target: {target_fs} {status}")

    # Milestones
    print("\n" + "="*80)
    print("MILESTONES")
    print("="*80)
    milestones = progress_data['milestones']

    phases = [
        ('Phase 1: Difficulty Rebalancing', 'phase1_complete'),
        ('Phase 2: Professional Skills', 'phase2_complete'),
        ('Phase 3: Full-Stack Projects', 'phase3_complete'),
        ('Phase 4: Comprehensive Coverage', 'phase4_complete')
    ]

    for phase_name, key in phases:
        status = "[COMPLETE]" if milestones[key] else "[IN PROGRESS]"
        print(f"  {phase_name:35s}: {status}")

    # Next steps
    print("\n" + "="*80)
    print("NEXT STEPS")
    print("="*80)

    recommendations = []

    # Check what needs work
    overall_diff = current['overall']['difficulty']
    if overall_diff['Expert']['percentage'] > 15:
        recommendations.append("Continue reclassifying Expert lessons to Advanced/Intermediate")

    if overall_diff['Beginner']['percentage'] < 25:
        recommendations.append("Create more Beginner lessons (fundamentals, basic syntax)")

    if overall_diff['Intermediate']['percentage'] < 30:
        recommendations.append("Create more Intermediate lessons (common patterns, libraries)")

    for skill, target in TARGETS['professional_skills'].items():
        java_count = current['java']['professional_skills'].get(skill, 0)
        python_count = current['python']['professional_skills'].get(skill, 0)

        if java_count < target:
            recommendations.append(f"Add {skill} lessons to Java curriculum")
        if python_count < target:
            recommendations.append(f"Add {skill} lessons to Python curriculum")

    if current['java']['fullstack_projects'] < 5:
        recommendations.append("Create Java full-stack projects")

    if current['python']['fullstack_projects'] < 5:
        recommendations.append("Create Python full-stack projects")

    if recommendations:
        print("\nRecommended actions:")
        for i, rec in enumerate(recommendations[:5], 1):
            print(f"  {i}. {rec}")
    else:
        print("\n*** All targets achieved! Curriculum is 100% job-ready! ***")

def show_milestone_status():
    """Show current milestone achievements."""
    progress_data = load_progress()

    if not progress_data:
        print("Error: Progress tracking not initialized.")
        print("Run: python scripts/track_progress.py init")
        return

    print("\n" + "="*80)
    print("MILESTONE STATUS")
    print("="*80)

    milestones = progress_data['milestones']
    phases = [
        ('Phase 1: Difficulty Rebalancing', 'phase1_complete', 'Expert lessons <= 15%, proper distribution'),
        ('Phase 2: Professional Skills', 'phase2_complete', 'Git, Agile, Docs, Code Review coverage'),
        ('Phase 3: Full-Stack Projects', 'phase3_complete', '5+ full-stack projects per language'),
        ('Phase 4: Comprehensive Coverage', 'phase4_complete', 'All job-critical skills covered')
    ]

    completed = sum(1 for _, key, _ in phases if milestones[key])
    total = len(phases)

    print(f"\nOverall Progress: {completed}/{total} phases complete ({completed/total*100:.0f}%)")
    print()

    for phase_name, key, description in phases:
        status = "[COMPLETE]" if milestones[key] else "[IN PROGRESS]"
        print(f"{phase_name}")
        print(f"  Status: {status}")
        print(f"  Goal: {description}")
        print()

def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scripts/track_progress.py init        # Initialize tracking")
        print("  python scripts/track_progress.py update      # Update metrics")
        print("  python scripts/track_progress.py report      # Generate report")
        print("  python scripts/track_progress.py milestone   # Show milestones")
        return

    command = sys.argv[1]

    if command == 'init':
        init_tracking()
    elif command == 'update':
        update_tracking()
    elif command == 'report':
        generate_report()
    elif command == 'milestone':
        show_milestone_status()
    else:
        print(f"Unknown command: {command}")
        print("Valid commands: init, update, report, milestone")

if __name__ == '__main__':
    main()
