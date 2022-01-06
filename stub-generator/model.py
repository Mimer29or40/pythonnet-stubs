from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, Tuple, List, Dict, Union, Set


# TODO - Methods - Handle out


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
    classes: Dict[str, List[str]] = field(default_factory=dict, repr=False)
    structs: Dict[str, List[str]] = field(default_factory=dict, repr=False)
    interfaces: Dict[str, Interface] = field(default_factory=dict, repr=False)
    enums: Dict[str, List[str]] = field(default_factory=dict, repr=False)
    delegates: Dict[str, List[str]] = field(default_factory=dict, repr=False)
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        py_imports = ''
        if len(self.py_imports) > 0:
            bases = sorted(set(i.split('.')[0] for i in self.py_imports))
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
        
        classes = ''
        classes_sorted = sorted(self.classes.values(), key=lambda c: c.name)
        
        structs = ''
        structs_sorted = sorted(self.structs.values(), key=lambda s: s.name)

        interfaces = ''
        interfaces_sorted = sorted(self.interfaces.values(), key=lambda i: i.name)
        if len(interfaces_sorted) > 0:
            interfaces = '\n\n\n'.join(i.print() for i in interfaces_sorted)
            interfaces = f'\n\n{interfaces}\n'

        enums = ''
        enums_sorted = sorted(self.enums.values(), key=lambda e: e.name)

        delegates = ''
        delegates_sorted = sorted(self.delegates.values(), key=lambda d: d.name)
        
        all_list = []
        all_list += [c.name for c in classes_sorted]
        all_list += [s.name for s in structs_sorted]
        all_list += [i.name for i in interfaces_sorted]
        all_list += [e.name for e in enums_sorted]
        all_list += [d.name for d in delegates_sorted]
        all_str = ''
        if len(all_list) > 0:
            all_str = '\n'.join(f'    {a},' for a in all_list)
            all_str = f'\n{all_str}\n'

        return '\n'.join([
            f'from __future__ import annotations',
            f'',
            f'# ---------- Python Imports ---------- #{py_imports}{net_imports}',
            f'',
            f'# ---------- Types ---------- #{var_types}{sys_types}{special_types}',
            f'',
            f'# ---------- Classes ---------- #{classes}',
            f'',
            f'# ---------- Structs ---------- #{structs}',
            f'',
            f'# ---------- Interfaces ---------- #{interfaces}',
            f'',
            f'# ---------- Enums ---------- #{enums}',
            f'',
            f'# ---------- Delegates ---------- #{delegates}',
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
        
        # ---------- Sub Classes ---------- #
        
        SUB_CLASSES
    """
    
    name: str
    super_type: Optional[Type]
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        pass


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
    type_args: Tuple[VarType, ...] = field(default_factory=tuple, repr=False)
    bases: Tuple[TypeBase, ...] = field(default_factory=tuple, repr=False)
    properties: Tuple[Property, ...] = field(default_factory=tuple, repr=False)
    methods: Tuple[Method, ...] = field(default_factory=tuple, repr=False)
    events: Tuple[Event, ...] = field(default_factory=tuple, repr=False)
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        
        type_args = ''
        if len(self.type_args) > 0:
            type_args = f'[{", ".join(t.resolve() for t in self.type_args)}]'
        
        bases = ''
        if len(self.bases) > 0:
            bases = f', '.join(b.resolve() for b in self.bases)
            bases = f', {bases}'
        
        properties = ''
        if len(self.properties) > 0:
            properties = f'\n{_indent}    \n{_indent}'.join(p.print(indent + 4) for p in self.properties)
            properties = f'\n{_indent}    \n{_indent}{properties}'
        
        methods = ''
        if len(self.methods) > 0:
            methods = f'\n{_indent}    \n{_indent}'.join(m.print(indent + 4) for m in self.methods)
            methods = f'\n{_indent}    \n{_indent}{methods}'
        
        events = ''
        if len(self.events) > 0:
            events = f'\n{_indent}    \n{_indent}'.join(e.print(indent + 4) for e in self.events)
            events = f'\n{_indent}    \n{_indent}{events}'
        
        return '\n'.join([
            f'{_indent}class {self.name}(Protocol{type_args}{bases}):',
            f'{_indent}    """{self.doc_string}"""',
            f'{_indent}    ',
            f'{_indent}    # ---------- Properties ---------- #{properties}',
            f'{_indent}    ',
            f'{_indent}    # ---------- Methods ---------- #{methods}',
            f'{_indent}    ',
            f'{_indent}    # ---------- Events ---------- #{events}',
        ])


@dataclass
class Field(Member):
    """
    [#]FIELD_NAME: FIELD_TYPE = ...
    FIELD_DOC_STRING
    """
    
    name: str
    type: TypeBase
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        return '\n'.join([
            f'{_indent}{self.name}: {self.type.resolve()} = ...',
            f'{_indent}"""{self.doc_string}"""',
        ])


@dataclass
class Constructor(Member):
    """
    [@overload]
    def __init__(self[, ', '.join((PARAMETERS)])[ -> NoReturn]:
        DOC_STRING
    """
    parameters: Tuple[Parameter, ...] = field(default_factory=tuple)
    overload: bool = False
    no_return: bool = False
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        _indent = ' ' * indent
        overload = f'{_indent}@overload\n' if self.overload else ''
        
        args = ''
        if len(self.parameters) > 0:
            args = ', ' + ', '.join(map(lambda p: p.print(), self.parameters))
        
        return_str = ' -> NoReturn' if self.no_return else ''
        
        doc_str = ''
        if self.doc_string != '':
            doc_str = self.doc_string
        if len(self.parameters) > 0:
            arg_doc = f'\n{_indent}    '.join(f":param {arg.name}: {arg.doc_string}" for arg in self.parameters)
            if self.doc_string != '':
                doc_str += f'\n{_indent}    '
            doc_str += f'\n{_indent}    {arg_doc}\n{_indent}    '
        
        return '\n'.join([
            f'{overload}{_indent}def __init__(self{args}){return_str}:',
            f'{_indent}    """{doc_str}"""',
        ])


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
            args += f'value: {self.type.resolve()}'
        
        _return = 'None' if self.setter else self.type.resolve()
        
        doc_str = ''
        if self.doc_string != '':
            doc_str = self.doc_string
        
        return '\n'.join([
            f'{static}{_indent}{property}',
            f'{_indent}def {self.name}({args}) -> {_return}:',
            f'{_indent}    """{doc_str}"""',
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
    parameters: Tuple[Parameter, ...] = field(default_factory=tuple)
    return_types: Tuple[TypeBase, ...] = field(default_factory=tuple)
    static: bool = False
    overload: bool = False
    self_type: Type = None
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
                return_str = f' -> {self.return_types[0].resolve()}'
            else:
                return_str = f' -> Tuple[{", ".join(t.resolve() for t in self.return_types)}]'
        
        doc_str = ''
        if self.doc_string != '':
            doc_str = self.doc_string
        if len(self.parameters) > 0:
            arg_doc = f'\n{_indent}    '.join(f":param {arg.name}: {arg.doc_string}" for arg in self.parameters)
            if self.doc_string != '':
                doc_str += f'\n{_indent}    '
            doc_str += f'\n{_indent}    {arg_doc}\n{_indent}    '
        
        return '\n'.join([
            f'{static}{overload}{_indent}def {self.name}({params}){return_str}:',
            f'{_indent}    """{doc_str}"""',
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
        
        return '\n'.join([
            f'{_indent}{self.name}: EventType[{self.type.resolve()}] = ...',
            f'{_indent}"""{self.doc_string}"""',
        ])


@dataclass
class Parameter(Member):
    """[in/out ]ARGUMENT_NAME: ARGUMENT_TYPE[ = DEFAULT_VALUE]"""
    
    name: str
    type: TypeBase
    default: str = None
    is_in: bool = False
    is_out: bool = False
    doc_string: str = ''
    
    def print(self, indent: int = 0) -> str:
        return f'{self.name}: {self.type.resolve()}{f" = {self.default}" if self.default else ""}'


@dataclass
class TypeBase(Member):
    @abstractmethod
    def resolve(self) -> str: ...


@dataclass
class Type(TypeBase):
    """TYPE_NAME[[INNER]]"""
    
    base: Union[str, SystemType]
    inner: Tuple[TypeBase, ...] = field(default_factory=tuple)
    
    def resolve(self) -> str:
        return self.print()
    
    def print(self, indent: int = 0) -> str:
        if isinstance(self.base, str):
            name = self.base
        else:
            name = self.base.name
        inner = ''
        if len(self.inner) > 0:
            if len(self.inner) == 1:
                inner = f'[{self.inner[0].resolve()}]'
            else:
                inner = f'[{", ".join(i.resolve() for i in self.inner)}]'
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
    
    def resolve(self) -> str:
        return self.name
    
    def print(self, indent: int = 0) -> str:
        return f'{self.name} = {self.value}'


@dataclass
class SpecialType(TypeBase, ABC):
    name: str

    def resolve(self) -> str:
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
    
    def resolve(self) -> str:
        return self.name
    
    def print(self, indent: int = 0) -> str:
        bound = ''
        if len(self.bounds) > 0:
            if len(self.bounds) == 1:
                bound = f', bound={self.bounds[0].resolve()}'
            else:
                bound = f', bound=Union[{", ".join(b.resolve() for b in self.bounds)}]'
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
    
    print(boolean_type.print(0))
    null_int_type = Type(nullable_type, (int_type,))
    array_null_int_type = Type(array_type, (null_int_type,))
    print('null_int_type', null_int_type.print())
    print('array_null_int_type', array_null_int_type.print())
    
    index1 = Parameter('index1', int_type)
    index2 = Parameter('index2', array_null_int_type)
    print(index1.print(0))
    print(index2.print(0))
    
    f = Field('MaxValue', array_null_int_type, doc_string='Test Field')
    print(f.print(0))
    
    c = Constructor((index1, index2), doc_string="Test Constructor", overload=True, no_return=False)
    print(c.print(0))
    
    p = Property('Count', array_null_int_type, doc_string="Test Property", static=True)
    print(p.print(0))
    
    p = Property('Count', array_null_int_type, doc_string="Test Property", static=True, setter=True)
    print(p.print(0))
    
    m = Method('do_things', (index1, index2), (void_type,), doc_string='Test Method', overload=True)
    print(m.print(0))
