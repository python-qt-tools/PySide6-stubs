# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtSerialBus, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtSerialBus`

import PySide6.QtSerialBus
import PySide6.QtCore
import PySide6.QtNetwork

import enum
from typing import Any, ClassVar, Dict, List, Optional, Sequence, Tuple, Union, overload
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


NoneType = type(None)


class QCanBus(PySide6.QtCore.QObject):
    def availableDevices(self, plugin: str) -> tuple: ...
    def createDevice(self, plugin: str, interfaceName: str) -> tuple: ...
    @staticmethod
    def instance() -> PySide6.QtSerialBus.QCanBus: ...
    def plugins(self) -> List[str]: ...


class QCanBusDevice(PySide6.QtCore.QObject):

    errorOccurred            : ClassVar[Signal] = ... # errorOccurred(QCanBusDevice::CanBusError)
    framesReceived           : ClassVar[Signal] = ... # framesReceived()
    framesWritten            : ClassVar[Signal] = ... # framesWritten(qlonglong)
    stateChanged             : ClassVar[Signal] = ... # stateChanged(QCanBusDevice::CanBusDeviceState)

    class CanBusDeviceState(enum.Enum):

        UnconnectedState         : QCanBusDevice.CanBusDeviceState = ... # 0x0
        ConnectingState          : QCanBusDevice.CanBusDeviceState = ... # 0x1
        ConnectedState           : QCanBusDevice.CanBusDeviceState = ... # 0x2
        ClosingState             : QCanBusDevice.CanBusDeviceState = ... # 0x3

    class CanBusError(enum.Enum):

        NoError                  : QCanBusDevice.CanBusError = ... # 0x0
        ReadError                : QCanBusDevice.CanBusError = ... # 0x1
        WriteError               : QCanBusDevice.CanBusError = ... # 0x2
        ConnectionError          : QCanBusDevice.CanBusError = ... # 0x3
        ConfigurationError       : QCanBusDevice.CanBusError = ... # 0x4
        UnknownError             : QCanBusDevice.CanBusError = ... # 0x5
        OperationError           : QCanBusDevice.CanBusError = ... # 0x6
        TimeoutError             : QCanBusDevice.CanBusError = ... # 0x7

    class CanBusStatus(enum.Enum):

        Unknown                  : QCanBusDevice.CanBusStatus = ... # 0x0
        Good                     : QCanBusDevice.CanBusStatus = ... # 0x1
        Warning                  : QCanBusDevice.CanBusStatus = ... # 0x2
        Error                    : QCanBusDevice.CanBusStatus = ... # 0x3
        BusOff                   : QCanBusDevice.CanBusStatus = ... # 0x4

    class ConfigurationKey(enum.Enum):

        RawFilterKey             : QCanBusDevice.ConfigurationKey = ... # 0x0
        ErrorFilterKey           : QCanBusDevice.ConfigurationKey = ... # 0x1
        LoopbackKey              : QCanBusDevice.ConfigurationKey = ... # 0x2
        ReceiveOwnKey            : QCanBusDevice.ConfigurationKey = ... # 0x3
        BitRateKey               : QCanBusDevice.ConfigurationKey = ... # 0x4
        CanFdKey                 : QCanBusDevice.ConfigurationKey = ... # 0x5
        DataBitRateKey           : QCanBusDevice.ConfigurationKey = ... # 0x6
        ProtocolKey              : QCanBusDevice.ConfigurationKey = ... # 0x7
        UserKey                  : QCanBusDevice.ConfigurationKey = ... # 0x1e

    class Direction(enum.Flag):

        Input                    : QCanBusDevice.Direction = ... # 0x1
        Output                   : QCanBusDevice.Direction = ... # 0x2
        AllDirections            : QCanBusDevice.Direction = ... # 0x3

    class Filter(Shiboken.Object):

        class FormatFilter(enum.Flag):

            MatchBaseFormat          : QCanBusDevice.Filter.FormatFilter = ... # 0x1
            MatchExtendedFormat      : QCanBusDevice.Filter.FormatFilter = ... # 0x2
            MatchBaseAndExtendedFormat: QCanBusDevice.Filter.FormatFilter = ... # 0x3


        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, Filter: PySide6.QtSerialBus.QCanBusDevice.Filter) -> None: ...

        @staticmethod
        def __copy__() -> None: ...


    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def busStatus(self) -> PySide6.QtSerialBus.QCanBusDevice.CanBusStatus: ...
    def clear(self, direction: PySide6.QtSerialBus.QCanBusDevice.Direction = ...) -> None: ...
    def clearError(self) -> None: ...
    def close(self) -> None: ...
    def configurationKeys(self) -> List[PySide6.QtSerialBus.QCanBusDevice.ConfigurationKey]: ...
    def configurationParameter(self, key: PySide6.QtSerialBus.QCanBusDevice.ConfigurationKey) -> Any: ...
    def connectDevice(self) -> bool: ...
    @overload
    @staticmethod
    def createDeviceInfo(plugin: str, name: str, isVirtual: bool, isFlexibleDataRateCapable: bool) -> PySide6.QtSerialBus.QCanBusDeviceInfo: ...
    @overload
    @staticmethod
    def createDeviceInfo(plugin: str, name: str, serialNumber: str, description: str, alias: str, channel: int, isVirtual: bool, isFlexibleDataRateCapable: bool) -> PySide6.QtSerialBus.QCanBusDeviceInfo: ...
    def dequeueOutgoingFrame(self) -> PySide6.QtSerialBus.QCanBusFrame: ...
    def deviceInfo(self) -> PySide6.QtSerialBus.QCanBusDeviceInfo: ...
    def disconnectDevice(self) -> None: ...
    def enqueueOutgoingFrame(self, newFrame: Union[PySide6.QtSerialBus.QCanBusFrame, PySide6.QtSerialBus.QCanBusFrame.FrameType]) -> None: ...
    def enqueueReceivedFrames(self, newFrames: Sequence[PySide6.QtSerialBus.QCanBusFrame]) -> None: ...
    def error(self) -> PySide6.QtSerialBus.QCanBusDevice.CanBusError: ...
    def errorString(self) -> str: ...
    def framesAvailable(self) -> int: ...
    def framesToWrite(self) -> int: ...
    def hasBusStatus(self) -> bool: ...
    def hasOutgoingFrames(self) -> bool: ...
    def interpretErrorFrame(self, errorFrame: Union[PySide6.QtSerialBus.QCanBusFrame, PySide6.QtSerialBus.QCanBusFrame.FrameType]) -> str: ...
    def open(self) -> bool: ...
    def readAllFrames(self) -> List[PySide6.QtSerialBus.QCanBusFrame]: ...
    def readFrame(self) -> PySide6.QtSerialBus.QCanBusFrame: ...
    def resetController(self) -> None: ...
    def setConfigurationParameter(self, key: PySide6.QtSerialBus.QCanBusDevice.ConfigurationKey, value: Any) -> None: ...
    def setError(self, errorText: str, arg__2: PySide6.QtSerialBus.QCanBusDevice.CanBusError) -> None: ...
    def setState(self, newState: PySide6.QtSerialBus.QCanBusDevice.CanBusDeviceState) -> None: ...
    def state(self) -> PySide6.QtSerialBus.QCanBusDevice.CanBusDeviceState: ...
    def waitForFramesReceived(self, msecs: int) -> bool: ...
    def waitForFramesWritten(self, msecs: int) -> bool: ...
    def writeFrame(self, frame: Union[PySide6.QtSerialBus.QCanBusFrame, PySide6.QtSerialBus.QCanBusFrame.FrameType]) -> bool: ...


class QCanBusDeviceInfo(Shiboken.Object):

    def __init__(self, other: PySide6.QtSerialBus.QCanBusDeviceInfo) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def alias(self) -> str: ...
    def channel(self) -> int: ...
    def description(self) -> str: ...
    def hasFlexibleDataRate(self) -> bool: ...
    def isVirtual(self) -> bool: ...
    def name(self) -> str: ...
    def plugin(self) -> str: ...
    def serialNumber(self) -> str: ...


class QCanBusFactory(Shiboken.Object):

    def __init__(self) -> None: ...

    def availableDevices(self) -> Tuple[List[PySide6.QtSerialBus.QCanBusDeviceInfo], str]: ...
    def createDevice(self, interfaceName: str) -> Tuple[PySide6.QtSerialBus.QCanBusDevice, str]: ...


class QCanBusFrame(Shiboken.Object):

    class FrameError(enum.Flag):

        NoError                  : QCanBusFrame.FrameError = ... # 0x0
        TransmissionTimeoutError : QCanBusFrame.FrameError = ... # 0x1
        LostArbitrationError     : QCanBusFrame.FrameError = ... # 0x2
        ControllerError          : QCanBusFrame.FrameError = ... # 0x4
        ProtocolViolationError   : QCanBusFrame.FrameError = ... # 0x8
        TransceiverError         : QCanBusFrame.FrameError = ... # 0x10
        MissingAcknowledgmentError: QCanBusFrame.FrameError = ... # 0x20
        BusOffError              : QCanBusFrame.FrameError = ... # 0x40
        BusError                 : QCanBusFrame.FrameError = ... # 0x80
        ControllerRestartError   : QCanBusFrame.FrameError = ... # 0x100
        UnknownError             : QCanBusFrame.FrameError = ... # 0x200
        AnyError                 : QCanBusFrame.FrameError = ... # 0x1fffffff

    class FrameType(enum.Enum):

        UnknownFrame             : QCanBusFrame.FrameType = ... # 0x0
        DataFrame                : QCanBusFrame.FrameType = ... # 0x1
        ErrorFrame               : QCanBusFrame.FrameType = ... # 0x2
        RemoteRequestFrame       : QCanBusFrame.FrameType = ... # 0x3
        InvalidFrame             : QCanBusFrame.FrameType = ... # 0x4

    class TimeStamp(Shiboken.Object):

        @overload
        def __init__(self, TimeStamp: PySide6.QtSerialBus.QCanBusFrame.TimeStamp) -> None: ...
        @overload
        def __init__(self, s: int = ..., usec: int = ...) -> None: ...

        @staticmethod
        def __copy__() -> None: ...
        @staticmethod
        def fromMicroSeconds(usec: int) -> PySide6.QtSerialBus.QCanBusFrame.TimeStamp: ...
        def microSeconds(self) -> int: ...
        def seconds(self) -> int: ...


    @overload
    def __init__(self, QCanBusFrame: Union[PySide6.QtSerialBus.QCanBusFrame, PySide6.QtSerialBus.QCanBusFrame.FrameType]) -> None: ...
    @overload
    def __init__(self, identifier: int, data: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> None: ...
    @overload
    def __init__(self, type: PySide6.QtSerialBus.QCanBusFrame.FrameType = ...) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, arg__1: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, arg__1: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def error(self) -> PySide6.QtSerialBus.QCanBusFrame.FrameError: ...
    def frameId(self) -> int: ...
    def frameType(self) -> PySide6.QtSerialBus.QCanBusFrame.FrameType: ...
    def hasBitrateSwitch(self) -> bool: ...
    def hasErrorStateIndicator(self) -> bool: ...
    def hasExtendedFrameFormat(self) -> bool: ...
    def hasFlexibleDataRateFormat(self) -> bool: ...
    def hasLocalEcho(self) -> bool: ...
    def isValid(self) -> bool: ...
    def payload(self) -> PySide6.QtCore.QByteArray: ...
    def setBitrateSwitch(self, bitrateSwitch: bool) -> None: ...
    def setError(self, e: PySide6.QtSerialBus.QCanBusFrame.FrameError) -> None: ...
    def setErrorStateIndicator(self, errorStateIndicator: bool) -> None: ...
    def setExtendedFrameFormat(self, isExtended: bool) -> None: ...
    def setFlexibleDataRateFormat(self, isFlexibleData: bool) -> None: ...
    def setFrameId(self, newFrameId: int) -> None: ...
    def setFrameType(self, newFormat: PySide6.QtSerialBus.QCanBusFrame.FrameType) -> None: ...
    def setLocalEcho(self, localEcho: bool) -> None: ...
    def setPayload(self, data: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> None: ...
    def setTimeStamp(self, ts: PySide6.QtSerialBus.QCanBusFrame.TimeStamp) -> None: ...
    def timeStamp(self) -> PySide6.QtSerialBus.QCanBusFrame.TimeStamp: ...
    def toString(self) -> str: ...


class QIntList(object): ...


class QModbusClient(PySide6.QtSerialBus.QModbusDevice):

    timeoutChanged           : ClassVar[Signal] = ... # timeoutChanged(int)

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def numberOfRetries(self) -> int: ...
    def sendRawRequest(self, request: PySide6.QtSerialBus.QModbusRequest, serverAddress: int) -> PySide6.QtSerialBus.QModbusReply: ...
    def sendReadRequest(self, read: PySide6.QtSerialBus.QModbusDataUnit, serverAddress: int) -> PySide6.QtSerialBus.QModbusReply: ...
    def sendReadWriteRequest(self, read: PySide6.QtSerialBus.QModbusDataUnit, write: PySide6.QtSerialBus.QModbusDataUnit, serverAddress: int) -> PySide6.QtSerialBus.QModbusReply: ...
    def sendWriteRequest(self, write: PySide6.QtSerialBus.QModbusDataUnit, serverAddress: int) -> PySide6.QtSerialBus.QModbusReply: ...
    def setNumberOfRetries(self, number: int) -> None: ...
    def setTimeout(self, newTimeout: int) -> None: ...
    def timeout(self) -> int: ...


class QModbusDataUnit(Shiboken.Object):

    class RegisterType(enum.Enum):

        Invalid                  : QModbusDataUnit.RegisterType = ... # 0x0
        DiscreteInputs           : QModbusDataUnit.RegisterType = ... # 0x1
        Coils                    : QModbusDataUnit.RegisterType = ... # 0x2
        InputRegisters           : QModbusDataUnit.RegisterType = ... # 0x3
        HoldingRegisters         : QModbusDataUnit.RegisterType = ... # 0x4


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QModbusDataUnit: PySide6.QtSerialBus.QModbusDataUnit) -> None: ...
    @overload
    def __init__(self, type: PySide6.QtSerialBus.QModbusDataUnit.RegisterType) -> None: ...
    @overload
    def __init__(self, type: PySide6.QtSerialBus.QModbusDataUnit.RegisterType, newStartAddress: int, newValueCount: int) -> None: ...
    @overload
    def __init__(self, type: PySide6.QtSerialBus.QModbusDataUnit.RegisterType, newStartAddress: int, newValues: Sequence[int]) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def isValid(self) -> bool: ...
    def registerType(self) -> PySide6.QtSerialBus.QModbusDataUnit.RegisterType: ...
    def setRegisterType(self, type: PySide6.QtSerialBus.QModbusDataUnit.RegisterType) -> None: ...
    def setStartAddress(self, newAddress: int) -> None: ...
    def setValue(self, index: int, newValue: int) -> None: ...
    def setValueCount(self, newCount: int) -> None: ...
    def setValues(self, newValues: Sequence[int]) -> None: ...
    def startAddress(self) -> int: ...
    def value(self, index: int) -> int: ...
    def valueCount(self) -> int: ...
    def values(self) -> List[int]: ...


class QModbusDevice(PySide6.QtCore.QObject):

    errorOccurred            : ClassVar[Signal] = ... # errorOccurred(QModbusDevice::Error)
    stateChanged             : ClassVar[Signal] = ... # stateChanged(QModbusDevice::State)

    class ConnectionParameter(enum.Enum):

        SerialPortNameParameter  : QModbusDevice.ConnectionParameter = ... # 0x0
        SerialParityParameter    : QModbusDevice.ConnectionParameter = ... # 0x1
        SerialBaudRateParameter  : QModbusDevice.ConnectionParameter = ... # 0x2
        SerialDataBitsParameter  : QModbusDevice.ConnectionParameter = ... # 0x3
        SerialStopBitsParameter  : QModbusDevice.ConnectionParameter = ... # 0x4
        NetworkPortParameter     : QModbusDevice.ConnectionParameter = ... # 0x5
        NetworkAddressParameter  : QModbusDevice.ConnectionParameter = ... # 0x6

    class Error(enum.Enum):

        NoError                  : QModbusDevice.Error = ... # 0x0
        ReadError                : QModbusDevice.Error = ... # 0x1
        WriteError               : QModbusDevice.Error = ... # 0x2
        ConnectionError          : QModbusDevice.Error = ... # 0x3
        ConfigurationError       : QModbusDevice.Error = ... # 0x4
        TimeoutError             : QModbusDevice.Error = ... # 0x5
        ProtocolError            : QModbusDevice.Error = ... # 0x6
        ReplyAbortedError        : QModbusDevice.Error = ... # 0x7
        UnknownError             : QModbusDevice.Error = ... # 0x8
        InvalidResponseError     : QModbusDevice.Error = ... # 0x9

    class IntermediateError(enum.Enum):

        ResponseCrcError         : QModbusDevice.IntermediateError = ... # 0x0
        ResponseRequestMismatch  : QModbusDevice.IntermediateError = ... # 0x1

    class State(enum.Enum):

        UnconnectedState         : QModbusDevice.State = ... # 0x0
        ConnectingState          : QModbusDevice.State = ... # 0x1
        ConnectedState           : QModbusDevice.State = ... # 0x2
        ClosingState             : QModbusDevice.State = ... # 0x3


    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def close(self) -> None: ...
    def connectDevice(self) -> bool: ...
    def connectionParameter(self, parameter: PySide6.QtSerialBus.QModbusDevice.ConnectionParameter) -> Any: ...
    def device(self) -> PySide6.QtCore.QIODevice: ...
    def disconnectDevice(self) -> None: ...
    def error(self) -> PySide6.QtSerialBus.QModbusDevice.Error: ...
    def errorString(self) -> str: ...
    def open(self) -> bool: ...
    def setConnectionParameter(self, parameter: PySide6.QtSerialBus.QModbusDevice.ConnectionParameter, value: Any) -> None: ...
    def setError(self, errorText: str, error: PySide6.QtSerialBus.QModbusDevice.Error) -> None: ...
    def setState(self, newState: PySide6.QtSerialBus.QModbusDevice.State) -> None: ...
    def state(self) -> PySide6.QtSerialBus.QModbusDevice.State: ...


class QModbusDeviceIdentification(Shiboken.Object):

    class ConformityLevel(enum.Enum):

        BasicConformityLevel     : QModbusDeviceIdentification.ConformityLevel = ... # 0x1
        RegularConformityLevel   : QModbusDeviceIdentification.ConformityLevel = ... # 0x2
        ExtendedConformityLevel  : QModbusDeviceIdentification.ConformityLevel = ... # 0x3
        BasicIndividualConformityLevel: QModbusDeviceIdentification.ConformityLevel = ... # 0x81
        RegularIndividualConformityLevel: QModbusDeviceIdentification.ConformityLevel = ... # 0x82
        ExtendedIndividualConformityLevel: QModbusDeviceIdentification.ConformityLevel = ... # 0x83

    class ObjectId(enum.Enum):

        VendorNameObjectId       : QModbusDeviceIdentification.ObjectId = ... # 0x0
        ProductCodeObjectId      : QModbusDeviceIdentification.ObjectId = ... # 0x1
        MajorMinorRevisionObjectId: QModbusDeviceIdentification.ObjectId = ... # 0x2
        VendorUrlObjectId        : QModbusDeviceIdentification.ObjectId = ... # 0x3
        ProductNameObjectId      : QModbusDeviceIdentification.ObjectId = ... # 0x4
        ModelNameObjectId        : QModbusDeviceIdentification.ObjectId = ... # 0x5
        UserApplicationNameObjectId: QModbusDeviceIdentification.ObjectId = ... # 0x6
        ReservedObjectId         : QModbusDeviceIdentification.ObjectId = ... # 0x7
        ProductDependentObjectId : QModbusDeviceIdentification.ObjectId = ... # 0x80
        UndefinedObjectId        : QModbusDeviceIdentification.ObjectId = ... # 0x100

    class ReadDeviceIdCode(enum.Enum):

        BasicReadDeviceIdCode    : QModbusDeviceIdentification.ReadDeviceIdCode = ... # 0x1
        RegularReadDeviceIdCode  : QModbusDeviceIdentification.ReadDeviceIdCode = ... # 0x2
        ExtendedReadDeviceIdCode : QModbusDeviceIdentification.ReadDeviceIdCode = ... # 0x3
        IndividualReadDeviceIdCode: QModbusDeviceIdentification.ReadDeviceIdCode = ... # 0x4


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QModbusDeviceIdentification: PySide6.QtSerialBus.QModbusDeviceIdentification) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def conformityLevel(self) -> PySide6.QtSerialBus.QModbusDeviceIdentification.ConformityLevel: ...
    def contains(self, objectId: int) -> bool: ...
    @staticmethod
    def fromByteArray(ba: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> PySide6.QtSerialBus.QModbusDeviceIdentification: ...
    def insert(self, objectId: int, data: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> bool: ...
    def isValid(self) -> bool: ...
    def objectIds(self) -> List[int]: ...
    def remove(self, objectId: int) -> None: ...
    def setConformityLevel(self, level: PySide6.QtSerialBus.QModbusDeviceIdentification.ConformityLevel) -> None: ...
    def value(self, objectId: int) -> PySide6.QtCore.QByteArray: ...


class QModbusPdu(Shiboken.Object):

    class ExceptionCode(enum.Enum):

        IllegalFunction          : QModbusPdu.ExceptionCode = ... # 0x1
        IllegalDataAddress       : QModbusPdu.ExceptionCode = ... # 0x2
        IllegalDataValue         : QModbusPdu.ExceptionCode = ... # 0x3
        ServerDeviceFailure      : QModbusPdu.ExceptionCode = ... # 0x4
        Acknowledge              : QModbusPdu.ExceptionCode = ... # 0x5
        ServerDeviceBusy         : QModbusPdu.ExceptionCode = ... # 0x6
        NegativeAcknowledge      : QModbusPdu.ExceptionCode = ... # 0x7
        MemoryParityError        : QModbusPdu.ExceptionCode = ... # 0x8
        GatewayPathUnavailable   : QModbusPdu.ExceptionCode = ... # 0xa
        GatewayTargetDeviceFailedToRespond: QModbusPdu.ExceptionCode = ... # 0xb
        ExtendedException        : QModbusPdu.ExceptionCode = ... # 0xff

    class FunctionCode(enum.Enum):

        Invalid                  : QModbusPdu.FunctionCode = ... # 0x0
        ReadCoils                : QModbusPdu.FunctionCode = ... # 0x1
        ReadDiscreteInputs       : QModbusPdu.FunctionCode = ... # 0x2
        ReadHoldingRegisters     : QModbusPdu.FunctionCode = ... # 0x3
        ReadInputRegisters       : QModbusPdu.FunctionCode = ... # 0x4
        WriteSingleCoil          : QModbusPdu.FunctionCode = ... # 0x5
        WriteSingleRegister      : QModbusPdu.FunctionCode = ... # 0x6
        ReadExceptionStatus      : QModbusPdu.FunctionCode = ... # 0x7
        Diagnostics              : QModbusPdu.FunctionCode = ... # 0x8
        GetCommEventCounter      : QModbusPdu.FunctionCode = ... # 0xb
        GetCommEventLog          : QModbusPdu.FunctionCode = ... # 0xc
        WriteMultipleCoils       : QModbusPdu.FunctionCode = ... # 0xf
        WriteMultipleRegisters   : QModbusPdu.FunctionCode = ... # 0x10
        ReportServerId           : QModbusPdu.FunctionCode = ... # 0x11
        ReadFileRecord           : QModbusPdu.FunctionCode = ... # 0x14
        WriteFileRecord          : QModbusPdu.FunctionCode = ... # 0x15
        MaskWriteRegister        : QModbusPdu.FunctionCode = ... # 0x16
        ReadWriteMultipleRegisters: QModbusPdu.FunctionCode = ... # 0x17
        ReadFifoQueue            : QModbusPdu.FunctionCode = ... # 0x18
        EncapsulatedInterfaceTransport: QModbusPdu.FunctionCode = ... # 0x2b
        UndefinedFunctionCode    : QModbusPdu.FunctionCode = ... # 0x100


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg__1: PySide6.QtSerialBus.QModbusPdu) -> None: ...
    @overload
    def __init__(self, code: PySide6.QtSerialBus.QModbusPdu.FunctionCode, newData: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> None: ...

    def __lshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def data(self) -> PySide6.QtCore.QByteArray: ...
    def dataSize(self) -> int: ...
    def exceptionCode(self) -> PySide6.QtSerialBus.QModbusPdu.ExceptionCode: ...
    def functionCode(self) -> PySide6.QtSerialBus.QModbusPdu.FunctionCode: ...
    def isException(self) -> bool: ...
    def isValid(self) -> bool: ...
    def setData(self, newData: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> None: ...
    def setFunctionCode(self, code: PySide6.QtSerialBus.QModbusPdu.FunctionCode) -> None: ...
    def size(self) -> int: ...


class QModbusReply(PySide6.QtCore.QObject):

    errorOccurred            : ClassVar[Signal] = ... # errorOccurred(QModbusDevice::Error)
    finished                 : ClassVar[Signal] = ... # finished()
    intermediateErrorOccurred: ClassVar[Signal] = ... # intermediateErrorOccurred(QModbusDevice::IntermediateError)

    class ReplyType(enum.Enum):

        Raw                      : QModbusReply.ReplyType = ... # 0x0
        Common                   : QModbusReply.ReplyType = ... # 0x1
        Broadcast                : QModbusReply.ReplyType = ... # 0x2


    def __init__(self, type: PySide6.QtSerialBus.QModbusReply.ReplyType, serverAddress: int, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def addIntermediateError(self, error: PySide6.QtSerialBus.QModbusDevice.IntermediateError) -> None: ...
    def error(self) -> PySide6.QtSerialBus.QModbusDevice.Error: ...
    def errorString(self) -> str: ...
    def intermediateErrors(self) -> List[PySide6.QtSerialBus.QModbusDevice.IntermediateError]: ...
    def isFinished(self) -> bool: ...
    def result(self) -> PySide6.QtSerialBus.QModbusDataUnit: ...
    def serverAddress(self) -> int: ...
    def setError(self, error: PySide6.QtSerialBus.QModbusDevice.Error, errorText: str) -> None: ...
    def setFinished(self, isFinished: bool) -> None: ...
    def setResult(self, unit: PySide6.QtSerialBus.QModbusDataUnit) -> None: ...
    def type(self) -> PySide6.QtSerialBus.QModbusReply.ReplyType: ...


class QModbusRequest(PySide6.QtSerialBus.QModbusPdu):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, code: PySide6.QtSerialBus.QModbusPdu.FunctionCode, newData: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview] = ...) -> None: ...
    @overload
    def __init__(self, pdu: PySide6.QtSerialBus.QModbusPdu) -> None: ...

    def __lshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    @staticmethod
    def calculateDataSize(pdu: PySide6.QtSerialBus.QModbusRequest) -> int: ...
    @staticmethod
    def minimumDataSize(pdu: PySide6.QtSerialBus.QModbusRequest) -> int: ...


class QModbusRtuSerialClient(PySide6.QtSerialBus.QModbusClient):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def close(self) -> None: ...
    def interFrameDelay(self) -> int: ...
    def open(self) -> bool: ...
    def setInterFrameDelay(self, microseconds: int) -> None: ...
    def setTurnaroundDelay(self, turnaroundDelay: int) -> None: ...
    def turnaroundDelay(self) -> int: ...


class QModbusRtuSerialServer(PySide6.QtSerialBus.QModbusServer):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def close(self) -> None: ...
    def interFrameDelay(self) -> int: ...
    def open(self) -> bool: ...
    def processesBroadcast(self) -> bool: ...
    def setInterFrameDelay(self, microseconds: int) -> None: ...


class QModbusServer(PySide6.QtSerialBus.QModbusDevice):

    dataWritten              : ClassVar[Signal] = ... # dataWritten(QModbusDataUnit::RegisterType,int,int)

    class Option(enum.Enum):

        DiagnosticRegister       : QModbusServer.Option = ... # 0x0
        ExceptionStatusOffset    : QModbusServer.Option = ... # 0x1
        DeviceBusy               : QModbusServer.Option = ... # 0x2
        AsciiInputDelimiter      : QModbusServer.Option = ... # 0x3
        ListenOnlyMode           : QModbusServer.Option = ... # 0x4
        ServerIdentifier         : QModbusServer.Option = ... # 0x5
        RunIndicatorStatus       : QModbusServer.Option = ... # 0x6
        AdditionalData           : QModbusServer.Option = ... # 0x7
        DeviceIdentification     : QModbusServer.Option = ... # 0x8
        UserOption               : QModbusServer.Option = ... # 0x100


    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    @overload
    def data(self, newData: PySide6.QtSerialBus.QModbusDataUnit) -> bool: ...
    @overload
    def data(self, table: PySide6.QtSerialBus.QModbusDataUnit.RegisterType, address: int) -> Tuple[bool, int]: ...
    def processesBroadcast(self) -> bool: ...
    def readData(self, newData: PySide6.QtSerialBus.QModbusDataUnit) -> bool: ...
    def serverAddress(self) -> int: ...
    @overload
    def setData(self, table: PySide6.QtSerialBus.QModbusDataUnit.RegisterType, address: int, data: int) -> bool: ...
    @overload
    def setData(self, unit: PySide6.QtSerialBus.QModbusDataUnit) -> bool: ...
    def setMap(self, map: Dict[PySide6.QtSerialBus.QModbusDataUnit.RegisterType, PySide6.QtSerialBus.QModbusDataUnit]) -> bool: ...
    def setServerAddress(self, serverAddress: int) -> None: ...
    def setValue(self, option: int, value: Any) -> bool: ...
    def value(self, option: int) -> Any: ...
    def writeData(self, unit: PySide6.QtSerialBus.QModbusDataUnit) -> bool: ...


class QModbusTcpClient(PySide6.QtSerialBus.QModbusClient):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def close(self) -> None: ...
    def open(self) -> bool: ...


class QModbusTcpConnectionObserver(Shiboken.Object):

    def __init__(self) -> None: ...

    def acceptNewConnection(self, newClient: PySide6.QtNetwork.QTcpSocket) -> bool: ...


class QModbusTcpServer(PySide6.QtSerialBus.QModbusServer):

    modbusClientDisconnected : ClassVar[Signal] = ... # modbusClientDisconnected(QTcpSocket*)

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def close(self) -> None: ...
    def installConnectionObserver(self, observer: PySide6.QtSerialBus.QModbusTcpConnectionObserver) -> None: ...
    def open(self) -> bool: ...


# eof