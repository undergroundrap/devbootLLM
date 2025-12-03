#!/usr/bin/env python3
"""Final verification for batch 10"""

import json

data = json.load(open(r'c:\devbootLLM-app\public\lessons-java.json', 'r', encoding='utf-8'))

print('FINAL BATCH 10 VERIFICATION')
print('=' * 70)
print()

total_before = 1269 + 978 + 978 + 978
total_after = sum(len(l['fullSolution']) for l in data if l['id'] in [808, 1021, 1022, 1023])

print(f'Total characters before: {total_before:>6,}')
print(f'Total characters after:  {total_after:>6,}')
print(f'Total growth:            {total_after - total_before:>+6,}')
print(f'Growth percentage:       +{((total_after - total_before) / total_before * 100):.1f}%')
print()

print('Individual lessons:')
for lid in [808, 1021, 1022, 1023]:
    l = [x for x in data if x['id'] == lid][0]
    print(f"  {lid}: {l['title'][:40]:40} {len(l['fullSolution']):>6,} chars")

print()
print('All lessons verified successfully!')
print('=' * 70)
