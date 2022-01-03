from typing import TypeVar, Generic

TKey = TypeVar('TKey')
TValue = TypeVar('TValue')


class Item(Generic[TKey, TValue]):
    def __getitem__(self, key: TKey) -> TValue: ...
    
    def __setitem__(self, key: TKey, value: TValue) -> None: ...


class ReadOnlyItem(Generic[TKey, TValue]):
    def __getitem__(self, key: TKey) -> TValue: ...
