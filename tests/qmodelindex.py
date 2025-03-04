from PySide6.QtCore import QModelIndex

m = QModelIndex()

i: int
s: str

i = m.internalPointer()
s = m.internalPointer()

i = m.constInternalPointer()
s = m.constInternalPointer()