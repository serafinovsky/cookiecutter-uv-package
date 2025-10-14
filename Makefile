.PHONY: help test lint security format build check update-deps dev-setup version tags docs-serve clean tox

help: ## Show help
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


test: ## Run tests
	@make update-deps
	uv run pytest

lint: ## Check code with linters
	@make update-deps
	uv run ruff check hooks/ --preview
	uv run ruff check tests/ --preview
	uv run ruff check cookiecutter_uv_package/ --preview
	uv run ruff format hooks/
	uv run ruff format tests/
	uv run ruff format cookiecutter_uv_package/

security: ## Run security checks
	@make update-deps
	@uv run bandit -c pyproject.toml -r . -f json -o bandit-report.json

format: ## Format code
	@make update-deps
	uv run ruff format hooks/
	uv run ruff format tests/
	uv run ruff format cookiecutter_uv_package/
	uv run ruff check hooks/ --preview --fix
	uv run ruff check tests/ --preview --fix
	uv run ruff check cookiecutter_uv_package/ --preview --fix

build: ## Build package
	@make update-deps
	uv build

check: ## Full pre-commit check
	@make update-deps
	@make lint
	@make test
	@make security

update-deps: ## Update dependencies and regenerate uv.lock
	uv lock

dev-setup: ## Setup development environment
	@make update-deps
	@uv sync --dev

version: ## Show current version
	@make update-deps
	@uv run python -c "import cookiecutter_uv_package; print(cookiecutter_uv_package.__version__)"

tags: ## List all git tags
	@git tag --sort=-version:refname

docs-serve: ## Serve documentation locally
	@make update-deps
	uv run mkdocs serve

tox: ## Run tests with tox on multiple Python versions
	@make update-deps
	uv run tox

clean: ## Clean temporary files
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
	find . -type f -name "coverage.xml" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type f -name "bandit-report.json" -delete
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name ".tox" -exec rm -rf {} +
	find . -type d -name "site" -exec rm -rf {} +
	find . -type d -name ".tox" -exec rm -rf {} +