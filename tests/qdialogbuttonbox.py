from PySide6 import QtWidgets

a: QtWidgets.QDialogButtonBox.StandardButton
a = (QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Ok)
d = (a | QtWidgets.QDialogButtonBox.StandardButton.Ok)  # type: QtWidgets.QDialogButtonBox.StandardButton
e = a | a  # type: QtWidgets.QDialogButtonBox.StandardButton
