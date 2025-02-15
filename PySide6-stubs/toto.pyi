# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtCore, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtCore`

import PySide6.QtCore

import os
import enum
from typing import Any, Callable, ClassVar, Dict, List, Optional, Sequence, Tuple, Union, overload, Type, TypeVar
from shiboken6 import Shiboken
import datetime


NoneType = type(None)



class QAbstractAnimation(PySide6.QtCore.QObject):
    toto       : PySide6.QtCore.Signal = ...
    titi       : PySide6.QtCore.Signal

    def __init__(self) -> None: ...


