from typing import List, Iterable

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget, QApplication

if __name__ == '__main__':
    app = QApplication([])

o1 = QWidget()
o2 = QWidget(o1)
o3 = QObject(o1)

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
c = o1.findChildren(QObject, '')

# cast works, List[QWidget] is a List[QObject]
d: List[QObject]
d = o1.findChildren(QWidget, '')

o1.inherits('toto')
o1.property('toto')
o1.setProperty('toto', True)
o1.tr('abc', 'def')
