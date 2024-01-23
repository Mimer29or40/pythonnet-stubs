from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from typing import Dict
from typing import Final
from typing import List
from typing import Mapping
from typing import Optional
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


class DocDict:
    data: Mapping[str, Any]

    def __init__(self, data: Mapping[str, Any]):
        self.data = data

    def merge(self, other: DocDict) -> DocDict:
        return DocDict(DocDict.merge_node(self.data, other.data))

    @staticmethod
    def merge_node(d1: Mapping[str, Any], d2: Mapping[str, Any]) -> Mapping[str, Any]:
        new_dict: Dict[str, Any] = dict(**d1)

        for k2, v2 in d2.items():
            if k2 not in new_dict:
                new_dict[k2] = v2
                continue

            v1: Any = new_dict[k2]
            if k2 in ("doc", "return"):
                new_dict[k2] = (v1 + "\n" + v2) if v1 != "" and v2 != "" else (v1 + v2)
            elif k2 == "doc_formatted":
                new: Dict[str, Sequence[str]] = dict(**v1)
                for k, v in v2.items():
                    if k in new:
                        new[k] += v
                    else:
                        new[k] = v
                new_dict[k2] = new
            elif k2 in ("parameters", "exceptions"):
                new: Dict[str, str] = dict(**v1)
                for k, v in v2.items():
                    if k in new:
                        new[k] = (new[k] + "\n" + v) if new[k] != "" and v != "" else (new[k] + v)
                    else:
                        new[k] = v
                new_dict[k2] = new
            else:
                new_dict[k2] = DocDict.merge_node(v1, v2)

        return new_dict

    def get(self, node_str: str) -> Optional[DocDict]:
        search: str
        doc_dict: Mapping[str, Any] = self.data
        while True:
            if node_str in doc_dict:
                return DocDict(doc_dict[node_str])
            if "." in node_str:
                search, node_str = node_str.split(".", 1)
            else:
                search = node_str
            if search not in doc_dict:
                return None
            doc_dict = doc_dict[search]

    def doc_string(self, indent: int = 0, line_limit: int = 100) -> Sequence[str]:
        indent_str: str = "    " * indent

        doc: Optional[str] = self.data.get("doc", None)
        doc_formatted: Mapping[str, Sequence[str]] = self.data.get("doc_formatted", {})
        parameters: Mapping[str, str] = self.data.get("parameters", {})
        return_str: Optional[str] = self.data.get("return", None)
        exceptions: Mapping[str, str] = self.data.get("exceptions", {})

        if len(parameters) == 0 and return_str is None and len(exceptions) == 0:
            if doc is None:
                return (f'{indent_str}""""""',)
            if "\n" not in doc and 4 * indent + len(doc) + 3 <= line_limit:
                return (f'{indent_str}"""{doc}"""',)

        doc = '"""' + doc.replace("\n", "\n\n")
        doc_lines: List[str] = list(self.split(doc, indent, line_limit))

        if len(parameters) > 0 or return_str is not None or len(exceptions) > 0:
            doc_lines.append("")

            for param, param_doc in parameters.items():
                param_str: str = f":param {param}: {param_doc}"
                doc_lines.extend(self.split(param_str, indent, line_limit, "  "))

            if return_str is not None:
                doc_lines.extend(self.split(f":return: {return_str}", indent, line_limit, "  "))

            for exception, exception_doc in exceptions.items():
                param_str: str = f":except {exception}: {exception_doc}"
                doc_lines.extend(self.split(param_str, indent, line_limit, "  "))

        line_index: int = 0
        while line_index < len(doc_lines):
            line: str = doc_lines[line_index]
            for replace_str, replace_seq in doc_formatted.items():
                replace_str = f"%{replace_str}%"
                if replace_str in line:
                    doc_lines[line_index] = line.replace(replace_str, replace_seq[0])
                    for new_line in reversed(replace_seq[1:]):
                        doc_lines.insert(line_index + 1, indent_str + new_line)
            line_index += 1

        doc_lines.append(indent_str + '"""')
        return tuple(doc_lines)

    @staticmethod
    def split(text: str, indent: int = 0, line_limit: int = 100, prefix: str = "") -> Sequence[str]:
        indent_str: str = "    " * indent

        lines: List[str] = []
        for doc_paragraph in text.splitlines():
            words: List[str] = doc_paragraph.split(" ")
            doc_line: str = indent_str + words[0]
            for word in words[1:]:
                if len(doc_line) + len(word) + 1 > line_limit:
                    lines.append(doc_line)
                    doc_line = indent_str + prefix + word
                else:
                    doc_line += " " + word
            lines.append(doc_line)
        return lines


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

    doc_dict: DocDict = DocDict({})
    for doc_file in doc_files:
        logger.info("Loading Doc File: %r", str(doc_file))
        with doc_file.open("r") as file:
            loaded_doc_dict_tree: Dict[str, Any] = json.load(file)

        doc_dict = doc_dict.merge(DocDict(loaded_doc_dict_tree))

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
