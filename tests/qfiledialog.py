from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QUrl


def call_me() -> None:
    fname, filter = '',  ''
    fnames = ['', '']

    url = QUrl()
    urls = [url]

    fname, filter = QFileDialog.getOpenFileName(None, caption='getOPenFileName')
    assert type(fname) == str
    assert type(filter) == str

    fnames, filter = QFileDialog.getOpenFileNames(None, caption='getOpenFileNames')
    assert type(fnames) == list
    assert len(fnames) >= 1
    assert type(fnames[0]) == str
    assert type(filter) == str

    fname, filter = QFileDialog.getSaveFileName(None, caption='getSaveFileName')
    assert type(fname) == str
    assert type(filter) == str

    url, filter = QFileDialog.getOpenFileUrl(None, caption='getOpenFileUrl')
    assert type(url) == QUrl
    assert type(filter) == str

    urls, filter = QFileDialog.getOpenFileUrls(None, caption='getOpenFileUrls')
    assert type(urls) == list
    assert len(urls) >= 1
    assert type(urls[0]) == QUrl
    assert type(filter) == str

    url, filter = QFileDialog.getSaveFileUrl(None, caption='getSaveFileUrl')
    assert type(url) == QUrl
    assert type(filter) == str




# Enable me if you are ready to click 5 times on the dialog
call_me()