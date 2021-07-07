from typing import Any, TypeVar

from .observable_object import ObservableObject

import logging  #  temporary
logger = logging.getLogger(__name__)

T = TypeVar('T')


def published(name: str):
    def getter(instance: T) -> Any:
        return instance.__dict__[name]

    def setter(instance: T, value: Any) -> None:
        instance.__dict__[name] = value
        if isinstance(instance, ObservableObject):
            print(f'set: {instance}\n{value}')
            instance.notify()

    return property(getter, setter)
