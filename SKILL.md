# Legacy Code Modernization Skill

## Installation

```bash
/install https://github.com/yourusername/claude-legacy-analyzer
```

## Overview

This skill enables me (Claude) to intelligently analyze and modernize legacy codebases **in ANY programming language**. I use lightweight helper tools to gather basic data, then apply my AI understanding to provide deep, contextual analysis and recommendations.

**Supports ALL languages**: Java, Python, JavaScript, TypeScript, Go, Rust, C++, C#, Ruby, PHP, Kotlin, Swift, Scala, Haskell, Elixir, Clojure, and any other programming language.

## How It Works

### Helper Tools (Language-Agnostic)
1. **File Finder** - Discovers code files across any language
2. **Basic Metrics** - Counts lines, estimates complexity patterns
3. **Git Analyzer** - Extracts change history and patterns

### My AI Analysis (The Intelligence)
I read and understand your code, then provide:
- **Semantic analysis** - Understanding what the code actually does
- **Context-aware recommendations** - Specific to your codebase
- **Real refactoring suggestions** - With actual code examples
- **Working test generation** - Real tests, not just templates
- **Architectural insights** - Based on understanding, not just patterns

## What I Do

### 1. Deep Code Understanding
When you ask me to analyze code, I:
- Read and comprehend the actual logic
- Understand business intent and responsibilities
- Identify complex or unclear sections
- Recognize patterns and anti-patterns
- Map dependencies and interactions

### 2. Intelligent Risk Assessment
I evaluate risk based on:
- **Semantic complexity** - Is the logic hard to follow?
- **Hidden assumptions** - Are there edge cases not handled?
- **Fragile coupling** - Will changes break other things?
- **Test coverage gaps** - Is critical logic untested?
- **Unclear intent** - Would a new developer understand this?

NOT just: "High cyclomatic complexity" ✗
BUT: "This method does 3 things: validation, notification, and persistence. If validation fails after sending an email, you'll have inconsistent state." ✓

### 3. Context-Aware Refactoring Plans
For each issue I identify, I provide:
- **WHY** it's problematic
- **SPECIFIC** code to extract/change
- **BEFORE/AFTER** examples with real implementation
- **IMPACT** assessment - what else might be affected
- **SAFE STEPS** - ordered sequence to minimize risk

### 4. Real Code Generation
I generate actual, working code:
- **Tests** - With meaningful test cases I derive from the logic
- **Refactored code** - Complete implementations, not templates
- **Migration scripts** - Step-by-step with actual commands
- **Documentation** - Explaining architectural decisions

### 5. Language-Specific Best Practices
I apply best practices for YOUR language:
- **Java**: SOLID principles, Spring patterns, stream API usage
- **Python**: Pythonic idioms, type hints, dataclasses
- **JavaScript/TypeScript**: Modern ES6+, async patterns, hooks
- **Go**: Idiomatic Go, error handling, goroutines
- **Rust**: Ownership, lifetimes, error handling with Result
- **Any language**: Framework conventions, community standards

## Usage Examples

### Example 1: Analyze Any Codebase

```
"Analyze my Rust project at ~/projects/my-rust-app for modernization opportunities"
```

I will:
1. Use FileFinder to discover all .rs files
2. Use BasicMetrics to get overview statistics
3. Use Git Analyzer to understand change patterns
4. **Read and understand your Rust code**
5. **Identify areas for improvement** (e.g., unnecessary clone(), missing error propagation)
6. **Suggest specific refactorings** with idiomatic Rust examples

### Example 2: Modernize Specific File

```
"Help me modernize UserService.java - it's a mess"
```

I will:
1. Read UserService.java thoroughly
2. Understand what it's trying to do
3. Identify the specific problems (not just "complexity 47")
4. Show you exactly how to refactor it:
   - Extract UserValidator with complete implementation
   - Create EmailNotificationService with real code
   - Update UserService to use them
5. Generate comprehensive JUnit tests with real test cases

### Example 3: Generate Tests

```
"Generate tests for payment_processor.py"
```

I will:
1. Read and understand the payment processing logic
2. Identify edge cases from the code:
   - Negative amounts
   - Invalid payment methods
   - Network failures
   - Partial refunds
3. Write pytest tests with realistic test data
4. Include fixtures for common test scenarios
5. Add comments explaining what each test validates

### Example 4: Architectural Analysis

```
"Analyze the architecture of my Express.js app and suggest improvements"
```

I will:
1. Map your route structure, middleware, and services
2. Identify architectural issues:
   - Controllers doing too much
   - Missing error handling layers
   - Inconsistent patterns
3. Suggest specific restructuring with code examples
4. Show migration path from current to improved structure

## My Methodology

### Phase 1: Discovery
- Find all code files (any language)
- Get basic metrics and git history
- Understand project structure

### Phase 2: Deep Analysis
- Read critical files thoroughly
- Understand business logic and intent
- Identify complexity hotspots
- Map dependencies

### Phase 3: Risk Assessment
- Evaluate semantic complexity
- Identify untested critical paths
- Find fragile coupling points
- Spot unclear or confusing code

### Phase 4: Recommendations
- Prioritize issues by risk and impact
- Suggest specific refactorings with code
- Provide step-by-step migration plans
- Generate tests and documentation

### Phase 5: Implementation Support
- Write actual refactored code
- Create comprehensive tests
- Review proposed changes
- Answer questions about the approach

## Safety Principles

1. **Test First** - I always recommend adding tests before refactoring
2. **Small Steps** - Break changes into reviewable chunks
3. **Backward Compatible** - Maintain existing interfaces when possible
4. **Rollback Ready** - Every change should be easily revertable
5. **Explain Trade-offs** - I'll tell you pros/cons of each approach

## When to Use This Skill

Use this skill when you want to:
- ✅ Understand unfamiliar legacy code
- ✅ Safely refactor complex code
- ✅ Improve test coverage strategically
- ✅ Modernize to current best practices
- ✅ Prepare code for new features
- ✅ Reduce technical debt systematically
- ✅ Get architectural guidance
- ✅ Generate tests for existing code

## What Makes This Different

**Traditional Static Analysis Tools**:
- Count metrics blindly
- Generic, one-size-fits-all suggestions
- No understanding of intent
- Template-based output

**Me (With This Skill)**:
- Understand what your code does and why
- Context-specific recommendations
- Real code examples in your language
- Explain the reasoning behind suggestions
- Adapt to your project's conventions
- Consider your business constraints

## Examples of My Analysis

### Bad (Static Tool):
```
UserService.java: Complexity 47 (HIGH)
Recommendation: Reduce complexity
```

### Good (Me):
```
UserService.java has 3 distinct responsibilities that should be separated:

1. User Validation (lines 45-120)
   - Contains email format checking, password strength validation
   - Should be: UserValidator.java
   - Why: Validation logic is complex and will grow with new rules

2. Email Notifications (lines 121-180)
   - Sends welcome emails, confirmation emails
   - Should be: EmailNotificationService.java
   - Why: Tightly couples user management to email provider

3. Database Operations (lines 181-220)
   - User CRUD operations
   - Should be: UserRepository.java
   - Why: Follows repository pattern used elsewhere in your code

Here's the specific refactoring:

[Shows actual code for UserValidator]
[Shows actual code for EmailNotificationService]
[Shows updated UserService]
[Shows complete tests for each]

Migration steps:
1. Create UserValidatorTest.java [shows tests]
2. Extract UserValidator.java [shows code]
3. Update UserService to use validator
4. Run tests to verify behavior unchanged
...
```

## Supported Languages

✅ **ALL** programming languages, including but not limited to:

**Compiled Languages**: Java, C, C++, C#, Go, Rust, Swift, Kotlin, Scala, Haskell, OCaml, F#

**Scripting Languages**: Python, JavaScript, TypeScript, Ruby, PHP, Perl, Lua, Shell

**Functional Languages**: Haskell, Elixir, Clojure, Erlang, F#, OCaml, Elm

**Systems Languages**: C, C++, Rust, Go, Zig

**JVM Languages**: Java, Kotlin, Scala, Groovy, Clojure

**.NET Languages**: C#, F#, VB.NET

**Mobile**: Swift, Objective-C, Kotlin, Dart (Flutter)

**Web**: JavaScript, TypeScript, PHP, Ruby, Python

**Data Science**: R, Julia, Python, MATLAB

**And any other language!** If it's code, I can understand and help modernize it.

## Philosophy

I don't just count metrics - I understand your code and help you improve it intelligently. Every recommendation is specific, actionable, and explained with clear reasoning.

**Remember**: The tools gather data. I provide the intelligence.
