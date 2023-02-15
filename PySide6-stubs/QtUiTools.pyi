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
PySide6.QtUiTools, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtUiTools`

import PySide6.QtUiTools
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

import os
from typing import Optional, Union, List, overload


class QIntList(object): ...


class QUiLoader(PySide6.QtCore.QObject):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def addPluginPath(self, path: str) -> None: ...
    def availableLayouts(self) -> List[str]: ...
    def availableWidgets(self) -> List[str]: ...
    def clearPluginPaths(self) -> None: ...
    def createAction(self, parent: Optional[PySide6.QtCore.QObject] = ..., name: str = ...) -> PySide6.QtGui.QAction: ...
    def createActionGroup(self, parent: Optional[PySide6.QtCore.QObject] = ..., name: str = ...) -> PySide6.QtGui.QActionGroup: ...
    def createLayout(self, className: str, parent: Optional[PySide6.QtCore.QObject] = ..., name: str = ...) -> PySide6.QtWidgets.QLayout: ...
    def createWidget(self, className: str, parent: Optional[PySide6.QtWidgets.QWidget] = ..., name: str = ...) -> PySide6.QtWidgets.QWidget: ...
    def errorString(self) -> str: ...
    def isLanguageChangeEnabled(self) -> bool: ...
    def isTranslationEnabled(self) -> bool: ...
    @overload
    def load(self, arg__1: Union[str, bytes, os.PathLike], parentWidget: Optional[PySide6.QtWidgets.QWidget] = ...) -> PySide6.QtWidgets.QWidget: ...
    @overload
    def load(self, device: PySide6.QtCore.QIODevice, parentWidget: Optional[PySide6.QtWidgets.QWidget] = ...) -> PySide6.QtWidgets.QWidget: ...
    def pluginPaths(self) -> List[str]: ...
    def registerCustomWidget(self, customWidgetType: object) -> None: ...
    def setLanguageChangeEnabled(self, enabled: bool) -> None: ...
    def setTranslationEnabled(self, enabled: bool) -> None: ...
    def setWorkingDirectory(self, dir: Union[PySide6.QtCore.QDir, str]) -> None: ...
    def workingDirectory(self) -> PySide6.QtCore.QDir: ...


def loadUiType(uifile: str) -> object: ...


# eof
