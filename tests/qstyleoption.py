from PySide6.QtWidgets import QStyleOption, QStyle
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QFontMetrics, QPalette


direction: Qt.LayoutDirection
fontMetrics: QFontMetrics
palette: QPalette
rect: QRect
state: QStyle.StateFlag
t: int

so = QStyleOption()
direction = so.direction
fontMetrics = so.fontMetrics
palette = so.palette
rect = so.rect
state = so.state
t = so.type

