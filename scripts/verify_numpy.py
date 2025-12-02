import json

lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-python.json', encoding='utf-8'))
numpy_ids = [523, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 979]
numpy_lessons = [l for l in lessons if l.get('id') in numpy_ids]

print('NUMPY VERIFICATION:\n')
total_chars = 0
simulations = 0

for l in sorted(numpy_lessons, key=lambda x: x['id']):
    sol = l.get('fullSolution', '')
    has_prod = '# In production:' in sol
    length = len(sol)
    is_sim = has_prod and length > 2000
    total_chars += length
    simulations += is_sim
    status = "SIMULATION" if is_sim else "STUB"
    print(f'ID {l["id"]}: {l["title"][:45]:45s} - {length:5d} chars - {status:10s}')

print(f'\nTOTAL: {simulations}/17 simulations, {total_chars:,} total chars, avg {total_chars//17:,} chars')
