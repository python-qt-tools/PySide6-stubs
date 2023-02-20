from typing import Any, cast, overload

from PySide6.QtWidgets import QApplication

def slotAppStateChanged(*args: Any) -> None:
    pass

def slotFocusChanged(*args: Any) -> None:
    pass

app = cast(QApplication, QApplication.instance())
app.applicationStateChanged.connect(slotAppStateChanged)
app.focusChanged.connect(slotFocusChanged)
QApplication.processEvents()

# deactivated because of mypy bug: https://github.com/python/mypy/issues/7781
# app.processEvents()
