# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtWebEngineWidgets, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtWebEngineWidgets`

import PySide6.QtWebEngineWidgets
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import PySide6.QtPrintSupport
import PySide6.QtWebEngineCore

from typing import Optional, Union, overload


class QIntList(object): ...


class QWebEngineView(PySide6.QtWidgets.QWidget):

    @overload
    def __init__(self, page: PySide6.QtWebEngineCore.QWebEnginePage, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...
    @overload
    def __init__(self, profile: PySide6.QtWebEngineCore.QWebEngineProfile, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...

    def back(self) -> None: ...
    def closeEvent(self, arg__1: PySide6.QtGui.QCloseEvent) -> None: ...
    def contextMenuEvent(self, arg__1: PySide6.QtGui.QContextMenuEvent) -> None: ...
    def createStandardContextMenu(self) -> PySide6.QtWidgets.QMenu: ...
    def createWindow(self, type: PySide6.QtWebEngineCore.QWebEnginePage.WebWindowType) -> PySide6.QtWebEngineWidgets.QWebEngineView: ...
    def dragEnterEvent(self, e: PySide6.QtGui.QDragEnterEvent) -> None: ...
    def dragLeaveEvent(self, e: PySide6.QtGui.QDragLeaveEvent) -> None: ...
    def dragMoveEvent(self, e: PySide6.QtGui.QDragMoveEvent) -> None: ...
    def dropEvent(self, e: PySide6.QtGui.QDropEvent) -> None: ...
    def event(self, arg__1: PySide6.QtCore.QEvent) -> bool: ...
    @overload
    def findText(self, arg__1: str, arg__2: PySide6.QtWebEngineCore.QWebEnginePage.FindFlag, arg__3: object) -> None: ...
    @overload
    def findText(self, subString: str, options: PySide6.QtWebEngineCore.QWebEnginePage.FindFlag = ...) -> None: ...
    @staticmethod
    def forPage(page: PySide6.QtWebEngineCore.QWebEnginePage) -> PySide6.QtWebEngineWidgets.QWebEngineView: ...
    def forward(self) -> None: ...
    def hasSelection(self) -> bool: ...
    def hideEvent(self, arg__1: PySide6.QtGui.QHideEvent) -> None: ...
    def history(self) -> PySide6.QtWebEngineCore.QWebEngineHistory: ...
    def icon(self) -> PySide6.QtGui.QIcon: ...
    def iconUrl(self) -> PySide6.QtCore.QUrl: ...
    def lastContextMenuRequest(self) -> PySide6.QtWebEngineCore.QWebEngineContextMenuRequest: ...
    @overload
    def load(self, request: PySide6.QtWebEngineCore.QWebEngineHttpRequest) -> None: ...
    @overload
    def load(self, url: Union[PySide6.QtCore.QUrl, str]) -> None: ...
    def page(self) -> PySide6.QtWebEngineCore.QWebEnginePage: ...
    def pageAction(self, action: PySide6.QtWebEngineCore.QWebEnginePage.WebAction) -> PySide6.QtGui.QAction: ...
    def print(self, printer: PySide6.QtPrintSupport.QPrinter) -> None: ...
    def printToPdf(self, filePath: str, layout: PySide6.QtGui.QPageLayout = ..., ranges: PySide6.QtGui.QPageRanges = ...) -> None: ...
    def reload(self) -> None: ...
    def selectedText(self) -> str: ...
    def setContent(self, data: Union[PySide6.QtCore.QByteArray, bytes], mimeType: str = ..., baseUrl: Union[PySide6.QtCore.QUrl, str] = ...) -> None: ...
    def setHtml(self, html: str, baseUrl: Union[PySide6.QtCore.QUrl, str] = ...) -> None: ...
    def setPage(self, page: PySide6.QtWebEngineCore.QWebEnginePage) -> None: ...
    def setUrl(self, url: Union[PySide6.QtCore.QUrl, str]) -> None: ...
    def setZoomFactor(self, factor: float) -> None: ...
    def settings(self) -> PySide6.QtWebEngineCore.QWebEngineSettings: ...
    def showEvent(self, arg__1: PySide6.QtGui.QShowEvent) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def stop(self) -> None: ...
    def title(self) -> str: ...
    def triggerPageAction(self, action: PySide6.QtWebEngineCore.QWebEnginePage.WebAction, checked: bool = ...) -> None: ...
    def url(self) -> PySide6.QtCore.QUrl: ...
    def zoomFactor(self) -> float: ...


# eof
