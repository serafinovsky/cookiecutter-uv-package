# Prompt Arguments

When running the `cookiecutter` command, an interactive prompt will start to configure your repository. Below are all prompt values and their explanations:

---

## **project_name**

Human-readable project name. This will be displayed in documentation and package metadata.

**Example:** `My Awesome Package`

---

## **project_short_description**

Brief description of your project. This will be displayed in documentation and package metadata.

**Example:** `A modern Python package for data processing`

---

## **author_name**

Your full name.

**Example:** `John Doe`

---

## **author_email**

Your email address.

**Example:** `john.doe@example.com`

---

## **github_username**

Your GitHub username, i.e. `<handle>` in `https://github.com/<handle>`

**Example:** `johndoe`

---

## **python_versions**

Supported Python versions. Default: `3.11, 3.12, 3.13`

**Example:** `3.11, 3.12, 3.13`

---

## **use_docker**

`"no"` or `"yes"`. Adds Docker support to the project.

- `"no"`: No Docker files added
- `"yes"`: Adds `Dockerfile` and `docker-compose.yml`

---

## **deployment_setup**

Choose deployment configuration:

- `"none"`: No CI/CD
- `"github-ci"`: GitHub Actions for checks and tests
- `"github-ci-pypi"`: GitHub Actions + automatic PyPI publishing

---

## **license**

Choose license:

- `"MIT"`: MIT License
- `"Apache-2.0"`: Apache Software License 2.0
- `"BSD-3-Clause"`: BSD 3-Clause License
- `"GPL-3.0"`: GNU General Public License v3
- `"ISC"`: ISC License
- `"none"`: No license

---

## Example interactive prompt

```bash
$ cookiecutter https://github.com/serafinovsky/cookiecutter-uv-package

project_name [My Python Package]: Data Processor
project_short_description [A modern Python package with complete CI/CD setup]: Advanced data processing library
author_name [Your Name]: John Doe
author_email [your.email@example.com]: john.doe@example.com
github_username [yourusername]: johndoe
python_versions [3.11, 3.12, 3.13]: 3.11, 3.12, 3.13
use_docker [no]: yes
deployment_setup [none]: github-ci-pypi
license [MIT]: MIT
```

After completing the prompt, a `data-processor` folder will be created with a ready Python package.
