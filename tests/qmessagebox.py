from typing import Callable

from PySide6.QtWidgets import QMessageBox

multiple_buttons = QMessageBox.StandardButtons()
multiple_buttons = (QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Ok)
multiple_buttons = QMessageBox.StandardButton.Ok | 0
multiple_buttons = multiple_buttons | 0
multiple_buttons = (multiple_buttons | QMessageBox.StandardButton.Ok)
multiple_buttons = multiple_buttons | multiple_buttons
multiple_buttons = QMessageBox.StandardButtons(44)
multiple_buttons = QMessageBox.StandardButtons(QMessageBox.StandardButton.Ok)
multiple_buttons = QMessageBox.StandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Ok)

one_button = QMessageBox.StandardButton.Ok   # type: QMessageBox.StandardButton
one_button = QMessageBox.StandardButton(44)
one_button = QMessageBox.StandardButton(QMessageBox.StandardButton.Ok)
one_button = QMessageBox.Ok


my_warning = QMessageBox.warning # type: Callable[[None, str, str], QMessageBox.StandardButton]
