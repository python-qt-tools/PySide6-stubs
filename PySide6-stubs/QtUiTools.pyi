# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations
"""
This file contains the exact signatures for all functions in module
PySide6.QtUiTools, except for defaults which are replaced by "...".

# mypy: disable-error-code="override, overload-overlap"
"""

# Module `PySide6.QtUiTools`

import PySide6.QtUiTools
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

import os
import typing


class QIntList(object): ...


class QUiLoader(PySide6.QtCore.QObject):

    def __init__(self, /, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def addPluginPath(self, path: str, /) -> None: ...
    def availableLayouts(self, /) -> typing.List[str]: ...
    def availableWidgets(self, /) -> typing.List[str]: ...
    def clearPluginPaths(self, /) -> None: ...
    def createAction(self, /, parent: PySide6.QtCore.QObject | None= ..., name: str = ...) -> PySide6.QtGui.QAction: ...
    def createActionGroup(self, /, parent: PySide6.QtCore.QObject | None= ..., name: str = ...) -> PySide6.QtGui.QActionGroup: ...
    def createLayout(self, className: str, /, parent: PySide6.QtCore.QObject | None= ..., name: str = ...) -> PySide6.QtWidgets.QLayout: ...
    def createWidget(self, className: str, /, parent: PySide6.QtWidgets.QWidget | None= ..., name: str = ...) -> PySide6.QtWidgets.QWidget: ...
    def errorString(self, /) -> str: ...
    def isLanguageChangeEnabled(self, /) -> bool: ...
    def isTranslationEnabled(self, /) -> bool: ...
    @typing.overload
    def load(self, device: PySide6.QtCore.QIODevice, /, parentWidget: PySide6.QtWidgets.QWidget | None= ...) -> PySide6.QtWidgets.QWidget: ...
    @typing.overload
    def load(self, arg__1: str | bytes | os.PathLike[str], /, parentWidget: PySide6.QtWidgets.QWidget | None= ...) -> PySide6.QtWidgets.QWidget: ...
    def pluginPaths(self, /) -> typing.List[str]: ...
    def registerCustomWidget(self, customWidgetType: object, /) -> None: ...
    def setLanguageChangeEnabled(self, enabled: bool, /) -> None: ...
    def setTranslationEnabled(self, enabled: bool, /) -> None: ...
    def setWorkingDirectory(self, dir: PySide6.QtCore.QDir, /) -> None: ...
    def workingDirectory(self, /) -> PySide6.QtCore.QDir: ...


def loadUiType(uifile: str, /) -> object: ...


# eof
