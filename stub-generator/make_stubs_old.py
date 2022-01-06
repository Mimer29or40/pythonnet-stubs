import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Any, List

import clr

from System.Reflection import Assembly, ConstructorInfo, ParameterInfo
from reference.generator3 import SkeletonGenerator, generate_skeleton
from .logger import logger
from .options import Options
from .model import Parameter, RegularType, Constructor


def make(package: str, options: Options):
    """Main Processing Function"""
    logger.info('=' * 80)
    logger.info('Making [{}]'.format(package))
    
    # pymodule = sys.modules[package]
    
    assembly: Assembly = clr.AddReference(package)
    
    # print('assembly', assembly)
    # print('getmembers', inspect.getmembers(assembly))
    # for member in inspect.getmembers(assembly)[1:]:
    #     # if inspect.ismethod(member[1]) or inspect.isfunction(member[1]):
    #     print('signature', inspect.signature(member[1]))
    #     print('getargvalues', inspect.getargvalues(member[1]))
    #     print('getcallargs', inspect.getcallargs(member[1]))
    #     print('getfullargspec', inspect.getfullargspec(member[1]))
    # print('getclasstree', inspect.getclasstree([Assembly]))
    # # print('getsource', inspect.getsource(Assembly))
    # print('getmodule', inspect.getmodule(assembly))
    # print('getmodule', inspect.getmodule(assembly))
    # # getfile(), getsourcefile(), getsource() - find an object's source code
    # # getdoc(), getcomments() - get documentation on an object
    # # getmodule() - determine the module that an object came from
    # # getclasstree() - arrange classes so as to represent their hierarchy
    # #
    # # getargvalues(), getcallargs() - get info about function arguments
    # # getfullargspec() - same, with support for Python 3 features
    # # formatargvalues() - format an argument spec
    # # getouterframes(), getinnerframes() - get info about frames
    # # currentframe() - get the current stack frame
    # # stack(), trace() - get info about frames on the stack or in a traceback
    # #
    # # signature() - get a Signature object for the callable
    
    # for type in assembly.GetTypes():
    # for type in assembly.ExportedTypes:
    # for type in assembly.GetExportedTypes():
    #     process_type(type)
    # process_type(assembly.GetType('System.Collections.CollectionBase'))
    # process_type(assembly.GetType('System.Collections.Comparer'))
    # process_type(assembly.GetType('System.Collections.Hashtable'))
    process_type(assembly.GetType('System.Collections.Queue'))
    
    # assembly_dict: Dict[str, Any]
    #
    # # noinspection PyBroadException
    # try:
    #     clr.AddReference(assembly_or_builtin)
    # except Exception:
    #     builtin_name: str = assembly_or_builtin
    #     logger.info(f'Adding BuiltIn [{builtin_name}]')
    #     importlib.import_module(builtin_name)
    #     assembly_dict = {'__builtins__': {builtin_name: str(sys.modules[builtin_name])}}
    # else:
    #     assembly_name: str = assembly_or_builtin
    #     logger.info(f'Adding Assembly [{assembly_name}]')
    #     assembly_dict = crawl_loaded_references(assembly_name)
    #
    # if assembly_dict is None:
    #     raise Exception(f'No NamesSpaces to Process for \'{assembly_or_builtin}\'')
    #
    # modules = [list(d.keys()) for d in assembly_dict.values()]
    # logger.info(f'Modules and Assemblies Loaded: {modules}')
    # logger.debug(json.dumps(assembly_dict, indent=2, sort_keys=True))
    #
    # if not options.all and input(f'>>> Write Stubs ({options.output_dir}) [y/n] [n]:\n>>> ') != 'y':
    #     logger.info('No Stubs Created')
    # else:
    #     for assembly, modules in assembly_dict.items():
    #         for module_name in modules.keys():
    #             if not stub_exists(options.output_dir, module_name) or options.overwrite:
    #                 create_stubs(options.output_dir, module_name)
    #             else:
    #                 logger.info(f'Skipping [{module_name}] Already Exists')
    #         for module_name in modules.keys():
    #             delete_module(module_name)
    #
    # dump_json_log(assembly_dict)
    
    print()


def process_type(type: RegularType):
    if not type.Namespace.startswith('System.Collections'):
        return
    print(f'type={type} abstract={type.IsAbstract} BaseType={type.BaseType} Namespace={type.Namespace}')
    for args in type.GetGenericArguments():
        print('  args', args)
    for interface in type.GetInterfaces():
        print('  interface', interface)
    for field in type.GetFields():
        print('  field', field)
    for constructor in type.GetConstructors():
        process_constructor(constructor)
    for property in type.GetProperties():
        print('  property', property)
    for method in type.GetMethods():
        print('  method', method)
    for nested_type in type.GetNestedTypes():
        print('  nested_type', nested_type)
    # for empty_type in type.EmptyTypes:
    #     print('  empty_type', empty_type)
    for event in type.GetEvents():
        print('  event', event)


def process_constructor(constructor_info: ConstructorInfo):
    # print('  constructor', constructor_info)
    params = tuple(map(process_parameter, constructor_info.GetParameters()))
    constructor = Constructor(params)
    print('  constructor', constructor_info)
    print(constructor.print(len('    ')))


def process_parameter(parameter_info: ParameterInfo) -> Parameter:
    default = None
    if parameter_info.IsOptional:
        default = parameter_info.RawDefaultValue
    
    parameter_type = process_parameter_type(parameter_info.ParameterType)
    
    # print('      IsIn', parameter_info.IsIn)
    # print('      IsOptional', parameter_info.IsOptional)
    # print('      IsOut', parameter_info.IsOut)
    # print('      Name', parameter_info.Name)
    # print('      ParameterType', parameter_info.ParameterType)
    # print('      RawDefaultValue', parameter_info.RawDefaultValue)
    
    return Parameter(parameter_info.Name, parameter_type, default=default, doc_string='')


def process_parameter_type(type: RegularType) -> RegularType:
    return RegularType(str(type))


def crawl_loaded_references(target_assembly_name: str) -> Dict[str, Any]:
    """Crawl Loaded assemblies to get Namespaces"""
    namespaces_dict = {}
    assembly: Assembly
    for assembly in AppDomain.CurrentDomain.GetAssemblies():
        if assembly.IsDynamic:
            continue
        assembly_name: str = assembly.GetName().Name
        assembly_path: Path = Path(assembly.CodeBase)
        if assembly_name == target_assembly_name:
            logger.info(f'Parsing Assembly: {assembly_name}')
            namespaces_dict[assembly_path.stem] = get_modules(assembly_name, assembly)
        else:
            logger.debug(f'Assembly Skipped. Does not match Target: {assembly_name}')
    return namespaces_dict


def get_modules(name: str, assembly_or_module: 'Assembly') -> Dict[str, List[str]]:
    """Recursively iterate through all namespaces in assembly"""
    namespace_dict = defaultdict(set)
    
    for type in assembly_or_module.GetTypes():
        if (namespace := type.Namespace) is not None and namespace.startswith(name):
            namespace_dict[namespace].add(type.Name)
    
    sorted_dict: Dict[str, List[str]] = {}
    for key in sorted(namespace_dict.keys()):
        sorted_dict[key] = list(sorted(namespace_dict[key]))
    
    return sorted_dict


def stub_exists(dir: Path, path: str) -> bool:
    path: Path = dir.joinpath(*path.split('.'))
    return path.exists() or Path(str(path) + '.py').exists()


def create_stubs(output_dir: Path, module_name: str) -> None:
    """Actually Make Stubs"""
    try:
        logger.info('=' * 30)
        logger.info(f'Processing [{module_name}]')
        # process_one(module_path, None, True, output_dir)
        
        generator = SkeletonGenerator(output_dir=str(output_dir))
        
        # if not args.mod_name:
        #     generator.discover_and_process_all_modules(name_pattern=args.name_pattern,
        #                                                builtins_only=args.builtins_only)
        #     sys.exit(0)
        #
        # if sys.platform == 'cli':
        #     # noinspection PyUnresolvedReferences
        #     import clr
        #
        #     for ref in args.clr_assemblies:
        #         clr.AddReferenceByPartialName(ref)
        #
        #     if args.run_clr_profiler:
        #         atexit.register(print_profile)
        #
        #     # We take module name from import statement
        #     args.mod_name = get_namespace_by_name(args.mod_name)
        
        result = generate_skeleton(module_name, None, str(output_dir / 'cache'), str(output_dir))
        
        logger.info(result)
    except Exception as errmsg:
        logger.error(f'Could not process module_path: {module_name}')
        logger.error(errmsg)
    else:
        logger.info('Done')


def delete_module(module_name: str) -> None:
    """Delete Module after it has been processed"""
    # noinspection PyBroadException
    try:
        del sys.modules[module_name]
        logger.debug(f'Deleted Module: {module_name}')
    except Exception:
        logger.debug(f'Could not delete: {module_name}')


def dump_json_log(namespaces_dict: Dict[str, Any]):
    json_dir: Path = Path('logs')
    json_dir.mkdir(exist_ok=True)
    name = '-'.join(namespaces_dict.keys())
    filepath = json_dir / f'{name}.json'
    with filepath.open('w') as fp:
        json.dump(namespaces_dict, fp, indent=2)
