# Tidygen

## Overview

The Tidygen project is a command-line tool for creating and managing application components in a clean architectural manner. 

All dependencies should flow from app > core > entities or app > data > entities. This ensures that the core and data layers are not dependent on each other. However, the adherence to this structure is wholly dependent on the user.

It uses the `click` library to provide a set of commands for generating application, core, and data classes in specified domains.

## Installation

To install, run:

```bash
pip install tidygen
```

## Usage

### Initialize a New Project

To initialize a new project, use the `init` command:

```bash
tidygen init -d <destination>
```


# Building the Project

## Installation

To install the required dependencies, run:

```bash
poetry install
```

## Usage

### Initialize a New Project

To initialize a new project, use the `init` command:

```bash
python src/tidygen/main.py init -d <destination>
```

This will create the necessary directory structure and an abstract `Operation` class.

### Create Application Components

#### Create an Application Class

To create a new application class, use the `create` command under the `app` group:

```bash
python src/tidygen/main.py app create -d <destination> -e <domain> -n <name>
```

This will create a new class in the specified domain under the `app` directory.

#### Create a Core Class

To create a new core class, use the `create` command under the `core` group:

```bash
python src/tidygen/main.py core create -d <destination> -e <domain> -n <name>
```

This will create a new class in the specified domain under the `core` directory.

### Create Data Components

#### Create a Queries Class

To create a new queries class, use the `create_queries` command under the `data` group:

```bash
python src/tidygen/main.py data create_queries -d <destination> -e <domain>
```

This will create a new queries class in the specified domain under the `data` directory.

#### Create a Statement Class

To create a new statement class, use the `create_statement` command under the `data` group:

```bash
python src/tidygen/main.py data create_statement -d <destination> -e <domain>
```

This will create a new statement class in the specified domain under the `data` directory.

## Directory Structure

The project will generate the following directory structure:

```
<destination>/
├── app/
│   ├── __init__.py
│   └── <domain>/
│       ├── __init__.py
│       └── <name>.py
├── core/
│   ├── __init__.py
│   └── <domain>/
│       ├── __init__.py
│       └── <name>.py
├── data/
│   ├── __init__.py
│   └── <domain>/
│       ├── __init__.py
│       ├── queries.py
│       └── statements.py
└── entities/
    ├── __init__.py
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.