# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtPdfWidgets, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtPdfWidgets`

import PySide6.QtPdfWidgets
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import PySide6.QtPdf

import enum
from typing import ClassVar, overload
from PySide6.QtCore import Signal


NoneType = type(None)


class QIntList(object): ...


class QPdfPageSelector(PySide6.QtWidgets.QWidget):

    currentPageChanged       : ClassVar[Signal] = ... # currentPageChanged(int)
    currentPageLabelChanged  : ClassVar[Signal] = ... # currentPageLabelChanged(QString)
    documentChanged          : ClassVar[Signal] = ... # documentChanged(QPdfDocument*)

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget) -> None: ...

    def currentPage(self) -> int: ...
    def currentPageLabel(self) -> str: ...
    def document(self) -> PySide6.QtPdf.QPdfDocument: ...
    def setCurrentPage(self, index: int) -> None: ...
    def setDocument(self, document: PySide6.QtPdf.QPdfDocument) -> None: ...


class QPdfView(PySide6.QtWidgets.QAbstractScrollArea):

    currentSearchResultIndexChanged: ClassVar[Signal] = ... # currentSearchResultIndexChanged(int)
    documentChanged          : ClassVar[Signal] = ... # documentChanged(QPdfDocument*)
    documentMarginsChanged   : ClassVar[Signal] = ... # documentMarginsChanged(QMargins)
    pageModeChanged          : ClassVar[Signal] = ... # pageModeChanged(QPdfView::PageMode)
    pageSpacingChanged       : ClassVar[Signal] = ... # pageSpacingChanged(int)
    searchModelChanged       : ClassVar[Signal] = ... # searchModelChanged(QPdfSearchModel*)
    zoomFactorChanged        : ClassVar[Signal] = ... # zoomFactorChanged(double)
    zoomModeChanged          : ClassVar[Signal] = ... # zoomModeChanged(QPdfView::ZoomMode)

    class PageMode(enum.Enum):

        SinglePage               : QPdfView.PageMode = ... # 0x0
        MultiPage                : QPdfView.PageMode = ... # 0x1

    class ZoomMode(enum.Enum):

        Custom                   : QPdfView.ZoomMode = ... # 0x0
        FitToWidth               : QPdfView.ZoomMode = ... # 0x1
        FitInView                : QPdfView.ZoomMode = ... # 0x2


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget) -> None: ...

    def currentSearchResultIndex(self) -> int: ...
    def document(self) -> PySide6.QtPdf.QPdfDocument: ...
    def documentMargins(self) -> PySide6.QtCore.QMargins: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def pageMode(self) -> PySide6.QtPdfWidgets.QPdfView.PageMode: ...
    def pageNavigator(self) -> PySide6.QtPdf.QPdfPageNavigator: ...
    def pageSpacing(self) -> int: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...
    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None: ...
    def scrollContentsBy(self, dx: int, dy: int) -> None: ...
    def searchModel(self) -> PySide6.QtPdf.QPdfSearchModel: ...
    def setCurrentSearchResultIndex(self, currentResult: int) -> None: ...
    def setDocument(self, document: PySide6.QtPdf.QPdfDocument) -> None: ...
    def setDocumentMargins(self, margins: PySide6.QtCore.QMargins) -> None: ...
    def setPageMode(self, mode: PySide6.QtPdfWidgets.QPdfView.PageMode) -> None: ...
    def setPageSpacing(self, spacing: int) -> None: ...
    def setSearchModel(self, searchModel: PySide6.QtPdf.QPdfSearchModel) -> None: ...
    def setZoomFactor(self, factor: float) -> None: ...
    def setZoomMode(self, mode: PySide6.QtPdfWidgets.QPdfView.ZoomMode) -> None: ...
    def zoomFactor(self) -> float: ...
    def zoomMode(self) -> PySide6.QtPdfWidgets.QPdfView.ZoomMode: ...


# eof
