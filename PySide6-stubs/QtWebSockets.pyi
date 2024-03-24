# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtWebSockets, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtWebSockets`

import PySide6.QtWebSockets
import PySide6.QtCore
import PySide6.QtNetwork

import enum
from typing import ClassVar, List, Optional, Sequence, Union, overload
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


NoneType = type(None)


class QIntList(object): ...


class QMaskGenerator(PySide6.QtCore.QObject):

    destroyed                : ClassVar[Signal] = ... # destroyed()
    objectNameChanged        : ClassVar[Signal] = ... # objectNameChanged(QString)

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def nextMask(self) -> int: ...
    def seed(self) -> bool: ...


class QWebSocket(PySide6.QtCore.QObject):

    aboutToClose             : ClassVar[Signal] = ... # aboutToClose()
    alertReceived            : ClassVar[Signal] = ... # alertReceived(QSsl::AlertLevel,QSsl::AlertType,QString)
    alertSent                : ClassVar[Signal] = ... # alertSent(QSsl::AlertLevel,QSsl::AlertType,QString)
    binaryFrameReceived      : ClassVar[Signal] = ... # binaryFrameReceived(QByteArray,bool)
    binaryMessageReceived    : ClassVar[Signal] = ... # binaryMessageReceived(QByteArray)
    bytesWritten             : ClassVar[Signal] = ... # bytesWritten(qlonglong)
    connected                : ClassVar[Signal] = ... # connected()
    disconnected             : ClassVar[Signal] = ... # disconnected()
    error                    : ClassVar[Signal] = ... # error(QAbstractSocket::SocketError)
    errorOccurred            : ClassVar[Signal] = ... # errorOccurred(QAbstractSocket::SocketError)
    handshakeInterruptedOnError: ClassVar[Signal] = ... # handshakeInterruptedOnError(QSslError)
    peerVerifyError          : ClassVar[Signal] = ... # peerVerifyError(QSslError)
    pong                     : ClassVar[Signal] = ... # pong(qulonglong,QByteArray)
    preSharedKeyAuthenticationRequired: ClassVar[Signal] = ... # preSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator*)
    proxyAuthenticationRequired: ClassVar[Signal] = ... # proxyAuthenticationRequired(QNetworkProxy,QAuthenticator*)
    readChannelFinished      : ClassVar[Signal] = ... # readChannelFinished()
    sslErrors                : ClassVar[Signal] = ... # sslErrors(QList<QSslError>)
    stateChanged             : ClassVar[Signal] = ... # stateChanged(QAbstractSocket::SocketState)
    textFrameReceived        : ClassVar[Signal] = ... # textFrameReceived(QString,bool)
    textMessageReceived      : ClassVar[Signal] = ... # textMessageReceived(QString)

    def __init__(self, origin: str = ..., version: PySide6.QtWebSockets.QWebSocketProtocol.Version = ..., parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def abort(self) -> None: ...
    def bytesToWrite(self) -> int: ...
    def close(self, closeCode: PySide6.QtWebSockets.QWebSocketProtocol.CloseCode = ..., reason: str = ...) -> None: ...
    def closeCode(self) -> PySide6.QtWebSockets.QWebSocketProtocol.CloseCode: ...
    def closeReason(self) -> str: ...
    def continueInterruptedHandshake(self) -> None: ...
    def errorString(self) -> str: ...
    def flush(self) -> bool: ...
    def handshakeOptions(self) -> PySide6.QtWebSockets.QWebSocketHandshakeOptions: ...
    @overload
    def ignoreSslErrors(self) -> None: ...
    @overload
    def ignoreSslErrors(self, errors: Sequence[PySide6.QtNetwork.QSslError]) -> None: ...
    def isValid(self) -> bool: ...
    def localAddress(self) -> PySide6.QtNetwork.QHostAddress: ...
    def localPort(self) -> int: ...
    def maskGenerator(self) -> PySide6.QtWebSockets.QMaskGenerator: ...
    def maxAllowedIncomingFrameSize(self) -> int: ...
    def maxAllowedIncomingMessageSize(self) -> int: ...
    @staticmethod
    def maxIncomingFrameSize() -> int: ...
    @staticmethod
    def maxIncomingMessageSize() -> int: ...
    @staticmethod
    def maxOutgoingFrameSize() -> int: ...
    @overload
    def open(self, request: PySide6.QtNetwork.QNetworkRequest) -> None: ...
    @overload
    def open(self, request: PySide6.QtNetwork.QNetworkRequest, options: PySide6.QtWebSockets.QWebSocketHandshakeOptions) -> None: ...
    @overload
    def open(self, url: Union[PySide6.QtCore.QUrl, str]) -> None: ...
    @overload
    def open(self, url: Union[PySide6.QtCore.QUrl, str], options: PySide6.QtWebSockets.QWebSocketHandshakeOptions) -> None: ...
    def origin(self) -> str: ...
    def outgoingFrameSize(self) -> int: ...
    def pauseMode(self) -> PySide6.QtNetwork.QAbstractSocket.PauseMode: ...
    def peerAddress(self) -> PySide6.QtNetwork.QHostAddress: ...
    def peerName(self) -> str: ...
    def peerPort(self) -> int: ...
    def ping(self, payload: Union[PySide6.QtCore.QByteArray, bytes] = ...) -> None: ...
    def proxy(self) -> PySide6.QtNetwork.QNetworkProxy: ...
    def readBufferSize(self) -> int: ...
    def request(self) -> PySide6.QtNetwork.QNetworkRequest: ...
    def requestUrl(self) -> PySide6.QtCore.QUrl: ...
    def resourceName(self) -> str: ...
    def resume(self) -> None: ...
    def sendBinaryMessage(self, data: Union[PySide6.QtCore.QByteArray, bytes]) -> int: ...
    def sendTextMessage(self, message: str) -> int: ...
    def setMaskGenerator(self, maskGenerator: PySide6.QtWebSockets.QMaskGenerator) -> None: ...
    def setMaxAllowedIncomingFrameSize(self, maxAllowedIncomingFrameSize: int) -> None: ...
    def setMaxAllowedIncomingMessageSize(self, maxAllowedIncomingMessageSize: int) -> None: ...
    def setOutgoingFrameSize(self, outgoingFrameSize: int) -> None: ...
    def setPauseMode(self, pauseMode: PySide6.QtNetwork.QAbstractSocket.PauseMode) -> None: ...
    def setProxy(self, networkProxy: Union[PySide6.QtNetwork.QNetworkProxy, PySide6.QtNetwork.QNetworkProxy.ProxyType]) -> None: ...
    def setReadBufferSize(self, size: int) -> None: ...
    def setSslConfiguration(self, sslConfiguration: PySide6.QtNetwork.QSslConfiguration) -> None: ...
    def sslConfiguration(self) -> PySide6.QtNetwork.QSslConfiguration: ...
    def state(self) -> PySide6.QtNetwork.QAbstractSocket.SocketState: ...
    def subprotocol(self) -> str: ...
    def version(self) -> PySide6.QtWebSockets.QWebSocketProtocol.Version: ...


class QWebSocketCorsAuthenticator(Shiboken.Object):

    @overload
    def __init__(self, origin: str) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtWebSockets.QWebSocketCorsAuthenticator) -> None: ...

    def allowed(self) -> bool: ...
    def origin(self) -> str: ...
    def setAllowed(self, allowed: bool) -> None: ...
    def swap(self, other: PySide6.QtWebSockets.QWebSocketCorsAuthenticator) -> None: ...


class QWebSocketHandshakeOptions(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtWebSockets.QWebSocketHandshakeOptions) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def setSubprotocols(self, protocols: Sequence[str]) -> None: ...
    def subprotocols(self) -> List[str]: ...
    def swap(self, other: PySide6.QtWebSockets.QWebSocketHandshakeOptions) -> None: ...


class QWebSocketProtocol(Shiboken.Object):

    class CloseCode(enum.Enum):

        CloseCodeNormal          : QWebSocketProtocol.CloseCode = ... # 0x3e8
        CloseCodeGoingAway       : QWebSocketProtocol.CloseCode = ... # 0x3e9
        CloseCodeProtocolError   : QWebSocketProtocol.CloseCode = ... # 0x3ea
        CloseCodeDatatypeNotSupported: QWebSocketProtocol.CloseCode = ... # 0x3eb
        CloseCodeReserved1004    : QWebSocketProtocol.CloseCode = ... # 0x3ec
        CloseCodeMissingStatusCode: QWebSocketProtocol.CloseCode = ... # 0x3ed
        CloseCodeAbnormalDisconnection: QWebSocketProtocol.CloseCode = ... # 0x3ee
        CloseCodeWrongDatatype   : QWebSocketProtocol.CloseCode = ... # 0x3ef
        CloseCodePolicyViolated  : QWebSocketProtocol.CloseCode = ... # 0x3f0
        CloseCodeTooMuchData     : QWebSocketProtocol.CloseCode = ... # 0x3f1
        CloseCodeMissingExtension: QWebSocketProtocol.CloseCode = ... # 0x3f2
        CloseCodeBadOperation    : QWebSocketProtocol.CloseCode = ... # 0x3f3
        CloseCodeTlsHandshakeFailed: QWebSocketProtocol.CloseCode = ... # 0x3f7


    class Version(enum.Enum):

        VersionUnknown           : QWebSocketProtocol.Version = ... # -0x1
        Version0                 : QWebSocketProtocol.Version = ... # 0x0
        Version4                 : QWebSocketProtocol.Version = ... # 0x4
        Version5                 : QWebSocketProtocol.Version = ... # 0x5
        Version6                 : QWebSocketProtocol.Version = ... # 0x6
        Version7                 : QWebSocketProtocol.Version = ... # 0x7
        Version8                 : QWebSocketProtocol.Version = ... # 0x8
        Version13                : QWebSocketProtocol.Version = ... # 0xd
        VersionLatest            : QWebSocketProtocol.Version = ... # 0xd


class QWebSocketServer(PySide6.QtCore.QObject):

    acceptError              : ClassVar[Signal] = ... # acceptError(QAbstractSocket::SocketError)
    alertReceived            : ClassVar[Signal] = ... # alertReceived(QSsl::AlertLevel,QSsl::AlertType,QString)
    alertSent                : ClassVar[Signal] = ... # alertSent(QSsl::AlertLevel,QSsl::AlertType,QString)
    closed                   : ClassVar[Signal] = ... # closed()
    handshakeInterruptedOnError: ClassVar[Signal] = ... # handshakeInterruptedOnError(QSslError)
    newConnection            : ClassVar[Signal] = ... # newConnection()
    originAuthenticationRequired: ClassVar[Signal] = ... # originAuthenticationRequired(QWebSocketCorsAuthenticator*)
    peerVerifyError          : ClassVar[Signal] = ... # peerVerifyError(QSslError)
    preSharedKeyAuthenticationRequired: ClassVar[Signal] = ... # preSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator*)
    serverError              : ClassVar[Signal] = ... # serverError(QWebSocketProtocol::CloseCode)
    sslErrors                : ClassVar[Signal] = ... # sslErrors(QList<QSslError>)

    class SslMode(enum.Enum):

        SecureMode               : QWebSocketServer.SslMode = ... # 0x0
        NonSecureMode            : QWebSocketServer.SslMode = ... # 0x1


    def __init__(self, serverName: str, secureMode: PySide6.QtWebSockets.QWebSocketServer.SslMode, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def close(self) -> None: ...
    def error(self) -> PySide6.QtWebSockets.QWebSocketProtocol.CloseCode: ...
    def errorString(self) -> str: ...
    def handleConnection(self, socket: PySide6.QtNetwork.QTcpSocket) -> None: ...
    def handshakeTimeoutMS(self) -> int: ...
    def hasPendingConnections(self) -> bool: ...
    def isListening(self) -> bool: ...
    def listen(self, address: Union[PySide6.QtNetwork.QHostAddress, PySide6.QtNetwork.QHostAddress.SpecialAddress] = ..., port: int = ...) -> bool: ...
    def maxPendingConnections(self) -> int: ...
    def nativeDescriptor(self) -> int: ...
    def nextPendingConnection(self) -> PySide6.QtWebSockets.QWebSocket: ...
    def pauseAccepting(self) -> None: ...
    def proxy(self) -> PySide6.QtNetwork.QNetworkProxy: ...
    def resumeAccepting(self) -> None: ...
    def secureMode(self) -> PySide6.QtWebSockets.QWebSocketServer.SslMode: ...
    def serverAddress(self) -> PySide6.QtNetwork.QHostAddress: ...
    def serverName(self) -> str: ...
    def serverPort(self) -> int: ...
    def serverUrl(self) -> PySide6.QtCore.QUrl: ...
    def setHandshakeTimeout(self, msec: int) -> None: ...
    def setMaxPendingConnections(self, numConnections: int) -> None: ...
    def setNativeDescriptor(self, descriptor: int) -> bool: ...
    def setProxy(self, networkProxy: Union[PySide6.QtNetwork.QNetworkProxy, PySide6.QtNetwork.QNetworkProxy.ProxyType]) -> None: ...
    def setServerName(self, serverName: str) -> None: ...
    def setSocketDescriptor(self, socketDescriptor: int) -> bool: ...
    def setSslConfiguration(self, sslConfiguration: PySide6.QtNetwork.QSslConfiguration) -> None: ...
    def setSupportedSubprotocols(self, protocols: Sequence[str]) -> None: ...
    def socketDescriptor(self) -> int: ...
    def sslConfiguration(self) -> PySide6.QtNetwork.QSslConfiguration: ...
    def supportedSubprotocols(self) -> List[str]: ...
    def supportedVersions(self) -> List[PySide6.QtWebSockets.QWebSocketProtocol.Version]: ...


# eof
