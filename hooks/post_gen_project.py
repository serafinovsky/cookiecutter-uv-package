#!/usr/bin/env python3
"""
Post-generation hook for cookiecutter-uv-package.

This hook removes files and directories that are not needed based on the user's choices.
"""

import shutil
import sys
from pathlib import Path


def remove_file_or_dir(path):
    """Remove a file or directory if it exists."""
    path_obj = Path(path)
    if path_obj.exists():
        if path_obj.is_dir():
            shutil.rmtree(path_obj)
            sys.stdout.write(f"Removed directory: {path_obj}\n")
        else:
            path_obj.unlink()
            sys.stdout.write(f"Removed file: {path_obj}\n")


def remove_empty_dirs(path):
    """Recursively remove empty directories."""
    path_obj = Path(path)
    if not path_obj.is_dir():
        return

    # Remove empty subdirectories first
    for item in path_obj.iterdir():
        if item.is_dir():
            remove_empty_dirs(item)

    # Remove this directory if it's empty
    try:
        if not any(path_obj.iterdir()):
            path_obj.rmdir()
            sys.stdout.write(f"Removed empty directory: {path_obj}\n")
    except OSError:
        pass  # Directory not empty or other error


def main():
    """Main function to clean up generated files based on user choices."""
    # Get the project directory (where cookiecutter generated the project)
    project_dir = Path.cwd()

    # Get cookiecutter variables
    deployment_setup = "{{ cookiecutter.deployment_setup }}"
    license_choice = "{{ cookiecutter.license }}"
    use_docker = "{{ cookiecutter.use_docker }}"

    sys.stdout.write("Cleaning up project based on choices:\n")
    sys.stdout.write(f"  - Deployment setup: {deployment_setup}\n")
    sys.stdout.write(f"  - License: {license_choice}\n")
    sys.stdout.write(f"  - Use Docker: {use_docker}\n")

    # Remove GitHub CI/CD files if not needed
    if deployment_setup == "none":
        remove_file_or_dir(project_dir / ".github")
        remove_file_or_dir(project_dir / ".release-please-manifest.json")
        remove_file_or_dir(project_dir / "release-please-config.json")

    # Remove PyPI-specific files if not using github-ci-pypi
    if deployment_setup != "github-ci-pypi":
        remove_file_or_dir(project_dir / ".github" / "workflows" / "publish.yml")

    # Remove license file if none selected
    if license_choice == "none":
        remove_file_or_dir(project_dir / "LICENSE")

    # Remove Docker files if not using Docker
    if use_docker == "no":
        remove_file_or_dir(project_dir / "docker-compose.yml")
        remove_file_or_dir(project_dir / "Dockerfile")

    # Clean up .github directory if it exists and is empty
    github_dir = project_dir / ".github"
    if github_dir.exists():
        remove_empty_dirs(github_dir)
        # Remove .github if it's now empty
        if github_dir.exists() and not any(github_dir.iterdir()):
            github_dir.rmdir()
            sys.stdout.write("Removed empty .github directory\n")

    sys.stdout.write("Cleanup completed successfully!\n")


if __name__ == "__main__":
    main()
