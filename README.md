# Python Package Template

![Cookiecutter](https://img.shields.io/badge/cookiecutter-template-red)
[![Tests passed](https://github.com/serafinovsky/cookiecutter-uv-package/workflows/Checks/badge.svg)](https://github.com/serafinovsky/cookiecutter-uv-package/actions)
![License](https://img.shields.io/badge/license-MIT-green)
![Tox](https://img.shields.io/badge/tox-multi--version-blue)
![Pytest](https://img.shields.io/badge/pytest-testing-blue)
![Ruff](https://img.shields.io/badge/ruff-linting-blue)
[![Documentation](https://img.shields.io/badge/docs-latest-blue)](https://serafinovsky.github.io/cookiecutter-uv-package)

**Cookiecutter template for creating Python packages with complete CI/CD setup and automatic PyPI publishing.**

## Features

- **Modern tools**: Hatchling, uv, Ruff, MyPy, Pytest
- **CI/CD out of the box**: GitHub Actions with automatic PyPI publishing
- **Release management**: Release Please + Conventional Commits
- **Code quality**: linting, typing, tests, security checks
- **Ready commands**: Makefile for all development tasks

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

# Get help with available arguments
cookiecutter-uv-package --help

# Create project with CLI
python-package-template

# Or with custom options
python-package-template --output-dir /path/to/projects --no-input

# Setup development environment
cd your-project-name
make dev-setup
```

## Configuration Options

When creating a project, you'll be asked to configure:

- **project_name**: Display name for your package (e.g., "My Awesome Package")
- **project_short_description**: Brief description of what your package does
- **author_name**: Your name
- **author_email**: Your email address
- **github_username**: Your GitHub username
- **python_versions**: Supported Python versions (default: "3.11, 3.12, 3.13")
- **use_docker**: Whether to include Docker support (yes/no)
- **deployment_setup**: Choose deployment setup (none/github-ci/github-ci-pypi)
- **license**: Choose license (MIT/Apache-2.0/BSD-3-Clause/GPL-3.0/ISC/none)

## Main Commands

```bash
make dev-setup     # Setup development environment
make test          # Run tests
make check         # Check code
make format        # Format code
make build         # Build package
```

## What You Get

- Ready Python package with proper structure
- CI/CD pipeline with GitHub Actions
- Automatic PyPI publishing
- Version management via Release Please

## Example Project

See a real example of this template in action:
**[demo-example-package](https://github.com/serafinovsky/demo-example-package)**

## Documentation

- **[Full Documentation](https://serafinovsky.github.io/cookiecutter-uv-package)** - Complete guide and reference
- **[Tutorial](https://serafinovsky.github.io/cookiecutter-uv-package/tutorial/)** - Step-by-step setup guide
- **[Features](https://serafinovsky.github.io/cookiecutter-uv-package/features/)** - Detailed feature descriptions
- **[Examples](https://serafinovsky.github.io/cookiecutter-uv-package/examples/)** - Usage examples and scenarios

## License

MIT License
