import re
from collections import defaultdict
from functools import partial
from pathlib import Path
from typing import Dict, Tuple, Optional

import clr

from System import Type, Nullable, Delegate as _Delegate, MulticastDelegate
from System.Reflection import Assembly, ConstructorInfo, ParameterInfo, PropertyInfo, MethodInfo, EventInfo, FieldInfo
from .logger import logger
from .model import Parameter, RegularType, Constructor, Namespace, Interface, SystemType, Property, Method, TypeBase, VarType, EventType, Event, EnumField, Enum, Class, Delegate
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
            process_declared_type(namespace, assembly.GetType(type_name))
    
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
        public_key_token = ''.join(hex(b).lstrip('0x') for b in assembly_name_type.GetPublicKeyToken())
        
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
            init_file: Path = parent_dir / '__init__.pyi'
            for n in name.split('.'):
                if parent_dir == stub_dir:
                    namespace_dir = parent_dir / f'{n}-stubs'
                else:
                    namespace_dir = parent_dir / n
                namespace_dir.mkdir(exist_ok=True)
                
                init_file = namespace_dir / '__init__.pyi'
                init_file.touch(exist_ok=True)
                
                parent_dir = namespace_dir
            init_file.write_text(namespace.print())


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
    name = _strip_str(class_type.Name)
    
    abstract = class_type.IsAbstract
    
    type_args = [process_var_type(namespace, type_arg.Name, type_arg) for type_arg in class_type.GetGenericArguments()]
    
    if abstract and len(type_args) > 0:
        namespace.py_imports.add('typing.Prototype')
    elif len(type_args) > 0:
        namespace.py_imports.add('typing.Generic')
    elif abstract:
        namespace.py_imports.add('abc.ABC')
    
    super_type = process_type(namespace, class_type.BaseType) if class_type.BaseType is not None else None
    interfaces = []
    for interface_type in class_type.GetInterfaces():
        interfaces.append(process_type(namespace, interface_type))
    
    fields = []
    for field_info in class_type.GetFields():
        if field_info.DeclaringType == class_type:
            getter, setter = process_field(namespace, field_info)
            fields.append(getter)
            if setter is not None:
                fields.append(setter)
    fields.sort(key=lambda p: p.name)
    
    constructor_list = [c for c in class_type.GetConstructors()]
    overload = len(constructor_list) > 1
    constructors = []
    for constructor_info in constructor_list:
        if constructor_info.DeclaringType == class_type:
            constructors.append(process_constructor(namespace, constructor_info, overload))
    
    properties = []
    for property_info in class_type.GetProperties():
        if property_info.DeclaringType == class_type:
            getter, setter = process_property(namespace, property_info)
            if getter is not None:
                properties.append(getter)
            if setter is not None:
                properties.append(setter)
    properties.sort(key=lambda p: p.name)
    
    methods = []
    method_dict = defaultdict(list)
    for method_info in class_type.GetMethods():
        method_dict[method_info.Name].append(method_info)
    for method_list in method_dict.values():
        overload = len(method_list) > 1
        for method_info in method_list:
            if method_info.DeclaringType == class_type:
                methods.append(process_method(namespace, method_info, overload))
    methods.sort(key=lambda m: m.name)
    
    events = []
    for event_info in class_type.GetEvents():
        if event_info.DeclaringType == class_type:
            events.append(process_event(namespace, event_info))
    events.sort(key=lambda e: e.name)
    
    sub_classes = []
    sub_structs = []
    sub_interfaces = []
    sub_enums = []
    for nested_type in class_type.GetNestedTypes():
        if nested_type.IsValueType:
            if nested_type.IsEnum:
                sub_enums.append(process_enum(namespace, nested_type))
                continue
            sub_structs.append(process_class(namespace, nested_type))
            continue
        if nested_type.IsInterface:
            sub_interfaces.append(process_interface(namespace, nested_type))
            continue
        if nested_type.IsClass:
            sub_classes.append(process_class(namespace, nested_type))
            continue
    
    return Class(name=name,
                 abstract=abstract,
                 type_args=tuple(type_args),
                 super_type=super_type,
                 interfaces=tuple(interfaces),
                 fields=tuple(fields),
                 constructors=tuple(constructors),
                 properties=tuple(properties),
                 methods=tuple(methods),
                 events=tuple(events),
                 sub_classes=tuple(sub_classes),
                 sub_structs=tuple(sub_structs),
                 sub_interfaces=tuple(sub_interfaces),
                 sub_enums=tuple(sub_enums),
                 doc_string='')


def process_interface(namespace: Namespace, interface_type: Type) -> Interface:
    namespace.py_imports.add('typing.Protocol')
    name = _strip_str(interface_type.Name)
    # if name in namespace.interfaces:
    #     return  # Redeclared Interface Type. This should only happen for generic types. ie: Type -> Type<T>
    
    type_args = [process_var_type(namespace, type_arg.Name, type_arg) for type_arg in interface_type.GetGenericArguments()]
    
    bases = [process_type(namespace, base) for base in interface_type.GetInterfaces()]
    
    property_info: PropertyInfo
    properties = []
    for property_info in interface_type.GetProperties():
        if property_info.DeclaringType == interface_type:
            getter, setter = process_property(namespace, property_info)
            if getter is not None:
                properties.append(getter)
            if setter is not None:
                properties.append(setter)
    properties.sort(key=lambda p: p.name)
    
    method_info: MethodInfo
    methods = []
    method_dict = defaultdict(list)
    for method_info in interface_type.GetMethods():
        method_dict[method_info.Name].append(method_info)
    for method_list in method_dict.values():
        overload = len(method_list) > 1
        for method_info in method_list:
            if method_info.DeclaringType == interface_type:
                methods.append(process_method(namespace, method_info, overload))
    methods.sort(key=lambda m: m.name)
    
    event_info: EventInfo
    events = []
    for event_info in interface_type.GetEvents():
        if event_info.DeclaringType == interface_type:
            events.append(process_event(namespace, event_info))
    events.sort(key=lambda e: e.name)
    
    return Interface(name=name,
                     type_args=tuple(type_args),
                     bases=tuple(bases),
                     properties=tuple(properties),
                     methods=tuple(methods),
                     events=tuple(events),
                     doc_string='')


def process_enum(namespace: Namespace, enum_type: Type) -> Enum:
    namespace.net_imports.add('System.Enum')
    
    value_type = process_type(namespace, enum_type.GetEnumUnderlyingType())
    
    enum_fields = []
    for name, value in zip(enum_type.GetEnumNames(), enum_type.GetEnumValues()):
        enum_fields.append(EnumField(name=name,
                                     type=value_type,
                                     value=str(value),
                                     doc_string=''))
    
    return Enum(name=enum_type.Name,
                fields=tuple(enum_fields),
                doc_string='')


def process_delegate(namespace: Namespace, delegate_type: Type) -> Delegate:
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
    parameters = [process_parameter(namespace, parameter_info) for parameter_info in constructor_info.GetParameters()]
    
    return Constructor(parameters=tuple(parameters),
                       overload=overload,
                       no_return=False,
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
    name = _strip_str(type.ToString())
    name = name.replace('*', '')  # TODO - Handle Pointers Better
    
    # if type.IsByRef:
    # if type.IsPointer:
    
    if name in namespace.sys_types:
        new_type = namespace.sys_types[name]
    # elif name in namespace.net_imports:
    #     new_type = Type(base=type.Name)
    elif type.IsGenericType:
        if '+' in name:
            namespace.net_imports.add(name[:name.index('+')])
        else:
            namespace.net_imports.add(name)
        types = tuple(process_type(namespace, p, parent_var_type=parent_var_type) for p in type.GetGenericArguments())
        # new_type = Type(base=type.Name, inner=types)
        new_type = RegularType(base=name.replace('+', '.').split('.')[-1], inner=types)
    elif type.IsGenericParameter or type.ContainsGenericParameters:
        new_type = process_var_type(namespace, name, type, parent_var_type == parent_var_type)
    elif name in _system_type_dict:
        new_type = _system_type_dict[name](namespace)
    # obsolete_type = SystemType('Obsolete', 'NoReturn')
    else:
        if '+' in name:
            namespace.net_imports.add(name[:name.index('+')])
        else:
            namespace.net_imports.add(name)
        new_type = RegularType(base=name.replace('+', '.').split('.')[-1])
        # new_type = Type(base=type.Name)
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
        namespace.net_imports.add(system_name)
        namespace.py_imports.add('typing.Union')
        namespace.sys_types[system_name] = SystemType(name=name, value=value)
    return namespace.sys_types[system_name]


def process_var_type(namespace: Namespace, name: str, type: Type, force_unbounded: bool = False) -> VarType:
    if name not in namespace.var_types:
        namespace.py_imports.add('typing.TypeVar')
        # Handle Recursive Case by defaulting to unbounded VarType
        bounds = tuple() if force_unbounded else tuple(process_type(namespace, p, parent_var_type=type) for p in type.GetGenericParameterConstraints())
        namespace.var_types[name] = VarType(name=name, bounds=bounds)  # TODO - Handle duplicate names better, Handle Multiple Bounds Better
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
