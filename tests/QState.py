from PySide6.QtCore import QObject
from PySide6.QtStateMachine import QState


b = QObject()

s = QState()
s.assignProperty(b,"string",True)
