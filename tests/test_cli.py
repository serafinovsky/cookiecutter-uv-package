import tempfile
from pathlib import Path
from unittest.mock import patch

from click.testing import CliRunner
from helpers import (
    assert_file_contains,
    assert_file_exists,
    assert_file_not_exists,
    cleanup_project,
)

from cookiecutter_uv_package.cli import get_template_dir, main


class TestGetTemplateDir:
    """Test the get_template_dir function."""

    def test_get_template_dir_returns_correct_path(self):
        """Test that get_template_dir returns the correct template directory path."""
        template_dir = get_template_dir()

        # Should point to the project root directory
        assert_file_exists(template_dir, "/")
        assert_file_exists(template_dir, "cookiecutter.json")
        assert_file_exists(template_dir, "{{cookiecutter.project_slug}}")


class TestCLIMain:
    """Test the main CLI function."""

    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_help_command(self):
        """Test that the help command works correctly."""
        result = self.runner.invoke(main, ["--help"])

        assert result.exit_code == 0
        assert "Create a new Python package using a modern cookiecutter template" in result.output
        assert "--output-dir" in result.output
        assert "--no-input" in result.output
        assert "--replay" in result.output
        assert "--overwrite-if-exists" in result.output
        assert "--skip-if-file-exists" in result.output
        assert "--config-file" in result.output

    def test_version_command(self):
        """Test that the version command works correctly."""
        result = self.runner.invoke(main, ["--version"])

        assert result.exit_code == 0
        assert "version" in result.output.lower()

    @patch("cookiecutter_uv_package.cli.cookiecutter")
    def test_basic_project_creation(self, mock_cookiecutter):
        """Test basic project creation with default options."""
        with tempfile.TemporaryDirectory() as mock_project_dir:
            mock_cookiecutter.return_value = mock_project_dir

        with tempfile.TemporaryDirectory() as temp_dir:
            result = self.runner.invoke(main, ["--output-dir", temp_dir, "--no-input"])

            assert result.exit_code == 0
            assert "Creating new Python package..." in result.output
            assert "Project successfully created at:" in result.output
            assert "Next steps:" in result.output

            # Verify cookiecutter was called with correct arguments
            mock_cookiecutter.assert_called_once()
            call_args = mock_cookiecutter.call_args

            assert call_args[1]["output_dir"] == temp_dir
            assert call_args[1]["no_input"] is True
            assert call_args[1]["replay"] is False
            assert call_args[1]["overwrite_if_exists"] is False
            assert call_args[1]["skip_if_file_exists"] is False
            assert call_args[1]["config_file"] is None

    @patch("cookiecutter_uv_package.cli.cookiecutter")
    def test_project_creation_with_all_flags(self, mock_cookiecutter):
        """Test project creation with all CLI flags enabled."""
        with tempfile.TemporaryDirectory() as temp_dir, tempfile.TemporaryDirectory() as mock_project_dir:
            mock_cookiecutter.return_value = mock_project_dir
            config_file = Path(temp_dir) / "config.yaml"
            config_file.write_text("test: config")

            result = self.runner.invoke(
                main,
                [
                    "--output-dir",
                    temp_dir,
                    "--no-input",
                    "--replay",
                    "--overwrite-if-exists",
                    "--skip-if-file-exists",
                    "--config-file",
                    str(config_file),
                ],
            )

            assert result.exit_code == 0

            # Verify cookiecutter was called with correct arguments
            mock_cookiecutter.assert_called_once()
            call_args = mock_cookiecutter.call_args

            assert call_args[1]["output_dir"] == temp_dir
            assert call_args[1]["no_input"] is True
            assert call_args[1]["replay"] is True
            assert call_args[1]["overwrite_if_exists"] is True
            assert call_args[1]["skip_if_file_exists"] is True
            assert call_args[1]["config_file"] == str(config_file)

    @patch("cookiecutter_uv_package.cli.cookiecutter")
    def test_project_creation_with_short_flags(self, mock_cookiecutter):
        """Test project creation with short flags."""
        with tempfile.TemporaryDirectory() as temp_dir, tempfile.TemporaryDirectory() as mock_project_dir:
            mock_cookiecutter.return_value = mock_project_dir
            result = self.runner.invoke(
                main,
                [
                    "-o",
                    temp_dir,
                    "-f",  # --overwrite-if-exists
                    "-s",  # --skip-if-file-exists
                ],
            )

            assert result.exit_code == 0

            # Verify cookiecutter was called with correct arguments
            mock_cookiecutter.assert_called_once()
            call_args = mock_cookiecutter.call_args

            assert call_args[1]["output_dir"] == temp_dir
            assert call_args[1]["overwrite_if_exists"] is True
            assert call_args[1]["skip_if_file_exists"] is True

    @patch("cookiecutter_uv_package.cli.cookiecutter")
    def test_cookiecutter_error_handling(self, mock_cookiecutter):
        """Test that cookiecutter errors are handled properly."""
        mock_cookiecutter.side_effect = Exception("Test error")

        with tempfile.TemporaryDirectory() as temp_dir:
            result = self.runner.invoke(main, ["--output-dir", temp_dir, "--no-input"])

            assert result.exit_code == 1
            assert "Error creating project: Test error" in result.output

    def test_invalid_output_directory(self):
        """Test handling of invalid output directory."""
        result = self.runner.invoke(main, ["--output-dir", "/nonexistent/directory", "--no-input"])

        # Should fail with click's path validation error
        assert result.exit_code != 0
        assert "does not exist" in result.output.lower()

    def test_invalid_config_file(self):
        """Test handling of invalid config file."""
        result = self.runner.invoke(main, ["--config-file", "/nonexistent/config.yaml", "--no-input"])

        # Should fail with click's path validation error
        assert result.exit_code != 0
        assert "does not exist" in result.output.lower()

    @patch("cookiecutter_uv_package.cli.cookiecutter")
    def test_default_output_directory(self, mock_cookiecutter):
        """Test that default output directory is current working directory."""
        with tempfile.TemporaryDirectory() as mock_project_dir:
            mock_cookiecutter.return_value = mock_project_dir

            result = self.runner.invoke(main, ["--no-input"])

            assert result.exit_code == 0

            # Verify cookiecutter was called with current directory
            mock_cookiecutter.assert_called_once()
            call_args = mock_cookiecutter.call_args

            # The output_dir should be the string representation of current directory
            assert Path(call_args[1]["output_dir"]).exists()

    @patch("cookiecutter_uv_package.cli.cookiecutter")
    def test_template_directory_is_correct(self, mock_cookiecutter):
        """Test that the correct template directory is passed to cookiecutter."""
        with tempfile.TemporaryDirectory() as mock_project_dir:
            mock_cookiecutter.return_value = mock_project_dir

            result = self.runner.invoke(main, ["--no-input"])

            assert result.exit_code == 0

            # Verify cookiecutter was called with correct template directory
            mock_cookiecutter.assert_called_once()
            call_args = mock_cookiecutter.call_args

            template_dir = call_args[0][0]  # First positional argument
            template_path = Path(template_dir)

            assert template_path.exists()
            assert (template_path / "cookiecutter.json").exists()
            assert (template_path / "{{cookiecutter.project_slug}}").exists()

    @patch("cookiecutter_uv_package.cli.cookiecutter")
    def test_output_messages(self, mock_cookiecutter):
        """Test that correct output messages are displayed."""
        with tempfile.TemporaryDirectory() as temp_dir:
            test_project_path = str(Path(temp_dir) / "my-test-project")
            mock_cookiecutter.return_value = test_project_path

            result = self.runner.invoke(main, ["--no-input"])

            assert result.exit_code == 0
            assert "Creating new Python package..." in result.output
            assert f"Project successfully created at: {test_project_path}" in result.output
            assert "Next steps:" in result.output
            assert f"cd {Path.cwd() / 'my-test-project'}" in result.output
            assert "make dev-setup" in result.output
            assert "For detailed setup instructions, see the SETUP.md file" in result.output


class TestCLIRealGeneration:
    """Test CLI with real project generation using helpers."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_real_project_generation_with_defaults(self):
        """Test real project generation with default context."""
        with tempfile.TemporaryDirectory() as temp_dir:
            result = self.runner.invoke(main, ["--output-dir", temp_dir, "--no-input"])

            assert result.exit_code == 0
            assert "Creating new Python package..." in result.output
            assert "Project successfully created at:" in result.output

            project_dirs = list(Path(temp_dir).glob("*"))
            assert len(project_dirs) == 1
            project_path = str(project_dirs[0])

            try:
                assert_file_exists(project_path, "pyproject.toml")
                assert_file_exists(project_path, "README.md")
                assert_file_exists(project_path, "LICENSE")
                assert_file_exists(project_path, "tests/__init__.py")
                assert_file_exists(project_path, "tests/conftest.py")
                assert_file_exists(project_path, "Makefile")
                assert_file_exists(project_path, "SETUP.md")
                assert_file_exists(project_path, "WORKFLOW.md")

                assert_file_contains(project_path, "pyproject.toml", 'name = "my-python-package"')
                assert_file_contains(
                    project_path, "pyproject.toml", 'description = "A modern Python package with complete CI/CD setup"'
                )
                assert_file_contains(project_path, "pyproject.toml", 'license = {text = "MIT"}')

                assert_file_contains(project_path, "README.md", "# My Python Package")
                assert_file_contains(project_path, "README.md", "A modern Python package with complete CI/CD setup")

                assert_file_contains(project_path, "LICENSE", "MIT License")
            finally:
                cleanup_project(project_path)

    def test_real_project_generation_with_custom_context(self):
        """Test real project generation with custom context via config file."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_file = Path(temp_dir) / "config.yml"
            config_file.write_text("""
default_context:
  project_name: "Test Project"
  deployment_setup: "github-ci"
""")

            result = self.runner.invoke(
                main, ["--output-dir", temp_dir, "--no-input", "--config-file", str(config_file)]
            )

            assert result.exit_code == 0

            project_dirs = list(Path(temp_dir).glob("*"))
            project_dirs = [p for p in project_dirs if p.is_dir()]
            assert len(project_dirs) == 1
            project_path = str(project_dirs[0])

            try:
                assert_file_exists(project_path, "test_project/__init__.py")
                assert_file_exists(project_path, "test_project/py.typed")
                assert_file_exists(project_path, "tests/test_test_project.py")
                assert_file_exists(project_path, "examples/basic_usage.py")

                # Check that GitHub CI files exist (deployment_setup = "github-ci")
                assert_file_exists(project_path, ".github/workflows/checks.yml")
                assert_file_exists(project_path, ".github/workflows/coverage.yml")

                # Check that Docker files don't exist (default use_docker = "no")
                assert_file_not_exists(project_path, "Dockerfile")
                assert_file_not_exists(project_path, "docker-compose.yml")
            finally:
                cleanup_project(project_path)

    def test_real_project_generation_with_docker(self):
        """Test real project generation with Docker support."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_file = Path(temp_dir) / "config.yml"
            config_file.write_text("""
default_context:
  use_docker: "yes"
""")

            result = self.runner.invoke(
                main, ["--output-dir", temp_dir, "--no-input", "--config-file", str(config_file)]
            )

            assert result.exit_code == 0

            project_dirs = list(Path(temp_dir).glob("*"))
            project_dirs = [p for p in project_dirs if p.is_dir()]
            assert len(project_dirs) == 1
            project_path = str(project_dirs[0])

            try:
                assert_file_exists(project_path, "Dockerfile")
                assert_file_exists(project_path, "docker-compose.yml")
            finally:
                cleanup_project(project_path)

    def test_real_project_generation_with_pypi_publishing(self):
        """Test real project generation with PyPI publishing."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_file = Path(temp_dir) / "config.yml"
            config_file.write_text("""
default_context:
  deployment_setup: "github-ci-pypi"
""")

            result = self.runner.invoke(
                main, ["--output-dir", temp_dir, "--no-input", "--config-file", str(config_file)]
            )

            assert result.exit_code == 0

            project_dirs = list(Path(temp_dir).glob("*"))
            project_dirs = [p for p in project_dirs if p.is_dir()]
            assert len(project_dirs) == 1
            project_path = str(project_dirs[0])

            try:
                assert_file_exists(project_path, ".github/workflows/publish.yml")
            finally:
                cleanup_project(project_path)

    def test_real_project_generation_without_ci_cd(self):
        """Test real project generation without CI/CD."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_file = Path(temp_dir) / "config.yml"
            config_file.write_text("""
default_context:
  deployment_setup: "none"
""")

            result = self.runner.invoke(
                main, ["--output-dir", temp_dir, "--no-input", "--config-file", str(config_file)]
            )

            assert result.exit_code == 0

            project_dirs = list(Path(temp_dir).glob("*"))
            project_dirs = [p for p in project_dirs if p.is_dir()]
            assert len(project_dirs) == 1
            project_path = str(project_dirs[0])

            try:
                assert_file_not_exists(project_path, ".github")
                assert_file_not_exists(project_path, "release-please-config.json")
                assert_file_not_exists(project_path, ".release-please-manifest.json")
            finally:
                cleanup_project(project_path)
