from typing import Callable
from PySide6.QtWidgets import QMessageBox, QWidget

my_msgbox_function: Callable[[QWidget, str, str, QMessageBox.StandardButton, QMessageBox.StandardButton], QMessageBox.StandardButton]
my_msgbox_function = QMessageBox.warning
my_msgbox_function = QMessageBox.information
my_msgbox_function = QMessageBox.critical
my_msgbox_function = QMessageBox.question

my_about_qt: Callable[[None, str], None]
my_about_qt = QMessageBox.aboutQt
my_about: Callable[[None, str, str], None]
my_about = QMessageBox.about

QMessageBox.information(None, 'info', 'info')
QMessageBox.warning(None, 'warning', 'warning')
QMessageBox.critical(None, 'critical', 'critical')
QMessageBox.question(None, 'question', 'question')
QMessageBox.about(None, 'about', 'about')
QMessageBox.aboutQt(None, 'aboutQt')
