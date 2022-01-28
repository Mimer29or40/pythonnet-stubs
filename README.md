# stubgen

Generate stubs for .NET libraries

Python.NET Stub Generator

## Usage:

    stubgen make (<assembly-name>|--all|--built_in|--core) [options]
    stubgen group [<assembly-names>...] [--all|--built_in|--core] [options]
    stubgen (-h | --help)
    stubgen (-V | --version)

## Examples:

    ipy -m stubgen make System.Reflection --overwrite

## Options:

    <assembly-name>         Name of Dll Assembly to Process
    <assembly-names>...     Names of Dll Assemblies to Process
    
    --all                   Process All Assemblies in defaults.py
    --built_in              Process All Built-In Assemblies in defaults.py
    --core                  Process All Core Assemblies in defaults.py

    --output=<dir>          Name of Output Directory [default: stubs]
    --paths=<dir>...        Additional Directory to add to Path [default:]
    --overwrite             Force Overwrite if stub already exists [default: False].
    --no-json               Disables Json Log

    -h --help               Show this help
    -V --version            Show version
