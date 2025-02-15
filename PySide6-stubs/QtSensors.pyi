# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtSensors, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtSensors`

import PySide6.QtSensors
import PySide6.QtCore

import os
import enum
from typing import Any, ClassVar, List, Optional, Tuple, Union, overload
from PySide6.QtCore import Signal
from shiboken6 import Shiboken
from typing import TypeAlias, TypeVar


NoneType: TypeAlias = type[None]
PlaceHolderType = TypeVar("PlaceHolderType", bound=QObject)


class QAccelerometer(PySide6.QtSensors.QSensor):

    accelerationModeChanged  : ClassVar[Signal] = ... # accelerationModeChanged(AccelerationMode)

    class AccelerationMode(enum.Enum):

        Combined                 : QAccelerometer.AccelerationMode = ... # 0x0
        Gravity                  : QAccelerometer.AccelerationMode = ... # 0x1
        User                     : QAccelerometer.AccelerationMode = ... # 0x2


    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def accelerationMode(self) -> PySide6.QtSensors.QAccelerometer.AccelerationMode: ...
    def reading(self) -> PySide6.QtSensors.QAccelerometerReading: ...
    def setAccelerationMode(self, accelerationMode: PySide6.QtSensors.QAccelerometer.AccelerationMode) -> None: ...


class QAccelerometerFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QAccelerometerReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QAccelerometerReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def setX(self, x: float) -> None: ...
    def setY(self, y: float) -> None: ...
    def setZ(self, z: float) -> None: ...
    def x(self) -> float: ...
    def y(self) -> float: ...
    def z(self) -> float: ...


class QAmbientLightFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QAmbientLightReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QAmbientLightReading(PySide6.QtSensors.QSensorReading):

    class LightLevel(enum.Enum):

        Undefined                : QAmbientLightReading.LightLevel = ... # 0x0
        Dark                     : QAmbientLightReading.LightLevel = ... # 0x1
        Twilight                 : QAmbientLightReading.LightLevel = ... # 0x2
        Light                    : QAmbientLightReading.LightLevel = ... # 0x3
        Bright                   : QAmbientLightReading.LightLevel = ... # 0x4
        Sunny                    : QAmbientLightReading.LightLevel = ... # 0x5


    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def lightLevel(self) -> PySide6.QtSensors.QAmbientLightReading.LightLevel: ...
    def setLightLevel(self, lightLevel: PySide6.QtSensors.QAmbientLightReading.LightLevel) -> None: ...


class QAmbientLightSensor(PySide6.QtSensors.QSensor):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QAmbientLightReading: ...


class QAmbientTemperatureFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QAmbientTemperatureReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QAmbientTemperatureReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def setTemperature(self, temperature: float) -> None: ...
    def temperature(self) -> float: ...


class QAmbientTemperatureSensor(PySide6.QtSensors.QSensor):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QAmbientTemperatureReading: ...


class QCompass(PySide6.QtSensors.QSensor):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QCompassReading: ...


class QCompassFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QCompassReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QCompassReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def azimuth(self) -> float: ...
    def calibrationLevel(self) -> float: ...
    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def setAzimuth(self, azimuth: float) -> None: ...
    def setCalibrationLevel(self, calibrationLevel: float) -> None: ...


class QGyroscope(PySide6.QtSensors.QSensor):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QGyroscopeReading: ...


class QGyroscopeFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QGyroscopeReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QGyroscopeReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def setX(self, x: float) -> None: ...
    def setY(self, y: float) -> None: ...
    def setZ(self, z: float) -> None: ...
    def x(self) -> float: ...
    def y(self) -> float: ...
    def z(self) -> float: ...


class QHumidityFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QHumidityReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QHumidityReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def absoluteHumidity(self) -> float: ...
    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def relativeHumidity(self) -> float: ...
    def setAbsoluteHumidity(self, value: float) -> None: ...
    def setRelativeHumidity(self, percent: float) -> None: ...


class QHumiditySensor(PySide6.QtSensors.QSensor):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QHumidityReading: ...


class QIRProximityFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QIRProximityReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QIRProximityReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def reflectance(self) -> float: ...
    def setReflectance(self, reflectance: float) -> None: ...


class QIRProximitySensor(PySide6.QtSensors.QSensor):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QIRProximityReading: ...


class QIntList(object): ...


class QLidFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QLidReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QLidReading(PySide6.QtSensors.QSensorReading):

    backLidChanged           : ClassVar[Signal] = ... # backLidChanged(bool)
    frontLidChanged          : ClassVar[Signal] = ... # frontLidChanged(bool)

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def backLidClosed(self) -> bool: ...
    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def frontLidClosed(self) -> bool: ...
    def setBackLidClosed(self, closed: bool) -> None: ...
    def setFrontLidClosed(self, closed: bool) -> None: ...


class QLidSensor(PySide6.QtSensors.QSensor):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QLidReading: ...


class QLightFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QLightReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QLightReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def lux(self) -> float: ...
    def setLux(self, lux: float) -> None: ...


class QLightSensor(PySide6.QtSensors.QSensor):

    fieldOfViewChanged       : ClassVar[Signal] = ... # fieldOfViewChanged(double)

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def fieldOfView(self) -> float: ...
    def reading(self) -> PySide6.QtSensors.QLightReading: ...
    def setFieldOfView(self, fieldOfView: float) -> None: ...


class QMagnetometer(PySide6.QtSensors.QSensor):

    returnGeoValuesChanged   : ClassVar[Signal] = ... # returnGeoValuesChanged(bool)

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QMagnetometerReading: ...
    def returnGeoValues(self) -> bool: ...
    def setReturnGeoValues(self, returnGeoValues: bool) -> None: ...


class QMagnetometerFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QMagnetometerReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QMagnetometerReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def calibrationLevel(self) -> float: ...
    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def setCalibrationLevel(self, calibrationLevel: float) -> None: ...
    def setX(self, x: float) -> None: ...
    def setY(self, y: float) -> None: ...
    def setZ(self, z: float) -> None: ...
    def x(self) -> float: ...
    def y(self) -> float: ...
    def z(self) -> float: ...


class QOrientationFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QOrientationReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QOrientationReading(PySide6.QtSensors.QSensorReading):

    class Orientation(enum.Enum):

        Undefined                : QOrientationReading.Orientation = ... # 0x0
        TopUp                    : QOrientationReading.Orientation = ... # 0x1
        TopDown                  : QOrientationReading.Orientation = ... # 0x2
        LeftUp                   : QOrientationReading.Orientation = ... # 0x3
        RightUp                  : QOrientationReading.Orientation = ... # 0x4
        FaceUp                   : QOrientationReading.Orientation = ... # 0x5
        FaceDown                 : QOrientationReading.Orientation = ... # 0x6


    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def orientation(self) -> PySide6.QtSensors.QOrientationReading.Orientation: ...
    def setOrientation(self, orientation: PySide6.QtSensors.QOrientationReading.Orientation) -> None: ...


class QOrientationSensor(PySide6.QtSensors.QSensor):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QOrientationReading: ...


class QPressureFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QPressureReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QPressureReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def pressure(self) -> float: ...
    def setPressure(self, pressure: float) -> None: ...
    def setTemperature(self, temperature: float) -> None: ...
    def temperature(self) -> float: ...


class QPressureSensor(PySide6.QtSensors.QSensor):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QPressureReading: ...


class QProximityFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QProximityReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QProximityReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def close(self) -> bool: ...
    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def setClose(self, close: bool) -> None: ...


class QProximitySensor(PySide6.QtSensors.QSensor):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QProximityReading: ...


class QRotationFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QRotationReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...


class QRotationReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def setFromEuler(self, x: float, y: float, z: float) -> None: ...
    def x(self) -> float: ...
    def y(self) -> float: ...
    def z(self) -> float: ...


class QRotationSensor(PySide6.QtSensors.QSensor):

    hasZChanged              : ClassVar[Signal] = ... # hasZChanged(bool)

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def hasZ(self) -> bool: ...
    def reading(self) -> PySide6.QtSensors.QRotationReading: ...
    def setHasZ(self, hasZ: bool) -> None: ...


class QSensor(PySide6.QtCore.QObject):

    activeChanged            : ClassVar[Signal] = ... # activeChanged()
    alwaysOnChanged          : ClassVar[Signal] = ... # alwaysOnChanged()
    availableSensorsChanged  : ClassVar[Signal] = ... # availableSensorsChanged()
    axesOrientationModeChanged: ClassVar[Signal] = ... # axesOrientationModeChanged(AxesOrientationMode)
    bufferSizeChanged        : ClassVar[Signal] = ... # bufferSizeChanged(int)
    busyChanged              : ClassVar[Signal] = ... # busyChanged()
    currentOrientationChanged: ClassVar[Signal] = ... # currentOrientationChanged(int)
    dataRateChanged          : ClassVar[Signal] = ... # dataRateChanged()
    efficientBufferSizeChanged: ClassVar[Signal] = ... # efficientBufferSizeChanged(int)
    identifierChanged        : ClassVar[Signal] = ... # identifierChanged()
    maxBufferSizeChanged     : ClassVar[Signal] = ... # maxBufferSizeChanged(int)
    readingChanged           : ClassVar[Signal] = ... # readingChanged()
    sensorError              : ClassVar[Signal] = ... # sensorError(int)
    skipDuplicatesChanged    : ClassVar[Signal] = ... # skipDuplicatesChanged(bool)
    userOrientationChanged   : ClassVar[Signal] = ... # userOrientationChanged(int)

    class AxesOrientationMode(enum.Enum):

        FixedOrientation         : QSensor.AxesOrientationMode = ... # 0x0
        AutomaticOrientation     : QSensor.AxesOrientationMode = ... # 0x1
        UserOrientation          : QSensor.AxesOrientationMode = ... # 0x2

    class Feature(enum.Enum):

        Buffering                : QSensor.Feature = ... # 0x0
        AlwaysOn                 : QSensor.Feature = ... # 0x1
        GeoValues                : QSensor.Feature = ... # 0x2
        FieldOfView              : QSensor.Feature = ... # 0x3
        AccelerationMode         : QSensor.Feature = ... # 0x4
        SkipDuplicates           : QSensor.Feature = ... # 0x5
        AxesOrientation          : QSensor.Feature = ... # 0x6
        PressureSensorTemperature: QSensor.Feature = ... # 0x7
        Reserved                 : QSensor.Feature = ... # 0x101


    def __init__(self, type: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def addFilter(self, filter: PySide6.QtSensors.QSensorFilter) -> None: ...
    def availableDataRates(self) -> List[Tuple[int, int]]: ...
    def axesOrientationMode(self) -> PySide6.QtSensors.QSensor.AxesOrientationMode: ...
    def backend(self) -> PySide6.QtSensors.QSensorBackend: ...
    def bufferSize(self) -> int: ...
    def connectToBackend(self) -> bool: ...
    def currentOrientation(self) -> int: ...
    def dataRate(self) -> int: ...
    @staticmethod
    def defaultSensorForType(type: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> PySide6.QtCore.QByteArray: ...
    def description(self) -> str: ...
    def efficientBufferSize(self) -> int: ...
    def error(self) -> int: ...
    def filters(self) -> List[PySide6.QtSensors.QSensorFilter]: ...
    def identifier(self) -> PySide6.QtCore.QByteArray: ...
    def isActive(self) -> bool: ...
    def isAlwaysOn(self) -> bool: ...
    def isBusy(self) -> bool: ...
    def isConnectedToBackend(self) -> bool: ...
    def isFeatureSupported(self, feature: PySide6.QtSensors.QSensor.Feature) -> bool: ...
    def maxBufferSize(self) -> int: ...
    def outputRange(self) -> int: ...
    def outputRanges(self) -> List[PySide6.QtSensors.qoutputrange]: ...
    def reading(self) -> PySide6.QtSensors.QSensorReading: ...
    def removeFilter(self, filter: PySide6.QtSensors.QSensorFilter) -> None: ...
    @staticmethod
    def sensorTypes() -> List[PySide6.QtCore.QByteArray]: ...
    @staticmethod
    def sensorsForType(type: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> List[PySide6.QtCore.QByteArray]: ...
    def setActive(self, active: bool) -> None: ...
    def setAlwaysOn(self, alwaysOn: bool) -> None: ...
    def setAxesOrientationMode(self, axesOrientationMode: PySide6.QtSensors.QSensor.AxesOrientationMode) -> None: ...
    def setBufferSize(self, bufferSize: int) -> None: ...
    def setCurrentOrientation(self, currentOrientation: int) -> None: ...
    def setDataRate(self, rate: int) -> None: ...
    def setEfficientBufferSize(self, efficientBufferSize: int) -> None: ...
    def setIdentifier(self, identifier: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> None: ...
    def setMaxBufferSize(self, maxBufferSize: int) -> None: ...
    def setOutputRange(self, index: int) -> None: ...
    def setSkipDuplicates(self, skipDuplicates: bool) -> None: ...
    def setUserOrientation(self, userOrientation: int) -> None: ...
    def skipDuplicates(self) -> bool: ...
    def start(self) -> bool: ...
    def stop(self) -> None: ...
    def type(self) -> PySide6.QtCore.QByteArray: ...
    def userOrientation(self) -> int: ...


class QSensorBackend(PySide6.QtCore.QObject):

    def __init__(self, sensor: PySide6.QtSensors.QSensor, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def addDataRate(self, min: float, max: float) -> None: ...
    def addOutputRange(self, min: float, max: float, accuracy: float) -> None: ...
    def isFeatureSupported(self, feature: PySide6.QtSensors.QSensor.Feature) -> bool: ...
    def newReadingAvailable(self) -> None: ...
    def reading(self) -> PySide6.QtSensors.QSensorReading: ...
    def sensor(self) -> PySide6.QtSensors.QSensor: ...
    def sensorBusy(self, busy: bool = ...) -> None: ...
    def sensorError(self, error: int) -> None: ...
    def sensorStopped(self) -> None: ...
    def setDataRates(self, otherSensor: PySide6.QtSensors.QSensor) -> None: ...
    def setDescription(self, description: str) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...


class QSensorBackendFactory(Shiboken.Object):

    def __init__(self) -> None: ...

    def createBackend(self, sensor: PySide6.QtSensors.QSensor) -> PySide6.QtSensors.QSensorBackend: ...


class QSensorChangesInterface(Shiboken.Object):

    def __init__(self) -> None: ...

    def sensorsChanged(self) -> None: ...


class QSensorFilter(Shiboken.Object):

    def __init__(self) -> None: ...

    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...
    def setSensor(self, sensor: PySide6.QtSensors.QSensor) -> None: ...


class QSensorManager(Shiboken.Object):

    def __init__(self) -> None: ...

    @staticmethod
    def createBackend(sensor: PySide6.QtSensors.QSensor) -> PySide6.QtSensors.QSensorBackend: ...
    @staticmethod
    def isBackendRegistered(type: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], identifier: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> bool: ...
    @staticmethod
    def registerBackend(type: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], identifier: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], factory: PySide6.QtSensors.QSensorBackendFactory) -> None: ...
    @staticmethod
    def setDefaultBackend(type: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], identifier: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> None: ...
    @staticmethod
    def unregisterBackend(type: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], identifier: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview]) -> None: ...


class QSensorPluginInterface(Shiboken.Object):

    def __init__(self) -> None: ...

    def registerSensors(self) -> None: ...


class QSensorReading(PySide6.QtCore.QObject):
    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def setTimestamp(self, timestamp: int) -> None: ...
    def timestamp(self) -> int: ...
    def value(self, index: int) -> Any: ...
    def valueCount(self) -> int: ...


class QTapFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QTapReading) -> bool: ...


class QTapReading(PySide6.QtSensors.QSensorReading):

    class TapDirection(enum.Enum):

        Undefined                : QTapReading.TapDirection = ... # 0x0
        X                        : QTapReading.TapDirection = ... # 0x1
        Y                        : QTapReading.TapDirection = ... # 0x2
        Z                        : QTapReading.TapDirection = ... # 0x4
        X_Pos                    : QTapReading.TapDirection = ... # 0x11
        Y_Pos                    : QTapReading.TapDirection = ... # 0x22
        Z_Pos                    : QTapReading.TapDirection = ... # 0x44
        X_Neg                    : QTapReading.TapDirection = ... # 0x101
        X_Both                   : QTapReading.TapDirection = ... # 0x111
        Y_Neg                    : QTapReading.TapDirection = ... # 0x202
        Y_Both                   : QTapReading.TapDirection = ... # 0x222
        Z_Neg                    : QTapReading.TapDirection = ... # 0x404
        Z_Both                   : QTapReading.TapDirection = ... # 0x444


    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def isDoubleTap(self) -> bool: ...
    def setDoubleTap(self, doubleTap: bool) -> None: ...
    def setTapDirection(self, tapDirection: PySide6.QtSensors.QTapReading.TapDirection) -> None: ...
    def tapDirection(self) -> PySide6.QtSensors.QTapReading.TapDirection: ...


class QTapSensor(PySide6.QtSensors.QSensor):

    returnDoubleTapEventsChanged: ClassVar[Signal] = ... # returnDoubleTapEventsChanged(bool)

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def reading(self) -> PySide6.QtSensors.QTapReading: ...
    def returnDoubleTapEvents(self) -> bool: ...
    def setReturnDoubleTapEvents(self, returnDoubleTapEvents: bool) -> None: ...


class QTiltFilter(PySide6.QtSensors.QSensorFilter):
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool: ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QTiltReading) -> bool: ...


class QTiltReading(PySide6.QtSensors.QSensorReading):

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def setXRotation(self, x: float) -> None: ...
    def setYRotation(self, y: float) -> None: ...
    def xRotation(self) -> float: ...
    def yRotation(self) -> float: ...


class QTiltSensor(PySide6.QtSensors.QSensor):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def calibrate(self) -> None: ...
    def reading(self) -> PySide6.QtSensors.QTiltReading: ...


class qoutputrange(Shiboken.Object):

    accuracy: float
    maximum: float
    minimum: float


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, qoutputrange: PySide6.QtSensors.qoutputrange) -> None: ...

    @staticmethod
    def __copy__() -> None: ...


# eof
