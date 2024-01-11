from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict
from typing import List
from typing import Mapping
from typing import Sequence
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
    # raw_assembly: Assembly = clr.AddReference("mscorlib")

    assembly = CAssembly.extract(raw_assembly)
    # json = assembly.to_json()

    file: Path = Path("out.json")
    file.write_text(json.dumps(assembly.to_json(), indent=4))
    print("DONE")


if __name__ == "__main__":
    main()
