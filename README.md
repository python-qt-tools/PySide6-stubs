<img src="http://mypy-lang.org/static/mypy_light.svg" alt="mypy logo" width="300px"/>


# Mypy stubs for the PySide6 (Qt6 for Python)

*Author :* Philippe Fremy

This package provides improved typing stubs for [Qt6 for Python/PySide6](https://pypi.org/project/PySide6/). The 
official stubs delivered along with PySide6 are insufficent 
for proper typing verification with `mypy`.

### Notable improvements:
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


See [CHANGELOG.md](CHANGELOG.md) for full details.

This effort was inspired by the PyQt5-stubs and PySide2-stubs project.

Please note that this work is far from complete. Don't hesitate to report problems or propose improvements.


# Licensing
As a derived work from PySide6, the stubs are delivered under the LGPL v2.1 . See file LICENSE for more details.


# Installation

Today, this work exists only inside the Git repository. So the installation command is:

    $ pip install git+https://github.com/python-qt-tools/PySide6-stubs

As soon as a Python pip package is created, this will be reflected in the recommendations here.


# Help improve the stubs

If you notice incorrect or missing typing information (mypy reports errors eventhough your code is correct), please report it
here with the following steps:

* create an issue showing your problem
* even better, create a PR to fix the problem. See CONTRIBUTING.md for details.


