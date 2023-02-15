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
PySide6.QtWebEngineQuick, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtWebEngineQuick`

import PySide6.QtWebEngineQuick
import PySide6.QtCore

from typing import Optional, Union, Sequence, List
from shiboken6 import Shiboken


class QIntList(object): ...


class QQuickWebEngineProfile(PySide6.QtCore.QObject):

    MemoryHttpCache          : QQuickWebEngineProfile.HttpCacheType = ... # 0x0
    DiskHttpCache            : QQuickWebEngineProfile.HttpCacheType = ... # 0x1
    NoCache                  : QQuickWebEngineProfile.HttpCacheType = ... # 0x2
    NoPersistentCookies      : QQuickWebEngineProfile.PersistentCookiesPolicy = ... # 0x0
    AllowPersistentCookies   : QQuickWebEngineProfile.PersistentCookiesPolicy = ... # 0x1
    ForcePersistentCookies   : QQuickWebEngineProfile.PersistentCookiesPolicy = ... # 0x2

    class HttpCacheType(Shiboken.Enum):

        MemoryHttpCache          : QQuickWebEngineProfile.HttpCacheType = ... # 0x0
        DiskHttpCache            : QQuickWebEngineProfile.HttpCacheType = ... # 0x1
        NoCache                  : QQuickWebEngineProfile.HttpCacheType = ... # 0x2

    class PersistentCookiesPolicy(Shiboken.Enum):

        NoPersistentCookies      : QQuickWebEngineProfile.PersistentCookiesPolicy = ... # 0x0
        AllowPersistentCookies   : QQuickWebEngineProfile.PersistentCookiesPolicy = ... # 0x1
        ForcePersistentCookies   : QQuickWebEngineProfile.PersistentCookiesPolicy = ... # 0x2


    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def cachePath(self) -> str: ...
    def clearHttpCache(self) -> None: ...
    @staticmethod
    def defaultProfile() -> PySide6.QtWebEngineQuick.QQuickWebEngineProfile: ...
    def downloadPath(self) -> str: ...
    def httpAcceptLanguage(self) -> str: ...
    def httpCacheMaximumSize(self) -> int: ...
    def httpCacheType(self) -> PySide6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType: ...
    def httpUserAgent(self) -> str: ...
    def isOffTheRecord(self) -> bool: ...
    def isSpellCheckEnabled(self) -> bool: ...
    def persistentCookiesPolicy(self) -> PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy: ...
    def persistentStoragePath(self) -> str: ...
    def removeAllUrlSchemeHandlers(self) -> None: ...
    def removeUrlScheme(self, scheme: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    def setCachePath(self, path: str) -> None: ...
    def setDownloadPath(self, path: str) -> None: ...
    def setHttpAcceptLanguage(self, httpAcceptLanguage: str) -> None: ...
    def setHttpCacheMaximumSize(self, maxSize: int) -> None: ...
    def setHttpCacheType(self, arg__1: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType) -> None: ...
    def setHttpUserAgent(self, userAgent: str) -> None: ...
    def setOffTheRecord(self, offTheRecord: bool) -> None: ...
    def setPersistentCookiesPolicy(self, arg__1: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy) -> None: ...
    def setPersistentStoragePath(self, path: str) -> None: ...
    def setSpellCheckEnabled(self, enabled: bool) -> None: ...
    def setSpellCheckLanguages(self, languages: Sequence[str]) -> None: ...
    def setStorageName(self, name: str) -> None: ...
    def spellCheckLanguages(self) -> List[str]: ...
    def storageName(self) -> str: ...


class QtWebEngineQuick(Shiboken.Object):
    @staticmethod
    def initialize() -> None: ...


# eof
