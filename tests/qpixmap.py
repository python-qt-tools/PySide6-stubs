from PySide6.QtCore import QByteArray, Qt
from PySide6.QtGui import QPixmap

emptyPixmap = QPixmap(16, 16)
emptyPixmap.fill(Qt.GlobalColor.transparent)
emptyPixmap.fill('white')
emptyPixmap.fill(0xFFFFFF)

# Should accept str for format
worlds_smallest_png = QByteArray.fromBase64(b"iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQAAAAA3bvkkAAAACklEQVR4AWNgAAAAAgABc3UBGAAAAABJRU5ErkJggg==")
load_pixmap = QPixmap()
load_pixmap.loadFromData(worlds_smallest_png, "PNG")
