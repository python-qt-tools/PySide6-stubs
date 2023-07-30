from typing import Any
from PySide6.QtWidgets import QMenu, QTreeWidget

# the default version of pyside2 stubs would not detect missing attributes
# this test verifies that this is fixed

class Toto(QTreeWidget):

    m: QMenu

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self.m = QMenu()

    def toto(self) -> None:
        try:
            self.m.exec()
            assert False, 'Should not reach here'
        except AttributeError:
            pass
        try:
            self.m.exec_()
            assert False, 'Should not reach here'
        except AttributeError:
            pass