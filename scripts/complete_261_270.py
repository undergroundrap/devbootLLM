#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 261: Environment Configuration
lesson261 = next(l for l in lessons if l['id'] == 261)
lesson261['content'] = '''# Environment Configuration

Manage application configuration across development, staging, and production environments using environment variables, config files, and best practices. Proper environment configuration enables secure credential management, feature toggling, and environment-specific behavior without code changes.

## Example 1: Basic Environment Variables

Access environment variables in Python:

```python
import os

# Get environment variables
environment = os.getenv('ENVIRONMENT', 'development')
debug_mode = os.getenv('DEBUG', 'False') == 'True'
api_key = os.getenv('API_KEY')

print(f"Environment: {environment}")
print(f"Debug mode: {debug_mode}")
print(f"API key present: {api_key is not None}")

# Set environment variable (for current process only)
os.environ['APP_NAME'] = 'MyApp'
print(f"App name: {os.environ.get('APP_NAME')}")
```

**Result**: Access and set environment-specific configuration.

## Example 2: .env File with Manual Parsing

Parse .env files without external dependencies:

```python
import os

def load_env_file(filepath='.env'):
    """Load environment variables from .env file."""
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue

            # Parse KEY=VALUE
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()

                # Remove quotes if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]

                os.environ[key] = value

# Load .env file
load_env_file('.env')

# Access loaded variables
database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
print(f"Database URL: {database_url}")
```

**Result**: Load configuration from .env files.

## Example 3: Environment-Specific Config Classes

Create config objects for each environment:

```python
import os

class Config:
    """Base configuration."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    DATABASE_URL = 'sqlite:///dev.db'

class StagingConfig(Config):
    """Staging configuration."""
    DATABASE_URL = os.getenv('STAGING_DATABASE_URL')

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    DATABASE_URL = os.getenv('PROD_DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')  # Must be set

# Config factory
config_map = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}

def get_config():
    """Get config for current environment."""
    env = os.getenv('ENVIRONMENT', 'development')
    return config_map.get(env, DevelopmentConfig)

# Usage
config = get_config()
print(f"Debug mode: {config.DEBUG}")
print(f"Database: {config.DATABASE_URL}")
```

**Result**: Environment-specific configuration classes.

## Example 4: Configuration Validation

Validate required configuration on startup:

```python
import os
import sys

class ConfigValidator:
    def __init__(self, environment):
        self.environment = environment
        self.errors = []

    def require(self, key, message=None):
        """Require environment variable to be set."""
        value = os.getenv(key)
        if not value:
            error = message or f"Required environment variable '{key}' not set"
            self.errors.append(error)
        return value

    def require_in_production(self, key, message=None):
        """Require variable only in production."""
        if self.environment == 'production':
            return self.require(key, message)
        return os.getenv(key)

    def validate(self):
        """Validate configuration and exit if errors."""
        if self.errors:
            print("Configuration errors:")
            for error in self.errors:
                print(f"  - {error}")
            sys.exit(1)

# Usage
env = os.getenv('ENVIRONMENT', 'development')
validator = ConfigValidator(env)

# Required in all environments
validator.require('DATABASE_URL', 'Database URL must be configured')

# Required only in production
validator.require_in_production('SECRET_KEY', 'Secret key required in production')
validator.require_in_production('API_KEY', 'API key required in production')

# Validate
validator.validate()
print("Configuration valid!")
```

**Result**: Startup configuration validation.

## Example 5: Feature Flags

Toggle features by environment:

```python
import os

class FeatureFlags:
    def __init__(self):
        self.environment = os.getenv('ENVIRONMENT', 'development')

    def is_enabled(self, feature_name):
        """Check if feature is enabled."""
        # Check explicit environment variable
        env_var = f"FEATURE_{feature_name.upper()}"
        value = os.getenv(env_var)

        if value is not None:
            return value.lower() in ('true', '1', 'yes', 'on')

        # Default feature states by environment
        defaults = {
            'development': {
                'new_ui': True,
                'analytics': False,
                'premium_features': True
            },
            'staging': {
                'new_ui': True,
                'analytics': True,
                'premium_features': True
            },
            'production': {
                'new_ui': False,
                'analytics': True,
                'premium_features': True
            }
        }

        env_defaults = defaults.get(self.environment, {})
        return env_defaults.get(feature_name, False)

# Usage
flags = FeatureFlags()

if flags.is_enabled('new_ui'):
    print("Using new UI")
else:
    print("Using legacy UI")

if flags.is_enabled('analytics'):
    print("Analytics enabled")
```

**Result**: Environment-based feature toggling.

## Example 6: Multi-File Configuration

Load configuration from multiple sources:

```python
import os
import json

class ConfigLoader:
    def __init__(self):
        self.config = {}

    def load_from_file(self, filepath):
        """Load configuration from JSON file."""
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                file_config = json.load(f)
                self.config.update(file_config)

    def load_from_env(self, prefix='APP_'):
        """Load configuration from environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self.config[config_key] = value

    def get(self, key, default=None):
        """Get configuration value."""
        return self.config.get(key, default)

    def get_int(self, key, default=0):
        """Get integer configuration value."""
        value = self.get(key)
        if value is None:
            return default
        try:
            return int(value)
        except ValueError:
            return default

# Usage
loader = ConfigLoader()

# Load base config
loader.load_from_file('config/base.json')

# Load environment-specific config (overrides base)
env = os.getenv('ENVIRONMENT', 'development')
loader.load_from_file(f'config/{env}.json')

# Environment variables override file config
loader.load_from_env('APP_')

# Access config
port = loader.get_int('port', 8000)
host = loader.get('host', '0.0.0.0')
print(f"Server: {host}:{port}")
```

**Result**: Multi-source configuration loading with precedence.

## Example 7: Secrets Management

Safely handle sensitive configuration:

```python
import os
import json
from pathlib import Path

class SecretsManager:
    def __init__(self):
        self.secrets = {}
        self._load_secrets()

    def _load_secrets(self):
        """Load secrets from various sources."""
        # 1. Environment variables (highest priority)
        self.secrets['database_password'] = os.getenv('DATABASE_PASSWORD')
        self.secrets['api_key'] = os.getenv('API_KEY')
        self.secrets['secret_key'] = os.getenv('SECRET_KEY')

        # 2. Secrets file (if exists, lower priority)
        secrets_file = Path('.secrets.json')
        if secrets_file.exists():
            with open(secrets_file, 'r') as f:
                file_secrets = json.load(f)
                for key, value in file_secrets.items():
                    if key not in self.secrets or self.secrets[key] is None:
                        self.secrets[key] = value

    def get(self, key):
        """Get secret value."""
        value = self.secrets.get(key)
        if value is None:
            raise ValueError(f"Secret '{key}' not configured")
        return value

    def get_optional(self, key, default=None):
        """Get optional secret."""
        return self.secrets.get(key, default)

# Usage
secrets = SecretsManager()

# Required secrets
db_password = secrets.get('database_password')

# Optional secrets
analytics_key = secrets.get_optional('analytics_key')
```

**Result**: Secure secrets management.

## Example 8: Configuration Schema

Define and validate configuration schema:

```python
import os

class ConfigSchema:
    def __init__(self):
        self.schema = {
            'database_url': {
                'type': str,
                'required': True,
                'env': 'DATABASE_URL'
            },
            'port': {
                'type': int,
                'required': False,
                'default': 8000,
                'env': 'PORT'
            },
            'debug': {
                'type': bool,
                'required': False,
                'default': False,
                'env': 'DEBUG'
            },
            'max_connections': {
                'type': int,
                'required': False,
                'default': 100,
                'env': 'MAX_CONNECTIONS',
                'validator': lambda x: x > 0
            }
        }

    def load(self):
        """Load and validate configuration."""
        config = {}
        errors = []

        for key, spec in self.schema.items():
            env_var = spec['env']
            value = os.getenv(env_var)

            # Check required
            if value is None:
                if spec.get('required'):
                    errors.append(f"Required config '{key}' not set")
                    continue
                value = spec.get('default')

            # Type conversion
            if value is not None:
                try:
                    if spec['type'] == bool:
                        value = value.lower() in ('true', '1', 'yes')
                    elif spec['type'] == int:
                        value = int(value)
                    elif spec['type'] == str:
                        value = str(value)
                except ValueError:
                    errors.append(f"Invalid type for '{key}'")
                    continue

            # Custom validation
            validator = spec.get('validator')
            if validator and not validator(value):
                errors.append(f"Validation failed for '{key}'")
                continue

            config[key] = value

        if errors:
            raise ValueError(f"Configuration errors: {', '.join(errors)}")

        return config

# Usage
schema = ConfigSchema()
config = schema.load()
print(f"Port: {config['port']}")
print(f"Debug: {config['debug']}")
```

**Result**: Schema-based configuration validation.

## Example 9: Environment Detection

Auto-detect environment from various signals:

```python
import os
import socket

class EnvironmentDetector:
    @staticmethod
    def detect():
        """Detect current environment."""
        # 1. Explicit environment variable
        env = os.getenv('ENVIRONMENT') or os.getenv('ENV')
        if env:
            return env.lower()

        # 2. Check for production indicators
        if os.getenv('PRODUCTION') == '1':
            return 'production'

        # 3. Check hostname patterns
        hostname = socket.gethostname().lower()
        if 'prod' in hostname:
            return 'production'
        elif 'staging' in hostname or 'stg' in hostname:
            return 'staging'
        elif 'dev' in hostname:
            return 'development'

        # 4. Check for CI environment
        if os.getenv('CI') == 'true':
            return 'ci'

        # 5. Default to development
        return 'development'

    @staticmethod
    def is_production():
        """Check if running in production."""
        return EnvironmentDetector.detect() == 'production'

    @staticmethod
    def is_development():
        """Check if running in development."""
        return EnvironmentDetector.detect() == 'development'

# Usage
detector = EnvironmentDetector()
env = detector.detect()
print(f"Detected environment: {env}")

if detector.is_production():
    print("Running in production mode")
else:
    print("Running in non-production mode")
```

**Result**: Automatic environment detection.

## Example 10: Production Configuration Manager

Complete configuration management system:

```python
import os
import json
from typing import Any, Dict, Optional
from pathlib import Path

class ConfigurationManager:
    def __init__(self, env: Optional[str] = None):
        self.env = env or os.getenv('ENVIRONMENT', 'development')
        self.config: Dict[str, Any] = {}
        self._load_configuration()

    def _load_configuration(self):
        """Load configuration from all sources."""
        # 1. Load defaults
        self._load_defaults()

        # 2. Load base config file
        self._load_file('config/base.json')

        # 3. Load environment-specific file
        self._load_file(f'config/{self.env}.json')

        # 4. Load .env file
        self._load_env_file('.env')
        self._load_env_file(f'.env.{self.env}')

        # 5. Environment variables override all
        self._load_env_vars()

    def _load_defaults(self):
        """Set default configuration values."""
        self.config = {
            'debug': False,
            'port': 8000,
            'host': '0.0.0.0',
            'log_level': 'INFO',
            'max_connections': 100,
            'timeout': 30
        }

    def _load_file(self, filepath: str):
        """Load configuration from JSON file."""
        path = Path(filepath)
        if path.exists():
            with open(path, 'r') as f:
                data = json.load(f)
                self.config.update(data)

    def _load_env_file(self, filepath: str):
        """Load environment variables from .env file."""
        path = Path(filepath)
        if not path.exists():
            return

        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip().lower()
                    value = value.strip().strip('"').strip("'")
                    self.config[key] = value

    def _load_env_vars(self, prefix: str = 'APP_'):
        """Load environment variables with prefix."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self.config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        return self.config.get(key, default)

    def get_int(self, key: str, default: int = 0) -> int:
        """Get integer configuration value."""
        value = self.get(key, default)
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    def get_bool(self, key: str, default: bool = False) -> bool:
        """Get boolean configuration value."""
        value = self.get(key, default)
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ('true', '1', 'yes', 'on')
        return default

    def require(self, key: str) -> Any:
        """Get required configuration value."""
        value = self.get(key)
        if value is None:
            raise ValueError(f"Required configuration '{key}' not set")
        return value

    def is_production(self) -> bool:
        """Check if running in production."""
        return self.env == 'production'

    def is_development(self) -> bool:
        """Check if running in development."""
        return self.env == 'development'

# Usage
config = ConfigurationManager()

# Get configuration values
debug = config.get_bool('debug', False)
port = config.get_int('port', 8000)
database_url = config.require('database_url')

print(f"Environment: {config.env}")
print(f"Debug: {debug}")
print(f"Port: {port}")
print(f"Database: {database_url}")

# Environment checks
if config.is_production():
    print("Production mode: Extra security enabled")
```

**Result**: Production-ready configuration management.

## KEY TAKEAWAYS

- **Environment Variables**: Use os.getenv() for environment-specific config
- **Multi-Source Loading**: Combine files, .env, and env vars with precedence
- **Validation**: Validate required configuration on startup
- **Type Safety**: Convert and validate types (str, int, bool)
- **Secrets Management**: Keep sensitive data separate from code
- **Feature Flags**: Toggle features by environment
- **Environment Detection**: Auto-detect from hostname, env vars, CI
- **Configuration Classes**: Use environment-specific config classes
- **Defaults**: Provide sensible defaults for non-required values
- **Best Practices**: Never commit secrets, use .env files, validate early
'''

# Lesson 262: Filter Evens
lesson262 = next(l for l in lessons if l['id'] == 262)
lesson262['content'] = '''# Filter Evens

Filter even numbers from collections using list comprehensions, filter(), and loops. Filtering is a fundamental operation for data processing, validation, and transformation. Understanding filtering patterns enables efficient data manipulation and functional programming techniques.

## Example 1: Basic List Comprehension

Filter evens using comprehension:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# One-liner
evens = [n for n in range(1, 11) if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]
```

**Result**: List comprehension for filtering evens.

## Example 2: Using filter() Function

Filter with built-in filter():

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() with lambda
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Using filter() with function
def is_even(n):
    return n % 2 == 0

evens = list(filter(is_even, numbers))
print(evens)  # [2, 4, 6, 8, 10]
```

**Result**: filter() function for functional filtering.

## Example 3: Manual Loop Filtering

Traditional loop approach:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Manual filtering
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

print(evens)  # [2, 4, 6, 8, 10]

# Count evens without storing
count = 0
for n in numbers:
    if n % 2 == 0:
        count += 1

print(f"Even count: {count}")  # 5
```

**Result**: Traditional loop-based filtering.

## Example 4: Filter and Transform

Filter and modify simultaneously:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter evens and square them
even_squares = [n**2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# Filter and format
even_strings = [f"Even: {n}" for n in numbers if n % 2 == 0]
print(even_strings)  # ['Even: 2', 'Even: 4', ...]

# Filter evens, double them
doubled_evens = [n * 2 for n in numbers if n % 2 == 0]
print(doubled_evens)  # [4, 8, 12, 16, 20]
```

**Result**: Combined filtering and transformation.

## Example 5: Filter with Multiple Conditions

Complex filtering criteria:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20]

# Even AND greater than 5
filtered = [n for n in numbers if n % 2 == 0 and n > 5]
print(filtered)  # [6, 8, 10, 12, 20]

# Even OR divisible by 3
filtered = [n for n in numbers if n % 2 == 0 or n % 3 == 0]
print(filtered)  # [2, 3, 4, 6, 8, 9, 10, 12, 15, 20]

# Even and divisible by 3 (divisible by 6)
filtered = [n for n in numbers if n % 2 == 0 and n % 3 == 0]
print(filtered)  # [6, 12]
```

**Result**: Multi-condition filtering.

## Example 6: Filter from Generator

Memory-efficient filtering:

```python
# Generator for evens (lazy evaluation)
def even_generator(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

# Use generator
numbers = range(1, 1000000)  # Large range
evens = even_generator(numbers)

# Consume first 5 evens
first_five = []
for i, n in enumerate(evens):
    if i >= 5:
        break
    first_five.append(n)

print(first_five)  # [2, 4, 6, 8, 10]

# Generator expression
evens_gen = (n for n in range(1, 100) if n % 2 == 0)
print(list(evens_gen)[:5])  # [2, 4, 6, 8, 10]
```

**Result**: Memory-efficient generator filtering.

## Example 7: Filter Nested Structures

Filter in nested lists:

```python
# 2D list filtering
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Filter evens from all rows
evens = [n for row in matrix for n in row if n % 2 == 0]
print(evens)  # [2, 4, 6, 8]

# Filter rows containing evens
rows_with_evens = [
    row for row in matrix
    if any(n % 2 == 0 for n in row)
]
print(rows_with_evens)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Filter only even rows (all elements even)
even_rows = [
    row for row in matrix
    if all(n % 2 == 0 for n in row)
]
print(even_rows)  # []
```

**Result**: Filtering in nested structures.

## Example 8: Filter Dictionaries

Filter dict keys/values:

```python
data = {
    'a': 1, 'b': 2, 'c': 3,
    'd': 4, 'e': 5, 'f': 6
}

# Filter dict by even values
even_items = {k: v for k, v in data.items() if v % 2 == 0}
print(even_items)  # {'b': 2, 'd': 4, 'f': 6}

# Get only even values (as list)
even_values = [v for v in data.values() if v % 2 == 0]
print(even_values)  # [2, 4, 6]

# Get keys with even values
even_keys = [k for k, v in data.items() if v % 2 == 0]
print(even_keys)  # ['b', 'd', 'f']
```

**Result**: Dictionary filtering.

## Example 9: Filter with Index

Access index during filtering:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter evens with their original index
evens_with_index = [
    (i, n) for i, n in enumerate(numbers)
    if n % 2 == 0
]
print(evens_with_index)
# [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# Filter by even index position
even_position = [
    n for i, n in enumerate(numbers)
    if i % 2 == 0
]
print(even_position)  # [1, 3, 5, 7, 9]

# Filter even numbers at even positions
even_at_even = [
    n for i, n in enumerate(numbers)
    if i % 2 == 0 and n % 2 == 0
]
print(even_at_even)  # []
```

**Result**: Index-aware filtering.

## Example 10: Production Filtering Utility

Complete filtering library:

```python
from typing import Callable, Iterable, List, TypeVar

T = TypeVar('T')

class FilterUtils:
    @staticmethod
    def filter_evens(numbers: Iterable[int]) -> List[int]:
        """Filter even numbers from iterable."""
        return [n for n in numbers if n % 2 == 0]

    @staticmethod
    def filter_odds(numbers: Iterable[int]) -> List[int]:
        """Filter odd numbers from iterable."""
        return [n for n in numbers if n % 2 != 0]

    @staticmethod
    def filter_divisible(numbers: Iterable[int], divisor: int) -> List[int]:
        """Filter numbers divisible by divisor."""
        if divisor == 0:
            raise ValueError("Divisor cannot be zero")
        return [n for n in numbers if n % divisor == 0]

    @staticmethod
    def filter_range(numbers: Iterable[int], min_val: int, max_val: int) -> List[int]:
        """Filter numbers within range [min_val, max_val]."""
        return [n for n in numbers if min_val <= n <= max_val]

    @staticmethod
    def filter_by(items: Iterable[T], predicate: Callable[[T], bool]) -> List[T]:
        """Generic filter by predicate function."""
        return [item for item in items if predicate(item)]

    @staticmethod
    def partition_evens(numbers: Iterable[int]) -> tuple:
        """Partition into evens and odds."""
        evens = []
        odds = []
        for n in numbers:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        return evens, odds

    @staticmethod
    def filter_unique_evens(numbers: Iterable[int]) -> List[int]:
        """Filter unique even numbers, preserving order."""
        seen = set()
        result = []
        for n in numbers:
            if n % 2 == 0 and n not in seen:
                seen.add(n)
                result.append(n)
        return result

# Usage
utils = FilterUtils()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4]

# Filter evens
evens = utils.filter_evens(numbers)
print(f"Evens: {evens}")

# Filter by custom predicate
multiples_of_3 = utils.filter_by(numbers, lambda n: n % 3 == 0)
print(f"Multiples of 3: {multiples_of_3}")

# Partition
evens, odds = utils.partition_evens(numbers)
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# Unique evens
unique_evens = utils.filter_unique_evens(numbers)
print(f"Unique evens: {unique_evens}")
```

**Result**: Production filtering utilities.

## KEY TAKEAWAYS

- **List Comprehension**: [n for n in nums if n % 2 == 0] - Most Pythonic
- **filter() Function**: filter(lambda n: n % 2 == 0, nums) - Functional style
- **Manual Loops**: Traditional approach with explicit control
- **Generator Expressions**: (n for n in nums if ...) - Memory efficient
- **Transform While Filtering**: [n**2 for n in nums if ...] - Combined ops
- **Multiple Conditions**: Use and/or for complex criteria
- **Nested Filtering**: Flatten nested structures while filtering
- **Dictionary Filtering**: {k: v for k, v in d.items() if ...}
- **Index Access**: enumerate() for index-aware filtering
- **Partitioning**: Split into matching/non-matching groups
'''

# Lesson 263: GitHub Actions CI Pipeline
lesson263 = next(l for l in lessons if l['id'] == 263)
lesson263['content'] = '''# GitHub Actions CI Pipeline

Automate testing, building, and deployment using GitHub Actions CI/CD workflows. GitHub Actions enables continuous integration and delivery directly in your repository, triggering automated workflows on push, pull request, schedule, or manual dispatch.

## Example 1: Basic Workflow Structure

Create a simple GitHub Actions workflow:

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          python -m pytest tests/
```

**Result**: Basic CI workflow for Python project.

## Example 2: Matrix Testing

Test across multiple Python versions:

```yaml
# .github/workflows/test-matrix.yml
name: Test Matrix

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.9', '3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest

      - name: Run tests
        run: pytest tests/ -v
```

**Result**: Test across OS and Python versions.

## Example 3: Caching Dependencies

Speed up workflows with caching:

```yaml
# .github/workflows/cached-ci.yml
name: CI with Caching

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Cache pip packages
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

**Result**: Cached dependencies for faster builds.

## Example 4: Conditional Workflows

Run jobs conditionally:

```yaml
# .github/workflows/conditional.yml
name: Conditional Deployment

on:
  push:
    branches: [ main ]
    tags:
      - 'v*'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: pytest

  deploy:
    runs-on: ubuntu-latest
    needs: test
    if: startsWith(github.ref, 'refs/tags/v')

    steps:
      - uses: actions/checkout@v3

      - name: Deploy to production
        run: |
          echo "Deploying version ${{ github.ref_name }}"
          # Deployment commands here
```

**Result**: Deploy only on tags after tests pass.

## Example 5: Environment Variables and Secrets

Use secrets and environment variables:

```yaml
# .github/workflows/secrets.yml
name: Deploy with Secrets

on:
  push:
    branches: [ main ]

env:
  PYTHON_VERSION: '3.11'
  ENVIRONMENT: production

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Deploy to AWS
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_REGION: us-east-1
        run: |
          pip install boto3
          python deploy.py
```

**Result**: Secure credential management in workflows.

## Example 6: Artifact Upload and Download

Share files between jobs:

```yaml
# .github/workflows/artifacts.yml
name: Build and Test Artifacts

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Build application
        run: |
          python setup.py build
          mkdir -p dist
          cp -r build/lib dist/

      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: build-output
          path: dist/
          retention-days: 5

  test:
    runs-on: ubuntu-latest
    needs: build

    steps:
      - uses: actions/checkout@v3

      - name: Download artifact
        uses: actions/download-artifact@v3
        with:
          name: build-output
          path: dist/

      - name: Test build
        run: |
          python -m pytest tests/
```

**Result**: Share build artifacts between jobs.

## Example 7: Scheduled Workflows

Run workflows on schedule:

```yaml
# .github/workflows/scheduled.yml
name: Nightly Build

on:
  schedule:
    # Run at 2 AM UTC every day
    - cron: '0 2 * * *'
  workflow_dispatch:  # Allow manual trigger

jobs:
  nightly-test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run comprehensive tests
        run: |
          pytest tests/ --slow --integration -v

      - name: Generate report
        if: always()
        run: |
          pytest tests/ --junitxml=report.xml

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: test-results
          path: report.xml
```

**Result**: Scheduled nightly testing.

## Example 8: Multi-Job Pipeline

Complex pipeline with dependencies:

```yaml
# .github/workflows/pipeline.yml
name: Full Pipeline

on:
  push:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Lint code
        run: |
          pip install flake8 black
          flake8 src/
          black --check src/

  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Run tests
        run: |
          pip install pytest pytest-cov
          pytest --cov=src tests/

  build:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Build package
        run: |
          pip install build
          python -m build
      - uses: actions/upload-artifact@v3
        with:
          name: package
          path: dist/

  deploy:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/download-artifact@v3
        with:
          name: package
      - name: Deploy
        run: echo "Deploying to production"
```

**Result**: Multi-stage pipeline with dependencies.

## Example 9: Status Badges and Notifications

Add status badges and notifications:

```yaml
# .github/workflows/notify.yml
name: CI with Notifications

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

      - name: Run tests
        id: tests
        run: |
          pip install pytest
          pytest tests/

      - name: Create status badge
        if: always()
        run: |
          if [ "${{ steps.tests.outcome }}" == "success" ]; then
            echo "Tests passed ✓" >> $GITHUB_STEP_SUMMARY
          else
            echo "Tests failed ✗" >> $GITHUB_STEP_SUMMARY
          fi
```

Add to README.md:
```markdown
![CI Status](https://github.com/username/repo/workflows/CI%20with%20Notifications/badge.svg)
```

**Result**: Visual status indicators and summaries.

## Example 10: Production CI/CD Pipeline

Complete enterprise-grade pipeline:

```yaml
# .github/workflows/production.yml
name: Production CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  release:
    types: [created]

env:
  PYTHON_VERSION: '3.11'
  CACHE_VERSION: v1

jobs:
  quality-checks:
    name: Code Quality
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Cache dependencies
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ env.CACHE_VERSION }}-${{ hashFiles('**/requirements*.txt') }}

      - name: Install linting tools
        run: |
          pip install flake8 black isort mypy pylint

      - name: Run linters
        run: |
          echo "Running flake8..."
          flake8 src/ tests/ --max-line-length=100

          echo "Checking formatting..."
          black --check src/ tests/

          echo "Checking imports..."
          isort --check-only src/ tests/

          echo "Running type checks..."
          mypy src/

  test:
    name: Test Suite
    runs-on: ${{ matrix.os }}
    needs: quality-checks

    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ['3.9', '3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      - name: Cache dependencies
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ matrix.os }}-py${{ matrix.python-version }}-${{ hashFiles('**/requirements*.txt') }}

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov pytest-xdist

      - name: Run tests with coverage
        run: |
          pytest tests/ \
            --cov=src \
            --cov-report=xml \
            --cov-report=html \
            --junitxml=junit.xml \
            -n auto \
            -v

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml
          flags: ${{ matrix.os }}-py${{ matrix.python-version }}

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: test-results-${{ matrix.os }}-${{ matrix.python-version }}
          path: |
            junit.xml
            htmlcov/

  build:
    name: Build Package
    runs-on: ubuntu-latest
    needs: test

    steps:
      - uses: actions/checkout@v3

      - uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install build tools
        run: pip install build twine

      - name: Build package
        run: python -m build

      - name: Check package
        run: twine check dist/*

      - name: Upload distribution
        uses: actions/upload-artifact@v3
        with:
          name: dist
          path: dist/

  deploy-staging:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/develop'
    environment:
      name: staging
      url: https://staging.example.com

    steps:
      - uses: actions/checkout@v3

      - uses: actions/download-artifact@v3
        with:
          name: dist
          path: dist/

      - name: Deploy to staging
        env:
          DEPLOY_KEY: ${{ secrets.STAGING_DEPLOY_KEY }}
        run: |
          echo "Deploying to staging environment"
          # Add deployment commands

  deploy-production:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: build
    if: github.event_name == 'release'
    environment:
      name: production
      url: https://example.com

    steps:
      - uses: actions/checkout@v3

      - uses: actions/download-artifact@v3
        with:
          name: dist
          path: dist/

      - name: Deploy to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: |
          pip install twine
          twine upload dist/*

      - name: Create deployment summary
        run: |
          echo "## Deployment Summary" >> $GITHUB_STEP_SUMMARY
          echo "Version: ${{ github.ref_name }}" >> $GITHUB_STEP_SUMMARY
          echo "Environment: Production" >> $GITHUB_STEP_SUMMARY
          echo "Status: ✓ Deployed" >> $GITHUB_STEP_SUMMARY
```

**Result**: Enterprise-grade CI/CD pipeline.

## KEY TAKEAWAYS

- **Workflow Triggers**: on: [push, pull_request, schedule, workflow_dispatch]
- **Job Dependencies**: needs: [job1, job2] for sequential execution
- **Matrix Builds**: Test across multiple OS/versions simultaneously
- **Caching**: actions/cache for faster builds
- **Secrets**: ${{ secrets.SECRET_NAME }} for secure credentials
- **Artifacts**: Upload/download build outputs between jobs
- **Conditionals**: if: conditions for selective execution
- **Environments**: Define staging/production with protection rules
- **Status Checks**: Required checks for PR merging
- **Best Practices**: Fail-fast, parallel execution, comprehensive testing
'''

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Lesson 264: GitLab CI/CD
lesson264 = next(l for l in lessons if l['id'] == 264)
lesson264['content'] = '''# GitLab CI/CD

Automate build, test, and deployment pipelines using GitLab CI/CD with .gitlab-ci.yml configuration. GitLab CI/CD provides integrated continuous integration and deployment directly in GitLab repositories with powerful features like Auto DevOps, container registry, and Kubernetes integration.

## Example 1: Basic Pipeline Structure

Create a simple GitLab CI pipeline:

```yaml
# .gitlab-ci.yml
stages:
  - test
  - build
  - deploy

variables:
  PYTHON_VERSION: "3.11"

before_script:
  - python --version
  - pip install --upgrade pip

test:
  stage: test
  image: python:${PYTHON_VERSION}
  script:
    - pip install -r requirements.txt
    - pip install pytest pytest-cov
    - pytest tests/ --cov=src
  coverage: '/TOTAL.*\\s+(\\d+%)$/'

build:
  stage: build
  image: python:${PYTHON_VERSION}
  script:
    - pip install build
    - python -m build
  artifacts:
    paths:
      - dist/
    expire_in: 1 week

deploy:
  stage: deploy
  script:
    - echo "Deploying application"
  only:
    - main
```

**Result**: Basic three-stage GitLab CI pipeline.

## Example 2: Multi-Environment Deployment

Deploy to different environments:

```yaml
# .gitlab-ci.yml
stages:
  - test
  - deploy-staging
  - deploy-production

test:
  stage: test
  image: python:3.11
  script:
    - pip install pytest
    - pytest tests/

deploy-staging:
  stage: deploy-staging
  environment:
    name: staging
    url: https://staging.example.com
  script:
    - echo "Deploying to staging"
    - pip install -r requirements.txt
    - python deploy.py --env=staging
  only:
    - develop

deploy-production:
  stage: deploy-production
  environment:
    name: production
    url: https://example.com
  script:
    - echo "Deploying to production"
    - python deploy.py --env=production
  only:
    - main
  when: manual
```

**Result**: Environment-specific deployments.

## Example 3: Docker Integration

Build and push Docker images:

```yaml
# .gitlab-ci.yml with Docker
stages:
  - build
  - test
  - push

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
  DOCKER_IMAGE_LATEST: $CI_REGISTRY_IMAGE:latest

build-docker:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker tag $DOCKER_IMAGE $DOCKER_IMAGE_LATEST
    - docker push $DOCKER_IMAGE
    - docker push $DOCKER_IMAGE_LATEST

test-docker:
  stage: test
  image: $DOCKER_IMAGE
  script:
    - pytest tests/
```

**Result**: Docker-based CI/CD pipeline.

## Example 4: Parallel Testing

Run tests in parallel:

```yaml
# .gitlab-ci.yml with parallel jobs
stages:
  - test

test-unit:
  stage: test
  image: python:3.11
  script:
    - pip install pytest
    - pytest tests/unit/ -v
  parallel: 3

test-integration:
  stage: test
  image: python:3.11
  services:
    - postgres:13
  variables:
    POSTGRES_DB: testdb
    POSTGRES_USER: testuser
    POSTGRES_PASSWORD: testpass
  script:
    - pip install pytest psycopg2-binary
    - pytest tests/integration/ -v

test-e2e:
  stage: test
  image: python:3.11
  script:
    - pip install pytest selenium
    - pytest tests/e2e/ -v
```

**Result**: Parallel test execution.

## Example 5: Artifacts and Cache

Use artifacts and caching for efficiency:

```yaml
# .gitlab-ci.yml with caching
variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

cache:
  paths:
    - .cache/pip
    - venv/

stages:
  - build
  - test
  - deploy

install-deps:
  stage: build
  image: python:3.11
  script:
    - python -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
  artifacts:
    paths:
      - venv/
    expire_in: 1 hour

run-tests:
  stage: test
  image: python:3.11
  dependencies:
    - install-deps
  script:
    - source venv/bin/activate
    - pytest tests/
  artifacts:
    reports:
      junit: report.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml
```

**Result**: Efficient builds with caching and artifacts.

## Example 6: Conditional Jobs

Run jobs based on conditions:

```yaml
# .gitlab-ci.yml with rules
stages:
  - test
  - deploy

test:
  stage: test
  script:
    - pytest tests/
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == "main"'

deploy-dev:
  stage: deploy
  script:
    - echo "Deploy to dev"
  rules:
    - if: '$CI_COMMIT_BRANCH == "develop"'
      when: always

deploy-prod:
  stage: deploy
  script:
    - echo "Deploy to production"
  rules:
    - if: '$CI_COMMIT_TAG'
      when: manual
    - when: never

security-scan:
  stage: test
  script:
    - pip install safety
    - safety check
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
    - if: '$CI_MERGE_REQUEST_TARGET_BRANCH_NAME == "main"'
```

**Result**: Conditional job execution with rules.

## Example 7: Matrix Builds

Test multiple configurations:

```yaml
# .gitlab-ci.yml with matrix
test:
  stage: test
  image: python:${PYTHON_VERSION}
  parallel:
    matrix:
      - PYTHON_VERSION: ["3.9", "3.10", "3.11", "3.12"]
        OS: ["linux", "windows"]
  script:
    - pip install pytest
    - pytest tests/
  tags:
    - ${OS}
```

**Result**: Matrix testing across versions and platforms.

## Example 8: Scheduled Pipelines

Run pipelines on schedule:

```yaml
# .gitlab-ci.yml for scheduled pipelines
stages:
  - test
  - report

nightly-tests:
  stage: test
  image: python:3.11
  script:
    - pip install pytest pytest-timeout
    - pytest tests/ --slow --timeout=300
  only:
    - schedules
  artifacts:
    when: always
    reports:
      junit: report.xml

weekly-security-scan:
  stage: test
  image: python:3.11
  script:
    - pip install safety bandit
    - safety check --json > safety-report.json
    - bandit -r src/ -f json -o bandit-report.json
  only:
    variables:
      - $SCAN_TYPE == "security"
  artifacts:
    paths:
      - "*-report.json"
```

**Result**: Scheduled pipeline execution.

## Example 9: Include and Extend

Reuse pipeline configurations:

```yaml
# .gitlab-ci-templates.yml
.python-base:
  image: python:3.11
  before_script:
    - pip install --upgrade pip
    - pip install -r requirements.txt

.test-template:
  extends: .python-base
  stage: test
  script:
    - pytest tests/

# .gitlab-ci.yml
include:
  - local: '.gitlab-ci-templates.yml'

stages:
  - test
  - build

unit-tests:
  extends: .test-template
  script:
    - pytest tests/unit/

integration-tests:
  extends: .test-template
  services:
    - postgres:13
  script:
    - pytest tests/integration/

build:
  extends: .python-base
  stage: build
  script:
    - python -m build
```

**Result**: Reusable pipeline components.

## Example 10: Production GitLab CI Pipeline

Enterprise-grade complete pipeline:

```yaml
# .gitlab-ci.yml - Production Pipeline
workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == "main"'
    - if: '$CI_COMMIT_BRANCH == "develop"'
    - if: '$CI_COMMIT_TAG'

variables:
  PYTHON_VERSION: "3.11"
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA

stages:
  - lint
  - test
  - build
  - security
  - deploy

cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - .cache/pip
    - venv/

.python-base:
  image: python:${PYTHON_VERSION}
  before_script:
    - python -m venv venv
    - source venv/bin/activate
    - pip install --upgrade pip

lint:
  extends: .python-base
  stage: lint
  script:
    - pip install flake8 black isort mypy
    - echo "Running flake8..."
    - flake8 src/ tests/ --max-line-length=100 --statistics
    - echo "Checking code formatting..."
    - black --check src/ tests/
    - echo "Checking import order..."
    - isort --check-only src/ tests/
    - echo "Running type checks..."
    - mypy src/ --ignore-missing-imports
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == "main"'
    - if: '$CI_COMMIT_BRANCH == "develop"'

test:unit:
  extends: .python-base
  stage: test
  needs: [lint]
  script:
    - pip install -r requirements.txt
    - pip install pytest pytest-cov pytest-xdist
    - pytest tests/unit/ --cov=src --cov-report=xml --cov-report=html --junitxml=report.xml -n auto
  coverage: '/TOTAL.*\\s+(\\d+%)$/'
  artifacts:
    when: always
    reports:
      junit: report.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml
    paths:
      - htmlcov/
    expire_in: 30 days

test:integration:
  extends: .python-base
  stage: test
  needs: [lint]
  services:
    - postgres:13
    - redis:6
  variables:
    POSTGRES_DB: testdb
    POSTGRES_USER: testuser
    POSTGRES_PASSWORD: testpass
    REDIS_URL: redis://redis:6379/0
  script:
    - pip install -r requirements.txt
    - pip install pytest
    - pytest tests/integration/ -v --junitxml=integration-report.xml
  artifacts:
    when: always
    reports:
      junit: integration-report.xml

build:package:
  extends: .python-base
  stage: build
  needs: ["test:unit", "test:integration"]
  script:
    - pip install build twine
    - python -m build
    - twine check dist/*
  artifacts:
    paths:
      - dist/
    expire_in: 1 week

build:docker:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  needs: ["test:unit", "test:integration"]
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker tag $DOCKER_IMAGE $CI_REGISTRY_IMAGE:latest
    - docker push $DOCKER_IMAGE
    - docker push $CI_REGISTRY_IMAGE:latest
  only:
    - main
    - develop
    - tags

security:dependency-scan:
  extends: .python-base
  stage: security
  allow_failure: true
  script:
    - pip install safety
    - safety check --json --output safety-report.json || true
  artifacts:
    paths:
      - safety-report.json
    expire_in: 7 days

security:sast:
  extends: .python-base
  stage: security
  allow_failure: true
  script:
    - pip install bandit
    - bandit -r src/ -f json -o bandit-report.json || true
  artifacts:
    paths:
      - bandit-report.json
    expire_in: 7 days

deploy:staging:
  stage: deploy
  image: python:${PYTHON_VERSION}
  environment:
    name: staging
    url: https://staging.example.com
    on_stop: stop:staging
  needs:
    - build:package
    - build:docker
  before_script:
    - pip install boto3  # For AWS deployment
  script:
    - echo "Deploying to staging environment"
    - python deploy.py --env=staging --version=$CI_COMMIT_SHORT_SHA
  only:
    - develop
  when: on_success

stop:staging:
  stage: deploy
  environment:
    name: staging
    action: stop
  script:
    - echo "Stopping staging environment"
  when: manual
  only:
    - develop

deploy:production:
  stage: deploy
  image: python:${PYTHON_VERSION}
  environment:
    name: production
    url: https://example.com
  needs:
    - build:package
    - build:docker
    - security:dependency-scan
    - security:sast
  before_script:
    - pip install boto3
  script:
    - echo "Deploying to production environment"
    - python deploy.py --env=production --version=$CI_COMMIT_TAG
  only:
    - tags
  when: manual

pages:
  extends: .python-base
  stage: deploy
  needs: ["test:unit"]
  script:
    - mkdir -p public
    - mv htmlcov public/coverage
    - echo '<html><body><a href="coverage/index.html">Coverage Report</a></body></html>' > public/index.html
  artifacts:
    paths:
      - public
  only:
    - main
```

**Result**: Production-ready GitLab CI/CD pipeline.

## KEY TAKEAWAYS

- **Stages**: Define pipeline stages (test, build, deploy)
- **Jobs**: Configure jobs within stages with scripts
- **Docker**: Use Docker images for consistent environments
- **Artifacts**: Share build outputs between jobs
- **Cache**: Speed up pipelines with dependency caching
- **Rules**: Conditional job execution based on branch/tag/MR
- **Parallel**: Run jobs in parallel for faster execution
- **Environments**: Define staging/production deployment targets
- **Matrix**: Test across multiple configurations
- **Best Practices**: Include templates, security scans, manual production deploys
'''

# Lesson 265: Integration Testing
lesson265 = next(l for l in lessons if l['id'] == 265)
lesson265['content'] = '''# Integration Testing

Test how multiple components work together including databases, APIs, and external services. Integration tests verify that different parts of your application integrate correctly, catching issues that unit tests miss like database queries, API interactions, and service communication.

## Example 1: Basic Integration Test

Test database integration:

```python
import sqlite3
import unittest

class UserRepository:
    def __init__(self, db_path):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                email TEXT
            )
        """)
        conn.commit()
        conn.close()

    def add_user(self, username, email):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (username, email)
        )
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return user_id

    def get_user(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute(
            "SELECT id, username, email FROM users WHERE id = ?",
            (user_id,)
        )
        row = cursor.fetchone()
        conn.close()
        return dict(zip(['id', 'username', 'email'], row)) if row else None

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repo = UserRepository(':memory:')

    def test_add_and_retrieve_user(self):
        # Integration test: database operations
        user_id = self.repo.add_user('john', 'john@example.com')
        self.assertIsNotNone(user_id)

        user = self.repo.get_user(user_id)
        self.assertEqual(user['username'], 'john')
        self.assertEqual(user['email'], 'john@example.com')
```

**Result**: Database integration testing.

## Example 2: API Integration Test

Test external API integration:

```python
import json
import urllib.request
import unittest

class WeatherService:
    def get_weather(self, city):
        # Simulated API call (in real scenario, call actual API)
        url = f"https://api.example.com/weather?city={city}"
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                data = json.loads(response.read())
                return {
                    'temperature': data.get('temp'),
                    'conditions': data.get('conditions')
                }
        except Exception as e:
            return None

class MockWeatherService(WeatherService):
    """Mock service for testing without external dependency."""
    def get_weather(self, city):
        # Return mock data
        return {
            'temperature': 72,
            'conditions': 'sunny'
        }

class TestWeatherIntegration(unittest.TestCase):
    def setUp(self):
        self.service = MockWeatherService()

    def test_get_weather(self):
        result = self.service.get_weather('London')
        self.assertIsNotNone(result)
        self.assertIn('temperature', result)
        self.assertIn('conditions', result)
```

**Result**: API integration testing with mocks.

## Example 3: Multi-Component Integration

Test multiple components together:

```python
import sqlite3
import unittest

class Database:
    def __init__(self, db_path=':memory:'):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL
            )
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                product_id INTEGER,
                quantity INTEGER,
                total REAL,
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        """)
        self.conn.commit()

class ProductService:
    def __init__(self, db):
        self.db = db

    def add_product(self, name, price):
        cursor = self.db.conn.execute(
            "INSERT INTO products (name, price) VALUES (?, ?)",
            (name, price)
        )
        self.db.conn.commit()
        return cursor.lastrowid

    def get_product(self, product_id):
        cursor = self.db.conn.execute(
            "SELECT id, name, price FROM products WHERE id = ?",
            (product_id,)
        )
        row = cursor.fetchone()
        if row:
            return {'id': row[0], 'name': row[1], 'price': row[2]}
        return None

class OrderService:
    def __init__(self, db, product_service):
        self.db = db
        self.product_service = product_service

    def create_order(self, product_id, quantity):
        product = self.product_service.get_product(product_id)
        if not product:
            raise ValueError("Product not found")

        total = product['price'] * quantity
        cursor = self.db.conn.execute(
            "INSERT INTO orders (product_id, quantity, total) VALUES (?, ?, ?)",
            (product_id, quantity, total)
        )
        self.db.conn.commit()
        return cursor.lastrowid

class TestEcommerceIntegration(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.product_service = ProductService(self.db)
        self.order_service = OrderService(self.db, self.product_service)

    def test_create_order_flow(self):
        # Integration test: product + order services
        product_id = self.product_service.add_product("Laptop", 999.99)
        order_id = self.order_service.create_order(product_id, 2)

        self.assertIsNotNone(order_id)

        # Verify order in database
        cursor = self.db.conn.execute(
            "SELECT product_id, quantity, total FROM orders WHERE id = ?",
            (order_id,)
        )
        row = cursor.fetchone()
        self.assertEqual(row[0], product_id)
        self.assertEqual(row[1], 2)
        self.assertAlmostEqual(row[2], 1999.98, places=2)
```

**Result**: Multi-component integration testing.

## Example 4: File System Integration

Test file operations:

```python
import os
import tempfile
import unittest

class FileStorage:
    def __init__(self, base_path):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

    def save(self, filename, content):
        filepath = os.path.join(self.base_path, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        return filepath

    def load(self, filename):
        filepath = os.path.join(self.base_path, filename)
        if not os.path.exists(filepath):
            return None
        with open(filepath, 'r') as f:
            return f.read()

    def delete(self, filename):
        filepath = os.path.join(self.base_path, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
        return False

class TestFileStorageIntegration(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.storage = FileStorage(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

    def test_save_and_load(self):
        content = "Hello, World!"
        filepath = self.storage.save("test.txt", content)
        self.assertTrue(os.path.exists(filepath))

        loaded = self.storage.load("test.txt")
        self.assertEqual(loaded, content)

    def test_delete_file(self):
        self.storage.save("temp.txt", "data")
        result = self.storage.delete("temp.txt")
        self.assertTrue(result)

        loaded = self.storage.load("temp.txt")
        self.assertIsNone(loaded)
```

**Result**: File system integration testing.

## Example 5: HTTP Server Integration

Test HTTP server endpoints:

```python
import http.server
import json
import threading
import time
import unittest
import urllib.request

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = json.dumps({'status': 'healthy'})
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # Suppress logs

class TestHTTPServerIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.port = 8888
        cls.server = http.server.HTTPServer(
            ('localhost', cls.port),
            SimpleAPIHandler
        )
        cls.thread = threading.Thread(target=cls.server.serve_forever)
        cls.thread.daemon = True
        cls.thread.start()
        time.sleep(0.1)  # Wait for server to start

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def test_health_endpoint(self):
        url = f'http://localhost:{self.port}/health'
        with urllib.request.urlopen(url) as response:
            self.assertEqual(response.status, 200)
            data = json.loads(response.read())
            self.assertEqual(data['status'], 'healthy')
```

**Result**: HTTP server integration testing.

## Example 6: Database Transaction Integration

Test transaction handling:

```python
import sqlite3
import unittest

class BankAccount:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                balance REAL DEFAULT 0
            )
        """)
        self.conn.commit()

    def create_account(self, initial_balance=0):
        cursor = self.conn.execute(
            "INSERT INTO accounts (balance) VALUES (?)",
            (initial_balance,)
        )
        self.conn.commit()
        return cursor.lastrowid

    def transfer(self, from_id, to_id, amount):
        try:
            self.conn.execute("BEGIN TRANSACTION")

            # Check balance
            cursor = self.conn.execute(
                "SELECT balance FROM accounts WHERE id = ?",
                (from_id,)
            )
            from_balance = cursor.fetchone()[0]

            if from_balance < amount:
                self.conn.execute("ROLLBACK")
                raise ValueError("Insufficient funds")

            # Debit from account
            self.conn.execute(
                "UPDATE accounts SET balance = balance - ? WHERE id = ?",
                (amount, from_id)
            )

            # Credit to account
            self.conn.execute(
                "UPDATE accounts SET balance = balance + ? WHERE id = ?",
                (amount, to_id)
            )

            self.conn.execute("COMMIT")
            return True

        except Exception as e:
            self.conn.execute("ROLLBACK")
            raise

    def get_balance(self, account_id):
        cursor = self.conn.execute(
            "SELECT balance FROM accounts WHERE id = ?",
            (account_id,)
        )
        row = cursor.fetchone()
        return row[0] if row else None

class TestBankTransactionIntegration(unittest.TestCase):
    def setUp(self):
        self.bank = BankAccount(':memory:')

    def test_successful_transfer(self):
        account1 = self.bank.create_account(1000)
        account2 = self.bank.create_account(500)

        self.bank.transfer(account1, account2, 200)

        self.assertEqual(self.bank.get_balance(account1), 800)
        self.assertEqual(self.bank.get_balance(account2), 700)

    def test_insufficient_funds_rollback(self):
        account1 = self.bank.create_account(100)
        account2 = self.bank.create_account(0)

        with self.assertRaises(ValueError):
            self.bank.transfer(account1, account2, 200)

        # Verify rollback
        self.assertEqual(self.bank.get_balance(account1), 100)
        self.assertEqual(self.bank.get_balance(account2), 0)
```

**Result**: Transaction integrity testing.

## Example 7: Cache Integration Testing

Test caching layer:

```python
import time
import unittest

class SimpleCache:
    def __init__(self):
        self.cache = {}
        self.timestamps = {}
        self.ttl = 60  # seconds

    def set(self, key, value):
        self.cache[key] = value
        self.timestamps[key] = time.time()

    def get(self, key):
        if key not in self.cache:
            return None

        if time.time() - self.timestamps[key] > self.ttl:
            del self.cache[key]
            del self.timestamps[key]
            return None

        return self.cache[key]

class DataService:
    def __init__(self, cache=None):
        self.cache = cache
        self.fetch_count = 0

    def fetch_data(self, key):
        # Check cache first
        if self.cache:
            cached = self.cache.get(key)
            if cached is not None:
                return cached

        # Simulate expensive operation
        self.fetch_count += 1
        data = f"data_for_{key}"

        # Store in cache
        if self.cache:
            self.cache.set(key, data)

        return data

class TestCacheIntegration(unittest.TestCase):
    def setUp(self):
        self.cache = SimpleCache()
        self.service = DataService(self.cache)

    def test_cache_hit(self):
        # First call - cache miss
        result1 = self.service.fetch_data('key1')
        self.assertEqual(self.service.fetch_count, 1)

        # Second call - cache hit
        result2 = self.service.fetch_data('key1')
        self.assertEqual(result1, result2)
        self.assertEqual(self.service.fetch_count, 1)  # No additional fetch

    def test_cache_expiration(self):
        self.cache.ttl = 0.1  # 100ms TTL

        result1 = self.service.fetch_data('key1')
        self.assertEqual(self.service.fetch_count, 1)

        time.sleep(0.2)  # Wait for expiration

        result2 = self.service.fetch_data('key1')
        self.assertEqual(self.service.fetch_count, 2)  # Cache expired, fetched again
```

**Result**: Cache integration testing.

## Example 8: Message Queue Integration

Test message queue functionality:

```python
import queue
import threading
import time
import unittest

class MessageQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def publish(self, message):
        self.queue.put(message)

    def subscribe(self, timeout=1):
        try:
            return self.queue.get(timeout=timeout)
        except queue.Empty:
            return None

class MessageProcessor:
    def __init__(self, message_queue):
        self.queue = message_queue
        self.processed = []
        self.running = False

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._process)
        self.thread.start()

    def stop(self):
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join(timeout=2)

    def _process(self):
        while self.running:
            message = self.queue.subscribe(timeout=0.1)
            if message:
                self.processed.append(message.upper())

class TestMessageQueueIntegration(unittest.TestCase):
    def setUp(self):
        self.queue = MessageQueue()
        self.processor = MessageProcessor(self.queue)

    def tearDown(self):
        self.processor.stop()

    def test_message_processing(self):
        self.processor.start()

        # Publish messages
        self.queue.publish("hello")
        self.queue.publish("world")

        # Wait for processing
        time.sleep(0.5)

        self.assertIn("HELLO", self.processor.processed)
        self.assertIn("WORLD", self.processor.processed)
```

**Result**: Message queue integration testing.

## Example 9: Configuration Integration

Test configuration loading and usage:

```python
import json
import os
import tempfile
import unittest

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.load()

    def load(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return {}

    def get(self, key, default=None):
        return self.config.get(key, default)

class Application:
    def __init__(self, config_loader):
        self.config = config_loader
        self.port = self.config.get('port', 8000)
        self.debug = self.config.get('debug', False)

class TestConfigurationIntegration(unittest.TestCase):
    def setUp(self):
        self.config_file = tempfile.NamedTemporaryFile(
            mode='w',
            delete=False,
            suffix='.json'
        )
        config_data = {
            'port': 9000,
            'debug': True,
            'database': 'sqlite:///test.db'
        }
        json.dump(config_data, self.config_file)
        self.config_file.close()

    def tearDown(self):
        os.unlink(self.config_file.name)

    def test_application_with_config(self):
        loader = ConfigLoader(self.config_file.name)
        app = Application(loader)

        self.assertEqual(app.port, 9000)
        self.assertEqual(app.debug, True)
        self.assertEqual(loader.get('database'), 'sqlite:///test.db')
```

**Result**: Configuration integration testing.

## Example 10: Production Integration Test Suite

Complete integration testing framework:

```python
import os
import sqlite3
import tempfile
import unittest
from typing import Optional

class Database:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self._init_schema()

    def _init_schema(self):
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """)
        self.conn.commit()

    def close(self):
        self.conn.close()

class UserService:
    def __init__(self, db: Database):
        self.db = db

    def create_user(self, username: str, email: str) -> int:
        cursor = self.db.conn.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (username, email)
        )
        self.db.conn.commit()
        return cursor.lastrowid

    def get_user(self, user_id: int) -> Optional[dict]:
        cursor = self.db.conn.execute(
            "SELECT id, username, email FROM users WHERE id = ?",
            (user_id,)
        )
        row = cursor.fetchone()
        if row:
            return {'id': row[0], 'username': row[1], 'email': row[2]}
        return None

class PostService:
    def __init__(self, db: Database):
        self.db = db

    def create_post(self, user_id: int, title: str, content: str) -> int:
        cursor = self.db.conn.execute(
            "INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)",
            (user_id, title, content)
        )
        self.db.conn.commit()
        return cursor.lastrowid

    def get_user_posts(self, user_id: int) -> list:
        cursor = self.db.conn.execute(
            "SELECT id, title, content, created_at FROM posts WHERE user_id = ?",
            (user_id,)
        )
        return [
            {
                'id': row[0],
                'title': row[1],
                'content': row[2],
                'created_at': row[3]
            }
            for row in cursor.fetchall()
        ]

class BlogApplication:
    def __init__(self, db: Database):
        self.db = db
        self.user_service = UserService(db)
        self.post_service = PostService(db)

    def create_user_with_post(self, username: str, email: str, post_title: str, post_content: str):
        user_id = self.user_service.create_user(username, email)
        post_id = self.post_service.create_post(user_id, post_title, post_content)
        return {'user_id': user_id, 'post_id': post_id}

class IntegrationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.mkdtemp()

    @classmethod
    def tearDownClass(cls):
        import shutil
        shutil.rmtree(cls.temp_dir)

    def setUp(self):
        self.db_path = os.path.join(self.temp_dir, 'test.db')
        self.db = Database(self.db_path)
        self.user_service = UserService(self.db)
        self.post_service = PostService(self.db)
        self.app = BlogApplication(self.db)

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

class TestBlogIntegration(IntegrationTestCase):
    def test_create_user_and_verify(self):
        user_id = self.user_service.create_user('alice', 'alice@example.com')
        user = self.user_service.get_user(user_id)

        self.assertIsNotNone(user)
        self.assertEqual(user['username'], 'alice')
        self.assertEqual(user['email'], 'alice@example.com')

    def test_create_post_for_user(self):
        user_id = self.user_service.create_user('bob', 'bob@example.com')
        post_id = self.post_service.create_post(
            user_id,
            'First Post',
            'Hello, World!'
        )

        posts = self.post_service.get_user_posts(user_id)
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], 'First Post')

    def test_full_workflow(self):
        # Integration test: full user + post creation workflow
        result = self.app.create_user_with_post(
            'charlie',
            'charlie@example.com',
            'Welcome Post',
            'This is my first blog post!'
        )

        self.assertIn('user_id', result)
        self.assertIn('post_id', result)

        # Verify user
        user = self.user_service.get_user(result['user_id'])
        self.assertEqual(user['username'], 'charlie')

        # Verify post
        posts = self.post_service.get_user_posts(result['user_id'])
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], 'Welcome Post')

    def test_multiple_posts_per_user(self):
        user_id = self.user_service.create_user('diana', 'diana@example.com')

        self.post_service.create_post(user_id, 'Post 1', 'Content 1')
        self.post_service.create_post(user_id, 'Post 2', 'Content 2')
        self.post_service.create_post(user_id, 'Post 3', 'Content 3')

        posts = self.post_service.get_user_posts(user_id)
        self.assertEqual(len(posts), 3)

if __name__ == '__main__':
    unittest.main()
```

**Result**: Production-ready integration test suite.

## KEY TAKEAWAYS

- **Scope**: Test multiple components working together
- **Database Testing**: Use in-memory or temporary databases
- **Setup/Teardown**: Create clean state for each test
- **External Services**: Use mocks or test instances
- **Transactions**: Test rollback and commit behavior
- **File System**: Use tempfile for isolated testing
- **Server Testing**: Start test servers in setUp, shutdown in tearDown
- **Real Dependencies**: Test with actual DB, cache, queue when possible
- **Isolation**: Each test should be independent
- **Production-Like**: Mirror production environment as closely as possible
'''

# Lesson 266: Iterator Basics
lesson266 = next(l for l in lessons if l['id'] == 266)
lesson266['content'] = '''# Iterator Basics

Understand Python iterators, the iter() and next() functions, and how to create custom iterables. Iterators are fundamental to Python's for loops, comprehensions, and generator expressions, enabling memory-efficient iteration over sequences and lazy evaluation of data.

## Example 1: Basic Iterator Usage

Use built-in iterators:

```python
# List iterator
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

# Continue iterating
for num in iterator:
    print(num)  # 4, 5
```

**Result**: Manual iteration with iter() and next().

## Example 2: Iterator Protocol

Understand the iterator protocol:

```python
class SimpleIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        """Return the iterator object (self)."""
        return self

    def __next__(self):
        """Return the next item."""
        if self.index >= len(self.data):
            raise StopIteration

        value = self.data[self.index]
        self.index += 1
        return value

# Usage
it = SimpleIterator([10, 20, 30])
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

# Works in for loop
it2 = SimpleIterator(['a', 'b', 'c'])
for item in it2:
    print(item)  # a, b, c
```

**Result**: Custom iterator implementation.

## Example 3: String Iterator

Iterate over string characters:

```python
text = "Python"
text_iter = iter(text)

print(next(text_iter))  # P
print(next(text_iter))  # y
print(next(text_iter))  # t

# Iterate remaining
for char in text_iter:
    print(char)  # h, o, n
```

**Result**: String iteration.

## Example 4: Dictionary Iterator

Iterate over dictionary keys/values:

```python
data = {'a': 1, 'b': 2, 'c': 3}

# Keys iterator
keys_iter = iter(data.keys())
print(next(keys_iter))  # a

# Values iterator
values_iter = iter(data.values())
print(next(values_iter))  # 1

# Items iterator
items_iter = iter(data.items())
print(next(items_iter))  # ('a', 1)
print(next(items_iter))  # ('b', 2)
```

**Result**: Dictionary iteration.

## Example 5: File Iterator

Iterate over file lines:

```python
# Files are iterators
def read_file_lines(filename):
    """Read file line by line using iterator."""
    with open(filename, 'r') as f:
        file_iter = iter(f)
        for line in file_iter:
            yield line.strip()

# Simulated file reading (without actual file)
class FileSimulator:
    def __init__(self, lines):
        self.lines = lines
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lines):
            raise StopIteration
        line = self.lines[self.index]
        self.index += 1
        return line

# Usage
fake_file = FileSimulator(['line 1', 'line 2', 'line 3'])
for line in fake_file:
    print(line)
```

**Result**: File-like iteration.

## Example 6: Range Iterator

Understand range as an iterator:

```python
# Range is an iterable, not a list
r = range(5)
print(type(r))  # <class 'range'>

# Get iterator
r_iter = iter(r)
print(next(r_iter))  # 0
print(next(r_iter))  # 1

# Use in for loop
for num in range(3, 6):
    print(num)  # 3, 4, 5

# Memory efficient
big_range = range(1000000)  # Doesn't create list in memory
```

**Result**: Range iterator usage.

## Example 7: Custom Countdown Iterator

Create countdown iterator:

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value

# Usage
countdown = Countdown(5)
for num in countdown:
    print(num)  # 5, 4, 3, 2, 1

# Manual iteration
cd2 = Countdown(3)
print(next(cd2))  # 3
print(next(cd2))  # 2
print(next(cd2))  # 1
```

**Result**: Custom countdown iterator.

## Example 8: Infinite Iterator

Create infinite iterators:

```python
class InfiniteCounter:
    def __init__(self, start=0):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current += 1
        return value

# Usage (be careful - infinite!)
counter = InfiniteCounter()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2

# Use with limit
counter2 = InfiniteCounter(10)
for i, value in enumerate(counter2):
    if i >= 5:
        break
    print(value)  # 10, 11, 12, 13, 14
```

**Result**: Infinite iterator with controlled iteration.

## Example 9: Iterator with State

Iterator that maintains state:

```python
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration

        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value

# Usage
fib = FibonacciIterator(10)
for num in fib:
    print(num, end=' ')  # 0 1 1 2 3 5 8 13 21 34
print()

# Get first N manually
fib2 = FibonacciIterator(5)
print([next(fib2) for _ in range(5)])  # [0, 1, 1, 2, 3]
```

**Result**: Stateful iterator for Fibonacci sequence.

## Example 10: Production Iterator Framework

Complete iterator implementation with utilities:

```python
from typing import Any, Callable, Iterator, Optional, TypeVar

T = TypeVar('T')

class IteratorUtils:
    @staticmethod
    def take(iterator: Iterator[T], n: int) -> list:
        """Take first n items from iterator."""
        result = []
        for _ in range(n):
            try:
                result.append(next(iterator))
            except StopIteration:
                break
        return result

    @staticmethod
    def consume(iterator: Iterator[T], n: Optional[int] = None):
        """Advance iterator n steps or until exhausted."""
        if n is None:
            for _ in iterator:
                pass
        else:
            for _ in range(n):
                try:
                    next(iterator)
                except StopIteration:
                    break

class ChunkedIterator:
    """Iterator that yields items in chunks."""
    def __init__(self, iterable, chunk_size):
        self.iterator = iter(iterable)
        self.chunk_size = chunk_size

    def __iter__(self):
        return self

    def __next__(self):
        chunk = []
        for _ in range(self.chunk_size):
            try:
                chunk.append(next(self.iterator))
            except StopIteration:
                if chunk:
                    return chunk
                raise

        return chunk

class FilterIterator:
    """Iterator that filters items based on predicate."""
    def __init__(self, iterable, predicate: Callable[[Any], bool]):
        self.iterator = iter(iterable)
        self.predicate = predicate

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            value = next(self.iterator)
            if self.predicate(value):
                return value

class MapIterator:
    """Iterator that transforms items."""
    def __init__(self, iterable, func: Callable):
        self.iterator = iter(iterable)
        self.func = func

    def __iter__(self):
        return self

    def __next__(self):
        return self.func(next(self.iterator))

class ZipIterator:
    """Iterator that zips multiple iterables."""
    def __init__(self, *iterables):
        self.iterators = [iter(it) for it in iterables]

    def __iter__(self):
        return self

    def __next__(self):
        values = []
        for it in self.iterators:
            try:
                values.append(next(it))
            except StopIteration:
                raise StopIteration

        return tuple(values)

# Usage examples
utils = IteratorUtils()

# Take first N
numbers = iter(range(100))
first_five = utils.take(numbers, 5)
print(f"First 5: {first_five}")  # [0, 1, 2, 3, 4]

# Chunked iteration
chunked = ChunkedIterator(range(10), 3)
for chunk in chunked:
    print(f"Chunk: {chunk}")
# Output: [0, 1, 2], [3, 4, 5], [6, 7, 8], [9]

# Filtered iteration
evens = FilterIterator(range(10), lambda x: x % 2 == 0)
print(f"Evens: {list(evens)}")  # [0, 2, 4, 6, 8]

# Mapped iteration
squared = MapIterator(range(5), lambda x: x**2)
print(f"Squared: {list(squared)}")  # [0, 1, 4, 9, 16]

# Zipped iteration
zipped = ZipIterator([1, 2, 3], ['a', 'b', 'c'])
print(f"Zipped: {list(zipped)}")  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

**Result**: Production-ready iterator utilities.

## KEY TAKEAWAYS

- **Iterator Protocol**: Implement __iter__() and __next__()
- **iter() Function**: Convert iterable to iterator
- **next() Function**: Get next item from iterator
- **StopIteration**: Signal end of iteration
- **Lazy Evaluation**: Iterators compute values on demand
- **Memory Efficiency**: Don't store all values in memory
- **One-Time Use**: Iterators are exhausted after full iteration
- **Built-in Iterables**: Lists, strings, dicts, files are iterable
- **Custom Iterators**: Maintain state between calls
- **Best Practices**: Use for loops for iteration, generators for simple cases
'''

# Lesson 267: Long Polling vs WebSockets
lesson267 = next(l for l in lessons if l['id'] == 267)
lesson267['content'] = '''# Long Polling vs WebSockets

Compare long polling and WebSocket techniques for real-time bidirectional communication. Long polling maintains HTTP connections open until data is available, while WebSockets provide persistent full-duplex connections for low-latency real-time updates.

## Example 1: Long Polling Client

Implement long polling:

```python
import time
import urllib.request
import json

class LongPollingClient:
    def __init__(self, url):
        self.url = url
        self.running = False

    def poll(self):
        """Long poll for updates."""
        try:
            req = urllib.request.Request(self.url, headers={'Connection': 'keep-alive'})
            with urllib.request.urlopen(req, timeout=30) as response:
                data = json.loads(response.read())
                return data
        except Exception as e:
            return None

    def start(self, callback):
        """Start polling loop."""
        self.running = True
        while self.running:
            data = self.poll()
            if data:
                callback(data)
            time.sleep(1)

# Usage (simulated)
# client = LongPollingClient('http://example.com/poll')
# client.start(lambda data: print(f"Received: {data}"))
```

## Example 2: Long Polling Server Simulation

Simulated long polling server:

```python
import http.server
import json
import time
from queue import Queue, Empty

class LongPollHandler(http.server.BaseHTTPRequestHandler):
    message_queue = Queue()

    def do_GET(self):
        if self.path == '/poll':
            # Wait for message or timeout
            try:
                message = self.message_queue.get(timeout=25)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(message).encode())
            except Empty:
                # Timeout - return empty
                self.send_response(204)
                self.end_headers()

# Start server
# server = http.server.HTTPServer(('localhost', 8000), LongPollHandler)
```

## Example 3: WebSocket Simulation

WebSocket-style communication pattern:

```python
import json

class WebSocketSimulator:
    """Simulates WebSocket behavior."""
    def __init__(self):
        self.connected = False
        self.handlers = {}

    def connect(self):
        self.connected = True
        if 'open' in self.handlers:
            self.handlers['open']()

    def send(self, message):
        if not self.connected:
            raise RuntimeError("Not connected")
        # Simulate sending
        return True

    def on(self, event, handler):
        """Register event handler."""
        self.handlers[event] = handler

    def receive(self, data):
        """Simulate receiving message."""
        if 'message' in self.handlers:
            self.handlers['message'](data)

# Usage
ws = WebSocketSimulator()
ws.on('open', lambda: print("Connected"))
ws.on('message', lambda data: print(f"Received: {data}"))

ws.connect()
ws.send({'type': 'chat', 'text': 'Hello'})
ws.receive({'type': 'chat', 'text': 'Hi there'})
```

## KEY TAKEAWAYS

- **Long Polling**: HTTP requests held open until data available
- **WebSockets**: Persistent bidirectional TCP connection
- **Latency**: WebSockets have lower latency
- **Overhead**: Long polling has HTTP overhead per request
- **Use Cases**: Long polling for simple updates, WebSockets for real-time apps
'''

# Lesson 268: Parse nested JSON
lesson268 = next(l for l in lessons if l['id'] == 268)
lesson268['content'] = """# Parse nested JSON

Parse and navigate deeply nested JSON structures using Python's json module and recursive traversal. Handle complex hierarchical data from APIs, configuration files, and data serialization formats.

## Example 1: Basic JSON Parsing

Parse simple JSON:

```python
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)

print(data['name'])  # John
print(data['age'])   # 30
print(data['city'])  # New York
```

## Example 2: Nested Object Access

Access nested properties:

```python
import json

json_data = '''{
    "user": {
        "name": "Alice",
        "profile": {
            "email": "alice@example.com",
            "preferences": {
                "theme": "dark",
                "notifications": true
            }
        }
    }
}'''

data = json.loads(json_data)
print(data['user']['name'])  # Alice
print(data['user']['profile']['email'])  # alice@example.com
print(data['user']['profile']['preferences']['theme'])  # dark
```

## Example 3: Arrays in JSON

Parse JSON arrays:

```python
import json

json_data = '''{
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
}'''

data = json.loads(json_data)
for user in data['users']:
    print(f"{user['id']}: {user['name']}")
# Output: 1: Alice, 2: Bob, 3: Charlie
```

## Example 4: Deep Nested Structures

Navigate complex nesting:

```python
import json

json_data = '''{
    "company": {
        "departments": [
            {
                "name": "Engineering",
                "teams": [
                    {"name": "Backend", "members": [{"name": "Alice"}, {"name": "Bob"}]},
                    {"name": "Frontend", "members": [{"name": "Charlie"}]}
                ]
            }
        ]
    }
}'''

data = json.loads(json_data)
for dept in data['company']['departments']:
    print(f"Department: {dept['name']}")
    for team in dept['teams']:
        print(f"  Team: {team['name']}")
        for member in team['members']:
            print(f"    Member: {member['name']}")
```

## Example 5: Safe Navigation

Handle missing keys safely:

```python
import json

json_data = '{"user": {"name": "Alice"}}'
data = json.loads(json_data)

# Safe access with get()
email = data.get('user', {}).get('profile', {}).get('email')
print(email)  # None

# With default value
theme = data.get('user', {}).get('preferences', {}).get('theme', 'light')
print(theme)  # light
```

## Example 6: Recursive Traversal

Traverse all nested values:

```python
import json

def traverse_json(obj, path=""):
    """Recursively traverse JSON structure."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            new_path = f"{path}.{key}" if path else key
            traverse_json(value, new_path)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            new_path = f"{path}[{i}]"
            traverse_json(item, new_path)
    else:
        print(f"{path}: {obj}")

json_data = '''{
    "name": "John",
    "contacts": [
        {"type": "email", "value": "john@example.com"},
        {"type": "phone", "value": "555-1234"}
    ]
}'''

data = json.loads(json_data)
traverse_json(data)
```

## KEY TAKEAWAYS

- **json.loads()**: Parse JSON string to Python object
- **json.dumps()**: Convert Python object to JSON string
- **Nested Access**: Use bracket notation for deep access
- **Safe Navigation**: Use get() to avoid KeyError
- **Arrays**: Access with indices, iterate with loops
- **Recursion**: Traverse deeply nested structures
"""

# Lesson 269: Read Replicas
lesson269 = next(l for l in lessons if l['id'] == 269)
lesson269['content'] = """# Read Replicas - Scaling Reads

Implement read replica patterns for horizontal read scaling in database architectures. Read replicas are synchronized copies of the primary database that handle read queries, reducing load on the primary and improving read performance for high-traffic applications.

## Example 1: Simulated Read Replica Pattern

Basic read replica routing:

```python
import random

class DatabaseConnection:
    def __init__(self, name, is_primary=False):
        self.name = name
        self.is_primary = is_primary

    def execute_read(self, query):
        return f"[{self.name}] Read: {query}"

    def execute_write(self, query):
        if not self.is_primary:
            raise RuntimeError("Cannot write to replica")
        return f"[{self.name}] Write: {query}"

class DatabasePool:
    def __init__(self):
        self.primary = DatabaseConnection("primary", is_primary=True)
        self.replicas = [
            DatabaseConnection("replica-1"),
            DatabaseConnection("replica-2"),
            DatabaseConnection("replica-3")
        ]

    def execute(self, query, is_write=False):
        if is_write:
            return self.primary.execute_write(query)
        else:
            # Load balance across replicas
            replica = random.choice(self.replicas)
            return replica.execute_read(query)

# Usage
pool = DatabasePool()

# Writes go to primary
result = pool.execute("INSERT INTO users VALUES (1, 'Alice')", is_write=True)
print(result)

# Reads go to replicas
for _ in range(3):
    result = pool.execute("SELECT * FROM users")
    print(result)
```

## Example 2: Round-Robin Load Balancing

Distribute reads evenly:

```python
class RoundRobinPool:
    def __init__(self):
        self.primary = DatabaseConnection("primary", is_primary=True)
        self.replicas = [
            DatabaseConnection("replica-1"),
            DatabaseConnection("replica-2")
        ]
        self.current_index = 0

    def get_replica(self):
        replica = self.replicas[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.replicas)
        return replica

    def execute_read(self, query):
        replica = self.get_replica()
        return replica.execute_read(query)

# Usage
pool = RoundRobinPool()

for i in range(5):
    result = pool.execute_read(f"SELECT * FROM table WHERE id={i}")
    print(result)
# Alternates: replica-1, replica-2, replica-1, replica-2, replica-1
```

## Example 3: Weighted Load Balancing

Route based on replica capacity:

```python
import random

class WeightedReplica:
    def __init__(self, connection, weight):
        self.connection = connection
        self.weight = weight

class WeightedPool:
    def __init__(self):
        self.replicas = [
            WeightedReplica(DatabaseConnection("replica-1"), weight=3),
            WeightedReplica(DatabaseConnection("replica-2"), weight=2),
            WeightedReplica(DatabaseConnection("replica-3"), weight=1)
        ]

    def get_replica(self):
        total_weight = sum(r.weight for r in self.replicas)
        choice = random.randint(1, total_weight)

        current = 0
        for replica in self.replicas:
            current += replica.weight
            if choice <= current:
                return replica.connection

        return self.replicas[0].connection

# Usage
pool = WeightedPool()
# Replica-1 gets ~50% of traffic, replica-2 ~33%, replica-3 ~17%
```

## KEY TAKEAWAYS

- **Read Scaling**: Distribute read load across multiple database copies
- **Primary/Replica**: Writes to primary, reads from replicas
- **Replication Lag**: Replicas may be slightly behind primary
- **Load Balancing**: Random, round-robin, or weighted distribution
- **High Availability**: Multiple replicas provide redundancy
- **Use Cases**: Read-heavy applications, reporting, analytics
"""

# Lesson 270: Stripe Payment Intent API
lesson270 = next(l for l in lessons if l['id'] == 270)
lesson270['content'] = """# Stripe - Payment Intent API

Integrate Stripe Payment Intents for secure payment processing. Payment Intents represent the entire payment flow from creation through confirmation, handling complex scenarios like authentication, retries, and webhooks for robust payment handling.

## Example 1: Simulated Payment Intent

Simulate Stripe Payment Intent flow:

```python
import json
import secrets

class PaymentIntent:
    def __init__(self, amount, currency='usd'):
        self.id = f"pi_{secrets.token_hex(12)}"
        self.amount = amount
        self.currency = currency
        self.status = 'requires_payment_method'
        self.client_secret = f"{self.id}_secret_{secrets.token_hex(16)}"

    def confirm(self, payment_method):
        """Confirm payment with payment method."""
        if self.status != 'requires_payment_method':
            raise ValueError(f"Cannot confirm in status: {self.status}")

        self.payment_method = payment_method
        self.status = 'processing'

        # Simulate processing
        if self._process_payment():
            self.status = 'succeeded'
        else:
            self.status = 'requires_action'

        return self.status

    def _process_payment(self):
        """Simulate payment processing."""
        # In real scenario, this involves actual payment processing
        return True

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'currency': self.currency,
            'status': self.status,
            'client_secret': self.client_secret
        }

# Usage
intent = PaymentIntent(amount=1999, currency='usd')  # $19.99
print(f"Created: {intent.id}")
print(f"Status: {intent.status}")
print(f"Client Secret: {intent.client_secret}")

# Confirm payment
status = intent.confirm(payment_method='pm_card_visa')
print(f"Payment status: {status}")
```

## Example 2: Payment Flow Manager

Complete payment flow:

```python
class PaymentFlowManager:
    def __init__(self):
        self.intents = {}

    def create_intent(self, amount, currency='usd', metadata=None):
        """Create a new payment intent."""
        intent = PaymentIntent(amount, currency)
        if metadata:
            intent.metadata = metadata
        self.intents[intent.id] = intent
        return intent

    def retrieve_intent(self, intent_id):
        """Get existing payment intent."""
        return self.intents.get(intent_id)

    def confirm_intent(self, intent_id, payment_method):
        """Confirm payment intent."""
        intent = self.retrieve_intent(intent_id)
        if not intent:
            raise ValueError("Intent not found")
        return intent.confirm(payment_method)

    def cancel_intent(self, intent_id):
        """Cancel payment intent."""
        intent = self.retrieve_intent(intent_id)
        if intent and intent.status in ['requires_payment_method', 'requires_action']:
            intent.status = 'canceled'
            return True
        return False

# Usage
manager = PaymentFlowManager()

# Create payment
intent = manager.create_intent(
    amount=4999,
    metadata={'order_id': '12345', 'customer': 'cus_123'}
)
print(f"Created intent: {intent.id}")

# Confirm payment
status = manager.confirm_intent(intent.id, 'pm_card_visa')
print(f"Payment confirmed: {status}")
```

## Example 3: Webhook Handler

Handle payment webhooks:

```python
import json
import hashlib
import hmac

class WebhookHandler:
    def __init__(self, webhook_secret):
        self.webhook_secret = webhook_secret

    def verify_signature(self, payload, signature):
        """Verify webhook signature."""
        expected = hmac.new(
            self.webhook_secret.encode(),
            payload.encode(),
            hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(expected, signature)

    def handle_event(self, event_type, data):
        """Handle webhook event."""
        handlers = {
            'payment_intent.succeeded': self._handle_success,
            'payment_intent.payment_failed': self._handle_failure,
            'payment_intent.requires_action': self._handle_action_required
        }

        handler = handlers.get(event_type)
        if handler:
            return handler(data)

    def _handle_success(self, data):
        print(f"Payment succeeded: {data.get('id')}")
        # Update order status, send confirmation email, etc.
        return {'status': 'processed'}

    def _handle_failure(self, data):
        print(f"Payment failed: {data.get('id')}")
        # Notify customer, log failure, etc.
        return {'status': 'failed'}

    def _handle_action_required(self, data):
        print(f"Action required: {data.get('id')}")
        # Prompt customer for additional authentication
        return {'status': 'action_required'}

# Usage
webhook = WebhookHandler('whsec_test123')

# Simulated webhook event
event = {
    'type': 'payment_intent.succeeded',
    'data': {'id': 'pi_123', 'amount': 1999}
}

webhook.handle_event(event['type'], event['data'])
```

## KEY TAKEAWAYS

- **Payment Intent**: Represents entire payment lifecycle
- **Client Secret**: Frontend uses this to confirm payment
- **Payment Method**: Card, bank account, or other payment source
- **Status Flow**: requires_payment_method → processing → succeeded
- **Webhooks**: Handle asynchronous payment updates
- **Error Handling**: Handle payment failures gracefully
- **Security**: Verify webhook signatures
"""

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created comprehensive unique content for lessons 261-270:")
for lid in range(261, 271):
    lesson = next(l for l in lessons if l['id'] == lid)
    chars = len(lesson['content'])
    print(f"  {lid}: {lesson['title'][:45]:45s} {chars:5,d} chars")
