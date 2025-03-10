from typing import List, Iterable, Optional

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget, QApplication

if __name__ == '__main__':
    app = QApplication([])

o1 = QWidget()
w2 = QWidget(o1)
o3 = QObject(o1)

### QObject.findChildren()

a: List[QObject]
a = o1.findChildren(QObject)
assert type(a) == list
assert isinstance(a[0], QObject)

b: List[QWidget]
b = o1.findChildren(QWidget)
assert type(b) == list
assert isinstance(b[0], QWidget)

# incorrect here, correctly detected by mypy
c: List[QWidget]
c = o1.findChildren(QObject, '')    # type: ignore[arg-type]

# cast works, List[QWidget] is a List[QObject]
d: List[QObject]
d = o1.findChildren(QWidget, '')


### QObject.findChild()
w3: Optional[QWidget] = None
w3 = o1.findChild(QWidget)

# incorrect here, correctly detected by mypy
w3 = o1.findChild(QObject)  # type: ignore[assignment]


### inherits and other methods

o1.inherits('toto')
try:
    o1.inherits(b'toto')    # type: ignore[arg-type]
    assert False, 'We expect bytes not to be supported...'
except ValueError:
    pass
o1.property('toto')
o1.setProperty('toto', True)
o1.tr('abc', 'def')
