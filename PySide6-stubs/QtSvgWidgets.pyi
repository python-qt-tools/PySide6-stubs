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
PySide6.QtSvgWidgets, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtSvgWidgets`

import PySide6.QtSvgWidgets
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import PySide6.QtSvg

from typing import Optional, Union, overload


class QGraphicsSvgItem(PySide6.QtWidgets.QGraphicsObject):

    @overload
    def __init__(self, fileName: str, parentItem: Optional[PySide6.QtWidgets.QGraphicsItem] = ...) -> None: ...
    @overload
    def __init__(self, parentItem: Optional[PySide6.QtWidgets.QGraphicsItem] = ...) -> None: ...

    def boundingRect(self) -> PySide6.QtCore.QRectF: ...
    def elementId(self) -> str: ...
    def isCachingEnabled(self) -> bool: ...
    def maximumCacheSize(self) -> PySide6.QtCore.QSize: ...
    def paint(self, painter: PySide6.QtGui.QPainter, option: PySide6.QtWidgets.QStyleOptionGraphicsItem, widget: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...
    def renderer(self) -> PySide6.QtSvg.QSvgRenderer: ...
    def setCachingEnabled(self, arg__1: bool) -> None: ...
    def setElementId(self, id: str) -> None: ...
    def setMaximumCacheSize(self, size: PySide6.QtCore.QSize) -> None: ...
    def setSharedRenderer(self, renderer: PySide6.QtSvg.QSvgRenderer) -> None: ...
    def type(self) -> int: ...


class QIntList(object): ...


class QSvgWidget(PySide6.QtWidgets.QWidget):

    @overload
    def __init__(self, file: str, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...

    @overload
    def load(self, contents: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    @overload
    def load(self, file: str) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...
    def renderer(self) -> PySide6.QtSvg.QSvgRenderer: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...


# eof
