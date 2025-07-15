from __future__ import annotations

import dataclasses
from collections.abc import Collection
from collections.abc import Mapping
from collections.abc import Sequence
from dataclasses import replace

import clr
from System.Reflection import Assembly
from System.Reflection import BindingFlags
from System.Reflection import MethodInfo
from System.Reflection import PropertyInfo
from System.Reflection import TypeInfo

from stubgen.build_stubs import Doc
from stubgen.build_stubs import Imports
from stubgen.build_stubs import build_method
from stubgen.build_stubs import build_property
from stubgen.extract_stubs import extract_method
from stubgen.extract_stubs import extract_property
from stubgen.model import CMethod
from stubgen.model import CParameter
from stubgen.model import CProperty


def _extract_properties(
    type: TypeInfo, binding_flags: BindingFlags = None
) -> Collection[CProperty]:
    found: dict[str, CProperty] = {}

    info: PropertyInfo
    if binding_flags is None:
        binding_flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
    for info in type.GetProperties(binding_flags):
        obj: CProperty = extract_property(info)
        key: str = obj.to_doc_json()[0]
        found[key] = obj

    bases: list[CProperty] = []
    base_binding_flags: BindingFlags = BindingFlags.Public | BindingFlags.Instance
    if type.BaseType is not None:
        bases.extend(_extract_properties(type.BaseType, binding_flags=base_binding_flags))
    interface: TypeInfo
    for interface in type.GetInterfaces():
        bases.extend(_extract_properties(interface, binding_flags=base_binding_flags))

    base: CProperty
    for base in bases:
        key: str = base.to_doc_json()[0]
        new: CProperty
        if key in found:
            new = replace(found[key], declaring_type=base.declaring_type)
        else:
            new = base
        found[key] = new

    return found.values()


def extract_properties(info: TypeInfo) -> Mapping[str, CProperty]:
    raw: Sequence[CProperty] = sorted(_extract_properties(info))

    excluded: Collection[str] = ("Item",)

    return {str(p): p for p in raw if p.name not in excluded}


def _extract_methods(type: TypeInfo, binding_flags: BindingFlags = None) -> Collection[CMethod]:
    found: dict[str, CMethod] = {}

    info: MethodInfo
    if binding_flags is None:
        binding_flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
    for info in type.GetMethods(binding_flags):
        obj: CMethod = extract_method(info)
        key: str = obj.to_doc_json()[0]
        found[key] = obj

    bases: list[CMethod] = []
    base_binding_flags: BindingFlags = BindingFlags.Public | BindingFlags.Instance
    if type.BaseType is not None:
        bases.extend(_extract_methods(type.BaseType, binding_flags=base_binding_flags))
    interface: TypeInfo
    for interface in type.GetInterfaces():
        bases.extend(_extract_methods(interface, binding_flags=base_binding_flags))

    base: CMethod
    for base in bases:
        key: str = base.to_doc_json()[0]
        new: CMethod
        if key in found:
            new = replace(found[key], declaring_type=base.declaring_type)
        else:
            new = base
        found[key] = new

    return found.values()


def extract_methods(info: TypeInfo) -> Mapping[str, CMethod]:
    raw: list[CMethod] = list(_extract_methods(info))

    supported_methods: Mapping[str, tuple[str, bool]] = {
        "op_Addition": ("__add__", True),
        "op_BitwiseAnd": ("__and__", True),
        "op_BitwiseOr": ("__or__", True),
        # "op_Decrement": "",
        "op_Division": ("__truediv__", True),
        "op_Equality": ("__eq__", True),
        "op_ExclusiveOr": ("__xor__", True),
        "op_GreaterThan": ("__gt__", True),
        "op_GreaterThanOrEqual": ("__ge__", True),
        # "op_Implicit": ""
        # "op_Increment": "",
        "op_Inequality": ("__ne__", True),
        "op_LeftShift": ("__lshift__", True),
        "op_LessThan": ("__lt__", True),
        "op_LessThanOrEqual": ("__le__", True),
        "op_Modulus": ("__mod__", True),
        "op_Multiply": ("__mul__", True),
        "op_OnesComplement": ("__invert__", True),
        "op_RightShift": ("__rshift__", True),
        "op_Subtraction": ("__sub__", True),
        "op_UnaryNegation": ("__neg__", True),
        "op_UnaryPlus": ("__pos__", True),
        # "op_UnsignedRightShift": "",
        "get_Item": ("__getitem__", False),
        "set_Item": ("__setitem__", False),
        "Remove": ("__delitem__", False),
        "get_Count": ("__len__", False),
        "Contains": ("__contains__", False),
        "ContainsKey": ("__contains__", False),
        "GetEnumerator": ("__iter__", False),
    }

    method: CMethod
    for method in tuple(filter(lambda m: m.name in supported_methods, raw)):
        new_name, remove_param = supported_methods[method.name]
        parameters: Sequence[CParameter] = method.parameters
        if remove_param:
            parameters = tuple(
                map(
                    lambda p: dataclasses.replace(p, name="other"),
                    method.parameters[1:],
                )
            )

        method: CMethod = dataclasses.replace(
            method,
            name=new_name,
            parameters=parameters,
            static=False,
        )
        raw.append(method)

    def func(method: CMethod) -> bool:
        return not (
            method.name.startswith("get_")
            or method.name.startswith("set_")
            or method.name.startswith("add_")
            or method.name.startswith("remove_")
        )

    return {str(m): m for m in sorted(filter(func, raw))}


def do_main(type: TypeInfo) -> None:
    print(type.Name)

    imports: Imports = Imports()
    doc: Doc = Doc({})

    properties: Mapping[str, CProperty] = extract_properties(type)
    property: CProperty
    for property in properties.values():
        print(property)
        built: Sequence[str] = build_property(property, imports=imports, doc=doc)
        # print("\n".join(built))
        built += []

    methods: Mapping[str, CMethod] = extract_methods(type)
    method: CMethod
    for method in methods.values():
        print(method)
        built: Sequence[str] = build_method(method, imports=imports, doc=doc, overload=False)
        # print("\n".join(built))
        built += []

    print()


ASSEMBLY_LIST: Sequence[str] = (
    "TestLib",
    "OSIsoft.AFSDK",
)


TYPE_LIST: Sequence[str] = (
    "ClassWithProperties",
    "OverriddenProperty",
    "AFTime",
    "AFTimeRules",
    "PIPoint",
    "PISystems",
    "AFCategories",
    # "AFDictionary`2",
    "AFDeliveryFormatProperties",
)


def main() -> None:
    import sys

    sys.path.append("C:/Projects/pythonnet-stubs/dlls")

    assembly_name: str
    for assembly_name in ASSEMBLY_LIST:
        assembly: Assembly = clr.AddReference(assembly_name)

        type: TypeInfo
        for type in assembly.GetTypes():
            if type.Name in TYPE_LIST:
                do_main(type)


if __name__ == "__main__":
    main()
