# Makefile

Our template includes a convenient Makefile with ready commands for all main development tasks.

## Main Commands

### Development Environment Setup

```bash
make dev-setup
```

**What it does:**

- Installs all dependencies
- Verifies everything works correctly

### Testing

```bash
make test
```

**What it does:**

- Runs all tests with pytest
- Generates coverage reports
- Creates HTML report in `htmlcov/` folder

### Code Quality Checking

```bash
make check
```

**What it does:**

- Runs linting with Ruff
- Checks types with MyPy
- Checks security with Bandit
- Checks code formatting
- Run tests

### Formatting

```bash
make format
```

**What it does:**

- Formats code with Ruff
- Sorts imports
- Fixes automatically fixable issues

### Package Building

```bash
make build
```

**What it does:**

- Builds wheel and source distribution
- Verifies package builds correctly
- Creates files in `dist/` folder

### Cleanup

```bash
make clean
```

**What it does:**

- Removes temporary files
- Cleans Python cache
- Removes built packages
- Removes coverage reports

## Benefits

- **Simplicity**: One command for complex operations
- **Consistency**: Same commands for all developers
- **Documentation**: Built-in help
- **Automation**: Minimal manual work
- **Standardization**: Unified development approach
- **CI/CD Ready**: Commands ready for pipeline use
