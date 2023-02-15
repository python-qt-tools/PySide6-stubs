# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.Qt3DLogic, except for defaults which are replaced by "...".
"""

# Module `PySide6.Qt3DLogic`

import PySide6.Qt3DLogic
import PySide6.QtCore
import PySide6.Qt3DCore

from typing import Optional
from shiboken6 import Shiboken


class QIntList(object): ...


class Qt3DLogic(Shiboken.Object):

    class QFrameAction(PySide6.Qt3DCore.Qt3DCore.QComponent):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...


    class QLogicAspect(PySide6.Qt3DCore.Qt3DCore.QAbstractAspect):

        def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...


# eof
