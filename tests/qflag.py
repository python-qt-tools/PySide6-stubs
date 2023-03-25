
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDialog

# I need to run this script manually to verify it works
if __name__ == '__main__':
    app = QApplication([])

w = QDialog()
w.setWindowFlags(w.windowFlags() | Qt.WindowType.WindowContextHelpButtonHint)
w.setWindowFlags(Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowContextHelpButtonHint)
w.setWindowFlags(Qt.WindowType.WindowContextHelpButtonHint)
w.setWindowFlag(Qt.WindowType.WindowContextHelpButtonHint)

try:
    w.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowContextHelpButtonHint)
except TypeError:
    pass

if __name__ == '__main__':
    w.show()
    app.exec()


