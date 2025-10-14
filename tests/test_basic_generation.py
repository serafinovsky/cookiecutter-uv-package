from helpers import (
    assert_file_contains,
    assert_file_exists,
    assert_file_not_exists,
    cleanup_project,
    get_default_context,
    get_template_dir,
    run_cookiecutter,
)


class TestBasicGeneration:
    def test_basic_project_generation(self):
        """Test that a basic project is generated correctly."""
        template_dir = get_template_dir()
        context = get_default_context()

        project_path = run_cookiecutter(template_dir, context)

        try:
            # Check that essential files exist
            assert_file_exists(project_path, "pyproject.toml")
            assert_file_exists(project_path, "README.md")
            assert_file_exists(project_path, "LICENSE")
            assert_file_exists(project_path, "tests/__init__.py")
            assert_file_exists(project_path, "tests/conftest.py")
            assert_file_exists(project_path, "tests/test_test_project.py")
            assert_file_exists(project_path, "test_project/__init__.py")
            assert_file_exists(project_path, "test_project/py.typed")
            assert_file_exists(project_path, "examples/basic_usage.py")
            assert_file_exists(project_path, "Makefile")
            assert_file_exists(project_path, "SETUP.md")
            assert_file_exists(project_path, "WORKFLOW.md")

            # Check pyproject.toml content
            assert_file_contains(project_path, "pyproject.toml", 'name = "test-project"')
            assert_file_contains(project_path, "pyproject.toml", 'description = "A test project"')
            assert_file_contains(project_path, "pyproject.toml", 'name = "Test Author"')
            assert_file_contains(project_path, "pyproject.toml", 'email = "test@example.com"')
            assert_file_contains(project_path, "pyproject.toml", 'license = {text = "MIT"}')
            assert_file_contains(project_path, "pyproject.toml", '"License :: OSI Approved :: MIT License"')

            # Check README.md content
            assert_file_contains(project_path, "README.md", "# Test Project")
            assert_file_contains(project_path, "README.md", "A test project")

            # Check LICENSE content
            assert_file_contains(project_path, "LICENSE", "MIT License")
            assert_file_contains(project_path, "LICENSE", "Test Author")
        finally:
            cleanup_project(project_path)

    def test_project_with_docker(self):
        """Test project generation with Docker support."""
        template_dir = get_template_dir()
        context = get_default_context()
        context["use_docker"] = "yes"
        project_path = run_cookiecutter(template_dir, context)
        try:
            assert_file_exists(project_path, "Dockerfile")
            assert_file_exists(project_path, "docker-compose.yml")
        finally:
            cleanup_project(project_path)

    def test_project_without_docker(self):
        """Test project generation without Docker support."""
        template_dir = get_template_dir()
        context = get_default_context()
        context["use_docker"] = "no"
        project_path = run_cookiecutter(template_dir, context)
        try:
            assert_file_not_exists(project_path, "Dockerfile")
            assert_file_not_exists(project_path, "docker-compose.yml")
        finally:
            cleanup_project(project_path)

    def test_project_with_pypi_publishing(self):
        """Test project generation with PyPI publishing enabled."""
        template_dir = get_template_dir()
        context = get_default_context()
        context["deployment_setup"] = "github-ci-pypi"
        project_path = run_cookiecutter(template_dir, context)
        try:
            assert_file_exists(project_path, ".github/workflows/publish.yml")
        finally:
            cleanup_project(project_path)

    def test_project_without_pypi_publishing(self):
        """Test project generation without PyPI publishing."""
        template_dir = get_template_dir()
        context = get_default_context()
        context["deployment_setup"] = "github-ci"
        project_path = run_cookiecutter(template_dir, context)
        try:
            assert_file_not_exists(project_path, ".github/workflows/publish.yml")
        finally:
            cleanup_project(project_path)

    def test_package_name_generation(self):
        """Test that package names are generated correctly."""
        template_dir = get_template_dir()
        context = get_default_context()
        context["project_name"] = "My Awesome Project"
        project_path = run_cookiecutter(template_dir, context)
        try:
            assert_file_exists(project_path, "my_awesome_project/__init__.py")
            assert_file_exists(project_path, "tests/test_my_awesome_project.py")
            assert_file_contains(project_path, "pyproject.toml", 'name = "my-awesome-project"')
        finally:
            cleanup_project(project_path)
