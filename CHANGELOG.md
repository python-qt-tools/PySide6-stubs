

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

