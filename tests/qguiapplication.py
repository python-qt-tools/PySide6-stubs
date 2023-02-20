from typing import cast

from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import Qt

app = cast(QGuiApplication, QGuiApplication.instance())
app.setOverrideCursor(Qt.CursorShape.WaitCursor)
