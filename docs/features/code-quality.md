# Linting and Code Quality

Our template includes a complete set of tools for maintaining high code quality.

## Code Quality Tools

### 1. **Ruff** - Ultra-fast Linter and Formatter

Ruff replaces multiple tools with one fast solution:

```toml
[tool.ruff]
target-version = "py311"
line-length = 120
respect-gitignore = true

[tool.ruff.lint]
select = [
    "E",        # pycodestyle errors
    "W",        # pycodestyle warnings
    "F",        # pyflakes
    "I",        # isort
    "B",        # flake8-bugbear
    "C4",       # flake8-comprehensions
    "UP",       # pyupgrade
    "ASYNC",    # async/await rules
    "S",        # security rules
    "LOG",      # logging best practices
    "Q",        # quotes standardization
    "SLF",      # private member access
    "SIM",      # code simplification
    "TC",       # type checking
    "ARG",      # unused arguments
    "PTH",      # pathlib best practices
    "N",        # naming conventions
    "T20"       # print statement usage
]
```

**What is checked:**

- Code style (PEP 8)
- Imports and sorting
- Potential bugs
- Security
- Performance
- Best practices

### 2. **MyPy** - Static Typing

```toml
[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
```

**Functions:**

- Type checking during development
- Error detection before execution
- Better code readability
- Enhanced IDE support

### 3. **Bandit** - Security Checking

```toml
[tool.bandit]
exclude_dirs = ["tests", "examples"]
skips = ["B101", "B601"]
```

**What is checked:**

- Security vulnerabilities
- Unsafe functions
- Password and token issues
- SQL injections
- Unsafe module usage

## Benefits

- **Speed**: Ruff works 10-100x faster than other linters
- **Completeness**: Covers all aspects of code quality
- **Automation**: Automatic checks prevent issues
- **Consistency**: Unified standards for the entire team
- **Security**: Automatic vulnerability detection
- **Typing**: Early type error detection
