from typing import Optional, List

from discord import ui

from .item import Item
from .select_option import SelectOption


class CustomSelect(ui.Select):
    pass


class Select(Item):
    def __init__(
            self,
            placeholder: Optional[str] = None,
            min_values: int = 1,
            max_values: int = 1,
            options: Optional[list] = None
    ):
        self._placeholder = placeholder
        self._min_values = min_values
        self._max_values = max_values
        self._options = [] if options is None else options
        self._group = None

    def placeholder(self, placeholder: str) -> 'Select':
        self._placeholder = placeholder
        return self

    def min_values(self, min_values: int) -> 'Select':
        self._min_values = min_values
        return self

    def max_values(self, max_values: int) -> 'Select':
        self._max_values = max_values
        return self

    def options(self, options: List[SelectOption]):
        self._options = options
        return self

    def to_discord(self):
        return CustomSelect(
            placeholder=self._placeholder,
            min_values=self._min_values,
            max_values=self._max_values,
            options=[o.to_discord_select_option() for o in self._options],
            group=self._group
        )
