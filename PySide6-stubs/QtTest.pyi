# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtTest, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtTest`

import PySide6.QtTest
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

from typing import Any, Optional, Union, List, overload
from shiboken6 import Shiboken


class QAbstractItemModelTester(PySide6.QtCore.QObject):

    class FailureReportingMode(shibokensupport.enum_310.Enum):

        QtTest                   : QAbstractItemModelTester.FailureReportingMode = ... # 0x0
        Warning                  : QAbstractItemModelTester.FailureReportingMode = ... # 0x1
        Fatal                    : QAbstractItemModelTester.FailureReportingMode = ... # 0x2


    @overload
    def __init__(self, model: PySide6.QtCore.QAbstractItemModel, mode: PySide6.QtTest.QAbstractItemModelTester.FailureReportingMode, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, model: PySide6.QtCore.QAbstractItemModel, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def failureReportingMode(self) -> PySide6.QtTest.QAbstractItemModelTester.FailureReportingMode: ...
    def model(self) -> PySide6.QtCore.QAbstractItemModel: ...
    def setUseFetchMore(self, value: bool) -> None: ...


class QIntList(object): ...


class QSignalSpy(PySide6.QtCore.QObject):

    @overload
    def __init__(self, obj: PySide6.QtCore.QObject, aSignal: bytes) -> None: ...
    @overload
    def __init__(self, obj: PySide6.QtCore.QObject, signal: PySide6.QtCore.QMetaMethod) -> None: ...
    @overload
    def __init__(self, signal: PySide6.QtCore.SignalInstance) -> None: ...

    def at(self, arg__1: int) -> List[Any]: ...
    def count(self) -> int: ...
    def isValid(self) -> bool: ...
    def signal(self) -> PySide6.QtCore.QByteArray: ...
    def size(self) -> int: ...
    def wait(self, timeout: int = ...) -> bool: ...


class QTest(Shiboken.Object):

    class KeyAction(shibokensupport.enum_310.Enum):

        Press                    : QTest.KeyAction = ... # 0x0
        Release                  : QTest.KeyAction = ... # 0x1
        Click                    : QTest.KeyAction = ... # 0x2
        Shortcut                 : QTest.KeyAction = ... # 0x3


    class MouseAction(shibokensupport.enum_310.Enum):

        MousePress               : QTest.MouseAction = ... # 0x0
        MouseRelease             : QTest.MouseAction = ... # 0x1
        MouseClick               : QTest.MouseAction = ... # 0x2
        MouseDClick              : QTest.MouseAction = ... # 0x3
        MouseMove                : QTest.MouseAction = ... # 0x4


    class QBenchmarkMetric(shibokensupport.enum_310.Enum):

        FramesPerSecond          : QTest.QBenchmarkMetric = ... # 0x0
        BitsPerSecond            : QTest.QBenchmarkMetric = ... # 0x1
        BytesPerSecond           : QTest.QBenchmarkMetric = ... # 0x2
        WalltimeMilliseconds     : QTest.QBenchmarkMetric = ... # 0x3
        CPUTicks                 : QTest.QBenchmarkMetric = ... # 0x4
        InstructionReads         : QTest.QBenchmarkMetric = ... # 0x5
        Events                   : QTest.QBenchmarkMetric = ... # 0x6
        WalltimeNanoseconds      : QTest.QBenchmarkMetric = ... # 0x7
        BytesAllocated           : QTest.QBenchmarkMetric = ... # 0x8
        CPUMigrations            : QTest.QBenchmarkMetric = ... # 0x9
        CPUCycles                : QTest.QBenchmarkMetric = ... # 0xa
        BusCycles                : QTest.QBenchmarkMetric = ... # 0xb
        StalledCycles            : QTest.QBenchmarkMetric = ... # 0xc
        Instructions             : QTest.QBenchmarkMetric = ... # 0xd
        BranchInstructions       : QTest.QBenchmarkMetric = ... # 0xe
        BranchMisses             : QTest.QBenchmarkMetric = ... # 0xf
        CacheReferences          : QTest.QBenchmarkMetric = ... # 0x10
        CacheReads               : QTest.QBenchmarkMetric = ... # 0x11
        CacheWrites              : QTest.QBenchmarkMetric = ... # 0x12
        CachePrefetches          : QTest.QBenchmarkMetric = ... # 0x13
        CacheMisses              : QTest.QBenchmarkMetric = ... # 0x14
        CacheReadMisses          : QTest.QBenchmarkMetric = ... # 0x15
        CacheWriteMisses         : QTest.QBenchmarkMetric = ... # 0x16
        CachePrefetchMisses      : QTest.QBenchmarkMetric = ... # 0x17
        ContextSwitches          : QTest.QBenchmarkMetric = ... # 0x18
        PageFaults               : QTest.QBenchmarkMetric = ... # 0x19
        MinorPageFaults          : QTest.QBenchmarkMetric = ... # 0x1a
        MajorPageFaults          : QTest.QBenchmarkMetric = ... # 0x1b
        AlignmentFaults          : QTest.QBenchmarkMetric = ... # 0x1c
        EmulationFaults          : QTest.QBenchmarkMetric = ... # 0x1d
        RefCPUCycles             : QTest.QBenchmarkMetric = ... # 0x1e


    class QTouchEventSequence(Shiboken.Object):
        def commit(self, processEvents: bool = ...) -> None: ...
        @overload
        def move(self, touchId: int, pt: PySide6.QtCore.QPoint, widget: Optional[PySide6.QtWidgets.QWidget] = ...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        @overload
        def move(self, touchId: int, pt: PySide6.QtCore.QPoint, window: Optional[PySide6.QtGui.QWindow] = ...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        @overload
        def press(self, touchId: int, pt: PySide6.QtCore.QPoint, widget: Optional[PySide6.QtWidgets.QWidget] = ...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        @overload
        def press(self, touchId: int, pt: PySide6.QtCore.QPoint, window: Optional[PySide6.QtGui.QWindow] = ...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        @overload
        def release(self, touchId: int, pt: PySide6.QtCore.QPoint, widget: Optional[PySide6.QtWidgets.QWidget] = ...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        @overload
        def release(self, touchId: int, pt: PySide6.QtCore.QPoint, window: Optional[PySide6.QtGui.QWindow] = ...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        def stationary(self, touchId: int) -> PySide6.QtTest.QTest.QTouchEventSequence: ...

    class TestFailMode(shibokensupport.enum_310.Enum):

        Abort                    : QTest.TestFailMode = ... # 0x1
        Continue                 : QTest.TestFailMode = ... # 0x2


    @staticmethod
    def addColumnInternal(id: int, name: bytes) -> None: ...
    @staticmethod
    def asciiToKey(ascii: int) -> PySide6.QtCore.Qt.Key: ...
    @overload
    @staticmethod
    def compare_ptr_helper(t1: PySide6.QtCore.QObject, t2: PySide6.QtCore.QObject, actual: bytes, expected: bytes, file: bytes, line: int) -> bool: ...
    @overload
    @staticmethod
    def compare_ptr_helper(t1: int, t2: int, actual: bytes, expected: bytes, file: bytes, line: int) -> bool: ...
    @staticmethod
    def compare_string_helper(t1: bytes, t2: bytes, actual: bytes, expected: bytes, file: bytes, line: int) -> bool: ...
    @staticmethod
    def createTouchDevice(devType: PySide6.QtGui.QInputDevice.DeviceType = ..., caps: PySide6.QtGui.QInputDevice.Capability = ...) -> PySide6.QtGui.QPointingDevice: ...
    @staticmethod
    def currentAppName() -> bytes: ...
    @staticmethod
    def currentDataTag() -> bytes: ...
    @staticmethod
    def currentTestFailed() -> bool: ...
    @staticmethod
    def currentTestFunction() -> bytes: ...
    @overload
    @staticmethod
    def failOnWarning(message: bytes) -> None: ...
    @overload
    @staticmethod
    def failOnWarning(messagePattern: Union[PySide6.QtCore.QRegularExpression, str]) -> None: ...
    @staticmethod
    def formatString(prefix: bytes, suffix: bytes, numArguments: int) -> bytes: ...
    @overload
    @staticmethod
    def ignoreMessage(type: PySide6.QtCore.QtMsgType, message: bytes) -> None: ...
    @overload
    @staticmethod
    def ignoreMessage(type: PySide6.QtCore.QtMsgType, messagePattern: Union[PySide6.QtCore.QRegularExpression, str]) -> None: ...
    @overload
    @staticmethod
    def keyClick(widget: PySide6.QtWidgets.QWidget, key: PySide6.QtCore.Qt.Key, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyClick(widget: PySide6.QtWidgets.QWidget, key: int, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyClick(window: PySide6.QtGui.QWindow, key: PySide6.QtCore.Qt.Key, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyClick(window: PySide6.QtGui.QWindow, key: int, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @staticmethod
    def keyClicks(widget: PySide6.QtWidgets.QWidget, sequence: str, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyEvent(action: PySide6.QtTest.QTest.KeyAction, widget: PySide6.QtWidgets.QWidget, ascii: int, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyEvent(action: PySide6.QtTest.QTest.KeyAction, widget: PySide6.QtWidgets.QWidget, key: PySide6.QtCore.Qt.Key, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyEvent(action: PySide6.QtTest.QTest.KeyAction, window: PySide6.QtGui.QWindow, ascii: int, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyEvent(action: PySide6.QtTest.QTest.KeyAction, window: PySide6.QtGui.QWindow, key: PySide6.QtCore.Qt.Key, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyPress(widget: PySide6.QtWidgets.QWidget, key: PySide6.QtCore.Qt.Key, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyPress(widget: PySide6.QtWidgets.QWidget, key: int, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyPress(window: PySide6.QtGui.QWindow, key: PySide6.QtCore.Qt.Key, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyPress(window: PySide6.QtGui.QWindow, key: int, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyRelease(widget: PySide6.QtWidgets.QWidget, key: PySide6.QtCore.Qt.Key, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyRelease(widget: PySide6.QtWidgets.QWidget, key: int, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyRelease(window: PySide6.QtGui.QWindow, key: PySide6.QtCore.Qt.Key, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keyRelease(window: PySide6.QtGui.QWindow, key: int, modifier: PySide6.QtCore.Qt.KeyboardModifier = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def keySequence(widget: PySide6.QtWidgets.QWidget, keySequence: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int]) -> None: ...
    @overload
    @staticmethod
    def keySequence(window: PySide6.QtGui.QWindow, keySequence: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int]) -> None: ...
    @staticmethod
    def keyToAscii(key: PySide6.QtCore.Qt.Key) -> int: ...
    @overload
    @staticmethod
    def mouseClick(widget: PySide6.QtWidgets.QWidget, button: PySide6.QtCore.Qt.MouseButton, stateKey: PySide6.QtCore.Qt.KeyboardModifier = ..., pos: PySide6.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def mouseClick(window: PySide6.QtGui.QWindow, button: PySide6.QtCore.Qt.MouseButton, stateKey: PySide6.QtCore.Qt.KeyboardModifier = ..., pos: PySide6.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def mouseDClick(widget: PySide6.QtWidgets.QWidget, button: PySide6.QtCore.Qt.MouseButton, stateKey: PySide6.QtCore.Qt.KeyboardModifier = ..., pos: PySide6.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def mouseDClick(window: PySide6.QtGui.QWindow, button: PySide6.QtCore.Qt.MouseButton, stateKey: PySide6.QtCore.Qt.KeyboardModifier = ..., pos: PySide6.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def mouseEvent(action: PySide6.QtTest.QTest.MouseAction, widget: PySide6.QtWidgets.QWidget, button: PySide6.QtCore.Qt.MouseButton, stateKey: PySide6.QtCore.Qt.KeyboardModifier, pos: PySide6.QtCore.QPoint, delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def mouseEvent(action: PySide6.QtTest.QTest.MouseAction, window: PySide6.QtGui.QWindow, button: PySide6.QtCore.Qt.MouseButton, stateKey: PySide6.QtCore.Qt.KeyboardModifier, pos: PySide6.QtCore.QPoint, delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def mouseMove(widget: PySide6.QtWidgets.QWidget, pos: PySide6.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def mouseMove(window: PySide6.QtGui.QWindow, pos: PySide6.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def mousePress(widget: PySide6.QtWidgets.QWidget, button: PySide6.QtCore.Qt.MouseButton, stateKey: PySide6.QtCore.Qt.KeyboardModifier = ..., pos: PySide6.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def mousePress(window: PySide6.QtGui.QWindow, button: PySide6.QtCore.Qt.MouseButton, stateKey: PySide6.QtCore.Qt.KeyboardModifier = ..., pos: PySide6.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def mouseRelease(widget: PySide6.QtWidgets.QWidget, button: PySide6.QtCore.Qt.MouseButton, stateKey: PySide6.QtCore.Qt.KeyboardModifier = ..., pos: PySide6.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def mouseRelease(window: PySide6.QtGui.QWindow, button: PySide6.QtCore.Qt.MouseButton, stateKey: PySide6.QtCore.Qt.KeyboardModifier = ..., pos: PySide6.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @staticmethod
    def qCaught(expected: bytes, what: bytes, file: bytes, line: int) -> None: ...
    @staticmethod
    def qCleanup() -> None: ...
    @staticmethod
    def qElementData(elementName: bytes, metaTypeId: int) -> int: ...
    @staticmethod
    def qExpectFail(dataIndex: bytes, comment: bytes, mode: PySide6.QtTest.QTest.TestFailMode, file: bytes, line: int) -> bool: ...
    @overload
    @staticmethod
    def qFindTestData(basepath: str, file: Optional[bytes] = ..., line: int = ..., builddir: Optional[bytes] = ..., sourcedir: Optional[bytes] = ...) -> str: ...
    @overload
    @staticmethod
    def qFindTestData(basepath: bytes, file: Optional[bytes] = ..., line: int = ..., builddir: Optional[bytes] = ..., sourcedir: Optional[bytes] = ...) -> str: ...
    @staticmethod
    def qGlobalData(tagName: bytes, typeId: int) -> int: ...
    @staticmethod
    def qRun() -> int: ...
    @staticmethod
    def qSkip(message: bytes, file: bytes, line: int) -> None: ...
    @staticmethod
    def qSleep(ms: int) -> None: ...
    @staticmethod
    def qWait(ms: int) -> None: ...
    @overload
    @staticmethod
    def qWaitForWindowActive(widget: PySide6.QtWidgets.QWidget, timeout: int = ...) -> bool: ...
    @overload
    @staticmethod
    def qWaitForWindowActive(window: PySide6.QtGui.QWindow, timeout: int = ...) -> bool: ...
    @overload
    @staticmethod
    def qWaitForWindowExposed(widget: PySide6.QtWidgets.QWidget, timeout: int = ...) -> bool: ...
    @overload
    @staticmethod
    def qWaitForWindowExposed(window: PySide6.QtGui.QWindow, timeout: int = ...) -> bool: ...
    @overload
    @staticmethod
    def sendKeyEvent(action: PySide6.QtTest.QTest.KeyAction, widget: PySide6.QtWidgets.QWidget, code: PySide6.QtCore.Qt.Key, ascii: int, modifier: PySide6.QtCore.Qt.KeyboardModifier, delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def sendKeyEvent(action: PySide6.QtTest.QTest.KeyAction, widget: PySide6.QtWidgets.QWidget, code: PySide6.QtCore.Qt.Key, text: str, modifier: PySide6.QtCore.Qt.KeyboardModifier, delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def sendKeyEvent(action: PySide6.QtTest.QTest.KeyAction, window: PySide6.QtGui.QWindow, code: PySide6.QtCore.Qt.Key, ascii: int, modifier: PySide6.QtCore.Qt.KeyboardModifier, delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def sendKeyEvent(action: PySide6.QtTest.QTest.KeyAction, window: PySide6.QtGui.QWindow, code: PySide6.QtCore.Qt.Key, text: str, modifier: PySide6.QtCore.Qt.KeyboardModifier, delay: int = ...) -> None: ...
    @staticmethod
    def setBenchmarkResult(result: float, metric: PySide6.QtTest.QTest.QBenchmarkMetric) -> None: ...
    @staticmethod
    def setMainSourcePath(file: bytes, builddir: Optional[bytes] = ...) -> None: ...
    @overload
    @staticmethod
    def simulateEvent(widget: PySide6.QtWidgets.QWidget, press: bool, code: int, modifier: PySide6.QtCore.Qt.KeyboardModifier, text: str, repeat: bool, delay: int = ...) -> None: ...
    @overload
    @staticmethod
    def simulateEvent(window: PySide6.QtGui.QWindow, press: bool, code: int, modifier: PySide6.QtCore.Qt.KeyboardModifier, text: str, repeat: bool, delay: int = ...) -> None: ...
    @staticmethod
    def testObject() -> PySide6.QtCore.QObject: ...
    @staticmethod
    def toPrettyCString(unicode: bytes, length: int) -> bytes: ...
    @overload
    @staticmethod
    def touchEvent(widget: PySide6.QtWidgets.QWidget, device: PySide6.QtGui.QPointingDevice, autoCommit: bool = ...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
    @overload
    @staticmethod
    def touchEvent(window: PySide6.QtGui.QWindow, device: PySide6.QtGui.QPointingDevice, autoCommit: bool = ...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...


# eof
