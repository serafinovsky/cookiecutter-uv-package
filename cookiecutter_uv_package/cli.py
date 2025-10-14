"""CLI interface for cookiecutter-uv-package."""

import sys
from pathlib import Path
from typing import Optional

import click
from cookiecutter.main import cookiecutter


def get_template_dir() -> str:
    package_dir = Path(__file__).parent.parent
    return str(package_dir)


@click.command(help="Create a new Python package using a modern cookiecutter template")
@click.option(
    "--output-dir",
    "-o",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path, writable=True),
    default=Path.cwd(),
    help="Output directory for the generated project (default: current directory)",
)
@click.option(
    "--no-input",
    is_flag=True,
    help="Do not prompt for parameters and only use cookiecutter.json file content",
)
@click.option(
    "--replay",
    is_flag=True,
    help="Do not prompt for parameters and only use information entered previously",
)
@click.option(
    "--overwrite-if-exists",
    "-f",
    is_flag=True,
    help="Overwrite the contents of the output directory if it already exists",
)
@click.option(
    "--skip-if-file-exists",
    "-s",
    is_flag=True,
    help="Skip the files in the corresponding directories if they already exist",
)
@click.option(
    "--config-file",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=Path),
    help="User configuration file",
)
@click.version_option()
def main(
    output_dir: Path,
    no_input: bool,
    replay: bool,
    overwrite_if_exists: bool,
    skip_if_file_exists: bool,
    config_file: Optional[Path],
) -> None:
    template_dir = get_template_dir()

    try:
        click.echo("Creating new Python package...")
        project_path = cookiecutter(
            template_dir,
            output_dir=str(output_dir),
            no_input=no_input,
            replay=replay,
            overwrite_if_exists=overwrite_if_exists,
            skip_if_file_exists=skip_if_file_exists,
            config_file=str(config_file) if config_file else None,
        )

        click.echo(f"Project successfully created at: {project_path}")
        click.echo("\nNext steps:")
        click.echo(f"   cd {output_dir / Path(project_path).name}")
        click.echo("   make dev-setup")
        click.echo("\nFor detailed setup instructions, see the SETUP.md file")

    except Exception as e:
        click.echo(f"Error creating project: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
