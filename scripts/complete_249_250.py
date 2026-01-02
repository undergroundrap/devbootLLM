#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 249: Grafana - Dashboard Creation
lesson249 = next(l for l in lessons if l['id'] == 249)
lesson249['content'] = '''# Grafana - Dashboard Creation

Create and manage Grafana dashboards programmatically using Python and the Grafana API. Grafana is a popular observability platform for visualizing metrics, logs, and traces. Python enables automation of dashboard creation, updates, and management at scale.

## Example 1: Basic Grafana API Client

Connect to Grafana API:

```python
import requests
import json

class GrafanaClient:
    def __init__(self, url, api_key):
        self.url = url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def get_dashboards(self):
        """List all dashboards."""
        response = requests.get(
            f'{self.url}/api/search',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

# Usage
client = GrafanaClient('http://localhost:3000', 'your-api-key')
dashboards = client.get_dashboards()
print(f"Found {len(dashboards)} dashboards")
```

**Result**: Connect to Grafana API.

## Example 2: Create Simple Dashboard

Build dashboard JSON structure:

```python
def create_dashboard_json(title, description=""):
    """Create basic dashboard structure."""
    return {
        "dashboard": {
            "title": title,
            "description": description,
            "tags": ["automated"],
            "timezone": "browser",
            "panels": [],
            "schemaVersion": 16,
            "version": 0,
            "refresh": "5s"
        },
        "folderId": 0,
        "overwrite": False
    }

# Create dashboard
dashboard = create_dashboard_json(
    "System Metrics",
    "Automated system monitoring dashboard"
)

# Post to Grafana
response = requests.post(
    f'{client.url}/api/dashboards/db',
    headers=client.headers,
    json=dashboard
)
result = response.json()
print(f"Dashboard created: {result['url']}")
```

**Result**: Create basic dashboard.

## Example 3: Add Panel to Dashboard

Create visualization panels:

```python
def create_panel(title, targets, panel_type="graph"):
    """Create a dashboard panel."""
    return {
        "title": title,
        "type": panel_type,
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 0},
        "targets": targets,
        "datasource": "Prometheus"
    }

# Create CPU usage panel
cpu_panel = create_panel(
    "CPU Usage",
    [{
        "expr": "100 - (avg by(instance) (irate(node_cpu_seconds_total{mode='idle'}[5m])) * 100)",
        "legendFormat": "{{instance}}",
        "refId": "A"
    }]
)

# Add to dashboard
dashboard["dashboard"]["panels"].append(cpu_panel)
```

**Result**: Add monitoring panels.

## Example 4: Dashboard Template Variables

Create dynamic dashboards:

```python
def add_template_variable(dashboard, name, query, datasource="Prometheus"):
    """Add template variable for dynamic filtering."""
    if "templating" not in dashboard["dashboard"]:
        dashboard["dashboard"]["templating"] = {"list": []}

    variable = {
        "name": name,
        "type": "query",
        "datasource": datasource,
        "query": query,
        "refresh": 1,
        "includeAll": True,
        "multi": True
    }

    dashboard["dashboard"]["templating"]["list"].append(variable)
    return dashboard

# Add instance variable
dashboard = add_template_variable(
    dashboard,
    "instance",
    "label_values(node_cpu_seconds_total, instance)"
)

# Use in panel query
panel_with_var = create_panel(
    "CPU by Instance",
    [{
        "expr": "node_cpu_seconds_total{instance=~'$instance'}",
        "refId": "A"
    }]
)
```

**Result**: Dynamic dashboard filtering.

## Example 5: Multiple Panel Types

Create different visualization types:

```python
def create_stat_panel(title, query, unit="short"):
    """Create single stat panel."""
    return {
        "title": title,
        "type": "stat",
        "gridPos": {"h": 4, "w": 6, "x": 0, "y": 0},
        "targets": [{
            "expr": query,
            "refId": "A"
        }],
        "options": {
            "reduceOptions": {
                "values": False,
                "calcs": ["lastNotNull"]
            }
        },
        "fieldConfig": {
            "defaults": {
                "unit": unit
            }
        }
    }

# Create various panels
uptime_panel = create_stat_panel(
    "System Uptime",
    "time() - node_boot_time_seconds",
    "s"
)

memory_panel = create_stat_panel(
    "Memory Usage %",
    "(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100",
    "percent"
)

# Add to dashboard
dashboard["dashboard"]["panels"].extend([uptime_panel, memory_panel])
```

**Result**: Different visualization types.

## Example 6: Dashboard Rows and Layout

Organize panels in rows:

```python
def create_row(title, collapsed=False):
    """Create dashboard row for organization."""
    return {
        "type": "row",
        "title": title,
        "collapsed": collapsed,
        "gridPos": {"h": 1, "w": 24, "x": 0, "y": 0}
    }

def layout_panels(panels, cols=2):
    """Auto-layout panels in grid."""
    panel_width = 24 // cols
    panel_height = 8

    for i, panel in enumerate(panels):
        row = i // cols
        col = i % cols

        panel["gridPos"] = {
            "h": panel_height,
            "w": panel_width,
            "x": col * panel_width,
            "y": row * panel_height
        }

    return panels

# Create organized dashboard
dashboard["dashboard"]["panels"] = [
    create_row("System Metrics"),
    *layout_panels([cpu_panel, memory_panel], cols=2),
    create_row("Network Metrics"),
    *layout_panels([network_panel], cols=1)
]
```

**Result**: Organized panel layout.

## Example 7: Alert Rules

Add alerting to panels:

```python
def add_alert(panel, condition, threshold):
    """Add alert rule to panel."""
    panel["alert"] = {
        "name": f"{panel['title']} Alert",
        "conditions": [{
            "evaluator": {
                "params": [threshold],
                "type": "gt"
            },
            "query": {
                "params": ["A", "5m", "now"]
            },
            "reducer": {
                "params": [],
                "type": "avg"
            },
            "type": "query"
        }],
        "executionErrorState": "alerting",
        "frequency": "1m",
        "handler": 1,
        "noDataState": "no_data",
        "notifications": []
    }
    return panel

# Add alert to CPU panel
cpu_panel = add_alert(cpu_panel, "CPU high", 80)
```

**Result**: Dashboard alerts.

## Example 8: Import/Export Dashboards

Backup and restore dashboards:

```python
class GrafanaDashboardManager:
    def __init__(self, client):
        self.client = client

    def export_dashboard(self, uid, filepath):
        """Export dashboard to JSON file."""
        response = requests.get(
            f'{self.client.url}/api/dashboards/uid/{uid}',
            headers=self.client.headers
        )
        response.raise_for_status()

        with open(filepath, 'w') as f:
            json.dump(response.json(), f, indent=2)

    def import_dashboard(self, filepath):
        """Import dashboard from JSON file."""
        with open(filepath, 'r') as f:
            dashboard = json.load(f)

        response = requests.post(
            f'{self.client.url}/api/dashboards/db',
            headers=self.client.headers,
            json=dashboard
        )
        return response.json()

# Usage
manager = GrafanaDashboardManager(client)

# Export
manager.export_dashboard('abc123', 'backup.json')

# Import
result = manager.import_dashboard('backup.json')
print(f"Imported: {result['uid']}")
```

**Result**: Dashboard backup/restore.

## Example 9: Dashboard Templating with Python

Generate dashboards from templates:

```python
def generate_dashboard_from_template(title, metrics):
    """Generate dashboard from metric definitions."""
    panels = []

    for i, metric in enumerate(metrics):
        panel = {
            "title": metric["name"],
            "type": "graph",
            "gridPos": {
                "h": 8,
                "w": 12,
                "x": (i % 2) * 12,
                "y": (i // 2) * 8
            },
            "targets": [{
                "expr": metric["query"],
                "refId": "A"
            }]
        }
        panels.append(panel)

    return {
        "dashboard": {
            "title": title,
            "panels": panels
        }
    }

# Generate dashboard
metrics = [
    {"name": "CPU", "query": "cpu_usage"},
    {"name": "Memory", "query": "mem_usage"}
]

dashboard = generate_dashboard_from_template("Auto Generated", metrics)
print(f"Generated dashboard with {len(dashboard['dashboard']['panels'])} panels")
```

**Result**: Template-based generation.

## Example 10: Production Dashboard Manager

Complete Grafana automation:

```python
import requests
from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class Panel:
    title: str
    query: str
    panel_type: str = "graph"

class GrafanaAutomation:
    def __init__(self, url: str, api_key: str):
        self.url = url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def create_dashboard(self, title: str, panels: List[Panel]) -> Dict[str, Any]:
        """Create complete dashboard with panels."""
        dashboard = {
            "dashboard": {
                "title": title,
                "panels": self._build_panels(panels),
                "schemaVersion": 16
            },
            "overwrite": True
        }

        response = requests.post(
            f'{self.url}/api/dashboards/db',
            headers=self.headers,
            json=dashboard
        )
        response.raise_for_status()
        return response.json()

    def _build_panels(self, panels: List[Panel]) -> List[Dict]:
        """Build panel configurations."""
        panel_configs = []
        for i, panel in enumerate(panels):
            config = {
                "title": panel.title,
                "type": panel.panel_type,
                "gridPos": {
                    "h": 8,
                    "w": 12,
                    "x": (i % 2) * 12,
                    "y": (i // 2) * 8
                },
                "targets": [{
                    "expr": panel.query,
                    "refId": "A"
                }]
            }
            panel_configs.append(config)
        return panel_configs

# Usage
grafana = GrafanaAutomation('http://localhost:3000', 'api-key')

panels = [
    Panel("CPU Usage", "cpu_percent"),
    Panel("Memory Usage", "mem_percent"),
    Panel("Disk I/O", "disk_io_rate")
]

result = grafana.create_dashboard("System Overview", panels)
print(f"Dashboard URL: {result['url']}")
```

**Result**: Production dashboard automation.

## KEY TAKEAWAYS

- **Grafana API**: RESTful API for programmatic access
- **Dashboard JSON**: Structured format for dashboard definition
- **Panels**: Individual visualization components
- **Templates**: Dynamic filtering with variables
- **Layout**: Grid-based positioning system
- **Data Sources**: Connect to Prometheus, InfluxDB, etc.
- **Alerts**: Threshold-based monitoring
- **Export/Import**: JSON-based backup and migration
- **Automation**: Python scripts for dashboard management
- **Best Practices**: Version control dashboards, use templates
'''

# Lesson 250: E2E Testing - User Flows
lesson250 = next(l for l in lessons if l['id'] == 250)
lesson250['content'] = '''# E2E Testing - User Flows

Test complete user workflows from start to finish using Python end-to-end testing frameworks. E2E testing validates entire application flows, ensuring all components work together correctly. Python offers powerful tools like Selenium, Playwright, and pytest for comprehensive E2E testing.

## Example 1: Basic Selenium Setup

Configure Selenium for browser automation:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class E2ETest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown(self):
        self.driver.quit()

# Basic test
test = E2ETest()
test.driver.get("https://example.com")
title = test.driver.title
print(f"Page title: {title}")
test.teardown()
```

**Result**: Basic browser automation.

## Example 2: Login Flow Test

Test authentication workflow:

```python
def test_login_flow(driver):
    """Test complete login process."""
    # Navigate to login page
    driver.get("https://example.com/login")

    # Find and fill username
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("testuser")

    # Find and fill password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("password123")

    # Click login button
    login_button = driver.find_element(By.ID, "login-btn")
    login_button.click()

    # Wait for redirect to dashboard
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/dashboard"))

    # Verify login success
    welcome_msg = driver.find_element(By.CLASS_NAME, "welcome")
    assert "Welcome" in welcome_msg.text

    return True

# Run test
driver = webdriver.Chrome()
result = test_login_flow(driver)
print(f"Login test: {'PASSED' if result else 'FAILED'}")
driver.quit()
```

**Result**: Complete login workflow test.

## Example 3: Form Submission Test

Test data entry and submission:

```python
from selenium.webdriver.support.ui import Select

def test_form_submission(driver):
    """Test form filling and submission."""
    driver.get("https://example.com/contact")

    # Fill text inputs
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john@example.com")

    # Select dropdown
    select = Select(driver.find_element(By.ID, "subject"))
    select.select_by_visible_text("Support")

    # Fill textarea
    message = driver.find_element(By.ID, "message")
    message.send_keys("This is a test message")

    # Submit form
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    # Wait for success message
    wait = WebDriverWait(driver, 10)
    success = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "success"))
    )

    assert "submitted successfully" in success.text.lower()
    return True
```

**Result**: Form interaction testing.

## Example 4: Shopping Cart Flow

Test e-commerce workflow:

```python
def test_shopping_cart_flow(driver):
    """Test complete purchase process."""
    # Browse products
    driver.get("https://shop.example.com/products")

    # Add item to cart
    add_to_cart = driver.find_element(
        By.CSS_SELECTOR,
        ".product:first-child .add-to-cart"
    )
    add_to_cart.click()

    # Wait for cart update
    wait = WebDriverWait(driver, 10)
    cart_count = wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "cart-count"),
            "1"
        )
    )

    # Go to cart
    driver.find_element(By.CLASS_NAME, "cart-icon").click()

    # Proceed to checkout
    driver.find_element(By.ID, "checkout-btn").click()

    # Fill shipping info
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "zip").send_keys("12345")

    # Complete purchase
    driver.find_element(By.ID, "place-order").click()

    # Verify order confirmation
    confirmation = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "order-confirm"))
    )

    assert "order placed" in confirmation.text.lower()
    return True
```

**Result**: Multi-step purchase flow.

## Example 5: Playwright for Modern Testing

Use Playwright for better automation:

```python
from playwright.sync_api import sync_playwright

def test_with_playwright():
    """Modern E2E testing with Playwright."""
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate and interact
        page.goto("https://example.com")
        page.click("#login-btn")

        # Fill form
        page.fill("#username", "testuser")
        page.fill("#password", "password123")

        # Submit
        page.click("button[type='submit']")

        # Wait for navigation
        page.wait_for_url("**/dashboard")

        # Verify
        welcome = page.text_content(".welcome")
        assert "Welcome" in welcome

        browser.close()

test_with_playwright()
print("Playwright test passed")
```

**Result**: Modern browser automation.

## Example 6: Page Object Pattern

Organize tests with Page Objects:

```python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://example.com/login"

    def navigate(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        field = self.driver.find_element(By.ID, "username")
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element(By.ID, "password")
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "login-btn").click()

    def login(self, username, password):
        """Complete login flow."""
        self.navigate()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

# Usage
driver = webdriver.Chrome()
login_page = LoginPage(driver)
login_page.login("testuser", "password123")

# Verify on dashboard
assert "/dashboard" in driver.current_url
driver.quit()
```

**Result**: Maintainable test structure.

## Example 7: pytest Integration

Structure E2E tests with pytest:

```python
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    """Setup and teardown browser."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_user(browser):
    """Login before test."""
    login_page = LoginPage(browser)
    login_page.login("testuser", "password123")
    return browser

def test_dashboard_access(logged_in_user):
    """Test authenticated user can access dashboard."""
    driver = logged_in_user
    driver.get("https://example.com/dashboard")

    # Verify dashboard elements
    assert driver.find_element(By.CLASS_NAME, "dashboard-title")
    assert driver.find_element(By.CLASS_NAME, "user-menu")

def test_logout_flow(logged_in_user):
    """Test user can logout."""
    driver = logged_in_user
    driver.find_element(By.ID, "logout-btn").click()

    # Verify redirected to login
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    assert "/login" in driver.current_url
```

**Result**: Structured pytest E2E tests.

## Example 8: Screenshot on Failure

Capture evidence on test failure:

```python
import os
from datetime import datetime

class E2ETestRunner:
    def __init__(self, driver):
        self.driver = driver
        self.screenshots_dir = "test_screenshots"
        os.makedirs(self.screenshots_dir, exist_ok=True)

    def take_screenshot(self, name):
        """Save screenshot with timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(self.screenshots_dir, filename)
        self.driver.save_screenshot(filepath)
        return filepath

    def run_test(self, test_func, name):
        """Run test with screenshot on failure."""
        try:
            test_func(self.driver)
            print(f"✓ {name} passed")
            return True
        except Exception as e:
            screenshot = self.take_screenshot(f"failure_{name}")
            print(f"✗ {name} failed: {e}")
            print(f"  Screenshot: {screenshot}")
            return False

# Usage
driver = webdriver.Chrome()
runner = E2ETestRunner(driver)

runner.run_test(test_login_flow, "login_test")
runner.run_test(test_form_submission, "form_test")

driver.quit()
```

**Result**: Failure diagnostics.

## Example 9: API + UI Combined Testing

Test full stack integration:

```python
import requests

class FullStackTest:
    def __init__(self, api_base, web_base):
        self.api_base = api_base
        self.web_base = web_base
        self.driver = webdriver.Chrome()

    def test_data_sync(self):
        """Test API data appears in UI."""
        # Create data via API
        response = requests.post(
            f"{self.api_base}/api/items",
            json={"name": "Test Item", "price": 9.99}
        )
        item_id = response.json()["id"]

        # Verify in UI
        self.driver.get(f"{self.web_base}/items")

        # Wait for item to appear
        wait = WebDriverWait(self.driver, 10)
        item_element = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f"[data-item-id='{item_id}']")
            )
        )

        assert "Test Item" in item_element.text
        assert "9.99" in item_element.text

        return True

    def cleanup(self):
        self.driver.quit()

# Run full stack test
test = FullStackTest("http://api.example.com", "http://example.com")
result = test.test_data_sync()
print(f"Full stack test: {'PASSED' if result else 'FAILED'}")
test.cleanup()
```

**Result**: API and UI integration testing.

## Example 10: Production E2E Framework

Complete E2E testing framework:

```python
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Callable
import logging

class E2ETestFramework:
    def __init__(self, base_url: str, headless: bool = False):
        self.base_url = base_url
        self.headless = headless
        self.driver = None
        self.logger = logging.getLogger(__name__)

    def setup(self):
        """Initialize browser."""
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        return self.driver

    def teardown(self):
        """Cleanup browser."""
        if self.driver:
            self.driver.quit()

    def navigate(self, path: str):
        """Navigate to path."""
        url = f"{self.base_url}{path}"
        self.logger.info(f"Navigating to {url}")
        self.driver.get(url)

    def wait_for(self, condition: Callable, timeout: int = 10):
        """Wait for condition."""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(condition)

    def run_user_flow(self, flow_name: str, steps: list):
        """Execute multi-step user flow."""
        self.logger.info(f"Starting flow: {flow_name}")

        for i, step in enumerate(steps, 1):
            try:
                self.logger.info(f"Step {i}: {step['description']}")
                step['action'](self.driver)
            except Exception as e:
                self.logger.error(f"Step {i} failed: {e}")
                self.driver.save_screenshot(f"failure_step_{i}.png")
                raise

# Usage
framework = E2ETestFramework("https://example.com", headless=True)
framework.setup()

# Define user flow
login_and_purchase = [
    {
        "description": "Navigate to homepage",
        "action": lambda d: framework.navigate("/")
    },
    {
        "description": "Click login",
        "action": lambda d: d.find_element(By.ID, "login").click()
    },
    {
        "description": "Enter credentials",
        "action": lambda d: (
            d.find_element(By.ID, "username").send_keys("user"),
            d.find_element(By.ID, "password").send_keys("pass")
        )
    },
    {
        "description": "Submit login",
        "action": lambda d: d.find_element(By.ID, "submit").click()
    }
]

framework.run_user_flow("Login and Purchase", login_and_purchase)
framework.teardown()
```

**Result**: Production E2E framework.

## KEY TAKEAWAYS

- **E2E Testing**: Validates complete user workflows
- **Selenium**: Industry-standard browser automation
- **Playwright**: Modern, fast browser automation
- **Page Objects**: Maintainable test structure pattern
- **pytest Integration**: Structured test organization
- **Wait Strategies**: Handle asynchronous UI updates
- **Screenshots**: Capture failure evidence
- **User Flows**: Multi-step workflow validation
- **CI/CD**: Automated testing in pipelines
- **Best Practices**: Stable selectors, explicit waits, test isolation
'''

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created comprehensive unique content for lessons 249-250:")
for lid in [249, 250]:
    lesson = next(l for l in lessons if l['id'] == lid)
    chars = len(lesson['content'])
    print(f"  {lid}: {lesson['title'][:45]:45s} {chars:5,d} chars")
