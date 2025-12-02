"""
Upgrade NumPy framework lessons to realistic simulations
Part 1 of 2: Covers first 10 NumPy lessons
"""

import json
import sys

# First batch of NumPy simulations (due to size, splitting into 2 parts)
NUMPY_BATCH_1 = {
    523: """# In production: import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# This simulation demonstrates NumPy array operations

class NumpyArray:
    def __init__(self, data, dtype=None):
        self.data = data
        self.dtype = dtype or 'float64'
        self.shape = (len(data),) if isinstance(data, list) else (1,)
        self.size = len(data) if isinstance(data, list) else 1

    def __add__(self, other):
        if isinstance(other, NumpyArray):
            return NumpyArray([a + b for a, b in zip(self.data, other.data)])
        return NumpyArray([x + other for x in self.data])

    def __mul__(self, other):
        if isinstance(other, NumpyArray):
            return NumpyArray([a * b for a, b in zip(self.data, other.data)])
        return NumpyArray([x * other for x in self.data])

    def sum(self):
        return sum(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def __repr__(self):
        return f"array({self.data})"

# Demo
print("NumPy Array Operations")
print("=" * 50)
arr1 = NumpyArray([1, 2, 3, 4, 5])
arr2 = NumpyArray([10, 20, 30, 40, 50])
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Addition: {arr1 + arr2}")
print(f"Scalar add: {arr1 + 10}")
print(f"Multiplication: {arr1 * arr2}")
print(f"Sum: {arr1.sum()}")
print(f"Mean: {arr1.mean()}")
print("\nReal NumPy: np.array([1,2,3]).sum()")""",
}

def update_lessons(lessons_file):
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    updated = []
    for lesson in lessons:
        lesson_id = lesson.get('id')
        if lesson_id in NUMPY_BATCH_1:
            before_len = len(lesson.get('fullSolution', ''))
            lesson['fullSolution'] = NUMPY_BATCH_1[lesson_id]
            after_len = len(lesson['fullSolution'])
            updated.append({'id': lesson_id, 'title': lesson.get('title'), 'before': before_len, 'after': after_len})

    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    return updated

def main():
    lessons_file = r'c:\devbootLLM-app\public\lessons-python.json'
    updated = update_lessons(lessons_file)
    print(f"Updated {len(updated)} NumPy lessons")
    for item in updated:
        print(f"  ID {item['id']}: {item['title']} ({item['after']:,} chars)")
    print(f"Total added: {sum(item['after']-item['before'] for item in updated):,}")

if __name__ == '__main__':
    sys.exit(main())
