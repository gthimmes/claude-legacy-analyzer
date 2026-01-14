# Installation Guide

## Install from GitHub URL (Recommended for Claude Code)

```bash
/install https://github.com/yourusername/claude-legacy-analyzer
```

That's it! Claude Code will automatically:
1. Download the repository
2. Install Python dependencies from `requirements.txt`
3. Make the skill available for use

## Usage After Installation

Simply ask Claude in natural language:

```
"Analyze my codebase at ~/projects/my-app using the legacy modernization skill"

"Help me modernize the UserService class in my Spring Boot app"

"Generate a refactoring plan for PaymentProcessor"
```

## Verify Installation

```bash
# Check if the skill is installed
/skills

# Or test directly
python -m main --help
```

## Manual Installation (Alternative)

If you prefer to install manually:

```bash
git clone https://github.com/yourusername/claude-legacy-analyzer.git
cd claude-legacy-analyzer
pip install -r requirements.txt
```

Then run commands directly:

```bash
python -m main analyze /path/to/codebase --language java
```

## Troubleshooting

**Issue**: Import errors when running

**Solution**: Make sure you're in the repository root directory. All imports are absolute from the root.

**Issue**: Skill not found in Claude Code

**Solution**: Reinstall using `/install https://github.com/yourusername/claude-legacy-analyzer`

## Requirements

- Python 3.8 or higher
- Git (optional, for history analysis features)

See `requirements.txt` for Python package dependencies.
