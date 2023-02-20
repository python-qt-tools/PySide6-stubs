from typing import Callable

from PySide6.QtWidgets import QMessageBox, QWidget

multiple_buttons = QMessageBox.StandardButton(0)
multiple_buttons = (QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Ok)
multiple_buttons = QMessageBox.StandardButton.Ok | 0
multiple_buttons = multiple_buttons | 0
multiple_buttons = (multiple_buttons | QMessageBox.StandardButton.Ok)
multiple_buttons = multiple_buttons | multiple_buttons
multiple_buttons = QMessageBox.StandardButton(44)
multiple_buttons = QMessageBox.StandardButton(QMessageBox.StandardButton.Ok)
multiple_buttons = QMessageBox.StandardButton(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Ok)

one_button = QMessageBox.StandardButton.Ok   # type: QMessageBox.StandardButton
one_button = QMessageBox.StandardButton(44)
one_button = QMessageBox.StandardButton(QMessageBox.StandardButton.Ok)

my_warning = QMessageBox.warning # type: Callable[[QWidget, str, str], QMessageBox.StandardButton]
