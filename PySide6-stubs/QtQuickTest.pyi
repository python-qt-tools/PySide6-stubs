# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtQuickTest, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtQuickTest`

import PySide6.QtQuickTest

from typing import Sequence
from typing import TypeAlias, TypeVar


NoneType: TypeAlias = type[None]
PlaceHolderType = TypeVar("PlaceHolderType", bound=QObject)


class QIntList(object): ...


def QUICK_TEST_MAIN(name: str, argv: Sequence[str] = ..., dir: str = ...) -> int: ...
def QUICK_TEST_MAIN_WITH_SETUP(name: str, setup: type, argv: Sequence[str] = ..., dir: str = ...) -> int: ...


# eof
