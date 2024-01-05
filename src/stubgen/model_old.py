from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

from .util import reserved_python_names


class Namespace:
    def __init__(self, name: str):
        self.name: str = name
        self.py_imports: Set[str] = set()
        self.net_imports: Set[str] = set()
        self.var_types: Dict[str, VarType] = {}
        self.sys_types: Dict[str, SystemType] = {}
        self.special_types: Dict[str, SpecialType] = {}
        self.classes: Dict[str, Set[Class]] = defaultdict(set)
        self.structs: Dict[str, Set[Class]] = defaultdict(set)
        self.interfaces: Dict[str, Set[Interface]] = defaultdict(set)
        self.enums: Dict[str, Set[Enum]] = defaultdict(set)
        self.delegates: Dict[str, Set[Delegate]] = defaultdict(set)
        self.doc_string: str = ""

    def to_lines(self) -> List[str]:
        lines: List[str] = ["from __future__ import annotations"]

        classes_sorted = sorted(self.classes.keys())
        structs_sorted = sorted(self.structs.keys())
        interfaces_sorted = sorted(self.interfaces.keys())
        enums_sorted = sorted(self.enums.keys())
        delegates_sorted = sorted(self.delegates.keys())

        all_list = []
        all_list.extend(classes_sorted)
        all_list.extend(structs_sorted)
        all_list.extend(interfaces_sorted)
        all_list.extend(enums_sorted)
        all_list.extend(delegates_sorted)

        if len(self.py_imports) > 0:
            bases = sorted(set(".".join(i.split(".")[:-1]) for i in self.py_imports))
            import_str_list = []
            for base in bases:
                prefix = f"{base}."
                classes = sorted(
                    set(i[len(prefix) :] for i in self.py_imports if i.startswith(prefix))
                )
                import_str_list.append(f'from {base} import {", ".join(classes)}')
            if len(import_str_list) > 0:
                lines.extend(["", *import_str_list])

        if len(self.net_imports) > 0:
            bases = sorted(set(".".join(i.split(".")[:-1]) for i in self.net_imports))
            import_str_list = []
            for base in bases:
                if base == "":
                    continue
                prefix = f"{base}."
                classes = sorted(
                    set(
                        s
                        for i in self.net_imports
                        if i.startswith(prefix)
                        and "." not in (s := i[len(prefix) :])
                        and s not in all_list
                    )
                )
                if len(classes) == 0:
                    continue
                import_str_list.append(f'from {base} import {", ".join(classes)}')
            if len(import_str_list) > 0:
                lines.extend(["", *import_str_list])

        var_types_list = sorted(self.var_types.values(), key=lambda t: t.name)
        sys_types_list = sorted(self.sys_types.values(), key=lambda t: t.name)
        special_types_list = sorted(self.special_types.values(), key=lambda t: t.name)

        if len(var_types_list) > 0 or len(sys_types_list) > 0 or len(special_types_list) > 0:
            lines.extend(["", "# ---------- Types ---------- #"])

            if len(var_types_list) > 0:
                lines.append("")
                for t in var_types_list:
                    lines.extend(t.to_lines())

            if len(sys_types_list) > 0:
                lines.append("")
                for t in sys_types_list:
                    lines.extend(t.to_lines())

            if len(special_types_list) > 0:
                lines.append("")
                for t in special_types_list:
                    lines.extend(["", *t.to_lines(), ""])

        lines.append("")
        lines.append("")

        if len(classes_sorted) > 0:
            lines.extend(["# ---------- Classes ---------- #"])
            for class_name in classes_sorted:
                for i in sorted(self.classes[class_name], key=lambda c: str(c), reverse=True):
                    lines.extend(["", *i.to_lines(), ""])
        else:
            lines.append("# No Classes")

        lines.append("")

        if len(structs_sorted) > 0:
            lines.extend(["# ---------- Structs ---------- #"])
            for struct_name in structs_sorted:
                for i in sorted(self.structs[struct_name], key=lambda s: str(s), reverse=True):
                    lines.extend(["", *i.to_lines(), ""])
        else:
            lines.append("# No Structs")

        lines.append("")

        if len(interfaces_sorted) > 0:
            lines.extend(["# ---------- Interfaces ---------- #"])
            for interface_name in interfaces_sorted:
                for i in sorted(
                    self.interfaces[interface_name], key=lambda i: str(i), reverse=True
                ):
                    lines.extend(["", *i.to_lines(), ""])
        else:
            lines.append("# No Interfaces")

        lines.append("")

        if len(enums_sorted) > 0:
            lines.extend(["# ---------- Enums ---------- #"])
            for enum_name in enums_sorted:
                for i in sorted(self.enums[enum_name], key=lambda e: str(e), reverse=True):
                    lines.extend(["", *i.to_lines(), ""])
        else:
            lines.append("# No Enums")

        lines.append("")

        if len(self.delegates) > 0:
            lines.extend(["# ---------- Delegates ---------- #"])
            for delegate_name in delegates_sorted:
                for i in sorted(self.delegates[delegate_name], key=lambda d: str(d), reverse=True):
                    lines.extend(["", *i.to_lines()])
        else:
            lines.append("# No Delegates")

        lines.append("")

        if len(all_list) > 0:
            lines.extend(["__all__ = [", *(f"    {a}," for a in all_list), "]"])
        else:
            lines.append("__all__ = []")

        lines.append("")

        return lines


class Class:
    def __init__(self, name: str):
        self.name: str = name
        self.abstract: bool = False
        self.generic_args: List[VarType] = []
        self.super_type: Optional[BaseType] = None
        self.interfaces: List[BaseType] = []
        self.fields: List[Property] = []
        self.constructors: List[Constructor] = []
        self.properties: List[Property] = []
        self.methods: List[Method] = []
        self.events: List[Event] = []
        self.sub_classes: List[Class] = []
        self.sub_structs: List[Class] = []
        self.sub_interfaces: List[Interface] = []
        self.sub_enums: List[Enum] = []
        self.doc_string: str = ""

    def __repr__(self) -> str:
        imports = []
        if len(self.generic_args) > 0:
            args = ", ".join(str(a) for a in self.generic_args)
            if self.abstract:
                imports.append(f"Protocol[{args}]")
            else:
                imports.append(f"Generic[{args}]")
        elif self.abstract:
            imports.append("ABC")

        if self.super_type is not None:
            imports.append(str(self.super_type))

        imports.extend(str(i) for i in self.interfaces)

        import_str = f'({", ".join(imports)})' if len(imports) > 0 else ""

        return f"class {self.name}{import_str}:"

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        if isinstance(other, Class):
            return repr(self) == repr(other)
        return False

    def to_lines(self) -> List[str]:
        lines: List[str] = []

        imports = []
        if len(self.generic_args) > 0:
            args = ", ".join(str(a) for a in self.generic_args)
            if self.abstract:
                imports.append(f"Protocol[{args}]")
            else:
                imports.append(f"Generic[{args}]")
        elif self.abstract:
            imports.append("ABC")

        if self.super_type is not None:
            imports.append(str(self.super_type))

        imports.extend(str(i) for i in self.interfaces)

        import_str = f'({", ".join(imports)})' if len(imports) > 0 else ""

        lines.append(f"class {self.name}{import_str}:")

        if self.doc_string != "" or (
            len(self.fields) == 0
            and len(self.constructors) == 0
            and len(self.properties) == 0
            and len(self.methods) == 0
            and len(self.events) == 0
            and len(self.sub_classes) == 0
            and len(self.sub_structs) == 0
            and len(self.sub_interfaces) == 0
            and len(self.sub_enums) == 0
        ):
            lines.extend([f'    """{self.doc_string}"""', "    "])

        if len(self.fields) > 0:
            lines.append("    # ---------- Fields ---------- #")
            for field in self.fields:
                lines.extend(["    ", *(f"    {line}" for line in field.to_lines())])
        else:
            lines.append("    # No Fields")

        lines.append("    ")

        if len(self.constructors) > 0:
            lines.append("    # ---------- Constructors ---------- #")
            for constructor in self.constructors:
                lines.extend(["    ", *(f"    {line}" for line in constructor.to_lines())])
        else:
            lines.append("    # No Constructors")

        lines.append("    ")

        if len(self.properties) > 0:
            lines.append("    # ---------- Properties ---------- #")
            for property in self.properties:
                lines.extend(["    ", *(f"    {line}" for line in property.to_lines())])
        else:
            lines.append("    # No Properties")

        lines.append("    ")

        if len(self.methods) > 0:
            lines.append("    # ---------- Methods ---------- #")
            for method in self.methods:
                lines.extend(["    ", *(f"    {line}" for line in method.to_lines())])
        else:
            lines.append("    # No Methods")

        lines.append("    ")

        if len(self.events) > 0:
            lines.append("    # ---------- Events ---------- #")
            for event in self.events:
                lines.extend(["    ", *(f"    {line}" for line in event.to_lines())])
        else:
            lines.append("    # No Events")

        lines.append("    ")

        if len(self.sub_classes) > 0:
            lines.append("    ")
            lines.append("    # ---------- Sub Classes ---------- #")
            for clazz in self.sub_classes:
                lines.extend(["    ", *(f"    {line}" for line in clazz.to_lines()), "    "])
        else:
            lines.append("    # No Sub Classes")

        lines.append("    ")

        if len(self.sub_structs) > 0:
            lines.append("    # ---------- Sub Structs ---------- #")
            for struct in self.sub_structs:
                lines.extend(["    ", *(f"    {line}" for line in struct.to_lines()), "    "])
        else:
            lines.append("    # No Sub Structs")

        lines.append("    ")

        if len(self.sub_interfaces) > 0:
            lines.extend(["    # ---------- Sub Interfaces ---------- #"])
            for interface in self.sub_structs:
                lines.extend(["    ", *(f"    {line}" for line in interface.to_lines()), "    "])
        else:
            lines.extend(["    # No Sub Interfaces"])

        lines.append("    ")

        if len(self.sub_enums) > 0:
            lines.extend(["    # ---------- Sub Enums ---------- #"])
            for enum in self.sub_enums:
                lines.extend(["    ", *(f"    {line}" for line in enum.to_lines()), "    "])
        else:
            lines.append("    # No Sub Enums")

        return lines


class Interface:
    def __init__(self, name: str):
        self.name: str = name
        self.generic_args: List[VarType] = []
        self.super_classes: List[BaseType] = []
        self.properties: List[Property] = []
        self.methods: List[Method] = []
        self.events: List[Event] = []
        self.doc_string: str = ""

    def __repr__(self) -> str:
        type_args = ""
        if len(self.generic_args) > 0:
            type_args = f'[{", ".join(str(t) for t in self.generic_args)}]'

        super_types = ""
        if len(self.super_classes) > 0:
            super_types = f", ".join(str(b) for b in self.super_classes)
            super_types = f", {super_types}"

        return f"class {self.name}(Protocol{type_args}{super_types}):"

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        if isinstance(other, Interface):
            return repr(self) == repr(other)
        return False

    def to_lines(self) -> List[str]:
        lines: List[str] = []

        type_args = ""
        if len(self.generic_args) > 0:
            type_args = f'[{", ".join(str(t) for t in self.generic_args)}]'

        super_types = ""
        if len(self.super_classes) > 0:
            super_types = f", ".join(str(b) for b in self.super_classes)
            super_types = f", {super_types}"

        lines.append(f"class {self.name}(Protocol{type_args}{super_types}):")

        if self.doc_string != "" or (
            len(self.properties) == 0 and len(self.methods) == 0 and len(self.events) == 0
        ):
            lines.extend([f'    """{self.doc_string}"""', "    "])

        if len(self.properties) > 0:
            lines.extend(["    # ---------- Properties ---------- #"])
            for property in self.properties:
                lines.extend(["    ", *(f"    {line}" for line in property.to_lines())])
        else:
            lines.append("    # No Properties")

        lines.append("    ")

        if len(self.methods) > 0:
            lines.extend(["    # ---------- Methods ---------- #"])
            for method in self.methods:
                lines.extend(["    ", *(f"    {line}" for line in method.to_lines())])
        else:
            lines.append("    # No Methods")

        lines.append("    ")

        if len(self.events) > 0:
            lines.extend(["    # ---------- Events ---------- #"])
            for event in self.events:
                lines.extend(["    ", *(f"    {line}" for line in event.to_lines())])
        else:
            lines.append("    # No Events")

        return lines


class Enum:
    def __init__(self, name: str):
        self.name: str = name
        self.fields: List[EnumField] = []
        self.doc_string: str = ""

    def __repr__(self) -> str:
        return f"class {self.name}(Enum):"

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        if isinstance(other, Enum):
            return repr(self) == repr(other)
        return False

    def to_lines(self) -> List[str]:
        lines: List[str] = [f"class {self.name}(Enum):"]

        if self.doc_string != "" or len(self.fields) == 0:
            lines.extend([f'    """{self.doc_string}"""', "    "])

        if len(self.fields) > 0:
            previous_doc = False
            for field in self.fields:
                if previous_doc:
                    lines.append("    ")
                lines.extend(f"    {line}" for line in field.to_lines())
                previous_doc = field.doc_string != ""

        return lines


class Delegate:
    def __init__(self, name: str):
        self.name = name
        self.input_types: List[BaseType] = []
        self.return_type: Optional[BaseType] = None
        self.doc_string: str = ""

    def __repr__(self) -> str:
        input_types = ", ".join(str(t) for t in self.input_types)

        return_type = "None"
        if self.return_type is not None:
            return_type = str(self.return_type)

        return f"{self.name} = Callable[[{input_types}], {return_type}]"

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        if isinstance(other, Delegate):
            return repr(self) == repr(other)
        return False

    def to_lines(self) -> List[str]:
        lines: List[str] = []

        input_types = ", ".join(str(t) for t in self.input_types)

        return_type = "None"
        if self.return_type is not None:
            return_type = str(self.return_type)

        lines.append(f"{self.name} = Callable[[{input_types}], {return_type}]")

        if self.doc_string != "":
            lines.append(f'"""{self.doc_string}"""')

        return lines


@dataclass
class EnumField:
    name: str
    type: BaseType
    value: Any
    doc_string: str

    def to_lines(self) -> List[str]:
        lines: List[str] = []

        name = self.name
        if name in reserved_python_names:
            name = f"#{self.name}"

        # lines.append(f'{name}: {self.type} = {self.value}')
        lines.append(f"{name} = {self.value}")

        if self.doc_string != "":
            lines.append(f'"""{self.doc_string}"""')

        return lines


@dataclass
class Constructor:
    parameters: List[Parameter]
    overload: bool = False
    doc_string: str = ""

    def __str__(self) -> str:
        return f'__init__({", ".join(["self"] + list(map(str, self.parameters)))})'

    def to_lines(self) -> List[str]:
        lines: List[str] = []

        if self.overload:
            lines.append("@overload")

        lines.append(
            f'def __init__({", ".join(["self", *map(str, self.parameters)])}):{" ..." if self.doc_string == "" else ""}'
        )

        if self.doc_string != "":
            if len(self.parameters) > 0:
                lines.extend([f'    """{self.doc_string}', "    "])
                for param in self.parameters:
                    lines.append(f"    :param {param.name}: {param.doc_string}")
                lines.append(f'    """')
            else:
                lines.append(f'    """{self.doc_string}"""')

        return lines


@dataclass
class Property:
    name: str
    type: BaseType
    setter: bool
    static: bool
    doc_string: str

    def to_lines(self) -> List[str]:
        lines: List[str] = []

        if self.static:
            lines.append("@staticmethod")

        lines.append(f"@{self.name}.setter" if self.setter else "@property")

        args = ", ".join(
            ([] if self.static else ["self"]) + ([f"value: {self.type}"] if self.setter else [])
        )

        lines.append(
            f'def {self.name}({args}) -> {"None" if self.setter else self.type}:{" ..." if self.doc_string == "" else ""}'
        )

        if self.doc_string != "":
            lines.append(f'    """{self.doc_string}"""')

        return lines


@dataclass
class ItemProperty(Property):
    def __init__(
        self, key_type: BaseType, value_type: BaseType, setter: bool, doc_string: str = ""
    ):
        super().__init__("Item", value_type, setter, False, doc_string)
        self.key_type: BaseType = key_type

    def to_lines(self) -> List[str]:
        lines: List[str] = []

        if self.setter:
            lines.append(
                f'def __setitem__(self, key: {self.key_type}, value: {self.type}) -> None:{" ..." if self.doc_string == "" else ""}'
            )
        else:
            lines.append(
                f'def __getitem__(self, key: {self.key_type}) -> {self.type}:{" ..." if self.doc_string == "" else ""}'
            )

        if self.doc_string != "":
            lines.append(f'    """{self.doc_string}"""')

        return lines


@dataclass
class Method:
    name: str
    parameters: Tuple[Parameter, ...]
    return_types: Tuple[BaseType, ...]
    static: bool = False
    overload: bool = False
    doc_string: str = ""

    def to_lines(self) -> List[str]:
        lines: List[str] = []

        if self.static:
            lines.append("@staticmethod")

        if self.overload:
            lines.append("@overload")

        params = ", ".join(([] if self.static else ["self"]) + list(map(str, self.parameters)))

        return_str = ""
        if len(self.return_types) > 0:
            if len(self.return_types) == 1:
                return_str = f" -> {self.return_types[0]}"
            else:
                return_str = f' -> Tuple[{", ".join(str(t) for t in self.return_types)}]'

        lines.append(
            f'def {self.name}({params}){return_str}:{" ..." if self.doc_string == "" else ""}'
        )

        if self.doc_string != "":
            if len(self.parameters) > 0:
                lines.extend([f'    """{self.doc_string}', "    "])
                for param in self.parameters:
                    lines.append(f"    :param {param.name}: {param.doc_string}")
                lines.append(f'    """')
            else:
                lines.append(f'    """{self.doc_string}"""')

        return lines


@dataclass
class Event:
    name: str
    type: BaseType
    doc_string: str = ""

    def to_lines(self) -> List[str]:
        lines: List[str] = [f"{self.name}: EventType[{self.type}] = ..."]

        if self.doc_string != "":
            lines.append(f'"""{self.doc_string}"""')

        return lines


@dataclass
class Parameter:
    name: str
    type: BaseType
    default: Optional[str] = None
    is_out: bool = False
    doc_string: str = ""

    def __str__(self) -> str:
        return f'{self.name}: {self.type}{f" = {self.default}" if self.default else ""}'


class BaseType:
    def __init__(self, name: str):
        self.name = name
        self.is_ref = False
        self.is_pointer = False

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class WrappedType(BaseType):
    def __init__(self, base: BaseType, inner: Tuple[BaseType, ...] = ()):
        super().__init__(str(base))

        self.base: BaseType = base
        self.inner: Tuple[BaseType, ...] = inner

    def __str__(self) -> str:
        return str(self.base) + (
            f'[{", ".join(map(str, self.inner))}]' if len(self.inner) > 0 else ""
        )


class SpecialType(BaseType):
    def __init__(self, name: str, value: str):
        super().__init__(name)
        self.value = value

    def to_lines(self) -> List[str]:
        return [self.__str__()]


class SystemType(SpecialType):
    def __init__(self, name: str, value: str):
        super().__init__(name, value)

    def to_lines(self) -> List[str]:
        return [f"{self.name} = {self.value}"]


class EventType(SpecialType):
    def __init__(self):
        super().__init__("EventType", "")

    def to_lines(self) -> List[str]:
        return [
            "class EventType(Generic[T]):",
            "    def __iadd__(self, other: T): ...",
            "    ",
            "    def __isub__(self, other: T): ...",
        ]


class VarType(BaseType):
    def __init__(self, name: str, bounds: Tuple[BaseType, ...] = ()):
        super().__init__(name)
        self.bounds: Tuple[BaseType, ...] = bounds

    def to_lines(self) -> List[str]:
        bound = ""
        if len(self.bounds) > 0:
            if len(self.bounds) == 1:
                bound = f", bound={self.bounds[0]}"
            else:
                bound = f', bound=Union[{", ".join(str(b) for b in self.bounds)}]'
        return [f"{self.name} = TypeVar('{self.name}'{bound})"]
