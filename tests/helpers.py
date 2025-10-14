import shutil
import tempfile
from pathlib import Path
from typing import Any, Dict, Optional

from cookiecutter.main import cookiecutter


def run_cookiecutter(
    template_dir: str,
    extra_context: Optional[Dict[str, Any]] = None,
    output_dir: Optional[str] = None,
    no_input: bool = True,
) -> str:
    """
    Run cookiecutter to generate a project from the template.

    Args:
        template_dir: Path to the cookiecutter template directory
        extra_context: Additional context variables for the template
        output_dir: Directory to output the generated project
        no_input: Whether to run without user input

    Returns:
        Path to the generated project directory
    """
    if output_dir is None:
        output_dir = tempfile.mkdtemp()

    try:
        return cookiecutter(
            template_dir,
            no_input=no_input,
            output_dir=output_dir,
            extra_context=extra_context or {},
            overwrite_if_exists=True,
        )
    except Exception as e:
        raise RuntimeError(f"Cookiecutter failed: {str(e)}") from e


def assert_file_exists(project_path: str, file_path: str) -> None:
    """Assert that a file exists in the generated project."""
    full_path = Path(project_path) / file_path
    assert full_path.exists(), f"File {file_path} does not exist in generated project"


def assert_file_not_exists(project_path: str, file_path: str) -> None:
    """Assert that a file does not exist in the generated project."""
    full_path = Path(project_path) / file_path
    assert not full_path.exists(), f"File {file_path} should not exist in generated project"


def assert_file_contains(project_path: str, file_path: str, content: str) -> None:
    """Assert that a file contains specific content."""
    full_path = Path(project_path) / file_path
    assert_file_exists(project_path, file_path)

    file_content = full_path.read_text(encoding="utf-8")
    assert content in file_content, f"File {file_path} does not contain expected content: {content}"


def assert_file_not_contains(project_path: str, file_path: str, content: str) -> None:
    """Assert that a file does not contain specific content."""
    full_path = Path(project_path) / file_path
    assert_file_exists(project_path, file_path)

    file_content = full_path.read_text(encoding="utf-8")
    assert content not in file_content, f"File {file_path} should not contain content: {content}"


def cleanup_project(project_path: str) -> None:
    """Clean up the generated project directory."""
    project_path_obj = Path(project_path)
    if project_path_obj.exists():
        shutil.rmtree(project_path)


def get_template_dir() -> str:
    """Get the path to the cookiecutter template directory."""
    return str(Path(__file__).parent.parent.absolute())


def get_default_context() -> Dict[str, Any]:
    """Get default context for testing."""
    return {
        "project_name": "Test Project",
        "author_name": "Test Author",
        "author_email": "test@example.com",
        "github_username": "testuser",
        "project_short_description": "A test project",
        "version": "0.1.0",
        "python_versions": "3.11, 3.12, 3.13",
        "use_docker": "no",
        "deployment_setup": "github-ci",
        "license": "MIT",
    }
