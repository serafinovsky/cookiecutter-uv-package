import pytest
from helpers import (
    assert_file_contains,
    assert_file_exists,
    assert_file_not_contains,
    assert_file_not_exists,
    cleanup_project,
    get_default_context,
    get_template_dir,
    run_cookiecutter,
)


class TestLicenseOptions:
    """Test license option functionality."""

    @pytest.mark.parametrize(
        "license_type,license_text,version_text,classifier",
        [
            (
                "MIT",
                "MIT License",
                "Permission is hereby granted",
                '"License :: OSI Approved :: MIT License"',
            ),
            (
                "Apache-2.0",
                "Apache License",
                "Version 2.0",
                '"License :: OSI Approved :: Apache Software License"',
            ),
            (
                "BSD-3-Clause",
                "BSD 3-Clause License",
                "Redistribution and use",
                '"License :: OSI Approved :: BSD License"',
            ),
            (
                "GPL-3.0",
                "GNU GENERAL PUBLIC LICENSE",
                "Version 3",
                '"License :: OSI Approved :: GNU General Public License v3 (GPLv3)"',
            ),
            (
                "ISC",
                "ISC License",
                "Permission to use, copy, modify",
                '"License :: OSI Approved :: ISC License (ISCL)"',
            ),
        ],
    )
    def test_license_generation(self, license_type, license_text, version_text, classifier):
        template_dir = get_template_dir()
        context = get_default_context()
        context["license"] = license_type
        project_path = run_cookiecutter(template_dir, context)

        try:
            assert_file_exists(project_path, "LICENSE")

            assert_file_contains(project_path, "LICENSE", license_text)
            assert_file_contains(project_path, "LICENSE", "Test Author")
            assert_file_contains(project_path, "LICENSE", version_text)

            assert_file_contains(project_path, "pyproject.toml", f'license = {{text = "{license_type}"}}')
            assert_file_contains(project_path, "pyproject.toml", classifier)
        finally:
            cleanup_project(project_path)

    def test_no_license(self):
        template_dir = get_template_dir()
        context = get_default_context()
        context["license"] = "none"
        project_path = run_cookiecutter(template_dir, context)

        try:
            assert_file_not_exists(project_path, "LICENSE")

            assert_file_not_contains(project_path, "pyproject.toml", "license = {text =")
            assert_file_not_contains(project_path, "pyproject.toml", '"License :: OSI Approved ::')
        finally:
            cleanup_project(project_path)
