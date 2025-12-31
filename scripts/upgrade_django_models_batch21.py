import json

# Read lessons
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons to upgrade
lesson_753 = next(l for l in lessons if l['id'] == 753)  # Django Model Aggregation
lesson_755 = next(l for l in lessons if l['id'] == 755)  # Django REST Framework Serializer
lesson_752 = next(l for l in lessons if l['id'] == 752)  # Django ManyToMany Relationships

# ============================================================================
# LESSON 753: Django Model Aggregation
# ============================================================================

lesson_753['fullSolution'] = '''"""
Django Model Aggregation - Comprehensive Guide
==============================================

This lesson covers comprehensive Django model aggregation including COUNT, SUM, AVG,
MAX, MIN, annotate(), aggregate(), GROUP BY, HAVING clauses, complex aggregations,
conditional aggregations, window functions, and performance optimization.

**Zero Package Installation Required**

Learning Objectives:
- Master Django aggregation functions
- Use annotate() for per-object aggregations
- Use aggregate() for query-level aggregations
- Implement GROUP BY and HAVING clauses
- Perform conditional aggregations
- Calculate running totals and window functions
- Optimize aggregation performance
- Handle NULL values in aggregations
- Combine multiple aggregations
- Create custom aggregation functions
"""

from typing import Dict, List, Any, Optional, Callable
from datetime import datetime, timedelta
from decimal import Decimal
import json

# ============================================================================
# Example 1: Basic Aggregation Functions
# ============================================================================

class AggregateFunction:
    """
    Base class for aggregation functions.
    """

    def __init__(self, field: str):
        self.field = field

    def calculate(self, values: List[Any]) -> Any:
        """Calculate aggregation result."""
        raise NotImplementedError

class Count(AggregateFunction):
    """COUNT aggregation."""

    def calculate(self, values: List[Any]) -> int:
        return len([v for v in values if v is not None])

class Sum(AggregateFunction):
    """SUM aggregation."""

    def calculate(self, values: List[Any]) -> Decimal:
        return sum(Decimal(str(v)) for v in values if v is not None)

class Avg(AggregateFunction):
    """AVG aggregation."""

    def calculate(self, values: List[Any]) -> Decimal:
        valid_values = [Decimal(str(v)) for v in values if v is not None]
        return sum(valid_values) / len(valid_values) if valid_values else Decimal('0')

class Max(AggregateFunction):
    """MAX aggregation."""

    def calculate(self, values: List[Any]) -> Any:
        valid_values = [v for v in values if v is not None]
        return max(valid_values) if valid_values else None

class Min(AggregateFunction):
    """MIN aggregation."""

    def calculate(self, values: List[Any]) -> Any:
        valid_values = [v for v in values if v is not None]
        return min(valid_values) if valid_values else None

class QuerySet:
    """
    Simulates Django QuerySet with aggregation support.
    """

    def __init__(self, objects: List[Dict]):
        self.objects = objects

    def aggregate(self, **kwargs) -> Dict[str, Any]:
        """Perform aggregations on the queryset."""
        results = {}

        for alias, agg_func in kwargs.items():
            values = [obj.get(agg_func.field) for obj in self.objects]
            results[alias] = agg_func.calculate(values)

        return results

    def count(self) -> int:
        """Count objects in queryset."""
        return len(self.objects)

def example_basic_aggregations():
    """
    Demonstrates basic aggregation functions.
    """
    print(f"{'='*60}")
    print("Example 1: Basic Aggregation Functions")
    print(f"{'='*60}")

    # Sample data - Product sales
    sales = [
        {'id': 1, 'product': 'Laptop', 'quantity': 5, 'price': Decimal('1200.00')},
        {'id': 2, 'product': 'Mouse', 'quantity': 20, 'price': Decimal('25.00')},
        {'id': 3, 'product': 'Keyboard', 'quantity': 15, 'price': Decimal('75.00')},
        {'id': 4, 'product': 'Monitor', 'quantity': 8, 'price': Decimal('350.00')},
        {'id': 5, 'product': 'Headphones', 'quantity': 12, 'price': Decimal('80.00')},
    ]

    queryset = QuerySet(sales)

    print("\\nSales Data:")
    for sale in sales:
        print(f"  {sale['product']:12s} - Qty: {sale['quantity']:2d}, Price: ${sale['price']}")

    # Perform aggregations
    result = queryset.aggregate(
        total_products=Count('id'),
        total_quantity=Sum('quantity'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )

    print("\\nAggregation Results:")
    print(f"  Total Products: {result['total_products']}")
    print(f"  Total Quantity: {result['total_quantity']}")
    print(f"  Average Price: ${result['avg_price']:.2f}")
    print(f"  Max Price: ${result['max_price']}")
    print(f"  Min Price: ${result['min_price']}")

# ============================================================================
# Example 2: Annotate for Per-Object Aggregations
# ============================================================================

class AnnotatedQuerySet(QuerySet):
    """
    QuerySet with annotation support.
    """

    def annotate(self, **kwargs) -> 'AnnotatedQuerySet':
        """Add aggregated fields to each object."""
        annotated_objects = []

        for obj in self.objects:
            annotated_obj = obj.copy()

            for alias, value in kwargs.items():
                if callable(value):
                    annotated_obj[alias] = value(obj)
                else:
                    annotated_obj[alias] = value

            annotated_objects.append(annotated_obj)

        return AnnotatedQuerySet(annotated_objects)

    def values(self, *fields) -> List[Dict]:
        """Return list of dicts with specified fields."""
        if not fields:
            return self.objects

        return [{field: obj.get(field) for field in fields} for obj in self.objects]

def example_annotate():
    """
    Demonstrates annotate() for per-object calculations.
    """
    print(f"\\n{'='*60}")
    print("Example 2: Annotate - Per-Object Aggregations")
    print(f"{'='*60}")

    # Sample data - Orders with line items
    orders = [
        {'id': 1, 'customer': 'John', 'quantity': 5, 'unit_price': Decimal('100.00')},
        {'id': 2, 'customer': 'Jane', 'quantity': 3, 'unit_price': Decimal('200.00')},
        {'id': 3, 'customer': 'Bob', 'quantity': 10, 'unit_price': Decimal('50.00')},
    ]

    queryset = AnnotatedQuerySet(orders)

    print("\\nOriginal Orders:")
    for order in orders:
        print(f"  Order {order['id']}: {order['customer']:8s} - Qty: {order['quantity']}, Price: ${order['unit_price']}")

    # Annotate with calculated total
    annotated = queryset.annotate(
        total=lambda obj: Decimal(str(obj['quantity'])) * obj['unit_price']
    )

    print("\\nAnnotated Orders (with total):")
    for order in annotated.objects:
        print(f"  Order {order['id']}: {order['customer']:8s} - Total: ${order['total']:.2f}")

# ============================================================================
# Example 3: GROUP BY with Aggregation
# ============================================================================

class GroupByQuerySet(AnnotatedQuerySet):
    """
    QuerySet with GROUP BY support.
    """

    def group_by(self, *fields) -> Dict[Any, List[Dict]]:
        """Group objects by specified fields."""
        groups: Dict[Any, List[Dict]] = {}

        for obj in self.objects:
            key = tuple(obj.get(field) for field in fields)
            if key not in groups:
                groups[key] = []
            groups[key].append(obj)

        return groups

    def values_group(self, *group_fields, **aggregations) -> List[Dict]:
        """
        Group by fields and perform aggregations.
        Simulates: Model.objects.values('field').annotate(count=Count('id'))
        """
        groups = self.group_by(*group_fields)
        results = []

        for key, objects in groups.items():
            result = {}

            # Add group fields
            for i, field in enumerate(group_fields):
                result[field] = key[i]

            # Add aggregations
            for alias, agg_func in aggregations.items():
                values = [obj.get(agg_func.field) for obj in objects]
                result[alias] = agg_func.calculate(values)

            results.append(result)

        return results

def example_group_by():
    """
    Demonstrates GROUP BY with aggregations.
    """
    print(f"\\n{'='*60}")
    print("Example 3: GROUP BY with Aggregation")
    print(f"{'='*60}")

    # Sample data - Sales by category
    sales = [
        {'id': 1, 'category': 'Electronics', 'product': 'Laptop', 'amount': Decimal('1200.00')},
        {'id': 2, 'category': 'Electronics', 'product': 'Phone', 'amount': Decimal('800.00')},
        {'id': 3, 'category': 'Books', 'product': 'Python Guide', 'amount': Decimal('45.00')},
        {'id': 4, 'category': 'Books', 'product': 'Django Book', 'amount': Decimal('55.00')},
        {'id': 5, 'category': 'Electronics', 'product': 'Tablet', 'amount': Decimal('500.00')},
        {'id': 6, 'category': 'Clothing', 'product': 'Shirt', 'amount': Decimal('30.00')},
        {'id': 7, 'category': 'Clothing', 'product': 'Pants', 'amount': Decimal('50.00')},
    ]

    queryset = GroupByQuerySet(sales)

    print("\\nAll Sales:")
    for sale in sales:
        print(f"  {sale['category']:12s} - {sale['product']:15s}: ${sale['amount']}")

    # Group by category with aggregations
    results = queryset.values_group(
        'category',
        count=Count('id'),
        total=Sum('amount'),
        average=Avg('amount')
    )

    print("\\nSales by Category:")
    print(f"{'Category':15s} {'Count':>8s} {'Total':>12s} {'Average':>12s}")
    print('-' * 50)
    for result in results:
        print(f"{result['category']:15s} {result['count']:8d} ${result['total']:>11.2f} ${result['average']:>11.2f}")

# ============================================================================
# Example 4: Conditional Aggregation
# ============================================================================

class Case:
    """
    Simulates Django's Case/When for conditional expressions.
    """

    def __init__(self, conditions: List[tuple], default=None):
        self.conditions = conditions  # List of (condition_func, value)
        self.default = default

    def evaluate(self, obj: Dict) -> Any:
        """Evaluate conditional expression."""
        for condition_func, value in self.conditions:
            if condition_func(obj):
                return value
        return self.default

def example_conditional_aggregation():
    """
    Demonstrates conditional aggregations.
    """
    print(f"\\n{'='*60}")
    print("Example 4: Conditional Aggregation")
    print(f"{'='*60}")

    # Sample data - Orders with status
    orders = [
        {'id': 1, 'amount': Decimal('100.00'), 'status': 'completed'},
        {'id': 2, 'amount': Decimal('200.00'), 'status': 'pending'},
        {'id': 3, 'amount': Decimal('150.00'), 'status': 'completed'},
        {'id': 4, 'amount': Decimal('75.00'), 'status': 'cancelled'},
        {'id': 5, 'amount': Decimal('300.00'), 'status': 'completed'},
        {'id': 6, 'amount': Decimal('120.00'), 'status': 'pending'},
    ]

    queryset = AnnotatedQuerySet(orders)

    print("\\nAll Orders:")
    for order in orders:
        print(f"  Order {order['id']}: ${order['amount']:>7.2f} - {order['status']}")

    # Annotate with conditional values
    annotated = queryset.annotate(
        completed_amount=lambda obj: obj['amount'] if obj['status'] == 'completed' else Decimal('0'),
        pending_amount=lambda obj: obj['amount'] if obj['status'] == 'pending' else Decimal('0'),
        cancelled_amount=lambda obj: obj['amount'] if obj['status'] == 'cancelled' else Decimal('0')
    )

    # Aggregate by status
    result = GroupByQuerySet(annotated.objects).aggregate(
        completed_total=Sum('completed_amount'),
        pending_total=Sum('pending_amount'),
        cancelled_total=Sum('cancelled_amount'),
        total=Sum('amount')
    )

    print("\\nAggregation by Status:")
    print(f"  Completed: ${result['completed_total']:.2f}")
    print(f"  Pending: ${result['pending_total']:.2f}")
    print(f"  Cancelled: ${result['cancelled_total']:.2f}")
    print(f"  Total: ${result['total']:.2f}")

# ============================================================================
# Example 5: Complex Multi-Level Aggregations
# ============================================================================

def example_complex_aggregations():
    """
    Demonstrates complex multi-level aggregations.
    """
    print(f"\\n{'='*60}")
    print("Example 5: Complex Multi-Level Aggregations")
    print(f"{'='*60}")

    # Sample data - E-commerce with nested relationships
    orders = [
        {'id': 1, 'customer_id': 1, 'customer': 'John', 'region': 'North', 'total': Decimal('500.00'), 'items': 5},
        {'id': 2, 'customer_id': 2, 'customer': 'Jane', 'region': 'South', 'total': Decimal('750.00'), 'items': 8},
        {'id': 3, 'customer_id': 1, 'customer': 'John', 'region': 'North', 'total': Decimal('300.00'), 'items': 3},
        {'id': 4, 'customer_id': 3, 'customer': 'Bob', 'region': 'North', 'total': Decimal('1200.00'), 'items': 15},
        {'id': 5, 'customer_id': 2, 'customer': 'Jane', 'region': 'South', 'total': Decimal('450.00'), 'items': 6},
        {'id': 6, 'customer_id': 4, 'customer': 'Alice', 'region': 'East', 'total': Decimal('900.00'), 'items': 10},
    ]

    queryset = GroupByQuerySet(orders)

    print("\\nAll Orders:")
    for order in orders:
        print(f"  Order {order['id']}: {order['customer']:8s} ({order['region']:5s}) - ${order['total']:>7.2f}, {order['items']} items")

    # Aggregation 1: By Region
    print("\\nAggregation by Region:")
    by_region = queryset.values_group(
        'region',
        order_count=Count('id'),
        total_revenue=Sum('total'),
        avg_order=Avg('total'),
        total_items=Sum('items')
    )

    print(f"{'Region':8s} {'Orders':>8s} {'Revenue':>12s} {'Avg Order':>12s} {'Items':>8s}")
    print('-' * 60)
    for result in sorted(by_region, key=lambda x: x['total_revenue'], reverse=True):
        print(f"{result['region']:8s} {result['order_count']:8d} ${result['total_revenue']:>11.2f} ${result['avg_order']:>11.2f} {result['total_items']:8d}")

    # Aggregation 2: By Customer
    print("\\nAggregation by Customer:")
    by_customer = queryset.values_group(
        'customer',
        order_count=Count('id'),
        total_spent=Sum('total'),
        avg_order=Avg('total')
    )

    print(f"{'Customer':10s} {'Orders':>8s} {'Total Spent':>12s} {'Avg Order':>12s}")
    print('-' * 50)
    for result in sorted(by_customer, key=lambda x: x['total_spent'], reverse=True):
        print(f"{result['customer']:10s} {result['order_count']:8d} ${result['total_spent']:>11.2f} ${result['avg_order']:>11.2f}")

# ============================================================================
# Example 6: Window Functions (Running Totals)
# ============================================================================

class WindowFunction:
    """
    Simulates window functions for running calculations.
    """

    @staticmethod
    def running_total(objects: List[Dict], field: str, order_by: str) -> List[Dict]:
        """Calculate running total."""
        sorted_objects = sorted(objects, key=lambda x: x[order_by])
        running_sum = Decimal('0')

        for obj in sorted_objects:
            running_sum += Decimal(str(obj[field]))
            obj['running_total'] = running_sum

        return sorted_objects

    @staticmethod
    def rank(objects: List[Dict], field: str, order_by: str, ascending: bool = False) -> List[Dict]:
        """Calculate rank."""
        sorted_objects = sorted(objects, key=lambda x: x[order_by], reverse=not ascending)

        for i, obj in enumerate(sorted_objects, 1):
            obj['rank'] = i

        return sorted_objects

def example_window_functions():
    """
    Demonstrates window functions for running calculations.
    """
    print(f"\\n{'='*60}")
    print("Example 6: Window Functions (Running Totals)")
    print(f"{'='*60}")

    # Sample data - Daily sales
    daily_sales = [
        {'date': '2024-01-01', 'revenue': Decimal('1000.00')},
        {'date': '2024-01-02', 'revenue': Decimal('1500.00')},
        {'date': '2024-01-03', 'revenue': Decimal('1200.00')},
        {'date': '2024-01-04', 'revenue': Decimal('1800.00')},
        {'date': '2024-01-05', 'revenue': Decimal('2000.00')},
    ]

    print("\\nDaily Sales with Running Total:")
    print(f"{'Date':12s} {'Revenue':>12s} {'Running Total':>15s}")
    print('-' * 45)

    with_running_total = WindowFunction.running_total(daily_sales.copy(), 'revenue', 'date')

    for sale in with_running_total:
        print(f"{sale['date']:12s} ${sale['revenue']:>11.2f} ${sale['running_total']:>14.2f}")

# ============================================================================
# Example 7: HAVING Clause Simulation
# ============================================================================

def example_having_clause():
    """
    Demonstrates HAVING clause for filtering aggregated results.
    """
    print(f"\\n{'='*60}")
    print("Example 7: HAVING Clause (Filter Aggregated Results)")
    print(f"{'='*60}")

    # Sample data - Product sales
    sales = [
        {'id': 1, 'product': 'Laptop', 'quantity': 5, 'amount': Decimal('6000.00')},
        {'id': 2, 'product': 'Mouse', 'quantity': 50, 'amount': Decimal('1250.00')},
        {'id': 3, 'product': 'Laptop', 'quantity': 3, 'amount': Decimal('3600.00')},
        {'id': 4, 'product': 'Keyboard', 'quantity': 20, 'amount': Decimal('1500.00')},
        {'id': 5, 'product': 'Mouse', 'quantity': 30, 'amount': Decimal('750.00')},
        {'id': 6, 'product': 'Monitor', 'quantity': 2, 'amount': Decimal('700.00')},
    ]

    queryset = GroupByQuerySet(sales)

    # Group by product
    by_product = queryset.values_group(
        'product',
        total_sales=Count('id'),
        total_quantity=Sum('quantity'),
        total_revenue=Sum('amount')
    )

    # Filter with HAVING (total_revenue > 1000)
    print("\\nProducts with Revenue > $1000:")
    print(f"{'Product':12s} {'Sales':>8s} {'Quantity':>10s} {'Revenue':>12s}")
    print('-' * 50)

    for result in by_product:
        if result['total_revenue'] > Decimal('1000.00'):
            print(f"{result['product']:12s} {result['total_sales']:8d} {result['total_quantity']:10d} ${result['total_revenue']:>11.2f}")

# ============================================================================
# Example 8: Distinct Count
# ============================================================================

class DistinctCount(AggregateFunction):
    """COUNT DISTINCT aggregation."""

    def calculate(self, values: List[Any]) -> int:
        return len(set(v for v in values if v is not None))

def example_distinct_count():
    """
    Demonstrates distinct count aggregation.
    """
    print(f"\\n{'='*60}")
    print("Example 8: Distinct Count Aggregation")
    print(f"{'='*60}")

    # Sample data - Orders
    orders = [
        {'id': 1, 'customer_id': 1, 'product_id': 10, 'amount': Decimal('100.00')},
        {'id': 2, 'customer_id': 2, 'product_id': 10, 'amount': Decimal('100.00')},
        {'id': 3, 'customer_id': 1, 'product_id': 20, 'amount': Decimal('200.00')},
        {'id': 4, 'customer_id': 3, 'product_id': 10, 'amount': Decimal('100.00')},
        {'id': 5, 'customer_id': 2, 'product_id': 30, 'amount': Decimal('300.00')},
    ]

    queryset = QuerySet(orders)

    result = queryset.aggregate(
        total_orders=Count('id'),
        unique_customers=DistinctCount('customer_id'),
        unique_products=DistinctCount('product_id')
    )

    print("\\nAggregation Results:")
    print(f"  Total Orders: {result['total_orders']}")
    print(f"  Unique Customers: {result['unique_customers']}")
    print(f"  Unique Products: {result['unique_products']}")

# ============================================================================
# Example 9: Aggregation with Filtering
# ============================================================================

def example_aggregation_with_filter():
    """
    Demonstrates aggregations with pre-filtering.
    """
    print(f"\\n{'='*60}")
    print("Example 9: Aggregation with Filtering")
    print(f"{'='*60}")

    # Sample data - Sales with dates
    sales = [
        {'id': 1, 'date': '2024-01-15', 'amount': Decimal('500.00'), 'status': 'completed'},
        {'id': 2, 'date': '2024-01-20', 'amount': Decimal('750.00'), 'status': 'pending'},
        {'id': 3, 'date': '2024-02-05', 'amount': Decimal('300.00'), 'status': 'completed'},
        {'id': 4, 'date': '2024-02-10', 'amount': Decimal('1200.00'), 'status': 'completed'},
        {'id': 5, 'date': '2024-02-15', 'amount': Decimal('450.00'), 'status': 'cancelled'},
    ]

    # Filter: Only completed sales in February
    filtered_sales = [
        s for s in sales
        if s['status'] == 'completed' and s['date'].startswith('2024-02')
    ]

    queryset = QuerySet(filtered_sales)

    result = queryset.aggregate(
        count=Count('id'),
        total=Sum('amount'),
        average=Avg('amount')
    )

    print("\\nCompleted Sales in February 2024:")
    print(f"  Count: {result['count']}")
    print(f"  Total: ${result['total']:.2f}")
    print(f"  Average: ${result['average']:.2f}")

# ============================================================================
# Example 10: Complete Aggregation Report
# ============================================================================

def example_complete_aggregation_report():
    """
    Complete aggregation report with multiple metrics.
    """
    print(f"\\n{'='*60}")
    print("Example 10: Complete Aggregation Report")
    print(f"{'='*60}")

    # Sample data - E-commerce database
    transactions = [
        {'id': 1, 'date': '2024-01-15', 'customer_id': 1, 'category': 'Electronics', 'product': 'Laptop', 'quantity': 1, 'price': Decimal('1200.00')},
        {'id': 2, 'date': '2024-01-16', 'customer_id': 2, 'category': 'Books', 'product': 'Python Book', 'quantity': 2, 'price': Decimal('45.00')},
        {'id': 3, 'date': '2024-01-17', 'customer_id': 1, 'category': 'Electronics', 'product': 'Mouse', 'quantity': 1, 'price': Decimal('25.00')},
        {'id': 4, 'date': '2024-01-18', 'customer_id': 3, 'category': 'Clothing', 'product': 'Shirt', 'quantity': 3, 'price': Decimal('30.00')},
        {'id': 5, 'date': '2024-01-19', 'customer_id': 2, 'category': 'Electronics', 'product': 'Keyboard', 'quantity': 1, 'price': Decimal('75.00')},
        {'id': 6, 'date': '2024-01-20', 'customer_id': 4, 'category': 'Books', 'product': 'Django Book', 'quantity': 1, 'price': Decimal('55.00')},
    ]

    # Add total to each transaction
    for t in transactions:
        t['total'] = Decimal(str(t['quantity'])) * t['price']

    queryset = GroupByQuerySet(transactions)

    print("\\n=== SALES ANALYTICS REPORT ===\\n")

    # 1. Overall Statistics
    overall = QuerySet(transactions).aggregate(
        total_transactions=Count('id'),
        total_revenue=Sum('total'),
        avg_transaction=Avg('total'),
        unique_customers=DistinctCount('customer_id')
    )

    print("1. Overall Statistics:")
    print(f"   Total Transactions: {overall['total_transactions']}")
    print(f"   Total Revenue: ${overall['total_revenue']:.2f}")
    print(f"   Average Transaction: ${overall['avg_transaction']:.2f}")
    print(f"   Unique Customers: {overall['unique_customers']}")

    # 2. Sales by Category
    print("\\n2. Sales by Category:")
    by_category = queryset.values_group(
        'category',
        transactions=Count('id'),
        revenue=Sum('total'),
        avg_order=Avg('total')
    )

    print(f"   {'Category':15s} {'Txns':>6s} {'Revenue':>12s} {'Avg Order':>12s}")
    print('   ' + '-' * 50)
    for cat in sorted(by_category, key=lambda x: x['revenue'], reverse=True):
        print(f"   {cat['category']:15s} {cat['transactions']:6d} ${cat['revenue']:>11.2f} ${cat['avg_order']:>11.2f}")

    # 3. Top Customers
    print("\\n3. Top Customers (by revenue):")
    by_customer = queryset.values_group(
        'customer_id',
        orders=Count('id'),
        total_spent=Sum('total')
    )

    print(f"   {'Customer ID':12s} {'Orders':>8s} {'Total Spent':>14s}")
    print('   ' + '-' * 40)
    for cust in sorted(by_customer, key=lambda x: x['total_spent'], reverse=True):
        print(f"   {str(cust['customer_id']):12s} {cust['orders']:8d} ${cust['total_spent']:>13.2f}")

    # 4. Daily Revenue Trend
    print("\\n4. Daily Revenue Trend:")
    by_date = queryset.values_group(
        'date',
        transactions=Count('id'),
        revenue=Sum('total')
    )

    print(f"   {'Date':12s} {'Txns':>6s} {'Revenue':>12s}")
    print('   ' + '-' * 35)
    for day in sorted(by_date, key=lambda x: x['date']):
        print(f"   {day['date']:12s} {day['transactions']:6d} ${day['revenue']:>11.2f}")

    print("\\n=== END OF REPORT ===")

# ============================================================================
# Run All Examples
# ============================================================================

if __name__ == "__main__":
    # Example 1: Basic aggregations
    example_basic_aggregations()

    # Example 2: Annotate
    example_annotate()

    # Example 3: GROUP BY
    example_group_by()

    # Example 4: Conditional aggregation
    example_conditional_aggregation()

    # Example 5: Complex aggregations
    example_complex_aggregations()

    # Example 6: Window functions
    example_window_functions()

    # Example 7: HAVING clause
    example_having_clause()

    # Example 8: Distinct count
    example_distinct_count()

    # Example 9: Aggregation with filtering
    example_aggregation_with_filter()

    # Example 10: Complete report
    example_complete_aggregation_report()

    print(f"\\n{'='*60}")
    print("All Django aggregation examples completed successfully!")
    print(f"{'='*60}")
'''

print("Upgraded Lesson 753: Django Model Aggregation")
print(f"  New length: {len(lesson_753['fullSolution']):,} characters")

# Save lessons
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2)

print("\\n" + "="*70)
print("BATCH 21 PART 1 COMPLETE: Django Model Aggregation")
print("="*70)
print("\\nUpgraded lesson:")
print(f"  - Lesson 753: Django Model Aggregation ({len(lesson_753['fullSolution']):,} chars)")
print("\\nLesson upgraded to 13,000+ characters")
print("Zero package installation required!")
print("="*70)
