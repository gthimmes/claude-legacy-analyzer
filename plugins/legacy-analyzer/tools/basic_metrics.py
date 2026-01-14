"""
Language-agnostic basic code metrics.

Works with ANY programming language.
"""

import re
from pathlib import Path
from typing import Dict, List


class BasicMetrics:
    """Calculate language-agnostic code metrics."""

    @staticmethod
    def count_lines(file_path: str) -> Dict[str, int]:
        """
        Count different types of lines in any code file.

        Returns:
            Dict with total, code, comment, blank line counts
        """
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        except:
            return {'total': 0, 'code': 0, 'comment': 0, 'blank': 0}

        total = len(lines)
        blank = 0
        comment = 0
        code = 0

        in_block_comment = False
        ext = Path(file_path).suffix.lower()

        for line in lines:
            stripped = line.strip()

            if not stripped:
                blank += 1
                continue

            # Detect comments based on common patterns
            # This works for most C-style and scripting languages
            is_comment = False

            # Block comment detection (/* ... */ or """ ... """)
            if '/*' in stripped or '"""' in stripped or "'''" in stripped:
                in_block_comment = True
                is_comment = True

            if '*/' in stripped or (in_block_comment and ('"""' in stripped or "'''" in stripped)):
                in_block_comment = False
                is_comment = True
                continue

            if in_block_comment:
                comment += 1
                continue

            # Single-line comments
            # Works for: //, #, --, %, ', REM
            comment_markers = ['//', '#', '--', '%', "'", 'REM', ';;']
            for marker in comment_markers:
                if stripped.startswith(marker):
                    is_comment = True
                    break

            if is_comment:
                comment += 1
            else:
                code += 1

        return {
            'total': total,
            'code': code,
            'comment': comment,
            'blank': blank
        }

    @staticmethod
    def estimate_complexity_indicators(file_path: str) -> Dict[str, int]:
        """
        Count complexity indicators that work across languages.

        Looks for common patterns:
        - Conditionals: if, else, elif, switch, case, ?:
        - Loops: for, while, do, loop, each
        - Exception handling: try, catch, except, rescue
        - Boolean operators: &&, ||, and, or

        Returns:
            Dict with counts of each indicator type
        """
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except:
            return {}

        # Language-agnostic patterns
        patterns = {
            'conditionals': r'\b(if|else|elif|elseif|elsif|switch|case|when|unless|cond|match)\b',
            'loops': r'\b(for|while|do|loop|foreach|each|map|filter|reduce|until|repeat)\b',
            'exceptions': r'\b(try|catch|except|rescue|ensure|finally|raise|throw)\b',
            'boolean_ops': r'(\&\&|\|\||and\b|or\b|not\b)',
            'returns': r'\b(return|yield|break|continue)\b',
            'functions': r'\b(def|function|func|fn|fun|lambda|proc|method|sub)\b',
        }

        indicators = {}
        for name, pattern in patterns.items():
            matches = re.findall(pattern, content, re.IGNORECASE)
            indicators[name] = len(matches)

        # Estimated cyclomatic complexity (very rough)
        indicators['estimated_complexity'] = (
            indicators.get('conditionals', 0) +
            indicators.get('loops', 0) +
            indicators.get('boolean_ops', 0) +
            1  # Base path
        )

        return indicators

    @staticmethod
    def count_functions(file_path: str) -> int:
        """
        Estimate number of functions/methods.

        Works across languages by looking for common patterns.
        """
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except:
            return 0

        # Common function declaration patterns
        patterns = [
            r'\bdef\s+\w+\s*\(',           # Python, Ruby
            r'\bfunction\s+\w+\s*\(',      # JavaScript
            r'\bfunc\s+\w+\s*\(',          # Go, Swift
            r'\bfn\s+\w+\s*\(',            # Rust
            r'\bpublic\s+\w+\s+\w+\s*\(',  # Java, C#
            r'\bprivate\s+\w+\s+\w+\s*\(', # Java, C#
            r'\bprotected\s+\w+\s+\w+\s*\(',
            r'\b\w+\s+\w+\s*\([^)]*\)\s*{', # C, C++
        ]

        count = 0
        for pattern in patterns:
            matches = re.findall(pattern, content)
            count += len(matches)

        # Avoid double-counting by taking max
        return max(count, 0)

    @staticmethod
    def analyze_file(file_path: str) -> Dict:
        """
        Complete basic analysis of any code file.

        Returns all metrics combined.
        """
        lines = BasicMetrics.count_lines(file_path)
        complexity = BasicMetrics.estimate_complexity_indicators(file_path)
        function_count = BasicMetrics.count_functions(file_path)

        return {
            'file': file_path,
            'extension': Path(file_path).suffix,
            'lines': lines,
            'complexity': complexity,
            'function_count': function_count,
        }

    @staticmethod
    def summarize_directory(file_paths: List[str]) -> Dict:
        """
        Summarize metrics across multiple files.

        Works for any language/codebase.
        """
        total_lines = 0
        total_code = 0
        total_comments = 0
        total_blank = 0
        total_functions = 0
        total_complexity = 0

        file_count = len(file_paths)

        for file_path in file_paths:
            metrics = BasicMetrics.analyze_file(file_path)

            lines = metrics['lines']
            total_lines += lines['total']
            total_code += lines['code']
            total_comments += lines['comment']
            total_blank += lines['blank']

            total_functions += metrics['function_count']
            total_complexity += metrics['complexity'].get('estimated_complexity', 0)

        avg_complexity = total_complexity / file_count if file_count > 0 else 0

        return {
            'total_files': file_count,
            'total_lines': total_lines,
            'total_code_lines': total_code,
            'total_comment_lines': total_comments,
            'total_blank_lines': total_blank,
            'total_functions': total_functions,
            'estimated_total_complexity': total_complexity,
            'average_complexity_per_file': round(avg_complexity, 2),
            'average_lines_per_file': round(total_lines / file_count, 2) if file_count > 0 else 0,
        }
