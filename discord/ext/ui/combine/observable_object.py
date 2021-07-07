from typing import List, Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from ..view import View


class ObservableObject:
    def __init__(self) -> None:
        self._watch_variables: List[str] = []
        self.view: Optional['View'] = None

    def notify(self) -> None:
        """
        update view
        :return: None
        """
        print('view_is_not_none', self.view is not None)
        if self.view is not None:
            self.view.update_sync()
