import re
from collections import defaultdict
from functools import partial
from pathlib import Path
from typing import Dict, Tuple, Optional

import clr

from System import Type as _SystemType, Nullable
from System.Reflection import Assembly, ConstructorInfo, ParameterInfo, PropertyInfo, MethodInfo, EventInfo
from .logger import logger
from .model import Parameter, Type, Constructor, Namespace, Interface, SystemType, Property, Method, TypeBase, VarType, EventType, Event
from .options import Options


def make(assembly_name: str, options: Options):
    """Main Processing Function"""
    logger.info('=' * 80)
    logger.info('Making [{}]'.format(assembly_name))
    
    assembly: Assembly = clr.AddReference(assembly_name)
    
    namespace_dict = defaultdict(list)
    for type in assembly.GetTypes():
        if type.Namespace is None or type.IsNested:
            continue
        namespace_dict[type.Namespace].append(type.FullName)
    # pprint(namespace_dict)
    
    namespaces: Dict[str, Namespace] = {}
    
    for name, type_names in namespace_dict.items():
        namespace: Namespace
        if name in namespaces:
            namespace = namespaces[name]
        else:
            namespace = Namespace(name)
            namespaces[name] = namespace
        
        for type_name in type_names:
            process_assembly_type(namespace, assembly.GetType(type_name))
    
    stub_dir = options.output_dir / f'{assembly_name}-stubs'
    
    if options.overwrite and stub_dir.exists():
        _rm_tree(stub_dir)
    
    if not stub_dir.exists():
        stub_dir.mkdir(parents=True, exist_ok=True)
        
        assembly_name_type = assembly.GetName()
        version = assembly_name_type.Version
        culture = 'neutral'
        if (culture_info := assembly_name_type.CultureInfo) is not None and (culture_name := culture_info.Name) != '':
            culture = culture_name
        public_key_token = ''.join(hex(b).lstrip("0x") for b in assembly_name_type.GetPublicKeyToken())
        
        setup_file = stub_dir / 'setup.cfg'
        setup_file.write_text('\n'.join([
            f'[metadata]',
            f'name = {assembly_name}-stubs',
            f'version = {version}',
            f'description = Stubs Package for {assembly_name}',
            f'long_description = file: README.md, LICENSE',
            f'keywords = pythonnet, stubs, {assembly_name}',
            f'license = MIT License',
            f'culture = {culture}',
            f'public_key_token = {public_key_token}',
            f'classifiers =',
            f'    Development Status :: 5 - Production/Stable',
            f'    Intended Audience :: Developers',
            f'    License :: OSI Approved :: MIT License',
            f'    Programming Language :: Python :: 3',
            f'    Programming Language :: Python :: 3.8',
            f'    Topic :: Software Development :: Build Tools',
            f'    Topic :: Software Development :: Documentation',
            f'    Topic :: Utilities',
            f'',
            f'[options]',
            f'packages = find:',
            f'install_requires =',
            f'    pythonnet==2.5.2',
            f'python_requires = >=3.8',
            f'',
        ]))
        
        readme_file = stub_dir / 'README.md'
        readme_file.write_text('\n'.join([
            f'# {assembly_name}-stubs',
            f'Stubs Package for {assembly_name}',
            f'',
        ]))
        
        license_file = stub_dir / 'LICENSE'
        license_file.write_text('\n'.join([
            f'MIT License',
            f'',
            f'Copyright (c) 2021 Ryan Smith',
            f'',
            f'Permission is hereby granted, free of charge, to any person obtaining a copy',
            f'of this software and associated documentation files (the "Software"), to deal',
            f'in the Software without restriction, including without limitation the rights',
            f'to use, copy, modify, merge, publish, distribute, sublicense, and/or sell',
            f'copies of the Software, and to permit persons to whom the Software is',
            f'furnished to do so, subject to the following conditions:',
            f'',
            f'The above copyright notice and this permission notice shall be included in all',
            f'copies or substantial portions of the Software.',
            f'',
            f'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR',
            f'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,',
            f'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE',
            f'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER',
            f'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,',
            f'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE',
            f'SOFTWARE.',
            f'',
        ]))
        
        manifest_file = stub_dir / 'MANIFEST.in'
        manifest_file.write_text('\n'.join([f'include {n.split(".")[0]}-stubs/*.pyi' for n in namespaces] + [f'']))
        
        for name, namespace in namespaces.items():
            parent_dir: Path = stub_dir
            namespace_dir: Path
            init_file: Path
            for n in name.split('.'):
                if parent_dir == stub_dir:
                    namespace_dir = parent_dir / f'{n}-stubs'
                else:
                    namespace_dir = parent_dir / n
                namespace_dir.mkdir(exist_ok=True)
                
                init_file = namespace_dir / '__init__.pyi'
                init_file.touch(exist_ok=True)
                
                parent_dir = namespace_dir
            
            # noinspection PyUnboundLocalVariable
            init_file.write_text(namespace.print())


def process_assembly_type(namespace: Namespace, type: _SystemType):
    # if type.IsClass:
    #     return process_class(namespace, type)
    # if type.IsStruct:
    #     return process_struct(namespace, type)
    if type.IsInterface:
        return process_interface(namespace, type)
    # if type.IsEnum:
    #     return process_enum(namespace, type)
    # print(f'type={type} abstract={type.IsAbstract} BaseType={type.BaseType} Namespace={type.Namespace}')
    # for args in type.GetGenericArguments():
    #     print('  args', args)
    # for interface in type.GetInterfaces():
    #     print('  interface', interface)
    # for field in type.GetFields():
    #     print('  field', field)
    # for constructor in type.GetConstructors():
    #     process_constructor(constructor)
    # for property in type.GetProperties():
    #     print('  property', property)
    # for method in type.GetMethods():
    #     print('  method', method)
    # for nested_type in type.GetNestedTypes():
    #     print('  nested_type', nested_type)
    # # for empty_type in type.EmptyTypes:
    # #     print('  empty_type', empty_type)
    # for event in type.GetEvents():
    #     print('  event', event)


def process_interface(namespace: Namespace, interface_type: _SystemType):
    namespace.py_imports.add('typing.Protocol')
    name = _strip_str(interface_type.Name)
    if name in namespace.interfaces:
        return  # Redeclared Interface Type. This should only happen for generic types. ie: Type -> Type<T>
    
    type_args = [process_var_type(namespace, type_arg.Name, type_arg) for type_arg in interface_type.GetGenericArguments()]
    
    bases = [process_type(namespace, base) for base in interface_type.GetInterfaces()]
    
    properties = []
    for property_info in interface_type.GetProperties():
        getter, setter = process_property(namespace, property_info)
        if getter is not None:
            properties.append(getter)
        if setter is not None:
            properties.append(setter)
    properties.sort(key=lambda p: p.name)
    
    methods = []
    method_dict = defaultdict(list)
    for method_info in interface_type.GetMethods():
        method_dict[method_info.Name].append(method_info)
    for method_list in method_dict.values():
        overload = len(method_list) > 1
        for method_info in method_list:
            methods.append(process_method(namespace, method_info, overload))
    methods.sort(key=lambda m: m.name)
    
    events = []
    for event_info in interface_type.GetEvents():
        events.append(process_event(namespace, event_info))
    events.sort(key=lambda e: e.name)
    
    interface = Interface(name,
                          type_args=tuple(type_args),
                          bases=tuple(bases),
                          properties=tuple(properties),
                          methods=tuple(methods),
                          events=tuple(events),
                          doc_string='')
    namespace.interfaces[interface.name] = interface


def process_property(namespace: Namespace, property_info: PropertyInfo) -> Tuple[Optional[Property], Optional[Property]]:
    if not property_info.CanRead:
        return None, None
    
    # TODO - To determine whether a property is static, you must obtain the MethodInfo for the get or set accessor,
    # by calling the GetGetMethod or the GetSetMethod method, and examine its IsStatic property.
    static = False
    
    property_type = process_type(namespace, property_info.PropertyType)
    
    getter = Property(property_info.Name, property_type, static=static)
    
    setter = None
    if property_info.CanWrite:
        setter = Property(property_info.Name, property_type, static=static, setter=True)
    return getter, setter


def process_method(namespace: Namespace, method_info: MethodInfo, overload: bool) -> Method:
    # IsAbstract
    # IsVirtual
    # IsStatic
    # IsGenericMethod
    # IsGenericMethodDefinition
    
    return_parameters = [process_type(namespace, method_info.ReturnType)]
    
    parameters = []
    for parameter_info in method_info.GetParameters():
        parameter = process_parameter(namespace, parameter_info)
        parameters.append(parameter)
        if parameter.is_out:
            return_parameters.append(parameter.type)
    
    # TODO - Any out parameters are added to the return type as a tuple
    
    return Method(method_info.Name, tuple(parameters), tuple(return_parameters), overload=overload)


def process_event(namespace: Namespace, event_info: EventInfo) -> Event:
    if 'EventType' not in namespace.sys_types:
        namespace.py_imports.add('typing.Generic')
        namespace.special_types['EventType'] = EventType()
    return Event(event_info.Name, process_type(namespace, event_info.EventHandlerType))


def process_constructor(constructor_info: ConstructorInfo):
    # print('  constructor', constructor_info)
    params = tuple(map(process_parameter, constructor_info.GetParameters()))
    constructor = Constructor(params)
    print('  constructor', constructor_info)
    print(constructor.print(len('    ')))


def process_parameter(namespace: Namespace, parameter_info: ParameterInfo) -> Parameter:
    default = None
    if parameter_info.IsOptional:
        default = parameter_info.RawDefaultValue
    
    parameter_type = process_type(namespace, parameter_info.ParameterType)
    
    # print('      IsIn', parameter_info.IsIn)
    # print('      IsOut', parameter_info.IsOut)
    # print('      Name', parameter_info.Name)
    # print('      ParameterType', parameter_info.ParameterType)
    # print('      RawDefaultValue', parameter_info.RawDefaultValue)
    
    return Parameter(parameter_info.Name, parameter_type, default=default, is_out=parameter_info.IsOut, doc_string='')


def process_type(namespace: Namespace, type: _SystemType) -> TypeBase:
    name = _strip_str(type.Name if type.FullName is None else type.FullName)
    
    # if type.IsByRef:
    # if type.IsPointer:
    
    if type.IsGenericType:
        namespace.net_imports.add(f'{type.Namespace}.{name}')
        types = tuple(process_type(namespace, p) for p in type.GetGenericArguments())
        new_type = Type(name, types)
    elif type.IsGenericParameter:
        new_type = process_var_type(namespace, name, type)
    elif name in _system_type_dict:
        new_type = _system_type_dict[name](namespace)
    # obsolete_type = SystemType('Obsolete', 'NoReturn')
    else:
        namespace.net_imports.add(name)
        new_type = Type(type.Name)
    if Nullable.GetUnderlyingType(type) is not None:
        namespace.py_imports.add('typing.Optional')
        nullable_type = process_system_type('NullableType', 'System.Nullable', 'Union[Optional, Nullable]', namespace)
        return Type(nullable_type, (new_type,))
    if type.IsArray:
        namespace.py_imports.add('typing.List')
        array_type = process_system_type('ArrayType', 'System.Array', 'Union[List, Array]', namespace)
        return Type(array_type, (new_type,))
    return new_type


def process_system_type(name: str, system_name: str, value: str, namespace: Namespace) -> SystemType:
    if name not in namespace.sys_types:
        namespace.net_imports.add(system_name)
        namespace.py_imports.add('typing.Union')
        namespace.sys_types[name] = SystemType(name, value)
    return namespace.sys_types[name]


def process_var_type(namespace: Namespace, name: str, type: _SystemType) -> VarType:
    if name not in namespace.var_types:
        namespace.py_imports.add("typing.TypeVar")
        bounds = tuple(process_type(namespace, p) for p in type.GetGenericParameterConstraints())
        namespace.var_types[name] = VarType(name, bounds)  # TODO - Handle duplicate names better, Handle Multiple Bounds Better
    return namespace.var_types[name]


_system_type_dict = {
    'System.Boolean': partial(process_system_type, 'BooleanType', 'System.Boolean', 'Union[bool, Boolean]'),
    'System.SByte':   partial(process_system_type, 'SByteType', 'System.SByte', 'Union[int, SByte]'),
    'System.Int16':   partial(process_system_type, 'ShortType', 'System.Int16', 'Union[int, Int16]'),
    'System.Int32':   partial(process_system_type, 'IntType', 'System.Int32', 'Union[int, Int32]'),
    'System.Int64':   partial(process_system_type, 'LongType', 'System.Int64', 'Union[int, Int64]'),
    'System.Byte':    partial(process_system_type, 'ByteType', 'System.Byte', 'Union[int, Byte]'),
    'System.UInt16':  partial(process_system_type, 'UShortType', 'System.UInt16', 'Union[int, UInt16]'),
    'System.UInt32':  partial(process_system_type, 'UIntType', 'System.UInt32', 'Union[int, UInt32]'),
    'System.UInt64':  partial(process_system_type, 'ULongType', 'System.UInt64', 'Union[int, UInt64]'),
    'System.IntPtr':  partial(process_system_type, 'NIntType', 'System.IntPtr', 'Union[int, IntPtr]'),
    'System.UIntPtr': partial(process_system_type, 'NUIntType', 'System.UIntPtr', 'Union[int, UIntPtr]'),
    'System.Single':  partial(process_system_type, 'FloatType', 'System.Single', 'Union[float, Single]'),
    'System.Double':  partial(process_system_type, 'DoubleType', 'System.Double', 'Union[float, Double]'),
    'System.Decimal': partial(process_system_type, 'DecimalType', 'System.Decimal', 'Union[float, Decimal]'),
    'System.Char':    partial(process_system_type, 'CharType', 'System.Char', 'Union[str, Char]'),
    'System.String':  partial(process_system_type, 'StringType', 'System.String', 'Union[str, String]'),
    'System.Object':  partial(process_system_type, 'ObjectType', 'System.Object', 'Union[object, Object]'),
    'System.Type':    partial(process_system_type, 'TypeType', 'System.Type', 'Union[type, Type]'),
    'System.Void':    partial(process_system_type, 'VoidType', 'System.Void', 'Union[None, Void]'),
}


def _strip_str(string: str) -> str:
    if not hasattr(_strip_str, 'pattern'):
        _strip_str.pattern = re.compile(r'(?:`\d+|&|\[\])')
    return _strip_str.pattern.sub('', string)


def _rm_tree(dir_path: Path):
    for child in dir_path.iterdir():
        if child.is_file():
            child.unlink()
        else:
            _rm_tree(child)
    dir_path.rmdir()
