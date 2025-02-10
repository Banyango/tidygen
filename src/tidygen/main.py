import click
from pathlib import Path

from tidygen.app import app
from tidygen.data import data
from tidygen.common import destination_option
from tidygen.core import core


@click.group()
def entry_point():
    pass


@entry_point.command()
@destination_option
def init(destination: str):
    if (Path(destination) / 'app').exists():
        click.echo('App already exists')
        return

    click.echo('Creating app ...')

    def make_dir(path):
        (Path(destination) / path).mkdir(parents=True)
        (Path(destination) / path / '__init__.py').touch()

    make_dir('app')
    make_dir('core')
    make_dir('data')
    make_dir('entities')

    # Create abstract operation class
    with open(Path(destination) / 'core' / 'operation.py', 'w') as f:
        f.write("""from abc import abstractmethod


class Operation:
    @abstractmethod
    def execute(self):
        pass
""")

    click.echo('App created ...')


entry_point.add_command(app)
entry_point.add_command(core)
entry_point.add_command(data)

if __name__ == '__main__':
    entry_point()
