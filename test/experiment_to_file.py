from __future__ import annotations

import json
import sys
from pathlib import Path

import clr
from System.Reflection import Assembly

from stubgen.model import CAssembly

sys.path.append("C:/Projects/pythonnet-stubs/dlls")


def main() -> None:
    raw_assembly: Assembly = clr.AddReference("OSIsoft.AFSDK")
    # raw_assembly: Assembly = clr.AddReference("mscorlib")

    assembly = CAssembly.extract(raw_assembly)
    # json = assembly.to_json()

    file: Path = Path("out.json")
    file.write_text(json.dumps(assembly.to_json(), indent=4))
    print("DONE")


if __name__ == "__main__":
    main()
