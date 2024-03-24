# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtQuickControls2, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtQuickControls2`

import PySide6.QtQuickControls2

from shiboken6 import Shiboken


NoneType = type(None)


class QIntList(object): ...


class QQuickStyle(Shiboken.Object):

    def __init__(self) -> None: ...

    @staticmethod
    def name() -> str: ...
    @staticmethod
    def setFallbackStyle(style: str) -> None: ...
    @staticmethod
    def setStyle(style: str) -> None: ...


# eof
