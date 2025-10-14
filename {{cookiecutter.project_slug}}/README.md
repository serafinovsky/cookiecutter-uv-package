[![CI/CD]({{ cookiecutter.repository_url }}/actions/workflows/checks.yml/badge.svg)]({{ cookiecutter.repository_url }}/actions/workflows/release-please.yml)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})]({{ cookiecutter.repository_url }}/releases)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
{% if cookiecutter.deployment_setup == 'github-ci-pypi' -%}
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg)](https://badge.fury.io/py/{{ cookiecutter.project_slug }})
[![Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
{% endif -%}
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked with mypy](https://img.shields.io/badge/mypy-checked-blue.svg)](http://mypy-lang.org/)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
{% if cookiecutter.license == 'MIT' -%}
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
{% elif cookiecutter.license == 'Apache-2.0' -%}
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
{% elif cookiecutter.license == 'BSD-3-Clause' -%}
[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
{% elif cookiecutter.license == 'GPL-3.0' -%}
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)
{% elif cookiecutter.license == 'ISC' -%}
[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
{% endif -%}

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Documentation

- **[Setup Guide]({{ cookiecutter.repository_url }}/blob/main/SETUP.md)** - Initial project configuration
- **[Development Workflow]({{ cookiecutter.repository_url }}/blob/main/WORKFLOW.md)** - How to contribute and work with the project
