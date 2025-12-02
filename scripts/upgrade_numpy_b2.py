"""NumPy simulations batch 2 - Lessons 798-803"""
import json
import sys

NUMPY_BATCH = {
    798: r'''# In production: import numpy as np
# This simulation demonstrates NumPy random generation without installation

import random

class NumpyRandom:
    """Simulates numpy.random operations"""
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
        self.seed_val = seed

    def uniform(self, low=0.0, high=1.0, size=None):
        """Generate uniform random numbers"""
        if size is None:
            return random.uniform(low, high)
        if isinstance(size, int):
            return [random.uniform(low, high) for _ in range(size)]
        # For tuple sizes, create nested lists
        total = 1
        for s in size:
            total *= s
        return [random.uniform(low, high) for _ in range(total)]

    def normal(self, loc=0.0, scale=1.0, size=None):
        """Generate normally distributed numbers"""
        def gauss():
            u1, u2 = random.random(), random.random()
            z = ((-2 * (u1**2 + u2**2)) ** 0.5) / (u1**2 + u2**2)
            return loc + scale * u1 * z
        if size is None:
            return gauss()
        if isinstance(size, int):
            return [gauss() for _ in range(size)]
        total = 1
        for s in size:
            total *= s
        return [gauss() for _ in range(total)]

    def randint(self, low, high=None, size=None):
        """Generate random integers"""
        if high is None:
            high = low
            low = 0
        if size is None:
            return random.randint(low, high - 1)
        if isinstance(size, int):
            return [random.randint(low, high - 1) for _ in range(size)]
        total = 1
        for s in size:
            total *= s
        return [random.randint(low, high - 1) for _ in range(total)]

    def choice(self, a, size=None):
        """Random choice from array"""
        if size is None:
            return random.choice(a)
        return [random.choice(a) for _ in range(size)]

# Demo: Random distributions, seeding, reproducibility
print("NumPy Random Generation Simulation")
print("=" * 60)

# Seeding for reproducibility
print("1. Seeding for Reproducibility:")
rng1 = NumpyRandom(seed=42)
print("With seed=42:")
vals1 = rng1.uniform(0, 1, 5)
print(f"  First run: {[f'{x:.4f}' for x in vals1]}")

rng2 = NumpyRandom(seed=42)
vals2 = rng2.uniform(0, 1, 5)
print(f"  Second run: {[f'{x:.4f}' for x in vals2]}")
print("Same seed produces same random sequence")

# Uniform distribution
print("\n2. Uniform Distribution:")
rng = NumpyRandom(seed=123)
uniform_vals = rng.uniform(0, 10, 10)
print(f"np.random.uniform(0, 10, 10):")
print(f"  {[f'{x:.2f}' for x in uniform_vals[:5]]}...")

# Normal distribution
print("\n3. Normal Distribution (Gaussian):")
rng = NumpyRandom(seed=123)
normal_vals = rng.normal(loc=100, scale=15, size=10)
print(f"np.random.normal(100, 15, 10) - mean=100, std=15:")
print(f"  {[f'{x:.2f}' for x in normal_vals[:5]]}...")

# Random integers
print("\n4. Random Integers:")
rng = NumpyRandom(seed=123)
int_vals = rng.randint(1, 100, 10)
print(f"np.random.randint(1, 100, 10):")
print(f"  {int_vals[:5]}...")

# Random choice
print("\n5. Random Choice (sampling):")
rng = NumpyRandom(seed=123)
choices = rng.choice(['A', 'B', 'C', 'D'], 8)
print(f"Choices from ['A', 'B', 'C', 'D']:")
print(f"  {choices}")

# Distribution shapes
print("\n6. Different Distribution Shapes:")
print("Uniform: flat probability")
print("Normal: bell curve (most values near mean)")
print("Exponential: skewed right")
print("Poisson: discrete, integer values")

# Common distributions table
print("\n7. Common Distributions:")
distributions = [
    "uniform(low, high) - flat between bounds",
    "normal(loc, scale) - Gaussian with mean and std",
    "binomial(n, p) - success/failure trials",
    "poisson(lam) - counting events",
    "exponential(scale) - waiting times",
    "gamma(shape, scale) - continuous positive",
]
for dist in distributions:
    print(f"  - np.random.{dist}")

print("\nReal NumPy API:")
print("import numpy as np")
print("np.random.seed(42)")
print("np.random.uniform(0, 1, 100)")
print("np.random.normal(0, 1, 100)")
print("np.random.randint(0, 100, 100)")
print("np.random.choice(a, size=100)")
''',

    799: r'''# In production: import numpy as np
# This simulation demonstrates NumPy memory optimization without installation

class NumpyMemory:
    """Simulates numpy memory management and optimization"""
    def __init__(self, data):
        self.data = data
        self._base = None  # Indicates if this is a view
        self.itemsize = 8  # bytes per element
        self.dtype = 'float64'

    def nbytes(self):
        """Calculate memory size"""
        count = 1
        if isinstance(self.data, list):
            for item in self.data:
                if isinstance(item, list):
                    for _ in item:
                        count += 1
                else:
                    count += 1
        return count * self.itemsize

    def view(self):
        """Create a view (shares data, no copy)"""
        new_arr = NumpyMemory(self.data)
        new_arr._base = self  # Mark as view
        return new_arr

    def copy(self):
        """Create a copy (separate data)"""
        import copy as cp
        new_arr = NumpyMemory(cp.deepcopy(self.data))
        return new_arr

    def astype(self, dtype):
        """Convert to different data type"""
        size_map = {'int32': 4, 'int64': 8, 'float32': 4, 'float64': 8}
        new_arr = NumpyMemory(self.data)
        new_arr.dtype = dtype
        new_arr.itemsize = size_map.get(dtype, 8)
        return new_arr

    def is_view(self):
        """Check if array is a view"""
        return self._base is not None

# Demo: Views vs. copies, data types, memory efficiency
print("NumPy Memory Optimization Simulation")
print("=" * 60)

# Views vs. Copies
print("1. Views vs. Copies:")
original = NumpyMemory([1, 2, 3, 4, 5])
print(f"Original array: {original.data}")
print(f"  Memory size: {original.nbytes()} bytes")

view = original.view()
print("\nView (shares data, zero-copy):")
print(f"  Is view: {view.is_view()}")
print(f"  Memory size: {view.nbytes()} bytes")
print("  Modifying view affects original")

copy = original.copy()
print("\nCopy (separate data):")
print(f"  Is view: {copy.is_view()}")
print(f"  Memory size: {copy.nbytes()} bytes")
print("  Modifying copy doesn't affect original")

# Data type impact
print("\n2. Data Type Impact on Memory:")
data = [1, 2, 3, 4, 5, 100, 200, 300]
arr_f64 = NumpyMemory(data)
arr_f32 = arr_f64.astype('float32')
arr_i32 = arr_f64.astype('int32')

print(f"Data: {data}")
print(f"  float64: {arr_f64.nbytes()} bytes ({arr_f64.itemsize} bytes/element)")
print(f"  float32: {arr_f32.nbytes()} bytes ({arr_f32.itemsize} bytes/element)")
print(f"  int32: {arr_i32.nbytes()} bytes ({arr_i32.itemsize} bytes/element)")

# Typical dtype sizes
print("\n3. Data Type Sizes:")
dtypes = [
    ('bool', 1, '1 byte'),
    ('int8', 1, '8-bit integer'),
    ('int16', 2, '16-bit integer'),
    ('int32', 4, '32-bit integer'),
    ('int64', 8, '64-bit integer'),
    ('float32', 4, 'Single precision'),
    ('float64', 8, 'Double precision'),
    ('complex64', 8, '2x float32'),
    ('complex128', 16, '2x float64'),
]
for dtype, size, desc in dtypes:
    print(f"  {dtype:12} - {size:2} bytes - {desc}")

# Memory optimization strategy
print("\n4. Memory Optimization Strategy:")
print("For array with 1 million elements:")
arr_f64_1m = 1_000_000 * 8
arr_f32_1m = 1_000_000 * 4
arr_i32_1m = 1_000_000 * 4
print(f"  float64: {arr_f64_1m / 1e6:.1f} MB")
print(f"  float32: {arr_f32_1m / 1e6:.1f} MB")
print(f"  int32:   {arr_i32_1m / 1e6:.1f} MB")
print("Use float32 when precision not critical - saves 50% memory!")

# Avoiding unnecessary copies
print("\n5. Memory-Efficient Operations:")
print("Inefficient: result = np.zeros(n); result[:] = arr")
print("  Creates temporary, then copies")
print("Efficient: arr *= 2")
print("  In-place operation, no copies")
print("Efficient: arr.reshape() without copy=True")
print("  Returns view, not copy")

# Memory layout
print("\n6. Memory Layout Impact:")
print("C-order (row-major): default in NumPy")
print("  Access rows sequentially: efficient")
print("F-order (column-major): Fortran-style")
print("  Access columns sequentially: efficient for column ops")

print("\nReal NumPy API:")
print("import numpy as np")
print("arr.copy() - explicit copy")
print("arr.view() - view same data")
print("arr.astype(dtype) - change data type")
print("arr.nbytes - total memory bytes")
print("arr.itemsize - bytes per element")
print("arr.flags - memory layout info")
''',

    800: r'''# In production: import numpy as np
# This simulation demonstrates NumPy universal functions (ufuncs) without installation

class NumpyUfuncs:
    """Simulates numpy universal functions"""
    def __init__(self, data):
        self.data = data

    def apply_ufunc(self, func_name):
        """Apply universal function to array"""
        if func_name == 'sqrt':
            return NumpyUfuncs([x ** 0.5 for x in self.data])
        elif func_name == 'exp':
            return NumpyUfuncs([self._exp(x) for x in self.data])
        elif func_name == 'log':
            return NumpyUfuncs([self._log(x) for x in self.data])
        elif func_name == 'sin':
            return NumpyUfuncs([self._sin(x) for x in self.data])
        elif func_name == 'cos':
            return NumpyUfuncs([self._cos(x) for x in self.data])
        elif func_name == 'abs':
            return NumpyUfuncs([abs(x) for x in self.data])
        return self

    @staticmethod
    def _exp(x):
        """Approximate e^x"""
        result = 1
        term = 1
        for i in range(1, 10):
            term *= x / i
            result += term
        return result

    @staticmethod
    def _log(x):
        """Approximate natural log"""
        if x <= 0:
            return float('-inf')
        return 2 * ((x - 1) / (x + 1)) + 2 * ((x - 1) / (x + 1))**3 / 3

    @staticmethod
    def _sin(x):
        """Approximate sine"""
        return x - x**3/6 + x**5/120 - x**7/5040

    @staticmethod
    def _cos(x):
        """Approximate cosine"""
        return 1 - x**2/2 + x**4/24 - x**6/720

    def __repr__(self):
        return f"[{', '.join(f'{x:.4f}' for x in self.data[:5])}...]"

# Demo: Universal functions, vectorization, broadcasting
print("NumPy Universal Functions (ufuncs) Simulation")
print("=" * 60)

# Math ufuncs
print("1. Mathematical Universal Functions:")
arr = NumpyUfuncs([1.0, 4.0, 9.0, 16.0, 25.0])
print(f"Input: {[x for x in arr.data]}")

sqrt_arr = arr.apply_ufunc('sqrt')
print(f"np.sqrt(): {sqrt_arr.data}")

abs_arr = NumpyUfuncs([-1, -4, 3, -2, 5]).apply_ufunc('abs')
print(f"np.abs([-1,-4,3,-2,5]): {abs_arr.data}")

# Trigonometric
print("\n2. Trigonometric Functions:")
angles = NumpyUfuncs([0.0, 0.785, 1.571, 3.14159])  # 0, pi/4, pi/2, pi
print(f"Angles (radians): {[f'{x:.3f}' for x in angles.data]}")
sin_vals = angles.apply_ufunc('sin')
cos_vals = angles.apply_ufunc('cos')
print(f"sin(): {[f'{x:.3f}' for x in sin_vals.data]}")
print(f"cos(): {[f'{x:.3f}' for x in cos_vals.data]}")

# Exponential and log
print("\n3. Exponential and Logarithmic:")
arr = NumpyUfuncs([0.5, 1.0, 2.0, 3.0])
print(f"Input: {arr.data}")
exp_arr = arr.apply_ufunc('exp')
print(f"np.exp(): {[f'{x:.4f}' for x in exp_arr.data]}")

# Element-wise operations
print("\n4. Element-wise (Vectorized) Operations:")
a = NumpyUfuncs([1, 2, 3, 4, 5])
b = NumpyUfuncs([10, 20, 30, 40, 50])
print(f"a: {a.data}")
print(f"b: {b.data}")
add = NumpyUfuncs([x + y for x, y in zip(a.data, b.data)])
mul = NumpyUfuncs([x * y for x, y in zip(a.data, b.data)])
print(f"a + b: {add.data}")
print(f"a * b: {mul.data}")

# Broadcasting with ufuncs
print("\n5. Broadcasting with Universal Functions:")
scalar_data = [1, 2, 3, 4, 5]
scalar = 10
broadcasted_add = [x + scalar for x in scalar_data]
broadcasted_mul = [x * scalar for x in scalar_data]
print(f"arr: {scalar_data}")
print(f"arr + 10: {broadcasted_add}")
print(f"arr * 10: {broadcasted_mul}")

# Ufunc properties
print("\n6. Universal Function Properties:")
print("Ufuncs operate element-wise on arrays:")
print("  - Automatic broadcasting")
print("  - Fast C implementations")
print("  - Support for type casting")
print("  - Accumulate/reduce operations")

# Common ufuncs list
print("\n7. Common Universal Functions:")
math_funcs = [
    "sqrt, cbrt - roots",
    "exp, log, log10, log2 - exponential/logarithm",
    "sin, cos, tan - trigonometric",
    "sinh, cosh, tanh - hyperbolic",
    "arcsin, arccos, arctan - inverse trig",
    "abs, sign - magnitude/sign",
    "add, subtract, multiply, divide - arithmetic",
    "power, mod - power/modulo",
]
for func in math_funcs:
    print(f"  np.{func}")

print("\nReal NumPy API:")
print("import numpy as np")
print("np.sqrt(a), np.cbrt(a)")
print("np.exp(a), np.log(a), np.log10(a)")
print("np.sin(a), np.cos(a), np.tan(a)")
print("np.add(a, b), np.multiply(a, b)")
''',

    801: r'''# In production: import numpy as np
# This simulation demonstrates NumPy structured arrays without installation

class StructuredArray:
    """Simulates numpy structured array (record array) functionality"""
    def __init__(self, fields, data):
        self.fields = fields  # List of (name, dtype) tuples
        self.data = data      # List of tuples, one per record
        self.dtype = {'names': [f[0] for f in fields], 'formats': [f[1] for f in fields]}

    def __getitem__(self, field_name):
        """Access field by name"""
        if isinstance(field_name, str):
            idx = [f[0] for f in self.fields].index(field_name)
            return [record[idx] for record in self.data]
        elif isinstance(field_name, int):
            return self.data[field_name]

    def __setitem__(self, field_name, values):
        """Set field values"""
        if isinstance(field_name, str):
            idx = [f[0] for f in self.fields].index(field_name)
            for i, val in enumerate(values):
                self.data[i] = self.data[i][:idx] + (val,) + self.data[i][idx+1:]

    def view(self):
        """View as structured array"""
        return self

    def __repr__(self):
        lines = []
        for record in self.data[:3]:
            lines.append(str(record))
        return '\n'.join(lines)

# Demo: Named fields, structured arrays, records
print("NumPy Structured Arrays Simulation")
print("=" * 60)

# Define structured array with named fields
print("1. Defining Structured Array:")
print("dtype definition:")
print("  dtype = [('name', 'U10'), ('age', 'i4'), ('height', 'f4')]")

# Create sample structured array
fields = [('name', 'U10'), ('age', 'i4'), ('height', 'f4')]
data = [
    ('Alice', 25, 5.6),
    ('Bob', 30, 5.9),
    ('Charlie', 28, 5.8),
    ('Diana', 26, 5.4),
]
arr = StructuredArray(fields, data)

print("\n2. Accessing Full Records:")
for i, record in enumerate(data):
    print(f"  Record {i}: {record}")

print("\n3. Accessing Individual Fields:")
print(f"Names: {arr['name']}")
print(f"Ages: {arr['age']}")
print(f"Heights: {arr['height']}")

# Field operations
print("\n4. Field-wise Operations:")
ages = arr['age']
avg_age = sum(ages) / len(ages)
print(f"Average age: {avg_age:.1f}")

heights = arr['height']
max_height = max(heights)
min_height = min(heights)
print(f"Height range: {min_height} to {max_height}")

# Filtering by field
print("\n5. Filtering Structured Arrays:")
print("Adults (age >= 25):")
for i, (name, age, height) in enumerate(data):
    if age >= 25:
        print(f"  {name}: age={age}, height={height}")

# Complex dtype example
print("\n6. Complex Structured Array:")
print("Multi-level dtype example:")
print("  dtype = [('id', 'i4'), ('info', [('name', 'U10'), ('score', 'f4')])]")
print("Access: arr['info']['name']")
print("Access: arr['info']['score']")

# Use cases
print("\n7. Common Use Cases for Structured Arrays:")
use_cases = [
    "Database-like records (rows with named columns)",
    "Scientific data with mixed types",
    "Time series with multiple attributes",
    "Simulation output with complex metadata",
    "CSV/HDF5 data loading with mixed types",
]
for i, case in enumerate(use_cases, 1):
    print(f"  {i}. {case}")

# Performance notes
print("\n8. Memory Efficiency:")
print("Structured arrays store data contiguously")
print("Each record occupies fixed memory")
print("Fast field access without copying")
print("Direct memory layout matches C structs")

print("\nReal NumPy API:")
print("import numpy as np")
print("dtype = [('name', 'U10'), ('age', 'i4')]")
print("arr = np.array([('Alice', 25)], dtype=dtype)")
print("arr['name']  # Access field by name")
print("arr[0]  # Access record by index")
print("arr[arr['age'] > 25]  # Filter by field")
''',

    802: r'''# In production: import numpy as np
# This simulation demonstrates NumPy advanced indexing without installation

class NumpyIndexing:
    """Simulates numpy advanced indexing techniques"""
    def __init__(self, data, shape=None):
        self.data = data
        self.shape = shape or (len(data),) if isinstance(data, list) else ()

    def boolean_indexing(self, condition):
        """Select elements where condition is True"""
        result = []
        for item in self.data:
            if callable(condition):
                if condition(item):
                    result.append(item)
            else:
                result.append(item)
        return NumpyIndexing(result)

    def fancy_indexing(self, indices):
        """Select elements using integer array"""
        if isinstance(indices, list):
            return NumpyIndexing([self.data[i] for i in indices])
        return self

    def advanced_slice(self, start, stop, step=1):
        """Advanced slicing"""
        return NumpyIndexing(self.data[start:stop:step])

# Demo: Boolean indexing, fancy indexing, advanced selection
print("NumPy Advanced Indexing Simulation")
print("=" * 60)

# Boolean indexing
print("1. Boolean Indexing:")
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
arr = NumpyIndexing(data)
print(f"Array: {data}")

# Select elements > 50
print("\nSelect elements > 50:")
mask = [x > 50 for x in data]
print(f"Mask: {mask}")
filtered = [data[i] for i, m in enumerate(mask) if m]
print(f"Result: {filtered}")

# Select even numbers
print("\nSelect even numbers:")
mask_even = [x % 2 == 0 for x in data]
evens = [data[i] for i, m in enumerate(mask_even) if m]
print(f"Result: {evens}")

# Fancy indexing
print("\n2. Fancy Indexing (Integer Array Indexing):")
print(f"Array: {data}")
indices = [0, 2, 4, 6, 8]
print(f"Indices: {indices}")
result = [data[i] for i in indices]
print(f"arr[indices]: {result}")

# Out of order indices
print("\nOut-of-order selection:")
indices_disorder = [8, 2, 5, 1]
result_disorder = [data[i] for i in indices_disorder]
print(f"arr[[8, 2, 5, 1]]: {result_disorder}")

# 2D indexing
print("\n3. Advanced 2D Indexing:")
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("2D Array:")
for row in array_2d:
    print(f"  {row}")

# Row selection
print("\nRow fancy indexing arr[[0, 2]]:")
result_rows = [array_2d[i] for i in [0, 2]]
for row in result_rows:
    print(f"  {row}")

# Boolean 2D
print("\n4. Boolean Indexing in 2D:")
print("Select where value > 5:")
mask_2d = []
for row in array_2d:
    for val in row:
        if val > 5:
            mask_2d.append(val)
print(f"Result: {mask_2d}")

# np.where equivalent
print("\n5. Conditional Selection (np.where equivalent):")
arr = data
print(f"Array: {arr}")
condition_result = [x if x < 50 else 0 for x in arr]
print(f"np.where(arr < 50, arr, 0):")
print(f"  {condition_result}")

# Index tricks
print("\n6. Index Tricks and Patterns:")
print("Get indices of non-zero elements:")
nonzero = [i for i, x in enumerate([0, 1, 0, 2, 0, 3]) if x != 0]
print(f"  Indices: {nonzero}")

print("\nGet min/max indices:")
arr = [10, 5, 30, 15, 25]
print(f"  Array: {arr}")
print(f"  argmin (index of min): {arr.index(min(arr))}")
print(f"  argmax (index of max): {arr.index(max(arr))}")

# Advanced multi-axis
print("\n7. Multi-Axis Indexing:")
array_3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]
print("3D array shape (2, 2, 2):")
print(f"arr[0, 1, 1] = {array_3d[0][1][1]}")
print(f"arr[1, :, 0] (all middle axis, first last): [6, 8]")
print(f"arr[:, 0, :] (first middle axis, all first/last):")

# Performance considerations
print("\n8. Performance Considerations:")
print("Boolean indexing: Creates copy, but filters efficiently")
print("Fancy indexing: Flexible, but may create copies")
print("Simple slicing: Returns view, zero-copy")
print("Avoid: Multiple boolean operations in sequence")

print("\nReal NumPy API:")
print("import numpy as np")
print("arr[arr > 50]  # Boolean indexing")
print("arr[[0, 2, 5]]  # Fancy indexing")
print("arr[::2]  # Slicing with step")
print("np.where(condition, x, y)  # Conditional selection")
print("np.nonzero(arr)  # Find non-zero indices")
print("np.argsort(arr)  # Index sort order")
''',

    803: r'''# In production: import numpy as np
# This simulation demonstrates NumPy performance optimization without installation

class PerformanceOptimizer:
    """Performance tips and best practices"""
    def __init__(self):
        self.tips = []

    def vectorization_demo(self):
        """Demonstrate vectorization benefits"""
        data = list(range(1000))

        # Slow: Python loop
        result_slow = []
        for x in data:
            result_slow.append(x * 2 + 1)

        # Fast: NumPy-style vectorization
        result_fast = [x * 2 + 1 for x in data]

        return len(result_slow), len(result_fast)

    def memory_layout_demo(self):
        """Memory layout optimization"""
        # C-order (row-major): default
        c_order = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # F-order (column-major): Fortran-style
        f_order = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        return "C-order efficient for row ops, F-order for column ops"

    def dtype_optimization(self):
        """Data type selection impact"""
        return {
            'float64': (8, 'double precision'),
            'float32': (4, 'fast, less memory'),
            'int32': (4, 'integers, memory efficient'),
            'int16': (2, 'very memory efficient'),
        }

# Demo: Vectorization, broadcasting, memory layout, dtype
print("NumPy Performance Optimization Simulation")
print("=" * 60)

# 1. Vectorization
print("1. Vectorization Benefits:")
print("Slow approach - Python loop:")
print("  for i in range(1000000):")
print("    result[i] = data[i] * 2 + 1")
print("  Time: ~1000ms (estimated)")

print("\nFast approach - NumPy vectorization:")
print("  result = data * 2 + 1")
print("  Time: ~10ms (estimated)")
print("  Speedup: 100x")

# 2. Broadcasting optimization
print("\n2. Broadcasting for Memory Efficiency:")
print("Task: Add 1 to each row of 1000x1000 matrix")
print("\nInefficient:")
print("  for i in range(1000):")
print("    matrix[i] = matrix[i] + 1  # Copies entire row")

print("\nEfficient (broadcasting):")
print("  matrix = matrix + 1  # Broadcasting, minimal copying")

# 3. Memory layout
print("\n3. Memory Layout Optimization:")
matrix = [[i*10+j for j in range(5)] for i in range(5)]
print("Row-major (C-order) - default NumPy:")
print("  Efficient: iterate rows")
print("  Memory: [0,1,2,3,4,10,11,12,13,14,...]")
print("  Access time: fast row iteration")

print("\nColumn-major (F-order):")
print("  Efficient: iterate columns")
print("  Memory: [0,10,20,30,40,1,11,21,31,41,...]")
print("  Access time: fast column iteration")

# 4. Data type impact
print("\n4. Data Type Selection Impact:")
print("Array: 1 million elements")
sizes = {
    'bool': (1, 0.001),
    'int8': (1, 0.001),
    'int32': (4, 0.004),
    'int64': (8, 0.008),
    'float32': (4, 0.004),
    'float64': (8, 0.008),
    'complex128': (16, 0.016),
}
for dtype, (size, mb) in sizes.items():
    print(f"  {dtype:12} - {mb:.3f} MB")

# 5. Avoiding copies
print("\n5. Avoiding Unnecessary Copies:")
print("Inefficient: explicit loop")
print("  for i in range(n):")
print("    result[i] = arr[i] * scalar  # n assignments")

print("\nEfficient: in-place operation")
print("  arr *= scalar  # Single operation")

print("\nEfficient: vectorized")
print("  result = arr * scalar  # Vectorized, fast")

# 6. View vs. Copy
print("\n6. View vs. Copy Selection:")
print("Use view when:")
print("  - Just need different shape")
print("  - Don't modify data")
print("  - Memory critical")

print("\nUse copy when:")
print("  - Need to modify independently")
print("  - Changing dtype")
print("  - Data source might be garbage collected")

# 7. Algorithm optimization
print("\n7. Algorithm Optimization Strategies:")
optimizations = [
    "Use ufuncs (np.sqrt, np.sin, etc) - compiled C",
    "Use built-in functions (np.sum, np.mean) vs loops",
    "Reduce dimensionality: (n,) faster than (1,n)",
    "Batch operations together to minimize passes",
    "Use appropriate dtype (smallest sufficient size)",
    "Cache computations (avoid recalculating)",
    "Profile before optimizing - measure impact",
]
for i, opt in enumerate(optimizations, 1):
    print(f"  {i}. {opt}")

# 8. Profiling
print("\n8. Performance Measurement:")
print("import time")
print("start = time.time()")
print("# Operation")
print("elapsed = time.time() - start")
print("\nUse: timeit module for microsecond operations")
print("Or: cProfile for function-level timing")

print("\nReal NumPy API:")
print("import numpy as np")
print("arr = np.array(..., dtype=np.float32)  # Choose dtype")
print("view = arr.reshape(...)  # View, no copy")
print("copy = arr.copy()  # Explicit copy")
print("np.sum(arr, axis=0)  # Vectorized sum")
print("np.dot(a, b)  # Optimized matrix multiplication")
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
    print(f"Updated {len(updated)} lessons in batch 2: {updated}")

if __name__ == '__main__':
    sys.exit(main())
