from typing import TYPE_CHECKING

from PySide6.QtWidgets import QInputDialog

text: str
int_value: int
float_value: float

if TYPE_CHECKING:
    text, ok = QInputDialog.getText(
        None,
        "Title",
        "Please enter some value:",
    )

    text, ok = QInputDialog.getMultiLineText(
        None,
        "Title",
        "Please enter some value:",
    )

    text, ok = QInputDialog.getItem(
        None,
        "Title",
        "Please enter some value:",
        ['aaaa', 'bbbb', 'cccc']
    )

    int_value, ok = QInputDialog.getInt(
        None,
        "Title",
        "Please enter some value:",
    )

    float_value, ok = QInputDialog.getDouble(
        None,
        "Title",
        "Please enter some value:",
    )
