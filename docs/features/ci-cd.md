# CI/CD with GitHub Actions

Complete CI/CD pipeline setup with GitHub Actions for automating all aspects of development workflow.

## Workflow Files

### checks.yml - Main Checks

Runs on every push and pull request to ensure code quality:

- Linting with Ruff
- Type checking with MyPy
- Security scanning with Bandit
- Code formatting verification

### coverage.yml - Code Coverage

Measures and reports test coverage:

- Runs test suite with coverage measurement
- Uploads results to Codecov

### release-please.yml - Release Management

Manages version bumps and changelog generation:

- Automatically creates release PRs based on conventional commits
- Updates version numbers and CHANGELOG.md
- Creates GitHub releases when PRs are merged

### publish.yml - PyPI Publishing

Automatically publishes packages to PyPI when releases are created:

- Builds the package using Hatchling
- Publishes to PyPI using secure token authentication
- Only runs when GitHub releases are published

### uv-update.yml - Dependency Updates

Keeps dependencies up to date:

- Weekly updates of Python dependencies
- Automatic PR creation for dependency updates
- Maintains lock file consistency

### setup-protection.yml - Branch Protection

Configures branch protection rules:

- Requires status checks before merging
- Enforces up-to-date branches
- Protects main branch from force pushes

## Required Secrets

For full functionality, configure these secrets in your GitHub repository:

### REPO_ADMIN_TOKEN

Personal Access Token with repository permissions for Release Please workflow.

### PYPI_API_TOKEN

PyPI API token for package publishing (only needed for github-ci-pypi setup).

### CODECOV_TOKEN

Codecov token for coverage report uploads.

## Benefits

- **Complete automation** - No manual intervention needed for releases
- **Quality assurance** - Multiple code quality checks on every change
- **Security** - Automated security scanning and protected branches
- **Transparency** - Detailed logs and reports for all operations
- **Reliability** - Battle-tested workflows used in production projects
