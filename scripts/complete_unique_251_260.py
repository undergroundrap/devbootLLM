#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 251: Git Branch Summary
lesson251 = next(l for l in lessons if l['id'] == 251)
lesson251['content'] = '''# Git Branch Summary

Manage and analyze Git branches using Python to automate branch operations, generate reports, and maintain repository health. Python's subprocess and GitPython library enable powerful Git automation for branch management, merging strategies, and code review workflows.

## Example 1: List All Branches with subprocess

Get branch information using Git commands:

```python
import subprocess

def get_branches():
    """List all branches in repository."""
    result = subprocess.run(
        ['git', 'branch', '-a'],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        branches = [
            line.strip().lstrip('* ')
            for line in result.stdout.splitlines()
        ]
        return branches
    else:
        raise Exception(f"Git error: {result.stderr}")

branches = get_branches()
print(f"Total branches: {len(branches)}")
for branch in branches[:5]:
    print(f"  - {branch}")
```

**Result**: List repository branches.

## Example 2: Get Current Branch

Identify active branch:

```python
def get_current_branch():
    """Get name of current branch."""
    result = subprocess.run(
        ['git', 'branch', '--show-current'],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return result.stdout.strip()
    else:
        raise Exception(f"Git error: {result.stderr}")

current = get_current_branch()
print(f"Current branch: {current}")

# Alternative: parse git branch output
def get_current_branch_alt():
    """Alternative method using git branch."""
    result = subprocess.run(
        ['git', 'branch'],
        capture_output=True,
        text=True
    )

    for line in result.stdout.splitlines():
        if line.startswith('*'):
            return line[2:].strip()

    return None
```

**Result**: Detect active branch.

## Example 3: Branch Last Commit Info

Get branch metadata:

```python
def get_branch_last_commit(branch):
    """Get last commit info for branch."""
    result = subprocess.run(
        ['git', 'log', branch, '-1', '--format=%H|%an|%ae|%at|%s'],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        parts = result.stdout.strip().split('|')
        return {
            'hash': parts[0],
            'author': parts[1],
            'email': parts[2],
            'timestamp': int(parts[3]),
            'message': parts[4]
        }

    return None

# Get info for main branch
info = get_branch_last_commit('main')
print(f"Last commit: {info['message']}")
print(f"Author: {info['author']}")
```

**Result**: Branch commit metadata.

## Example 4: Compare Branches

Find differences between branches:

```python
def compare_branches(base, compare):
    """Get commits in compare but not in base."""
    result = subprocess.run(
        ['git', 'log', f'{base}..{compare}', '--oneline'],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        commits = [
            line.strip()
            for line in result.stdout.splitlines()
        ]
        return commits

    return []

# Compare feature branch to main
commits = compare_branches('main', 'feature/new-feature')
print(f"Commits ahead of main: {len(commits)}")
for commit in commits:
    print(f"  {commit}")
```

**Result**: Branch comparison.

## Example 5: Using GitPython Library

Advanced Git operations:

```python
from git import Repo
from datetime import datetime

repo = Repo('.')

# List all branches
branches = [b.name for b in repo.branches]
print(f"Local branches: {branches}")

# Get branch info
for branch in repo.branches:
    commit = branch.commit
    age_days = (datetime.now() - datetime.fromtimestamp(commit.committed_date)).days

    print(f"{branch.name}:")
    print(f"  Last commit: {commit.message.strip()}")
    print(f"  Author: {commit.author}")
    print(f"  Age: {age_days} days")
```

**Result**: GitPython for advanced operations.

## Example 6: Branch Status Report

Generate comprehensive branch report:

```python
def generate_branch_report():
    """Create detailed branch status report."""
    repo = Repo('.')
    report = {
        'total_branches': len(list(repo.branches)),
        'current_branch': repo.active_branch.name,
        'branches': []
    }

    for branch in repo.branches:
        commit = branch.commit
        branch_info = {
            'name': branch.name,
            'last_commit': {
                'hash': commit.hexsha[:7],
                'message': commit.message.strip(),
                'author': str(commit.author),
                'date': datetime.fromtimestamp(commit.committed_date).isoformat()
            },
            'ahead_of_main': len(list(repo.iter_commits(f'main..{branch.name}'))),
            'behind_main': len(list(repo.iter_commits(f'{branch.name}..main')))
        }
        report['branches'].append(branch_info)

    return report

report = generate_branch_report()
print(f"Branch Report:")
print(f"  Total: {report['total_branches']}")
print(f"  Current: {report['current_branch']}")
```

**Result**: Detailed branch report.

## Example 7: Find Stale Branches

Identify old branches for cleanup:

```python
from datetime import datetime, timedelta

def find_stale_branches(days=90):
    """Find branches not updated in N days."""
    repo = Repo('.')
    cutoff = datetime.now() - timedelta(days=days)
    stale = []

    for branch in repo.branches:
        commit_date = datetime.fromtimestamp(branch.commit.committed_date)

        if commit_date < cutoff:
            stale.append({
                'name': branch.name,
                'last_commit_date': commit_date,
                'days_old': (datetime.now() - commit_date).days
            })

    return sorted(stale, key=lambda x: x['days_old'], reverse=True)

# Find branches older than 90 days
stale = find_stale_branches(90)
print(f"Stale branches (>90 days): {len(stale)}")
for branch in stale[:5]:
    print(f"  {branch['name']}: {branch['days_old']} days old")
```

**Result**: Stale branch detection.

## Example 8: Merged Branch Detection

Find branches already merged:

```python
def find_merged_branches(base='main'):
    """Find branches fully merged into base."""
    repo = Repo('.')
    merged = []

    for branch in repo.branches:
        if branch.name == base:
            continue

        # Check if branch is merged
        result = subprocess.run(
            ['git', 'branch', '--merged', base],
            capture_output=True,
            text=True
        )

        if branch.name in result.stdout:
            merged.append(branch.name)

    return merged

# Find branches merged into main
merged = find_merged_branches('main')
print(f"Merged branches: {len(merged)}")
for branch in merged:
    print(f"  {branch}")
```

**Result**: Merged branch identification.

## Example 9: Branch Protection Check

Verify branch protection rules:

```python
def check_branch_protection(branch_name):
    """Check if branch has protection rules (via GitHub API)."""
    import requests

    # Requires GitHub token
    token = "your-github-token"
    repo_url = "owner/repo"

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    url = f'https://api.github.com/repos/{repo_url}/branches/{branch_name}/protection'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        protection = response.json()
        return {
            'protected': True,
            'required_reviews': protection.get('required_pull_request_reviews', {}).get('required_approving_review_count', 0),
            'enforce_admins': protection.get('enforce_admins', {}).get('enabled', False)
        }
    elif response.status_code == 404:
        return {'protected': False}

    return None

# Check main branch protection
protection = check_branch_protection('main')
if protection and protection['protected']:
    print(f"Branch is protected")
    print(f"  Required reviews: {protection['required_reviews']}")
```

**Result**: Branch protection verification.

## Example 10: Production Branch Manager

Complete branch management system:

```python
from git import Repo
from datetime import datetime, timedelta
from typing import List, Dict
import json

class BranchManager:
    def __init__(self, repo_path='.'):
        self.repo = Repo(repo_path)

    def list_branches(self, remote=False) -> List[str]:
        """List local or remote branches."""
        if remote:
            return [ref.name for ref in self.repo.remote().refs]
        return [b.name for b in self.repo.branches]

    def get_branch_info(self, branch_name: str) -> Dict:
        """Get detailed branch information."""
        branch = self.repo.branches[branch_name]
        commit = branch.commit

        return {
            'name': branch_name,
            'commit_hash': commit.hexsha,
            'author': str(commit.author),
            'date': datetime.fromtimestamp(commit.committed_date),
            'message': commit.message.strip(),
            'is_current': branch == self.repo.active_branch
        }

    def find_stale(self, days: int = 90) -> List[Dict]:
        """Find branches not updated in N days."""
        cutoff = datetime.now() - timedelta(days=days)
        stale = []

        for branch in self.repo.branches:
            commit_date = datetime.fromtimestamp(branch.commit.committed_date)
            if commit_date < cutoff:
                stale.append({
                    'name': branch.name,
                    'days_old': (datetime.now() - commit_date).days
                })

        return sorted(stale, key=lambda x: x['days_old'], reverse=True)

    def delete_branch(self, branch_name: str, force=False):
        """Delete a branch."""
        if branch_name == self.repo.active_branch.name:
            raise ValueError("Cannot delete current branch")

        self.repo.delete_head(branch_name, force=force)

    def generate_report(self) -> Dict:
        """Generate comprehensive branch report."""
        return {
            'timestamp': datetime.now().isoformat(),
            'current_branch': self.repo.active_branch.name,
            'total_branches': len(list(self.repo.branches)),
            'stale_branches': len(self.find_stale(90)),
            'branches': [
                self.get_branch_info(b.name)
                for b in self.repo.branches
            ]
        }

# Usage
manager = BranchManager()

# List all branches
branches = manager.list_branches()
print(f"Branches: {branches}")

# Find stale branches
stale = manager.find_stale(90)
print(f"Stale (>90 days): {len(stale)}")

# Generate report
report = manager.generate_report()
print(json.dumps(report, indent=2, default=str))
```

**Result**: Production branch management.

## KEY TAKEAWAYS

- **subprocess**: Execute Git commands from Python
- **GitPython**: Pythonic Git repository access
- **Branch Info**: Get commit metadata and status
- **Comparison**: Find differences between branches
- **Stale Detection**: Identify old, unused branches
- **Merged Branches**: Find fully merged branches
- **Reports**: Generate branch status summaries
- **Automation**: Automate branch cleanup and maintenance
- **Protection**: Verify branch protection rules
- **Best Practices**: Regular branch hygiene, clear naming
'''

# Note: Lessons 252-260 will be added here
# For now, save and commit lesson 251

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created comprehensive unique content for lessons 251:")
for lid in [251]:
    lesson = next(l for l in lessons if l['id'] == lid)
    chars = len(lesson['content'])
    print(f"  {lid}: {lesson['title'][:45]:45s} {chars:5,d} chars")
