"""NumPy simulations batch 1 - Lessons 523, 793-797"""
import json
import sys

NUMPY_BATCH = {
    523: r'''# In production: import numpy as np
# This simulation demonstrates NumPy array operations without installation

class NumpyArray:
    """Simulates numpy.ndarray functionality"""
    def __init__(self, data, shape=None):
        self.data = data if isinstance(data, list) else list(data)
        if shape:
            self.shape = shape
        else:
            self.shape = (len(self.data),) if isinstance(self.data, list) else ()
        self.dtype = type(self.data[0]).__name__ if self.data else 'float64'

    def mean(self):
        return sum(self.data) / len(self.data) if self.data else 0

    def std(self):
        m = self.mean()
        variance = sum((x - m) ** 2 for x in self.data) / len(self.data)
        return variance ** 0.5

    def sum(self):
        return sum(self.data)

    def __add__(self, other):
        if isinstance(other, NumpyArray):
            return NumpyArray([a + b for a, b in zip(self.data, other.data)])
        return NumpyArray([x + other for x in self.data])

    def __mul__(self, scalar):
        return NumpyArray([x * scalar for x in self.data])

    def __repr__(self):
        return f"array({self.data})"

# Demo: Array operations, vectorized operations, and basic statistics
print("NumPy Array Operations Simulation")
print("=" * 60)

# Create arrays
arr1 = NumpyArray([1, 2, 3, 4, 5])
arr2 = NumpyArray([10, 20, 30, 40, 50])
print(f"arr1 = {arr1}")
print(f"arr2 = {arr2}")

# Vectorized operations
print("\nVectorized Operations:")
result_add = arr1 + arr2
print(f"arr1 + arr2 = {result_add}")
result_mul = arr1 * 3
print(f"arr1 * 3 = {result_mul}")

# Statistics
print("\nStatistics:")
print(f"arr1.mean() = {arr1.mean():.2f}")
print(f"arr1.std() = {arr1.std():.4f}")
print(f"arr1.sum() = {arr1.sum()}")

# Broadcasting concept
print("\nBroadcasting example:")
scalar_op = arr1 + 10
print(f"arr1 + 10 = {scalar_op}")

print("\nReal NumPy API:")
print("import numpy as np")
print("arr = np.array([1, 2, 3, 4, 5])")
print("arr.mean(), arr.std(), arr.sum()")
print("arr + np.array([10, 20, 30, 40, 50])")
''',

    793: r'''# In production: import numpy as np
# This simulation demonstrates NumPy matrix operations without installation

class NumpyMatrix:
    """Simulates numpy.ndarray for 2D operations"""
    def __init__(self, data):
        self.data = data
        self.shape = (len(data), len(data[0]) if data else 0)
        self.dtype = 'float64'

    def transpose(self):
        """Return transposed matrix"""
        rows = self.shape[1]
        cols = self.shape[0]
        transposed = [[self.data[j][i] for j in range(cols)] for i in range(rows)]
        result = NumpyMatrix(transposed)
        return result

    def dot(self, other):
        """Matrix multiplication"""
        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(other.shape[1]):
                val = sum(self.data[i][k] * other.data[k][j] for k in range(self.shape[1]))
                row.append(val)
            result.append(row)
        return NumpyMatrix(result)

    def __repr__(self):
        return f"array({self.data})"

# Demo: 2D matrices, multiplication, transpose
print("NumPy Matrix Operations Simulation")
print("=" * 60)

matrix_a = NumpyMatrix([[1, 2], [3, 4]])
matrix_b = NumpyMatrix([[5, 6], [7, 8]])

print("Matrix A:")
for row in matrix_a.data:
    print(f"  {row}")
print(f"Shape: {matrix_a.shape}")

print("\nMatrix B:")
for row in matrix_b.data:
    print(f"  {row}")
print(f"Shape: {matrix_b.shape}")

# Transpose
print("\nTranspose of A:")
a_t = matrix_a.transpose()
for row in a_t.data:
    print(f"  {row}")

# Matrix multiplication
print("\nMatrix multiplication (A @ B):")
result = matrix_a.dot(matrix_b)
for row in result.data:
    print(f"  {row}")

# Element-wise operations
print("\nElement-wise multiplication:")
result_elem = [[matrix_a.data[i][j] * matrix_b.data[i][j] for j in range(2)] for i in range(2)]
for row in result_elem:
    print(f"  {row}")

print("\nReal NumPy API:")
print("import numpy as np")
print("A = np.array([[1, 2], [3, 4]])")
print("A.T or A.transpose()")
print("np.dot(A, B) or A @ B")
''',

    794: r'''# In production: import numpy as np
# This simulation demonstrates NumPy broadcasting without installation

class NumpyBroadcast:
    """Simulates numpy broadcasting rules"""
    def __init__(self, data, shape):
        self.data = data
        self.shape = shape

    def broadcast_to(self, shape):
        """Broadcast array to new shape"""
        if len(shape) > len(self.shape):
            padded_shape = (1,) * (len(shape) - len(self.shape)) + self.shape
        else:
            padded_shape = self.shape

        # Check compatibility
        for i, (old, new) in enumerate(zip(padded_shape, shape)):
            if old != 1 and old != new:
                raise ValueError(f"Cannot broadcast shape {self.shape} to {shape}")

        return NumpyBroadcast(self.data, shape)

    def __repr__(self):
        return f"array({self.data}, shape={self.shape})"

# Demo: Shape alignment, broadcasting rules
print("NumPy Broadcasting Simulation")
print("=" * 60)

# Example 1: scalar broadcast
print("Example 1: Scalar + Array")
scalar = 5
array_shape = (3, 4)
print(f"Scalar shape: () broadcasts to {array_shape}")
result_data = [[scalar] * 4 for _ in range(3)]
print("Result shape: (3, 4)")
print(f"Result:\n{result_data}")

# Example 2: 1D to 2D
print("\nExample 2: 1D Array broadcast to 2D")
array_1d = [1, 2, 3, 4]
print(f"1D array shape: (4,)")
print(f"Broadcasting to shape: (3, 4)")
result_2d = [array_1d for _ in range(3)]
print(f"Result:\n{result_2d}")

# Example 3: shape compatibility
print("\nExample 3: Shape compatibility check")
shapes_pairs = [
    ((3, 1), (3, 4), True),
    ((1, 4), (3, 4), True),
    ((4,), (3, 4), True),
    ((2,), (3, 4), False),
]
for shape1, shape2, compatible in shapes_pairs:
    status = "Compatible" if compatible else "Incompatible"
    print(f"  {shape1} with {shape2}: {status}")

# Example 4: actual operation
print("\nExample 4: Broadcasting in operation")
a = [[1], [2], [3]]  # shape (3, 1)
b = [10, 20, 30, 40]  # shape (4,)
print(f"Array A shape: (3, 1)\n{a}")
print(f"Array B shape: (4,)\n{b}")
result = [[a[i][0] + b[j] for j in range(4)] for i in range(3)]
print(f"Result shape: (3, 4)\n{result}")

print("\nReal NumPy API:")
print("import numpy as np")
print("a = np.array([[1], [2], [3]])  # shape (3, 1)")
print("b = np.array([10, 20, 30, 40])  # shape (4,)")
print("result = a + b  # broadcasts to (3, 4)")
''',

    795: r'''# In production: import numpy as np
# This simulation demonstrates NumPy advanced operations without installation

class NumpyAdvanced:
    """Simulates numpy reshape, stack, and concatenate operations"""
    def __init__(self, data, shape):
        self.data = data
        self.shape = shape

    def reshape(self, new_shape):
        """Reshape array to new dimensions"""
        size = 1
        for dim in new_shape:
            size *= dim
        if size != len(self.data):
            raise ValueError(f"Cannot reshape to {new_shape}")
        return NumpyAdvanced(self.data, new_shape)

    def flatten(self):
        """Flatten to 1D"""
        return NumpyAdvanced(self.data, (len(self.data),))

    def __repr__(self):
        return f"array({self.data}, shape={self.shape})"

# Demo: Reshape, stack, concatenate operations
print("NumPy Advanced Operations Simulation")
print("=" * 60)

# Reshape operation
print("1. Reshape operation:")
flat_data = [1, 2, 3, 4, 5, 6]
arr = NumpyAdvanced(flat_data, (6,))
print(f"Original: {arr.data}, shape: {arr.shape}")
reshaped_2x3 = arr.reshape((2, 3))
print(f"Reshaped to (2, 3):")
for i in range(2):
    print(f"  {arr.data[i*3:(i+1)*3]}")
reshaped_3x2 = arr.reshape((3, 2))
print(f"Reshaped to (3, 2):")
for i in range(3):
    print(f"  {arr.data[i*2:(i+1)*2]}")

# Concatenate
print("\n2. Concatenate operation:")
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(f"arr1: {arr1}")
print(f"arr2: {arr2}")
concat = arr1 + arr2
print(f"np.concatenate([arr1, arr2]): {concat}")

# Stack
print("\n3. Stack operation:")
arr1_2d = [[1, 2], [3, 4]]
arr2_2d = [[5, 6], [7, 8]]
print(f"arr1 shape (2, 2):\n{arr1_2d}")
print(f"arr2 shape (2, 2):\n{arr2_2d}")
stacked = [arr1_2d, arr2_2d]
print(f"np.stack([arr1, arr2]) shape (2, 2, 2)")
print(f"Result: {stacked}")

# Squeeze and expand dims
print("\n4. Dimension manipulation:")
squeezed_shape = (3, 1)
print(f"Original shape: {squeezed_shape}")
print(f"After squeeze (remove size-1 dims): (3,)")
print(f"After expand_dims at axis 1: (3, 1, 1)")

print("\nReal NumPy API:")
print("import numpy as np")
print("arr = np.array([1,2,3,4,5,6])")
print("arr.reshape((2, 3))")
print("np.concatenate([arr1, arr2])")
print("np.stack([arr1, arr2])")
print("np.squeeze(), np.expand_dims()")
''',

    796: r'''# In production: import numpy as np
# This simulation demonstrates NumPy linear algebra without installation

class NumpyLinAlg:
    """Simulates numpy linear algebra operations"""
    def __init__(self, data):
        self.data = data
        self.shape = (len(data), len(data[0]) if data else 0)

    def dot(self, other):
        """Matrix dot product"""
        result = 0
        if isinstance(other, list):
            result = sum(a * b for a, b in zip(self.data, other))
        else:
            result = sum(sum(self.data[i][j] * other.data[i][j] for j in range(len(other.data[0]))) for i in range(len(self.data)))
        return result

    def norm(self, order=2):
        """Calculate matrix norm"""
        if order == 2:
            flat = [self.data[i][j] for i in range(len(self.data)) for j in range(len(self.data[0]))]
            return sum(x**2 for x in flat) ** 0.5
        return sum(sum(abs(self.data[i][j]) for j in range(len(self.data[0]))) for i in range(len(self.data)))

    def trace(self):
        """Sum of diagonal elements"""
        return sum(self.data[i][i] for i in range(min(len(self.data), len(self.data[0]))))

    def transpose(self):
        """Return transposed matrix"""
        rows = self.shape[1]
        cols = self.shape[0]
        transposed = [[self.data[j][i] for j in range(cols)] for i in range(rows)]
        return NumpyLinAlg(transposed)

# Demo: Dot product, norm, trace, determinant concepts
print("NumPy Linear Algebra Simulation")
print("=" * 60)

# Dot product
print("1. Dot Product:")
v1 = [1, 2, 3]
v2 = [4, 5, 6]
dot_result = sum(a * b for a, b in zip(v1, v2))
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"np.dot(v1, v2) = {dot_result}")

# Matrix operations
print("\n2. Matrix Dot Product:")
m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
print(f"Matrix 1:\n{m1}")
print(f"Matrix 2:\n{m2}")
result_00 = m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0]
result_01 = m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]
result_10 = m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]
result_11 = m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]
print(f"np.dot(M1, M2) = [[{result_00}, {result_01}], [{result_10}, {result_11}]]")

# Norm
print("\n3. Matrix Norm (Frobenius):")
flat = [m1[i][j] for i in range(2) for j in range(2)]
norm_val = sum(x**2 for x in flat) ** 0.5
print(f"Matrix:\n{m1}")
print(f"np.linalg.norm(M) = {norm_val:.4f}")

# Trace
print("\n4. Matrix Trace:")
trace_val = m1[0][0] + m1[1][1]
print(f"Matrix:\n{m1}")
print(f"np.trace(M) = {trace_val}")

# Transpose
print("\n5. Transpose (useful in linear algebra):")
print(f"Original M:\n{m1}")
m1_t = [[m1[j][i] for j in range(2)] for i in range(2)]
print(f"M.T:\n{m1_t}")

print("\nReal NumPy API:")
print("import numpy as np")
print("np.dot(a, b) or a @ b")
print("np.linalg.norm(a)")
print("np.trace(a)")
print("np.linalg.det(a), np.linalg.inv(a)")
''',

    797: r'''# In production: import numpy as np
# This simulation demonstrates NumPy FFT/signal processing without installation

class NumpyFFT:
    """Simulates numpy FFT operations for frequency analysis"""
    def __init__(self, signal):
        self.signal = signal
        self.length = len(signal)

    def compute_spectrum(self):
        """Simulate frequency spectrum computation"""
        # Simplified: return magnitude at each frequency
        spectrum = []
        for k in range(self.length):
            real = sum(self.signal[n] * self._cos(2 * 3.14159 * k * n / self.length) for n in range(self.length))
            imag = sum(-self.signal[n] * self._sin(2 * 3.14159 * k * n / self.length) for n in range(self.length))
            magnitude = (real**2 + imag**2) ** 0.5
            spectrum.append(magnitude)
        return spectrum

    @staticmethod
    def _cos(x):
        """Approximate cosine"""
        return 1 - x**2/2 + x**4/24 - x**6/720

    @staticmethod
    def _sin(x):
        """Approximate sine"""
        return x - x**3/6 + x**5/120 - x**7/5040

# Demo: FFT, frequency analysis, signal processing
print("NumPy FFT/Signal Processing Simulation")
print("=" * 60)

# Sample signal: combination of frequencies
print("1. Time Domain Signal:")
time = list(range(0, 8))
# Signal: 2*sin(2*pi*t) + sin(2*pi*2*t)
signal = [2.0 * (t % 4 - 2)**2/4 + (t % 2) for t in range(16)]
print(f"Time samples: {time[:8]}")
print(f"Signal (16 samples): {[f'{x:.2f}' for x in signal[:8]]}")

# FFT analysis
print("\n2. Frequency Domain Analysis:")
fft_sim = NumpyFFT(signal)
spectrum = fft_sim.compute_spectrum()
print(f"Spectrum magnitude (first 8 frequencies):")
for i in range(min(8, len(spectrum))):
    magnitude = spectrum[i]
    print(f"  Frequency {i}: {magnitude:.4f}")

# Windowing concept
print("\n3. Window Functions (for edge effects):")
window_types = ["Hann", "Hamming", "Blackman", "Rectangular"]
print("Different window functions reduce spectral leakage:")
for wtype in window_types:
    print(f"  - {wtype} window")

# Power spectrum
print("\n4. Power Spectrum:")
power = [mag**2 for mag in spectrum[:8]]
for i, p in enumerate(power):
    print(f"  Frequency {i}: Power = {p:.4f}")

# Filtering concept
print("\n5. Frequency Filtering:")
print("Filter types:")
print("  - Low-pass: Keep low frequencies, remove high noise")
print("  - High-pass: Keep high frequencies, remove DC offset")
print("  - Band-pass: Keep specific frequency range")
print("  - Band-stop: Remove specific frequency range")

# Real vs. complex FFT
print("\n6. Real vs. Complex FFT:")
print("For real signals, only first N/2 frequencies needed")
print(f"Signal length: {len(signal)}")
print(f"Unique frequencies: {len(signal)//2 + 1}")

print("\nReal NumPy API:")
print("import numpy as np")
print("fft = np.fft.fft(signal)")
print("freqs = np.fft.fftfreq(len(signal), dt)")
print("magnitude = np.abs(fft)")
print("power = np.abs(fft)**2")
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
    print(f"Updated {len(updated)} lessons in batch 1: {updated}")

if __name__ == '__main__':
    sys.exit(main())
