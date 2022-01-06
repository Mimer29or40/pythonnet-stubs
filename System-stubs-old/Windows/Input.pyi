__all__ = [
    'ICommand',
]

from typing import Optional

from System import ObjectType, Boolean


# TODO

# ---------- INTERFACES ---------- #

class ICommand:
    """Defines a command."""
    
    def CanExecute(self, parameter: Optional[ObjectType]) -> Boolean:
        """Defines the method that determines whether the command can execute
        in its current state.
        """
    
    def Execute(self, parameter: Optional[ObjectType]) -> None:
        """Defines the method to be called when the command is invoked."""
    
    @property
    def CanExecuteChanged(self) -> Optional[EventHandler]:
        """Occurs when changes occur that affect whether or not the command
        should execute.
        """
