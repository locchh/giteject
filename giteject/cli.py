"""Command line interface for giteject."""
import click
from .core import parse_gitingest_output, create_repository

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
def main(input_file: str, output_path: str):
    """
    Create a repository from gitingest output.
    
    Args:
        input_file: Path to the gitingest output file
        output_path: Path where to create the repository
    """
    # Read gitingest output
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse the output
    structure = parse_gitingest_output(content)
    
    # Create the repository
    create_repository(output_path, structure)
    
    click.echo(f"Repository created at: {output_path}")
    click.echo(f"Created {len(structure.directories)} directories")
    click.echo(f"Created {len(structure.files)} files")
