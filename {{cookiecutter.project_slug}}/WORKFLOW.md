# 🔄 Development Workflow

## Feature Branch Development

All development happens in feature branches:

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and commit
git add .
git commit -m "feat: add new feature"

# Push and create PR
git push origin feature/your-feature-name
```

## Conventional Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - new feature (minor version bump)
- `fix:` - bug fix (patch version bump)
- `BREAKING CHANGE:` - breaking change (major version bump)
- `docs:`, `refactor:`, `perf:`, `chore:` - no version bump

```bash
git commit -m "feat: add user authentication"
git commit -m "fix: resolve login validation issue"
git commit -m "chore: update dependencies"
```

## Release Process

Releases are automated using [Release Please](https://github.com/googleapis/release-please):

1. **Merge PRs** to `main` branch
2. **Release Please** automatically:
   - Generates changelog from conventional commits
   - Creates release PR with version bump
   - Publishes to PyPI (if configured)
3. **Merge release PR** to trigger release
