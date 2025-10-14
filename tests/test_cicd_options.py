from helpers import (
    assert_file_contains,
    assert_file_exists,
    assert_file_not_exists,
    cleanup_project,
    get_default_context,
    get_template_dir,
    run_cookiecutter,
)


class TestCICDOptions:
    """Test CI/CD option functionality."""

    def test_github_ci_cd(self):
        """Test GitHub CI/CD generation."""
        template_dir = get_template_dir()
        context = get_default_context()
        context["deployment_setup"] = "github-ci"

        project_path = run_cookiecutter(template_dir, context)

        try:
            # Check that GitHub Actions files exist
            assert_file_exists(project_path, ".github/workflows/checks.yml")
            assert_file_exists(project_path, ".github/workflows/coverage.yml")
            assert_file_exists(project_path, ".github/workflows/release-please.yml")
            assert_file_exists(project_path, ".github/workflows/setup-protection.yml")
            assert_file_exists(project_path, ".github/workflows/uv-update.yml")
            assert_file_exists(project_path, ".github/dependabot.yml")

            # Check that release-please files exist
            assert_file_exists(project_path, "release-please-config.json")
            assert_file_exists(project_path, ".release-please-manifest.json")
        finally:
            cleanup_project(project_path)

    def test_github_ci_cd_with_pypi_publishing(self):
        """Test GitHub CI/CD with PyPI publishing enabled."""
        template_dir = get_template_dir()
        context = get_default_context()
        context["deployment_setup"] = "github-ci-pypi"
        project_path = run_cookiecutter(template_dir, context)
        try:
            # Check that publish workflow exists
            assert_file_exists(project_path, ".github/workflows/publish.yml")
        finally:
            cleanup_project(project_path)

    def test_no_ci_cd(self):
        """Test project generation without CI/CD."""
        template_dir = get_template_dir()
        context = get_default_context()
        context["deployment_setup"] = "none"

        project_path = run_cookiecutter(template_dir, context)

        try:
            # Check that GitHub Actions directory does not exist
            assert_file_not_exists(project_path, ".github")

            # Check that release-please files do not exist
            assert_file_not_exists(project_path, "release-please-config.json")
            assert_file_not_exists(project_path, ".release-please-manifest.json")
        finally:
            cleanup_project(project_path)

    def test_github_workflows_content(self):
        """Test that GitHub workflows contain expected content."""
        template_dir = get_template_dir()
        context = get_default_context()
        context["deployment_setup"] = "github-ci"
        context["python_versions"] = "3.11, 3.12"
        project_path = run_cookiecutter(template_dir, context)
        try:
            # Check checks.yml content
            assert_file_contains(project_path, ".github/workflows/checks.yml", "3.11")
            assert_file_contains(project_path, ".github/workflows/checks.yml", "3.12")

            # Check coverage.yml content (it uses only one Python version)
            assert_file_contains(project_path, ".github/workflows/coverage.yml", "3.11")
        finally:
            cleanup_project(project_path)
