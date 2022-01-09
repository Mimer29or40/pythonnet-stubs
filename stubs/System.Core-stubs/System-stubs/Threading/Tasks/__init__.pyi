from __future__ import annotations

from abc import ABC
from typing import TypeVar, Union, overload

from System import Object
from System.Threading.Tasks import Task

# ---------- Types ---------- #

TResult = TypeVar('TResult')

ObjectType = Object

# ---------- Classes ---------- #

class TaskExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Unwrap(task: Task[Task]) -> Task: ...
    
    @staticmethod
    @overload
    def Unwrap(task: Task[Task[TResult]]) -> Task[TResult]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    TaskExtensions,
]
