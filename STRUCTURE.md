# Project Structure

```
claude-legacy-analyzer/                  ← Repository root
│
├── SKILL.md                             ← Claude Code skill manifest ⭐
├── README.md                            ← Main documentation
├── INSTALL.md                           ← Installation instructions
├── STRUCTURE.md                         ← This file
├── LICENSE                              ← MIT License
├── .gitignore                           ← Git ignore rules
│
├── requirements.txt                     ← Minimal Python dependencies
├── config.yaml                          ← Optional configuration
│
└── tools/                               ← Language-agnostic helper tools
    ├── __init__.py
    ├── file_finder.py                   ← Find code files (50+ languages)
    ├── basic_metrics.py                 ← Universal line counts & patterns
    └── git_analyzer.py                  ← Git history analysis
```

## Key Points

✅ **SKILL.md at root** - Required for `/install` command
✅ **Minimal structure** - Only essential files
✅ **Language-agnostic tools** - Work with ANY programming language
✅ **AI-powered** - Claude does the intelligent analysis

## Architecture

```
Helper Tools (Python)           Claude's AI (The Intelligence)
──────────────────────         ────────────────────────────────
📁 file_finder.py         ──>   🧠 Read and understand code
📊 basic_metrics.py       ──>   🎯 Identify semantic issues
🔍 git_analyzer.py        ──>   ✍️ Suggest refactorings
                                 🧪 Generate real tests
                                 📋 Create migration plans
```

**The tools gather data. Claude provides the intelligence.**

## Installation

```bash
/install https://github.com/yourusername/claude-legacy-analyzer
```

Done! The skill is ready to use with any codebase in any language.
