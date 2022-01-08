import json
import logging
import re
from collections import defaultdict
from functools import partial
from pathlib import Path
from typing import Dict, Tuple, Optional, Any

import clr

from System import Type, Nullable, Delegate as _Delegate, AppDomain
from System.Reflection import Assembly, ConstructorInfo, ParameterInfo, PropertyInfo, MethodInfo, EventInfo, FieldInfo
from .logging import logger
from .model import Parameter, RegularType, Constructor, Namespace, Interface, SystemType, Property, Method, TypeBase, VarType, EventType, Event, EnumField, Enum, Class, Delegate
from .options import Options


def make(target_assembly_name: str, options: Options):
    """Main Processing Function"""
    logger.info('=' * 80)
    logger.info(f'Making [{target_assembly_name}]')
    
    target_assembly: Assembly = clr.AddReference(target_assembly_name)
    
    namespace_dict = defaultdict(list)
    
    assembly: Assembly
    for assembly in AppDomain.CurrentDomain.GetAssemblies():
        if assembly.IsDynamic:
            continue
        assembly_name: str = assembly.GetName().Name
        if assembly_name == target_assembly_name:  # TODO - Get types from all loaded assemblies
            logger.info(f'Parsing Assembly: {assembly_name}')
            for type in target_assembly.GetTypes():
                if type.Namespace is None or type.IsNested:
                    continue
                logger.debug(f'Found Type \'{type.FullName}\' in Namespace \'{type.Namespace}\'')
                namespace_dict[type.Namespace].append(type.FullName)
        else:
            logger.debug(f'Assembly Skipped. Does not match Target: {assembly_name}')
    
    namespaces: Dict[str, Namespace] = {}
    
    for name, type_names in namespace_dict.items():
        if name not in namespaces:
            namespaces[name] = Namespace(name)
        namespace: Namespace = namespaces[name]
        
        for type_name in type_names:
            process_declared_type(namespace, target_assembly.GetType(type_name))
    
    stub_dir = options.output_dir / f'{target_assembly_name}-stubs'
    
    if options.overwrite and stub_dir.exists():
        logger.info(r'Deleteing Existing Stubs')
        _rm_tree(stub_dir)
    
    if not stub_dir.exists():
        logger.info(f'Writing to Directory: {stub_dir}')
        stub_dir.mkdir(parents=True, exist_ok=True)
        
        assembly_name_type = target_assembly.GetName()
        version = assembly_name_type.Version
        culture = 'neutral'
        if (culture_info := assembly_name_type.CultureInfo) is not None and (culture_name := culture_info.Name) != '':
            culture = culture_name
        public_key_token = ''.join(hex(b).lstrip('0x') for b in assembly_name_type.GetPublicKeyToken())
        
        setup_file = stub_dir / 'setup.cfg'
        logger.info(f'Writing: setup.cfg')
        setup_file.write_text('\n'.join([
            f'[metadata]',
            f'name = {target_assembly_name}-stubs',
            f'version = {version}',
            f'description = Stubs Package for {target_assembly_name}',
            f'long_description = file: README.md, LICENSE',
            f'keywords = pythonnet, stubs, {target_assembly_name}',
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
        logger.info(f'Writing: README.md')
        readme_file.write_text('\n'.join([
            f'# {target_assembly_name}-stubs',
            f'Stubs Package for {target_assembly_name}',
            f'',
        ]))
        
        license_file = stub_dir / 'LICENSE'
        logger.info(f'Writing: LICENSE')
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
        logger.info(f'Writing: MANIFEST.in')
        manifest_file.write_text('\n'.join(set(f'include {n.split(".")[0]}-stubs/*.pyi' for n in namespaces)) + '\n')
        
        logger.info(f'Writing: Stub Files')
        for name, namespace in namespaces.items():
            parent_dir: Path = stub_dir
            init_file: Path = parent_dir / '__init__.pyi'
            for n in name.split('.'):
                namespace_dir: Path = parent_dir / (f'{n}-stubs' if parent_dir == stub_dir else n)
                namespace_dir.mkdir(parents=True, exist_ok=True)
                
                init_file = namespace_dir / '__init__.pyi'
                init_file.touch(exist_ok=True)
                
                parent_dir = namespace_dir
            logger.debug(f'Writing Stub File: \'{init_file}\'')
            init_file.write_text(namespace.print())
    else:
        logger.info('No Files Written')
    
    if options.json:
        json_dir: Path = Path('logs') / target_assembly_name
        logger.info(f'Exporting Json Files to \'{json_dir}\'')
        json_dir.mkdir(parents=True, exist_ok=True)
        for name, type_names in namespace_dict.items():
            json_file = json_dir / f'{name}.json'
            with json_file.open('w') as file:
                logger.debug(f'Writing: {json_file.name}')
                json.dump(type_names, file, indent=2)


def process_declared_type(namespace: Namespace, type: Type):
    if type.IsValueType:
        if type.IsEnum:
            enum = process_enum(namespace, type)
            namespace.enums[enum.name].append(enum)
            return
        struct = process_class(namespace, type)
        namespace.structs[struct.name].append(struct)
        return
    if type.IsInterface:
        interface = process_interface(namespace, type)
        namespace.interfaces[interface.name].append(interface)
        return
    if type.IsSubclassOf(_Delegate) and type not in [Type.GetType('System.Delegate') and Type.GetType('System.MulticastDelegate')]:
        delegate = process_delegate(namespace, type)
        namespace.delegates[delegate.name].append(delegate)
    if type.IsClass:
        clazz = process_class(namespace, type)
        namespace.classes[clazz.name].append(clazz)
        return


def process_class(namespace: Namespace, class_type: Type) -> Class:
    logger.debug(f'Processing Class: \'{class_type}\'')
    
    clazz = Class(_strip_str(class_type.Name))
    
    clazz.abstract = class_type.IsAbstract
    
    clazz.type_args = [process_var_type(namespace, type_arg.Name, type_arg) for type_arg in class_type.GetGenericArguments()]
    
    if clazz.abstract and len(clazz.type_args) > 0:
        namespace.py_imports.add('typing.Prototype')
    elif len(clazz.type_args) > 0:
        namespace.py_imports.add('typing.Generic')
    elif clazz.abstract:
        namespace.py_imports.add('abc.ABC')
    
    clazz.super_type = process_type(namespace, class_type.BaseType) if class_type.BaseType is not None else None
    for interface_type in class_type.GetInterfaces():
        clazz.interfaces.append(process_type(namespace, interface_type))
    
    for field_info in class_type.GetFields():
        if field_info.DeclaringType == class_type:
            getter, setter = process_field(namespace, field_info)
            clazz.fields.append(getter)
            if setter is not None:
                clazz.fields.append(setter)
    clazz.fields.sort(key=lambda p: p.name)
    
    constructor_list = [c for c in class_type.GetConstructors()]
    overload = len(constructor_list) > 1
    for constructor_info in constructor_list:
        if constructor_info.DeclaringType == class_type:
            clazz.constructors.append(process_constructor(namespace, constructor_info, overload))
    
    for property_info in class_type.GetProperties():
        if property_info.DeclaringType == class_type:
            getter, setter = process_property(namespace, property_info)
            if getter is not None:
                clazz.properties.append(getter)
            if setter is not None:
                clazz.properties.append(setter)
    clazz.properties.sort(key=lambda p: p.name)
    
    method_dict = defaultdict(list)
    for method_info in class_type.GetMethods():
        method_dict[method_info.Name].append(method_info)
    for method_list in method_dict.values():
        overload = len(method_list) > 1
        for method_info in method_list:
            if method_info.DeclaringType == class_type:
                clazz.methods.append(process_method(namespace, method_info, overload))
    clazz.methods.sort(key=lambda m: m.name)
    
    for event_info in class_type.GetEvents():
        if event_info.DeclaringType == class_type:
            clazz.events.append(process_event(namespace, event_info))
    clazz.events.sort(key=lambda e: e.name)
    
    for nested_type in class_type.GetNestedTypes():
        if nested_type.IsValueType:
            if nested_type.IsEnum:
                clazz.sub_enums.append(process_enum(namespace, nested_type))
                continue
            clazz.sub_structs.append(process_class(namespace, nested_type))
            continue
        if nested_type.IsInterface:
            clazz.sub_interfaces.append(process_interface(namespace, nested_type))
            continue
        if nested_type.IsClass:
            clazz.sub_classes.append(process_class(namespace, nested_type))
            continue
    
    return clazz


def process_interface(namespace: Namespace, interface_type: Type) -> Interface:
    logger.debug(f'Processing Interface: {interface_type}')
    
    namespace.py_imports.add('typing.Protocol')
    
    interface = Interface(_strip_str(interface_type.Name))
    
    interface.type_args = [process_var_type(namespace, type_arg.Name, type_arg) for type_arg in interface_type.GetGenericArguments()]
    
    interface.bases = [process_type(namespace, base) for base in interface_type.GetInterfaces()]
    
    property_info: PropertyInfo
    for property_info in interface_type.GetProperties():
        if property_info.DeclaringType == interface_type:
            getter, setter = process_property(namespace, property_info)
            if getter is not None:
                interface.properties.append(getter)
            if setter is not None:
                interface.properties.append(setter)
    interface.properties.sort(key=lambda p: p.name)
    
    method_info: MethodInfo
    method_dict = defaultdict(list)
    for method_info in interface_type.GetMethods():
        method_dict[method_info.Name].append(method_info)
    for method_list in method_dict.values():
        overload = len(method_list) > 1
        for method_info in method_list:
            if method_info.DeclaringType == interface_type:
                interface.methods.append(process_method(namespace, method_info, overload))
    interface.methods.sort(key=lambda m: m.name)
    
    event_info: EventInfo
    for event_info in interface_type.GetEvents():
        if event_info.DeclaringType == interface_type:
            interface.events.append(process_event(namespace, event_info))
    interface.events.sort(key=lambda e: e.name)
    
    return interface


def process_enum(namespace: Namespace, enum_type: Type) -> Enum:
    logger.debug(f'Processing Enum: \'{enum_type}\'')
    
    namespace.net_imports.add('System.Enum')
    
    enum = Enum(_strip_str(enum_type.Name))
    
    type = process_type(namespace, enum_type.GetEnumUnderlyingType())
    
    for name, value in zip(enum_type.GetEnumNames(), enum_type.GetEnumValues()):
        logger.debug(f'Found Processing Field: {name}: {type} = {value}')
        enum_field = EnumField(name=name, type=type, value=str(value), doc_string='')
        enum.fields.append(enum_field)
    
    return enum


def process_delegate(namespace: Namespace, delegate_type: Type) -> Delegate:
    logger.debug(f'Processing Delegate: \'{delegate_type}\'')
    
    namespace.py_imports.add('typing.Callable')
    
    name = _strip_str(delegate_type.Name)
    
    invoke_method = delegate_type.GetMethod('Invoke')
    
    input_types = [process_type(namespace, p.ParameterType) for p in invoke_method.GetParameters()]
    return_type = process_type(namespace, invoke_method.ReturnType) if invoke_method.ReturnType is not None else None
    
    return Delegate(name=name,
                    input_types=tuple(input_types),
                    return_type=return_type,
                    doc_string='')


def process_field(namespace: Namespace, field_info: FieldInfo) -> Tuple[Property, Optional[Property]]:
    field_type = process_type(namespace, field_info.FieldType)
    
    getter = Property(name=field_info.Name,
                      type=field_type,
                      setter=False,
                      static=field_info.IsStatic,
                      doc_string='')
    setter = None
    if not (field_info.IsInitOnly or field_info.IsLiteral):
        setter = Property(name=field_info.Name,
                          type=field_type,
                          setter=True,
                          static=field_info.IsStatic,
                          doc_string='')
    return getter, setter


def process_constructor(namespace: Namespace, constructor_info: ConstructorInfo, overload: bool) -> Constructor:
    logger.debug(f'Processing Constructor: \'{constructor_info}\'')
    
    parameters = [process_parameter(namespace, parameter_info) for parameter_info in constructor_info.GetParameters()]
    
    return Constructor(parameters=parameters,
                       overload=overload,
                       doc_string='')


def process_property(namespace: Namespace, property_info: PropertyInfo) -> Tuple[Optional[Property], Optional[Property]]:
    if not property_info.CanRead:
        return None, None
    
    # TODO - Special Case - Item
    
    static = property_info.GetGetMethod().IsStatic
    
    property_type = process_type(namespace, property_info.PropertyType)
    
    getter = Property(name=property_info.Name,
                      type=property_type,
                      setter=False,
                      static=static,
                      doc_string='')
    
    setter = None
    if property_info.CanWrite:
        setter = Property(name=property_info.Name,
                          type=property_type,
                          setter=True,
                          static=static,
                          doc_string='')
    return getter, setter


def process_method(namespace: Namespace, method_info: MethodInfo, overload: bool) -> Method:
    # TODO - IsAbstract, IsVirtual, IsGenericMethod, IsGenericMethodDefinition
    
    if overload:
        namespace.py_imports.add('typing.overload')
    
    static = method_info.IsStatic
    
    return_types = [process_type(namespace, method_info.ReturnType)]
    
    parameters = []
    for parameter_info in method_info.GetParameters():
        parameter = process_parameter(namespace, parameter_info)
        parameters.append(parameter)
        if parameter.is_out:
            return_types.append(parameter.type)
    
    if len(return_types) > 1:
        namespace.py_imports.add('typing.Tuple')
    return Method(name=method_info.Name,
                  parameters=tuple(parameters),
                  return_types=tuple(return_types),
                  static=static,
                  overload=overload,
                  self_type=None,
                  doc_string='')


def process_event(namespace: Namespace, event_info: EventInfo) -> Event:
    if 'EventType' not in namespace.sys_types:
        namespace.py_imports.add('typing.Generic')
        namespace.special_types['EventType'] = EventType()
    return Event(name=event_info.Name,
                 type=process_type(namespace, event_info.EventHandlerType),
                 doc_string='')


def process_parameter(namespace: Namespace, parameter_info: ParameterInfo) -> Parameter:
    default = None
    if parameter_info.IsOptional:
        default = parameter_info.RawDefaultValue
    
    parameter_type = process_type(namespace, parameter_info.ParameterType)
    
    # TODO - riid: Guid&, pCorSig: Void*, Char*, Byte*, SByte*
    
    # print('    parameter.Name          ', parameter_info.Name)
    # print('    parameter.Type          ', parameter_info.ParameterType)
    # print('    parameter.Type.IsByRef  ', parameter_info.ParameterType.IsByRef)
    # print('    parameter.Type.IsPointer', parameter_info.ParameterType.IsPointer)
    return Parameter(name=parameter_info.Name,
                     type=parameter_type,
                     default=default,
                     is_in=parameter_info.IsIn,
                     is_out=parameter_info.IsOut,
                     doc_string='')


def process_type(namespace: Namespace, type: Type, parent_var_type: Type = None) -> TypeBase:
    name = _strip_str(type.ToString()).replace('*', '')  # TODO - Handle Pointers Better
    import_name = name[:name.index('+')] if '+' in name else name
    name = name.replace('+', '.').split('.')[-1]
    
    # if type.IsByRef:
    # if type.IsPointer:

    if name in _system_type_dict:
        new_type = _system_type_dict[name](namespace)
    elif type.IsGenericType:
        logging.debug(f'Processing Generic Type: {import_name}')
        namespace.net_imports.add(import_name)
        types = tuple(process_type(namespace, p, parent_var_type=parent_var_type) for p in type.GetGenericArguments())
        new_type = RegularType(base=name, inner=types)
    elif type.IsGenericParameter or type.ContainsGenericParameters:
        new_type = process_var_type(namespace, name, type, parent_var_type == parent_var_type)
    else:
        logging.debug(f'Processing Regular Type: {import_name}')
        namespace.net_imports.add(import_name)
        new_type = RegularType(base=name)
    
    # If the type should be wrapped
    if Nullable.GetUnderlyingType(type) is not None:
        namespace.py_imports.add('typing.Optional')
        nullable_type = process_system_type('NullableType', 'System.Nullable', 'Union[Optional, Nullable]', namespace)
        return RegularType(base=nullable_type, inner=(new_type,))
    if type.IsArray:
        namespace.py_imports.add('typing.List')
        array_type = process_system_type('ArrayType', 'System.Array', 'Union[List, Array]', namespace)
        return RegularType(base=array_type, inner=(new_type,))
    return new_type


def process_system_type(name: str, system_name: str, value: str, namespace: Namespace) -> SystemType:
    if system_name not in namespace.sys_types:
        logger.debug(f'Processing System Type: {system_name}')
        namespace.net_imports.add(system_name)
        namespace.py_imports.add('typing.Union')
        namespace.sys_types[system_name] = SystemType(name=name, value=value)
    return namespace.sys_types[system_name]


def process_var_type(namespace: Namespace, name: str, type_var: Type, force_unbounded: bool = False) -> VarType:
    if name not in namespace.var_types:
        logger.debug(f'Processing Var Type: {type_var}')
        namespace.py_imports.add('typing.TypeVar')
        # Handle Recursive Case by defaulting to unbounded VarType
        bounds = tuple() if force_unbounded else tuple(process_type(namespace, p, parent_var_type=type_var) for p in type_var.GetGenericParameterConstraints())
        namespace.var_types[name] = VarType(name=name, bounds=bounds)  # TODO - Handle duplicate names better, Handle Multiple Bounds Better
    return namespace.var_types[name]


_system_type_dict = {
    'Boolean': partial(process_system_type, 'BooleanType', 'System.Boolean', 'Union[bool, Boolean]'),
    'SByte':   partial(process_system_type, 'SByteType', 'System.SByte', 'Union[int, SByte]'),
    'Int16':   partial(process_system_type, 'ShortType', 'System.Int16', 'Union[int, Int16]'),
    'Int32':   partial(process_system_type, 'IntType', 'System.Int32', 'Union[int, Int32]'),
    'Int64':   partial(process_system_type, 'LongType', 'System.Int64', 'Union[int, Int64]'),
    'Byte':    partial(process_system_type, 'ByteType', 'System.Byte', 'Union[int, Byte]'),
    'UInt16':  partial(process_system_type, 'UShortType', 'System.UInt16', 'Union[int, UInt16]'),
    'UInt32':  partial(process_system_type, 'UIntType', 'System.UInt32', 'Union[int, UInt32]'),
    'UInt64':  partial(process_system_type, 'ULongType', 'System.UInt64', 'Union[int, UInt64]'),
    'IntPtr':  partial(process_system_type, 'NIntType', 'System.IntPtr', 'Union[int, IntPtr]'),
    'UIntPtr': partial(process_system_type, 'NUIntType', 'System.UIntPtr', 'Union[int, UIntPtr]'),
    'Single':  partial(process_system_type, 'FloatType', 'System.Single', 'Union[float, Single]'),
    'Double':  partial(process_system_type, 'DoubleType', 'System.Double', 'Union[float, Double]'),
    'Decimal': partial(process_system_type, 'DecimalType', 'System.Decimal', 'Union[float, Decimal]'),
    'Char':    partial(process_system_type, 'CharType', 'System.Char', 'Union[str, Char]'),
    'String':  partial(process_system_type, 'StringType', 'System.String', 'Union[str, String]'),
    'Object':  partial(process_system_type, 'ObjectType', 'System.Object', 'Union[object, Object]'),
    'Type':    partial(process_system_type, 'TypeType', 'System.Type', 'Union[type, Type]'),
    'Void':    partial(process_system_type, 'VoidType', 'System.Void', 'Union[None, Void]'),
}


def _dump_json_log(namespaces_dict: Dict[str, Any]):
    json_dir: Path = Path('logs')
    json_dir.mkdir(exist_ok=True)
    name = '-'.join(namespaces_dict.keys())
    filepath = json_dir / f'{name}.json'
    with filepath.open('w') as fp:
        json.dump(namespaces_dict, fp, indent=2)


def _strip_str(string: str) -> str:
    if not hasattr(_strip_str, 'pattern'):
        _strip_str.pattern = re.compile(r'`\d+|&|\[]')
    string = _strip_str.pattern.sub('', string)
    if '[' in string:
        return string[:string.index('[')]
    return string


def _rm_tree(dir_path: Path):
    for child in dir_path.iterdir():
        if child.is_file():
            child.unlink()
        else:
            _rm_tree(child)
    dir_path.rmdir()
