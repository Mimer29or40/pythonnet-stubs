from __future__ import annotations

from typing import TypeVar, Generic, Callable

T = TypeVar('T')


class Item(Generic[T]):
    def __getitem__(self, index: int) -> T: ...
    
    def __setitem__(self, key: int, value: T) -> None: ...
