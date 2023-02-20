import typing

from PySide6.QtCore import Signal, QObject


class SomeClassWithSignal(QObject):
    signal_no_arg = Signal()        # type: typing.ClassVar[Signal]
    signal_str    = Signal(str)     # type: typing.ClassVar[Signal]


    def __init__(self) -> None:
        super().__init__()  # note: this is mandatory for mypy to pickup the class attribute access

    def my_slot_no_arg(self) -> None:
        pass

    def my_slot_str(self, msg: str) -> None:
        pass


instance = SomeClassWithSignal()

connection = True
connection = instance.signal_no_arg.connect(instance.my_slot_no_arg)
instance.signal_no_arg.emit()

connection = instance.signal_str.connect(instance.my_slot_str)
instance.signal_str.emit('toto')


# instance.signal.disconnect(connection)

# SomeClassWithSignal.signal.__get__
# instance.signal[str].emit
