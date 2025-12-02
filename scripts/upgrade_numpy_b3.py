"""NumPy simulations batch 3 - Lessons 804, 805, 806, 807, 979"""
import json
import sys

NUMPY_BATCH = {
    804: r'''# In production: import numpy as np
# This simulation demonstrates NumPy masked arrays without installation

class MaskedArray:
    """Simulates numpy.ma masked array functionality"""
    def __init__(self, data, mask=None):
        self.data = data
        if mask is None:
            self.mask = [False] * len(data)
        else:
            self.mask = mask
        self.fill_value = 999999

    def sum(self, skip_masked=True):
        """Sum, optionally skipping masked values"""
        if skip_masked:
            return sum(self.data[i] for i in range(len(self.data)) if not self.mask[i])
        return sum(self.data)

    def mean(self, skip_masked=True):
        """Mean, optionally skipping masked values"""
        if skip_masked:
            valid = [self.data[i] for i in range(len(self.data)) if not self.mask[i]]
            return sum(valid) / len(valid) if valid else 0
        return sum(self.data) / len(self.data)

    def masked_where(self, condition):
        """Create new mask based on condition"""
        new_mask = [condition(self.data[i]) for i in range(len(self.data))]
        return MaskedArray(self.data, new_mask)

    def __repr__(self):
        result = []
        for i, val in enumerate(self.data):
            if self.mask[i]:
                result.append("--")
            else:
                result.append(str(val))
        return f"[{', '.join(result)}]"

    def compressed(self):
        """Return only non-masked values"""
        return [self.data[i] for i in range(len(self.data)) if not self.mask[i]]

# Demo: Masked operations, invalid data handling
print("NumPy Masked Arrays Simulation")
print("=" * 60)

# Basic masked array
print("1. Creating Masked Arrays:")
data = [10, 20, 30, 40, 50]
mask = [False, True, False, True, False]
arr = MaskedArray(data, mask)

print(f"Data: {data}")
print(f"Mask: {mask} (True = masked/hidden)")
print(f"Masked array: {arr}")
print(f"Display: 10, --, 30, --, 50")

# Masked where
print("\n2. Creating Mask with Condition:")
data = [10, 20, 30, 40, 50, 60, 70, 80]
arr = MaskedArray(data)
print(f"Data: {data}")
print("Mask values > 50:")
arr_masked = arr.masked_where(lambda x: x > 50)
print(f"Result: {arr_masked}")

# Statistics with masking
print("\n3. Statistics with Masked Data:")
data = [10, 20, 30, 40, 50, 60, 70, 80]
mask = [False, False, True, False, True, False, False, True]
arr = MaskedArray(data, mask)

print(f"Data: {data}")
print(f"Mask: {mask}")
print(f"Masked values: {[data[i] for i, m in enumerate(mask) if m]}")

sum_all = sum(data)
sum_valid = arr.sum(skip_masked=True)
print(f"\nSum of all: {sum_all}")
print(f"Sum of valid (unmasked): {sum_valid}")

mean_all = sum_all / len(data)
mean_valid = arr.mean(skip_masked=True)
print(f"Mean of all: {mean_all:.2f}")
print(f"Mean of valid: {mean_valid:.2f}")

# Invalid data reasons
print("\n4. Common Reasons to Mask Data:")
reasons = [
    "Missing values (NaN, None)",
    "Invalid measurements",
    "Out-of-range readings",
    "Data from failed sensors",
    "Measurement uncertainties",
    "Bad pixels in images",
    "Outliers to exclude",
]
for i, reason in enumerate(reasons, 1):
    print(f"  {i}. {reason}")

# Quality control example
print("\n5. Quality Control Example:")
print("Temperature sensor readings:")
temps = [20.5, 21.2, 30.5, 20.8, 21.1, -273.5, 20.9, 19.8]
print(f"Raw data: {temps}")

# Mask unrealistic values
mask_invalid = [t < -100 or t > 60 for t in temps]
print(f"Invalid mask: {mask_invalid}")
valid_temps = [temps[i] for i in range(len(temps)) if not mask_invalid[i]]
print(f"Valid temperatures: {valid_temps}")
print(f"Average: {sum(valid_temps) / len(valid_temps):.2f}°C")

# Combining masks
print("\n6. Combining Multiple Masks:")
data = [10, 20, 30, 40, 50, 60, 70, 80]
print(f"Data: {data}")
mask1 = [x < 30 for x in data]  # Mask low values
mask2 = [x > 60 for x in data]  # Mask high values
combined = [m1 or m2 for m1, m2 in zip(mask1, mask2)]
print(f"Mask low (<30): {mask1}")
print(f"Mask high (>60): {mask2}")
print(f"Combined OR: {combined}")
print(f"Valid range: {[data[i] for i in range(len(data)) if not combined[i]]}")

# File I/O
print("\n7. Masked Array I/O:")
print("Save masked arrays:")
print("  np.ma.savez('masked_data.npz', arr=masked_arr)")
print("\nLoad masked arrays:")
print("  loaded = np.load('masked_data.npz', allow_pickle=True)")

# Operations preserve mask
print("\n8. Operations Preserve Mask:")
print("If operation includes masked value, result is masked:")
print("  a = [1, 2, 3, 4] with mask [F, T, F, F]")
print("  b = [5, 6, 7, 8] with mask [F, F, T, F]")
print("  a + b = [6, --, --, 12] with mask [F, T, T, F]")

print("\nReal NumPy API:")
print("import numpy.ma as ma")
print("arr = ma.array(data, mask=mask)")
print("arr = ma.masked_where(condition, data)")
print("arr = ma.masked_invalid(data)  # mask NaN/inf")
print("arr.filled(fill_value)")
print("arr.compressed()  # return unmasked values")
print("arr.sum(), arr.mean()  # auto skip masked")
''',

    805: r'''# In production: import numpy as np
# This simulation demonstrates NumPy file I/O without installation

import os

class NumpyFileIO:
    """Simulates numpy file operations"""
    def __init__(self):
        self.supported_formats = ['.npy', '.npz', '.txt', '.csv']

    def save_npy(self, filename, data):
        """Simulate saving to .npy format"""
        return f"Saved to {filename} (binary format)"

    def load_npy(self, filename):
        """Simulate loading from .npy format"""
        return f"Loaded from {filename}"

    def save_npz(self, filename, **arrays):
        """Simulate saving compressed archive"""
        names = list(arrays.keys())
        return f"Saved to {filename} with arrays: {names}"

    def load_npz(self, filename):
        """Simulate loading npz archive"""
        return f"Loaded {filename} as NpzFile object"

    def save_txt(self, filename, data):
        """Simulate saving as text format"""
        return f"Saved to {filename} (text format)"

    def load_txt(self, filename):
        """Simulate loading from text file"""
        return f"Loaded from {filename} (auto-detect format)"

# Demo: Save/load arrays, multiple formats
print("NumPy File I/O Simulation")
print("=" * 60)

# Format comparison
print("1. Available Formats:")
formats = [
    ('.npy', 'Single array, binary, fast, compact'),
    ('.npz', 'Multiple arrays, compressed, binary'),
    ('.txt', 'Human-readable, text, larger'),
    ('.csv', 'Comma-separated, spreadsheet compatible'),
    ('.h5', 'HDF5 format, hierarchical, large-scale'),
]
for ext, desc in formats:
    print(f"  {ext:6} - {desc}")

# Saving single array
print("\n2. Save Single Array (.npy):")
print("Code:")
print("  arr = np.array([1, 2, 3, 4, 5])")
print("  np.save('array.npy', arr)")
print("\nResult:")
print("  - Binary file, optimized format")
print("  - Small file size")
print("  - Fast load")
print("  - Single array only")

# Loading single array
print("\n3. Load Single Array (.npy):")
print("Code:")
print("  arr = np.load('array.npy')")
print("\nResult:")
print("  - Returns ndarray directly")
print("  - Preserves dtype and shape")
print("  - Fast loading")

# Saving multiple arrays
print("\n4. Save Multiple Arrays (.npz):")
print("Code:")
print("  np.savez('data.npz', arr1=arr1, arr2=arr2, arr3=arr3)")
print("\nResult:")
print("  - Single compressed archive")
print("  - Multiple named arrays")
print("  - Smaller than multiple .npy files")

# Loading multiple arrays
print("\n5. Load Multiple Arrays (.npz):")
print("Code:")
print("  data = np.load('data.npz')")
print("  arr1 = data['arr1']")
print("  arr2 = data['arr2']")
print("\nResult:")
print("  - Returns NpzFile object (dict-like)")
print("  - Access by array name")
print("  - Lazy loading support")

# Text format
print("\n6. Save as Text Format (.txt, .csv):")
print("Code:")
print("  arr = np.array([[1, 2, 3], [4, 5, 6]])")
print("  np.savetxt('array.txt', arr, delimiter=',')")
print("\nResult:")
print("  - Human-readable format")
print("  - Larger file size")
print("  - Spreadsheet compatible")
print("  - Data loss for complex types")

# Load text
print("\n7. Load Text Format:")
print("Code:")
print("  arr = np.loadtxt('array.txt', delimiter=',')")
print("  arr = np.genfromtxt('data.csv')")
print("\nFeatures:")
print("  - Auto-detect delimiter")
print("  - Skip header rows")
print("  - Use specific dtype")
print("  - Handle missing values")

# Structured arrays save/load
print("\n8. Save/Load Structured Arrays:")
print("Code:")
print("  arr = np.array([(1, 'Alice'), (2, 'Bob')], dtype=[('id', 'i4'), ('name', 'U10')])")
print("  np.save('records.npy', arr)")
print("  loaded = np.load('records.npy')")
print("\nBenefit:")
print("  - Preserves dtype information")
print("  - Preserves field names")
print("  - Efficient storage")

# Memory mapping
print("\n9. Large File Handling (Memory Mapping):")
print("Code:")
print("  arr = np.memmap('large_file.npy', dtype='float32', mode='r')")
print("\nBenefit:")
print("  - Access data without loading to RAM")
print("  - Work with files larger than memory")
print("  - Faster access for random portions")

# Organization best practices
print("\n10. File Organization Best Practices:")
practices = [
    "Use .npz for related arrays",
    "Use .npy for single large arrays",
    "Use .txt for human inspection",
    "Include metadata (shape, dtype) in filename",
    "Version data files (v1, v2, etc)",
    "Store metadata separately (JSON/YAML)",
    "Use hdf5 for very large/hierarchical data",
]
for i, practice in enumerate(practices, 1):
    print(f"  {i}. {practice}")

print("\nReal NumPy API:")
print("import numpy as np")
print("np.save(file, arr)")
print("np.load(file)")
print("np.savez(file, arr1, arr2)  # or name=arr")
print("np.savez_compressed(file, ...)")
print("np.savetxt(fname, X, delimiter=',')")
print("np.loadtxt(fname, delimiter=',')")
print("np.genfromtxt(fname, ...)")
print("arr = np.memmap(filename, dtype=dtype, mode='r')")
''',

    806: r'''# In production: import numpy as np
# This simulation demonstrates NumPy broadcasting rules in detail without installation

class BroadcastRules:
    """Simulates numpy broadcasting rules"""
    def __init__(self):
        self.rules = [
            "If arrays have different dimensions, pad shorter shape with 1s on left",
            "Arrays are compatible if dimensions match or one is 1",
            "After broadcasting, arrays have shape of largest input",
        ]

    def check_compatible(self, shape1, shape2):
        """Check if shapes are broadcasting compatible"""
        # Pad to same length
        if len(shape1) < len(shape2):
            shape1 = (1,) * (len(shape2) - len(shape1)) + shape1
        elif len(shape2) < len(shape1):
            shape2 = (1,) * (len(shape1) - len(shape2)) + shape2

        # Check each dimension
        for s1, s2 in zip(shape1, shape2):
            if s1 != s2 and s1 != 1 and s2 != 1:
                return False, shape1, shape2
        return True, shape1, shape2

    def compute_broadcast_shape(self, shape1, shape2):
        """Compute result shape after broadcasting"""
        # Pad
        if len(shape1) < len(shape2):
            shape1 = (1,) * (len(shape2) - len(shape1)) + shape1
        elif len(shape2) < len(shape1):
            shape2 = (1,) * (len(shape1) - len(shape2)) + shape2

        result = tuple(max(s1, s2) for s1, s2 in zip(shape1, shape2))
        return result

# Demo: Broadcasting rules, shape alignment, detailed examples
print("NumPy Broadcasting Rules (Detailed)")
print("=" * 60)

rules = BroadcastRules()

# Rule 1: Dimension alignment
print("1. Dimension Alignment (Rule 1):")
print("If arrays have different numbers of dimensions,")
print("pad the smaller shape with 1s on the LEFT:")
examples = [
    ((5,), (3, 5), "(5,) -> (1, 5) vs (3, 5)"),
    ((4,), (3, 4, 5), "(4,) -> (1, 1, 4) vs (3, 4, 5)"),
    ((2, 3), (4, 2, 3), "(2, 3) -> (1, 2, 3) vs (4, 2, 3)"),
]
for shape1, shape2, explanation in examples:
    print(f"  {explanation}")

# Rule 2: Dimension compatibility
print("\n2. Dimension Compatibility (Rule 2):")
print("After padding, each dimension must be compatible:")
print("  - Dimensions are equal, OR")
print("  - One dimension is 1, OR")
print("  - (Not compatible otherwise)")

print("\nExamples:")
test_pairs = [
    ((3,), (3,), True),
    ((1,), (5,), True),
    ((3,), (1,), True),
    ((2,), (3,), False),
]
for s1, s2, compatible in test_pairs:
    status = "YES" if compatible else "NO"
    print(f"  {str(s1):10} with {str(s2):10} -> {status}")

# Rule 3: Output shape
print("\n3. Output Shape (Rule 3):")
print("Result shape = maximum of aligned dimensions:")
print("  For each dimension, take max(dim1, dim2)")

shape_tests = [
    ((5,), (1,), (5,)),
    ((1, 4), (3, 1), (3, 4)),
    ((2, 3), (2, 3), (2, 3)),
    ((1, 1, 1), (4, 5, 6), (4, 5, 6)),
]
print("\nExamples:")
for s1, s2, expected in shape_tests:
    result = rules.compute_broadcast_shape(s1, s2)
    print(f"  {str(s1):12} + {str(s2):12} -> {result}")

# Real-world examples
print("\n4. Real-World Broadcasting Examples:")

print("\nExample 1: Scalar + Array")
print("  Scalar shape: ()")
print("  Array shape: (3, 4)")
print("  After padding: () -> (1, 1) vs (3, 4)")
print("  Result shape: (3, 4)")
print("  Effect: Scalar broadcast to all elements")

print("\nExample 2: Vector + Matrix")
print("  Vector shape: (4,)")
print("  Matrix shape: (3, 4)")
print("  After padding: (1, 4) vs (3, 4)")
print("  Result shape: (3, 4)")
print("  Effect: Vector broadcast along rows")

print("\nExample 3: Row Vector + Column Vector")
print("  Row vector shape: (1, 4)")
print("  Col vector shape: (3, 1)")
print("  Result shape: (3, 4)")
print("  Effect: Outer product via broadcasting")

print("\nExample 4: Image + Mask")
print("  Image shape: (100, 200, 3) [RGB image]")
print("  Mask shape: (100, 200) [2D mask]")
print("  After padding: (100, 200, 3) vs (1, 100, 200)")
print("  NOT compatible! Shape mismatch at dimension 2")

print("\n5. Broadcasting in Operations:")
print("Any NumPy operation broadcasts automatically:")
ops = [
    "Arithmetic: a + b, a * b, a / b",
    "Comparison: a > b, a == b",
    "Ufuncs: np.sin(a), np.sqrt(a) + scalar",
    "Linear algebra: np.dot supports broadcasting",
]
for op in ops:
    print(f"  - {op}")

# Common errors
print("\n6. Common Broadcasting Errors:")
print("Error: shapes (3, 4) and (2, 4) cannot broadcast")
print("  Reason: 3 != 2 and neither is 1")
print("\nError: shapes (5,) and (3, 4) cannot broadcast")
print("  After padding: (1, 5) vs (3, 4)")
print("  5 != 4 and neither is 1 - incompatible!")

# Explicit broadcasting
print("\n7. Explicit Broadcasting (when automatic fails):")
print("Use np.broadcast_to() or np.broadcast_arrays():")
print("  a = np.array([1, 2, 3])  # shape (3,)")
print("  b = np.broadcast_to(a, (4, 3))  # shape (4, 3)")

# Memory layout
print("\n8. Broadcasting & Memory:")
print("Broadcasting doesn't copy data (usually):")
print("  - Creates views or uses in-place operations")
print("  - Memory efficient")
print("  - Modifying broadcast result affects original!")

print("\nReal NumPy API:")
print("import numpy as np")
print("# Automatic broadcasting:")
print("result = a + b  # Broadcasts if compatible")
print("\n# Explicit broadcasting:")
print("np.broadcast_to(arr, shape)")
print("np.broadcast_arrays(a, b, c)")
print("\n# Check compatibility:")
print("np.broadcast_shapes(shape1, shape2)")
''',

    807: r'''# In production: import numpy as np
# This simulation demonstrates NumPy advanced sorting without installation

class NumpySorting:
    """Simulates numpy sorting operations"""
    def __init__(self, data):
        self.data = data if isinstance(data, list) else list(data)

    def argsort(self, descending=False):
        """Return indices that would sort the array"""
        indices = list(range(len(self.data)))
        indices.sort(key=lambda i: self.data[i], reverse=descending)
        return indices

    def lexsort(self, keys):
        """Sort by multiple keys (last key is primary)"""
        combined = list(zip(*keys, range(len(keys[0]))))
        combined.sort()
        return [item[-1] for item in combined]

    def argsort_2d(self, axis=None):
        """Sort 2D array along axis"""
        if axis == 0:
            return "Sort each column independently"
        elif axis == 1:
            return "Sort each row independently"
        return "Flatten and sort"

    def partition(self, k):
        """Partition array around k-th element"""
        sorted_data = sorted(self.data)
        return sorted_data[:k], sorted_data[k], sorted_data[k+1:]

# Demo: argsort, lexsort, partition, multi-key sorting
print("NumPy Advanced Sorting Simulation")
print("=" * 60)

# argsort
print("1. argsort - Get Sort Indices:")
data = [30, 10, 50, 20, 40]
sorter = NumpySorting(data)
indices = sorter.argsort()

print(f"Data: {data}")
print(f"Indices of sort: {indices}")
print(f"Sorted data: {[data[i] for i in indices]}")

print("\nUseful for:")
print("  - Sorting one array by another")
print("  - Keeping track of original positions")
print("  - Reverse sorting: argsort()[::-1]")

# Getting sorted data using argsort
print("\nExample - Sort by corresponding array:")
names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
ages = [25, 30, 28, 26, 29]
sorter_ages = NumpySorting(ages)
age_indices = sorter_ages.argsort()
print(f"Names: {names}")
print(f"Ages: {ages}")
print(f"Sort indices: {age_indices}")
sorted_names = [names[i] for i in age_indices]
sorted_ages = [ages[i] for i in age_indices]
print(f"Sorted by age: {sorted_ages}")
print(f"Names in order: {sorted_names}")

# Descending sort
print("\n2. Descending Sort:")
descending_indices = sorter_ages.argsort(descending=True)
print(f"Descending indices: {descending_indices}")
print(f"Names (oldest first): {[names[i] for i in descending_indices]}")

# Multi-key sort (lexsort)
print("\n3. Lexsort - Multi-Key Sorting:")
print("Sort by multiple columns (keys)")
print("\nData:")
print("  Names: [Alice, Bob, Alice, Charlie]")
print("  Ages: [25, 25, 30, 25]")

names = ['Alice', 'Bob', 'Alice', 'Charlie']
ages = [25, 25, 30, 25]
print(f"  Name key: {names}")
print(f"  Age key: {ages}")

print("\nSort by age (primary), then name (secondary):")
combined = list(zip(ages, names, range(len(names))))
combined.sort()
sorted_indices = [item[2] for item in combined]
print(f"  Indices: {sorted_indices}")
print(f"  Result:")
for i in sorted_indices:
    print(f"    {names[i]}, age {ages[i]}")

# 2D sorting
print("\n4. 2D Array Sorting:")
array_2d = [
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5],
]
print("Array:")
for row in array_2d:
    print(f"  {row}")

print("\nSort axis 1 (each row):")
sorted_rows = [sorted(row) for row in array_2d]
for row in sorted_rows:
    print(f"  {row}")

print("\nSort axis 0 (each column):")
print("  Column 0 sorted:", sorted([row[0] for row in array_2d]))
print("  Column 1 sorted:", sorted([row[1] for row in array_2d]))

# Partition (quick select)
print("\n5. Partition (Quick Select):")
data = [30, 10, 50, 20, 40]
print(f"Data: {data}")
print("Find median without full sort:")
sorted_data = sorted(data)
median_idx = len(data) // 2
print(f"  Sorted: {sorted_data}")
print(f"  Median: {sorted_data[median_idx]}")
print("Faster than argsort for single element")

# Sorting stability
print("\n6. Sorting Stability:")
print("Stable sort: preserves order of equal elements")
print("Example with equal ages:")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 25, 25]
print(f"  Names: {names}")
print(f"  Ages: {ages}")
print("Stable sort by age: order preserved")
print(f"  Result: {names} (same order)")

# searchsorted
print("\n7. searchsorted - Find Insert Position:")
data = [10, 20, 30, 40, 50]
values_to_insert = [15, 25, 35]
print(f"Sorted array: {data}")
print(f"Insert values: {values_to_insert}")
positions = []
for val in values_to_insert:
    for i, item in enumerate(data):
        if val < item:
            positions.append(i)
            break
print(f"Insert positions: {positions}")

# Performance notes
print("\n8. Performance Considerations:")
print("argsort: O(n log n) - general purpose")
print("lexsort: O(k*n log n) - k keys")
print("searchsorted: O(log n) - on sorted array")
print("partition: O(n) average - single element")
print("Use heapq.nsmallest(k, arr) for k smallest")

# Use cases
print("\n9. Common Use Cases:")
uses = [
    "Find outliers: argsort and inspect tails",
    "Rank data: use argsort indices as ranks",
    "Multi-level sort: lexsort by key priority",
    "Find element quickly: searchsorted + binary search",
    "Top-N items: argsort with slicing",
]
for i, use in enumerate(uses, 1):
    print(f"  {i}. {use}")

print("\nReal NumPy API:")
print("import numpy as np")
print("np.argsort(a)")
print("np.lexsort(keys)")
print("np.sort(a)")
print("np.partition(a, kth)")
print("np.searchsorted(a, v)")
print("np.argsort(a)[::-1]  # descending")
print("a[np.argsort(a)]  # sorted array from indices")
''',

    979: r'''# In production: import numpy as np
# This simulation demonstrates NumPy best practices without installation

class NumpyBestPractices:
    """NumPy best practices and advanced patterns"""
    def __init__(self):
        self.practices = []

    def performance_tips(self):
        """Key performance tips"""
        return [
            "Use vectorization - avoid Python loops",
            "Choose appropriate dtype to save memory",
            "Use ufuncs for element-wise operations",
            "Leverage broadcasting to avoid loops",
            "Use views instead of copies when possible",
            "Keep arrays contiguous in memory (C-order)",
        ]

    def memory_tips(self):
        """Memory optimization tips"""
        return [
            "Use float32 for 50% less memory (if precision allows)",
            "Use int16/int32 for integer data",
            "Avoid unnecessary copies - use in-place ops",
            "Use memmap for files larger than RAM",
            "Monitor array size with arr.nbytes",
        ]

    def coding_practices(self):
        """Best coding practices"""
        return [
            "Always specify dtype explicitly",
            "Use meaningful variable names",
            "Document array dimensions in comments",
            "Add error checking for array operations",
            "Use type hints for function arguments",
            "Profile before optimizing",
        ]

# Demo: Performance, memory, best practices
print("NumPy Best Practices and Optimization")
print("=" * 60)

practices = NumpyBestPractices()

# 1. Vectorization
print("1. Vectorization - Core NumPy Strength:")
print("\nAVOID (pure Python loop):")
print("  result = []")
print("  for i in range(1000000):")
print("    result.append(data[i] * 2 + 1)")
print("  Time: ~1000ms")

print("\nFASTER (NumPy vectorization):")
print("  result = data * 2 + 1")
print("  Time: ~1ms")
print("  Speedup: 1000x")

print("\nKey principles:")
for tip in ["Use array operations, not loops",
            "Let NumPy handle the iteration",
            "Compiled C code is much faster"]:
    print(f"  - {tip}")

# 2. Memory optimization
print("\n2. Memory Optimization Strategy:")
print("\nProblem: 100 million float64 elements")
f64_size = 100_000_000 * 8
f32_size = 100_000_000 * 4
i32_size = 100_000_000 * 4
print(f"  float64: {f64_size / 1e9:.1f} GB")
print(f"  float32: {f32_size / 1e9:.1f} GB (50% reduction)")
print(f"  int32:   {i32_size / 1e9:.1f} GB (if integers OK)")

print("\nAction items:")
print("  1. Choose smallest sufficient dtype")
print("  2. Use in-place operations: arr *= 2")
print("  3. Delete unused arrays: del arr1, arr2")
print("  4. Monitor with arr.nbytes")

# 3. Algorithm selection
print("\n3. Algorithm Selection Guide:")
algorithms = [
    ("sum, mean, std", "Use np.sum, np.mean, np.std"),
    ("sorting", "Use np.argsort (returns indices)"),
    ("matrix mult", "Use np.dot or @ operator"),
    ("linear system", "Use np.linalg.solve"),
    ("eigenvalues", "Use np.linalg.eig"),
    ("FFT", "Use np.fft.fft"),
]
for problem, solution in algorithms:
    print(f"  {problem:20} -> {solution}")

# 4. Dtype selection
print("\n4. Data Type Selection Matrix:")
print("  Integer data:")
print("    - bool: 1 byte (True/False only)")
print("    - int8: 1 byte (-128 to 127)")
print("    - int16: 2 bytes (-32k to 32k)")
print("    - int32: 4 bytes (default for integers)")
print("    - int64: 8 bytes (large integers)")
print("\n  Float data:")
print("    - float32: 4 bytes (7 decimal digits)")
print("    - float64: 8 bytes (15 decimal digits)")
print("\n  Complex data:")
print("    - complex64: 8 bytes (2x float32)")
print("    - complex128: 16 bytes (2x float64)")

# 5. Common pitfalls
print("\n5. Common Pitfalls to Avoid:")
pitfalls = [
    "Using [] instead of [[]] for 2D arrays",
    "Forgetting to copy data when needed",
    "Exceeding array bounds without checking",
    "Mixed dtypes causing unexpected behavior",
    "In-place operations modifying inputs",
    "View vs copy confusion",
]
for i, pitfall in enumerate(pitfalls, 1):
    print(f"  {i}. {pitfall}")

# 6. Debugging tips
print("\n6. Debugging Tips:")
tips = [
    "Use arr.shape to verify dimensions",
    "Use arr.dtype to check type",
    "Use arr.ndim to check rank",
    "Print arr.flags for memory layout",
    "Use np.allclose for float comparison",
    "Add assertions for expected shapes",
]
for tip in tips:
    print(f"  - {tip}")

# 7. Code organization
print("\n7. Good Code Organization:")
print("\nimport numpy as np")
print("")
print("# Constants")
print("BATCH_SIZE = 1000")
print("DATA_TYPE = np.float32")
print("")
print("def process_data(arr: np.ndarray) -> np.ndarray:")
print('    """Process array with type checking"""')
print("    assert arr.dtype == DATA_TYPE")
print("    assert arr.ndim == 2")
print("    # ... operations ...")
print("    return result")

# 8. Advanced patterns
print("\n8. Advanced Patterns:")
patterns = [
    "Vectorized if-else: np.where(condition, x, y)",
    "Batch processing: use reshape/reshape tricks",
    "Lazy evaluation: use generators with NumPy",
    "Parallel processing: use np.array_split",
    "Memory mapping: np.memmap for huge files",
]
for i, pattern in enumerate(patterns, 1):
    print(f"  {i}. {pattern}")

# 9. Integration with other libraries
print("\n9. Integration with Ecosystem:")
libraries = [
    "Pandas: convert with .values, .to_numpy()",
    "Matplotlib: direct plotting of arrays",
    "SciPy: advanced algorithms on arrays",
    "Scikit-learn: arrays as inputs/outputs",
    "TensorFlow/PyTorch: NumPy compatibility",
]
for lib in libraries:
    print(f"  - {lib}")

# 10. Testing strategies
print("\n10. Testing NumPy Code:")
print("Use numpy.testing for reliable comparisons:")
print("  np.testing.assert_array_equal(a, b)")
print("  np.testing.assert_allclose(a, b, rtol=1e-5)")
print("  np.testing.assert_raises(ValueError, func)")

print("\nReal NumPy Best Practices:")
print("1. Profile code to find bottlenecks")
print("2. Use appropriate dtypes from start")
print("3. Vectorize all loops possible")
print("4. Leverage broadcasting")
print("5. Use built-in functions over custom")
print("6. Document array shapes and dtypes")
print("7. Handle edge cases (empty, single element)")
print("8. Test numerically with assert_allclose")
''',
}

def update_lessons(lessons_file):
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    updated = []
    for lesson in lessons:
        if lesson.get('id') in NUMPY_BATCH:
            lesson['fullSolution'] = NUMPY_BATCH[lesson['id']]
            updated.append(lesson['id'])

    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    return updated

def main():
    lessons_file = r'c:\devbootLLM-app\public\lessons-python.json'
    updated = update_lessons(lessons_file)
    print(f"Updated {len(updated)} lessons in batch 3: {updated}")

if __name__ == '__main__':
    sys.exit(main())
