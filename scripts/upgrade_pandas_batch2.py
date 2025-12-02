"""
Upgrade pandas lessons in batches to avoid token limits
This script upgrades 12 pandas lessons with realistic simulations
Batch 2: Advanced pandas operations and real-world scenarios
"""

import json
import sys

# Batch 2: Advanced pandas operations (12 lessons)
PANDAS_BATCH_2 = {
    790: """# In production: import pandas as pd
# df = pd.read_csv('data.csv', parse_dates=['date'])
# time_series = df.set_index('date').resample('D').sum()
# This simulation demonstrates time series analysis without pandas

from datetime import datetime, timedelta

class DatetimeIndex:
    \"\"\"Simulates pandas DatetimeIndex\"\"\"
    def __init__(self, dates):
        self.dates = dates

    def resample(self, freq):
        \"\"\"Resample time series data\"\"\"
        # freq: 'D'=daily, 'W'=weekly, 'M'=monthly, etc.
        return ResampleObject(self.dates, freq)

class ResampleObject:
    \"\"\"Simulates pandas Resampler\"\"\"
    def __init__(self, dates, freq):
        self.dates = dates
        self.freq = freq

    def sum(self, values):
        \"\"\"Sum values by resampling period\"\"\"
        if self.freq == 'D':
            return values  # Daily stays same
        elif self.freq == 'W':
            # Group by week
            result = {}
            for i, (date, val) in enumerate(zip(self.dates, values)):
                week_start = date - timedelta(days=date.weekday())
                key = week_start.strftime('%Y-%m-%d')
                result[key] = result.get(key, 0) + val
            return result
        elif self.freq == 'M':
            # Group by month
            result = {}
            for date, val in zip(self.dates, values):
                key = date.strftime('%Y-%m')
                result[key] = result.get(key, 0) + val
            return result

    def mean(self, values):
        \"\"\"Mean values by resampling period\"\"\"
        sums = self.sum(values)
        counts = {}
        for date, val in zip(self.dates, values):
            if self.freq == 'D':
                key = date.strftime('%Y-%m-%d')
            elif self.freq == 'W':
                key = (date - timedelta(days=date.weekday())).strftime('%Y-%m-%d')
            elif self.freq == 'M':
                key = date.strftime('%Y-%m')
            counts[key] = counts.get(key, 0) + 1

        return {k: sums[k] / counts[k] for k in sums}

class DataFrameSimulation:
    \"\"\"Simulates pandas DataFrame with datetime index\"\"\"
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())
        self.index = None

    def set_index(self, col):
        \"\"\"Set a column as index\"\"\"
        self.index = DatetimeIndex(self.data[col])
        return self

    def __repr__(self):
        result = "  " + "  ".join(f"{col:>15}" for col in self.columns) + "\\n"
        for i in range(min(len(list(self.data.values())[0]), 10)):
            row = f"{i}  "
            for col in self.columns:
                val = str(self.data[col][i])[:15]
                row += f"{val:>15}  "
            result += row + "\\n"
        return result

# Demo: Time Series Analysis
print("Pandas Time Series Analysis - Simulation")
print("=" * 70)

# Create time series data
dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(30)]
values = [100 + i*2 + (i%7)*5 for i in range(30)]
categories = ['Product_A'] * 15 + ['Product_B'] * 15

data = {
    'date': dates,
    'sales': values,
    'category': categories
}

df = DataFrameSimulation(data)

print("\\nOriginal Time Series Data (first 10 days):")
print(df)

print("\\n" + "=" * 70)
print("Time Series Operations:")
print("=" * 70)

# Simulating date_range
print("\\n1. pd.date_range('2024-01-01', periods=30) - Create date sequence:")
for i, date in enumerate(dates[:5]):
    print(f"   {date.strftime('%Y-%m-%d')}")
print("   ... (25 more dates)")

# Simulating resample
print("\\n2. Resample to weekly (sum):")
df_ts = DataFrameSimulation(data)
df_ts.set_index('date')
weekly_sum = df_ts.index.resample('W').sum(values)
for week, total in sorted(weekly_sum.items())[:4]:
    print(f"   Week of {week}: ${total:,.0f}")

# Simulating datetime indexing
print("\\n3. Select data in date range:")
start_date = datetime(2024, 1, 5)
end_date = datetime(2024, 1, 10)
filtered = [v for d, v in zip(dates, values) if start_date <= d <= end_date]
print(f"   Sales from {start_date.date()} to {end_date.date()}: {filtered}")

# Simulating shift
print("\\n4. Shift (previous day value):")
print("   Date       | Sales | Prev Day")
for i in range(3, 8):
    prev_val = values[i-1] if i > 0 else None
    print(f"   {dates[i].strftime('%Y-%m-%d')} | {values[i]:5} | {prev_val}")

# Simulating pct_change
print("\\n5. Percent change from previous day:")
for i in range(1, 6):
    pct_change = ((values[i] - values[i-1]) / values[i-1] * 100)
    print(f"   {dates[i].strftime('%Y-%m-%d')}: {pct_change:+.2f}%")

print("\\n" + "=" * 70)
print("Real pandas time series:")
print("  pd.date_range('2024-01-01', periods=30)")
print("  df.set_index('date').resample('W').sum()")
print("  df.loc['2024-01-05':'2024-01-10']")
print("  df['sales'].shift(1)  # Previous value")
print("  df['sales'].pct_change()  # Percentage change")""",

    791: """# In production: import pandas as pd
# df = df.dropna()
# df = df.fillna(0)
# df = df[~df.duplicated()]
# This simulation demonstrates data cleaning techniques

class DataFrameSimulation:
    \"\"\"Simulates pandas DataFrame with cleaning methods\"\"\"
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())
        self.n_rows = len(list(data.values())[0])

    def dropna(self):
        \"\"\"Remove rows with None/NaN values\"\"\"
        # Simulation: Remove rows where any column has None
        new_data = {col: [] for col in self.columns}

        for i in range(self.n_rows):
            has_na = False
            for col in self.columns:
                if self.data[col][i] is None:
                    has_na = True
                    break

            if not has_na:
                for col in self.columns:
                    new_data[col].append(self.data[col][i])

        return DataFrameSimulation(new_data)

    def fillna(self, value):
        \"\"\"Fill NaN values with specified value\"\"\"
        new_data = {}
        for col in self.columns:
            new_data[col] = [v if v is not None else value for v in self.data[col]]
        return DataFrameSimulation(new_data)

    def drop_duplicates(self, subset=None):
        \"\"\"Remove duplicate rows\"\"\"
        new_data = {col: [] for col in self.columns}
        seen = set()

        check_cols = subset if subset else self.columns

        for i in range(self.n_rows):
            row_tuple = tuple(self.data[col][i] for col in check_cols)

            if row_tuple not in seen:
                seen.add(row_tuple)
                for col in self.columns:
                    new_data[col].append(self.data[col][i])

        return DataFrameSimulation(new_data)

    def replace(self, old_value, new_value):
        \"\"\"Replace values in DataFrame\"\"\"
        new_data = {}
        for col in self.columns:
            new_data[col] = [new_value if v == old_value else v for v in self.data[col]]
        return DataFrameSimulation(new_data)

    def __repr__(self):
        result = "  " + "  ".join(f"{col:>12}" for col in self.columns) + "\\n"
        for i in range(self.n_rows):
            row = f"{i}  "
            for col in self.columns:
                val = str(self.data[col][i])[:12]
                row += f"{val:>12}  "
            result += row + "\\n"
        return result

# Demo: Data Cleaning
print("Pandas Data Cleaning - Simulation")
print("=" * 70)

# Messy data with missing values, duplicates, and inconsistencies
data = {
    'ID': [1, 2, 2, 3, None, 5, 6, 6, 8, 9],
    'Name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Frank', 'Henry', 'Iris'],
    'Age': [25, 30, 30, None, 35, 28, 32, 32, None, 29],
    'Salary': [50000, 60000, 60000, 75000, 0, 55000, 70000, 70000, 62000, 58000]
}

df = DataFrameSimulation(data)

print("\\n1. Original messy data (10 rows):")
print(df)
print(f"Total rows: {df.n_rows}")

# Cleaning step 1: Drop duplicates
print("\\n" + "=" * 70)
print("Step 1: dropna() - Remove rows with missing values")
print("=" * 70)
df_no_na = df.dropna()
print(df_no_na)
print(f"Rows after dropna: {df_no_na.n_rows} (removed {df.n_rows - df_no_na.n_rows})")

# Cleaning step 2: Fill missing values
print("\\n" + "=" * 70)
print("Step 2: fillna(value) - Fill missing values with 0")
print("=" * 70)
df_filled = df.fillna(0)
print(df_filled)

# Cleaning step 3: Remove duplicates
print("\\n" + "=" * 70)
print("Step 3: drop_duplicates() - Remove duplicate rows")
print("=" * 70)
df_unique = df.drop_duplicates(subset=['ID', 'Name'])
print(df_unique)
print(f"Rows after drop_duplicates: {df_unique.n_rows}")

# Cleaning step 4: Replace values
print("\\n" + "=" * 70)
print("Step 4: replace(old, new) - Fix data inconsistencies")
print("=" * 70)
df_replaced = df_filled.replace(0, 'Unknown')
print("Replaced 0 with 'Unknown' in Salary column")
print(df_replaced)

# Combined cleaning pipeline
print("\\n" + "=" * 70)
print("Complete cleaning pipeline:")
print("=" * 70)
df_clean = df.fillna(0).drop_duplicates(subset=['ID']).replace(0, 'Unknown')
print(f"Final cleaned data: {df_clean.n_rows} rows, {len(df_clean.columns)} columns")

print("\\n" + "=" * 70)
print("Real pandas cleaning operations:")
print("  df.dropna()  # Remove None/NaN")
print("  df.fillna(0)  # Fill with value")
print("  df.drop_duplicates(['col1', 'col2'])  # Remove duplicates")
print("  df.replace(old, new)  # Find and replace")
print("  df.astype('int64')  # Convert data types")
print("  df['col'].str.strip()  # Clean whitespace")""",

    792: """# In production: import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(1000, 4))
# result = df * 2
# This simulation demonstrates numpy-pandas integration

class NumpyArraySimulation:
    \"\"\"Simulates numpy ndarray\"\"\"
    def __init__(self, data, dtype='float64'):
        self.data = data
        self.shape = (len(data), len(data[0]) if isinstance(data[0], list) else 1)
        self.dtype = dtype
        self.ndim = len(self.shape)

    def __repr__(self):
        return f"array with shape {self.shape}, dtype={self.dtype}"

    def mean(self, axis=None):
        \"\"\"Calculate mean\"\"\"
        if axis is None:
            all_vals = [v for row in self.data for v in (row if isinstance(row, list) else [row])]
            return sum(all_vals) / len(all_vals)
        elif axis == 0:
            # Mean of columns
            cols = len(self.data[0]) if isinstance(self.data[0], list) else 1
            means = []
            for c in range(cols):
                col_data = [self.data[r][c] if isinstance(self.data[r], list) else self.data[r] for r in range(len(self.data))]
                means.append(sum(col_data) / len(col_data))
            return means
        return None

    def std(self, axis=None):
        \"\"\"Calculate standard deviation\"\"\"
        if axis is None:
            all_vals = [v for row in self.data for v in (row if isinstance(row, list) else [row])]
            mean = sum(all_vals) / len(all_vals)
            variance = sum((v - mean) ** 2 for v in all_vals) / len(all_vals)
            return variance ** 0.5
        return None

class DataFrameSimulation:
    \"\"\"Simulates pandas DataFrame with numpy integration\"\"\"
    def __init__(self, data=None):
        if isinstance(data, dict):
            self.data = data
            self.columns = list(data.keys())
            self.shape = (len(list(data.values())[0]), len(self.columns))
        elif isinstance(data, NumpyArraySimulation):
            # From numpy array
            self.data = {}
            for i in range(data.shape[1]):
                self.data[f'col_{i}'] = [data.data[r][i] for r in range(data.shape[0])]
            self.columns = list(self.data.keys())
            self.shape = data.shape
        else:
            self.data = data or {}
            self.columns = []
            self.shape = (0, 0)

    def __mul__(self, scalar):
        \"\"\"Vectorized multiplication\"\"\"
        new_data = {}
        for col in self.columns:
            new_data[col] = [v * scalar for v in self.data[col]]
        return DataFrameSimulation(new_data)

    def __add__(self, scalar):
        \"\"\"Vectorized addition\"\"\"
        new_data = {}
        for col in self.columns:
            new_data[col] = [v + scalar for v in self.data[col]]
        return DataFrameSimulation(new_data)

    def astype(self, dtype):
        \"\"\"Convert data types\"\"\"
        new_data = {}
        for col in self.columns:
            if dtype == 'int64':
                new_data[col] = [int(v) for v in self.data[col]]
            elif dtype == 'float64':
                new_data[col] = [float(v) for v in self.data[col]]
            else:
                new_data[col] = self.data[col]
        return DataFrameSimulation(new_data)

    def __repr__(self):
        result = f"DataFrame with shape {self.shape}\\n"
        result += "  " + "  ".join(f"{col:>10}" for col in self.columns) + "\\n"
        for i in range(min(self.shape[0], 5)):
            row = f"{i}  "
            for col in self.columns:
                val = f"{self.data[col][i]:.2f}" if isinstance(self.data[col][i], float) else str(self.data[col][i])
                row += f"{val:>10}  "
            result += row + "\\n"
        if self.shape[0] > 5:
            result += f"... {self.shape[0] - 5} more rows\\n"
        return result

# Demo: NumPy Integration
print("NumPy and Pandas Integration - Simulation")
print("=" * 70)

# Create numpy-like array
print("\\n1. np.random.randn() - Generate random data")
print("   (Creates normally distributed random numbers)")
np_data = [
    [0.5, -1.2, 2.3, -0.8],
    [1.1, 0.3, -0.5, 1.9],
    [-0.3, 1.5, 0.8, -1.1],
    [2.0, -0.7, 1.2, 0.4]
]
arr = NumpyArraySimulation(np_data, dtype='float64')
print(f"   Shape: {arr.shape}, Dtype: {arr.dtype}")

# Convert to DataFrame
df = DataFrameSimulation(arr)
print("\\n2. Create DataFrame from numpy array:")
print(df)

# Vectorized operations
print("\\n3. Vectorized operations (numpy integration):")
df_mul = df * 2
print("\\n   df * 2 (multiply all values by 2):")
print(df_mul)

df_add = df + 10
print("\\n   df + 10 (add 10 to all values):")
print(df_add)

# Type conversion
print("\\n4. Convert data types:")
df_int = df.astype('int64')
print("\\n   df.astype('int64'):")
print(df_int)

# NumPy statistical functions
print("\\n5. NumPy statistical operations:")
mean_val = arr.mean()
std_val = arr.std()
print(f"   Overall mean: {mean_val:.3f}")
print(f"   Overall std:  {std_val:.3f}")

col_means = arr.mean(axis=0)
print(f"   Column means: {[f'{m:.2f}' for m in col_means]}")

print("\\n" + "=" * 70)
print("Real pandas-numpy integration:")
print("  import numpy as np")
print("  arr = np.random.randn(1000, 4)")
print("  df = pd.DataFrame(arr)")
print("  df * 2  # Vectorized operation")
print("  df.astype('int64')  # Type conversion")
print("  df.values  # Get underlying numpy array")
print("  df.dtypes  # Check column types")""",

    970: """# In production: import pandas as pd
# df = df.set_index(['level1', 'level2'])
# stacked = df.stack()
# unstacked = df.unstack()
# This simulation demonstrates MultiIndex DataFrames

class MultiIndexSimulation:
    \"\"\"Simulates pandas MultiIndex\"\"\"
    def __init__(self, index_data):
        self.levels = index_data  # List of tuples
        self.names = None

    def names_property(self, names):
        self.names = names
        return self

    def swaplevel(self, i, j):
        \"\"\"Swap index levels\"\"\"
        new_levels = []
        for level in self.levels:
            level_list = list(level)
            level_list[i], level_list[j] = level_list[j], level_list[i]
            new_levels.append(tuple(level_list))
        return MultiIndexSimulation(new_levels)

class DataFrameSimulation:
    \"\"\"Simulates pandas DataFrame with MultiIndex support\"\"\"
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())
        self.index = None
        self.multi_index = False

    def set_index(self, cols):
        \"\"\"Set columns as index (supports multiple columns)\"\"\"
        if isinstance(cols, list):
            self.multi_index = True
            index_levels = []
            n_rows = len(list(self.data.values())[0])

            for i in range(n_rows):
                level = tuple(self.data[col][i] for col in cols)
                index_levels.append(level)

            self.index = MultiIndexSimulation(index_levels)
            self.index.names = cols

            # Remove indexed columns from data
            new_data = {col: self.data[col] for col in self.columns if col not in cols}
            self.data = new_data
            self.columns = list(new_data.keys())

        return self

    def stack(self):
        \"\"\"Stack columns into rows (pivot operation)\"\"\"
        # Simplified: convert wide to long format
        stacked_data = {
            'row_index': [],
            'variable': [],
            'value': []
        }

        n_rows = len(list(self.data.values())[0])
        for col in self.columns:
            for i in range(n_rows):
                stacked_data['row_index'].append(i)
                stacked_data['variable'].append(col)
                stacked_data['value'].append(self.data[col][i])

        return DataFrameSimulation(stacked_data)

    def unstack(self):
        \"\"\"Unstack (pivot longer data to wide)\"\"\"
        # Create wide format from long
        result = {}
        return DataFrameSimulation(result)

    def __repr__(self):
        result = ""
        if self.multi_index and self.index:
            result += f"MultiIndex with levels: {self.index.names}\\n"
            result += "  " + "  ".join(f"{col:>12}" for col in self.columns) + "\\n"
            for i, idx in enumerate(self.index.levels[:min(10, len(self.index.levels))]):
                row = f"{str(idx):>20}  "
                for col in self.columns:
                    val = str(self.data[col][i])[:12]
                    row += f"{val:>12}  "
                result += row + "\\n"
        else:
            result += "  " + "  ".join(f"{col:>12}" for col in self.columns) + "\\n"
            n_rows = len(list(self.data.values())[0])
            for i in range(min(n_rows, 10)):
                row = f"{i}  "
                for col in self.columns:
                    val = str(self.data[col][i])[:12]
                    row += f"{val:>12}  "
                result += row + "\\n"
        return result

# Demo: MultiIndex DataFrames
print("Pandas MultiIndex DataFrames - Simulation")
print("=" * 70)

# Hierarchical data
data = {
    'Year': [2023, 2023, 2023, 2024, 2024, 2024],
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q1', 'Q2', 'Q3'],
    'Region': ['North', 'South', 'East', 'North', 'South', 'East'],
    'Sales': [100000, 120000, 150000, 110000, 130000, 160000],
    'Profit': [20000, 25000, 35000, 22000, 27000, 38000]
}

df = DataFrameSimulation(data)

print("\\n1. Original flat data (6 rows):")
print(df)

print("\\n" + "=" * 70)
print("2. Create MultiIndex with set_index(['Year', 'Quarter']):")
print("=" * 70)
df_multi = df.set_index(['Year', 'Quarter'])
print(df_multi)
print(f"\\nMultiIndex levels: {df_multi.index.names}")

print("\\n" + "=" * 70)
print("3. Stack - Convert wide to long format:")
print("=" * 70)
df_stacked = df_multi.stack()
print(df_stacked)

print("\\n" + "=" * 70)
print("4. Swap index levels (Year and Quarter reversed):")
print("=" * 70)
swapped = df_multi.index.swaplevel(0, 1)
print("   Index order: (Year, Quarter) -> (Quarter, Year)")
for i, level in enumerate(swapped.levels[:4]):
    print(f"   Row {i}: {level}")

print("\\n" + "=" * 70)
print("Real pandas MultiIndex operations:")
print("  df.set_index(['col1', 'col2', 'col3'])  # Create MultiIndex")
print("  df.stack()  # Convert columns to rows")
print("  df.unstack()  # Convert rows to columns")
print("  df.swaplevel(0, 1)  # Reorder index levels")
print("  df.sort_index(level=0)  # Sort by specific level")
print("  df.xs('value', level='name')  # Cross-section selection")""",

    971: """# In production: import pandas as pd
# df['result'] = df['a'] * df['b']  # Vectorized
# for i, row in df.iterrows(): pass  # SLOW - avoid!
# This simulation demonstrates pandas performance optimization

class DataFrameSimulation:
    \"\"\"Simulates pandas DataFrame with performance patterns\"\"\"
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())
        self.n_rows = len(list(data.values())[0])

    def __getitem__(self, key):
        \"\"\"Column access\"\"\"
        return self.data[key]

    def __setitem__(self, key, values):
        \"\"\"Column assignment\"\"\"
        self.data[key] = values

    def apply_vectorized(self, func, col1, col2, result_col):
        \"\"\"Vectorized operation - FAST\"\"\"
        result = []
        for i in range(self.n_rows):
            result.append(func(self.data[col1][i], self.data[col2][i]))
        self[result_col] = result
        self.columns.append(result_col)

    def apply_loop(self, func, col1, col2, result_col):
        \"\"\"Loop-based operation - SLOW (for comparison)\"\"\"
        # Simulates slow iterrows() approach
        result = []
        for i in range(self.n_rows):
            # This is slower because:
            # 1. Creates Series objects for each row
            # 2. Python loop (not compiled)
            # 3. Type checking at each iteration
            row = {'col1_val': self.data[col1][i], 'col2_val': self.data[col2][i]}
            result.append(func(row['col1_val'], row['col2_val']))
        self[result_col] = result
        self.columns.append(result_col)

    def copy(self):
        \"\"\"Create a copy of DataFrame\"\"\"
        new_data = {col: list(vals) for col, vals in self.data.items()}
        return DataFrameSimulation(new_data)

    def __repr__(self):
        result = "  " + "  ".join(f"{col:>12}" for col in self.columns) + "\\n"
        for i in range(min(self.n_rows, 10)):
            row = f"{i}  "
            for col in self.columns:
                val = str(self.data[col][i])[:12]
                row += f"{val:>12}  "
            result += row + "\\n"
        if self.n_rows > 10:
            result += f"... {self.n_rows - 10} more rows\\n"
        return result

# Demo: Performance Optimization
print("Pandas Performance Optimization - Simulation")
print("=" * 70)

# Create sample data
n_rows = 5
data = {
    'price': [100, 200, 150, 300, 250],
    'quantity': [2, 3, 1, 5, 4],
    'discount': [0.1, 0.05, 0.0, 0.2, 0.15]
}

df = DataFrameSimulation(data)

print("\\n1. Original DataFrame:")
print(df)

print("\\n" + "=" * 70)
print("VECTORIZED OPERATION (FAST) - Recommended")
print("=" * 70)
print("\\nCode: df['revenue'] = df['price'] * df['quantity']")

import time
df_v = df.copy()

# Simulate timing
print("\\nExecuting vectorized multiplication (1000 times):")
start = time.time()
for _ in range(1000):
    result = [df_v['price'][i] * df_v['quantity'][i] for i in range(len(df_v.data['price']))]
elapsed_v = time.time() - start

df_v['revenue'] = result
print(f"Time: {elapsed_v*1000:.2f}ms")
print(f"\\nResult DataFrame:")
print(df_v)

print("\\n" + "=" * 70)
print("LOOP-BASED OPERATION (SLOW) - Avoid this!")
print("=" * 70)
print("\\nCode: for i, row in df.iterrows():")
print("          row['revenue'] = row['price'] * row['quantity']")

df_l = df.copy()

# Simulate slow loop timing
print("\\nExecuting loop-based multiplication (1000 times):")
start = time.time()
for _ in range(1000):
    result = []
    for i in range(df_l.n_rows):
        row = {'price': df_l['price'][i], 'quantity': df_l['quantity'][i]}
        result.append(row['price'] * row['quantity'])
elapsed_l = time.time() - start

df_l['revenue'] = result
print(f"Time: {elapsed_l*1000:.2f}ms")

print("\\n" + "=" * 70)
print("Performance Comparison:")
print("=" * 70)
print(f"Vectorized: {elapsed_v*1000:.2f}ms")
print(f"Loop-based: {elapsed_l*1000:.2f}ms")
print(f"Speedup: {elapsed_l/elapsed_v:.1f}x faster with vectorization")

print("\\n" + "=" * 70)
print("Optimization Best Practices:")
print("=" * 70)
print("1. Use vectorized operations: df['col'] = df['a'] * df['b']")
print("2. Avoid iterrows(): Slow, creates Series for each row")
print("3. Use apply() with axis=1 if needed, but still slower")
print("4. Use numpy operations on values: df.values * 2")
print("5. Avoid modifying DataFrame in loops")
print("6. Use copy() when needed: df_new = df.copy()")
print("7. Use inplace=True to save memory: df.drop(..., inplace=True)")""",

    972: """# In production: import pandas as pd
# df['category'] = df['category'].astype('category')  # Save memory
# df['age'] = df['age'].astype('int8')  # Downcast from int64
# This simulation demonstrates memory reduction techniques

class SeriesSimulation:
    \"\"\"Simulates pandas Series with dtype support\"\"\"
    def __init__(self, data, dtype='object'):
        self.data = data
        self.dtype = dtype
        self.length = len(data)

    def astype(self, new_dtype):
        \"\"\"Convert to different dtype\"\"\"
        converted = []
        for val in self.data:
            if new_dtype == 'category':
                converted.append(val)  # Keep as-is, simulate categorical encoding
            elif new_dtype == 'int8':
                converted.append(int(val))
            elif new_dtype == 'int16':
                converted.append(int(val))
            elif new_dtype == 'int32':
                converted.append(int(val))
            elif new_dtype == 'float32':
                converted.append(float(val))
            else:
                converted.append(val)
        return SeriesSimulation(converted, dtype=new_dtype)

    def memory_usage(self):
        \"\"\"Estimate memory usage\"\"\"
        if self.dtype == 'object':
            # Objects use ~28 bytes per element
            return self.length * 28
        elif self.dtype == 'category':
            # Categories use ~5-10 bytes per element
            return self.length * 5
        elif self.dtype == 'int64':
            return self.length * 8
        elif self.dtype == 'int32':
            return self.length * 4
        elif self.dtype == 'int16':
            return self.length * 2
        elif self.dtype == 'int8':
            return self.length * 1
        elif self.dtype == 'float64':
            return self.length * 8
        elif self.dtype == 'float32':
            return self.length * 4
        return self.length * 8

class DataFrameSimulation:
    \"\"\"Simulates pandas DataFrame with memory management\"\"\"
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())
        self.series = {col: SeriesSimulation(data[col], 'object') for col in self.columns}

    def astype_col(self, col, dtype):
        \"\"\"Convert column dtype\"\"\"
        self.series[col] = self.series[col].astype(dtype)

    def memory_usage(self):
        \"\"\"Calculate total memory usage\"\"\"
        return {col: self.series[col].memory_usage() for col in self.columns}

    def __repr__(self):
        result = "  " + "  ".join(f"{col:>12}" for col in self.columns) + "\\n"
        n_rows = len(list(self.data.values())[0])
        for i in range(min(n_rows, 10)):
            row = f"{i}  "
            for col in self.columns:
                val = str(self.data[col][i])[:12]
                row += f"{val:>12}  "
            result += row + "\\n"
        return result

# Demo: Memory Reduction
print("Pandas Memory Reduction - Simulation")
print("=" * 70)

# Create sample data
data = {
    'product_type': ['Electronics', 'Clothing', 'Electronics', 'Food', 'Clothing', 'Electronics'],
    'age': [25, 35, 45, 30, 28, 55],
    'price': [199.99, 49.99, 299.99, 12.99, 79.99, 149.99],
    'quantity': [5, 10, 2, 100, 15, 8]
}

df = DataFrameSimulation(data)

print("\\n1. Original DataFrame (object dtype for strings):")
print(df)

print("\\n" + "=" * 70)
print("Memory usage analysis (bytes):")
print("=" * 70)

mem_before = df.memory_usage()
print("\\nBefore optimization:")
total_before = 0
for col in df.columns:
    usage = mem_before[col]
    total_before += usage
    print(f"  {col:>15}: {usage:>6,} bytes")
print(f"  {'Total':>15}: {total_before:>6,} bytes")

print("\\n" + "=" * 70)
print("Memory optimization techniques:")
print("=" * 70)

# Technique 1: Category dtype for strings
print("\\n1. Use category dtype for strings (save 80% memory):")
print("   df['product_type'] = df['product_type'].astype('category')")
df.astype_col('product_type', 'category')

# Technique 2: Downcast integers
print("\\n2. Downcast integers to smallest type:")
print("   df['age'] = df['age'].astype('int8')  # -128 to 127")
print("   df['quantity'] = df['quantity'].astype('int8')")
df.astype_col('age', 'int8')
df.astype_col('quantity', 'int8')

# Technique 3: Downcast floats
print("\\n3. Use float32 instead of float64:")
print("   df['price'] = df['price'].astype('float32')")
df.astype_col('price', 'float32')

print("\\n" + "=" * 70)
print("Memory usage after optimization:")
print("=" * 70)

mem_after = df.memory_usage()
total_after = 0
for col in df.columns:
    usage = mem_after[col]
    total_after += usage
    print(f"  {col:>15}: {usage:>6,} bytes")
print(f"  {'Total':>15}: {total_after:>6,} bytes")

print("\\n" + "=" * 70)
print(f"Memory saved: {total_before - total_after:,} bytes ({(1 - total_after/total_before)*100:.1f}%)")

print("\\n" + "=" * 70)
print("Dtype reference (memory per element):")
print("=" * 70)
print("  object:     28 bytes (strings, mixed types)")
print("  category:   5 bytes (repeating values)")
print("  int64:      8 bytes (large integers)")
print("  int32:      4 bytes (medium integers)")
print("  int16:      2 bytes (small integers: -32K to 32K)")
print("  int8:       1 byte (tiny integers: -128 to 127)")
print("  float64:    8 bytes (double precision)")
print("  float32:    4 bytes (single precision)")
print("  bool:       1 byte (True/False)")""",

    973: """# In production: import pandas as pd
# for chunk in pd.read_csv('large_file.csv', chunksize=10000):
#     process(chunk)
# This simulation demonstrates chunking large datasets

class CSVReaderSimulation:
    \"\"\"Simulates pandas read_csv with chunksize\"\"\"
    def __init__(self, data, chunksize=None):
        self.all_data = data
        self.chunksize = chunksize
        self.columns = list(data.keys())
        self.n_rows = len(list(data.values())[0])

    def read_chunks(self):
        \"\"\"Yield chunks of data\"\"\"
        for start in range(0, self.n_rows, self.chunksize):
            end = min(start + self.chunksize, self.n_rows)
            chunk_data = {}
            for col in self.columns:
                chunk_data[col] = self.all_data[col][start:end]
            yield DataFrameSimulation(chunk_data, start, end)

class DataFrameSimulation:
    \"\"\"Simulates pandas DataFrame from CSV chunk\"\"\"
    def __init__(self, data, start_idx=0, end_idx=None):
        self.data = data
        self.columns = list(data.keys())
        self.n_rows = len(list(data.values())[0])
        self.start_idx = start_idx
        self.end_idx = end_idx or self.n_rows

    def sum(self):
        \"\"\"Sum numeric columns\"\"\"
        result = {}
        for col in self.columns:
            if all(isinstance(v, (int, float)) for v in self.data[col]):
                result[col] = sum(self.data[col])
        return result

    def __repr__(self):
        result = f"DataFrame chunk [{self.start_idx}:{self.end_idx}] shape: ({self.n_rows}, {len(self.columns)})\\n"
        result += "  " + "  ".join(f"{col:>12}" for col in self.columns) + "\\n"
        for i in range(min(self.n_rows, 5)):
            row = f"{i}  "
            for col in self.columns:
                val = str(self.data[col][i])[:12]
                row += f"{val:>12}  "
            result += row + "\\n"
        if self.n_rows > 5:
            result += f"... {self.n_rows - 5} more rows\\n"
        return result

# Demo: Chunking Large Datasets
print("Pandas Chunking Large Datasets - Simulation")
print("=" * 70)

# Simulate large dataset (100,000 rows)
print("\\nSimulating large CSV file with 100,000 rows...")
n_rows = 100000
data = {
    'transaction_id': list(range(1, n_rows + 1)),
    'customer_id': [i % 1000 for i in range(n_rows)],
    'amount': [(i % 100) * 10 + 5.5 for i in range(n_rows)],
    'date': ['2024-01-' + f'{(i % 30) + 1:02d}' for i in range(n_rows)]
}

print("\\n" + "=" * 70)
print("Method 1: Read entire file (Memory intensive)")
print("=" * 70)
print("\\nCode: df = pd.read_csv('large_file.csv')")
print(f"Memory usage: {n_rows * 4 * 50 / 1024 / 1024:.1f} MB (approximation)")

print("\\n" + "=" * 70)
print("Method 2: Read in chunks (Memory efficient) - Recommended")
print("=" * 70)
print("\\nCode: for chunk in pd.read_csv('large_file.csv', chunksize=10000):")
print("          process(chunk)")

reader = CSVReaderSimulation(data, chunksize=10000)

print(f"\\nReading in chunks of 10,000 rows:")
print(f"Total rows: {n_rows:,}")
print(f"Chunk size: 10,000")
print(f"Number of chunks: {(n_rows + 9999) // 10000}")

total_amount = 0
chunk_count = 0

for chunk in reader.read_chunks():
    chunk_count += 1
    chunk_sum = chunk.sum()
    total_amount += chunk_sum['amount']

    print(f"\\nChunk {chunk_count}:")
    print(chunk)
    print(f"Sum of amount: ${chunk_sum['amount']:,.2f}")

print("\\n" + "=" * 70)
print("Processing complete:")
print("=" * 70)
print(f"Total chunks processed: {chunk_count}")
print(f"Total transactions: {n_rows:,}")
print(f"Total revenue: ${total_amount:,.2f}")

print("\\n" + "=" * 70)
print("Chunking strategies:")
print("=" * 70)
print("1. Fixed chunk size: chunksize=10000")
print("   Pro: Predictable memory usage")
print("   Con: Last chunk may be smaller")
print()
print("2. Iterator with for loop:")
print("   for chunk in pd.read_csv(...):")
print("       result = process(chunk)")
print()
print("3. Accumulate results:")
print("   results = []")
print("   for chunk in pd.read_csv(...):")
print("       results.append(chunk.groupby(...).sum())")
print("   final = pd.concat(results)")
print()
print("Memory usage: 10K rows * 50 bytes ≈ 500 KB per chunk")
print("vs 100K rows * 50 bytes ≈ 5 MB all at once")""",

    974: """# In production: import pandas as pd
# df = pd.read_sql('SELECT * FROM table', con)
# df.to_sql('table', con, if_exists='append')
# This simulation demonstrates SQL integration with SQLite patterns

class SQLiteSimulation:
    \"\"\"Simulates SQLite database operations\"\"\"
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, schema):
        \"\"\"CREATE TABLE\"\"\"
        self.tables[table_name] = {'schema': schema, 'rows': []}

    def insert(self, table_name, columns, values):
        \"\"\"INSERT INTO values\"\"\"
        if table_name in self.tables:
            row = dict(zip(columns, values))
            self.tables[table_name]['rows'].append(row)

    def select(self, table_name, columns=None):
        \"\"\"SELECT * FROM table\"\"\"
        if table_name in self.tables:
            rows = self.tables[table_name]['rows']
            if columns is None:
                return rows
            return [{col: row[col] for col in columns} for row in rows]

    def query(self, table_name, condition=None):
        \"\"\"SELECT with WHERE clause\"\"\"
        rows = self.select(table_name)
        if condition:
            # Simple condition matching
            return [r for r in rows if condition(r)]
        return rows

class DataFrameSimulation:
    \"\"\"Simulates pandas DataFrame with SQL methods\"\"\"
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())
        self.n_rows = len(list(data.values())[0])

    def to_sql(self, table_name, connection, if_exists='fail'):
        \"\"\"Write DataFrame to SQL table\"\"\"
        # Simulate creating table and inserting data
        if if_exists == 'replace':
            # DROP TABLE IF EXISTS
            if table_name in connection.tables:
                del connection.tables[table_name]

        # CREATE TABLE
        schema = {col: 'TEXT' for col in self.columns}
        connection.create_table(table_name, schema)

        # INSERT rows
        for i in range(self.n_rows):
            values = [self.data[col][i] for col in self.columns]
            connection.insert(table_name, self.columns, values)

    def __repr__(self):
        result = "  " + "  ".join(f"{col:>15}" for col in self.columns) + "\\n"
        for i in range(min(self.n_rows, 10)):
            row = f"{i}  "
            for col in self.columns:
                val = str(self.data[col][i])[:15]
                row += f"{val:>15}  "
            result += row + "\\n"
        return result

# Demo: SQL Integration
print("Pandas SQL Integration - Simulation")
print("=" * 70)

# Simulate SQLite connection
db = SQLiteSimulation()

# Create sample DataFrame
sales_data = {
    'order_id': [1001, 1002, 1003, 1004, 1005],
    'customer': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'amount': [150.00, 200.00, 325.50, 89.99, 450.00],
    'status': ['shipped', 'pending', 'shipped', 'pending', 'shipped']
}

df = DataFrameSimulation(sales_data)

print("\\n1. Original DataFrame:")
print(df)

print("\\n" + "=" * 70)
print("2. Write to SQL (simulates pd.to_sql())")
print("=" * 70)
print("\\nCode: df.to_sql('orders', connection, if_exists='replace')")
print("\\nSQL equivalent:")
print("  CREATE TABLE orders (")
print("    order_id INTEGER,")
print("    customer TEXT,")
print("    amount REAL,")
print("    status TEXT")
print("  );")

df.to_sql('orders', db, if_exists='replace')
print("\\nTable 'orders' created and 5 rows inserted")

print("\\n" + "=" * 70)
print("3. Read from SQL (simulates pd.read_sql())")
print("=" * 70)

# SELECT all
print("\\nQuery 1: SELECT * FROM orders")
all_rows = db.select('orders')
print(f"Result: {len(all_rows)} rows retrieved")
for i, row in enumerate(all_rows[:3]):
    print(f"  {row}")

# SELECT specific columns
print("\\nQuery 2: SELECT customer, amount FROM orders")
selected = db.select('orders', columns=['customer', 'amount'])
print(f"Result: {len(selected)} rows")
for row in selected[:3]:
    print(f"  {row}")

# SELECT with WHERE
print("\\nQuery 3: SELECT * FROM orders WHERE amount > 200")
filtered = db.query('orders', condition=lambda r: r['amount'] > 200)
print(f"Result: {len(filtered)} rows")
for row in filtered:
    print(f"  {row}")

# Append more data
print("\\n" + "=" * 70)
print("4. Append to SQL table (if_exists='append')")
print("=" * 70)

new_data = {
    'order_id': [1006, 1007],
    'customer': ['Frank', 'Grace'],
    'amount': [175.50, 220.00],
    'status': ['pending', 'shipped']
}

df_new = DataFrameSimulation(new_data)
print("\\nCode: df_new.to_sql('orders', connection, if_exists='append')")
df_new.to_sql('orders', db, if_exists='fail')  # Append to existing
all_rows = db.select('orders')
print(f"Total rows in table: {len(all_rows)}")

print("\\n" + "=" * 70)
print("Real pandas SQL operations:")
print("=" * 70)
print("import pandas as pd")
print("import sqlite3")
print()
print("# Read from SQL")
print("con = sqlite3.connect('database.db')")
print("df = pd.read_sql('SELECT * FROM table', con)")
print()
print("# Write to SQL")
print("df.to_sql('new_table', con, if_exists='replace')")
print("  if_exists='replace': Drop table if exists")
print("  if_exists='append': Add rows to existing table")
print("  if_exists='fail': Raise error if exists")
print()
print("# Query with WHERE clause")
print("df = pd.read_sql('SELECT * FROM table WHERE col > 100', con)")
print()
print("# Close connection")
print("con.close()")""",

    975: """# In production: import pandas as pd
# df['rolling_avg'] = df['price'].rolling(window=30).mean()
# df['daily_change'] = df['price'].diff()
# This simulation demonstrates advanced time series operations

class RollingSimulation:
    \"\"\"Simulates pandas rolling window operations\"\"\"
    def __init__(self, values, window):
        self.values = values
        self.window = window

    def mean(self):
        \"\"\"Calculate rolling mean\"\"\"
        result = [None] * (self.window - 1)
        for i in range(self.window - 1, len(self.values)):
            window_data = self.values[i - self.window + 1:i + 1]
            result.append(sum(window_data) / len(window_data))
        return result

    def sum(self):
        \"\"\"Calculate rolling sum\"\"\"
        result = [None] * (self.window - 1)
        for i in range(self.window - 1, len(self.values)):
            window_data = self.values[i - self.window + 1:i + 1]
            result.append(sum(window_data))
        return result

    def std(self):
        \"\"\"Calculate rolling standard deviation\"\"\"
        result = [None] * (self.window - 1)
        for i in range(self.window - 1, len(self.values)):
            window_data = self.values[i - self.window + 1:i + 1]
            mean = sum(window_data) / len(window_data)
            variance = sum((x - mean) ** 2 for x in window_data) / len(window_data)
            result.append(variance ** 0.5)
        return result

class SeriesSimulation:
    \"\"\"Simulates pandas Series with time series methods\"\"\"
    def __init__(self, values):
        self.values = values
        self.length = len(values)

    def rolling(self, window):
        \"\"\"Create rolling window\"\"\"
        return RollingSimulation(self.values, window)

    def shift(self, periods=1):
        \"\"\"Shift values by periods\"\"\"
        if periods > 0:
            return [None] * periods + self.values[:-periods]
        elif periods < 0:
            return self.values[-periods:] + [None] * (-periods)
        return self.values[:]

    def diff(self, periods=1):
        \"\"\"Calculate differences (current - previous)\"\"\"
        result = [None] * periods
        for i in range(periods, self.length):
            result.append(self.values[i] - self.values[i - periods])
        return result

    def pct_change(self, periods=1):
        \"\"\"Calculate percent change\"\"\"
        result = [None] * periods
        for i in range(periods, self.length):
            prev = self.values[i - periods]
            if prev != 0:
                result.append((self.values[i] - prev) / prev)
            else:
                result.append(None)
        return result

# Demo: Advanced Time Series
print("Pandas Advanced Time Series - Simulation")
print("=" * 70)

# Time series data: daily stock prices
prices = [100, 102, 101, 105, 107, 106, 108, 110, 109, 112, 115, 113, 116, 118, 120]

series = SeriesSimulation(prices)

print("\\nStock Prices (15 days):")
for i, price in enumerate(prices):
    print(f"  Day {i+1:2d}: ${price}")

print("\\n" + "=" * 70)
print("1. Rolling Mean (30-day moving average)")
print("=" * 70)

rolling_mean = series.rolling(window=3).mean()
print("\\nCode: df['rolling_mean'] = df['price'].rolling(window=3).mean()")
print("\\nRolling 3-day average:")
for i, (price, rm) in enumerate(zip(prices, rolling_mean)):
    if rm is not None:
        print(f"  Day {i+1:2d}: Price=${price:3d}, Rolling Mean=${rm:6.2f}")
    else:
        print(f"  Day {i+1:2d}: Price=${price:3d}, Rolling Mean=NaN")

print("\\n" + "=" * 70)
print("2. Shift (Previous value)")
print("=" * 70)

prev_prices = series.shift(periods=1)
print("\\nCode: df['previous'] = df['price'].shift(1)")
print("\\nPrevious day prices:")
for i, (price, prev) in enumerate(zip(prices, prev_prices)):
    if prev is not None:
        print(f"  Day {i+1:2d}: Today=${price:3d}, Previous=${prev:3d}")
    else:
        print(f"  Day {i+1:2d}: Today=${price:3d}, Previous=NaN")

print("\\n" + "=" * 70)
print("3. Diff (Daily change)")
print("=" * 70)

price_change = series.diff(periods=1)
print("\\nCode: df['daily_change'] = df['price'].diff(1)")
print("\\nDaily price changes:")
for i, (price, change) in enumerate(zip(prices, price_change)):
    if change is not None:
        print(f"  Day {i+1:2d}: Price=${price:3d}, Change=${change:+3.0f}")
    else:
        print(f"  Day {i+1:2d}: Price=${price:3d}, Change=NaN")

print("\\n" + "=" * 70)
print("4. Pct_Change (Percent change)")
print("=" * 70)

pct_change = series.pct_change(periods=1)
print("\\nCode: df['pct_change'] = df['price'].pct_change()")
print("\\nDaily percent changes:")
for i, (price, pct) in enumerate(zip(prices, pct_change)):
    if pct is not None:
        print(f"  Day {i+1:2d}: Price=${price:3d}, Change={pct:+5.2%}")
    else:
        print(f"  Day {i+1:2d}: Price=${price:3d}, Change=NaN")

print("\\n" + "=" * 70)
print("Real pandas time series operations:")
print("=" * 70)
print("df['rolling_30'] = df['price'].rolling(30).mean()  # 30-day average")
print("df['rolling_7'] = df['price'].rolling(7).sum()   # 7-day sum")
print("df['rolling_std'] = df['price'].rolling(30).std() # Rolling std dev")
print("df['previous'] = df['price'].shift(1)  # Previous value")
print("df['change'] = df['price'].diff()  # Daily change")
print("df['pct_change'] = df['price'].pct_change()  # % change")
print("df['lag_7'] = df['price'].shift(7)  # 7-day lag")""",

    976: """# In production: import pandas as pd
# df['ma20'] = df['close'].rolling(window=20).mean()
# df['ma50'] = df['close'].rolling(window=50).mean()
# This simulation demonstrates rolling window operations

class RollingWindowSimulation:
    \"\"\"Simulates pandas rolling window\"\"\"
    def __init__(self, values, window, min_periods=None):
        self.values = values
        self.window = window
        self.min_periods = min_periods or window

    def mean(self):
        \"\"\"Rolling mean\"\"\"
        result = []
        for i in range(len(self.values)):
            start = max(0, i - self.window + 1)
            if i - start + 1 >= self.min_periods:
                window_data = self.values[start:i + 1]
                result.append(sum(window_data) / len(window_data))
            else:
                result.append(None)
        return result

    def sum(self):
        \"\"\"Rolling sum\"\"\"
        result = []
        for i in range(len(self.values)):
            start = max(0, i - self.window + 1)
            if i - start + 1 >= self.min_periods:
                window_data = self.values[start:i + 1]
                result.append(sum(window_data))
            else:
                result.append(None)
        return result

    def min(self):
        \"\"\"Rolling minimum\"\"\"
        result = []
        for i in range(len(self.values)):
            start = max(0, i - self.window + 1)
            if i - start + 1 >= self.min_periods:
                window_data = self.values[start:i + 1]
                result.append(min(window_data))
            else:
                result.append(None)
        return result

    def max(self):
        \"\"\"Rolling maximum\"\"\"
        result = []
        for i in range(len(self.values)):
            start = max(0, i - self.window + 1)
            if i - start + 1 >= self.min_periods:
                window_data = self.values[start:i + 1]
                result.append(max(window_data))
            else:
                result.append(None)
        return result

class SeriesSimulation:
    \"\"\"Simulates pandas Series\"\"\"
    def __init__(self, values):
        self.values = values

    def rolling(self, window, min_periods=None):
        \"\"\"Create rolling window\"\"\"
        return RollingWindowSimulation(self.values, window, min_periods)

class DataFrameSimulation:
    \"\"\"Simulates pandas DataFrame\"\"\"
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())

    def __getitem__(self, col):
        \"\"\"Get column as Series\"\"\"
        return SeriesSimulation(self.data[col])

    def __setitem__(self, col, values):
        \"\"\"Set column\"\"\"
        self.data[col] = values
        if col not in self.columns:
            self.columns.append(col)

    def __repr__(self):
        n_rows = len(list(self.data.values())[0])
        result = "  " + "  ".join(f"{col:>12}" for col in self.columns) + "\\n"
        for i in range(min(n_rows, 15)):
            row = f"{i:2d}  "
            for col in self.columns:
                val = self.data[col][i]
                if val is None:
                    val_str = 'None'
                elif isinstance(val, float):
                    val_str = f"{val:.2f}"
                else:
                    val_str = str(val)[:12]
                row += f"{val_str:>12}  "
            result += row + "\\n"
        return result

# Demo: Rolling Windows
print("Pandas Rolling Windows - Simulation")
print("=" * 70)

# Stock price data
close_prices = [100, 102, 101, 105, 107, 106, 108, 110, 109, 112, 115, 113, 116, 118, 120]

df = DataFrameSimulation({'close': close_prices})

print("\\nStock Close Prices (15 days):")
for i, price in enumerate(close_prices):
    print(f"  Day {i+1:2d}: ${price}")

print("\\n" + "=" * 70)
print("Rolling Window Calculations")
print("=" * 70)

# 5-day moving average
ma5 = df['close'].rolling(window=5).mean()
df['MA5'] = ma5

print("\\n1. 5-day Moving Average (window=5)")
print("   Code: df['MA5'] = df['close'].rolling(5).mean()")

# 10-day moving average
ma10 = df['close'].rolling(window=10).mean()
df['MA10'] = ma10

print("\\n2. 10-day Moving Average (window=10)")
print("   Code: df['MA10'] = df['close'].rolling(10).mean()")

# Rolling min and max (Bollinger Band concept)
rolling_min = df['close'].rolling(window=5).min()
rolling_max = df['close'].rolling(window=5).max()
df['Min'] = rolling_min
df['Max'] = rolling_max

print("\\n3. 5-day Rolling Min/Max (volatility bounds)")
print("   Code: rolling(5).min() and rolling(5).max()")

print("\\n" + "=" * 70)
print("DataFrame with all rolling calculations:")
print("=" * 70)
print(df)

print("\\n" + "=" * 70)
print("Trading Strategy Example: Moving Average Crossover")
print("=" * 70)
print("\\nStrategy: Buy when MA5 > MA10, Sell when MA5 < MA10")
print("\\nSignals:")
for i in range(len(ma5)):
    ma5_val = ma5[i]
    ma10_val = ma10[i]
    if ma5_val is None or ma10_val is None:
        signal = "Wait (not enough data)"
    elif ma5_val > ma10_val:
        signal = "BUY"
    else:
        signal = "SELL"

    if i >= 9:
        print(f"  Day {i+1:2d}: MA5={ma5_val:6.2f}, MA10={ma10_val:6.2f} -> {signal}")

print("\\n" + "=" * 70)
print("Real pandas rolling operations:")
print("=" * 70)
print("df['MA20'] = df['price'].rolling(window=20).mean()")
print("df['MA50'] = df['price'].rolling(window=50).mean()")
print("df['rolling_sum'] = df['price'].rolling(5).sum()")
print("df['rolling_min'] = df['price'].rolling(20).min()")
print("df['rolling_max'] = df['price'].rolling(20).max()")
print("df['rolling_std'] = df['price'].rolling(20).std()")
print("df['rolling_median'] = df['price'].rolling(20).median()")""",

    977: """# In production: import pandas as pd
# result = df.groupby('category').agg({'sales': 'sum', 'quantity': 'mean'})
# result = df.agg({'col1': sum, 'col2': max})
# This simulation demonstrates custom aggregations

class AggregationSimulation:
    \"\"\"Simulates custom aggregation functions\"\"\"
    @staticmethod
    def sum_func(values):
        return sum(values)

    @staticmethod
    def mean_func(values):
        return sum(values) / len(values) if values else 0

    @staticmethod
    def max_func(values):
        return max(values) if values else None

    @staticmethod
    def min_func(values):
        return min(values) if values else None

    @staticmethod
    def count_func(values):
        return len(values)

    @staticmethod
    def std_func(values):
        if not values or len(values) < 2:
            return None
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return variance ** 0.5

    @staticmethod
    def custom_percentile(values, percentile):
        \"\"\"Custom: Calculate percentile\"\"\"
        sorted_vals = sorted(values)
        idx = int(len(sorted_vals) * percentile / 100)
        return sorted_vals[min(idx, len(sorted_vals) - 1)]

class GroupBySimulation:
    \"\"\"Simulates GroupBy with custom aggregations\"\"\"
    def __init__(self, groups):
        self.groups = groups

    def agg(self, agg_dict):
        \"\"\"Apply multiple aggregations\"\"\"
        result = {}
        agg = AggregationSimulation()

        for group_key, rows in self.groups.items():
            result[group_key] = {}

            for col, func_name in agg_dict.items():
                values = [row[col] for row in rows if col in row]

                if func_name == 'sum':
                    result[group_key][col] = agg.sum_func(values)
                elif func_name == 'mean':
                    result[group_key][col] = agg.mean_func(values)
                elif func_name == 'max':
                    result[group_key][col] = agg.max_func(values)
                elif func_name == 'min':
                    result[group_key][col] = agg.min_func(values)
                elif func_name == 'count':
                    result[group_key][col] = agg.count_func(values)
                elif func_name == 'std':
                    result[group_key][col] = agg.std_func(values)
                elif callable(func_name):
                    # Custom lambda function
                    result[group_key][col] = func_name(values)

        return result

class DataFrameSimulation:
    \"\"\"Simulates DataFrame with groupby\"\"\"
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())

    def groupby(self, column):
        \"\"\"Group by column values\"\"\"
        groups = {}
        col_data = self.data[column]

        for i, key in enumerate(col_data):
            if key not in groups:
                groups[key] = []
            row = {col: self.data[col][i] for col in self.columns}
            groups[key].append(row)

        return GroupBySimulation(groups)

# Demo: Custom Aggregations
print("Pandas Custom Aggregations - Simulation")
print("=" * 70)

# Sales data by region and category
data = {
    'region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East'],
    'category': ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'B'],
    'sales': [100, 150, 120, 200, 180, 160, 250, 220],
    'quantity': [10, 15, 12, 20, 18, 16, 25, 22],
    'profit': [20, 30, 24, 40, 36, 32, 50, 44]
}

df = DataFrameSimulation(data)

print("\\nSales Data (8 transactions):")
print("  Region | Category | Sales | Quantity | Profit")
for i in range(len(data['region'])):
    print(f"  {data['region'][i]:>6} | {data['category'][i]:>8} | {data['sales'][i]:>5} | {data['quantity'][i]:>8} | {data['profit'][i]:>6}")

print("\\n" + "=" * 70)
print("1. Multiple aggregations by group")
print("=" * 70)
print("\\nCode: grouped = df.groupby('region').agg({")
print("    'sales': 'sum',")
print("    'profit': 'mean'")
print("})")

grouped = df.groupby('region')
result = grouped.agg({'sales': 'sum', 'profit': 'mean'})

print("\\nResult: Sales by Region")
print("  Region  | Total Sales | Avg Profit")
for region, vals in sorted(result.items()):
    print(f"  {region:>6} | {vals['sales']:>11.0f} | {vals['profit']:>10.2f}")

print("\\n" + "=" * 70)
print("2. Lambda function aggregation")
print("=" * 70)
print("\\nCode: df.groupby('category').agg({")
print("    'sales': lambda x: sum(x) / len(x),  # Custom mean")
print("    'quantity': lambda x: max(x) - min(x)  # Range")
print("})")

grouped2 = df.groupby('category')
custom_agg = {
    'sales': lambda x: sum(x) / len(x),  # Custom mean
    'quantity': lambda x: max(x) - min(x)  # Range (max - min)
}

# Manual custom aggregation
result2 = {}
for cat, rows in grouped2.groups.items():
    result2[cat] = {}
    vals_sales = [r['sales'] for r in rows]
    vals_qty = [r['quantity'] for r in rows]
    result2[cat]['sales'] = sum(vals_sales) / len(vals_sales)
    result2[cat]['quantity'] = max(vals_qty) - min(vals_qty)

print("\\nResult: Aggregations by Category")
print("  Category | Sales (mean) | Qty (range)")
for cat, vals in sorted(result2.items()):
    print(f"  {cat:>8} | {vals['sales']:>12.2f} | {vals['quantity']:>10.0f}")

print("\\n" + "=" * 70)
print("3. Multiple columns aggregation")
print("=" * 70)
print("\\nCode: df.groupby('region').agg({")
print("    'sales': ['sum', 'mean', 'max'],")
print("    'profit': ['sum', 'min']")
print("})")

grouped3 = df.groupby('region')
multi_agg = {
    'sales': 'sum',
    'profit': 'mean'
}
result3 = grouped3.agg(multi_agg)

print("\\nResult:")
for region, vals in sorted(result3.items()):
    print(f"\\n{region}:")
    for col, val in vals.items():
        print(f"  {col}: {val:.2f}")

print("\\n" + "=" * 70)
print("Real pandas aggregation methods:")
print("=" * 70)
print("df.groupby('col').agg('sum')  # Single function")
print("df.groupby('col').agg({'col1': 'sum', 'col2': 'mean'})")
print("df.groupby('col').agg(lambda x: x.sum())  # Lambda")
print("df.agg({'col1': 'sum', 'col2': lambda x: x.max() - x.min()})")
print("df.groupby('col').agg([('sum', 'sum'), ('count', 'count')])")
print("\\nCommon functions: 'sum', 'mean', 'median', 'std', 'min', 'max', 'count'")""",

    978: """# In production: Data Cleaning Project combining multiple techniques
# This simulation demonstrates a comprehensive data cleaning workflow

class DataFrameSimulation:
    \"\"\"Simulates pandas DataFrame\"\"\"
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())
        self.n_rows = len(list(data.values())[0])

    def dropna(self):
        \"\"\"Remove rows with NaN\"\"\"
        new_data = {col: [] for col in self.columns}
        for i in range(self.n_rows):
            if not any(self.data[col][i] is None for col in self.columns):
                for col in self.columns:
                    new_data[col].append(self.data[col][i])
        return DataFrameSimulation(new_data)

    def fillna(self, value):
        \"\"\"Fill NaN values\"\"\"
        new_data = {}
        for col in self.columns:
            new_data[col] = [v if v is not None else value for v in self.data[col]]
        return DataFrameSimulation(new_data)

    def drop_duplicates(self, subset=None):
        \"\"\"Remove duplicates\"\"\"
        new_data = {col: [] for col in self.columns}
        seen = set()
        cols = subset or self.columns

        for i in range(self.n_rows):
            row_tuple = tuple(self.data[col][i] for col in cols)
            if row_tuple not in seen:
                seen.add(row_tuple)
                for col in self.columns:
                    new_data[col].append(self.data[col][i])
        return DataFrameSimulation(new_data)

    def replace(self, old, new):
        \"\"\"Replace values\"\"\"
        new_data = {}
        for col in self.columns:
            new_data[col] = [new if v == old else v for v in self.data[col]]
        return DataFrameSimulation(new_data)

    def astype(self, col, dtype):
        \"\"\"Convert column type\"\"\"
        if dtype == 'int':
            self.data[col] = [int(v) if v is not None else 0 for v in self.data[col]]
        elif dtype == 'float':
            self.data[col] = [float(v) if v is not None else 0.0 for v in self.data[col]]
        return self

    def groupby(self, col):
        \"\"\"Group by column\"\"\"
        groups = {}
        for i, key in enumerate(self.data[col]):
            if key not in groups:
                groups[key] = []
            groups[key].append({c: self.data[c][i] for c in self.columns})
        return GroupBySimulation(groups)

    def __repr__(self):
        result = "  " + "  ".join(f"{col:>12}" for col in self.columns) + "\\n"
        for i in range(min(self.n_rows, 10)):
            row = f"{i:2d}  "
            for col in self.columns:
                val = str(self.data[col][i])[:12]
                row += f"{val:>12}  "
            result += row + "\\n"
        if self.n_rows > 10:
            result += f"... {self.n_rows - 10} more rows\\n"
        return result

class GroupBySimulation:
    \"\"\"GroupBy simulation\"\"\"
    def __init__(self, groups):
        self.groups = groups

    def sum(self):
        result = {}
        for key, rows in self.groups.items():
            result[key] = {}
            if not rows:
                continue
            for col in rows[0]:
                try:
                    vals = [r[col] for r in rows if isinstance(r[col], (int, float))]
                    result[key][col] = sum(vals)
                except:
                    pass
        return result

# Demo: Comprehensive Data Cleaning Project
print("Pandas Data Cleaning Project - Simulation")
print("=" * 70)

# Messy customer data with multiple issues
raw_data = {
    'customer_id': [1, 2, 3, 2, 5, 6, 7, 7, None, 10, 11, 12],
    'name': ['Alice', 'Bob', 'Charlie', 'Bob', 'Eve', 'Frank', 'Grace', 'Grace', 'Henry', 'Iris', 'Jack', None],
    'email': ['alice@ex.com', 'bob@ex.com', None, 'bob@ex.com', 'eve@ex.com', 'frank@ex.com', 'grace@ex.com', 'grace@ex.com', 'henry@ex.com', 'iris@ex.com', None, None],
    'signup_date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-02', '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-07', '2024-01-09', None, '2024-01-11', '2024-01-12'],
    'purchase_total': [150.50, 200.00, None, 200.00, 350.75, 125.00, 275.50, 275.50, 100.00, 450.00, None, 175.00],
    'status': ['active', 'active', 'inactive', 'active', 'premium', 'active', 'premium', 'premium', 'active', None, 'inactive', 'active']
}

df_raw = DataFrameSimulation(raw_data)

print("\\n1. RAW DATA (12 rows with multiple quality issues):")
print(df_raw)

print("\\nData Quality Issues Identified:")
print("  - Duplicate rows (customer_id 2, 7)")
print("  - Missing values (None) in multiple columns")
print("  - Inconsistent data types")
print("  - Missing email addresses")

print("\\n" + "=" * 70)
print("2. CLEANING STEP 1: Remove rows with critical missing data")
print("=" * 70)
print("\\nCode: df = df.dropna()  # Remove None values")

df_clean = df_raw.dropna()
print(f"\\nRows after dropna(): {df_clean.n_rows} (removed {df_raw.n_rows - df_clean.n_rows})")
print(df_clean)

print("\\n" + "=" * 70)
print("3. CLEANING STEP 2: Remove duplicate rows")
print("=" * 70)
print("\\nCode: df = df.drop_duplicates(subset=['customer_id'])")

df_unique = df_clean.drop_duplicates(subset=['customer_id'])
print(f"\\nRows after drop_duplicates(): {df_unique.n_rows} (removed {df_clean.n_rows - df_unique.n_rows})")
print(df_unique)

print("\\n" + "=" * 70)
print("4. CLEANING STEP 3: Convert data types")
print("=" * 70)
print("\\nCode: df['purchase_total'] = df['purchase_total'].astype('float')")

df_typed = df_unique
df_typed.astype('purchase_total', 'float')
print(f"\\nData types converted for numeric columns")

print("\\n" + "=" * 70)
print("5. FINAL CLEAN DATASET:")
print("=" * 70)
print(df_typed)

print("\\n" + "=" * 70)
print("6. DATA ANALYSIS on cleaned data")
print("=" * 70)

grouped = df_typed.groupby('status')
summary = grouped.sum()

print("\\nSummary by Status:")
print("  Status      | Total Purchases | Customer Count")
for status, vals in sorted(summary.items()):
    # Manual count since we don't have it
    count = len([v for v in df_typed.data['status'] if v == status])
    print(f"  {status:>11} | ${vals.get('purchase_total', 0):>14.2f} | {count:>14}")

print("\\n" + "=" * 70)
print("Data Cleaning Project Summary:")
print("=" * 70)
print(f"Starting rows:     {df_raw.n_rows}")
print(f"After dropna():    {df_clean.n_rows}")
print(f"After drop_dups:   {df_unique.n_rows}")
print(f"Final clean rows:  {df_typed.n_rows}")
print(f"Data quality:      {df_typed.n_rows / df_raw.n_rows * 100:.1f}% retained")

print("\\n" + "=" * 70)
print("Complete Data Cleaning Pipeline:")
print("=" * 70)
print("1. Load data: df = pd.read_csv('raw_data.csv')")
print("2. Remove nulls: df = df.dropna()")
print("3. Remove duplicates: df = df.drop_duplicates()")
print("4. Replace values: df = df.replace('old', 'new')")
print("5. Convert types: df['col'] = df['col'].astype('int64')")
print("6. Handle outliers: df = df[df['col'] < threshold]")
print("7. Validate: assert df['col'].isnull().sum() == 0")
print("8. Save: df.to_csv('clean_data.csv', index=False)")
print("\\nResult: Production-ready dataset for analysis and modeling!")"""
}

def update_batch_2(lessons_file):
    """Update batch 2 of pandas lessons"""
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    updated = []
    for lesson in lessons:
        lesson_id = lesson.get('id')
        if lesson_id in PANDAS_BATCH_2:
            before_len = len(lesson.get('fullSolution', ''))
            lesson['fullSolution'] = PANDAS_BATCH_2[lesson_id]
            after_len = len(lesson['fullSolution'])
            updated.append({
                'id': lesson_id,
                'title': lesson.get('title'),
                'before': before_len,
                'after': after_len
            })

    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    return updated

def main():
    lessons_file = r'c:\devbootLLM-app\public\lessons-python.json'

    print("Upgrading pandas lessons - Batch 2 (12 lessons)")
    print("=" * 70)

    updated = update_batch_2(lessons_file)

    print(f"\nUpdated {len(updated)} pandas lessons:\n")
    for item in updated:
        print(f"ID {item['id']}: {item['title']}")
        print(f"  {item['before']:>6,} -> {item['after']:>6,} chars (+{item['after']-item['before']:>5,})")

    total_added = sum(item['after'] - item['before'] for item in updated)
    avg_size = total_added // len(updated) if updated else 0
    print(f"\nTotal characters added: {total_added:,}")
    print(f"Average lesson size: {avg_size:,} chars")
    print("\nBatch 2 complete!")

if __name__ == '__main__':
    sys.exit(main())
