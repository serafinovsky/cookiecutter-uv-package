[![CI/CD]({{ cookiecutter.repository_url }}/actions/workflows/checks.yml/badge.svg)]({{ cookiecutter.repository_url }}/actions/workflows/release-please.yml)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})]({{ cookiecutter.repository_url }}/releases)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
{% if cookiecutter.publish_to_pypi == 'yes' -%}
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg)](https://badge.fury.io/py/{{ cookiecutter.project_slug }})
[![Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
{% endif -%}
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked with mypy](https://img.shields.io/badge/mypy-checked-blue.svg)](http://mypy-lang.org/)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Documentation

- **[Setup Guide]({{ cookiecutter.repository_url }}/blob/main/SETUP.md)** - Initial project configuration
- **[Development Workflow]({{ cookiecutter.repository_url }}/blob/main/WORKFLOW.md)** - How to contribute and work with the project
