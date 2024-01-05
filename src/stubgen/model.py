from __future__ import annotations

import copy
import re
from abc import ABC
from dataclasses import dataclass
from dataclasses import field
from types import NoneType
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from System import Delegate
from System import MulticastDelegate
from System.Reflection import ConstructorInfo
from System.Reflection import EventInfo
from System.Reflection import FieldInfo
from System.Reflection import MethodInfo
from System.Reflection import ParameterInfo
from System.Reflection import PropertyInfo
from System.Reflection import TypeInfo

from stubgen.log import get_logger
from stubgen.util import make_python_name

logger = get_logger(__name__)

T = TypeVar("T")

JsonType = Union[NoneType, int, float, str, Sequence, Mapping]


@dataclass
class CAssembly:
    name: str
    version: str
    culture: str
    public_key_token: str
    namespaces: Dict[str, CNamespace] = field(default_factory=dict)


@dataclass
class CNamespace:
    name: str
    classes: Dict[str, CClass] = field(default_factory=dict)
    structs: Dict[str, CStruct] = field(default_factory=dict)
    interfaces: Dict[str, CInterface] = field(default_factory=dict)
    enums: Dict[str, CEnum] = field(default_factory=dict)
    delegates: Dict[str, CDelegate] = field(default_factory=dict)


@dataclass
class CTypeDefinition(ABC):
    name: str
    namespace: Optional[str]

    def to_json(self) -> JsonType:
        pass

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        pass

    @classmethod
    def from_info(cls: Type[T], info: TypeInfo) -> T:
        if info.IsValueType:
            if info.IsEnum:
                return CEnum.from_info(info)
            return CStruct.from_info(info)
        if info.IsInterface:
            return CInterface.from_info(info)
        if (
            info.IsSubclassOf(Delegate) or info.IsSubclassOf(MulticastDelegate)
        ) and info not in (Delegate, MulticastDelegate):
            return CDelegate.from_info(info)
        if info.IsClass:
            return CClass.from_info(info)


@dataclass
class CClass(CTypeDefinition):
    abstract: bool
    generic_args: Sequence[CType]
    super_class: CType
    interfaces: Sequence[CType]
    fields: Mapping[str, CField]
    constructors: Mapping[str, CConstructor]
    properties: Mapping[str, CProperty]
    methods: Mapping[str, CMethod]
    events: Mapping[str, CEvent]

    def __str__(self) -> str:
        name: str = self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        # TODO - Handle generic
        return name

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "namespace": self.namespace,
            "abstract": self.abstract,
            "generic_args": tuple(map(CType.to_json, self.generic_args)),
            "super_class": CType.to_json(self.super_class),
            "interfaces": tuple(map(CType.to_json, self.interfaces)),
            "fields": {k: CField.to_json(v) for k, v in self.fields.items()},
            "constructors": {k: CConstructor.to_json(v) for k, v in self.constructors.items()},
            "properties": {k: CProperty.to_json(v) for k, v in self.properties.items()},
            "methods": {k: CMethod.to_json(v) for k, v in self.methods.items()},
            "events": {k: CEvent.to_json(v) for k, v in self.events.items()},
        }

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            abstract=json["abstract"],
            generic_args=tuple(map(CType.from_json, json["generic_args"])),
            super_class=CType.from_json(json["super_class"]),
            interfaces=tuple(map(CType.from_json, json["interfaces"])),
            fields={k: CField.from_json(v) for k, v in json["fields"].items()},
            constructors={k: CConstructor.from_json(v) for k, v in json["constructors"].items()},
            properties={k: CProperty.from_json(v) for k, v in json["properties"].items()},
            methods={k: CMethod.from_json(v) for k, v in json["methods"].items()},
            events={k: CEvent.from_json(v) for k, v in json["events"].items()},
        )

    @classmethod
    def from_info(cls: Type[T], info: TypeInfo) -> T:
        logger.info(f'Processing {cls.__name__} "{info.Namespace}.{info.Name}"')

        generic_args: List[CType] = list(map(CType.from_info, info.GetGenericArguments()))
        super_class: CType = CType.from_info(info.BaseType)
        interfaces: List[CType] = list(map(CType.from_info, info.GetInterfaces()))

        fields: List[CField] = CField.get(info)
        constructors: List[CConstructor] = CConstructor.get(info)
        properties: List[CProperty] = CProperty.get(info)
        methods: List[CMethod] = CMethod.get(info)

        dunder_methods: Mapping[str, Tuple[str, bool]] = {
            # Arithmetic
            "op_Addition": ("__add__", True),
            "op_Subtraction": ("__sub__", True),
            "op_Multiply": ("__mul__", True),
            "op_Division": ("__truediv__", True),
            "op_Modulus": ("__mod__", True),
            "op_UnaryNegation": ("__neg__", True),
            "op_UnaryPlus": ("__pos__", True),
            # "op_Increment": "",
            # "op_Decrement": "",
            # Bitwise
            "op_BitwiseAnd": ("__and__", True),
            "op_BitwiseOr": ("__or__", True),
            "op_ExclusiveOr": ("__xor__", True),
            "op_LeftShift": ("__lshift__", True),
            "op_RightShift": ("__rshift__", True),
            "op_OnesComplement": ("__invert__", True),
            # "op_UnsignedRightShift": "",
            # Comparison
            "op_Equality": ("__eq__", True),
            "op_Inequality": ("__ne__", True),
            "op_LessThanOrEqual": ("__le__", True),
            "op_GreaterThanOrEqual": ("__ge__", True),
            "op_LessThan": ("__lt__", True),
            "op_GreaterThan": ("__gt__", True),
            # Other
            # "op_Implicit": ""
            # Collections
            "get_Item": ("__getitem__", False),
            "set_Item": ("__setitem__", False),
        }
        # Remove -> __delitem__
        for method in tuple(methods):
            if method.name in dunder_methods:
                new_name, remove_param = dunder_methods[method.name]
                method: CMethod = copy.deepcopy(method)
                method.name = new_name
                if remove_param:
                    method.parameters = method.parameters[1:]
                method.static = False
                methods.append(method)
        for interface in interfaces:
            if len(interface.inner) > 0:
                if interface.name == "IEnumerable":
                    method = CMethod(
                        name="__iter__",
                        declaring_type=CType.from_info(info),
                        parameters=tuple(),
                        returns=(
                            CType("Iterator", "typing", copy.deepcopy(interface.inner), False),
                        ),
                        static=False,
                        overload=False,
                    )
                    methods.append(method)
                elif interface.name == "ICollection":
                    method = CMethod(
                        name="__len__",
                        declaring_type=CType.from_info(info),
                        parameters=tuple(),
                        returns=(CType("int", None, tuple(), False),),
                        static=False,
                        overload=False,
                    )
                    methods.append(method)
                    method = CMethod(
                        name="__contains__",
                        declaring_type=CType.from_info(info),
                        parameters=(
                            CParameter("value", copy.deepcopy(interface.inner[0]), False, False),
                        ),
                        returns=(CType("bool", None, tuple(), False),),
                        static=False,
                        overload=False,
                    )
                    methods.append(method)

        methods = sorted(methods)
        # TODO - Sorting methods

        # TODO - event_info.DeclaringType == info
        events: Sequence[CEvent] = tuple(map(CEvent.from_info, info.GetEvents()))

        # TODO - Nested things
        # nested_type_obj: System.Type
        # for nested_type_obj in class_obj.GetNestedTypes():
        #     if nested_type_obj.IsValueType:
        #         if nested_type_obj.IsEnum:
        #             clazz.sub_enums.append(_process_enum(namespace, nested_type_obj))
        #             continue
        #         clazz.sub_structs.append(_process_class(namespace, nested_type_obj))
        #         continue
        #     if nested_type_obj.IsInterface:
        #         clazz.sub_interfaces.append(_process_interface(namespace, nested_type_obj))
        #         continue
        #     if nested_type_obj.IsClass:
        #         clazz.sub_classes.append(_process_class(namespace, nested_type_obj))
        #         continue

        return cls(
            name=make_python_name(info.Name),
            namespace=info.Namespace,
            abstract=info.IsAbstract,
            generic_args=generic_args,
            super_class=super_class,
            interfaces=interfaces,
            fields={str(f): f for f in fields if f is not None},
            constructors={str(c): c for c in constructors if c is not None},
            properties={str(p): p for p in properties if p is not None},
            methods={str(m): m for m in methods if m is not None},
            events={str(e): e for e in events if e is not None},
        )


@dataclass
class CStruct(CClass):
    pass


@dataclass
class CInterface(CTypeDefinition):
    abstract: bool
    generic_args: Sequence[CType]
    super_class: CType
    properties: Mapping[str, CProperty]
    methods: Mapping[str, CMethod]
    # events: Mapping[str, CEvent]
    dunder_methods: Mapping[str, CMethod]

    def to_json(self) -> JsonType:
        pass

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        pass

    @classmethod
    def from_info(cls: Type[T], info: TypeInfo) -> T:
        logger.info(f'Processing {cls.__name__} "{info.Namespace}.{info.Name}"')

        # generic_args: Sequence[CType] = tuple(map(CType.from_info, info.GetGenericArguments()))
        # super_class: CType = CType.from_info(info.BaseType)
        # interfaces: Sequence[CType] = tuple(map(CType.from_info, info.GetInterfaces()))
        # fields: Sequence[CField] = tuple(map(CField.from_info, CField.get_fields(info)))
        # constructors: Sequence[CConstructor] = tuple(
        #     map(CConstructor.from_info, info.GetConstructors())
        # )
        # properties: Sequence[CProperty] = tuple(
        #     map(CProperty.from_info, CProperty.get_properties(info))
        # )
        # methods: Sequence[CMethod] = tuple(map(CMethod.from_info, CMethod.get_methods(info)))
        #
        # dunder_methods: Dict[str, CMethod] = {}
        # supported_methods: Mapping[str, Tuple[str, bool]] = {
        #     # Arithmetic
        #     "op_Addition": ("__add__", True),
        #     "op_Subtraction": ("__sub__", True),
        #     "op_Multiply": ("__mul__", True),
        #     "op_Division": ("__truediv__", True),
        #     "op_Modulus": ("__mod__", True),
        #     "op_UnaryNegation": ("__neg__", True),
        #     "op_UnaryPlus": ("__pos__", True),
        #     # "op_Increment": "",
        #     # "op_Decrement": "",
        #     # Bitwise
        #     "op_BitwiseAnd": ("__and__", True),
        #     "op_BitwiseOr": ("__or__", True),
        #     "op_ExclusiveOr": ("__xor__", True),
        #     "op_LeftShift": ("__lshift__", True),
        #     "op_RightShift": ("__rshift__", True),
        #     "op_OnesComplement": ("__invert__", True),
        #     # "op_UnsignedRightShift": "",
        #     # Comparison
        #     "op_Equality": ("__eq__", True),
        #     "op_Inequality": ("__ne__", True),
        #     "op_LessThanOrEqual": ("__le__", True),
        #     "op_GreaterThanOrEqual": ("__ge__", True),
        #     "op_LessThan": ("__lt__", True),
        #     "op_GreaterThan": ("__gt__", True),
        #     # Other
        #     # "op_Implicit": ""
        #     # Collections
        #     "get_Item": ("__getitem__", False),
        #     "set_Item": ("__setitem__", False),
        # }
        # # Remove -> __delitem__
        # for method in methods:
        #     if method.name in supported_methods:
        #         new_name, remove_param = supported_methods[method.name]
        #         method: CMethod = copy.deepcopy(method)
        #         method.name = new_name
        #         if remove_param:
        #             method.parameters = method.parameters[1:]
        #         method.static = False
        #         dunder_methods[str(method)] = method
        # for interface in interfaces:
        #     if len(interface.inner) > 0:
        #         if interface.name == "IEnumerable":
        #             method = CMethod(
        #                 name="__iter__",
        #                 declaring_type=CType.from_info(info),
        #                 parameters=tuple(),
        #                 returns=(
        #                     CType("Iterator", "typing", copy.deepcopy(interface.inner), False),
        #                 ),
        #                 static=False,
        #                 overload=False,
        #             )
        #             dunder_methods[str(method)] = method
        #         elif interface.name == "ICollection":
        #             method = CMethod(
        #                 name="__len__",
        #                 declaring_type=CType.from_info(info),
        #                 parameters=tuple(),
        #                 returns=(CType("int", None, tuple(), False),),
        #                 static=False,
        #                 overload=False,
        #             )
        #             dunder_methods[str(method)] = method
        #             method = CMethod(
        #                 name="__contains__",
        #                 declaring_type=CType.from_info(info),
        #                 parameters=(
        #                     CParameter("value", copy.deepcopy(interface.inner[0]), False, False),
        #                 ),
        #                 returns=(CType("bool", None, tuple(), False),),
        #                 static=False,
        #                 overload=False,
        #             )
        #             dunder_methods[str(method)] = method
        #
        # # TODO - Culling/Sorting methods
        #
        # # TODO - Events
        # # event_info: EventInfo
        # # for event_info in class_obj.GetEvents():
        # #     if event_info.DeclaringType == class_obj:
        # #         clazz.events.append(_process_event(namespace, event_info))
        # # clazz.events.sort(key=lambda e: e.name)
        #
        # # TODO - Nested things
        # # nested_type_obj: System.Type
        # # for nested_type_obj in class_obj.GetNestedTypes():
        # #     if nested_type_obj.IsValueType:
        # #         if nested_type_obj.IsEnum:
        # #             clazz.sub_enums.append(_process_enum(namespace, nested_type_obj))
        # #             continue
        # #         clazz.sub_structs.append(_process_class(namespace, nested_type_obj))
        # #         continue
        # #     if nested_type_obj.IsInterface:
        # #         clazz.sub_interfaces.append(_process_interface(namespace, nested_type_obj))
        # #         continue
        # #     if nested_type_obj.IsClass:
        # #         clazz.sub_classes.append(_process_class(namespace, nested_type_obj))
        # #         continue
        #
        # return cls(
        #     name=make_python_name(info.Name),
        #     namespace=info.Namespace,
        #     abstract=info.IsAbstract,
        #     generic_args=generic_args,
        #     super_class=super_class,
        #     interfaces=interfaces,
        #     fields={str(f): f for f in fields if f is not None},
        #     constructors={str(c): c for c in constructors if c is not None},
        #     properties={str(p): p for p in properties if p is not None},
        #     methods={
        #         str(m): m
        #         for m in methods
        #         if m is not None and not m.name.startswith("get_") and not m.name.startswith("set_")
        #     },
        #     dunder_methods=dunder_methods,
        # )


@dataclass
class CEnum(CTypeDefinition):
    fields: Sequence[str]

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "namespace": self.namespace,
            "fields": self.fields,
        }

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            fields=tuple(json["fields"]),
        )

    @classmethod
    def from_info(cls: Type[T], info: TypeInfo) -> T:
        logger.info(f'Processing {cls.__name__} "{info.Namespace}.{info.Name}"')
        return cls(
            name=make_python_name(info.Name),
            namespace=info.Namespace,
            fields=tuple(info.GetEnumNames()),
        )


@dataclass
class CDelegate(CTypeDefinition):
    def to_json(self) -> JsonType:
        pass

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        pass

    @classmethod
    def from_info(cls: Type[T], info: TypeInfo) -> T:
        logger.info(f'Processing {cls.__name__} "{info.Namespace}.{info.Name}"')


@dataclass
class CType:
    name: str
    namespace: Optional[str]
    inner: Sequence[CType]
    is_generic: bool

    def __str__(self) -> str:
        name: str = ("$" if self.is_generic else "") + self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        if len(self.inner) > 0:
            name = f"{name}[{', '.join(map(str, self.inner))}]"
        return name

    def to_json(self) -> JsonType:
        return str(self)

    @classmethod
    def from_json(cls, json: JsonType) -> CType:
        match: re.Match = re.match(r"(\w+(?:\.\w+)+)\.(\$?\w+)(?:\[(.*)])?", json)
        name: str = match.group(2)
        inner: Sequence[CType] = tuple()
        if (inner_str := match.group(3)) is not None:
            inner = tuple(map(CType.from_json, inner_str.split(", ")))
        return cls(
            name=name.replace("$", ""),
            namespace=match.group(1),
            inner=inner,
            is_generic="$" in name,
        )

    @classmethod
    def from_info(cls, info: TypeInfo) -> CType:
        return cls(
            name=make_python_name(info.Name),
            namespace=info.Namespace,
            inner=tuple(map(CType.from_info, info.GetGenericArguments())),
            is_generic=info.IsGenericParameter,
        )


@dataclass
class CField:
    name: str
    declaring_type: CType
    returns: CType
    static: bool

    def __str__(self) -> str:
        return f"{self.declaring_type}.{self.name}"

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": CType.to_json(self.declaring_type),
            "returns": CType.to_json(self.returns),
            "static": self.static,
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CField:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            returns=CType.from_json(json["returns"]),
            static=json["static"],
        )

    @classmethod
    def from_info(cls, info: FieldInfo) -> CField:
        return cls(
            name=make_python_name(info.Name),
            declaring_type=CType.from_info(info.DeclaringType),
            returns=CType.from_info(info.FieldType),
            static=info.IsStatic,
        )

    @classmethod
    def get(cls, type: TypeInfo, exclude_static: bool = False) -> List[CField]:
        def check(obj: CField) -> str:
            return obj.name

        found: List[CField] = []
        if type.BaseType is not None:
            found.extend(cls.get(type.BaseType, exclude_static=True))
        for interface in type.GetInterfaces():
            found.extend(cls.get(interface, exclude_static=True))

        check_list: Sequence[str] = tuple(map(check, found))
        info: MethodInfo
        for info in type.GetFields():
            if info.IsStatic and exclude_static:
                continue
            parsed = cls.from_info(info)
            if check(parsed) in check_list:
                continue
            found.append(parsed)
        return found


@dataclass
class CConstructor:
    declaring_type: CType
    parameters: Sequence[CParameter]

    def __str__(self) -> str:
        param_types: str = ", ".join(str(p.type) for p in self.parameters)
        return f"{self.declaring_type}.__init__({param_types})"

    def to_json(self) -> JsonType:
        return {
            "declaring_type": CType.to_json(self.declaring_type),
            "parameters": tuple(map(CParameter.to_json, self.parameters)),
        }

    @classmethod
    def from_json(cls, info: JsonType) -> CConstructor:
        return cls(
            declaring_type=CType.from_json(info["declaring_type"]),
            parameters=tuple(map(CParameter.from_json, info["parameters"])),
        )

    @classmethod
    def from_info(cls, info: ConstructorInfo) -> CConstructor:
        return cls(
            declaring_type=CType.from_info(info.DeclaringType),
            parameters=tuple(map(CParameter.from_info, info.GetParameters())),
        )

    @classmethod
    def get(cls, type: TypeInfo) -> List[CConstructor]:
        return list(map(CConstructor.from_info, type.GetConstructors()))


@dataclass
class CProperty:
    name: str
    declaring_type: CType
    type: CType
    setter: bool
    static: bool

    def __str__(self) -> str:
        return f"{self.declaring_type}.{self.name}"

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": CType.to_json(self.declaring_type),
            "type": CType.to_json(self.type),
            "setter": self.setter,
            "static": self.static,
        }

    @classmethod
    def from_json(cls, info: JsonType) -> CProperty:
        return cls(
            name=info["name"],
            declaring_type=CType.from_json(info["declaring_type"]),
            type=CType.from_json(info["type"]),
            setter=info["setter"],
            static=info["static"],
        )

    @classmethod
    def from_info(cls, info: PropertyInfo) -> CProperty:
        get_method: MethodInfo = info.GetGetMethod()
        set_method: MethodInfo = info.GetSetMethod()

        return cls(
            name=make_python_name(info.Name),
            declaring_type=CType.from_info(info.DeclaringType),
            type=CType.from_info(info.PropertyType),
            setter=set_method is not None,
            static=get_method is not None and get_method.IsStatic,
        )

    @classmethod
    def get(cls, type: TypeInfo) -> List[CProperty]:
        def check(obj: CProperty) -> str:
            return obj.name

        found: List[CProperty] = []
        if type.BaseType is not None:
            found.extend(cls.get(type.BaseType))
        for interface in type.GetInterfaces():
            found.extend(cls.get(interface))

        check_list: Sequence[str] = tuple(map(check, found))
        info: PropertyInfo
        for info in type.GetProperties():
            parsed = cls.from_info(info)
            if check(parsed) in check_list:
                continue
            found.append(parsed)
        return found


@dataclass
class CMethod:
    name: str
    declaring_type: CType
    parameters: Sequence[CParameter]
    returns: Sequence[CType]
    static: bool
    overload: bool

    def __str__(self) -> str:
        param_types: str = ", ".join(str(p.type) for p in self.parameters)
        return f"{self.declaring_type}.{self.name}({param_types})"

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": CType.to_json(self.declaring_type),
            "parameters": tuple(map(CParameter.to_json, self.parameters)),
            "returns": tuple(map(CType.to_json, self.returns)),
            "static": self.static,
            "overload": self.overload,
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CMethod:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
            returns=tuple(map(CType.from_json, json["returns"])),
            static=json["static"],
            overload=json["overload"],
        )

    @classmethod
    def from_info(cls, info: MethodInfo) -> CMethod:
        return_types: List[CType] = [CType.from_info(info.ReturnType)]

        parameters: List[CParameter] = []
        for parameter_info in info.GetParameters():
            parameter: CParameter = CParameter.from_info(parameter_info)
            parameters.append(parameter)
            if parameter.is_out:
                return_types.append(copy.deepcopy(parameter.type))

        return cls(
            name=make_python_name(info.Name),
            declaring_type=CType.from_info(info.DeclaringType),
            parameters=parameters,
            returns=return_types,
            static=info.IsStatic,
            overload=False,  # TODO
        )

    @classmethod
    def get(cls, type: TypeInfo, exclude_static: bool = False) -> List[CMethod]:
        def check(obj: CMethod) -> Tuple[str, Sequence[str]]:
            return obj.name, tuple(map(lambda p: p.type, obj.parameters))

        found: List[CMethod] = []
        if type.BaseType is not None:
            found.extend(cls.get(type.BaseType, exclude_static=True))
        for interface in type.GetInterfaces():
            found.extend(cls.get(interface, exclude_static=True))

        check_list: Sequence[Tuple[str, Sequence[str]]] = tuple(map(check, found))
        info: MethodInfo
        for info in type.GetMethods():
            if info.IsStatic and exclude_static:
                continue
            parsed = cls.from_info(info)
            if check(parsed) in check_list:
                continue
            found.append(parsed)
        return found


@dataclass
class CParameter:
    name: str
    type: CType
    has_default: bool
    is_out: bool

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "type": CType.to_json(self.type),
            "has_default": self.has_default,
            "is_out": self.is_out,
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CParameter:
        return cls(
            name=json["name"],
            type=CType.from_json(json["type"]),
            has_default=json["has_default"],
            is_out=json["is_out"],
        )

    @classmethod
    def from_info(cls, info: ParameterInfo) -> CParameter:
        return cls(
            name=make_python_name(info.Name),
            type=CType.from_info(info.ParameterType),
            has_default=info.HasDefaultValue,
            is_out=info.IsOut,
        )


@dataclass
class CEvent:
    name: str
    declaring_type: CType
    type: CType

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": CType.to_json(self.declaring_type),
            "type": CType.to_json(self.type),
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CEvent:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            type=CType.from_json(json["type"]),
        )

    @classmethod
    def from_info(cls, info: EventInfo) -> CEvent:
        return cls(
            name=make_python_name(info.Name),
            declaring_type=CType.from_info(info.DeclaringType),
            type=CType.from_info(info.EventHandlerType),
        )
