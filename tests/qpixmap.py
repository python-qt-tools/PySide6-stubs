from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

emptyPixmap = QPixmap(16, 16)
emptyPixmap.fill(Qt.GlobalColor.transparent)
emptyPixmap.fill('white')
emptyPixmap.fill(0xFFFFFF)
