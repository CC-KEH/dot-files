from logging import Logger
from typing import Any, TypeVar, overload
from typing_extensions import Literal, Self, TypeAlias

_ClsT = TypeVar("_ClsT", bound=type)
_EchoFlag: TypeAlias = bool | Literal["debug"] | None

rootlogger: Any

def class_logger(cls: _ClsT) -> _ClsT: ...

class Identified:
    logging_name: str | None

class InstanceLogger:
    echo: _EchoFlag
    logger: Logger
    def __init__(self, echo: _EchoFlag, name: str | None) -> None: ...
    def debug(self, msg, *args, **kwargs) -> None: ...
    def info(self, msg, *args, **kwargs) -> None: ...
    def warning(self, msg, *args, **kwargs) -> None: ...
    warn = warning
    def error(self, msg, *args, **kwargs) -> None: ...
    def exception(self, msg, *args, **kwargs) -> None: ...
    def critical(self, msg, *args, **kwargs) -> None: ...
    def log(self, level, msg, *args, **kwargs) -> None: ...
    def isEnabledFor(self, level): ...
    def getEffectiveLevel(self): ...

def instance_logger(instance: Identified, echoflag: _EchoFlag = ...) -> None: ...

class echo_property:
    __doc__: str
    @overload
    def __get__(self, instance: None, owner: object) -> Self: ...
    @overload
    def __get__(self, instance: Identified, owner: object) -> _EchoFlag: ...
    def __set__(self, instance: Identified, value: _EchoFlag) -> None: ...
