import json
from collections import defaultdict
from functools import partial
from pathlib import Path
from typing import Dict, Tuple, Optional, List

import clr

import System
from System.Reflection import Assembly, ConstructorInfo, ParameterInfo, PropertyInfo, MethodInfo, EventInfo, FieldInfo
from .logging import logger
from .model import Parameter, WrappedType, Constructor, Namespace, Interface, SystemType, Property, Method, BaseType, VarType, EventType, Event, EnumField, Enum, Class, Delegate
from .options import options
from .util import time_function, time_it, make_python_name, strip_path_str, rm_tree


@time_function(log_func=logger.info)
def make(target_assembly_name: str):
    target_assembly_obj: Assembly = clr.AddReference(target_assembly_name)
    
    namespace_dict: Dict[str, List[System.Type]] = defaultdict(list)
    namespaces: Dict[str, Namespace] = {}
    
    with time_it('Parsing Assemblies', log_func=logger.info):
        assemblies: List[Assembly] = [target_assembly_obj]
        for parent_name_obj in target_assembly_obj.GetReferencedAssemblies():
            assemblies.append(Assembly.Load(parent_name_obj.Name))
        
        types_found = 0
        for assembly_obj in assemblies:
            for type in assembly_obj.GetTypes():
                if type.Namespace is None or type.IsNested:
                    continue
                logger.debug(f'Found Type \'{type.FullName}\' in Namespace \'{type.Namespace}\'')
                namespace_dict[type.Namespace].append(type)
                types_found += 1
        
        logger.info(f'Processing {types_found} Types in {len(namespace_dict)} Namespaces')
        for namespace_name, assembly_types in namespace_dict.items():
            if namespace_name not in namespaces:
                namespaces[namespace_name] = Namespace(namespace_name)
            namespace: Namespace = namespaces[namespace_name]
            
            for type_obj in assembly_types:
                _process_system_type_obj(namespace, type_obj)
    
    with time_it('Writing Stub Package', log_func=logger.info):
        stub_dir = options.output_dir / f'{target_assembly_name}-stubs'
        
        if options.overwrite or not stub_dir.exists():
            logger.info(f'Writing to Directory: {stub_dir}')
            stub_dir.mkdir(parents=True, exist_ok=True)
            
            assembly_name_type = target_assembly_obj.GetName()
            version = assembly_name_type.Version
            culture = 'neutral'
            if (culture_info := assembly_name_type.CultureInfo) is not None and (culture_name := culture_info.Name) != '':
                culture = culture_name
            public_key_token = ''.join(hex(b).lstrip('0x') for b in assembly_name_type.GetPublicKeyToken())
            
            logger.info(f'Writing: setup.cfg')
            setup_file = stub_dir / 'setup.cfg'
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
            
            logger.info(f'Writing: pyproject.toml')
            pyproject_file = stub_dir / 'pyproject.toml'
            pyproject_file.write_text('\n'.join([
                f'[build-system]',
                f'requires = ["setuptools", "wheel"]',
                f'build-backend = "setuptools.build_meta"',
            ]))
            
            logger.info(f'Writing: README.md')
            readme_file = stub_dir / 'README.md'
            readme_file.write_text('\n'.join([
                f'# {target_assembly_name}-stubs',
                f'Stubs Package for {target_assembly_name}',
                f'',
            ]))
            
            logger.info(f'Writing: LICENSE')
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
            
            logger.info(f'Writing: MANIFEST.in')
            manifest_file = stub_dir / 'MANIFEST.in'
            manifest_file.write_text('\n'.join(set(f'include {n.split(".")[0]}-stubs/*.pyi' for n in namespaces)) + '\n')
            
            logger.info(f'Writing: Stub Files')
            for namespace_name, namespace in namespaces.items():
                parent_dir: Path = stub_dir
                init_file: Path = parent_dir / '__init__.pyi'
                for n in namespace_name.split('.'):
                    namespace_dir: Path = parent_dir / strip_path_str(f'{n}-stubs' if parent_dir == stub_dir else n)
                    namespace_dir.mkdir(parents=True, exist_ok=True)
                    
                    init_file = namespace_dir / '__init__.pyi'
                    init_file.touch(exist_ok=True)
                    
                    parent_dir = namespace_dir
                logger.debug(f'Writing: Stub File \'{init_file}\'')
                init_file.write_text('\n'.join(namespace.to_lines()))
        else:
            logger.info('No Files Written')
        
        if options.json:  # TODO - Make this generate less files
            json_dir: Path = Path('logs') / target_assembly_name
            logger.info(f'Exporting Json Files: {json_dir}')
            json_dir.mkdir(parents=True, exist_ok=True)
            for namespace_name, assembly_types in namespace_dict.items():
                json_file = json_dir / f'{namespace_name}.json'
                try:
                    with json_file.open('w') as file:
                        logger.debug(f'Writing: {json_file.name}')
                        json.dump(list(map(lambda t: t.FullName, assembly_types)), file, indent=2)
                except OSError as e:
                    logger.warning(e)


@time_function(log_func=logger.info)
def group(assembly_names: List[str]):
    namespace_dict: Dict[str, List[Tuple[Assembly, str]]] = defaultdict(list)
    namespaces: Dict[str, Namespace] = {}
    
    with time_it('Parsing Assemblies', log_func=logger.info):
        types_found = 0
        for assembly_name in assembly_names:
            logger.info(f'Adding Assembly \'{assembly_name}\' to Namespaces')
            assembly: Assembly = clr.AddReference(assembly_name)
            
            for type in assembly.GetTypes():
                if type.Namespace is None or type.IsNested:
                    continue
                logger.debug(f'Found Type \'{type.FullName}\' in Namespace \'{type.Namespace}\'')
                namespace_dict[type.Namespace].append((assembly, type.FullName))
                types_found += 1
        
        logger.info(f'Processing {types_found} Types in {len(namespace_dict)} Namespaces')
        for name, type_names in namespace_dict.items():
            if name not in namespaces:
                namespaces[name] = Namespace(name)
            namespace: Namespace = namespaces[name]
            
            for assembly, type_name in type_names:
                _process_system_type_obj(namespace, assembly.GetType(type_name))
    
    with time_it('Writing Grouped Stubs', log_func=logger.info):
        stub_dir = options.output_dir / 'Grouped Stubs'
        
        if stub_dir.exists():
            rm_tree(stub_dir)
        
        logger.info(f'Writing to Directory: {stub_dir}')
        stub_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f'Writing: Stub Files')
        for name, namespace in namespaces.items():
            parent_dir: Path = stub_dir
            init_file: Path = parent_dir / '__init__.pyi'
            for n in name.split('.'):
                namespace_dir: Path = parent_dir / strip_path_str(f'{n}-stubs' if parent_dir == stub_dir else n)
                namespace_dir.mkdir(parents=True, exist_ok=True)
                
                init_file = namespace_dir / '__init__.pyi'
                init_file.touch(exist_ok=True)
                
                parent_dir = namespace_dir
            logger.debug(f'Writing: Stub File \'{init_file}\'')
            init_file.write_text('\n'.join(namespace.to_lines()))


def _process_system_type_obj(namespace: Namespace, system_type_obj: System.Type):
    if system_type_obj.IsValueType:
        if system_type_obj.IsEnum:
            enum = _process_enum(namespace, system_type_obj)
            namespace.enums[enum.name].append(enum)
            return
        struct = _process_class(namespace, system_type_obj)
        namespace.structs[struct.name].append(struct)
        return
    if system_type_obj.IsInterface:
        interface = _process_interface(namespace, system_type_obj)
        namespace.interfaces[interface.name].append(interface)
        return
    if (system_type_obj.IsSubclassOf(System.Delegate) or system_type_obj.IsSubclassOf(System.MulticastDelegate)) and system_type_obj not in [System.Type.GetType('System.Delegate'), System.Type.GetType('System.MulticastDelegate')]:
        delegate = _process_delegate(namespace, system_type_obj)
        namespace.delegates[delegate.name].append(delegate)
    if system_type_obj.IsClass:
        clazz = _process_class(namespace, system_type_obj)
        namespace.classes[clazz.name].append(clazz)
        return


def _process_class(namespace: Namespace, class_type_obj: System.Type) -> Class:
    logger.debug(f'Processing Class: {class_type_obj}')
    
    clazz = Class(make_python_name(class_type_obj.Name))
    
    clazz.abstract = class_type_obj.IsAbstract
    
    generic_arg_type: System.Type
    for generic_arg_type in class_type_obj.GetGenericArguments():
        clazz.generic_args.append(_get_var_type(namespace, generic_arg_type))
    
    if clazz.abstract and len(clazz.generic_args) > 0:
        namespace.py_imports.add('typing.Protocol')
    elif len(clazz.generic_args) > 0:
        namespace.py_imports.add('typing.Generic')
    elif clazz.abstract:
        namespace.py_imports.add('abc.ABC')
    
    if class_type_obj.BaseType is not None:
        clazz.super_type = _get_type(namespace, class_type_obj.BaseType)
    
    interface_type_obj: System.Type
    for interface_type_obj in class_type_obj.GetInterfaces():
        clazz.interfaces.append(_get_type(namespace, interface_type_obj))
    
    field_info: FieldInfo
    for field_info in class_type_obj.GetFields():
        if field_info.DeclaringType == class_type_obj:
            getter, setter = _process_field(namespace, field_info)
            clazz.fields.append(getter)
            if setter is not None:
                clazz.fields.append(setter)
    clazz.fields.sort(key=lambda p: p.name)
    
    constructor_info: ConstructorInfo
    constructor_list = [c for c in class_type_obj.GetConstructors()]
    overload = len(constructor_list) > 1
    for constructor_info in constructor_list:
        if constructor_info.DeclaringType == class_type_obj:
            clazz.constructors.append(_process_constructor(namespace, constructor_info, overload))
    
    property_info: PropertyInfo
    for property_info in class_type_obj.GetProperties():
        if property_info.DeclaringType == class_type_obj:
            getter, setter = _process_property(namespace, property_info)
            if getter is not None:
                clazz.properties.append(getter)
            if setter is not None:
                clazz.properties.append(setter)
    clazz.properties.sort(key=lambda p: p.name)
    
    method_info: MethodInfo
    method_dict = defaultdict(list)
    for method_info in class_type_obj.GetMethods():
        method_dict[method_info.Name].append(method_info)
    for method_list in method_dict.values():
        overload = len(method_list) > 1
        for method_info in method_list:
            if method_info.DeclaringType == class_type_obj:
                clazz.methods.append(_process_method(namespace, method_info, overload))
    clazz.methods.sort(key=lambda m: m.name)
    
    event_info: EventInfo
    for event_info in class_type_obj.GetEvents():
        if event_info.DeclaringType == class_type_obj:
            clazz.events.append(_process_event(namespace, event_info))
    clazz.events.sort(key=lambda e: e.name)
    
    nested_type_obj: System.Type
    for nested_type_obj in class_type_obj.GetNestedTypes():
        if nested_type_obj.IsValueType:
            if nested_type_obj.IsEnum:
                clazz.sub_enums.append(_process_enum(namespace, nested_type_obj))
                continue
            clazz.sub_structs.append(_process_class(namespace, nested_type_obj))
            continue
        if nested_type_obj.IsInterface:
            clazz.sub_interfaces.append(_process_interface(namespace, nested_type_obj))
            continue
        if nested_type_obj.IsClass:
            clazz.sub_classes.append(_process_class(namespace, nested_type_obj))
            continue
    
    return clazz


def _process_interface(namespace: Namespace, interface_type_obj: System.Type) -> Interface:
    logger.debug(f'Processing Interface: {interface_type_obj}')
    
    namespace.py_imports.add('typing.Protocol')
    
    interface = Interface(make_python_name(interface_type_obj.Name))
    
    generic_arg_type: System.Type
    for generic_arg_type in interface_type_obj.GetGenericArguments():
        interface.generic_args.append(_get_var_type(namespace, generic_arg_type))
    
    super_class_type_obj: System.Type
    for super_class_type_obj in interface_type_obj.GetInterfaces():
        interface.super_classes.append(_get_type(namespace, super_class_type_obj))
    
    property_info: PropertyInfo
    for property_info in interface_type_obj.GetProperties():
        if property_info.DeclaringType == interface_type_obj:
            getter, setter = _process_property(namespace, property_info)
            if getter is not None:
                interface.properties.append(getter)
            if setter is not None:
                interface.properties.append(setter)
    interface.properties.sort(key=lambda p: p.name)
    
    method_info: MethodInfo
    method_dict = defaultdict(list)
    for method_info in interface_type_obj.GetMethods():
        method_dict[method_info.Name].append(method_info)
    for method_list in method_dict.values():
        overload = len(method_list) > 1
        for method_info in method_list:
            if method_info.DeclaringType == interface_type_obj:
                interface.methods.append(_process_method(namespace, method_info, overload))
    interface.methods.sort(key=lambda m: m.name)
    
    event_info: EventInfo
    for event_info in interface_type_obj.GetEvents():
        if event_info.DeclaringType == interface_type_obj:
            interface.events.append(_process_event(namespace, event_info))
    interface.events.sort(key=lambda e: e.name)
    
    return interface


def _process_enum(namespace: Namespace, enum_type_obj: System.Type) -> Enum:
    logger.debug(f'Processing Enum: {enum_type_obj}')
    
    namespace.net_imports.add('System.Enum')
    
    enum = Enum(make_python_name(enum_type_obj.Name))
    
    enum_type = _get_type(namespace, enum_type_obj.GetEnumUnderlyingType())
    
    try:
        field_name: str
        for field_name, field_value in zip(enum_type_obj.GetEnumNames(), enum_type_obj.GetEnumValues()):
            enum.fields.append(EnumField(name=field_name, type=enum_type, value=field_value, doc_string=''))
    except System.NotSupportedException:
        field_info: FieldInfo
        for field_info in enum_type_obj.GetFields():
            enum.fields.append(EnumField(name=field_info.Name, type=enum_type, value='...', doc_string=''))
    enum.fields.sort(key=lambda f: f.value)
    
    return enum


def _process_delegate(namespace: Namespace, delegate_type_obj: System.Type) -> Delegate:
    logger.debug(f'Processing Delegate: {delegate_type_obj}')
    
    namespace.py_imports.add('typing.Callable')
    
    delegate = Delegate(make_python_name(delegate_type_obj.Name))
    
    invoke_method = delegate_type_obj.GetMethod('Invoke')
    
    parameter_info: ParameterInfo
    for parameter_info in invoke_method.GetParameters():
        delegate.input_types.append(_get_type(namespace, parameter_info.ParameterType))
    
    if invoke_method.ReturnType is not None:
        delegate.return_type = _get_type(namespace, invoke_method.ReturnType)
    
    return delegate


def _process_field(namespace: Namespace, field_info: FieldInfo) -> Tuple[Property, Optional[Property]]:
    logger.debug(f'Processing Field: {field_info}')
    
    field_name = make_python_name(field_info.Name)
    field_type = _get_type(namespace, field_info.FieldType)
    field_static = field_info.IsStatic
    
    getter = Property(name=field_name,
                      type=field_type,
                      setter=False,
                      static=field_static,
                      doc_string='')
    setter = None
    if not (field_info.IsInitOnly or field_info.IsLiteral):
        setter = Property(name=field_name,
                          type=field_type,
                          setter=True,
                          static=field_static,
                          doc_string='')
    return getter, setter


def _process_constructor(namespace: Namespace, constructor_info: ConstructorInfo, overload: bool) -> Constructor:
    logger.debug(f'Processing Constructor: {constructor_info}')
    
    if overload:
        namespace.py_imports.add('typing.overload')
    
    parameters = [_get_parameter(namespace, parameter_info) for parameter_info in constructor_info.GetParameters()]
    
    return Constructor(parameters=parameters,
                       overload=overload,
                       doc_string='')


def _process_property(namespace: Namespace, property_info: PropertyInfo) -> Tuple[Optional[Property], Optional[Property]]:
    logger.debug(f'Processing Property: {property_info}')
    # TODO - Special Case - Item
    
    property_type = _get_type(namespace, property_info.PropertyType)
    
    getter = None
    if (get_method := property_info.GetGetMethod()) is not None:
        getter = Property(name=make_python_name(property_info.Name),
                          type=property_type,
                          setter=False,
                          static=get_method.IsStatic,
                          doc_string='')
    
    setter = None
    if (set_method := property_info.GetSetMethod()) is not None:
        setter = Property(name=make_python_name(property_info.Name),
                          type=property_type,
                          setter=True,
                          static=set_method.IsStatic,
                          doc_string='')
    return getter, setter


def _process_method(namespace: Namespace, method_info: MethodInfo, overload: bool) -> Method:
    logger.debug(f'Processing Method: {method_info}')
    
    if overload:
        namespace.py_imports.add('typing.overload')
    
    # TODO - IsAbstract, IsVirtual, IsGenericMethod, IsGenericMethodDefinition
    
    name = make_python_name(method_info.Name)
    return_types = [_get_type(namespace, method_info.ReturnType)]
    static = method_info.IsStatic
    
    parameters = []
    for parameter_info in method_info.GetParameters():
        parameter = _get_parameter(namespace, parameter_info)
        parameters.append(parameter)
        if parameter.is_out:
            return_types.append(parameter.type)
    
    if len(return_types) > 1:
        namespace.py_imports.add('typing.Tuple')
    
    return Method(name=name,
                  parameters=tuple(parameters),
                  return_types=tuple(return_types),
                  static=static,
                  overload=overload,
                  doc_string='')


def _process_event(namespace: Namespace, event_info: EventInfo) -> Event:
    logger.debug(f'Processing Event: {event_info}')
    
    if 'EventType' not in namespace.sys_types:
        namespace.py_imports.add('typing.Generic')
        namespace.special_types['EventType'] = EventType()
        if 'T' not in namespace.var_types:
            namespace.py_imports.add('typing.TypeVar')
            namespace.var_types['T'] = VarType(name='T')
    
    name = make_python_name(event_info.Name)
    type = _get_type(namespace, event_info.EventHandlerType)
    
    return Event(name=name, type=type, doc_string='')


def _get_parameter(namespace: Namespace, parameter_info: ParameterInfo) -> Parameter:
    name = make_python_name(parameter_info.Name)
    type = _get_type(namespace, parameter_info.ParameterType)
    default = parameter_info.RawDefaultValue if parameter_info.IsOptional else None
    is_out = parameter_info.IsOut or type.is_ref
    
    return Parameter(name=name, type=type, default=default, is_out=is_out, doc_string='')


def _get_type(namespace: Namespace, type_obj: System.Type, parent_type: System.Type = None) -> BaseType:
    name = make_python_name(type_obj.ToString())
    import_name = name[:name.index('+')] if '+' in name else name
    name = name.replace('+', '.').split('.')[-1]
    
    base = name
    inner = tuple(_get_type(namespace, p, parent_type=parent_type) for p in type_obj.GetGenericArguments())
    
    if name in _system_type_dict:
        base = _system_type_dict[name](namespace)
    elif type_obj.IsGenericParameter:
        base = _get_var_type(namespace, type_obj, type_obj == parent_type)
    else:
        namespace.net_imports.add(import_name)
    
    new_type = WrappedType(base=base, inner=inner)
    new_type.is_ref = type_obj.IsByRef
    new_type.is_pointer = type_obj.IsPointer
    
    # If the type should be wrapped
    if System.Nullable.GetUnderlyingType(type_obj) is not None:
        namespace.py_imports.add('typing.Optional')
        nullable_type = _get_system_type('NullableType', 'System.Nullable', 'Union[Optional, Nullable]', namespace)
        return WrappedType(base=nullable_type, inner=(new_type,))
    if type_obj.IsArray:
        namespace.py_imports.add('typing.List')
        array_type = _get_system_type('ArrayType', 'System.Array', 'Union[List, Array]', namespace)
        return WrappedType(base=array_type, inner=(new_type,))
    return new_type


def _get_system_type(name: str, system_name: str, value: str, namespace: Namespace) -> SystemType:
    if system_name not in namespace.sys_types:
        namespace.net_imports.add(system_name)
        namespace.py_imports.add('typing.Union')
        namespace.sys_types[system_name] = SystemType(name=name, value=value)
    return namespace.sys_types[system_name]


def _get_var_type(namespace: Namespace, type_var: System.Type, force_unbounded: bool = False) -> VarType:
    name: str = make_python_name(type_var.Name)
    if name not in namespace.var_types:  # TODO - This will miss TypeVars that have bound if the name is the same as a previous TypeVar
        namespace.py_imports.add('typing.TypeVar')
        bounds = tuple() if force_unbounded else tuple(_get_type(namespace, p, parent_type=type_var) for p in type_var.GetGenericParameterConstraints())
        namespace.var_types[name] = VarType(name=name, bounds=bounds)  # TODO - Handle duplicate names better, Handle Multiple Bounds Better
    return namespace.var_types[name]


_system_type_dict = {
    'Boolean': partial(_get_system_type, 'BooleanType', 'System.Boolean', 'Union[bool, Boolean]'),
    'SByte':   partial(_get_system_type, 'SByteType', 'System.SByte', 'Union[int, SByte]'),
    'Int16':   partial(_get_system_type, 'ShortType', 'System.Int16', 'Union[int, Int16]'),
    'Int32':   partial(_get_system_type, 'IntType', 'System.Int32', 'Union[int, Int32]'),
    'Int64':   partial(_get_system_type, 'LongType', 'System.Int64', 'Union[int, Int64]'),
    'Byte':    partial(_get_system_type, 'ByteType', 'System.Byte', 'Union[int, Byte]'),
    'UInt16':  partial(_get_system_type, 'UShortType', 'System.UInt16', 'Union[int, UInt16]'),
    'UInt32':  partial(_get_system_type, 'UIntType', 'System.UInt32', 'Union[int, UInt32]'),
    'UInt64':  partial(_get_system_type, 'ULongType', 'System.UInt64', 'Union[int, UInt64]'),
    'IntPtr':  partial(_get_system_type, 'NIntType', 'System.IntPtr', 'Union[int, IntPtr]'),
    'UIntPtr': partial(_get_system_type, 'NUIntType', 'System.UIntPtr', 'Union[int, UIntPtr]'),
    'Single':  partial(_get_system_type, 'FloatType', 'System.Single', 'Union[float, Single]'),
    'Double':  partial(_get_system_type, 'DoubleType', 'System.Double', 'Union[float, Double]'),
    'Decimal': partial(_get_system_type, 'DecimalType', 'System.Decimal', 'Union[float, Decimal]'),
    'Char':    partial(_get_system_type, 'CharType', 'System.Char', 'Union[str, Char]'),
    'String':  partial(_get_system_type, 'StringType', 'System.String', 'Union[str, String]'),
    'Object':  partial(_get_system_type, 'ObjectType', 'System.Object', 'Object'),
    'Type':    partial(_get_system_type, 'TypeType', 'System.Type', 'Union[type, Type]'),
    'Void':    partial(_get_system_type, 'VoidType', 'System.Void', 'Union[None, Void]'),
}
