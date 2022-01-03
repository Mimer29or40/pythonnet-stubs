from __future__ import annotations

from typing import Union

import clr

import System
from System import String
from System.Collections import *


def main():
    print('__all__', getattr(clr, '__all__', None))
    print('__spec__', getattr(clr, '__spec__', None))
    print('__file__', getattr(clr, '__file__', None))
    print('__name__', getattr(clr, '__name__', None))
    print('__path__', getattr(clr, '__path__', None))
    print('__loader__', getattr(clr, '__loader__', None))
    print('__package__', getattr(clr, '__package__', None))
    
    print('__all__', getattr(System, '__all__', None))
    print('__spec__', getattr(System, '__spec__', None))
    print('__file__', getattr(System, '__file__', None))
    print('__name__', getattr(System, '__name__', None))
    print('__path__', getattr(System, '__path__', None))
    print('__loader__', getattr(System, '__loader__', None))
    print('__package__', getattr(System, '__package__', None))
    
    print('__all__', getattr(String, '__all__', None))
    print('__spec__', getattr(String, '__spec__', None))
    print('__file__', getattr(String, '__file__', None))
    print('__name__', getattr(String, '__name__', None))
    print('__path__', getattr(String, '__path__', None))
    print('__loader__', getattr(String, '__loader__', None))
    print('__package__', getattr(String, '__package__', None))


class Int32:
    def __init__(self, v=0):
        self.v = v
    
    def func(self) -> Int32:
        print(self.v)
        return self


IntType = Union[int, Int32]


def func(i: IntType) -> IntType:
    return Int32(i)
    

if __name__ == '__main__':
    i = Int32()
    x = func(i)
    x.func()
    y = func(3)
    y.func()
    main()
