# Python Package Template

**Cookiecutter template for creating Python packages with complete CI/CD setup and automatic PyPI publishing.**

## 🚀 Features

- **Modern tools**: Hatchling, uv, Ruff, MyPy, Pytest
- **CI/CD out of the box**: GitHub Actions with automatic PyPI publishing
- **Release management**: Release Please + Conventional Commits
- **Code quality**: linting, typing, tests, security checks
- **Ready commands**: Makefile for all development tasks

## 🛠️ Quick Start

```bash
# Install cookiecutter
pip install cookiecutter

# Create project
cookiecutter https://github.com/serafinovsky/cookiecutter-python-package

# Setup development environment
cd your-project-name
make dev-setup
```

## ⚙️ Configuration Options

When creating a project, you'll be asked to configure:

- **project_name**: Display name for your package (e.g., "My Awesome Package")
- **project_short_description**: Brief description of what your package does
- **author_name**: Your name
- **author_email**: Your email address
- **github_username**: Your GitHub username
- **python_versions**: Supported Python versions (default: "3.11, 3.12, 3.13")
- **use_docker**: Whether to include Docker support (yes/no)
- **publish_to_pypi**: Whether to set up PyPI publishing (yes/no)

## 🔧 Main Commands

```bash
make dev-setup     # Setup development environment
make test          # Run tests
make check         # Check code
make format        # Format code
make build         # Build package
```

## 📁 What You Get

- Ready Python package with proper structure
- CI/CD pipeline with GitHub Actions
- Automatic PyPI publishing
- Version management via Release Please

## 📄 License

MIT License
