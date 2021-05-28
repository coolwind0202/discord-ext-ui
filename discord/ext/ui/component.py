from typing import Optional, List, Union

from discord import ui

from .item import Item


class Component:
    def __init__(self, items: Optional[List[Union[Item, List[Item]]]] = None) -> None:
        self.items = items

    def __eq__(self, other: 'Component'):
        return self.items == other.items

    def make_view(self) -> ui.View:
        view = ui.View(None)
        i = 0
        for item in self.items:
            if not isinstance(item, list):
                view.add_item(item.to_discord())
                continue
            for item_ in item:  # type: Item
                item_._group = i
                view.add_item(item_.to_discord())
            i += 1
        return view
