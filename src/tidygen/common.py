import click

destination_option = click.option(
    "-d",
    "--destination",
    help="Destination to create the app",
    required=True,
)

domain_option = click.option(
    '-e',
    '--domain',
    help='Domain to place class under',
    required=True
)

name_option = click.option(
    '-n',
    '--name',
    prompt='Name',
    help='Name of the class',
    required=True
)
