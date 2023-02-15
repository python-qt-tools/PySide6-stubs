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
"""
This file contains the exact signatures for all functions in module
PySide6.QtScxml, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtScxml`

import PySide6.QtScxml
import PySide6.QtCore

from typing import Any, Optional, Tuple, Sequence, Dict, List, overload
from shiboken6 import Shiboken


class QIntList(object): ...


class QScxmlCompiler(Shiboken.Object):

    class Loader(Shiboken.Object):

        def __init__(self) -> None: ...

        def load(self, name:str, baseDir:str) -> Tuple[PySide6.QtCore.QByteArray, List[str]]: ...


    def __init__(self, xmlReader:PySide6.QtCore.QXmlStreamReader) -> None: ...

    def compile(self) -> PySide6.QtScxml.QScxmlStateMachine: ...
    def errors(self) -> List[PySide6.QtScxml.QScxmlError]: ...
    def fileName(self) -> str: ...
    def loader(self) -> PySide6.QtScxml.QScxmlCompiler.Loader: ...
    def setFileName(self, fileName:str) -> None: ...
    def setLoader(self, newLoader:PySide6.QtScxml.QScxmlCompiler.Loader) -> None: ...


class QScxmlCppDataModel(PySide6.QtScxml.QScxmlDataModel):

    def __init__(self, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def evaluateAssignment(self, id:int) -> bool: ...
    def evaluateForeach(self, id:int, body:PySide6.QtScxml.QScxmlDataModel.ForeachLoopBody) -> bool: ...
    def evaluateInitialization(self, id:int) -> bool: ...
    def hasScxmlProperty(self, name:str) -> bool: ...
    def inState(self, stateName:str) -> bool: ...
    def scxmlEvent(self) -> PySide6.QtScxml.QScxmlEvent: ...
    def scxmlProperty(self, name:str) -> Any: ...
    def setScxmlEvent(self, scxmlEvent:PySide6.QtScxml.QScxmlEvent) -> None: ...
    def setScxmlProperty(self, name:str, value:Any, context:str) -> bool: ...
    def setup(self, initialDataValues:Dict[str, Any]) -> bool: ...


class QScxmlDataModel(PySide6.QtCore.QObject):

    class ForeachLoopBody(Shiboken.Object):

        def __init__(self) -> None: ...

        def run(self) -> bool: ...


    def __init__(self, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    @staticmethod
    def createScxmlDataModel(pluginKey:str) -> PySide6.QtScxml.QScxmlDataModel: ...
    def evaluateAssignment(self, id:int) -> bool: ...
    def evaluateForeach(self, id:int, body:PySide6.QtScxml.QScxmlDataModel.ForeachLoopBody) -> bool: ...
    def evaluateInitialization(self, id:int) -> bool: ...
    def evaluateToBool(self, id:int) -> Tuple[bool, bool]: ...
    def evaluateToString(self, id:int) -> Tuple[str, bool]: ...
    def evaluateToVariant(self, id:int) -> Tuple[Any, bool]: ...
    def evaluateToVoid(self, id:int) -> bool: ...
    def hasScxmlProperty(self, name:str) -> bool: ...
    def scxmlProperty(self, name:str) -> Any: ...
    def setScxmlEvent(self, event:PySide6.QtScxml.QScxmlEvent) -> None: ...
    def setScxmlProperty(self, name:str, value:Any, context:str) -> bool: ...
    def setStateMachine(self, stateMachine:PySide6.QtScxml.QScxmlStateMachine) -> None: ...
    def setup(self, initialDataValues:Dict[str, Any]) -> bool: ...
    def stateMachine(self) -> PySide6.QtScxml.QScxmlStateMachine: ...


class QScxmlDynamicScxmlServiceFactory(PySide6.QtScxml.QScxmlInvokableServiceFactory):

    def __init__(self, invokeInfo:PySide6.QtScxml.QScxmlExecutableContent.InvokeInfo, names:Sequence[int], parameters:Sequence[PySide6.QtScxml.QScxmlExecutableContent.ParameterInfo], parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def invoke(self, parentStateMachine:PySide6.QtScxml.QScxmlStateMachine) -> PySide6.QtScxml.QScxmlInvokableService: ...


class QScxmlError(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg__1:PySide6.QtScxml.QScxmlError) -> None: ...
    @overload
    def __init__(self, fileName:str, line:int, column:int, description:str) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def column(self) -> int: ...
    def description(self) -> str: ...
    def fileName(self) -> str: ...
    def isValid(self) -> bool: ...
    def line(self) -> int: ...
    def toString(self) -> str: ...


class QScxmlEvent(Shiboken.Object):

    PlatformEvent            : QScxmlEvent.EventType = ... # 0x0
    InternalEvent            : QScxmlEvent.EventType = ... # 0x1
    ExternalEvent            : QScxmlEvent.EventType = ... # 0x2

    class EventType(Shiboken.Enum):

        PlatformEvent            : QScxmlEvent.EventType = ... # 0x0
        InternalEvent            : QScxmlEvent.EventType = ... # 0x1
        ExternalEvent            : QScxmlEvent.EventType = ... # 0x2


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other:PySide6.QtScxml.QScxmlEvent) -> None: ...

    def clear(self) -> None: ...
    def data(self) -> Any: ...
    def delay(self) -> int: ...
    def errorMessage(self) -> str: ...
    def eventType(self) -> PySide6.QtScxml.QScxmlEvent.EventType: ...
    def invokeId(self) -> str: ...
    def isErrorEvent(self) -> bool: ...
    def name(self) -> str: ...
    def origin(self) -> str: ...
    def originType(self) -> str: ...
    def scxmlType(self) -> str: ...
    def sendId(self) -> str: ...
    def setData(self, data:Any) -> None: ...
    def setDelay(self, delayInMiliSecs:int) -> None: ...
    def setErrorMessage(self, message:str) -> None: ...
    def setEventType(self, type:PySide6.QtScxml.QScxmlEvent.EventType) -> None: ...
    def setInvokeId(self, invokeId:str) -> None: ...
    def setName(self, name:str) -> None: ...
    def setOrigin(self, origin:str) -> None: ...
    def setOriginType(self, originType:str) -> None: ...
    def setSendId(self, sendId:str) -> None: ...


class QScxmlExecutableContent(Shiboken.Object):

    class AssignmentInfo(Shiboken.Object):

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, AssignmentInfo:PySide6.QtScxml.QScxmlExecutableContent.AssignmentInfo) -> None: ...

        @staticmethod
        def __copy__() -> None: ...

    class EvaluatorInfo(Shiboken.Object):

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, EvaluatorInfo:PySide6.QtScxml.QScxmlExecutableContent.EvaluatorInfo) -> None: ...

        @staticmethod
        def __copy__() -> None: ...

    class ForeachInfo(Shiboken.Object):

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, ForeachInfo:PySide6.QtScxml.QScxmlExecutableContent.ForeachInfo) -> None: ...

        @staticmethod
        def __copy__() -> None: ...

    class InvokeInfo(Shiboken.Object):

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, InvokeInfo:PySide6.QtScxml.QScxmlExecutableContent.InvokeInfo) -> None: ...

        @staticmethod
        def __copy__() -> None: ...

    class ParameterInfo(Shiboken.Object):

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, ParameterInfo:PySide6.QtScxml.QScxmlExecutableContent.ParameterInfo) -> None: ...

        @staticmethod
        def __copy__() -> None: ...


class QScxmlInvokableService(PySide6.QtCore.QObject):

    def __init__(self, parentStateMachine:PySide6.QtScxml.QScxmlStateMachine, parent:PySide6.QtScxml.QScxmlInvokableServiceFactory) -> None: ...

    def id(self) -> str: ...
    def name(self) -> str: ...
    def parentStateMachine(self) -> PySide6.QtScxml.QScxmlStateMachine: ...
    def postEvent(self, event:PySide6.QtScxml.QScxmlEvent) -> None: ...
    def start(self) -> bool: ...


class QScxmlInvokableServiceFactory(PySide6.QtCore.QObject):

    def __init__(self, invokeInfo:PySide6.QtScxml.QScxmlExecutableContent.InvokeInfo, names:Sequence[int], parameters:Sequence[PySide6.QtScxml.QScxmlExecutableContent.ParameterInfo], parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def invoke(self, parentStateMachine:PySide6.QtScxml.QScxmlStateMachine) -> PySide6.QtScxml.QScxmlInvokableService: ...
    def invokeInfo(self) -> PySide6.QtScxml.QScxmlExecutableContent.InvokeInfo: ...
    def names(self) -> List[int]: ...
    def parameters(self) -> List[PySide6.QtScxml.QScxmlExecutableContent.ParameterInfo]: ...


class QScxmlNullDataModel(PySide6.QtScxml.QScxmlDataModel):

    def __init__(self, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def evaluateAssignment(self, id:int) -> bool: ...
    def evaluateForeach(self, id:int, body:PySide6.QtScxml.QScxmlDataModel.ForeachLoopBody) -> bool: ...
    def evaluateInitialization(self, id:int) -> bool: ...
    def evaluateToBool(self, id:int) -> Tuple[bool, bool]: ...
    def evaluateToString(self, id:int) -> Tuple[str, bool]: ...
    def evaluateToVariant(self, id:int) -> Tuple[Any, bool]: ...
    def evaluateToVoid(self, id:int) -> bool: ...
    def hasScxmlProperty(self, name:str) -> bool: ...
    def scxmlProperty(self, name:str) -> Any: ...
    def setScxmlEvent(self, event:PySide6.QtScxml.QScxmlEvent) -> None: ...
    def setScxmlProperty(self, name:str, value:Any, context:str) -> bool: ...
    def setup(self, initialDataValues:Dict[str, Any]) -> bool: ...


class QScxmlStateMachine(PySide6.QtCore.QObject):

    def __init__(self, metaObject:PySide6.QtCore.QMetaObject, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def activeStateNames(self, compress:bool=...) -> List[str]: ...
    def cancelDelayedEvent(self, sendId:str) -> None: ...
    def connectToEvent(self, scxmlEventSpec:str, receiver:PySide6.QtCore.QObject, method:bytes, type:PySide6.QtCore.Qt.ConnectionType=...) -> PySide6.QtCore.QMetaObject.Connection: ...
    def connectToState(self, scxmlStateName:str, receiver:PySide6.QtCore.QObject, method:bytes, type:PySide6.QtCore.Qt.ConnectionType=...) -> PySide6.QtCore.QMetaObject.Connection: ...
    def dataModel(self) -> PySide6.QtScxml.QScxmlDataModel: ...
    @staticmethod
    def fromData(data:PySide6.QtCore.QIODevice, fileName:str=...) -> PySide6.QtScxml.QScxmlStateMachine: ...
    @staticmethod
    def fromFile(fileName:str) -> PySide6.QtScxml.QScxmlStateMachine: ...
    def init(self) -> bool: ...
    def initialValues(self) -> Dict[str, Any]: ...
    def invokedServices(self) -> List[PySide6.QtScxml.QScxmlInvokableService]: ...
    @overload
    def isActive(self, scxmlStateName:str) -> bool: ...
    @overload
    def isActive(self, stateIndex:int) -> bool: ...
    def isDispatchableTarget(self, target:str) -> bool: ...
    def isInitialized(self) -> bool: ...
    def isInvoked(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def loader(self) -> PySide6.QtScxml.QScxmlCompiler.Loader: ...
    def name(self) -> str: ...
    def parseErrors(self) -> List[PySide6.QtScxml.QScxmlError]: ...
    def sessionId(self) -> str: ...
    def setDataModel(self, model:PySide6.QtScxml.QScxmlDataModel) -> None: ...
    def setInitialValues(self, initialValues:Dict[str, Any]) -> None: ...
    def setLoader(self, loader:PySide6.QtScxml.QScxmlCompiler.Loader) -> None: ...
    def setRunning(self, running:bool) -> None: ...
    def setTableData(self, tableData:PySide6.QtScxml.QScxmlTableData) -> None: ...
    def start(self) -> None: ...
    def stateNames(self, compress:bool=...) -> List[str]: ...
    def stop(self) -> None: ...
    @overload
    def submitEvent(self, event:PySide6.QtScxml.QScxmlEvent) -> None: ...
    @overload
    def submitEvent(self, eventName:str) -> None: ...
    @overload
    def submitEvent(self, eventName:str, data:Any) -> None: ...
    def tableData(self) -> PySide6.QtScxml.QScxmlTableData: ...


class QScxmlStaticScxmlServiceFactory(PySide6.QtScxml.QScxmlInvokableServiceFactory):

    def __init__(self, metaObject:PySide6.QtCore.QMetaObject, invokeInfo:PySide6.QtScxml.QScxmlExecutableContent.InvokeInfo, nameList:Sequence[int], parameters:Sequence[PySide6.QtScxml.QScxmlExecutableContent.ParameterInfo], parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def invoke(self, parentStateMachine:PySide6.QtScxml.QScxmlStateMachine) -> PySide6.QtScxml.QScxmlInvokableService: ...


class QScxmlTableData(Shiboken.Object):

    def __init__(self) -> None: ...

    def assignmentInfo(self, assignmentId:int) -> PySide6.QtScxml.QScxmlExecutableContent.AssignmentInfo: ...
    def dataNames(self) -> Tuple[List[int], int]: ...
    def evaluatorInfo(self, evaluatorId:int) -> PySide6.QtScxml.QScxmlExecutableContent.EvaluatorInfo: ...
    def foreachInfo(self, foreachId:int) -> PySide6.QtScxml.QScxmlExecutableContent.ForeachInfo: ...
    def initialSetup(self) -> int: ...
    def instructions(self) -> List[int]: ...
    def name(self) -> str: ...
    def serviceFactory(self, id:int) -> PySide6.QtScxml.QScxmlInvokableServiceFactory: ...
    def stateMachineTable(self) -> List[int]: ...
    def string(self, id:int) -> str: ...


# eof
