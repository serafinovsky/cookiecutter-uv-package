import sys

python_versions = "{{ cookiecutter.python_versions }}"
python_versions_set = set(version.strip() for version in python_versions.split(","))
allowed_python_versions = {"3.6", "3.7", "3.8", "3.9", "3.10", "3.11", "3.12", "3.13"}

if not python_versions_set.issubset(allowed_python_versions):
    print("ERROR: Invalid Python versions list")
    sys.exit(1)
