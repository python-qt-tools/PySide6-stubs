from PySide6 import QtCore

some_bytes = b'123'
some_bytearray = QtCore.QByteArray(3, 'a')
some_bytes = bytes(some_bytearray)


