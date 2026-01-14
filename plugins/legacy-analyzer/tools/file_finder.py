"""
Language-agnostic file finder.

Works with ANY programming language or file type.
"""

import os
from pathlib import Path
from typing import List, Set, Dict
import fnmatch


class FileFinder:
    """Find files in a codebase - works with any language."""

    def __init__(self, root_path: str, exclude_patterns: List[str] = None):
        self.root_path = Path(root_path)
        self.exclude_patterns = exclude_patterns or [
            '**/node_modules/**',
            '**/vendor/**',
            '**/.git/**',
            '**/build/**',
            '**/dist/**',
            '**/target/**',
            '**/__pycache__/**',
            '**/*.pyc',
            '**/.venv/**',
            '**/venv/**',
        ]

    def find_files(self, patterns: List[str] = None) -> List[str]:
        """
        Find files matching patterns.

        Args:
            patterns: Glob patterns like ['*.py', '*.java', '*.js']
                     If None, finds all code files

        Returns:
            List of file paths
        """
        if patterns is None:
            # Default: common code file extensions
            patterns = [
                '*.py', '*.java', '*.js', '*.jsx', '*.ts', '*.tsx',
                '*.cpp', '*.c', '*.h', '*.hpp', '*.cs', '*.go',
                '*.rs', '*.rb', '*.php', '*.swift', '*.kt', '*.scala',
                '*.m', '*.mm', '*.dart', '*.ex', '*.exs', '*.clj',
                '*.hs', '*.ml', '*.elm', '*.erl', '*.jl', '*.r',
                '*.lua', '*.pl', '*.sh', '*.bash', '*.zsh'
            ]

        files = []
        for pattern in patterns:
            for file_path in self.root_path.rglob(pattern):
                if self._should_include(file_path):
                    files.append(str(file_path))

        return sorted(files)

    def _should_include(self, file_path: Path) -> bool:
        """Check if file should be included."""
        path_str = str(file_path)

        # Check exclude patterns
        for pattern in self.exclude_patterns:
            if fnmatch.fnmatch(path_str, pattern):
                return False

        # Must be a file
        return file_path.is_file()

    def find_by_extension(self, extension: str) -> List[str]:
        """Find all files with specific extension."""
        if not extension.startswith('.'):
            extension = '.' + extension
        return self.find_files([f'*{extension}'])

    def group_by_extension(self) -> Dict[str, List[str]]:
        """Group all code files by extension."""
        all_files = self.find_files()
        grouped = {}

        for file_path in all_files:
            ext = Path(file_path).suffix.lower()
            if ext not in grouped:
                grouped[ext] = []
            grouped[ext].append(file_path)

        return grouped

    def find_test_files(self) -> List[str]:
        """
        Find test files using common naming conventions.

        Works across languages:
        - Java: *Test.java, *Tests.java
        - Python: test_*.py, *_test.py
        - JavaScript: *.test.js, *.spec.js
        - Go: *_test.go
        - Ruby: *_spec.rb
        - etc.
        """
        test_patterns = [
            '*test*.py', '*Test*.java', '*.test.js', '*.spec.js',
            '*.test.ts', '*.spec.ts', '*_test.go', '*_spec.rb',
            '*Test*.kt', '*Spec*.scala', '*test*.cpp', '*_test.cpp'
        ]

        files = []
        for pattern in test_patterns:
            files.extend(self.find_files([pattern]))

        return list(set(files))  # Remove duplicates

    def get_directory_structure(self, max_depth: int = 3) -> Dict:
        """
        Get directory structure for overview.

        Returns a tree of directories and file counts.
        """
        structure = {}

        for file_path in self.find_files():
            path = Path(file_path)
            rel_path = path.relative_to(self.root_path)

            parts = rel_path.parts
            if len(parts) > max_depth:
                parts = parts[:max_depth]

            current = structure
            for part in parts[:-1]:  # Exclude filename
                if part not in current:
                    current[part] = {}
                current = current[part]

        return structure

    def count_files_by_language(self) -> Dict[str, int]:
        """
        Count files by language (using extension as proxy).

        Returns: {'Python': 45, 'Java': 23, ...}
        """
        extension_map = {
            '.py': 'Python',
            '.java': 'Java',
            '.js': 'JavaScript',
            '.jsx': 'JavaScript',
            '.ts': 'TypeScript',
            '.tsx': 'TypeScript',
            '.cpp': 'C++',
            '.cc': 'C++',
            '.c': 'C',
            '.h': 'C/C++',
            '.hpp': 'C++',
            '.cs': 'C#',
            '.go': 'Go',
            '.rs': 'Rust',
            '.rb': 'Ruby',
            '.php': 'PHP',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.scala': 'Scala',
            '.m': 'Objective-C',
            '.dart': 'Dart',
            '.ex': 'Elixir',
            '.exs': 'Elixir',
            '.clj': 'Clojure',
            '.hs': 'Haskell',
            '.ml': 'OCaml',
            '.elm': 'Elm',
            '.erl': 'Erlang',
            '.jl': 'Julia',
            '.r': 'R',
            '.lua': 'Lua',
            '.pl': 'Perl',
            '.sh': 'Shell',
        }

        grouped = self.group_by_extension()
        language_counts = {}

        for ext, files in grouped.items():
            language = extension_map.get(ext, f'Other ({ext})')
            language_counts[language] = language_counts.get(language, 0) + len(files)

        return dict(sorted(language_counts.items(), key=lambda x: x[1], reverse=True))
