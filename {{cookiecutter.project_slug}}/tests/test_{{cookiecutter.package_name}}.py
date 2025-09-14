"""Tests for {{ cookiecutter.package_name }}."""

import {{ cookiecutter.package_name }}


def test_version() -> None:
    """Test version is defined."""
    assert hasattr({{ cookiecutter.package_name }}, "__version__")
    assert isinstance({{ cookiecutter.package_name }}.__version__, str)
