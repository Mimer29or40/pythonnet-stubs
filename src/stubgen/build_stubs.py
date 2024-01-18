from __future__ import annotations

import glob
import json
from pathlib import Path
from typing import Any
from typing import Dict
from typing import Final
from typing import Mapping
from typing import Sequence
from typing import Set
from typing import Union

from stubgen.log import get_logger
from stubgen.model import CNamespace
from stubgen.util import rm_tree

logger = get_logger(__name__)


class Stub:
    imports: Final[Set[str]] = set()
    type_vars: Final[Set[str]] = set()


def build_stubs(
    skeleton_files: Sequence[Path], doc_files: Sequence[Path], output_dir: Path
) -> Union[int, str]:
    namespaces: Dict[str, CNamespace] = {}
    for skeleton_file in skeleton_files:
        with skeleton_file.open("r") as file:
            skeleton_dict: Dict[str, Any] = json.load(file)

        assembly_name: str = skeleton_dict["name"]
        assembly_version: str = skeleton_dict["version"]
        logger.info("Loading skeletons for assembly: '%s v%s'", assembly_name, assembly_version)

        for namespace_json in skeleton_dict["namespaces"].values():
            namespace: CNamespace = CNamespace.from_json(namespace_json)
            if namespace.name not in namespaces:
                namespaces[namespace.name] = namespace
            # else:
            #     namespaces[namespace.name] += namespace  # TODO - Combine namespaces

    for namespace in namespaces.values():
        namespace_dir: Path = output_dir
        namespace_file: Path = Path()
        for name in namespace.name.split("."):
            dir_name: str = f"{name}-stubs" if namespace_dir is output_dir else name
            namespace_dir = namespace_dir / dir_name
            if namespace_dir.exists():
                rm_tree(namespace_dir)
            namespace_dir.mkdir(parents=True)

            namespace_file = namespace_dir / "__init__.pyi"
            namespace_file.touch()

        print(namespace_file)

    return 0
