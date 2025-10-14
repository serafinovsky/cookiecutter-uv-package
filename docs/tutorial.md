# Setup Guide

Step-by-step guide to create a new Python project using our cookiecutter template.

## 1. Install cookiecutter

Install cookiecutter if not already installed:

```bash
pip install cookiecutter
```

## 2. Create project

Run cookiecutter with our template:

```bash
cookiecutter https://github.com/serafinovsky/cookiecutter-uv-package
```

You will be prompted to fill several configuration fields. For detailed description of all parameters, see [Prompt Arguments](prompt-arguments.md).

## 3. Setup development environment

Navigate to the created folder and setup development environment:

```bash
cd your-project-name
make dev-setup
```

This command will:

- Install all necessary dependencies
- Verify everything works correctly

## 4. Complete setup

Your generated project includes a detailed `SETUP.md` file with step-by-step instructions for:

- Creating GitHub repository
- Setting up required tokens (GitHub, PyPI, Codecov)
- Connecting your local repository
- Configuring CI/CD workflows

Follow the instructions in your project's `SETUP.md` file to complete the setup.

## Next steps

- Study [prompt arguments](prompt-arguments.md) to understand all available options
- Check [examples](examples.md) of template usage
- Review [features](features/index.md) of the template
