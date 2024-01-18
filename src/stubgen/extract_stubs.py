from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Dict
from typing import List
from typing import Sequence
from typing import Union

import clr
from System.Reflection import Assembly
from System.Reflection import AssemblyName
from System.Reflection import TypeInfo

from stubgen.log import get_logger
from stubgen.model import CNamespace
from stubgen.model import CTypeDefinition

logger = get_logger(__name__)


def extract_stubs(assembly_name: str, output_dir: Path, overwrite: bool) -> Union[int, str]:
    logger.debug(f"Extracting assembly: %r", assembly_name)

    assembly: Assembly = clr.AddReference(assembly_name)
    name: AssemblyName = assembly.GetName()

    assembly_name: str = name.Name
    assembly_version: str = name.Version.ToString()

    extract_file: Path = output_dir / f"{assembly_name}_{assembly_version}_skeleton.json"
    if extract_file.exists() and not overwrite:
        logger.critical("Extract file already exists: %r", str(extract_file))
        return 1

    doc_file: Path = output_dir / f"{assembly_name}_{assembly_version}_doc.json"
    if doc_file.exists() and not overwrite:
        logger.critical("Doc file already exists: %r", str(doc_file))
        return 1

    logger.info("Parsing types")
    type_lists: Dict[str, List[CTypeDefinition]] = defaultdict(list)
    info: TypeInfo
    for info in assembly.GetTypes():
        if info.Namespace is None or info.IsNested:
            continue
        wrapper: CTypeDefinition = CTypeDefinition.from_info(info)
        if wrapper is None:
            logger.warning("Unable to parse type:", info.FullName)
            continue
        type_lists[wrapper.namespace].append(wrapper)

    namespaces: Sequence[CNamespace] = tuple(
        CNamespace(
            name=namespace,
            types={str(t): t for t in sorted(type_list)},
        )
        for namespace, type_list in type_lists.items()
    )

    logger.info("Saving types to file")
    with extract_file.open("w") as file:
        json.dump(
            {
                "name": assembly_name,
                "version": assembly_version,
                "namespaces": {namespace.name: namespace.to_json() for namespace in namespaces},
            },
            file,
            indent=2,
        )

    logger.info("Generating doc file")
    main_doc_namespace = {}
    for namespace in namespaces:
        curr = main_doc_namespace
        for n in namespace.name.split("."):
            if n not in curr:
                curr[n] = {"doc": ""}
            curr = curr[n]
        for type in namespace.types.values():
            name, doc_json = type.to_doc_json()
            curr[name] = doc_json

    with doc_file.open("w") as file:
        json.dump(
            main_doc_namespace,
            file,
            indent=2,
        )

    return 0
