#!/usr/bin/env python3
"""
Difficulty Distribution Audit Tool

Analyzes the difficulty distribution of lessons and provides recommendations
for reclassification to achieve optimal beginner-to-job-ready balance.

Usage:
    python scripts/audit_difficulty.py
    python scripts/audit_difficulty.py --detailed
    python scripts/audit_difficulty.py --export difficulty_audit.txt
"""

import json
import sys
from collections import Counter, defaultdict

# Target distribution for beginner-to-job-ready curriculum
TARGETS = {
    'Beginner': (25, 30),      # 25-30%
    'Intermediate': (30, 35),   # 30-35%
    'Advanced': (25, 30),       # 25-30%
    'Expert': (10, 15)          # 10-15%
}

def load_lessons(filepath):
    """Load lessons from JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_difficulty(lessons, language):
    """Analyze difficulty distribution and return statistics."""
    total = len(lessons)
    difficulty_counts = Counter(l['difficulty'] for l in lessons)

    stats = {
        'language': language,
        'total': total,
        'counts': difficulty_counts,
        'percentages': {d: (count/total)*100 for d, count in difficulty_counts.items()},
        'gaps': {},
        'recommendations': []
    }

    # Calculate gaps from targets
    for difficulty, (min_pct, max_pct) in TARGETS.items():
        current_pct = stats['percentages'].get(difficulty, 0)
        target_mid = (min_pct + max_pct) / 2

        if current_pct < min_pct:
            gap = min_pct - current_pct
            needed = int((gap / 100) * total)
            stats['gaps'][difficulty] = f"Need {needed} more lessons ({gap:.1f}% below target)"
        elif current_pct > max_pct:
            gap = current_pct - max_pct
            excess = int((gap / 100) * total)
            stats['gaps'][difficulty] = f"Have {excess} excess lessons ({gap:.1f}% above target)"
        else:
            stats['gaps'][difficulty] = "Within target range [OK]"

    return stats

def generate_reclassification_recommendations(lessons, stats):
    """Generate specific recommendations for which lessons to reclassify."""
    recommendations = []

    # Group lessons by difficulty
    by_difficulty = defaultdict(list)
    for lesson in lessons:
        by_difficulty[lesson['difficulty']].append(lesson)

    # If too many Expert lessons, suggest reclassification
    if stats['percentages'].get('Expert', 0) > TARGETS['Expert'][1]:
        expert_lessons = sorted(by_difficulty['Expert'], key=lambda x: x['id'])
        excess_pct = stats['percentages']['Expert'] - TARGETS['Expert'][1]
        num_to_reclassify = int((excess_pct / 100) * stats['total'])

        recommendations.append({
            'action': 'RECLASSIFY EXPERT LESSONS',
            'count': num_to_reclassify,
            'from': 'Expert',
            'to': ['Advanced', 'Intermediate'],
            'suggestions': [
                f"ID {l['id']}: {l['title'][:60]}" for l in expert_lessons[:min(20, num_to_reclassify)]
            ]
        })

    # If need more Beginner lessons
    if stats['percentages'].get('Beginner', 0) < TARGETS['Beginner'][0]:
        gap_pct = TARGETS['Beginner'][0] - stats['percentages'].get('Beginner', 0)
        num_needed = int((gap_pct / 100) * stats['total'])

        recommendations.append({
            'action': 'CREATE NEW BEGINNER LESSONS',
            'count': num_needed,
            'topics': [
                'Basic syntax variations',
                'Simple problem-solving exercises',
                'Fundamental data structures',
                'Common patterns practice',
                'Loop and conditional variations',
                'String manipulation basics'
            ]
        })

    # If need more Intermediate lessons
    if stats['percentages'].get('Intermediate', 0) < TARGETS['Intermediate'][0]:
        gap_pct = TARGETS['Intermediate'][0] - stats['percentages'].get('Intermediate', 0)
        num_needed = int((gap_pct / 100) * stats['total'])

        recommendations.append({
            'action': 'CREATE NEW INTERMEDIATE LESSONS',
            'count': num_needed,
            'topics': [
                'Standard library usage',
                'Design patterns basics',
                'File I/O patterns',
                'Exception handling scenarios',
                'Common algorithms',
                'Real-world problem solutions'
            ]
        })

    return recommendations

def print_report(stats, recommendations, detailed=False):
    """Print formatted audit report."""
    lang = stats['language'].upper()

    print(f"\n{'='*80}")
    print(f"{lang} - DIFFICULTY DISTRIBUTION AUDIT")
    print('='*80)

    print(f"\nTotal Lessons: {stats['total']}")

    print("\nCURRENT DISTRIBUTION:")
    print("-" * 80)
    for difficulty in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
        count = stats['counts'].get(difficulty, 0)
        pct = stats['percentages'].get(difficulty, 0)
        target_min, target_max = TARGETS[difficulty]

        # Status indicator
        if pct < target_min:
            status = "[TOO LOW]"
        elif pct > target_max:
            status = "[TOO HIGH]"
        else:
            status = "[OK]"

        print(f"  {difficulty:15s}: {count:4d} lessons ({pct:5.1f}%) | "
              f"Target: {target_min}-{target_max}% | {status}")

    print("\nGAP ANALYSIS:")
    print("-" * 80)
    for difficulty, gap_msg in stats['gaps'].items():
        print(f"  {difficulty:15s}: {gap_msg}")

    print("\n" + "="*80)
    print("RECOMMENDATIONS")
    print("="*80)

    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. {rec['action']}")
        print(f"   Count: {rec['count']} lessons")

        if 'from' in rec:
            print(f"   From: {rec['from']}")
            print(f"   To: {' or '.join(rec['to'])}")

            if detailed and 'suggestions' in rec:
                print(f"\n   TOP CANDIDATES FOR RECLASSIFICATION:")
                for suggestion in rec['suggestions'][:10]:
                    print(f"     • {suggestion}")

        if 'topics' in rec:
            print(f"\n   SUGGESTED TOPICS:")
            for topic in rec['topics']:
                print(f"     • {topic}")

def export_report(stats, recommendations, filepath):
    """Export report to text file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        lang = stats['language'].upper()

        f.write(f"{lang} - DIFFICULTY DISTRIBUTION AUDIT\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"Total Lessons: {stats['total']}\n\n")

        f.write("CURRENT DISTRIBUTION:\n")
        f.write("-" * 80 + "\n")
        for difficulty in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
            count = stats['counts'].get(difficulty, 0)
            pct = stats['percentages'].get(difficulty, 0)
            target_min, target_max = TARGETS[difficulty]
            f.write(f"{difficulty}: {count} lessons ({pct:.1f}%) | Target: {target_min}-{target_max}%\n")

        f.write("\nGAP ANALYSIS:\n")
        f.write("-" * 80 + "\n")
        for difficulty, gap_msg in stats['gaps'].items():
            f.write(f"{difficulty}: {gap_msg}\n")

        f.write("\n" + "="*80 + "\n")
        f.write("RECOMMENDATIONS\n")
        f.write("="*80 + "\n\n")

        for i, rec in enumerate(recommendations, 1):
            f.write(f"{i}. {rec['action']}\n")
            f.write(f"   Count: {rec['count']} lessons\n")

            if 'from' in rec:
                f.write(f"   From: {rec['from']}\n")
                f.write(f"   To: {' or '.join(rec['to'])}\n")

                if 'suggestions' in rec:
                    f.write(f"\n   TOP CANDIDATES:\n")
                    for suggestion in rec['suggestions']:
                        f.write(f"     - {suggestion}\n")

            if 'topics' in rec:
                f.write(f"\n   SUGGESTED TOPICS:\n")
                for topic in rec['topics']:
                    f.write(f"     - {topic}\n")

            f.write("\n")

def main():
    """Main execution function."""
    detailed = '--detailed' in sys.argv
    export_path = None

    if '--export' in sys.argv:
        idx = sys.argv.index('--export')
        if idx + 1 < len(sys.argv):
            export_path = sys.argv[idx + 1]
        else:
            export_path = 'difficulty_audit_report.txt'

    # Analyze Java
    java_lessons = load_lessons('public/lessons-java.json')
    java_stats = analyze_difficulty(java_lessons, 'Java')
    java_recs = generate_reclassification_recommendations(java_lessons, java_stats)

    print_report(java_stats, java_recs, detailed)

    if export_path:
        export_report(java_stats, java_recs, export_path.replace('.txt', '_java.txt'))

    # Analyze Python
    python_lessons = load_lessons('public/lessons-python.json')
    python_stats = analyze_difficulty(python_lessons, 'Python')
    python_recs = generate_reclassification_recommendations(python_lessons, python_stats)

    print_report(python_stats, python_recs, detailed)

    if export_path:
        export_report(python_stats, python_recs, export_path.replace('.txt', '_python.txt'))

    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"\nJava:   {java_stats['total']} lessons")
    print(f"Python: {python_stats['total']} lessons")
    print(f"Total:  {java_stats['total'] + python_stats['total']} lessons")

    print("\nNEXT STEPS:")
    print("1. Review the recommendations above")
    print("2. Start with reclassifying Expert lessons")
    print("3. Then create new Beginner/Intermediate lessons")
    print("4. Track progress with: python scripts/track_progress.py")
    print("5. Validate after changes: python scripts/validate_lessons.py")

    if export_path:
        print(f"\nReports exported to:")
        print(f"  - {export_path.replace('.txt', '_java.txt')}")
        print(f"  - {export_path.replace('.txt', '_python.txt')}")

if __name__ == '__main__':
    main()
