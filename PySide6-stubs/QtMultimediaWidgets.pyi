#############################################################################
##
## Copyright (C) 2021 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtMultimediaWidgets, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtMultimediaWidgets`

import PySide6.QtMultimediaWidgets
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import PySide6.QtMultimedia

from typing import Any, Optional, Union


class QGraphicsVideoItem(PySide6.QtWidgets.QGraphicsObject):

    def __init__(self, parent: Optional[PySide6.QtWidgets.QGraphicsItem] = ...) -> None: ...

    def aspectRatioMode(self) -> PySide6.QtCore.Qt.AspectRatioMode: ...
    def boundingRect(self) -> PySide6.QtCore.QRectF: ...
    def itemChange(self, change: PySide6.QtWidgets.QGraphicsItem.GraphicsItemChange, value: Any) -> Any: ...
    def nativeSize(self) -> PySide6.QtCore.QSizeF: ...
    def offset(self) -> PySide6.QtCore.QPointF: ...
    def paint(self, painter: PySide6.QtGui.QPainter, option: PySide6.QtWidgets.QStyleOptionGraphicsItem, widget: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...
    def setAspectRatioMode(self, mode: PySide6.QtCore.Qt.AspectRatioMode) -> None: ...
    def setOffset(self, offset: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]) -> None: ...
    def setSize(self, size: Union[PySide6.QtCore.QSizeF, PySide6.QtCore.QSize]) -> None: ...
    def size(self) -> PySide6.QtCore.QSizeF: ...
    def timerEvent(self, event: PySide6.QtCore.QTimerEvent) -> None: ...
    def type(self) -> int: ...
    def videoSink(self) -> PySide6.QtMultimedia.QVideoSink: ...


class QIntList(object): ...


class QVideoWidget(PySide6.QtWidgets.QWidget):

    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...

    def aspectRatioMode(self) -> PySide6.QtCore.Qt.AspectRatioMode: ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool: ...
    def hideEvent(self, event: PySide6.QtGui.QHideEvent) -> None: ...
    def moveEvent(self, event: PySide6.QtGui.QMoveEvent) -> None: ...
    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None: ...
    def setAspectRatioMode(self, mode: PySide6.QtCore.Qt.AspectRatioMode) -> None: ...
    def setFullScreen(self, fullScreen: bool) -> None: ...
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def videoSink(self) -> PySide6.QtMultimedia.QVideoSink: ...


# eof
