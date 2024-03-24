# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtWebChannel, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtWebChannel`

import PySide6.QtWebChannel
import PySide6.QtCore

from typing import ClassVar, Dict, Optional
from PySide6.QtCore import Signal


NoneType = type(None)


class QIntList(object): ...


class QWebChannel(PySide6.QtCore.QObject):

    blockUpdatesChanged      : ClassVar[Signal] = ... # blockUpdatesChanged(bool)

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def blockUpdates(self) -> bool: ...
    def connectTo(self, transport: PySide6.QtWebChannel.QWebChannelAbstractTransport) -> None: ...
    def deregisterObject(self, object: PySide6.QtCore.QObject) -> None: ...
    def disconnectFrom(self, transport: PySide6.QtWebChannel.QWebChannelAbstractTransport) -> None: ...
    def propertyUpdateInterval(self) -> int: ...
    def registerObject(self, id: str, object: PySide6.QtCore.QObject) -> None: ...
    def registerObjects(self, objects: Dict[str, PySide6.QtCore.QObject]) -> None: ...
    def registeredObjects(self) -> Dict[str, PySide6.QtCore.QObject]: ...
    def setBlockUpdates(self, block: bool) -> None: ...
    def setPropertyUpdateInterval(self, ms: int) -> None: ...


class QWebChannelAbstractTransport(PySide6.QtCore.QObject):

    messageReceived          : ClassVar[Signal] = ... # messageReceived(QJsonObject,QWebChannelAbstractTransport*)

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def sendMessage(self, message: Dict[str, PySide6.QtCore.QJsonValue]) -> None: ...


# eof
