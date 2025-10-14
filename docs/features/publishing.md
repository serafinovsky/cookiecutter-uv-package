# Publishing to PyPI

Our template includes complete setup for automatic package publishing to PyPI.

## Automatic Publishing

### What Happens on Release

1. **Release Please** creates release automatically based on conventional commits
2. **Publishing workflow** triggers when GitHub release is created
3. **Package building** with Hatchling
4. **PyPI publishing** using API token
5. **Status notifications**

## Token Setup

Your generated project includes detailed token setup instructions in the `SETUP.md` file with step-by-step guidance for configuring PyPI API tokens and other required secrets.

## Version Management

### Release Please

Automatic version management via [Release Please](https://github.com/googleapis/release-please):

### Conventional Commits

Use standard commit messages:

```bash
# New features
git commit -m "feat: add new feature"

# Bug fixes
git commit -m "fix: resolve issue with data processing"

# API changes
git commit -m "feat!: remove paramert. BREAKING CHANGE: change API signature"
```

### Automatic Release Creation

1. **Commits** with conventional commits
2. **Release Please** analyzes changes
3. **Automatic creation** of Pull Request with changelog
4. **Merge PR** creates release
5. **Automatic publishing** to PyPI

## Publishing Monitoring

### README Badges

```markdown
[![PyPI version](https://badge.fury.io/py/your-package.svg)](https://badge.fury.io/py/your-package)
[![Python Versions](https://img.shields.io/pypi/pyversions/your-package.svg)](https://pypi.org/project/your-package/)
[![Downloads](https://pepy.tech/badge/your-package)](https://pepy.tech/project/your-package)
```

### Download Statistics

- [pepy.tech](https://pepy.tech/) - download statistics
- [pypistats.org](https://pypistats.org/) - PyPI analytics
- [libraries.io](https://libraries.io/) - dependency tracking

## Benefits

- **Automation**: Publishing happens automatically
- **Security**: API token usage
- **Reliability**: Testing before publishing
- **Transparency**: Full process logs
- **Speed**: Fast publishing via GitHub Actions
- **Standardization**: Following PyPI best practices
