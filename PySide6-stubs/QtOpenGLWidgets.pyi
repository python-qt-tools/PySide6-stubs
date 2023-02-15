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
PySide6.QtOpenGLWidgets, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtOpenGLWidgets`

import PySide6.QtOpenGLWidgets
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

from typing import Optional, Union
from shiboken6 import Shiboken


class QIntList(object): ...


class QOpenGLWidget(PySide6.QtWidgets.QWidget):

    NoPartialUpdate          : QOpenGLWidget.UpdateBehavior = ... # 0x0
    PartialUpdate            : QOpenGLWidget.UpdateBehavior = ... # 0x1

    class UpdateBehavior(Shiboken.Enum):

        NoPartialUpdate          : QOpenGLWidget.UpdateBehavior = ... # 0x0
        PartialUpdate            : QOpenGLWidget.UpdateBehavior = ... # 0x1


    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ..., f: PySide6.QtCore.Qt.WindowFlags = ...) -> None: ...

    def context(self) -> PySide6.QtGui.QOpenGLContext: ...
    def defaultFramebufferObject(self) -> int: ...
    def doneCurrent(self) -> None: ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    def format(self) -> PySide6.QtGui.QSurfaceFormat: ...
    def grabFramebuffer(self) -> PySide6.QtGui.QImage: ...
    def initializeGL(self) -> None: ...
    def isValid(self) -> bool: ...
    def makeCurrent(self) -> None: ...
    def metric(self, metric: PySide6.QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def paintEngine(self) -> PySide6.QtGui.QPaintEngine: ...
    def paintEvent(self, e: PySide6.QtGui.QPaintEvent) -> None: ...
    def paintGL(self) -> None: ...
    def redirected(self, p: PySide6.QtCore.QPoint) -> PySide6.QtGui.QPaintDevice: ...
    def resizeEvent(self, e: PySide6.QtGui.QResizeEvent) -> None: ...
    def resizeGL(self, w: int, h: int) -> None: ...
    def setFormat(self, format: Union[PySide6.QtGui.QSurfaceFormat, PySide6.QtGui.QSurfaceFormat.FormatOptions]) -> None: ...
    def setTextureFormat(self, texFormat: int) -> None: ...
    def setUpdateBehavior(self, updateBehavior: PySide6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior) -> None: ...
    def textureFormat(self) -> int: ...
    def updateBehavior(self) -> PySide6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior: ...


# eof
