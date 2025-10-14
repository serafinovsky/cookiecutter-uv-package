# Examples

Here are examples of using this cookiecutter template for different types of Python projects.

## Real Project Examples

**[demo-example-package](https://github.com/serafinovsky/demo-example-package)** - A complete example showing the template in action with full CI/CD, PyPI publishing, and documentation.

**[fastapi-redis-utils](https://github.com/serafinovsky/fastapi-redis-utils)** - A FastAPI Redis integration library created with this template, demonstrating real-world usage with complete CI/CD pipeline and PyPI publishing.

## Usage Scenarios

### Simple Library

For a basic library without publishing:

```bash
cookiecutter https://github.com/serafinovsky/cookiecutter-uv-package

# Choose these options:
deployment_setup: github-ci
use_docker: no
license: MIT
```

**Result:** Basic package with testing and code quality checks, but no PyPI publishing.

### Full Production Package

For a package you plan to publish and maintain:

```bash
cookiecutter https://github.com/serafinovsky/cookiecutter-uv-package

# Choose these options:
deployment_setup: github-ci-pypi
use_docker: yes
license: MIT
```

**Result:** Complete setup with automatic PyPI publishing, Docker support, and comprehensive CI/CD.

### Internal Tool

For company-internal tools:

```bash
cookiecutter https://github.com/serafinovsky/cookiecutter-uv-package

# Choose these options:
deployment_setup: none
use_docker: yes
license: none
```

**Result:** Minimal CI/CD with Docker support for internal deployment.
