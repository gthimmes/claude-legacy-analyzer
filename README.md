# AI-Powered Legacy Code Modernization

> **Claude analyzes and modernizes legacy code in ANY programming language - intelligently, safely, systematically.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Works with ALL Languages](https://img.shields.io/badge/languages-ALL-brightgreen.svg)]()

---

## The Problem

Every engineering team has legacy code that's hard to maintain:

- Engineers avoid touching it
- Changes break production
- Simple features take weeks
- Technical debt compounds

**This happens in every language** - Java, Python, JavaScript, Go, Rust, and everything else.

## The Solution

**Claude + Language-Agnostic Tools = Intelligent Modernization for ANY Codebase**

Unlike static analysis tools that just count metrics, this plugin lets Claude **understand your code semantically** and provide specific, actionable recommendations with real implementations.

---

## Installation

```bash
# Step 1: Add the marketplace
/plugin marketplace add gthimmes/claude-legacy-analyzer

# Step 2: Install the plugin
/plugin install legacy-analyzer@gthimmes
```

That's it!

---

## Usage

Just ask Claude naturally:

```
"Analyze my Rust project at ~/code/my-app for modernization opportunities"

"Help me refactor this messy Python class - payment_processor.py"

"Generate comprehensive tests for UserService.java"

"Review my Go codebase and suggest architectural improvements"
```

Claude will:
1. **Understand your code** (not just count metrics)
2. **Identify real issues** (semantic, not just patterns)
3. **Show specific fixes** (actual code, not templates)
4. **Generate working tests** (real test cases)
5. **Explain the reasoning** (learn why, not just what)

---

## What Makes This Different

### Traditional Static Analysis

```
SonarQube: "Complexity 47 - reduce complexity"
ESLint: "Function too long"
RuboCop: "Class has too many lines"

Generic, unhelpful, no context.
```

### This Plugin (AI-Powered)

```
Claude: "This class has 3 responsibilities that should be separated:

1. User Validation (lines 45-120)
   Problem: Mixes business rules with input validation
   Solution: Extract to UserValidator class
   Here's the code: [shows working implementation]

2. Email Notifications (lines 121-180)
   Problem: Couples user management to email provider
   Solution: Extract to EmailNotificationService
   Here's how: [shows real refactoring]

I've also generated comprehensive tests with edge cases..."

Specific, actionable, intelligent.
```

---

## Supports ALL Languages

| Enterprise | Systems | Functional |
|------------|---------|------------|
| Java, Kotlin, Scala | Rust, Go, C, C++ | Haskell, OCaml, Elm |
| C#, F#, VB.NET | Swift, Objective-C | Elixir, Erlang |
| TypeScript, JavaScript | Zig | Clojure |
| Python, Ruby, PHP | | |

**And literally any other language!** If it's code, Claude can understand and help modernize it.

---

## Features

### AI-Powered Analysis
- **Semantic understanding** - Knows what code does, not just syntax
- **Context-aware** - Adapts to your project's patterns
- **Language-specific best practices** - Idiomatic suggestions for each language

### Smart Refactoring
- **Specific code suggestions** - Not generic advice
- **Complete implementations** - Real code you can use
- **Step-by-step migration** - Safe, incremental changes

### Real Test Generation
- **Meaningful test cases** - Derived from understanding your logic
- **Edge case identification** - Finds scenarios you might miss
- **Framework-appropriate** - JUnit, pytest, Jest, etc.

---

## Architecture

```
Helper Tools (Python)           Claude's AI (The Intelligence)
──────────────────────         ────────────────────────────────
file_finder.py            ──>   Read and understand code
basic_metrics.py          ──>   Identify semantic issues
git_analyzer.py           ──>   Suggest refactorings
                                Generate real tests
                                Create migration plans
```

**Key**: Tools = Fast data gathering. Claude = Intelligent analysis.

---

## Project Structure

```
claude-legacy-analyzer/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace catalog
├── plugins/
│   └── legacy-analyzer/
│       ├── .claude-plugin/
│       │   └── plugin.json       # Plugin manifest
│       ├── skills/
│       │   └── legacy-analyzer/
│       │       └── SKILL.md      # Skill instructions
│       └── tools/                # Helper tools
│           ├── file_finder.py
│           ├── basic_metrics.py
│           └── git_analyzer.py
├── README.md
└── LICENSE
```

---

## Quick Reference

### Install
```bash
/plugin marketplace add gthimmes/claude-legacy-analyzer
/plugin install legacy-analyzer@gthimmes
```

### Use
```
"Analyze [path] for modernization"
"Help me refactor [file]"
"Generate tests for [class]"
"Review [codebase] architecture"
```

### Languages
ALL of them! Java, Python, JS, TS, Go, Rust, C++, C#, Ruby, PHP, Kotlin, Swift, and literally any other language.

---

## License

MIT License - see [LICENSE](LICENSE)

---

**Claude understands your code. Let's make it better.**
