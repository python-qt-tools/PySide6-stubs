

Version 6.7.3.0 
==============
* Synchronize stubs with upstream PySide6 6.7.3
* add typing information for all properties
* Allow `QGridLayout`, `QHBoxLayout` and `QVBoxLayout` to accept parent as None
* Make `QtCore.Slot()` verify its arguments and return value
* fix `QObject.inherits()` type signature to accept string
* fix `QStateMachine.assignProperty()` type signature
* fix `QObject.findChildren()` and `QObject.findChild()` to detect that type being returned is the one being searched
* fix many methods in QtCore incorrectly declared to accept bytes instead of string, like `QTimer.singleShot()`
* fix `QColumnView`, `QHeaderView`, `QTreeView` and more to accept None as model argument in `setModel()`
* allow `QProcess.ExitStatus.NormalExit.value` to be seen as `int`

Version 6.4.2.0 
===============
* add all missing signals to the stubs (many were missing)
* add conversion from `QByteArray` to `bytes`
* add construction of `QByteArray` from length and string
* fix `QFileDialog.getOpen*()` methods to accept `None` as parent argument
* fix `QLineEdit.setText()` to accept `None`
* fix `QTreeWidget.setItemWidget()` and `QListWidget.setItemWidget()` to accept `None` as a widget argument
* fix `QProgressDialog.setCancelButton()` accepting `None`
* support all `QSize` and `QSizeF` operations
* fix `QTabBar.setButtonWidget()` to accept `None` as a widget argument
* fix `QTreeWidget.topLevelItem()` returning possibly `None`
* fix `QTreeWidgetItem` comparison with `<`
* fix `QMessageBox.warning`, `information`, `critical`, `question`, `about`, `aboutQt` to accept `None` as parent argument
* fix `qVersion()` returns string, not bytes
* fix `qDebug()`, `qWarning()`, `qCritical()`, `qFatal()`, `SIGNAL()`, `SLOT()` to accept string, not bytes
* fix `Signal.connect()`, `Signal.disconnect()`, `QObject.connect()` and `QObject.disconnect()` to accept `str` instead
  of `bool`, and to return `bool` on disconnect.
* fix incorrect signature of `QCoreApplication.translate()`
* improve signature of operations on `QPolygon`

