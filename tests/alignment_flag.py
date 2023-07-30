from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSpinBox, QFormLayout, QGraphicsView, QLineEdit, QLabel, QLayout, QLayoutItem, QProgressBar, \
    QScrollArea, QTextEdit

a = QSpinBox()
a.setAlignment(Qt.AlignmentFlag.AlignRight)

b = QGraphicsView()
b.setAlignment(Qt.AlignmentFlag.AlignRight)

l = QLabel()
l.setAlignment(Qt.AlignmentFlag.AlignRight)

d = QLineEdit()
d.setAlignment(Qt.AlignmentFlag.AlignRight)

pb = QProgressBar()
pb.setAlignment(Qt.AlignmentFlag.AlignRight)

sa = QScrollArea()
sa.setAlignment(Qt.AlignmentFlag.AlignRight)

te = QTextEdit()
te.setAlignment(Qt.AlignmentFlag.AlignRight)

fl = QFormLayout()
fl.setFormAlignment(Qt.AlignmentFlag.AlignRight)
fl.setAlignment(Qt.AlignmentFlag.AlignRight)
fl.setAlignment(fl, Qt.AlignmentFlag.AlignRight)
fl.setAlignment(b, Qt.AlignmentFlag.AlignRight)

