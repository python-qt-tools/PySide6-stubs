
PySide6 has made great progresses over the year on typing. This file lists the remaining issues 
and their status in Qt bugtracker.


Reported issues
===============
* [PYSIDE-3034 - Typing: stubs are missing public variables](https://bugreports.qt.io/browse/PYSIDE-3034)
* [PYSIDE-3037 - Typing: allow QByteArray to convert to bytes](https://bugreports.qt.io/browse/PYSIDE-3037)
* [PYSIDE-3038 - Typing: QDateTime accepts python datetime objects](https://bugreports.qt.io/browse/PYSIDE-3038)
* [PYSIDE-3039 - Typing: QHBoxLayout does not accept None as parent](https://bugreports.qt.io/browse/PYSIDE-3039)
* [PYSIDE-3043 - Typing: QMessageBox static methods should support parent = None](https://bugreports.qt.io/browse/PYSIDE-3043)
* [PYSIDE-3046 - Typing: bad type signature for QObject.inherits()](https://bugreports.qt.io/browse/PYSIDE-3046)
* [PYSIDE-3047 - Typing: fix QPolygon << operator](https://bugreports.qt.io/browse/PYSIDE-3047)
* [PYSIDE-3048 - Typing: use IntEnum instead of enum](https://bugreports.qt.io/browse/PYSIDE-3048)
* [PYSIDE-3050 - Typing: QProgressDialog.setCancelButton() should accept None](https://bugreports.qt.io/browse/PYSIDE-3050)
* [PYSIDE-3051 - Typing: support more scalar operators for QSize and QSizeF](https://bugreports.qt.io/browse/PYSIDE-3051)
* [PYSIDE-3055 - Typing: QTabBar.setTabButton() should accept None](https://bugreports.qt.io/browse/PYSIDE-3055)
* [PYSIDE-3056 - Typing: qtTrId() argument should be string](https://bugreports.qt.io/browse/PYSIDE-3056)
* [PYSIDE-3057 - Typing: QTreeWidget.setItemWidget() accepts None](https://bugreports.qt.io/browse/PYSIDE-3057)
* [PYSIDE-3058 - Typing: QTredWidget.topLevelItem() may return None](https://bugreports.qt.io/browse/PYSIDE-3058)
* 

Fixed issues
============
* [PYSIDE-3045 - Typing: QObject.findChildren() and findChild() need typing improvements](https://bugreports.qt.io/browse/PYSIDE-3045)
* [PYSIDE-3044 - Typing: QMessageBox.information() should have a default button](https://bugreports.qt.io/browse/PYSIDE-3044)
* [PYSIDE-3042 - Typing: QListWidget.setItemWidget() accepts None](https://bugreports.qt.io/browse/PYSIDE-3042)
* [PYSIDE-3041 - Typing: QLineEdit.setText() accepts None](https://bugreports.qt.io/browse/PYSIDE-3041)
* [PYSIDE-3036 - Typing: QModelIndex.constInternalPointer() should return Any](https://bugreports.qt.io/browse/PYSIDE-3036)
* fix incorrect signature of `QCoreApplication.translate()`
* add all missing signals to the stubs (many were missing)
* fix `QStateMachine.assignProperty()` type signature
* add typing information for all properties
