<img src="http://mypy-lang.org/static/mypy_light.svg" alt="mypy logo" width="300px"/>


# Mypy stubs for the PySide6 (Qt6 for Python)

*Author :* Philippe Fremy

This package provides improved typing stubs for [Qt6 for Python/PySide6](https://pypi.org/project/PySide6/). The 
official stubs delivered along with PySide6 are insufficent 
for proper typing verification with `mypy`.

### Notable improvements:
* fix `Signal` to make it accept method emit()
* fix `qVersion()` returns string, not bytes
* fix `QMessageBox.warning`, information, critical, question, about, aboutQt to accept None as parent argument
* fix `QProgressDialog.setCancelButton()` accepting None
* fix `QTreeWidgetItem` comparison with `<`
* fix `Signal.connect()` return value to bool instead of None
* fix `QTimer.timeout` undeclared signal
* support all `QSize` and `QSizeF` operations
* fix `QLineEdit.setText()` to accept None
* add `QDialogButtonBox.StandardButton` `__or__` operations
* fix missing methods being undetected for all Qt objects
* add all missing signals to the stubs (many were missing)
* fix all method accepting a `QCursor` to accept also a `Qt.CursorShape`
* add conversion from `QByteArray` to bytes
* add `exec()` to QDialog
* fix `data()` and `setData()` to accept Qt.ItemDataRole
* add all method for operations on QFlag derived classes: `__or__`, `__xor__`, ...
* fix all method accepting a QColor to accept also a `Qt.GlobalColor`
* fix signature of `QCoreApplication.translate()`
* fix `QLabel.setAlignment()` to accept also Qt.AlignmentFlag


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
* even better, create a PR to fix the problem
    * make sure to add a test showing what is mistyped. Just create a file under `tests/` , with a name
      not starting with *test*. The test suite will run the file and type-check it.
    * fix the stubs in the PySide2-stubs directory
    * and open the PR


