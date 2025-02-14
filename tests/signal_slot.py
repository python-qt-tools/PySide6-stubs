from typing import List, ClassVar, TYPE_CHECKING

from PySide6.QtCore import Signal, QObject, QMetaObject, SIGNAL, SLOT, Qt
from PySide6.QtWidgets import QScrollBar


class SomeClassWithSignal(QScrollBar):
    signal_no_arg = Signal()        # type: ClassVar[Signal]
    signal_str    = Signal(str)     # type: ClassVar[Signal]
    signal_int    = Signal(int)     # type: ClassVar[Signal]


    def __init__(self) -> None:
        super().__init__()  # note: this is mandatory for mypy to pickup the class attribute access
        self._emitted: List[str] = []

    def my_slot_no_arg(self) -> None:
        print('my_slot_no_arg')
        self._emitted.append('my_slot_no_arg')

    def my_slot_str(self, msg: str) -> None:
        print(f'my_slot_str({msg})')
        self._emitted.append('my_slot_str')

    def my_slot_int(self, value: int) -> None:
        print(f'my_slot_int({value})')
        self._emitted.append('my_slot_int')

    @property
    def emitted(self) -> List[str]:
        ret = self._emitted[:]
        self._emitted = []
        return ret


b: bool
s: str

s = SIGNAL('valueChanged(int)')
assert type(s) == str
s = SLOT('valueChanged(int)')
assert type(s) == str

instance = SomeClassWithSignal()

# Connect using the signal
connection: QMetaObject.Connection
connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
assert type(connection) == QMetaObject.Connection

instance.signal_no_arg.emit()
assert instance.emitted == ['my_slot_no_arg']

# Disconnect
b = instance.signal_no_arg.disconnect(instance.my_slot_no_arg)
assert type(b) is bool
instance.signal_no_arg.emit()
assert instance.emitted == []

# Connect through QObject static method, using SIGNAL()/SLOT() functions
connection = QObject.connect(instance, SIGNAL('valueChanged(int)'), instance, SLOT('my_slot_int(int)'), Qt.ConnectionType.DirectConnection)
try:
    connection = QObject.connect(instance, b'valueChanged(int)', instance, b'my_slot_int(int)', Qt.ConnectionType.DirectConnection) # type: ignore[call-overload]
    assert False, 'We thought that bytes were not supported'
except ValueError:
    pass
assert type(connection) == QMetaObject.Connection
instance.valueChanged.emit(33)
assert instance.emitted == ['my_slot_int']

# disconnect
b = instance.valueChanged.disconnect(instance.my_slot_int)
assert type(b) is bool
assert b
instance.valueChanged.emit(33)
assert instance.emitted == []


# Connect through QObject static method, using SIGNAL + python functions
connection = QObject.connect(instance, SIGNAL('valueChanged(int)'), instance.my_slot_int, Qt.ConnectionType.DirectConnection)
assert type(connection) == QMetaObject.Connection
instance.valueChanged.emit(33)
assert instance.emitted == ['my_slot_int']

# disconnect
b = instance.valueChanged.disconnect(instance.my_slot_int)
assert type(b) is bool
assert b
instance.valueChanged.emit(33)
assert instance.emitted == []

# Connect through QObject instance method, using SIGNAL + python functions
connection = instance.connect(SIGNAL('valueChanged(int)'), instance.my_slot_int, Qt.ConnectionType.DirectConnection)
assert type(connection) == QMetaObject.Connection
instance.valueChanged.emit(33)
assert instance.emitted == ['my_slot_int']

# disconnect
b = instance.valueChanged.disconnect(instance.my_slot_int)
assert type(b) is bool
assert b
instance.valueChanged.emit(33)
assert instance.emitted == []

# Connect through QObject instance method, to another signal
connection = QObject.connect(instance, SIGNAL('signal_int(int)'), instance, SIGNAL('valueChanged(int)'), Qt.ConnectionType.DirectConnection)
assert type(connection) == QMetaObject.Connection
connection = instance.connect(SIGNAL('valueChanged(int)'), instance.my_slot_int, Qt.ConnectionType.DirectConnection)
assert type(connection) == QMetaObject.Connection
instance.signal_int.emit(33)
assert instance.emitted == ['my_slot_int']

# disconnect
b = instance.valueChanged.disconnect(instance.my_slot_int)
assert type(b) is bool
assert b
b = instance.signal_int.disconnect(instance.valueChanged)
assert type(b) is bool
assert b
instance.signal_int.emit(33)
assert instance.emitted == []


# disconnect by signal + function
connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
b = instance.signal_no_arg.disconnect(instance.my_slot_no_arg)
assert type(b) is bool
assert b

# disconnect by signal + QMetaObject.Connection
connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
b = instance.signal_no_arg.disconnect(connection)
assert type(b) is bool
assert b

# disconnect by instance + SIGNAL() + function
connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
b = instance.disconnect(SIGNAL('signal_no_arg()'), instance.my_slot_no_arg)
assert type(b) is bool
assert b

# disconnect by instance + receiver + SLOT()
connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
b = instance.disconnect(instance, SLOT('my_slot_no_arg()'))
assert type(b) is bool
assert b

# disconnect by instance + SIGNAL() + receiver + SLOT()
connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
b = instance.disconnect(SIGNAL('signal_no_arg()'), instance, SLOT('my_slot_no_arg()'))
assert type(b) is bool
assert b

# disconnect by class + QMetaObject.Connection
connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
b = SomeClassWithSignal.disconnect(connection)
assert type(b) is bool
assert b

# disconnect by class + instance + SIGNAL() + function
connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
b = SomeClassWithSignal.disconnect(instance, SIGNAL('signal_no_arg()'), instance.my_slot_no_arg)
assert type(b) is bool
assert b

# disconnect by class + instance + SIGNAL() + receiver + SLOT
connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
b = SomeClassWithSignal.disconnect(instance, SIGNAL('signal_no_arg()'), instance, SLOT('my_slot_no_arg()'))
assert type(b) is bool
assert b

connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
r = 33
r = instance.receivers(SIGNAL('signal_no_arg()'))
assert type(r) is int
