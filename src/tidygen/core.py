import os.path
from pathlib import Path
import click

from tidygen.common import destination_option, name_option, domain_option
import tidygen.utils as utils


@click.group(name='core')
def core():
    pass


@core.command()
@destination_option
@domain_option
@name_option
def create(destination: str, domain: str, name: str):
    """
    Create a new core level class in the specified domain

    Args:
        domain (str): The domain to place the class under
        name (str): The name of the class
        destination (str): The destination to create the class
    """
    path = Path(destination) / 'core' / utils.ensure_snake_case(domain)

    os.makedirs(path, exist_ok=True)

    (path / "__init__.py").touch()

    with open(path / f"{name}.py", 'w') as f:
        f.write(f"""from ..operation import Operation        
       
        
class {utils.ensure_camel_case(name)}Operation(Operation):
    def __init__(self):
        pass
        
    def execute(self):
        pass
""")
