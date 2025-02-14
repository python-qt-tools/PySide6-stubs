
from typing import Callable, TypeVar, Type, overload, Any, TYPE_CHECKING

from PySide6.QtCore import Slot, QObject

some_str: str
some_int: int

class SomeClass1(QObject):
    @Slot(int)
    def f_int_returns_str1(self, i: int) -> str:
        return 'abc'

sc1 = SomeClass1()
some_str = sc1.f_int_returns_str1(33)
some_int = sc1.f_int_returns_str1(33)      # type: ignore[assignment]
some_str = sc1.f_int_returns_str1('abc')   # type: ignore[arg-type]

class SomeClass2(QObject):
    @Slot(int, result=str)
    def f_int_returns_str2(self, i: int) -> str:
        return 'abc'

sc2 = SomeClass2()
some_str = sc2.f_int_returns_str2(33)
some_int = sc2.f_int_returns_str2(33)      # type: ignore[assignment]


class SomeClass3(QObject):
    @Slot(int, result=int)            # type: ignore[arg-type]
    def f_int_returns_str3(self, i: int) -> str:
        return 'abc'

    @Slot(int, float)
    def f_int_float_returns_str1(self, i: int, f: float) -> str:
        return 'abc'

sc3 = SomeClass3()
some_str = sc3.f_int_float_returns_str1(33, 1.0)
some_int = sc3.f_int_float_returns_str1(33, 1.0)      # type: ignore[assignment]
some_str = sc3.f_int_float_returns_str1('abc', 1.0)   # type: ignore[arg-type]
some_str = sc3.f_int_float_returns_str1(33, 'abc')   # type: ignore[arg-type]

class SomeClass4(QObject):
    @Slot(int, float, result=int)   # type: ignore[arg-type]
    def f_int_float_returns_str2(self, i: int, f: float) -> str:
        return 'abc'


    @Slot(int, float, str)
    def f_int_float_str_returns_str1(self, i: int, f: float, s: str) -> str:
        return 'abc'

sc4 = SomeClass4()
some_str = sc4.f_int_float_str_returns_str1(33, 1.0, 'abc')
some_int = sc4.f_int_float_str_returns_str1(33, 1.0, 'abc')      # type: ignore[assignment]
some_str = sc4.f_int_float_str_returns_str1('abc', 'abc', 33)   # type: ignore[arg-type]

class SomeClass5(QObject):
    @Slot(int, float, str, result=float)        # type: ignore[arg-type]
    def f_int_float_str_returns_str2(self, i: int, f: float, s: str) -> str:
        return 'abc'


    @Slot(int, float, str, int)
    def f_int_float_str_int_returns_str1(self, i: int, f: float, s: str, i2: int) -> str:
        return 'abc'

sc5 = SomeClass5()
some_str = sc5.f_int_float_str_int_returns_str1(33, 1.0, 'abc', 33)
some_int = sc5.f_int_float_str_int_returns_str1(33, 1.0, 'abc', 33)      # type: ignore[assignment]
some_str = sc5.f_int_float_str_int_returns_str1(33, 1.0, 'abc', 'abc')   # type: ignore[arg-type]

class SomeClass6(QObject):
    @Slot(int, float, str, int, result=float)        # type: ignore[arg-type]
    def f_int_float_str_int_returns_str2(self, i: int, f: float, s: str, i2: int) -> str:
        return 'abc'

    @Slot(int, float, str, float, result=str)        # type: ignore[arg-type]
    def f_int_float_str_int_returns_str3(self, i: int, f: float, s: str, i2: int) -> str:
        return 'abc'

    @Slot(int, float, str, int, bytes)
    def f_int_float_str_int_bytes_returns_str1(self, i: int, f: float, s: str, i2: int, b: bytes) -> str:
        return 'abc'

sc6 = SomeClass6()
some_str = sc6.f_int_float_str_int_bytes_returns_str1(33, 1.0, 'abc', 33, b'12')
some_int = sc6.f_int_float_str_int_bytes_returns_str1(33, 1.0, 'abc', 33, b'12')      # type: ignore[assignment]
some_str = sc6.f_int_float_str_int_bytes_returns_str1(33, 1.0, 'abc', 33, 'abc')   # type: ignore[arg-type]

class SomeClass7(QObject):
    @Slot(int, float, str, int, bytes, result=float)        # type: ignore[arg-type]
    def f_int_float_str_int_bytes_returns_str2(self, i: int, f: float, s: str, i2: int, b: bytes) -> str:
        return 'abc'

    @Slot(int, float, str, float, bytes, result=str)        # type: ignore[arg-type]
    def f_int_float_str_int_bytes_returns_str3(self, i: int, f: float, s: str, i2: int, b: bytes) -> str:
        return 'abc'

    # For 6 arguments, it still works without the result argument
    @Slot(int, float, str, int, bytes, float)
    def f_int_float_str_int_bytes_float_returns_str(self, i: int, f: float, s: str, i2: int, b1: bytes, f2: float) -> str:
        return 'abc'


sc7 = SomeClass7()
some_str = sc7.f_int_float_str_int_bytes_float_returns_str(33, 1.0, 'abc', 33, b'12', 1.0)
some_int = sc7.f_int_float_str_int_bytes_float_returns_str(33, 1.0, 'abc', 33, b'12', 1.0)      # type: ignore[assignment]
some_str = sc7.f_int_float_str_int_bytes_float_returns_str(33, 1.0, 'abc', 33, 'abc', 'abc')   # type: ignore[arg-type]

class SomeClass8(QObject):
    # For 6 arguments, with the result argument, arguments are no longer type-checked.
    @Slot(int, float, str, int, bytes, float, result=str)
    def f_int_float_str_int_bytes_float_returns_str2(self, s: str) -> str:
        return 'abc'

sc8 = SomeClass8()
# but return value is still type-checked
some_int = sc8.f_int_float_str_int_bytes_float_returns_str2('abc')      # type: ignore[assignment]






