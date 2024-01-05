from __future__ import annotations

import sys
from typing import Mapping
from typing import Type

import clr
from System.Reflection import Assembly
from System.Reflection import AssemblyName
from System.Reflection import TypeInfo

from stubgen.model import CAssembly
from stubgen.model import CClass
from stubgen.model import CDelegate
from stubgen.model import CEnum
from stubgen.model import CInterface
from stubgen.model import CNamespace
from stubgen.model import CStruct
from stubgen.model import CType
from stubgen.model import CTypeDefinition

sys.path.append("C:/Projects/pythonnet-stubs/dlls")


def main() -> None:
    import pprint

    raw_assembly: Assembly = clr.AddReference("OSIsoft.AFSDK")
    asm_name: AssemblyName = raw_assembly.GetName()

    assembly = CAssembly(
        name=asm_name.Name,
        version=asm_name.Version.ToString(),
        culture=asm_name.CultureName,
        public_key_token="".join(map(lambda b: f"{b:0x}", asm_name.GetPublicKeyToken())),
    )

    info: TypeInfo
    for info in raw_assembly.GetTypes():
        if info.Namespace is None or info.IsNested:
            continue
        wrapper: CTypeDefinition = CTypeDefinition.from_info(info)
        if wrapper is None:
            print("Unable to parse type:", info.FullName)
            continue

        if wrapper.namespace not in assembly.namespaces:
            assembly.namespaces[wrapper.namespace] = CNamespace(wrapper.namespace)
        namespace: CNamespace = assembly.namespaces[wrapper.namespace]

        if wrapper.__class__ == CClass and isinstance(wrapper, CClass):
            namespace.classes[wrapper.name] = wrapper
        elif wrapper.__class__ == CStruct and isinstance(wrapper, CStruct):
            namespace.structs[wrapper.name] = wrapper
        elif wrapper.__class__ == CInterface and isinstance(wrapper, CInterface):
            namespace.interfaces[wrapper.name] = wrapper
        elif wrapper.__class__ == CEnum and isinstance(wrapper, CEnum):
            namespace.enums[wrapper.name] = wrapper
        elif wrapper.__class__ == CDelegate and isinstance(wrapper, CDelegate):
            namespace.delegates[wrapper.name] = wrapper

        # # if info.Name == "IAFNamedCollection":
        # type = CType.from_info(info)
        # # if type.name == "IAFNamedCollection":
        # #     type = TypeWrapper.from_info(info)
        # json = CType.from_json(type.to_json())
        # print(type, type == json)
    print("DONE")


if __name__ == "__main__":
    main()
