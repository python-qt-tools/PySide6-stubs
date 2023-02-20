from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QUrl


def call_me() -> None:
    fname, filter = '', ''
    fnames = ['', '']

    fname, filter = QFileDialog.getOpenFileName(None, caption='caption', dir='dir', filter='filter', selectedFilter='abc')
    fnames, filter = QFileDialog.getOpenFileNames(None, caption='caption', dir='dir', filter='filter', selectedFilter='abc')
    fname, filter = QFileDialog.getSaveFileName(None, caption='caption', dir='dir', filter='filter', selectedFilter='abc')

    fname, filter = QFileDialog.getOpenFileUrl(None, caption='caption', dir=QUrl(), filter='filter',
                                                selectedFilter='abc', supportedSchemes=['file', 'http'])
    fnames, filter = QFileDialog.getOpenFileUrls(None, caption='caption', dir=QUrl(), filter='filter',
                                               selectedFilter='abc', supportedSchemes=['file', 'http'])
    fname, filter = QFileDialog.getSaveFileUrl(None, caption='caption', dir=QUrl(), filter='filter',
                                               selectedFilter='abc', supportedSchemes=['file', 'http'])



# Enable me if you are ready to click 5 times on the dialog
# call_me()