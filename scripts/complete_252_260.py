#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 252: GitHub Actions - Automated Testing
lesson252 = next(l for l in lessons if l['id'] == 252)
lesson252['title'] = "GitHub Actions - Automated Testing"
lesson252['content'] = '''# GitHub Actions - Automated Testing

Automate testing workflows with GitHub Actions using Python. CI/CD pipelines ensure code quality by running tests automatically on every commit and pull request. Python's ecosystem integrates seamlessly with GitHub Actions for comprehensive test automation.

## Example 1: Basic GitHub Actions Workflow

Create simple test workflow:

```yaml
# .github/workflows/test.yml
name: Python Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest

    - name: Run tests
      run: pytest
```

**Result**: Automated test execution on push.

## Example 2: Python Script to Generate Workflow

Create workflows programmatically:

```python
import yaml

def create_test_workflow(python_versions, test_command='pytest'):
    """Generate GitHub Actions workflow for testing."""
    workflow = {
        'name': 'Python Tests',
        'on': ['push', 'pull_request'],
        'jobs': {
            'test': {
                'runs-on': 'ubuntu-latest',
                'strategy': {
                    'matrix': {
                        'python-version': python_versions
                    }
                },
                'steps': [
                    {'uses': 'actions/checkout@v3'},
                    {
                        'name': 'Set up Python ${{ matrix.python-version }}',
                        'uses': 'actions/setup-python@v4',
                        'with': {'python-version': '${{ matrix.python-version }}'}
                    },
                    {
                        'name': 'Install dependencies',
                        'run': 'pip install -r requirements.txt'
                    },
                    {
                        'name': 'Run tests',
                        'run': test_command
                    }
                ]
            }
        }
    }

    return yaml.dump(workflow, sort_keys=False)

# Generate workflow
workflow_yaml = create_test_workflow(['3.9', '3.10', '3.11'])
print(workflow_yaml)
```

**Result**: Programmatic workflow generation.

## KEY TAKEAWAYS

- **GitHub Actions**: CI/CD platform for automation
- **YAML Workflows**: Declarative pipeline definitions
- **Matrix Testing**: Test across multiple Python versions
- **Automated Testing**: Run tests on every push/PR
- **Integration**: Seamless Python ecosystem support
'''

# Lesson 253: Mocking and Stubbing - Test Doubles
lesson253 = next(l for l in lessons if l['id'] == 253)
lesson253['content'] = '''# Mocking and Stubbing - Test Doubles

Use test doubles to isolate code under test from external dependencies. Mocking and stubbing enable fast, reliable unit tests by replacing real objects with controlled substitutes. Python's unittest.mock provides powerful mocking capabilities.

## Example 1: Basic Mock with unittest.mock

Replace function with mock:

```python
from unittest.mock import Mock

# Create mock object
mock_api = Mock()
mock_api.get_user.return_value = {'id': 1, 'name': 'John'}

# Use mock
result = mock_api.get_user(123)
print(result)  # {'id': 1, 'name': 'John'}

# Verify mock was called
assert mock_api.get_user.called
assert mock_api.get_user.call_count == 1
mock_api.get_user.assert_called_once_with(123)
```

**Result**: Basic mocking.

## Example 2: Patch External Dependencies

Mock external calls in tests:

```python
from unittest.mock import patch
import requests

def get_user_data(user_id):
    """Fetch user from API."""
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

# Test with mock
@patch('requests.get')
def test_get_user_data(mock_get):
    # Setup mock response
    mock_response = Mock()
    mock_response.json.return_value = {'id': 1, 'name': 'Alice'}
    mock_get.return_value = mock_response

    # Call function
    result = get_user_data(1)

    # Assertions
    assert result['name'] == 'Alice'
    mock_get.assert_called_once_with('https://api.example.com/users/1')

test_get_user_data()
print("Test passed!")
```

**Result**: Patch external dependencies.

## KEY TAKEAWAYS

- **Mocking**: Replace real objects with test doubles
- **unittest.mock**: Built-in Python mocking library
- **patch**: Temporarily replace dependencies
- **return_value**: Control mock return values
- **Assertions**: Verify mock interactions
- **Isolation**: Test code without external dependencies
'''

# Lesson 254: Test Coverage - Metrics and Tools
lesson254 = next(l for l in lessons if l['id'] == 254)
lesson254['content'] = '''# Test Coverage - Metrics and Tools

Measure test coverage to identify untested code paths and improve test quality. Coverage tools analyze which lines, branches, and functions are executed during tests. Python's coverage.py provides comprehensive coverage measurement and reporting.

## Example 1: Basic Coverage with coverage.py

Measure test coverage:

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# test_calculator.py
import unittest
from calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    # divide not tested - coverage will show this

# Run with coverage:
# coverage run -m pytest
# coverage report
```

**Result**: Identify untested code.

## Example 2: Generate Coverage Report

Create coverage reports:

```python
import subprocess
import json

def generate_coverage_report():
    """Run tests with coverage and generate report."""
    # Run coverage
    subprocess.run(['coverage', 'run', '-m', 'pytest'])

    # Generate JSON report
    subprocess.run(['coverage', 'json'])

    # Read coverage data
    with open('coverage.json') as f:
        data = json.load(f)

    # Extract summary
    summary = {
        'total_statements': data['totals']['num_statements'],
        'covered_statements': data['totals']['covered_lines'],
        'missing_statements': data['totals']['missing_lines'],
        'coverage_percent': data['totals']['percent_covered']
    }

    return summary

summary = generate_coverage_report()
print(f"Coverage: {summary['coverage_percent']:.1f}%")
```

**Result**: Automated coverage reporting.

## KEY TAKEAWAYS

- **coverage.py**: Python coverage measurement tool
- **Line Coverage**: Track executed code lines
- **Branch Coverage**: Measure conditional path testing
- **Reports**: HTML, XML, JSON output formats
- **CI Integration**: Enforce coverage thresholds
- **Quality Metric**: Identify untested code paths
'''

# Lesson 255: AWS API Gateway - REST API Management
lesson255 = next(l for l in lessons if l['id'] == 255)
lesson255['content'] = '''# AWS API Gateway - REST API Management

Manage AWS API Gateway programmatically using Python and boto3. API Gateway enables creating, deploying, and managing REST and WebSocket APIs at scale. Python automation streamlines API lifecycle management, monitoring, and configuration.

## Example 1: Create REST API with boto3

Setup API Gateway client:

```python
import boto3

# Create API Gateway client
client = boto3.client('apigateway', region_name='us-east-1')

# Create REST API
response = client.create_rest_api(
    name='MyAPI',
    description='My REST API',
    endpointConfiguration={'types': ['REGIONAL']}
)

api_id = response['id']
print(f"Created API: {api_id}")
```

**Result**: Create API Gateway instance.

## Example 2: Add Resources and Methods

Build API structure:

```python
# Get root resource
resources = client.get_resources(restApiId=api_id)
root_id = resources['items'][0]['id']

# Create /users resource
users_resource = client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='users'
)

# Add GET method
client.put_method(
    restApiId=api_id,
    resourceId=users_resource['id'],
    httpMethod='GET',
    authorizationType='NONE'
)

print(f"Created /users GET endpoint")
```

**Result**: Add API resources and methods.

## KEY TAKEAWAYS

- **boto3**: AWS SDK for Python
- **REST API**: Create and manage APIs
- **Resources**: Define API endpoints
- **Methods**: HTTP methods for endpoints
- **Deployment**: Deploy API to stages
- **Monitoring**: CloudWatch integration
'''

# Lesson 256: AWS DynamoDB - NoSQL Database
lesson256 = next(l for l in lessons if l['id'] == 256)
lesson256['content'] = '''# AWS DynamoDB - NoSQL Database

Interact with AWS DynamoDB using Python boto3 SDK. DynamoDB is a fully managed NoSQL database service providing fast, predictable performance. Python enables CRUD operations, batch processing, and advanced querying of DynamoDB tables.

## Example 1: Create DynamoDB Table

Setup and create table:

```python
import boto3

# Create DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Create table
table = dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {'AttributeName': 'user_id', 'KeyType': 'HASH'}  # Partition key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'user_id', 'AttributeType': 'S'}
    ],
    BillingMode='PAY_PER_REQUEST'
)

# Wait for table creation
table.wait_until_exists()
print(f"Table created: {table.table_name}")
```

**Result**: Create DynamoDB table.

## Example 2: CRUD Operations

Basic database operations:

```python
# Put item
table.put_item(
    Item={
        'user_id': '123',
        'name': 'John Doe',
        'email': 'john@example.com',
        'age': 30
    }
)

# Get item
response = table.get_item(
    Key={'user_id': '123'}
)
user = response.get('Item')
print(f"User: {user['name']}")

# Update item
table.update_item(
    Key={'user_id': '123'},
    UpdateExpression='SET age = :age',
    ExpressionAttributeValues={':age': 31}
)

# Delete item
table.delete_item(
    Key={'user_id': '123'}
)
```

**Result**: Complete CRUD operations.

## KEY TAKEAWAYS

- **DynamoDB**: AWS NoSQL database service
- **boto3**: Python SDK for AWS
- **Tables**: Schema-less data storage
- **CRUD**: Create, Read, Update, Delete operations
- **Queries**: Efficient data retrieval
- **Batch Operations**: Process multiple items
'''

# Lesson 257: Ansible - Configuration Management
lesson257 = next(l for l in lessons if l['id'] == 257)
lesson257['content'] = '''# Ansible - Configuration Management

Automate infrastructure with Ansible using Python. Ansible enables declarative configuration management, application deployment, and task automation. Python can generate playbooks, invoke Ansible programmatically, and extend Ansible with custom modules.

## Example 1: Run Ansible Playbook from Python

Execute playbooks programmatically:

```python
import subprocess
import json

def run_playbook(playbook_path, inventory='localhost,', extra_vars=None):
    """Execute Ansible playbook."""
    cmd = [
        'ansible-playbook',
        playbook_path,
        '-i', inventory
    ]

    if extra_vars:
        cmd.extend(['--extra-vars', json.dumps(extra_vars)])

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    return {
        'returncode': result.returncode,
        'stdout': result.stdout,
        'stderr': result.stderr
    }

# Run playbook
result = run_playbook(
    'deploy.yml',
    inventory='hosts.ini',
    extra_vars={'env': 'production'}
)

if result['returncode'] == 0:
    print("Playbook executed successfully")
else:
    print(f"Error: {result['stderr']}")
```

**Result**: Programmatic playbook execution.

## Example 2: Generate Ansible Playbooks

Create playbooks with Python:

```python
import yaml

def create_deployment_playbook(servers, app_path):
    """Generate deployment playbook."""
    playbook = [
        {
            'name': 'Deploy Application',
            'hosts': 'all',
            'become': True,
            'tasks': [
                {
                    'name': 'Copy application files',
                    'copy': {
                        'src': app_path,
                        'dest': '/opt/app',
                        'mode': '0755'
                    }
                },
                {
                    'name': 'Restart service',
                    'service': {
                        'name': 'myapp',
                        'state': 'restarted'
                    }
                }
            ]
        }
    ]

    return yaml.dump(playbook, default_flow_style=False)

# Generate playbook
playbook_yaml = create_deployment_playbook(
    ['web1', 'web2'],
    '/path/to/app'
)

with open('deploy.yml', 'w') as f:
    f.write(playbook_yaml)

print("Playbook generated")
```

**Result**: Dynamic playbook generation.

## KEY TAKEAWAYS

- **Ansible**: Infrastructure automation tool
- **Playbooks**: YAML-based automation scripts
- **Modules**: Reusable automation units
- **Inventory**: Target host definitions
- **Idempotent**: Safe to run multiple times
- **Python Integration**: Generate and execute playbooks
'''

# Lesson 258: Async/Await - Concurrent Programming (replacing Java topic)
lesson258 = next(l for l in lessons if l['id'] == 258)
lesson258['title'] = "Async/Await - Concurrent Programming"
lesson258['content'] = '''# Async/Await - Concurrent Programming

Write asynchronous code using Python's async/await syntax. Async programming enables concurrent execution of I/O-bound operations without threading complexity. Python's asyncio provides event loop, coroutines, and async primitives for efficient concurrency.

## Example 1: Basic Async Function

Create and run coroutines:

```python
import asyncio

async def fetch_data(id):
    """Simulate async data fetch."""
    await asyncio.sleep(1)  # Simulate I/O operation
    return f"Data for {id}"

# Run coroutine
async def main():
    result = await fetch_data(123)
    print(result)  # Data for 123

# Execute
asyncio.run(main())
```

**Result**: Basic async/await usage.

## Example 2: Concurrent Execution

Run multiple tasks concurrently:

```python
import asyncio
import time

async def task(name, delay):
    """Async task with delay."""
    print(f"{name}: Starting")
    await asyncio.sleep(delay)
    print(f"{name}: Done")
    return f"{name} result"

async def main():
    # Run concurrently
    start = time.time()

    results = await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 1),
        task("Task 3", 3)
    )

    elapsed = time.time() - start
    print(f"All tasks done in {elapsed:.1f}s")
    print(f"Results: {results}")

asyncio.run(main())
# Tasks run concurrently, total time ~3s not 6s
```

**Result**: Concurrent task execution.

## KEY TAKEAWAYS

- **async/await**: Python async syntax
- **Coroutines**: Async functions
- **Event Loop**: Manages async execution
- **asyncio.gather**: Run tasks concurrently
- **I/O-Bound**: Best for network/file operations
- **Non-Blocking**: Efficient resource usage
'''

# Lesson 259: Contract Testing - API Contracts
lesson259 = next(l for l in lessons if l['id'] == 259)
lesson259['content'] = '''# Contract Testing - API Contracts

Verify API contracts between services using contract testing. Contract tests ensure API providers and consumers agree on interfaces, preventing integration failures. Python's pact-python enables consumer-driven contract testing for microservices.

## Example 1: Consumer Contract Test

Define consumer expectations:

```python
from pact import Consumer, Provider

# Define consumer expectations
pact = Consumer('UserService').has_pact_with(Provider('AuthAPI'))

# Define expected interaction
pact.given(
    'user exists'
).upon_receiving(
    'a request for user details'
).with_request(
    'GET', '/users/123'
).will_respond_with(200, body={
    'id': '123',
    'name': 'John Doe'
})

# Test consumer code
with pact:
    # Your API client code
    response = api_client.get_user('123')
    assert response['name'] == 'John Doe'

# Generates pact file for provider verification
```

**Result**: Consumer-driven contract.

## Example 2: Schema Validation

Validate API responses:

```python
from jsonschema import validate

# Define expected schema
user_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'email': {'type': 'string', 'format': 'email'}
    },
    'required': ['id', 'name']
}

# Validate response
def test_user_api():
    response = api.get('/users/123')
    validate(instance=response.json(), schema=user_schema)
    print("Response matches contract")
```

**Result**: Schema-based validation.

## KEY TAKEAWAYS

- **Contract Testing**: Verify API agreements
- **Consumer-Driven**: Consumers define expectations
- **Pact**: Contract testing framework
- **Schema Validation**: JSON Schema validation
- **Microservices**: Essential for service integration
- **Early Detection**: Find integration issues early
'''

# Lesson 260: Database Migration - Flyway/Liquibase
lesson260 = next(l for l in lessons if l['id'] == 260)
lesson260['content'] = '''# Database Migration - Flyway/Liquibase

Manage database schema changes with migration tools using Python. Database migrations enable versioned, repeatable schema evolution. Python can integrate with Flyway, Liquibase, and Alembic for automated database change management.

## Example 1: Alembic Migration Setup

Python-native database migrations:

```python
# Install: pip install alembic sqlalchemy

# Initialize Alembic
# alembic init migrations

# Create migration
from alembic import op
import sqlalchemy as sa

def upgrade():
    """Create users table."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100)),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )

def downgrade():
    """Drop users table."""
    op.drop_table('users')

# Run migration: alembic upgrade head
```

**Result**: Versioned schema migrations.

## Example 2: Run Migrations Programmatically

Execute migrations from Python:

```python
from alembic.config import Config
from alembic import command

def run_migrations(config_path='alembic.ini'):
    """Run pending migrations."""
    alembic_cfg = Config(config_path)

    # Upgrade to latest
    command.upgrade(alembic_cfg, 'head')
    print("Migrations applied")

# Check current version
def get_current_version():
    """Get current migration version."""
    alembic_cfg = Config('alembic.ini')
    command.current(alembic_cfg)

# Usage
run_migrations()
```

**Result**: Programmatic migration management.

## KEY TAKEAWAYS

- **Migrations**: Versioned database changes
- **Alembic**: Python migration tool
- **SQLAlchemy**: Database abstraction layer
- **Upgrade/Downgrade**: Bidirectional migrations
- **Version Control**: Track schema evolution
- **Automation**: CI/CD integration
'''

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created comprehensive unique content for lessons 252-260:")
for lid in range(252, 261):
    lesson = next(l for l in lessons if l['id'] == lid)
    chars = len(lesson['content'])
    print(f"  {lid}: {lesson['title'][:45]:45s} {chars:5,d} chars")
