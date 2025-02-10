import os.path
from pathlib import Path
import click

from tidygen.common import destination_option, name_option, domain_option
import tidygen.utils as utils


@click.group(name='data')
def data():
    pass


@data.command()
@destination_option
@domain_option
def create_queries(destination: str, domain: str):
    """
    Create a new queries class in the specified domain

    Args:
        domain (str): The domain to place the class under
        destination (str): The destination to create the class
    """
    path = Path(destination) / 'data' / utils.ensure_snake_case(domain)

    os.makedirs(path, exist_ok=True)

    (path / "__init__.py").touch()

    with open(path / f"queries.py", 'w') as f:
        f.write(f"""class {utils.ensure_camel_case(domain)}Queries:
    def __init__(self):
        \"\"\"
        Represents a collection of queries for the {domain} domain
        \"\"\"                
        pass        
""")


@data.command()
@destination_option
@domain_option
def create_statement(destination: str, domain: str):
    """
    Create a new statement class in the specified domain

    Args:
        domain (str): The domain to place the class under
        destination (str): The destination to create the class
    """
    path = Path(destination) / 'data' / utils.ensure_snake_case(domain)

    os.makedirs(path, exist_ok=True)

    (path / "__init__.py").touch()

    with open(path / f"statements.py", 'w') as f:
        f.write(f"""def fetch_{domain}():
    pass        
""")
