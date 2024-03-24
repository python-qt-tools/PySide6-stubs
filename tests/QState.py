from PySide6.QtCore import QObject
from PySide6.QtStateMachine import QState, QFinalState


b = QObject()



s = QState()
### Note: this seems to be a Qt bug that this is not supported
s.assignProperty(b,"string", True)

abst = QFinalState()
### Note: this seems to be a Qt bug that this is not supported
# s.addTransition(b,'string', abst)

try:
    ### Note: this seems to be a Qt bug that this is not supported
    s.assignProperty(b, b'bytes', True) # type: ignore[arg-type]
    assert False, 'ValueError should have been raised'
    pass
except (ValueError, TypeError):
    # good, we get confirmation that string is the right type
    pass


try:
    ### Note: this seems to be a Qt bug that this is not supported
    s.addTransition(b, b'bytes', abst) # type: ignore[call-overload]
    assert False, 'ValueError should have been raised'
    pass
except (ValueError, TypeError):
    # good, we get confirmation that string is the right type
    pass

