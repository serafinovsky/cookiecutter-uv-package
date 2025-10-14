# Cookiecuter Python Package

![License](https://img.shields.io/badge/license-MIT-green)
![Cookiecutter](https://img.shields.io/badge/cookiecutter-template-red)

**Modern cookiecutter template for creating Python packages with complete CI/CD setup and automatic PyPI publishing.**

## Quick Start

### Using cookiecutter directly

```bash
# Install cookiecutter
pip install cookiecutter

# Create project
cookiecutter https://github.com/serafinovsky/cookiecutter-uv-package

# Setup development environment
cd your-project-name
make dev-setup
```

### Using CLI tool

```bash
# Install the CLI tool
pip install cookiecutter-uv-package

# Create project with CLI
python-package-template

# Or with custom options
python-package-template --output-dir /path/to/projects --no-input

# Setup development environment
cd your-project-name
make dev-setup
```

## Key Features

### Modern Tools

Hatchling, uv, Ruff, MyPy, Pytest - latest Python development tools

[Learn more about modern tools →](features/index.md)

### CI/CD Ready

GitHub Actions with automatic PyPI publishing and release management

[Learn more about CI/CD →](features/ci-cd.md)

### Code Quality

Linting, typing, tests, security checks - all configured automatically

[Learn more about code quality →](features/code-quality.md)

### Docker Support

Optional Docker and devcontainer support for convenient development

## What You Get

- Ready Python package with proper structure
- CI/CD pipeline with GitHub Actions
- Automatic PyPI publishing
- Version management via Release Please
- Complete code quality setup
- Ready-to-use Makefile commands

## Documentation

- **[Setup Guide](tutorial.md)** - Step-by-step project creation guide
- **[Prompt Arguments](prompt-arguments.md)** - All configuration parameters
- **[Examples](examples.md)** - Template usage examples

## Example Project

See a real example of this template in action:
**[demo-example-package](https://github.com/serafinovsky/demo-example-package)**

## License

MIT License
