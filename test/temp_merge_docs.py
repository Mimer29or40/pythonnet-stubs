from __future__ import annotations

import json
from collections.abc import Mapping
from collections.abc import MutableSequence
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from stubgen.build_stubs import Doc
from stubgen.build_stubs import merge_doc
from stubgen.build_stubs import merge_namespace
from stubgen.model import CNamespace


def main() -> None:
    skeleton_dir: Path = Path("C:/Projects/pyPIAF/src/stubgen/skeleton")
    doc_dir: Path = Path("C:/Projects/pyPIAF/src/stubgen/doc")
    output_dir: Path = Path("output")

    skeleton_files: MutableSequence[Path] = []
    for file_path in skeleton_dir.glob("*_skeleton.json"):
        skeleton_files.append(file_path)
        print(f"Using skeleton file: {str(file_path)!r}")

    doc_files: MutableSequence[Path] = []
    for file_path in doc_dir.glob("*_doc.json"):
        doc_files.append(file_path)
        print(f"Using doc file: {str(file_path)!r}")

    namespace: CNamespace
    namespaces: dict[str, CNamespace] = {}
    for skeleton_file in skeleton_files:
        print(f"Loading skeleton file: {str(skeleton_file)!r}")
        with skeleton_file.open("r") as file:
            skeleton_dict: Mapping[str, Any] = json.load(file)

        for namespace_json in skeleton_dict["namespaces"].values():
            namespace = CNamespace.from_json(namespace_json)
            if namespace.name in namespaces:
                namespace = merge_namespace(namespaces[namespace.name], namespace, False)
            namespaces[namespace.name] = namespace

    global_doc: Doc = Doc({})
    for doc_file in doc_files:
        print(f"Loading doc file: {str(doc_file)!r}")
        with doc_file.open("r") as file:
            loaded_doc_dict_tree: Mapping[str, Any] = json.load(file)

        new_doc: Doc = Doc(loaded_doc_dict_tree)
        global_doc = merge_doc(global_doc, new_doc)

    namespace_names: Sequence[str] = list(namespaces.keys())
    for namespace_name, namespace in namespaces.items():
        doc_file: Path = output_dir / f"{namespace_name}_doc.json"

        def func(name: str) -> bool:
            return name != namespace_name and name.startswith(namespace_name)

        doc: Doc = global_doc.get_node(namespace_name)
        raw_data: dict[str, Any] = {k: doc.data[k] for k in sorted(doc.data.keys())}
        sub_namespaces: Sequence[str] = list(filter(func, namespace_names))
        for sub_namespace in sub_namespaces:
            sub_namespace = sub_namespace.replace(namespace_name + ".", "").split(".")[0]
            if sub_namespace in raw_data:
                # noinspection PyUnresolvedReferences
                del raw_data[sub_namespace]
        doc_str = raw_data.pop("doc")
        raw_data = {"doc": doc_str, **raw_data}

        namespace_name_split: Sequence[str] = namespace_name.split(".")
        data: dict[str, Any] = {}
        data_dict: dict[str, Any] = data
        for name in namespace_name_split[:-1]:
            data_dict[name] = {}
            data_dict = data_dict[name]
        data_dict[namespace_name_split[-1]] = raw_data

        print(f"Writing doc file: {str(doc_file)!r}")
        with doc_file.open("w") as file:
            json.dump(data, file, indent=2)


if __name__ == "__main__":
    main()
