from typing_extensions import override
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QLayout, QLayoutItem

a = QGridLayout(parent=None)
b = QHBoxLayout(parent=None)
c = QVBoxLayout(parent=None)

class TestLayout(QLayout):
    # These can return None
    @override
    def itemAt(self, index: int) -> 'QLayoutItem | None':
        return super().itemAt(index)
    
    @override
    def takeAt(self, index: int) -> 'QLayoutItem | None':
        return super().takeAt(index)

assert a.itemAt(0) is None
assert a.takeAt(0) is None
