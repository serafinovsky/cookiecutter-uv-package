import tempfile
from pathlib import Path

import pytest
from helpers import get_template_dir, run_cookiecutter


class TestValidation:
    """Test input validation functionality."""

    @pytest.mark.parametrize(
        "invalid_name",
        [
            "123invalid",  # Starts with number
            "project@with#special$chars",  # Special characters
            "",  # Empty
        ],
    )
    def test_invalid_project_name(self, invalid_name):
        """Test validation of invalid project names."""
        template_dir = get_template_dir()

        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                run_cookiecutter(template_dir, extra_context={"project_name": invalid_name}, output_dir=temp_dir)
                raise AssertionError(f"Expected validation error for project name: {invalid_name}")
            except RuntimeError as e:
                assert "Hook script failed" in str(e)

    @pytest.mark.parametrize(
        "invalid_version",
        [
            "3.5, 3.6",  # Too old
            "3.14",  # Too new
            "invalid",  # Not a version
            "3.11, invalid",
        ],
    )
    def test_invalid_python_versions(self, invalid_version):
        """Test validation of invalid Python versions."""
        template_dir = get_template_dir()

        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                run_cookiecutter(template_dir, extra_context={"python_versions": invalid_version}, output_dir=temp_dir)
                raise AssertionError(f"Expected validation error for Python version: {invalid_version}")
            except RuntimeError as e:
                assert "Hook script failed" in str(e)

    @pytest.mark.parametrize(
        "valid_name",
        [
            "my-project",
            "my-awesome-project",
            "project123",
            "a",
            "my-project-123",
        ],
    )
    def test_valid_project_name(self, valid_name):
        """Test that valid project names pass validation."""
        template_dir = get_template_dir()

        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                project_path = run_cookiecutter(
                    template_dir, extra_context={"project_name": valid_name}, output_dir=temp_dir
                )
                assert Path(project_path).exists(), f"Failed for valid name: {valid_name}"
            except RuntimeError as e:
                raise AssertionError(f"Unexpected error for valid name '{valid_name}': {e}") from e

    @pytest.mark.parametrize(
        "valid_version",
        [
            "3.11",
            "3.11, 3.12",
            "3.11, 3.12, 3.13",
            "3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13",
        ],
    )
    def test_valid_python_versions(self, valid_version):
        """Test that valid Python versions pass validation."""
        template_dir = get_template_dir()

        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                project_path = run_cookiecutter(
                    template_dir, extra_context={"python_versions": valid_version}, output_dir=temp_dir
                )
                assert Path(project_path).exists(), f"Failed for valid version: {valid_version}"
            except RuntimeError as e:
                raise AssertionError(f"Unexpected error for valid version '{valid_version}': {e}") from e

    @pytest.mark.parametrize(
        "project_name,expected_slug",
        [
            ("my-project", "my_project"),
            ("my-awesome-project", "my_awesome_project"),
            ("simple", "simple"),
            ("test-project-123", "test_project_123"),
        ],
    )
    def test_project_slug_validation(self, project_name, expected_slug):
        """Test that project slugs are validated correctly."""
        template_dir = get_template_dir()

        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                project_path = run_cookiecutter(
                    template_dir, extra_context={"project_name": project_name}, output_dir=temp_dir
                )
                assert Path(project_path).exists(), f"Failed for project name: {project_name}"

                assert (Path(project_path) / expected_slug).exists(), f"Package directory {expected_slug} not found"
            except RuntimeError as e:
                raise AssertionError(f"Unexpected error for project name '{project_name}': {e}") from e

    @pytest.mark.parametrize(
        "invalid_email",
        [
            "invalid-email",  # No @ symbol
            "@example.com",  # No local part
            "user@",  # No domain
            "user@.com",  # Empty domain
            "user@example",  # No TLD
            "user@example.",  # Empty TLD
            "user space@example.com",  # Space in local part
            "",  # Empty
        ],
    )
    def test_invalid_email(self, invalid_email):
        """Test validation of invalid email addresses."""
        template_dir = get_template_dir()

        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                run_cookiecutter(template_dir, extra_context={"author_email": invalid_email}, output_dir=temp_dir)
                raise AssertionError(f"Expected validation error for email: {invalid_email}")
            except RuntimeError as e:
                assert "Hook script failed" in str(e), f"Expected hook script failure for email: {invalid_email}"

    @pytest.mark.parametrize(
        "valid_email",
        [
            "user@example.com",
            "test.email@domain.org",
            "user+tag@example.co.uk",
            "user_name@example-domain.com",
            "user123@example123.com",
            "a@b.co",
        ],
    )
    def test_valid_email(self, valid_email):
        """Test validation of valid email addresses."""
        template_dir = get_template_dir()

        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                project_path = run_cookiecutter(
                    template_dir, extra_context={"author_email": valid_email}, output_dir=temp_dir
                )
                assert Path(project_path).exists(), f"Failed for email: {valid_email}"
            except RuntimeError as e:
                raise AssertionError(f"Unexpected error for email '{valid_email}': {e}") from e
