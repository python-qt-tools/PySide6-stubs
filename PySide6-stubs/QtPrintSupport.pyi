# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations
"""
This file contains the exact signatures for all functions in module
PySide6.QtPrintSupport, except for defaults which are replaced by "...".

# mypy: disable-error-code="override, overload-overlap"
"""

# Module `PySide6.QtPrintSupport`

import PySide6.QtPrintSupport
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

import enum
import typing
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


class QAbstractPrintDialog(PySide6.QtWidgets.QDialog):

    class PrintDialogOption(enum.Flag):

        PrintToFile               = ...  # 0x1
        PrintSelection            = ...  # 0x2
        PrintPageRange            = ...  # 0x4
        PrintShowPageSize         = ...  # 0x8
        PrintCollateCopies        = ...  # 0x10
        PrintCurrentPage          = ...  # 0x40

    class PrintRange(enum.Enum):

        AllPages                  = ...  # 0x0
        Selection                 = ...  # 0x1
        PageRange                 = ...  # 0x2
        CurrentPage               = ...  # 0x3


    def __init__(self, printer: PySide6.QtPrintSupport.QPrinter, /, parent: PySide6.QtWidgets.QWidget | None= ...) -> None: ...

    def fromPage(self, /) -> int: ...
    def maxPage(self, /) -> int: ...
    def minPage(self, /) -> int: ...
    def printRange(self, /) -> PySide6.QtPrintSupport.QAbstractPrintDialog.PrintRange: ...
    def printer(self, /) -> PySide6.QtPrintSupport.QPrinter: ...
    def setFromTo(self, fromPage: int, toPage: int, /) -> None: ...
    def setMinMax(self, min: int, max: int, /) -> None: ...
    def setOptionTabs(self, tabs: typing.Sequence[PySide6.QtWidgets.QWidget], /) -> None: ...
    def setPrintRange(self, range: PySide6.QtPrintSupport.QAbstractPrintDialog.PrintRange, /) -> None: ...
    def toPage(self, /) -> int: ...


class QIntList(object): ...


class QPageSetupDialog(PySide6.QtWidgets.QDialog):

    @typing.overload
    def __init__(self, printer: PySide6.QtPrintSupport.QPrinter, /, parent: PySide6.QtWidgets.QWidget | None= ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None= ...) -> None: ...

    def done(self, result: int, /) -> None: ...
    def exec(self, /) -> int: ...
    def exec_(self, /) -> int: ...
    @typing.overload
    def open(self, /) -> None: ...
    @typing.overload
    def open(self, receiver: PySide6.QtCore.QObject, member: bytes | bytearray | memoryview, /) -> None: ...
    def printer(self, /) -> PySide6.QtPrintSupport.QPrinter: ...
    def setVisible(self, visible: bool, /) -> None: ...


class QPrintDialog(PySide6.QtPrintSupport.QAbstractPrintDialog):

    accepted                 : typing.ClassVar[Signal] = ... # accepted(QPrinter*)

    @typing.overload
    def __init__(self, printer: PySide6.QtPrintSupport.QPrinter, /, parent: PySide6.QtWidgets.QWidget | None= ..., *, options: PySide6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption | None= ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None= ..., *, options: PySide6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption | None= ...) -> None: ...

    def done(self, result: int, /) -> None: ...
    def exec(self, /) -> int: ...
    def exec_(self, /) -> int: ...
    def open(self, receiver: PySide6.QtCore.QObject, member: bytes | bytearray | memoryview, /) -> None: ...
    def options(self, /) -> PySide6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption: ...
    def setOption(self, option: PySide6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption, /, on: bool = ...) -> None: ...
    def setOptions(self, options: PySide6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption, /) -> None: ...
    def setVisible(self, visible: bool, /) -> None: ...
    def testOption(self, option: PySide6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption, /) -> bool: ...


class QPrintEngine(Shiboken.Object):

    class PrintEnginePropertyKey(enum.Enum):

        PPK_CollateCopies         = ...  # 0x0
        PPK_ColorMode             = ...  # 0x1
        PPK_Creator               = ...  # 0x2
        PPK_DocumentName          = ...  # 0x3
        PPK_FullPage              = ...  # 0x4
        PPK_NumberOfCopies        = ...  # 0x5
        PPK_Orientation           = ...  # 0x6
        PPK_OutputFileName        = ...  # 0x7
        PPK_PageOrder             = ...  # 0x8
        PPK_PageRect              = ...  # 0x9
        PPK_PageSize              = ...  # 0xa
        PPK_PaperSize             = ...  # 0xa
        PPK_PaperRect             = ...  # 0xb
        PPK_PaperSource           = ...  # 0xc
        PPK_PrinterName           = ...  # 0xd
        PPK_PrinterProgram        = ...  # 0xe
        PPK_Resolution            = ...  # 0xf
        PPK_SelectionOption       = ...  # 0x10
        PPK_SupportedResolutions  = ...  # 0x11
        PPK_WindowsPageSize       = ...  # 0x12
        PPK_FontEmbedding         = ...  # 0x13
        PPK_Duplex                = ...  # 0x14
        PPK_PaperSources          = ...  # 0x15
        PPK_CustomPaperSize       = ...  # 0x16
        PPK_PageMargins           = ...  # 0x17
        PPK_CopyCount             = ...  # 0x18
        PPK_SupportsMultipleCopies = ...  # 0x19
        PPK_PaperName             = ...  # 0x1a
        PPK_QPageSize             = ...  # 0x1b
        PPK_QPageMargins          = ...  # 0x1c
        PPK_QPageLayout           = ...  # 0x1d
        PPK_CustomBase            = ...  # 0xff00


    def __init__(self, /) -> None: ...

    def abort(self, /) -> bool: ...
    def metric(self, arg__1: PySide6.QtGui.QPaintDevice.PaintDeviceMetric, /) -> int: ...
    def newPage(self, /) -> bool: ...
    def printerState(self, /) -> PySide6.QtPrintSupport.QPrinter.PrinterState: ...
    def property(self, key: PySide6.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey, /) -> typing.Any: ...
    def setProperty(self, key: PySide6.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey, value: typing.Any, /) -> None: ...


class QPrintPreviewDialog(PySide6.QtWidgets.QDialog):

    paintRequested           : typing.ClassVar[Signal] = ... # paintRequested(QPrinter*)

    @typing.overload
    def __init__(self, printer: PySide6.QtPrintSupport.QPrinter, /, parent: PySide6.QtWidgets.QWidget | None= ..., flags: PySide6.QtCore.Qt.WindowType = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None= ..., flags: PySide6.QtCore.Qt.WindowType = ...) -> None: ...

    def done(self, result: int, /) -> None: ...
    @typing.overload
    def open(self, /) -> None: ...
    @typing.overload
    def open(self, receiver: PySide6.QtCore.QObject, member: bytes | bytearray | memoryview, /) -> None: ...
    def printer(self, /) -> PySide6.QtPrintSupport.QPrinter: ...
    def setVisible(self, visible: bool, /) -> None: ...


class QPrintPreviewWidget(PySide6.QtWidgets.QWidget):

    paintRequested           : typing.ClassVar[Signal] = ... # paintRequested(QPrinter*)
    previewChanged           : typing.ClassVar[Signal] = ... # previewChanged()

    class ViewMode(enum.Enum):

        SinglePageView            = ...  # 0x0
        FacingPagesView           = ...  # 0x1
        AllPagesView              = ...  # 0x2

    class ZoomMode(enum.Enum):

        CustomZoom                = ...  # 0x0
        FitToWidth                = ...  # 0x1
        FitInView                 = ...  # 0x2


    @typing.overload
    def __init__(self, printer: PySide6.QtPrintSupport.QPrinter, /, parent: PySide6.QtWidgets.QWidget | None= ..., flags: PySide6.QtCore.Qt.WindowType = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None= ..., flags: PySide6.QtCore.Qt.WindowType = ...) -> None: ...

    def currentPage(self, /) -> int: ...
    def fitInView(self, /) -> None: ...
    def fitToWidth(self, /) -> None: ...
    def orientation(self, /) -> PySide6.QtGui.QPageLayout.Orientation: ...
    def pageCount(self, /) -> int: ...
    def print_(self, /) -> None: ...
    def setAllPagesViewMode(self, /) -> None: ...
    def setCurrentPage(self, pageNumber: int, /) -> None: ...
    def setFacingPagesViewMode(self, /) -> None: ...
    def setLandscapeOrientation(self, /) -> None: ...
    def setOrientation(self, orientation: PySide6.QtGui.QPageLayout.Orientation, /) -> None: ...
    def setPortraitOrientation(self, /) -> None: ...
    def setSinglePageViewMode(self, /) -> None: ...
    def setViewMode(self, viewMode: PySide6.QtPrintSupport.QPrintPreviewWidget.ViewMode, /) -> None: ...
    def setVisible(self, visible: bool, /) -> None: ...
    def setZoomFactor(self, zoomFactor: float, /) -> None: ...
    def setZoomMode(self, zoomMode: PySide6.QtPrintSupport.QPrintPreviewWidget.ZoomMode, /) -> None: ...
    def updatePreview(self, /) -> None: ...
    def viewMode(self, /) -> PySide6.QtPrintSupport.QPrintPreviewWidget.ViewMode: ...
    def zoomFactor(self, /) -> float: ...
    def zoomIn(self, /, zoom: float = ...) -> None: ...
    def zoomMode(self, /) -> PySide6.QtPrintSupport.QPrintPreviewWidget.ZoomMode: ...
    def zoomOut(self, /, zoom: float = ...) -> None: ...


class QPrinter(PySide6.QtGui.QPagedPaintDevice):

    class ColorMode(enum.Enum):

        GrayScale                 = ...  # 0x0
        Color                     = ...  # 0x1

    class DuplexMode(enum.Enum):

        DuplexNone                = ...  # 0x0
        DuplexAuto                = ...  # 0x1
        DuplexLongSide            = ...  # 0x2
        DuplexShortSide           = ...  # 0x3

    class OutputFormat(enum.Enum):

        NativeFormat              = ...  # 0x0
        PdfFormat                 = ...  # 0x1

    class PageOrder(enum.Enum):

        FirstPageFirst            = ...  # 0x0
        LastPageFirst             = ...  # 0x1

    class PaperSource(enum.Enum):

        OnlyOne                   = ...  # 0x0
        Upper                     = ...  # 0x0
        Lower                     = ...  # 0x1
        Middle                    = ...  # 0x2
        Manual                    = ...  # 0x3
        Envelope                  = ...  # 0x4
        EnvelopeManual            = ...  # 0x5
        Auto                      = ...  # 0x6
        Tractor                   = ...  # 0x7
        SmallFormat               = ...  # 0x8
        LargeFormat               = ...  # 0x9
        LargeCapacity             = ...  # 0xa
        Cassette                  = ...  # 0xb
        FormSource                = ...  # 0xc
        MaxPageSource             = ...  # 0xd
        CustomSource              = ...  # 0xe
        LastPaperSource           = ...  # 0xe

    class PrintRange(enum.Enum):

        AllPages                  = ...  # 0x0
        Selection                 = ...  # 0x1
        PageRange                 = ...  # 0x2
        CurrentPage               = ...  # 0x3

    class PrinterMode(enum.Enum):

        ScreenResolution          = ...  # 0x0
        PrinterResolution         = ...  # 0x1
        HighResolution            = ...  # 0x2

    class PrinterState(enum.Enum):

        Idle                      = ...  # 0x0
        Active                    = ...  # 0x1
        Aborted                   = ...  # 0x2
        Error                     = ...  # 0x3

    class Unit(enum.Enum):

        Millimeter                = ...  # 0x0
        Point                     = ...  # 0x1
        Inch                      = ...  # 0x2
        Pica                      = ...  # 0x3
        Didot                     = ...  # 0x4
        Cicero                    = ...  # 0x5
        DevicePixel               = ...  # 0x6


    @typing.overload
    def __init__(self, /, mode: PySide6.QtPrintSupport.QPrinter.PrinterMode = ...) -> None: ...
    @typing.overload
    def __init__(self, printer: PySide6.QtPrintSupport.QPrinterInfo, /, mode: PySide6.QtPrintSupport.QPrinter.PrinterMode = ...) -> None: ...

    def abort(self, /) -> bool: ...
    def collateCopies(self, /) -> bool: ...
    def colorMode(self, /) -> PySide6.QtPrintSupport.QPrinter.ColorMode: ...
    def copyCount(self, /) -> int: ...
    def creator(self, /) -> str: ...
    def devType(self, /) -> int: ...
    def docName(self, /) -> str: ...
    def duplex(self, /) -> PySide6.QtPrintSupport.QPrinter.DuplexMode: ...
    def fontEmbeddingEnabled(self, /) -> bool: ...
    def fromPage(self, /) -> int: ...
    def fullPage(self, /) -> bool: ...
    def isValid(self, /) -> bool: ...
    def metric(self, arg__1: PySide6.QtGui.QPaintDevice.PaintDeviceMetric, /) -> int: ...
    def newPage(self, /) -> bool: ...
    def outputFileName(self, /) -> str: ...
    def outputFormat(self, /) -> PySide6.QtPrintSupport.QPrinter.OutputFormat: ...
    def pageOrder(self, /) -> PySide6.QtPrintSupport.QPrinter.PageOrder: ...
    def pageRect(self, arg__1: PySide6.QtPrintSupport.QPrinter.Unit, /) -> PySide6.QtCore.QRectF: ...
    def paintEngine(self, /) -> PySide6.QtGui.QPaintEngine: ...
    def paperRect(self, arg__1: PySide6.QtPrintSupport.QPrinter.Unit, /) -> PySide6.QtCore.QRectF: ...
    def paperSource(self, /) -> PySide6.QtPrintSupport.QPrinter.PaperSource: ...
    def pdfVersion(self, /) -> PySide6.QtGui.QPagedPaintDevice.PdfVersion: ...
    def printEngine(self, /) -> PySide6.QtPrintSupport.QPrintEngine: ...
    def printProgram(self, /) -> str: ...
    def printRange(self, /) -> PySide6.QtPrintSupport.QPrinter.PrintRange: ...
    def printerName(self, /) -> str: ...
    def printerState(self, /) -> PySide6.QtPrintSupport.QPrinter.PrinterState: ...
    def resolution(self, /) -> int: ...
    def setCollateCopies(self, collate: bool, /) -> None: ...
    def setColorMode(self, arg__1: PySide6.QtPrintSupport.QPrinter.ColorMode, /) -> None: ...
    def setCopyCount(self, arg__1: int, /) -> None: ...
    def setCreator(self, arg__1: str, /) -> None: ...
    def setDocName(self, arg__1: str, /) -> None: ...
    def setDuplex(self, duplex: PySide6.QtPrintSupport.QPrinter.DuplexMode, /) -> None: ...
    def setEngines(self, printEngine: PySide6.QtPrintSupport.QPrintEngine, paintEngine: PySide6.QtGui.QPaintEngine, /) -> None: ...
    def setFontEmbeddingEnabled(self, enable: bool, /) -> None: ...
    def setFromTo(self, fromPage: int, toPage: int, /) -> None: ...
    def setFullPage(self, arg__1: bool, /) -> None: ...
    def setOutputFileName(self, arg__1: str, /) -> None: ...
    def setOutputFormat(self, format: PySide6.QtPrintSupport.QPrinter.OutputFormat, /) -> None: ...
    def setPageOrder(self, arg__1: PySide6.QtPrintSupport.QPrinter.PageOrder, /) -> None: ...
    def setPageSize(self, size: PySide6.QtGui.QPageSize | PySide6.QtGui.QPageSize.PageSizeId | PySide6.QtCore.QSize, /) -> bool: ...
    def setPaperSource(self, arg__1: PySide6.QtPrintSupport.QPrinter.PaperSource, /) -> None: ...
    def setPdfVersion(self, version: PySide6.QtGui.QPagedPaintDevice.PdfVersion, /) -> None: ...
    def setPrintProgram(self, arg__1: str, /) -> None: ...
    def setPrintRange(self, range: PySide6.QtPrintSupport.QPrinter.PrintRange, /) -> None: ...
    def setPrinterName(self, arg__1: str, /) -> None: ...
    def setResolution(self, arg__1: int, /) -> None: ...
    def supportedResolutions(self, /) -> typing.List[int]: ...
    def supportsMultipleCopies(self, /) -> bool: ...
    def toPage(self, /) -> int: ...


class QPrinterInfo(Shiboken.Object):

    @typing.overload
    def __init__(self, /) -> None: ...
    @typing.overload
    def __init__(self, printer: PySide6.QtPrintSupport.QPrinter, /) -> None: ...
    @typing.overload
    def __init__(self, other: PySide6.QtPrintSupport.QPrinterInfo, /) -> None: ...

    def __copy__(self, /) -> typing.Self: ...
    @staticmethod
    def availablePrinterNames() -> typing.List[str]: ...
    @staticmethod
    def availablePrinters() -> typing.List[PySide6.QtPrintSupport.QPrinterInfo]: ...
    def defaultColorMode(self, /) -> PySide6.QtPrintSupport.QPrinter.ColorMode: ...
    def defaultDuplexMode(self, /) -> PySide6.QtPrintSupport.QPrinter.DuplexMode: ...
    def defaultPageSize(self, /) -> PySide6.QtGui.QPageSize: ...
    @staticmethod
    def defaultPrinter() -> PySide6.QtPrintSupport.QPrinterInfo: ...
    @staticmethod
    def defaultPrinterName() -> str: ...
    def description(self, /) -> str: ...
    def isDefault(self, /) -> bool: ...
    def isNull(self, /) -> bool: ...
    def isRemote(self, /) -> bool: ...
    def location(self, /) -> str: ...
    def makeAndModel(self, /) -> str: ...
    def maximumPhysicalPageSize(self, /) -> PySide6.QtGui.QPageSize: ...
    def minimumPhysicalPageSize(self, /) -> PySide6.QtGui.QPageSize: ...
    @staticmethod
    def printerInfo(printerName: str, /) -> PySide6.QtPrintSupport.QPrinterInfo: ...
    def printerName(self, /) -> str: ...
    def state(self, /) -> PySide6.QtPrintSupport.QPrinter.PrinterState: ...
    def supportedColorModes(self, /) -> typing.List[PySide6.QtPrintSupport.QPrinter.ColorMode]: ...
    def supportedDuplexModes(self, /) -> typing.List[PySide6.QtPrintSupport.QPrinter.DuplexMode]: ...
    def supportedPageSizes(self, /) -> typing.List[PySide6.QtGui.QPageSize]: ...
    def supportedResolutions(self, /) -> typing.List[int]: ...
    def supportsCustomPageSizes(self, /) -> bool: ...


# eof
