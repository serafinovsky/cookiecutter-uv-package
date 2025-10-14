import keyword
import re
import sys

# Validate Python versions
python_versions = "{{ cookiecutter.python_versions }}"
python_versions_set = {version.strip() for version in python_versions.split(",")}
allowed_python_versions = {"3.6", "3.7", "3.8", "3.9", "3.10", "3.11", "3.12", "3.13"}

if not python_versions_set.issubset(allowed_python_versions):
    sys.stderr.write("ERROR: Invalid Python versions list\n")
    sys.exit(1)


def validate_project_name(name):
    """Validate project name for display purposes."""
    if not name or not name.strip():
        return False, "Project name cannot be empty"

    # Allow letters, numbers, spaces, hyphens, underscores for display name
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9\s\-_]*$", name.strip()):
        return (
            False,
            "Project name must start with a letter and contain only letters, numbers, spaces, hyphens, and underscores",
        )

    return True, ""


def validate_project_slug(slug):
    """Validate project slug for PyPI package name."""
    if not slug or not slug.strip():
        return False, "Project slug cannot be empty"

    # PyPI package names: letters, numbers, hyphens, dots (normalize underscores to hyphens)
    # Must start with letter or number, be 1+ chars
    if not re.match(r"^[a-zA-Z0-9]([a-zA-Z0-9\-\.])*$", slug):
        return (
            False,
            "Project slug must start with a letter or number and contain only letters, numbers, hyphens, and dots",
        )

    return True, ""


def validate_package_name(name):
    """Validate package name as Python module identifier."""
    if not name or not name.strip():
        return False, "Package name cannot be empty"

    # Must be valid Python identifier
    if not name.isidentifier():
        return (
            False,
            "Package name must be a valid Python identifier "
            "(letters, numbers, underscores, start with letter/underscore)",
        )

    # Check for Python keywords
    if keyword.iskeyword(name):
        return False, f"Package name '{name}' is a Python keyword and cannot be used"

    return True, ""


def validate_email(email):
    """Validate email address format."""
    if not email or not email.strip():
        return False, "Email address cannot be empty"

    # Basic email validation regex
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, email.strip()):
        return False, "Email address must be in valid format (e.g., user@example.com)"

    return True, ""


# Validate project_name
project_name = "{{cookiecutter.project_name}}"
is_valid, error_msg = validate_project_name(project_name)
if not is_valid:
    sys.stderr.write(f"ERROR: {error_msg}\n")
    sys.exit(1)

# Validate project_slug
project_slug = "{{cookiecutter.project_slug}}"
is_valid, error_msg = validate_project_slug(project_slug)
if not is_valid:
    sys.stderr.write(f"ERROR: {error_msg}\n")
    sys.exit(1)

# Validate package_name
package_name = "{{cookiecutter.package_name}}"
is_valid, error_msg = validate_package_name(package_name)
if not is_valid:
    sys.stderr.write(f"ERROR: {error_msg}\n")
    sys.exit(1)

# Validate author_email
author_email = "{{cookiecutter.author_email}}"
is_valid, error_msg = validate_email(author_email)
if not is_valid:
    sys.stderr.write(f"ERROR: {error_msg}\n")
    sys.exit(1)
