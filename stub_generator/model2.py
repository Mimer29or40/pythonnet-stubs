from abc import ABC
from typing import List

from .logging import logger


class Namespace:
    """
    IMPORTS
    
    __doc__ = DOC_STRING
    
    SYSTEM_TYPES
    
    VAR_TYPES
    
    # ---------- Classes ---------- #
    
    CLASSES
    
    # ---------- Structs ---------- #
    
    STRUCTS
    
    # ---------- Interfaces ---------- #
    
    INTERFACES
    
    # ---------- Enums ---------- #
    
    ENUMS
    
    # ---------- Delegates ---------- #
    
    DELEGATES
    
    __all__ = [
        ', '.join(MEMBERS)
    ]
    """
    
    def __init__(self, name: str, doc_string: str = ''):
        self.name = name
        self.doc_string = doc_string
        
        self.py_imports = []
        self.net_imports = []
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'Namespace(name=\'{self.name}\', doc_string=\'{self.doc_string}\')'
    
    def add_py_import(self, name: str) -> None:
        if name in self.py_imports:
            return
        logger.debug(f'Adding Python Import: {name}')
        self.py_imports.append(name)
    
    def add_net_import(self, name: str) -> None:
        if name in self.net_imports:
            return
        logger.debug(f'Adding .NET Import: {name}')
        self.net_imports.append(name)
    
    def to_lines(self) -> List[str]:
        lines: List[str] = ['from __future__ import annotations']
        
        if len(self.py_imports) > 0:
            import_list: List[str] = []
            for base in sorted(set('.'.join(i.split('.')[:-1]) for i in self.py_imports)):
                prefix: str = f'{base}.'
                classes: str = ', '.join(sorted(set(i[len(prefix):] for i in self.py_imports if i.startswith(prefix))))
                import_list.append(f'from {base} import {classes}')
            lines.extend([''] + import_list)
        
        if len(self.net_imports) > 0:
            import_list: List[str] = []
            for base in sorted(set('.'.join(i.split('.')[:-1]) for i in self.net_imports)):
                if base == self.name:
                    continue
                prefix: str = f'{base}.'
                classes: str = ', '.join(sorted(set(s for i in self.net_imports if i.startswith(prefix) and '.' not in (s := i[len(prefix):]))))
                import_list.append(f'from {base} import {classes}')
            lines.extend([''] + import_list)
        
        if self.doc_string != '':
            lines.extend(['', f'"""{self.doc_string}"""'])
        
        return lines


class TypeBase(ABC):
    pass


class RegularType(TypeBase):
    pass
