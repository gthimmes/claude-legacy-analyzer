"""
Git history analysis for identifying change frequency and bug patterns.

Analyzes git history to:
- Track change frequency (churn)
- Identify bug fix patterns
- Find frequent contributors
- Calculate code age
"""

import subprocess
import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from models.codebase_model import GitHistory


class GitHistoryAnalyzer:
    """Analyzes git history for a codebase."""

    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.bug_keywords = ['fix', 'bug', 'issue', 'defect', 'patch', 'error', 'crash']

    def _run_git_command(self, args: List[str]) -> str:
        """Run a git command and return output."""
        try:
            result = subprocess.run(
                ['git'] + args,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            return ""
        except Exception as e:
            print(f"Git command failed: {e}")
            return ""

    def is_git_repo(self) -> bool:
        """Check if the path is a git repository."""
        result = self._run_git_command(['rev-parse', '--git-dir'])
        return bool(result)

    def get_file_history(self, file_path: str, max_commits: int = 100) -> GitHistory:
        """
        Get git history for a specific file.

        Returns:
            GitHistory object with commit count, authors, bug fixes, etc.
        """
        if not self.is_git_repo():
            return GitHistory(file_path=file_path)

        history = GitHistory(file_path=file_path)

        # Get commit log for this file
        log_output = self._run_git_command([
            'log',
            '--follow',  # Follow file renames
            '--format=%H|%an|%ae|%ad|%s',  # Hash|Author|Email|Date|Subject
            '--date=iso',
            f'-{max_commits}',
            '--',
            file_path
        ])

        if not log_output:
            return history

        commits = log_output.split('\n')
        history.commit_count = len(commits)

        authors = set()
        bug_fix_count = 0
        last_modified = None

        for commit in commits:
            if not commit:
                continue

            parts = commit.split('|')
            if len(parts) < 5:
                continue

            commit_hash, author_name, author_email, date, subject = parts

            # Track authors
            authors.add(author_name)

            # Check if this is a bug fix
            if self._is_bug_fix(subject):
                bug_fix_count += 1

            # Track last modified date
            if last_modified is None:
                last_modified = date

        history.author_count = len(authors)
        history.bug_fix_count = bug_fix_count
        history.last_modified = last_modified

        # Calculate days since last modified
        if last_modified:
            try:
                last_date = datetime.fromisoformat(last_modified.replace(' ', 'T'))
                days_since = (datetime.now() - last_date).days
                history.days_since_modified = days_since
            except:
                pass

        # Get top 3 authors
        author_counts = self._get_top_authors(file_path, 3)
        history.top_authors = author_counts

        return history

    def _is_bug_fix(self, commit_message: str) -> bool:
        """Check if a commit message indicates a bug fix."""
        message_lower = commit_message.lower()
        return any(keyword in message_lower for keyword in self.bug_keywords)

    def _get_top_authors(self, file_path: str, n: int = 3) -> List[str]:
        """Get top N authors by commit count for a file."""
        shortlog_output = self._run_git_command([
            'shortlog',
            '-sn',  # Summary with number of commits
            '--',
            file_path
        ])

        if not shortlog_output:
            return []

        authors = []
        for line in shortlog_output.split('\n')[:n]:
            # Format: "  5  John Doe"
            match = re.match(r'\s*\d+\s+(.+)', line)
            if match:
                authors.append(match.group(1))

        return authors

    def get_change_frequency_score(self, file_path: str,
                                   time_window_days: int = 180) -> float:
        """
        Calculate change frequency score (0-10).

        Higher score = more frequent changes = higher risk of instability.
        """
        history = self.get_file_history(file_path)

        if history.commit_count == 0:
            return 0.0

        # Calculate commits per month
        commits_per_month = (history.commit_count / time_window_days) * 30

        # Score based on frequency
        # 0-2 commits/month = low (0-3)
        # 2-5 commits/month = moderate (3-6)
        # 5-10 commits/month = high (6-9)
        # 10+ commits/month = critical (9-10)

        if commits_per_month <= 2:
            score = commits_per_month * 1.5
        elif commits_per_month <= 5:
            score = 3 + (commits_per_month - 2) * 1.0
        elif commits_per_month <= 10:
            score = 6 + (commits_per_month - 5) * 0.6
        else:
            score = 9 + min(1, (commits_per_month - 10) * 0.1)

        return min(10.0, score)

    def get_bug_density_score(self, file_path: str) -> float:
        """
        Calculate bug density score (0-10).

        Higher score = more bug fixes = higher risk.
        """
        history = self.get_file_history(file_path)

        if history.commit_count == 0:
            return 0.0

        # Calculate percentage of commits that are bug fixes
        bug_percentage = (history.bug_fix_count / history.commit_count) * 100

        # Score based on bug percentage
        # 0-10% bugs = low (0-3)
        # 10-25% bugs = moderate (3-6)
        # 25-50% bugs = high (6-9)
        # 50%+ bugs = critical (9-10)

        if bug_percentage <= 10:
            score = bug_percentage * 0.3
        elif bug_percentage <= 25:
            score = 3 + (bug_percentage - 10) * 0.2
        elif bug_percentage <= 50:
            score = 6 + (bug_percentage - 25) * 0.12
        else:
            score = 9 + min(1, (bug_percentage - 50) * 0.02)

        return min(10.0, score)

    def get_age_score(self, file_path: str) -> float:
        """
        Calculate age score (0-10).

        Files not touched in a long time may be:
        - Stable and working (low risk) - if no bugs
        - Forgotten and fragile (high risk) - if has bugs

        We return higher scores for files modified recently (more churn risk)
        and very old files (potentially fragile).
        """
        history = self.get_file_history(file_path)

        if not history.days_since_modified:
            return 5.0  # Unknown, assume moderate

        days = history.days_since_modified

        # U-shaped curve:
        # Very recent (0-30 days) = moderate risk (5-7)
        # Stable (30-180 days) = low risk (2-4)
        # Old (180-365 days) = moderate risk (4-6)
        # Very old (1+ years) = higher risk (6-8)

        if days <= 30:
            score = 5 + (30 - days) / 30 * 2  # 5-7
        elif days <= 180:
            score = 2 + (180 - days) / 150 * 2  # 2-4
        elif days <= 365:
            score = 4 + (days - 180) / 185 * 2  # 4-6
        else:
            score = 6 + min(2, (days - 365) / 365)  # 6-8

        return min(10.0, score)

    def analyze_repository_history(self, file_paths: List[str]) -> Dict[str, GitHistory]:
        """
        Analyze git history for multiple files.

        Returns:
            Dictionary mapping file paths to GitHistory objects.
        """
        results = {}

        for file_path in file_paths:
            results[file_path] = self.get_file_history(file_path)

        return results

    def get_hotspot_files(self, n: int = 10) -> List[tuple]:
        """
        Get the top N files with most commits (hotspots).

        Returns:
            List of (file_path, commit_count) tuples.
        """
        if not self.is_git_repo():
            return []

        # Get commit counts for all files
        log_output = self._run_git_command([
            'log',
            '--format=',
            '--name-only',
            '--diff-filter=M'  # Only modifications
        ])

        if not log_output:
            return []

        # Count occurrences
        file_counts = {}
        for line in log_output.split('\n'):
            line = line.strip()
            if line:
                file_counts[line] = file_counts.get(line, 0) + 1

        # Sort by count
        sorted_files = sorted(
            file_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_files[:n]

    def get_repository_stats(self) -> Dict:
        """
        Get overall repository statistics.
        """
        if not self.is_git_repo():
            return {}

        # Total commits
        total_commits = self._run_git_command(['rev-list', '--count', 'HEAD'])

        # Total authors
        authors = self._run_git_command(['shortlog', '-sn', '--all'])
        author_count = len(authors.split('\n')) if authors else 0

        # Age of repo
        first_commit_date = self._run_git_command([
            'log', '--reverse', '--format=%ad', '--date=iso', '-1'
        ])

        repo_age_days = 0
        if first_commit_date:
            try:
                first_date = datetime.fromisoformat(first_commit_date.replace(' ', 'T'))
                repo_age_days = (datetime.now() - first_date).days
            except:
                pass

        return {
            "total_commits": int(total_commits) if total_commits else 0,
            "total_authors": author_count,
            "repo_age_days": repo_age_days,
            "hotspot_files": self.get_hotspot_files(10)
        }
