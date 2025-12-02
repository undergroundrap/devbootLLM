"""
Upgrade pandas lessons in batches to avoid token limits
This script upgrades 5 pandas lessons at a time with realistic simulations
"""

import json
import sys

# Batch 1: Basic pandas operations (5 lessons)
PANDAS_BATCH_1 = {
    520: """# In production: import pandas as pd
# df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
# This is a simulation for learning pandas without installing it

class DataFrameSimulation:
    \"\"\"Simulates pandas DataFrame for learning\"\"\"
    def __init__(self, data):
        # Real: pandas uses optimized NumPy arrays and C extensions
        # Simulation: uses Python dicts/lists for educational purposes
        if isinstance(data, dict):
            self.data = data
            self.columns = list(data.keys())
            # Assume all columns have same length
            self.index = list(range(len(list(data.values())[0])))
        else:
            raise ValueError("Data must be a dictionary")

    def __repr__(self):
        \"\"\"Display DataFrame\"\"\"
        result = "  " + "  ".join(f"{col:>8}" for col in self.columns) + "\\n"
        for i in self.index:
            row = f"{i}  "
            for col in self.columns:
                row += f"{self.data[col][i]:>8}  "
            result += row + "\\n"
        return result

    def head(self, n=5):
        \"\"\"Return first n rows\"\"\"
        new_data = {col: self.data[col][:n] for col in self.columns}
        return DataFrameSimulation(new_data)

    def describe(self):
        \"\"\"Statistical summary\"\"\"
        print("\\nStatistical Summary:")
        print("-" * 40)
        for col in self.columns:
            values = self.data[col]
            if all(isinstance(v, (int, float)) for v in values):
                print(f"\\n{col}:")
                print(f"  Count: {len(values)}")
                print(f"  Mean:  {sum(values) / len(values):.2f}")
                print(f"  Min:   {min(values)}")
                print(f"  Max:   {max(values)}")

# Demo: Create and explore DataFrame
print("Pandas DataFrame Basics - Simulation")
print("=" * 50)

# Create DataFrame (simulates pd.DataFrame())
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 75000, 55000]
}

df = DataFrameSimulation(data)

print("\\nDataFrame:")
print(df)

print("\\nFirst 2 rows (df.head(2)):")
print(df.head(2))

print("\\nColumn names:", df.columns)
print("Index:", df.index)

df.describe()

print("\\n" + "=" * 50)
print("Key Concepts:")
print("- DataFrame stores data in columns")
print("- Each column can have different data types")
print("- Rows have numeric index (0, 1, 2, ...)")
print("- head() shows first n rows")
print("- describe() gives statistical summary")""",

    521: """# In production: import pandas as pd
# df = pd.read_csv('data.csv')
# filtered = df[df['Age'] > 25]
# This simulation demonstrates pandas filtering without installation

class DataFrameSimulation:
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())
        self.index = list(range(len(list(data.values())[0])))

    def __getitem__(self, key):
        \"\"\"Bracket operator for filtering\"\"\"
        if isinstance(key, str):
            # Column selection: df['Age']
            return self.data[key]
        elif isinstance(key, list) and all(isinstance(x, bool) for x in key):
            # Boolean indexing: df[mask]
            new_data = {}
            for col in self.columns:
                new_data[col] = [self.data[col][i] for i, keep in enumerate(key) if keep]
            return DataFrameSimulation(new_data)
        elif isinstance(key, list):
            # Multiple columns: df[['col1', 'col2']]
            new_data = {col: self.data[col] for col in key}
            return DataFrameSimulation(new_data)

    def __repr__(self):
        result = "  " + "  ".join(f"{col:>10}" for col in self.columns) + "\\n"
        for i in range(len(self.index)):
            row = f"{i}  "
            for col in self.columns:
                row += f"{str(self.data[col][i]):>10}  "
            result += row + "\\n"
        return result

    def query(self, column, operator, value):
        \"\"\"Filter rows based on condition\"\"\"
        col_data = self.data[column]
        if operator == '>':
            mask = [v > value for v in col_data]
        elif operator == '>=':
            mask = [v >= value for v in col_data]
        elif operator == '<':
            mask = [v < value for v in col_data]
        elif operator == '==':
            mask = [v == value for v in col_data]
        else:
            mask = [True] * len(col_data)
        return self[mask]

# Demo: Data Filtering
print("Pandas Data Filtering - Simulation")
print("=" * 60)

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 45],
    'City': ['NYC', 'LA', 'NYC', 'Chicago', 'LA'],
    'Salary': [50000, 60000, 75000, 55000, 90000]
}

df = DataFrameSimulation(data)

print("\\nOriginal DataFrame:")
print(df)

print("\\n1. Filter Age > 30:")
filtered = df.query('Age', '>', 30)
print(filtered)

print("\\n2. Filter Salary >= 60000:")
high_earners = df.query('Salary', '>=', 60000)
print(high_earners)

print("\\n3. Select specific columns:")
subset = df[['Name', 'Salary']]
print(subset)

print("\\n" + "=" * 60)
print("Key Concepts:")
print("- Boolean indexing: df[df['Age'] > 30]")
print("- Column selection: df['Name']")
print("- Multiple columns: df[['Name', 'Age']]")
print("- Chaining filters: df[condition1 & condition2]")""",

    522: """# In production: import pandas as pd
# import matplotlib.pyplot as plt
# df.plot(kind='bar')
# This simulation shows pandas visualization concepts

class DataFrameSimulation:
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())

    def plot_bar(self, x_col, y_col):
        \"\"\"Simulate bar chart (text-based)\"\"\"
        # Real: Uses matplotlib for graphical plotting
        # Simulation: ASCII bar chart for learning
        print(f"\\nBar Chart: {y_col} by {x_col}")
        print("-" * 50)

        max_val = max(self.data[y_col])
        scale = 40 / max_val if max_val > 0 else 1

        for i in range(len(self.data[x_col])):
            label = str(self.data[x_col][i])[:15]
            value = self.data[y_col][i]
            bar_len = int(value * scale)
            bar = '#' * bar_len
            print(f"{label:>15} | {bar} {value}")

    def plot_line(self, x_col, y_col):
        \"\"\"Simulate line chart\"\"\"
        print(f"\\nLine Chart: {y_col} over {x_col}")
        print("-" * 50)

        values = self.data[y_col]
        max_val = max(values)
        min_val = min(values)

        # Show trend
        for i in range(len(values)):
            x_label = str(self.data[x_col][i])
            y_val = values[i]
            # Normalize to 0-100
            normalized = int(((y_val - min_val) / (max_val - min_val)) * 100) if max_val != min_val else 50
            spaces = ' ' * normalized
            print(f"{x_label:>10} | {spaces}* ({y_val})")

    def describe_viz(self):
        \"\"\"Show data distribution\"\"\"
        print("\\nData Distribution:")
        print("-" * 50)
        for col in self.columns:
            if all(isinstance(v, (int, float)) for v in self.data[col]):
                values = self.data[col]
                print(f"\\n{col}:")
                print(f"  Min: {min(values)}, Max: {max(values)}")
                print(f"  Mean: {sum(values)/len(values):.1f}")
                # Show histogram
                bins = 5
                hist, _ = self._histogram(values, bins)
                for i, count in enumerate(hist):
                    bar = '█' * count
                    print(f"  Bin {i+1}: {bar} ({count})")

    def _histogram(self, values, bins):
        \"\"\"Helper to create histogram\"\"\"
        min_val, max_val = min(values), max(values)
        bin_width = (max_val - min_val) / bins if max_val != min_val else 1
        hist = [0] * bins
        for v in values:
            bin_idx = min(int((v - min_val) / bin_width), bins - 1)
            hist[bin_idx] += 1
        return hist, bin_width

# Demo: Data Visualization
print("Pandas Data Visualization - Simulation")
print("=" * 60)

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [15000, 18000, 22000, 17000, 25000],
    'Expenses': [12000, 13000, 15000, 14000, 16000]
}

df = DataFrameSimulation(data)

df.plot_bar('Month', 'Sales')
df.plot_line('Month', 'Expenses')
df.describe_viz()

print("\\n" + "=" * 60)
print("Real pandas visualization:")
print("  df.plot(kind='bar')  # Bar chart")
print("  df.plot(kind='line') # Line chart")
print("  df.plot(kind='hist') # Histogram")
print("  df.plot(kind='box')  # Box plot")
print("\\nRequires: pip install matplotlib")""",

    788: """# In production: import pandas as pd
# grouped = df.groupby('Category').agg({'Sales': 'sum', 'Count': 'mean'})
# This simulation demonstrates pandas groupby without installation

class GroupBySimulation:
    \"\"\"Simulates pandas GroupBy object\"\"\"
    def __init__(self, groups):
        # groups is dict of {key: [list of row dicts]}
        self.groups = groups

    def agg(self, agg_dict):
        \"\"\"Aggregate grouped data\"\"\"
        # Real: Uses optimized Cython implementations
        # Simulation: Pure Python aggregations
        result = {}

        for group_key, rows in self.groups.items():
            result[group_key] = {}

            for col, func in agg_dict.items():
                values = [row[col] for row in rows if col in row]

                if func == 'sum':
                    result[group_key][col] = sum(values)
                elif func == 'mean':
                    result[group_key][col] = sum(values) / len(values) if values else 0
                elif func == 'count':
                    result[group_key][col] = len(values)
                elif func == 'min':
                    result[group_key][col] = min(values) if values else None
                elif func == 'max':
                    result[group_key][col] = max(values) if values else None

        return result

    def sum(self):
        \"\"\"Sum all numeric columns\"\"\"
        result = {}
        for group_key, rows in self.groups.items():
            result[group_key] = {}
            # Get all numeric columns
            first_row = rows[0] if rows else {}
            for col in first_row:
                values = [row[col] for row in rows if isinstance(row.get(col), (int, float))]
                if values:
                    result[group_key][col] = sum(values)
        return result

class DataFrameSimulation:
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())

    def groupby(self, column):
        \"\"\"Group by column values\"\"\"
        # Real: Creates GroupBy object with optimized hash tables
        # Simulation: Simple dict grouping
        groups = {}
        col_data = self.data[column]

        for i, key in enumerate(col_data):
            if key not in groups:
                groups[key] = []
            row = {col: self.data[col][i] for col in self.columns}
            groups[key].append(row)

        return GroupBySimulation(groups)

# Demo: GroupBy Aggregation
print("Pandas GroupBy Aggregation - Simulation")
print("=" * 60)

data = {
    'Category': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Electronics'],
    'Product': ['Laptop', 'Mouse', 'Shirt', 'Pants', 'Keyboard'],
    'Sales': [1200, 25, 45, 60, 75],
    'Quantity': [2, 10, 15, 8, 5]
}

df = DataFrameSimulation(data)

print("\\nOriginal Data:")
for i in range(len(data['Category'])):
    print(f"{data['Category'][i]:>12} | {data['Product'][i]:>10} | ${data['Sales'][i]:>6} | Qty: {data['Quantity'][i]}")

print("\\n" + "=" * 60)
print("GroupBy: Category")
print("=" * 60)

grouped = df.groupby('Category')

# Aggregation 1: Total sales per category
agg1 = grouped.agg({'Sales': 'sum', 'Quantity': 'sum'})
print("\\nTotal Sales and Quantity by Category:")
for category, values in agg1.items():
    print(f"{category:>12} | Sales: ${values['Sales']:>6} | Qty: {values['Quantity']}")

# Aggregation 2: Average
agg2 = grouped.agg({'Sales': 'mean', 'Quantity': 'mean'})
print("\\nAverage Sales and Quantity by Category:")
for category, values in agg2.items():
    print(f"{category:>12} | Avg Sales: ${values['Sales']:>6.2f} | Avg Qty: {values['Quantity']:.1f}")

print("\\n" + "=" * 60)
print("Real pandas groupby:")
print("  df.groupby('Category').sum()")
print("  df.groupby('Category')['Sales'].mean()")
print("  df.groupby('Category').agg({'Sales': 'sum', 'Quantity': 'mean'})")""",

    789: """# In production: import pandas as pd
# merged = pd.merge(df1, df2, on='id', how='inner')
# This simulation demonstrates pandas merge/join operations

class DataFrameSimulation:
    def __init__(self, data):
        self.data = data
        self.columns = list(data.keys())

    def merge(self, other, on, how='inner'):
        \"\"\"Merge two DataFrames (simulates pd.merge())\"\"\"
        # Real: Uses optimized hash joins
        # Simulation: Nested loop join for learning

        # Create index for faster lookup
        other_index = {}
        for i in range(len(other.data[on])):
            key = other.data[on][i]
            if key not in other_index:
                other_index[key] = []
            row = {col: other.data[col][i] for col in other.columns}
            other_index[key].append(row)

        # Perform join
        result_data = {col: [] for col in self.columns}
        for col in other.columns:
            if col not in result_data and col != on:
                result_data[col] = []

        for i in range(len(self.data[on])):
            key = self.data[on][i]

            if how == 'inner':
                if key in other_index:
                    for other_row in other_index[key]:
                        # Add left row
                        for col in self.columns:
                            result_data[col].append(self.data[col][i])
                        # Add right row
                        for col in other.columns:
                            if col != on:
                                result_data[col].append(other_row[col])

            elif how == 'left':
                if key in other_index:
                    for other_row in other_index[key]:
                        for col in self.columns:
                            result_data[col].append(self.data[col][i])
                        for col in other.columns:
                            if col != on:
                                result_data[col].append(other_row[col])
                else:
                    # No match, add None for right columns
                    for col in self.columns:
                        result_data[col].append(self.data[col][i])
                    for col in other.columns:
                        if col != on:
                            result_data[col].append(None)

        return DataFrameSimulation(result_data)

    def __repr__(self):
        result = "  " + "  ".join(f"{col:>12}" for col in self.columns) + "\\n"
        for i in range(min(len(list(self.data.values())[0]), 10)):
            row = f"{i}  "
            for col in self.columns:
                val = str(self.data[col][i])[:12] if self.data[col][i] is not None else 'None'
                row += f"{val:>12}  "
            result += row + "\\n"
        return result

# Demo: Merge and Join
print("Pandas Merge and Join - Simulation")
print("=" * 70)

# DataFrame 1: Employees
employees = {
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': [10, 20, 10, 30]
}

# DataFrame 2: Departments
departments = {
    'dept_id': [10, 20, 40],
    'dept_name': ['Engineering', 'Sales', 'Marketing']
}

df_emp = DataFrameSimulation(employees)
df_dept = DataFrameSimulation(departments)

print("\\nEmployees DataFrame:")
print(df_emp)

print("\\nDepartments DataFrame:")
print(df_dept)

print("\\n" + "=" * 70)
print("INNER JOIN: Only matching rows")
print("=" * 70)
inner_join = df_emp.merge(df_dept, on='dept_id', how='inner')
print(inner_join)
print("Note: David (dept_id=30) and Marketing (dept_id=40) are excluded")

print("\\n" + "=" * 70)
print("LEFT JOIN: All employees, matching departments")
print("=" * 70)
left_join = df_emp.merge(df_dept, on='dept_id', how='left')
print(left_join)
print("Note: David has dept_id=30 but no matching department (None)")

print("\\n" + "=" * 70)
print("Real pandas merge:")
print("  pd.merge(df1, df2, on='key', how='inner')")
print("  pd.merge(df1, df2, on='key', how='left')")
print("  pd.merge(df1, df2, on='key', how='right')")
print("  pd.merge(df1, df2, on='key', how='outer')  # Full outer join")"""
}

def update_batch_1(lessons_file):
    """Update batch 1 of pandas lessons"""
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    updated = []
    for lesson in lessons:
        lesson_id = lesson.get('id')
        if lesson_id in PANDAS_BATCH_1:
            before_len = len(lesson.get('fullSolution', ''))
            lesson['fullSolution'] = PANDAS_BATCH_1[lesson_id]
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

    print("Upgrading pandas lessons - Batch 1 (5 lessons)")
    print("=" * 70)

    updated = update_batch_1(lessons_file)

    print(f"\\nUpdated {len(updated)} pandas lessons:\\n")
    for item in updated:
        print(f"ID {item['id']}: {item['title']}")
        print(f"  {item['before']:>6,} -> {item['after']:>6,} chars (+{item['after']-item['before']:>5,})")

    total_added = sum(item['after'] - item['before'] for item in updated)
    print(f"\\nTotal characters added: {total_added:,}")
    print("\\nBatch 1 complete!")

if __name__ == '__main__':
    sys.exit(main())
