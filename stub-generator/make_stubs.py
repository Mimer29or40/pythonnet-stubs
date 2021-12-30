import json
import os
from pathlib import Path
from typing import Dict

from .logger import logger


def make(output_dir: str, assembly_or_builtin: str, overwrite: bool = False, quiet: bool = False) -> Dict:
    """Main Processing Function"""
    assembly_dict = {}
    logger.info('='*80)
    logger.info('Making [{}]'.format(assembly_or_builtin))

    return assembly_dict


def dump_json_log(namespaces_dict):
    json_dir: Path = Path('logs')
    json_dir.mkdir(exist_ok=True)
    name = '-'.join(namespaces_dict.keys())
    filepath = json_dir / f'{name}.json'
    with filepath.open('w') as fp:
        json.dump(namespaces_dict, fp, indent=2)
