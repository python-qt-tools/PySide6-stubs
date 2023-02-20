

Version 6.4.2.0 (to be released)
===============
* add all missing signals to the stubs (many were missing)
* add conversion from `QByteArray` to bytes
* add construction of `QByteArray` from length and string




To be released
==============
* fix `QTabBar.setButtonWidget()` to accept `None` as a widget argument
* fix `QTreeWidget.setItemWidget()`  and `QListWidget.setItemWidget()` to accept `None` as a widget argument


Version 5.15.2.1.2:
===================
Many core improvements over previous version

* uses automatic code transforms from libcst to update all stubs at once
* add all missing signals to the stubs (many were missing)
* incorrect methods names are no longer silently ignored
* fix all QFlags values incorrectly declared as the QFlag wrapping class
* fix all method accepting a `QCursor` to accept also a `Qt.CursorShape`
* add `exec()` to QDialog
* fix `data()` and `setData()` to accept Qt.ItemDataRole
* add all method for operations on QFlag: `__or__`, `__xor__`, ...
* fix all method accepting a QColor to accept also a `Qt.GlobalColor`
* fix signature of `QCoreApplication.translate()`
* fix `QLabel.setAlignment()` to accept also Qt.AlignmentFlag


Version 5.15.2.1.0:
===================
Initial release for PySide2 v5.15.2.1

* fix `Signal` to make it accept method emit()
* fix `qVersion()` returns string, not bytes
* fix `QMessageBox.warning`, information, critical, question, about, aboutQt to accept None as parent argument
* fix `QProgressDialog.setCancelButton()` accepting None
* fix `QTreeWidget.topLevelItem()` returning possibly None
* fix `QMessageBox.StandardButton` or combinations
* fix `QProcess.ExitStatus` enum conversion to int
* fix `QAction.setShortcut()` to accept string as argument
* fix `QTreeWidgetItem` comparison with `<` 
* fix `Signal.connect()` return value to bool instead of None
* fix `QTimer.timeout` undeclared signal
* support all `QSize` and `QSizeF` operations
* improve signature of operations on `QPolygon`
* improve `QPainter` methods which use lists of `QPoint` in entry
* improve `QObject.findChildren()` type information
* fix `QLineEdit.setText()` to accept None
* add `QDialogButtonBox.StandardButton` `__or__` operations
* fix `Slot()` argument and return value type-checking
* fix missing methods being undetected for all Qt objects
* add platform-specific stubs: QMacExtras, QWinExtras, QX11Extras
