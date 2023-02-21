from typing import Callable, Union

from PySide6.QtCore import qVersion, qWarning, qCritical, qDebug, qFatal, SIGNAL, SLOT

s = ''  # type: str
s = qVersion()

def check_func_accepts_str_not_bytes(f: Union[Callable[[str], None], Callable[[str], str]]) -> None:
    f('toto')

    try:
        f(b'toto')  # type: ignore[arg-type]
        raise AssertionError()
    except ValueError:
        pass



check_func_accepts_str_not_bytes(qDebug)
check_func_accepts_str_not_bytes(qWarning)
check_func_accepts_str_not_bytes(qCritical)
# check_func_accepts_str_not_bytes(qFatal)
check_func_accepts_str_not_bytes(SIGNAL)
check_func_accepts_str_not_bytes(SLOT)

