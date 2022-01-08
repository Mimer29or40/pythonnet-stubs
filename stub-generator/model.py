from __future__ import annotations

from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass, field
from functools import partial
from typing import Optional, Tuple, List, Dict, Union, Set


class Member(ABC):
    @abstractmethod
    def print(self, indent: int = 0) -> str: ...


@dataclass
class Namespace(Member):
    """
    IMPORTS
    
    __doc__ = DOC_STRING
    
    SYSTEM_TYPES
    
    VAR_TYPES
    
    # ---------- Classes ---------- #
    
    CLASSES
    
    # ---------- Structs ---------- #
    
    STRUCTS
    
    # ---------- Interfaces ---------- #
    
    INTERFACES
    
    # ---------- Enums ---------- #
    
    ENUMS
    
    # ---------- Delegates ---------- #
    
    DELEGATES
    
    __all__ = [
        ', '.join(MEMBERS)
    ]
    """
    
    name: str
    py_imports: Set[str] = field(default_factory=set, repr=False)
    net_imports: Set[str] = field(default_factory=set, repr=False)
    var_types: Dict[str, VarType] = field(default_factory=dict, repr=False)
    sys_types: Dict[str, SystemType] = field(default_factory=dict, repr=False)
    special_types: Dict[str, SpecialType] = field(default_factory=dict, repr=False)
    classes: Dict[str, List[Class]] = field(default_factory=partial(defaultdict, list), repr=False)
    structs: Dict[str, List[Class]] = field(default_factory=partial(defaultdict, list), repr=False)
    interfaces: Dict[str, List[Interface]] = field(default_factory=partial(defaultdict, list), repr=False)
    enums: Dict[str, List[Enum]] = field(default_factory=partial(defaultdict, list), repr=False)
    delegates: Dict[str, List[Delegate]] = field(default_factory=partial(defaultdict, list), repr=False)
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        py_imports = ''
        if len(self.py_imports) > 0:
            bases = sorted(set('.'.join(i.split('.')[:-1]) for i in self.py_imports))
            import_str_list = []
            for base in bases:
                prefix = f'{base}.'
                classes = sorted(set(i[len(prefix):] for i in self.py_imports if i.startswith(prefix)))
                import_str_list.append(f'from {base} import {", ".join(classes)}')
            py_imports = '\n'.join(import_str_list)
            py_imports = f'\n\n{py_imports}'
        
        net_imports = ''
        if len(self.net_imports) > 0:
            bases = sorted(set('.'.join(i.split('.')[:-1]) for i in self.net_imports))
            import_str_list = []
            for base in bases:
                if base == self.name:
                    continue
                prefix = f'{base}.'
                classes = sorted(set(s for i in self.net_imports if i.startswith(prefix) and '.' not in (s := i[len(prefix):])))
                import_str_list.append(f'from {base} import {", ".join(classes)}')
            net_imports = '\n'.join(import_str_list)
            net_imports = f'\n\n{net_imports}'
        
        var_types = ''
        if len(self.var_types) > 0:
            var_types_list = sorted(self.var_types.values(), key=lambda t: t.name)
            var_types = '\n'.join(t.print() for t in var_types_list)
            var_types = f'\n\n{var_types}'
        
        sys_types = ''
        if len(self.sys_types) > 0:
            sys_types_list = sorted(self.sys_types.values(), key=lambda t: t.name)
            sys_types = '\n'.join(t.print() for t in sys_types_list)
            sys_types = f'\n\n{sys_types}'
        
        special_types = ''
        if len(self.special_types) > 0:
            special_types_list = sorted(self.special_types.values(), key=lambda t: t.name)
            special_types = '\n\n'.join(t.print() for t in special_types_list)
            special_types = f'\n\n\n{special_types}\n'
        
        classes = '# No Classes'
        classes_sorted = sorted(self.classes.keys())
        if len(classes_sorted) > 0:
            classes = '\n\n\n'.join(i.print() for class_name in classes_sorted for i in self.classes[class_name])
            classes = f'# ---------- Classes ---------- #\n\n{classes}\n'
        
        structs = '# No Structs'
        structs_sorted = sorted(self.structs.keys())
        if len(structs_sorted) > 0:
            structs = '\n\n\n'.join(i.print() for struct_name in structs_sorted for i in self.structs[struct_name])
            structs = f'# ---------- Structs ---------- #\n\n{structs}\n'
        
        interfaces = '# No Interfaces'
        interfaces_sorted = sorted(self.interfaces.keys())
        if len(interfaces_sorted) > 0:
            interfaces = '\n\n\n'.join(i.print() for interface_name in interfaces_sorted for i in self.interfaces[interface_name])
            interfaces = f'# ---------- Interfaces ---------- #\n\n{interfaces}\n'
        
        enums = '# No Enums'
        enums_sorted = sorted(self.enums.keys())
        if len(enums_sorted) > 0:
            enums = '\n\n\n'.join(i.print() for enum_name in enums_sorted for i in self.enums[enum_name])
            enums = f'# ---------- Enums ---------- #\n\n{enums}\n'
        
        delegates = '# No Enums'
        delegates_sorted = sorted(self.delegates.keys())
        if len(self.delegates) > 0:
            delegates = '\n\n'.join(i.print() for delegate_name in delegates_sorted for i in self.delegates[delegate_name])
            delegates = f'# ---------- Delegates ---------- #\n\n{delegates}\n'
        
        all_list = []
        all_list.extend(classes_sorted)
        all_list.extend(structs_sorted)
        all_list.extend(interfaces_sorted)
        all_list.extend(enums_sorted)
        all_list.extend(delegates_sorted)
        all_str = ''
        if len(all_list) > 0:
            all_str = '\n'.join(f'    {a},' for a in all_list)
            all_str = f'\n{all_str}\n'
        
        return '\n'.join([
            f'from __future__ import annotations{py_imports}{net_imports}',
            f'',
            f'# ---------- Types ---------- #{var_types}{sys_types}{special_types}',
            f'',
            f'{classes}',
            f'',
            f'{structs}',
            f'',
            f'{interfaces}',
            f'',
            f'{enums}',
            f'',
            f'{delegates}',
            f'',
            f'__all__ = [{all_str}]',
            f'',
        ])


@dataclass
class Class(Member):
    """
    [@overload]
    class CLASS_NAME(SUPER_TYPE[, ', '.join(INTERFACES)]):
        CLASS_DOC_STRING
        
        # ---------- Fields ---------- #
        
        FIELDS
        
        # ---------- Constructors ---------- #
        
        CONSTRUCTORS
        
        # ---------- Properties ---------- #
        
        PROPERTIES
        
        # ---------- Methods ---------- #
        
        METHODS
        
        # ---------- Events ---------- #
        
        EVENTS
        
        # ---------- Sub Classes ---------- #
        
        SUB_CLASSES
    """
    
    name: str
    abstract: bool = field(default=False, repr=False)
    type_args: List[VarType] = field(default_factory=list, repr=False)
    super_type: Optional[TypeBase] = field(default=None, repr=False)
    interfaces: List[TypeBase] = field(default_factory=list, repr=False)
    fields: List[Property] = field(default_factory=list, repr=False)
    constructors: List[Constructor] = field(default_factory=list, repr=False)
    properties: List[Property] = field(default_factory=list, repr=False)
    methods: List[Method] = field(default_factory=list, repr=False)
    events: List[Event] = field(default_factory=list, repr=False)
    sub_classes: List[Class] = field(default_factory=list, repr=False)
    sub_structs: List[Class] = field(default_factory=list, repr=False)
    sub_interfaces: List[Interface] = field(default_factory=list, repr=False)
    sub_enums: List[Enum] = field(default_factory=list, repr=False)
    doc_string: str = field(default='', repr=False)
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        
        imports = []
        if len(self.type_args) > 0:
            args = ', '.join(str(a) for a in self.type_args)
            if self.abstract:
                imports.append(f'Prototype[{args}]')
            else:
                imports.append(f'Generic[{args}]')
        elif self.abstract:
            imports.append('ABC')
        
        if self.super_type is not None:
            imports.append(str(self.super_type))
        
        imports.extend(str(i) for i in self.interfaces)
        
        doc_string = ''
        if self.doc_string != '' or (
                len(self.fields) == 0 and
                len(self.constructors) == 0 and
                len(self.properties) == 0 and
                len(self.methods) == 0 and
                len(self.events) == 0 and
                len(self.sub_classes) == 0 and
                len(self.sub_structs) == 0 and
                len(self.sub_interfaces) == 0 and
                len(self.sub_enums) == 0
        ):
            doc_string = f'\n{_indent}    """{self.doc_string}"""\n{_indent}    '
        
        fields = '# No Fields'
        if len(self.fields) > 0:
            fields = f'\n{_indent}    \n'.join(i.print(indent + 4) for i in self.fields)
            fields = f'# ---------- Fields ---------- #\n{_indent}    \n{fields}'
        
        constructors = '# No Constructors'
        if len(self.constructors) > 0:
            constructors = f'\n{_indent}    \n'.join(i.print(indent + 4) for i in self.constructors)
            constructors = f'# ---------- Constructors ---------- #\n{_indent}    \n{constructors}'
        
        properties = '# No Properties'
        if len(self.properties) > 0:
            properties = f'\n{_indent}    \n'.join(i.print(indent + 4) for i in self.properties)
            properties = f'# ---------- Properties ---------- #\n{_indent}    \n{properties}'
        
        methods = '# No Methods'
        if len(self.methods) > 0:
            methods = f'\n{_indent}    \n'.join(i.print(indent + 4) for i in self.methods)
            methods = f'# ---------- Methods ---------- #\n{_indent}    \n{methods}'
        
        events = '# No Events'
        if len(self.events) > 0:
            events = f'\n{_indent}    \n'.join(i.print(indent + 4) for i in self.events)
            events = f'# ---------- Events ---------- #\n{_indent}    \n{events}'
        
        sub_classes = '# No Classes'
        if len(self.sub_classes) > 0:
            sub_classes = f'\n{_indent}    \n'.join(i.print(indent + 4) for i in self.sub_classes)
            sub_classes = f'# ---------- Sub Classes ---------- #\n{_indent}    \n{sub_classes}'
        
        sub_structs = '# No Structs'
        if len(self.sub_structs) > 0:
            sub_structs = f'\n{_indent}    \n'.join(i.print(indent + 4) for i in self.sub_structs)
            sub_structs = f'# ---------- Sub Structs ---------- #\n{_indent}    \n{sub_structs}'
        
        sub_interfaces = '# No Interfaces'
        if len(self.sub_interfaces) > 0:
            sub_interfaces = f'\n{_indent}    \n'.join(i.print(indent + 4) for i in self.sub_interfaces)
            sub_interfaces = f'# ---------- Sub Interfaces ---------- #\n{_indent}    \n{sub_interfaces}'
        
        sub_enums = '# No Enums'
        if len(self.sub_enums) > 0:
            sub_enums = f'\n{_indent}    \n'.join(i.print(indent + 4) for i in self.sub_enums)
            sub_enums = f'# ---------- No Enums ---------- #\n{_indent}    \n{sub_enums}'
        
        return '\n'.join([
            f'{_indent}class {self.name}({", ".join(imports)}):{doc_string}',
            f'{_indent}    {fields}',
            f'{_indent}    ',
            f'{_indent}    {constructors}',
            f'{_indent}    ',
            f'{_indent}    {properties}',
            f'{_indent}    ',
            f'{_indent}    {methods}',
            f'{_indent}    ',
            f'{_indent}    {events}',
            f'{_indent}    ',
            f'{_indent}    {sub_classes}',
            f'{_indent}    ',
            f'{_indent}    {sub_structs}',
            f'{_indent}    ',
            f'{_indent}    {sub_interfaces}',
            f'{_indent}    ',
            f'{_indent}    {sub_enums}',
        ])


@dataclass
class Interface(Member):
    """
    class NAME(Protocol{[TYPE_ARGS]}{, BASES}):
        DOC_STRING
        
        # ---------- Properties ---------- #
        
        PROPERTIES
        
        # ---------- Methods ---------- #
        
        METHODS
        
        # ---------- Events ---------- #
        
        EVENTS
    """
    name: str
    type_args: List[VarType] = field(default_factory=list, repr=False)
    bases: List[TypeBase] = field(default_factory=list, repr=False)
    properties: List[Property] = field(default_factory=list, repr=False)
    methods: List[Method] = field(default_factory=list, repr=False)
    events: List[Event] = field(default_factory=list, repr=False)
    doc_string: str = field(default='', repr=False)
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        
        type_args = ''
        if len(self.type_args) > 0:
            type_args = f'[{", ".join(str(t) for t in self.type_args)}]'
        
        super_types = ''
        if len(self.bases) > 0:
            super_types = f', '.join(str(b) for b in self.bases)
            super_types = f', {super_types}'
        
        doc_string = ''
        if self.doc_string != '':
            doc_string = f'\n{_indent}    """{self.doc_string}"""\n{_indent}    '
        
        properties = f'# No Properties'
        if len(self.properties) > 0:
            properties = f'\n{_indent}    \n'.join(p.print(indent + 4) for p in self.properties)
            properties = f'# ---------- Properties ---------- #\n{_indent}    \n{properties}'
        
        methods = f'# No Methods'
        if len(self.methods) > 0:
            methods = f'\n{_indent}    \n'.join(m.print(indent + 4) for m in self.methods)
            methods = f'# ---------- Methods ---------- #\n{_indent}    \n{methods}'
        
        events = f'# No Events'
        if len(self.events) > 0:
            events = f'\n{_indent}    \n'.join(e.print(indent + 4) for e in self.events)
            events = f'# ---------- Events ---------- #\n{_indent}    \n{events}'
        
        return '\n'.join([
            f'{_indent}class {self.name}(Protocol{type_args}{super_types}):{doc_string}',
            f'{_indent}    {properties}',
            f'{_indent}    ',
            f'{_indent}    {methods}',
            f'{_indent}    ',
            f'{_indent}    {events}',
        ])


@dataclass
class Enum(Member):
    """
    class NAME(Enum):
        DOC_STRING
        
        FIELDS
    """
    name: str
    fields: List[EnumField] = field(default_factory=list, repr=False)
    doc_string: str = field(default='', repr=False)
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        
        doc_str = ''
        if self.doc_string != '':
            doc_str = f'\n{_indent}    """{self.doc_string}"""\n{_indent}    '
        
        fields = ''
        if len(self.fields) > 0:
            previous_doc = False
            for field in self.fields:
                if previous_doc:
                    fields += f'\n{_indent}    '
                fields += f'\n{field.print(indent + 4)}'
                previous_doc = field.doc_string != ''
        
        return '\n'.join([
            f'{_indent}class {self.name}(Enum):{doc_str}{fields}',
        ])


@dataclass
class Delegate(Member):
    """
    NAME = Callable[[TYPES], RETURN_TYPE]
    DOC_STRING
    """
    
    name: str
    input_types: Tuple[TypeBase, ...]
    return_type: Optional[TypeBase] = None
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent

        input_types = ', '.join(str(t) for t in self.input_types)
        
        return_type = 'None'
        if self.doc_string is not None:
            return_type = str(self.return_type)
        
        doc_string = ''
        if self.doc_string != '':
            doc_string = f'\n{_indent}"""{doc_string}"""'
        
        return '\n'.join([
            f'{self.name} = Callable[[{input_types}], {return_type}]{doc_string}',
        ])


@dataclass
class Field(Member):
    """
    [#]FIELD_NAME: Final[FIELD_TYPE] = ...
    FIELD_DOC_STRING
    """
    
    name: str
    type: TypeBase
    final: bool = False
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        
        type = str(self.type)
        if self.final:
            type = f'Final[{type}]'
        
        doc_str = ''
        if self.doc_string != '':
            doc_str = f'\n{_indent}"""{self.doc_string}"""'
        
        return '\n'.join([
            f'{_indent}{self.name}: {type} = ...{doc_str}',
        ])


@dataclass
class EnumField(Member):
    """
    [#]NAME: TYPE = VALUE
    DOC_STRING
    """
    
    name: str
    type: TypeBase
    value: str
    doc_string: str
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        
        name = self.name
        if self._is_name_invalid(name):
            name = f'#{name}'
        
        doc_str = ''
        if self.doc_string != '':
            doc_str = f'\n{_indent}"""{self.doc_string}"""'
        
        return '\n'.join([
            f'{_indent}{name}: {self.type} = {self.value}{doc_str}',
        ])
    
    @staticmethod
    def _is_name_invalid(name: str) -> bool:
        return name in [
            'None'
        ]


@dataclass
class Constructor(Member):
    """
    [@overload]
    def __init__(self[, ', '.join((PARAMETERS)]):
        DOC_STRING
    """
    parameters: List[Parameter] = field(default_factory=list)
    overload: bool = field(default=False, repr=True)
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        overload = f'{_indent}@overload\n' if self.overload else ''
        
        args = ''
        if len(self.parameters) > 0:
            args = ', ' + ', '.join(map(lambda p: p.print(), self.parameters))
        
        doc_str = ' ...'
        if self.doc_string != '':
            doc_str = self.doc_string
            if len(self.parameters) > 0:
                arg_doc = f'\n{_indent}    '.join(f":param {arg.name}: {arg.doc_string}" for arg in self.parameters)
                if self.doc_string != '':
                    doc_str += f'\n{_indent}    '
                doc_str += f'\n{_indent}    {arg_doc}\n{_indent}    '
            doc_str = f'\n{_indent}    """{doc_str}"""'
        
        return f'{overload}{_indent}def __init__(self{args}):{doc_str}'


@dataclass
class Property(Member):
    """
    [@staticmethod]
    @property
    def PROPERTY_NAME([self]) -> PROPERTY_RETURN_TYPE:
        PROPERTY_DOC_STRING
    """
    name: str
    type: TypeBase
    setter: bool = False
    static: bool = False
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        static = f'{_indent}@staticmethod\n' if self.static else ''
        
        property = f'@{self.name}.setter' if self.setter else '@property'
        
        args = '' if self.static else 'self'
        if self.setter:
            if not self.static:
                args += ', '
            args += f'value: {self.type}'
        
        _return = 'None' if self.setter else str(self.type)
        
        doc_str = ' ...'
        if self.doc_string != '':
            doc_str = f'\n{_indent}    """{self.doc_string}"""'
        
        return '\n'.join([
            f'{static}{_indent}{property}',
            f'{_indent}def {self.name}({args}) -> {_return}:{doc_str}',
        ])


@dataclass
class Method(Member):
    """
    [@staticmethod]
    [@overload]
    def METHOD_NAME([self[: METHOD_SELF_TYPE]][, ][', '.join((PARAMETERS)]) -> PROPERTY_RETURN_TYPE:
        METHOD_DOC_STRING
    """
    name: str
    parameters: Tuple[Parameter, ...]
    return_types: Tuple[TypeBase, ...]
    static: bool = False
    overload: bool = False
    self_type: Optional[RegularType] = None
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        static = f'{_indent}@staticmethod\n' if self.static else ''
        overload = f'{_indent}@overload\n' if self.overload else ''
        self_str = f'self{"" if self.self_type is None else (": " + self.self_type.print())}' + (', ' if self.parameters else '')
        params = f'{"" if self.static else self_str}' + (f'{", ".join(map(lambda i: i.print(), self.parameters))}' if self.parameters else '')
        
        return_str = ''
        if len(self.return_types) > 0:
            if len(self.return_types) == 1:
                return_str = f' -> {self.return_types[0]}'
            else:
                return_str = f' -> Tuple[{", ".join(str(t) for t in self.return_types)}]'
        
        doc_str = ' ...'
        if self.doc_string != '':
            doc_str = self.doc_string
            if len(self.parameters) > 0:
                arg_doc = f'\n{_indent}    '.join(f":param {arg.name}: {arg.doc_string}" for arg in self.parameters)
                if self.doc_string != '':
                    doc_str += f'\n{_indent}    '
                doc_str += f'\n{_indent}    {arg_doc}\n{_indent}    '
            doc_str = f'\n{_indent}    """{doc_str}"""'
        
        return '\n'.join([
            f'{static}{overload}{_indent}def {self.name}({params}){return_str}:{doc_str}',
        ])


@dataclass
class Event(Member):
    """
    NAME: EventType[EVENT_TYPE] = ...
    DOC_STRING
    """
    
    name: str
    type: TypeBase
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        
        doc_str = ''
        if self.doc_string != '':
            doc_str = f'\n{_indent}"""{self.doc_string}"""'
        
        return '\n'.join([
            f'{_indent}{self.name}: EventType[{self.type}] = ...{doc_str}',
        ])


@dataclass
class Parameter(Member):
    """ARGUMENT_NAME: ARGUMENT_TYPE[ = DEFAULT_VALUE]"""
    
    name: str
    type: TypeBase
    default: Optional[str] = None
    is_in: bool = False
    is_out: bool = False
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        return f'{self.name}: {self.type}{f" = {self.default}" if self.default else ""}'


@dataclass
class TypeBase(Member, ABC):
    pass


@dataclass
class RegularType(TypeBase):
    """TYPE_NAME[[INNER]]"""
    
    base: Union[str, SystemType]
    inner: Tuple[TypeBase, ...] = field(default_factory=tuple)
    
    def __str__(self) -> str:
        return self.print()
    
    def print(self, indent: int = 0) -> str:
        if isinstance(self.base, str):
            name = self.base
        else:
            name = self.base.name
        inner = ''
        if len(self.inner) > 0:
            if len(self.inner) == 1:
                inner = f'[{self.inner[0]}]'
            else:
                inner = f'[{", ".join(str(i) for i in self.inner)}]'
        return name + inner


@dataclass
class SystemType(TypeBase):
    """
    BooleanType = Union[bool, System.Boolean]
    ByteType = Union[int, System.Byte]
    SByteType = Union[int, System.SByte]
    CharType = Union[str, System.Char]
    DecimalType = Union[float, System.Decimal]
    DoubleType = Union[float, System.Double]
    FloatType = Union[float, System.Single]
    SingleType = Union[float, System.Single]
    IntType = Union[int, System.Int32]
    UIntType = Union[int, System.UInt32]
    NIntType = Union[int, System.IntPtr]
    NUIntType = Union[int, System.UIntPtr]
    LongType = Union[int, System.Int64]
    ULongType = Union[int, System.UInt64]
    ShortType = Union[int, System.Int16]
    UShortType = Union[int, System.UInt16]
    StringType = Union[str, System.String]
    ObjectType = Union[object, System.Object]
    TypeType = Union[type, System.Type]
    NullableType = Union[Nullable, Optional]
    VoidType = Optional[Void]
    ArrayType = Union[list, Array]
    Obsolete = NoReturn
    """
    
    name: str
    value: str
    
    def __str__(self) -> str:
        return self.name
    
    def print(self, indent: int = 0) -> str:
        return f'{self.name} = {self.value}'


@dataclass
class SpecialType(TypeBase, ABC):
    name: str
    
    def __str__(self) -> str:
        return self.name


@dataclass
class EventType(SpecialType):
    def __init__(self):
        super().__init__('EventType')
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        return '\n'.join([
            f'{_indent}class EventType(Generic[T]):',
            f'{_indent}    def __iadd__(self, other: T): ...',
            f'{_indent}    ',
            f'{_indent}    def __isub__(self, other: T): ...',
        ])


@dataclass
class VarType(TypeBase):
    """NAME = TypeVar('NAME'[, bound=BOUND_TYPE])"""
    
    name: str
    bounds: Tuple[TypeBase, ...] = field(default_factory=tuple)
    
    def __str__(self) -> str:
        return self.name
    
    def print(self, indent: int = 0) -> str:
        bound = ''
        if len(self.bounds) > 0:
            if len(self.bounds) == 1:
                bound = f', bound={self.bounds[0]}'
            else:
                bound = f', bound=Union[{", ".join(str(b) for b in self.bounds)}]'
        return f'{self.name} = TypeVar(\'{self.name}\'{bound})'


if __name__ == '__main__':
    boolean_type = SystemType('BooleanType', 'Union[bool, Boolean]')
    sbyte_type = SystemType('SByteType', 'Union[int, SByte]')
    short_type = SystemType('ShortType', 'Union[int, Int16]')
    int_type = SystemType('IntType', 'Union[int, Int32]')
    long_type = SystemType('LongType', 'Union[int, Int64]')
    byte_type = SystemType('ByteType', 'Union[int, Byte]')
    ushort_type = SystemType('UShortType', 'Union[int, UInt16]')
    uint_type = SystemType('UIntType', 'Union[int, UInt32]')
    ulong_type = SystemType('ULongType', 'Union[int, UInt64]')
    nint_type = SystemType('NIntType', 'Union[int, IntPtr]')
    nuint_type = SystemType('NUIntType', 'Union[int, UIntPtr]')
    float_type = SystemType('FloatType', 'Union[float, Single]')
    double_type = SystemType('DoubleType', 'Union[float, Double]')
    decimal_type = SystemType('DecimalType', 'Union[float, Decimal]')
    char_type = SystemType('CharType', 'Union[str, Char]')
    string_type = SystemType('StringType', 'Union[str, String]')
    object_type = SystemType('ObjectType', 'Union[object, Object]')
    type_type = SystemType('TypeType', 'Union[type, Type]')
    void_type = SystemType('VoidType', 'Union[None, Void]')
    nullable_type = SystemType('NullableType', 'Union[Optional, Nullable]')
    array_type = SystemType('ArrayType', 'Union[list, Array]')
    obsolete_type = SystemType('Obsolete', 'NoReturn')
    
    # print(boolean_type.print(0))
    null_int_type = RegularType(nullable_type, (int_type,))
    array_null_int_type = RegularType(array_type, (null_int_type,))
    # print('null_int_type', null_int_type.print())
    # print('array_null_int_type', array_null_int_type.print())
    
    index1 = Parameter('index1', int_type)
    index2 = Parameter('index2', array_null_int_type)
    # print(index1.print(0))
    # print(index2.print(0))
    
    f = Field('MaxValue', array_null_int_type, doc_string='Test Field')
    # print(f.print(4))
    
    c = Constructor((index1, index2), doc_string="Test Constructor", overload=True, no_return=False)
    # print(c.print(4))
    
    p = Property('Count', array_null_int_type, doc_string="Test Property", static=True, setter=True)
    # print(p.print(4))
    
    m = Method('do_things', (index1, index2), (void_type,), doc_string='Test Method', overload=True)
    # print(m.print(4))
    
    d = Delegate(name='Name',
                 input_types=tuple([double_type]),
                 return_type=void_type,
                 doc_string='')
    
    inner_class = Class(name='Inner',
                        abstract=False,
                        type_args=[],
                        super_type=None,
                        interfaces=[],
                        fields=[],
                        constructors=[c],
                        properties=[p],
                        methods=[m],
                        events=[],
                        sub_classes=[],
                        sub_structs=[],
                        sub_interfaces=[],
                        sub_enums=[],
                        doc_string='')
    
    clazz = Class(name='Class',
                  abstract=False,
                  type_args=[],
                  super_type=None,
                  interfaces=[],
                  fields=[],
                  constructors=[c],
                  properties=[p],
                  methods=[m],
                  events=[],
                  sub_classes=[inner_class],
                  sub_structs=[],
                  sub_interfaces=[],
                  sub_enums=[],
                  doc_string='')
    
    print(clazz.print(0))
