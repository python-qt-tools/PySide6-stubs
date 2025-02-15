# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtNetworkAuth, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtNetworkAuth`

import PySide6.QtNetworkAuth
import PySide6.QtCore
import PySide6.QtNetwork

import enum
from typing import Any, ClassVar, Dict, List, Optional, Tuple, Type, Union, overload
from PySide6.QtCore import Signal
from shiboken6 import Shiboken
from typing import TypeAlias, TypeVar


NoneType: TypeAlias = type[None]
PlaceHolderType = TypeVar("PlaceHolderType", bound=QObject)


class QAbstractOAuth(PySide6.QtCore.QObject):

    authorizationUrlChanged  : ClassVar[Signal] = ... # authorizationUrlChanged(QUrl)
    authorizeWithBrowser     : ClassVar[Signal] = ... # authorizeWithBrowser(QUrl)
    clientIdentifierChanged  : ClassVar[Signal] = ... # clientIdentifierChanged(QString)
    contentTypeChanged       : ClassVar[Signal] = ... # contentTypeChanged(ContentType)
    extraTokensChanged       : ClassVar[Signal] = ... # extraTokensChanged(QVariantMap)
    finished                 : ClassVar[Signal] = ... # finished(QNetworkReply*)
    granted                  : ClassVar[Signal] = ... # granted()
    replyDataReceived        : ClassVar[Signal] = ... # replyDataReceived(QByteArray)
    requestFailed            : ClassVar[Signal] = ... # requestFailed(Error)
    statusChanged            : ClassVar[Signal] = ... # statusChanged(Status)
    tokenChanged             : ClassVar[Signal] = ... # tokenChanged(QString)

    class ContentType(enum.Enum):

        WwwFormUrlEncoded        : QAbstractOAuth.ContentType = ... # 0x0
        Json                     : QAbstractOAuth.ContentType = ... # 0x1

    class Error(enum.Enum):

        NoError                  : QAbstractOAuth.Error = ... # 0x0
        NetworkError             : QAbstractOAuth.Error = ... # 0x1
        ServerError              : QAbstractOAuth.Error = ... # 0x2
        OAuthTokenNotFoundError  : QAbstractOAuth.Error = ... # 0x3
        OAuthTokenSecretNotFoundError: QAbstractOAuth.Error = ... # 0x4
        OAuthCallbackNotVerified : QAbstractOAuth.Error = ... # 0x5

    class Stage(enum.Enum):

        RequestingTemporaryCredentials: QAbstractOAuth.Stage = ... # 0x0
        RequestingAuthorization  : QAbstractOAuth.Stage = ... # 0x1
        RequestingAccessToken    : QAbstractOAuth.Stage = ... # 0x2
        RefreshingAccessToken    : QAbstractOAuth.Stage = ... # 0x3

    class Status(enum.Enum):

        NotAuthenticated         : QAbstractOAuth.Status = ... # 0x0
        TemporaryCredentialsReceived: QAbstractOAuth.Status = ... # 0x1
        Granted                  : QAbstractOAuth.Status = ... # 0x2
        RefreshingToken          : QAbstractOAuth.Status = ... # 0x3


    def authorizationUrl(self) -> PySide6.QtCore.QUrl: ...
    def callback(self) -> str: ...
    def clientIdentifier(self) -> str: ...
    def contentType(self) -> PySide6.QtNetworkAuth.QAbstractOAuth.ContentType: ...
    def deleteResource(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def extraTokens(self) -> Dict[str, Any]: ...
    @staticmethod
    def generateRandomString(length: int) -> PySide6.QtCore.QByteArray: ...
    def get(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def grant(self) -> None: ...
    def head(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def networkAccessManager(self) -> PySide6.QtNetwork.QNetworkAccessManager: ...
    def post(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def prepareRequest(self, request: PySide6.QtNetwork.QNetworkRequest, verb: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], body: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview] = ...) -> None: ...
    def put(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def replyHandler(self) -> PySide6.QtNetworkAuth.QAbstractOAuthReplyHandler: ...
    def resourceOwnerAuthorization(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any]) -> None: ...
    def setAuthorizationUrl(self, url: Union[PySide6.QtCore.QUrl, str]) -> None: ...
    def setClientIdentifier(self, clientIdentifier: str) -> None: ...
    def setContentType(self, contentType: PySide6.QtNetworkAuth.QAbstractOAuth.ContentType) -> None: ...
    def setModifyParametersFunction(self, modifyParametersFunction: object) -> None: ...
    def setNetworkAccessManager(self, networkAccessManager: PySide6.QtNetwork.QNetworkAccessManager) -> None: ...
    def setReplyHandler(self, handler: PySide6.QtNetworkAuth.QAbstractOAuthReplyHandler) -> None: ...
    def setStatus(self, status: PySide6.QtNetworkAuth.QAbstractOAuth.Status) -> None: ...
    def setToken(self, token: str) -> None: ...
    def status(self) -> PySide6.QtNetworkAuth.QAbstractOAuth.Status: ...
    def token(self) -> str: ...


class QAbstractOAuth2(PySide6.QtNetworkAuth.QAbstractOAuth):

    authorizationCallbackReceived: ClassVar[Signal] = ... # authorizationCallbackReceived(QVariantMap)
    clientIdentifierSharedKeyChanged: ClassVar[Signal] = ... # clientIdentifierSharedKeyChanged(QString)
    error                    : ClassVar[Signal] = ... # error(QString,QString,QUrl)
    expirationAtChanged      : ClassVar[Signal] = ... # expirationAtChanged(QDateTime)
    refreshTokenChanged      : ClassVar[Signal] = ... # refreshTokenChanged(QString)
    responseTypeChanged      : ClassVar[Signal] = ... # responseTypeChanged(QString)
    scopeChanged             : ClassVar[Signal] = ... # scopeChanged(QString)
    sslConfigurationChanged  : ClassVar[Signal] = ... # sslConfigurationChanged(QSslConfiguration)
    stateChanged             : ClassVar[Signal] = ... # stateChanged(QString)
    userAgentChanged         : ClassVar[Signal] = ... # userAgentChanged(QString)

    @overload
    def __init__(self, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def clientIdentifierSharedKey(self) -> str: ...
    def createAuthenticatedUrl(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtCore.QUrl: ...
    def deleteResource(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def expirationAt(self) -> PySide6.QtCore.QDateTime: ...
    def get(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def head(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    @overload
    def post(self, url: Union[PySide6.QtCore.QUrl, str], data: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> PySide6.QtNetwork.QNetworkReply: ...
    @overload
    def post(self, url: Union[PySide6.QtCore.QUrl, str], multiPart: PySide6.QtNetwork.QHttpMultiPart) -> PySide6.QtNetwork.QNetworkReply: ...
    @overload
    def post(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def prepareRequest(self, request: PySide6.QtNetwork.QNetworkRequest, verb: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], body: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview] = ...) -> None: ...
    @overload
    def put(self, url: Union[PySide6.QtCore.QUrl, str], data: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> PySide6.QtNetwork.QNetworkReply: ...
    @overload
    def put(self, url: Union[PySide6.QtCore.QUrl, str], multiPart: PySide6.QtNetwork.QHttpMultiPart) -> PySide6.QtNetwork.QNetworkReply: ...
    @overload
    def put(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def refreshToken(self) -> str: ...
    def responseType(self) -> str: ...
    def scope(self) -> str: ...
    def setClientIdentifierSharedKey(self, clientIdentifierSharedKey: str) -> None: ...
    def setRefreshToken(self, refreshToken: str) -> None: ...
    def setResponseType(self, responseType: str) -> None: ...
    def setScope(self, scope: str) -> None: ...
    def setSslConfiguration(self, configuration: PySide6.QtNetwork.QSslConfiguration) -> None: ...
    def setState(self, state: str) -> None: ...
    def setUserAgent(self, userAgent: str) -> None: ...
    def sslConfiguration(self) -> PySide6.QtNetwork.QSslConfiguration: ...
    def state(self) -> str: ...
    def userAgent(self) -> str: ...


class QAbstractOAuthReplyHandler(PySide6.QtCore.QObject):

    callbackDataReceived     : ClassVar[Signal] = ... # callbackDataReceived(QByteArray)
    callbackReceived         : ClassVar[Signal] = ... # callbackReceived(QVariantMap)
    replyDataReceived        : ClassVar[Signal] = ... # replyDataReceived(QByteArray)
    tokenRequestErrorOccurred: ClassVar[Signal] = ... # tokenRequestErrorOccurred(QAbstractOAuth::Error,QString)
    tokensReceived           : ClassVar[Signal] = ... # tokensReceived(QVariantMap)

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def callback(self) -> str: ...
    def networkReplyFinished(self, reply: PySide6.QtNetwork.QNetworkReply) -> None: ...


class QIntList(object): ...


class QOAuth1(PySide6.QtNetworkAuth.QAbstractOAuth):

    clientSharedSecretChanged: ClassVar[Signal] = ... # clientSharedSecretChanged(QString)
    signatureMethodChanged   : ClassVar[Signal] = ... # signatureMethodChanged(QOAuth1::SignatureMethod)
    temporaryCredentialsUrlChanged: ClassVar[Signal] = ... # temporaryCredentialsUrlChanged(QUrl)
    tokenCredentialsUrlChanged: ClassVar[Signal] = ... # tokenCredentialsUrlChanged(QUrl)
    tokenSecretChanged       : ClassVar[Signal] = ... # tokenSecretChanged(QString)

    class SignatureMethod(enum.Enum):

        Hmac_Sha1                : QOAuth1.SignatureMethod = ... # 0x0
        Rsa_Sha1                 : QOAuth1.SignatureMethod = ... # 0x1
        PlainText                : QOAuth1.SignatureMethod = ... # 0x2


    @overload
    def __init__(self, clientIdentifier: str, clientSharedSecret: str, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def clientCredentials(self) -> Tuple[str, str]: ...
    def clientSharedSecret(self) -> str: ...
    def continueGrantWithVerifier(self, verifier: str) -> None: ...
    def deleteResource(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    @staticmethod
    def generateAuthorizationHeader(oauthParams: Dict[str, Any]) -> PySide6.QtCore.QByteArray: ...
    def get(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def grant(self) -> None: ...
    def head(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    @staticmethod
    def nonce() -> PySide6.QtCore.QByteArray: ...
    def post(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def prepareRequest(self, request: PySide6.QtNetwork.QNetworkRequest, verb: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], body: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview] = ...) -> None: ...
    def put(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def requestTemporaryCredentials(self, operation: PySide6.QtNetwork.QNetworkAccessManager.Operation, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def requestTokenCredentials(self, operation: PySide6.QtNetwork.QNetworkAccessManager.Operation, url: Union[PySide6.QtCore.QUrl, str], temporaryToken: Tuple[str, str], parameters: Dict[str, Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    @overload
    def setClientCredentials(self, clientCredentials: Tuple[str, str]) -> None: ...
    @overload
    def setClientCredentials(self, clientIdentifier: str, clientSharedSecret: str) -> None: ...
    def setClientSharedSecret(self, clientSharedSecret: str) -> None: ...
    def setSignatureMethod(self, value: PySide6.QtNetworkAuth.QOAuth1.SignatureMethod) -> None: ...
    def setTemporaryCredentialsUrl(self, url: Union[PySide6.QtCore.QUrl, str]) -> None: ...
    @overload
    def setTokenCredentials(self, token: str, tokenSecret: str) -> None: ...
    @overload
    def setTokenCredentials(self, tokenCredentials: Tuple[str, str]) -> None: ...
    def setTokenCredentialsUrl(self, url: Union[PySide6.QtCore.QUrl, str]) -> None: ...
    def setTokenSecret(self, tokenSecret: str) -> None: ...
    @overload
    def setup(self, request: PySide6.QtNetwork.QNetworkRequest, signingParameters: Dict[str, Any], operation: PySide6.QtNetwork.QNetworkAccessManager.Operation) -> None: ...
    @overload
    def setup(self, request: PySide6.QtNetwork.QNetworkRequest, signingParameters: Dict[str, Any], operationVerb: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> None: ...
    def signatureMethod(self) -> PySide6.QtNetworkAuth.QOAuth1.SignatureMethod: ...
    def temporaryCredentialsUrl(self) -> PySide6.QtCore.QUrl: ...
    def tokenCredentials(self) -> Tuple[str, str]: ...
    def tokenCredentialsUrl(self) -> PySide6.QtCore.QUrl: ...
    def tokenSecret(self) -> str: ...


class QOAuth1Signature(Shiboken.Object):

    class HttpRequestMethod(enum.Enum):

        Unknown                  : QOAuth1Signature.HttpRequestMethod = ... # 0x0
        Head                     : QOAuth1Signature.HttpRequestMethod = ... # 0x1
        Get                      : QOAuth1Signature.HttpRequestMethod = ... # 0x2
        Put                      : QOAuth1Signature.HttpRequestMethod = ... # 0x3
        Post                     : QOAuth1Signature.HttpRequestMethod = ... # 0x4
        Delete                   : QOAuth1Signature.HttpRequestMethod = ... # 0x5
        Custom                   : QOAuth1Signature.HttpRequestMethod = ... # 0x6


    @overload
    def __init__(self, other: PySide6.QtNetworkAuth.QOAuth1Signature) -> None: ...
    @overload
    def __init__(self, url: Union[PySide6.QtCore.QUrl, str], clientSharedKey: str, tokenSecret: str, method: PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod = ..., parameters: Dict[str, Any] = ...) -> None: ...
    @overload
    def __init__(self, url: Union[PySide6.QtCore.QUrl, str] = ..., method: PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod = ..., parameters: Dict[str, Any] = ...) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def addRequestBody(self, body: PySide6.QtCore.QUrlQuery) -> None: ...
    def clientSharedKey(self) -> str: ...
    def customMethodString(self) -> PySide6.QtCore.QByteArray: ...
    def hmacSha1(self) -> PySide6.QtCore.QByteArray: ...
    def httpRequestMethod(self) -> PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod: ...
    def insert(self, key: str, value: Any) -> None: ...
    def keys(self) -> List[str]: ...
    def parameters(self) -> Dict[str, Any]: ...
    @overload
    @staticmethod
    def plainText(clientSharedSecret: str, tokenSecret: str) -> PySide6.QtCore.QByteArray: ...
    @overload
    def plainText(self) -> PySide6.QtCore.QByteArray: ...
    def rsaSha1(self) -> PySide6.QtCore.QByteArray: ...
    def setClientSharedKey(self, secret: str) -> None: ...
    def setCustomMethodString(self, verb: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> None: ...
    def setHttpRequestMethod(self, method: PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod) -> None: ...
    def setParameters(self, parameters: Dict[str, Any]) -> None: ...
    def setTokenSecret(self, secret: str) -> None: ...
    def setUrl(self, url: Union[PySide6.QtCore.QUrl, str]) -> None: ...
    def swap(self, other: PySide6.QtNetworkAuth.QOAuth1Signature) -> None: ...
    def take(self, key: str) -> Any: ...
    def tokenSecret(self) -> str: ...
    def url(self) -> PySide6.QtCore.QUrl: ...
    def value(self, key: str, defaultValue: Any = ...) -> Any: ...


class QOAuth2AuthorizationCodeFlow(PySide6.QtNetworkAuth.QAbstractOAuth2):

    accessTokenUrlChanged    : ClassVar[Signal] = ... # accessTokenUrlChanged(QUrl)

    @overload
    def __init__(self, authorizationUrl: Union[PySide6.QtCore.QUrl, str], accessTokenUrl: Union[PySide6.QtCore.QUrl, str], manager: PySide6.QtNetwork.QNetworkAccessManager, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, clientIdentifier: str, authorizationUrl: Union[PySide6.QtCore.QUrl, str], accessTokenUrl: Union[PySide6.QtCore.QUrl, str], manager: PySide6.QtNetwork.QNetworkAccessManager, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, clientIdentifier: str, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def accessTokenUrl(self) -> PySide6.QtCore.QUrl: ...
    def buildAuthenticateUrl(self, parameters: Dict[str, Any] = ...) -> PySide6.QtCore.QUrl: ...
    def grant(self) -> None: ...
    def refreshAccessToken(self) -> None: ...
    def requestAccessToken(self, code: str) -> None: ...
    def resourceOwnerAuthorization(self, url: Union[PySide6.QtCore.QUrl, str], parameters: Dict[str, Any] = ...) -> None: ...
    def setAccessTokenUrl(self, accessTokenUrl: Union[PySide6.QtCore.QUrl, str]) -> None: ...


class QOAuthHttpServerReplyHandler(PySide6.QtNetworkAuth.QOAuthOobReplyHandler):

    @overload
    def __init__(self, address: Union[PySide6.QtNetwork.QHostAddress, PySide6.QtNetwork.QHostAddress.SpecialAddress], port: int, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, port: int, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def callback(self) -> str: ...
    def callbackPath(self) -> str: ...
    def callbackText(self) -> str: ...
    def close(self) -> None: ...
    def isListening(self) -> bool: ...
    def listen(self, address: Union[PySide6.QtNetwork.QHostAddress, PySide6.QtNetwork.QHostAddress.SpecialAddress] = ..., port: int = ...) -> bool: ...
    def port(self) -> int: ...
    def setCallbackPath(self, path: str) -> None: ...
    def setCallbackText(self, text: str) -> None: ...


class QOAuthOobReplyHandler(PySide6.QtNetworkAuth.QAbstractOAuthReplyHandler):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def callback(self) -> str: ...
    def networkReplyFinished(self, reply: PySide6.QtNetwork.QNetworkReply) -> None: ...


# eof
