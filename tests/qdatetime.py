from datetime import datetime
from PySide6.QtCore import QDateTime, QDate

dt = datetime(2000,1,1)
QDateTime(dt)
QDate(dt)
QDate(dt.date())
