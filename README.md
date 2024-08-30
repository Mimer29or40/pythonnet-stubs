# stubgen

Generate stubs for .NET libraries

Python.NET Stub Generator

## Usage:

    usage: stubgen [-h] [-v] [--verbose] [-o OUTPUT_DIR] [-m] command ...
    
    A library for generating stubs of .NET libraries
    
    positional arguments:
    command
    extract             extract types from assemblies to json
    build               build stub file tree
    
    options:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    --verbose             set log level to DEBUG
    -o OUTPUT_DIR, --output-dir OUTPUT_DIR
    path to output directory [default: .]
    -m, --multi-threaded  flag to use multi threading
