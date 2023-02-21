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

my_msgbox_function: Callable[[None, str, str], QMessageBox.StandardButton]
my_msgbox_function = QMessageBox.warning
my_msgbox_function = QMessageBox.information
my_msgbox_function = QMessageBox.critical
my_msgbox_function = QMessageBox.question

my_about_qt: Callable[[None, str], None]
my_about_qt = QMessageBox.aboutQt
my_about: Callable[[None, str, str], None]
my_about = QMessageBox.about
