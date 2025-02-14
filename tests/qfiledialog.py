from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QUrl


def call_me() -> None:
    fname, filter = '',  ''
    fnames = ['', '']

    url = QUrl()
    urls = [url]

    fname, filter = QFileDialog.getOpenFileName(None, caption='getOPenFileName')
    print(fname, filter)
    assert type(fname) == str
    assert type(filter) == str

    fnames, filter = QFileDialog.getOpenFileNames(None, caption='getOpenFileNames')
    print(fnames, filter)
    assert type(fnames) == list
    if fnames:
        assert type(fnames[0]) == str
    assert type(filter) == str

    fname, filter = QFileDialog.getSaveFileName(None, caption='getSaveFileName')
    print(fname, filter)
    assert type(fname) == str
    assert type(filter) == str

    url, filter = QFileDialog.getOpenFileUrl(None, caption='getOpenFileUrl')
    print(url, filter)
    assert type(url) == QUrl
    assert type(filter) == str

    urls, filter = QFileDialog.getOpenFileUrls(None, caption='getOpenFileUrls')
    print(urls, filter)
    assert type(urls) == list
    if urls:
        assert type(urls[0]) == QUrl
    assert type(filter) == str

    url, filter = QFileDialog.getSaveFileUrl(None, caption='getSaveFileUrl')
    print(url, filter)
    assert type(url) == QUrl
    assert type(filter) == str




# Enable me if you are ready to click 5 times on the dialog
# call_me()