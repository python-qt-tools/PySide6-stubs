from PySide6.QtGui import QRegularExpressionValidator, QValidator


v = QRegularExpressionValidator()

valid_info: tuple[QValidator.State, str, int] = v.validate("", 0)
assert isinstance(valid_info, tuple)
assert isinstance(valid_info[0], QValidator.State)
assert isinstance(valid_info[1], str)
assert isinstance(valid_info[2], int)
