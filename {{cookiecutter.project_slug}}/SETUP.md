# 🚀 Project Setup

## 1. Development Environment Setup

[Install uv (if not already installed)](https://docs.astral.sh/uv/getting-started/installation/)

```bash
make dev-setup
make check
```

## 2. Initialize Git Repository

```bash
git init
git add .
git commit -m "chore: initial commit"
```

## 3. Create and Configure Repository

### 3.1. Create GitHub Repository

- Go to [github.com/new](https://github.com/new)
- Repository name: `{{ cookiecutter.project_slug }}`
- Description: `{{ cookiecutter.project_short_description }}`

### 3.2. Configure Tokens

#### Personal Access Token (for repository access)

1. **Create Personal Access Token:**

   - Go to [GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)](https://github.com/settings/tokens)
   - Click "Generate new token (classic)"
   - **Note:** `{{ cookiecutter.project_slug }}-development`
   - **Expiration:** choose appropriate duration
   - **Scopes:** select required permissions (repo, workflow, write:packages, admin:repo_hook)
   - Click "Generate token"
   - **Copy the token** (it's shown only once!)

2. **Add token to GitHub Secrets:**

   - Go to your repository: [github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/secrets/actions](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/secrets/actions)
   - Click "New repository secret"
   - **Name:** `REPO_ADMIN_TOKEN`
   - **Secret:** paste your Personal Access Token
   - Click "Add secret"

{% if cookiecutter.deployment_setup == 'github-ci-pypi' -%}

#### PyPI API Token (for publishing)

1. **Create PyPI API Token:**

   - Go to [pypi.org/manage/account/token/](https://pypi.org/manage/account/token/)
   - Click "Add API token"
   - **Token name:** `{{ cookiecutter.project_slug }}-publish`
   - **Scope:** Entire account
   - **Expiration:** set appropriate date
   - **Copy the token** (it's shown only once!)

2. **Add token to GitHub Secrets:**

   - Go to your repository: [github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/secrets/actions](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/secrets/actions)
   - Click "New repository secret"
   - **Name:** `PYPI_API_TOKEN`
   - **Secret:** paste your PyPI API token
   - Click "Add secret"

{% endif -%}

#### Codecov Token (for code coverage)

1. **Get Codecov Token:**

   - Go to [codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/new](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/new)
   - Copy the **Repository Upload Token**

2. **Add token to GitHub Secrets:**
   - Go to your repository: [github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/secrets/actions](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/secrets/actions)
   - Click "New repository secret"
   - **Name:** `CODECOV_TOKEN`
   - **Secret:** paste your Codecov token
   - Click "Add secret"

## 4. Connect Local Repository

```bash
git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
git branch -M main
git push -u origin main
```

## 5. Verify setup

After setup:

1. **Check that CI/CD works:**

   - Go to Actions tab in your GitHub repository
   - Ensure all workflows run successfully
