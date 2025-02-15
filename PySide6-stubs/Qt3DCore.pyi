# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations
"""
This file contains the exact signatures for all functions in module
PySide6.Qt3DCore, except for defaults which are replaced by "...".

# mypy: disable-error-code="override, overload-overlap"
"""

# Module `PySide6.Qt3DCore`

import PySide6.Qt3DCore
import PySide6.QtCore
import PySide6.QtGui

import enum
import typing
from collections.abc import Iterable
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


class QIntList(object): ...


class Qt3DCore(Shiboken.Object):

    class QAbstractAspect(PySide6.QtCore.QObject):

        def __init__(self, /, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

        def dependencies(self, /) -> typing.List[str]: ...
        def registerBackendType(self, obj: PySide6.QtCore.QMetaObject, functor: PySide6.Qt3DCore.Qt3DCore.QBackendNodeMapperPtr, /) -> None: ...
        def rootEntityId(self, /) -> PySide6.Qt3DCore.Qt3DCore.QNodeId: ...
        def scheduleSingleShotJob(self, job: PySide6.Qt3DCore.Qt3DCore.QAspectJobPtr, /) -> None: ...
        def unregisterBackendType(self, arg__1: PySide6.QtCore.QMetaObject, /) -> None: ...

    class QAbstractFunctor(Shiboken.Object):

        def __init__(self, /) -> None: ...

        def id(self, /) -> int: ...

    class QAbstractSkeleton(PySide6.Qt3DCore.Qt3DCore.QNode):

        jointCountChanged        : typing.ClassVar[Signal] = ... # jointCountChanged(int)
        def jointCount(self, /) -> int: ...

    class QArmature(PySide6.Qt3DCore.Qt3DCore.QComponent):

        skeletonChanged          : typing.ClassVar[Signal] = ... # skeletonChanged(Qt3DCore::QAbstractSkeleton*)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, skeleton: PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton | None= ...) -> None: ...

        def setSkeleton(self, skeleton: PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton, /) -> None: ...
        def skeleton(self, /) -> PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton: ...

    class QAspectEngine(PySide6.QtCore.QObject):

        class RunMode(enum.Enum):

            Manual                    = ...  # 0x0
            Automatic                 = ...  # 0x1


        def __init__(self, /, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

        def aspect(self, name: str, /) -> PySide6.Qt3DCore.Qt3DCore.QAbstractAspect: ...
        def aspects(self, /) -> typing.List[PySide6.Qt3DCore.Qt3DCore.QAbstractAspect]: ...
        def executeCommand(self, command: str, /) -> typing.Any: ...
        def lookupNode(self, id: PySide6.Qt3DCore.Qt3DCore.QNodeId, /) -> PySide6.Qt3DCore.Qt3DCore.QNode: ...
        def lookupNodes(self, ids: typing.Sequence[PySide6.Qt3DCore.Qt3DCore.QNodeId], /) -> typing.List[PySide6.Qt3DCore.Qt3DCore.QNode]: ...
        def processFrame(self, /) -> None: ...
        @typing.overload
        def registerAspect(self, aspect: PySide6.Qt3DCore.Qt3DCore.QAbstractAspect, /) -> None: ...
        @typing.overload
        def registerAspect(self, name: str, /) -> None: ...
        def rootEntity(self, /) -> PySide6.Qt3DCore.Qt3DCore.QEntityPtr: ...
        def runMode(self, /) -> PySide6.Qt3DCore.Qt3DCore.QAspectEngine.RunMode: ...
        def setRootEntity(self, root: PySide6.Qt3DCore.Qt3DCore.QEntityPtr, /) -> None: ...
        def setRunMode(self, mode: PySide6.Qt3DCore.Qt3DCore.QAspectEngine.RunMode, /) -> None: ...
        @typing.overload
        def unregisterAspect(self, aspect: PySide6.Qt3DCore.Qt3DCore.QAbstractAspect, /) -> None: ...
        @typing.overload
        def unregisterAspect(self, name: str, /) -> None: ...

    class QAspectJob(Shiboken.Object):

        def __init__(self, /) -> None: ...

        def isRequired(self, /) -> bool: ...
        def postFrame(self, aspectEngine: PySide6.Qt3DCore.Qt3DCore.QAspectEngine, /) -> None: ...
        def run(self, /) -> None: ...

    class QAspectJobPtr(Shiboken.Object):

        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, pointee: PySide6.Qt3DCore.Qt3DCore.QAspectJob, /) -> None: ...

        def __copy__(self, /) -> typing.Self: ...
        def __dir__(self, /) -> typing.Iterable[str]: ...
        def __repr__(self, /) -> str: ...
        def data(self, /) -> PySide6.Qt3DCore.Qt3DCore.QAspectJob: ...
        @typing.overload
        def reset(self, /) -> None: ...
        @typing.overload
        def reset(self, t: PySide6.Qt3DCore.Qt3DCore.QAspectJob, /) -> None: ...

    class QAttribute(PySide6.Qt3DCore.Qt3DCore.QNode):

        attributeTypeChanged     : typing.ClassVar[Signal] = ... # attributeTypeChanged(AttributeType)
        bufferChanged            : typing.ClassVar[Signal] = ... # bufferChanged(QBuffer*)
        byteOffsetChanged        : typing.ClassVar[Signal] = ... # byteOffsetChanged(uint)
        byteStrideChanged        : typing.ClassVar[Signal] = ... # byteStrideChanged(uint)
        countChanged             : typing.ClassVar[Signal] = ... # countChanged(uint)
        dataSizeChanged          : typing.ClassVar[Signal] = ... # dataSizeChanged(uint)
        dataTypeChanged          : typing.ClassVar[Signal] = ... # dataTypeChanged(VertexBaseType)
        divisorChanged           : typing.ClassVar[Signal] = ... # divisorChanged(uint)
        nameChanged              : typing.ClassVar[Signal] = ... # nameChanged(QString)
        vertexBaseTypeChanged    : typing.ClassVar[Signal] = ... # vertexBaseTypeChanged(VertexBaseType)
        vertexSizeChanged        : typing.ClassVar[Signal] = ... # vertexSizeChanged(uint)

        class AttributeType(enum.Enum):

            VertexAttribute           = ...  # 0x0
            IndexAttribute            = ...  # 0x1
            DrawIndirectAttribute     = ...  # 0x2

        class VertexBaseType(enum.Enum):

            Byte                      = ...  # 0x0
            UnsignedByte              = ...  # 0x1
            Short                     = ...  # 0x2
            UnsignedShort             = ...  # 0x3
            Int                       = ...  # 0x4
            UnsignedInt               = ...  # 0x5
            HalfFloat                 = ...  # 0x6
            Float                     = ...  # 0x7
            Double                    = ...  # 0x8


        @typing.overload
        def __init__(self, buf: PySide6.Qt3DCore.Qt3DCore.QBuffer, vertexBaseType: PySide6.Qt3DCore.Qt3DCore.QAttribute.VertexBaseType, vertexSize: int, count: int, /, offset: int | None= ..., stride: int | None= ..., parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, buffer: PySide6.Qt3DCore.Qt3DCore.QBuffer | None= ..., name: str | None= ..., byteStride: int | None= ..., byteOffset: int | None= ..., divisor: int | None= ..., attributeType: PySide6.Qt3DCore.Qt3DCore.QAttribute.AttributeType | None= ..., defaultPositionAttributeName: str | None= ..., defaultNormalAttributeName: str | None= ..., defaultColorAttributeName: str | None= ..., defaultTextureCoordinateAttributeName: str | None= ..., defaultTextureCoordinate1AttributeName: str | None= ..., defaultTextureCoordinate2AttributeName: str | None= ..., defaultTangentAttributeName: str | None= ..., defaultJointIndicesAttributeName: str | None= ..., defaultJointWeightsAttributeName: str | None= ...) -> None: ...
        @typing.overload
        def __init__(self, buf: PySide6.Qt3DCore.Qt3DCore.QBuffer, name: str, vertexBaseType: PySide6.Qt3DCore.Qt3DCore.QAttribute.VertexBaseType, vertexSize: int, count: int, /, offset: int | None= ..., stride: int | None= ..., parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, buffer: PySide6.Qt3DCore.Qt3DCore.QBuffer | None= ..., byteStride: int | None= ..., byteOffset: int | None= ..., divisor: int | None= ..., attributeType: PySide6.Qt3DCore.Qt3DCore.QAttribute.AttributeType | None= ..., defaultPositionAttributeName: str | None= ..., defaultNormalAttributeName: str | None= ..., defaultColorAttributeName: str | None= ..., defaultTextureCoordinateAttributeName: str | None= ..., defaultTextureCoordinate1AttributeName: str | None= ..., defaultTextureCoordinate2AttributeName: str | None= ..., defaultTangentAttributeName: str | None= ..., defaultJointIndicesAttributeName: str | None= ..., defaultJointWeightsAttributeName: str | None= ...) -> None: ...
        @typing.overload
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, buffer: PySide6.Qt3DCore.Qt3DCore.QBuffer | None= ..., name: str | None= ..., vertexBaseType: PySide6.Qt3DCore.Qt3DCore.QAttribute.VertexBaseType | None= ..., vertexSize: int | None= ..., count: int | None= ..., byteStride: int | None= ..., byteOffset: int | None= ..., divisor: int | None= ..., attributeType: PySide6.Qt3DCore.Qt3DCore.QAttribute.AttributeType | None= ..., defaultPositionAttributeName: str | None= ..., defaultNormalAttributeName: str | None= ..., defaultColorAttributeName: str | None= ..., defaultTextureCoordinateAttributeName: str | None= ..., defaultTextureCoordinate1AttributeName: str | None= ..., defaultTextureCoordinate2AttributeName: str | None= ..., defaultTangentAttributeName: str | None= ..., defaultJointIndicesAttributeName: str | None= ..., defaultJointWeightsAttributeName: str | None= ...) -> None: ...

        def attributeType(self, /) -> PySide6.Qt3DCore.Qt3DCore.QAttribute.AttributeType: ...
        def buffer(self, /) -> PySide6.Qt3DCore.Qt3DCore.QBuffer: ...
        def byteOffset(self, /) -> int: ...
        def byteStride(self, /) -> int: ...
        def count(self, /) -> int: ...
        @staticmethod
        def defaultColorAttributeName() -> str: ...
        @staticmethod
        def defaultJointIndicesAttributeName() -> str: ...
        @staticmethod
        def defaultJointWeightsAttributeName() -> str: ...
        @staticmethod
        def defaultNormalAttributeName() -> str: ...
        @staticmethod
        def defaultPositionAttributeName() -> str: ...
        @staticmethod
        def defaultTangentAttributeName() -> str: ...
        @staticmethod
        def defaultTextureCoordinate1AttributeName() -> str: ...
        @staticmethod
        def defaultTextureCoordinate2AttributeName() -> str: ...
        @staticmethod
        def defaultTextureCoordinateAttributeName() -> str: ...
        def divisor(self, /) -> int: ...
        def name(self, /) -> str: ...
        def setAttributeType(self, attributeType: PySide6.Qt3DCore.Qt3DCore.QAttribute.AttributeType, /) -> None: ...
        def setBuffer(self, buffer: PySide6.Qt3DCore.Qt3DCore.QBuffer, /) -> None: ...
        def setByteOffset(self, byteOffset: int, /) -> None: ...
        def setByteStride(self, byteStride: int, /) -> None: ...
        def setCount(self, count: int, /) -> None: ...
        def setDivisor(self, divisor: int, /) -> None: ...
        def setName(self, name: str, /) -> None: ...
        def setVertexBaseType(self, type: PySide6.Qt3DCore.Qt3DCore.QAttribute.VertexBaseType, /) -> None: ...
        def setVertexSize(self, size: int, /) -> None: ...
        def vertexBaseType(self, /) -> PySide6.Qt3DCore.Qt3DCore.QAttribute.VertexBaseType: ...
        def vertexSize(self, /) -> int: ...

    class QBackendNode(Shiboken.Object):

        class Mode(enum.Enum):

            ReadOnly                  = ...  # 0x0
            ReadWrite                 = ...  # 0x1


        def __init__(self, /, mode: PySide6.Qt3DCore.Qt3DCore.QBackendNode.Mode = ...) -> None: ...

        def isEnabled(self, /) -> bool: ...
        def mode(self, /) -> PySide6.Qt3DCore.Qt3DCore.QBackendNode.Mode: ...
        def peerId(self, /) -> PySide6.Qt3DCore.Qt3DCore.QNodeId: ...
        def setEnabled(self, enabled: bool, /) -> None: ...
        def syncFromFrontEnd(self, frontEnd: PySide6.Qt3DCore.Qt3DCore.QNode, firstTime: bool, /) -> None: ...

    class QBackendNodeMapper(Shiboken.Object):

        def __init__(self, /) -> None: ...

        def create(self, id: PySide6.Qt3DCore.Qt3DCore.QNodeId, /) -> PySide6.Qt3DCore.Qt3DCore.QBackendNode: ...
        def destroy(self, id: PySide6.Qt3DCore.Qt3DCore.QNodeId, /) -> None: ...
        def get(self, id: PySide6.Qt3DCore.Qt3DCore.QNodeId, /) -> PySide6.Qt3DCore.Qt3DCore.QBackendNode: ...

    class QBackendNodeMapperPtr(Shiboken.Object):

        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, pointee: PySide6.Qt3DCore.Qt3DCore.QBackendNodeMapper, /) -> None: ...

        def __copy__(self, /) -> typing.Self: ...
        def __dir__(self, /) -> typing.Iterable[str]: ...
        def __repr__(self, /) -> str: ...
        def data(self, /) -> PySide6.Qt3DCore.Qt3DCore.QBackendNodeMapper: ...
        @typing.overload
        def reset(self, /) -> None: ...
        @typing.overload
        def reset(self, t: PySide6.Qt3DCore.Qt3DCore.QBackendNodeMapper, /) -> None: ...

    class QBoundingVolume(PySide6.Qt3DCore.Qt3DCore.QComponent):

        implicitMaxPointChanged  : typing.ClassVar[Signal] = ... # implicitMaxPointChanged(QVector3D)
        implicitMinPointChanged  : typing.ClassVar[Signal] = ... # implicitMinPointChanged(QVector3D)
        implicitPointsValidChanged: typing.ClassVar[Signal] = ... # implicitPointsValidChanged(bool)
        maxPointChanged          : typing.ClassVar[Signal] = ... # maxPointChanged(QVector3D)
        minPointChanged          : typing.ClassVar[Signal] = ... # minPointChanged(QVector3D)
        viewChanged              : typing.ClassVar[Signal] = ... # viewChanged(QGeometryView*)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, view: PySide6.Qt3DCore.Qt3DCore.QGeometryView | None= ..., implicitMinPoint: PySide6.QtGui.QVector3D | None= ..., implicitMaxPoint: PySide6.QtGui.QVector3D | None= ..., implicitPointsValid: bool | None= ..., minPoint: PySide6.QtGui.QVector3D | None= ..., maxPoint: PySide6.QtGui.QVector3D | None= ...) -> None: ...

        def areImplicitPointsValid(self, /) -> bool: ...
        def implicitMaxPoint(self, /) -> PySide6.QtGui.QVector3D: ...
        def implicitMinPoint(self, /) -> PySide6.QtGui.QVector3D: ...
        def maxPoint(self, /) -> PySide6.QtGui.QVector3D: ...
        def minPoint(self, /) -> PySide6.QtGui.QVector3D: ...
        def setMaxPoint(self, maxPoint: PySide6.QtGui.QVector3D, /) -> None: ...
        def setMinPoint(self, minPoint: PySide6.QtGui.QVector3D, /) -> None: ...
        def setView(self, view: PySide6.Qt3DCore.Qt3DCore.QGeometryView, /) -> None: ...
        def updateImplicitBounds(self, /) -> bool: ...
        def view(self, /) -> PySide6.Qt3DCore.Qt3DCore.QGeometryView: ...

    class QBuffer(PySide6.Qt3DCore.Qt3DCore.QNode):

        accessTypeChanged        : typing.ClassVar[Signal] = ... # accessTypeChanged(AccessType)
        dataAvailable            : typing.ClassVar[Signal] = ... # dataAvailable()
        dataChanged              : typing.ClassVar[Signal] = ... # dataChanged(QByteArray)
        usageChanged             : typing.ClassVar[Signal] = ... # usageChanged(UsageType)

        class AccessType(enum.Enum):

            Write                     = ...  # 0x1
            Read                      = ...  # 0x2
            ReadWrite                 = ...  # 0x3

        class UsageType(enum.Enum):

            StreamDraw                = ...  # 0x88e0
            StreamRead                = ...  # 0x88e1
            StreamCopy                = ...  # 0x88e2
            StaticDraw                = ...  # 0x88e4
            StaticRead                = ...  # 0x88e5
            StaticCopy                = ...  # 0x88e6
            DynamicDraw               = ...  # 0x88e8
            DynamicRead               = ...  # 0x88e9
            DynamicCopy               = ...  # 0x88ea


        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, usage: PySide6.Qt3DCore.Qt3DCore.QBuffer.UsageType | None= ..., accessType: PySide6.Qt3DCore.Qt3DCore.QBuffer.AccessType | None= ...) -> None: ...

        def accessType(self, /) -> PySide6.Qt3DCore.Qt3DCore.QBuffer.AccessType: ...
        def data(self, /) -> PySide6.QtCore.QByteArray: ...
        def setAccessType(self, access: PySide6.Qt3DCore.Qt3DCore.QBuffer.AccessType, /) -> None: ...
        def setData(self, bytes: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview, /) -> None: ...
        def setUsage(self, usage: PySide6.Qt3DCore.Qt3DCore.QBuffer.UsageType, /) -> None: ...
        def updateData(self, offset: int, bytes: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview, /) -> None: ...
        def usage(self, /) -> PySide6.Qt3DCore.Qt3DCore.QBuffer.UsageType: ...

    class QComponent(PySide6.Qt3DCore.Qt3DCore.QNode):

        addedToEntity            : typing.ClassVar[Signal] = ... # addedToEntity(QEntity*)
        removedFromEntity        : typing.ClassVar[Signal] = ... # removedFromEntity(QEntity*)
        shareableChanged         : typing.ClassVar[Signal] = ... # shareableChanged(bool)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, isShareable: bool | None= ...) -> None: ...

        def entities(self, /) -> typing.List[PySide6.Qt3DCore.Qt3DCore.QEntity]: ...
        def isShareable(self, /) -> bool: ...
        def setShareable(self, isShareable: bool, /) -> None: ...

    class QCoreAspect(PySide6.Qt3DCore.Qt3DCore.QAbstractAspect):

        def __init__(self, /, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

        def calculateBoundingVolumeJob(self, /) -> PySide6.Qt3DCore.Qt3DCore.QAspectJobPtr: ...

    class QCoreSettings(PySide6.Qt3DCore.Qt3DCore.QComponent):

        boundingVolumesEnabledChanged: typing.ClassVar[Signal] = ... # boundingVolumesEnabledChanged(bool)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, boundingVolumesEnabled: bool | None= ...) -> None: ...

        def boundingVolumesEnabled(self, /) -> bool: ...
        def setBoundingVolumesEnabled(self, boundingVolumesEnabled: bool, /) -> None: ...

    class QEntity(PySide6.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ...) -> None: ...

        def addComponent(self, comp: PySide6.Qt3DCore.Qt3DCore.QComponent, /) -> None: ...
        def components(self, /) -> typing.List[PySide6.Qt3DCore.Qt3DCore.QComponent]: ...
        def parentEntity(self, /) -> PySide6.Qt3DCore.Qt3DCore.QEntity: ...
        def removeComponent(self, comp: PySide6.Qt3DCore.Qt3DCore.QComponent, /) -> None: ...

    class QEntityPtr(Shiboken.Object):

        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, pointee: PySide6.Qt3DCore.Qt3DCore.QEntity, /) -> None: ...

        def __copy__(self, /) -> typing.Self: ...
        def __dir__(self, /) -> typing.Iterable[str]: ...
        def __repr__(self, /) -> str: ...
        def data(self, /) -> PySide6.Qt3DCore.Qt3DCore.QEntity: ...
        @typing.overload
        def reset(self, /) -> None: ...
        @typing.overload
        def reset(self, t: PySide6.Qt3DCore.Qt3DCore.QEntity, /) -> None: ...

    class QGeometry(PySide6.Qt3DCore.Qt3DCore.QNode):

        boundingVolumePositionAttributeChanged: typing.ClassVar[Signal] = ... # boundingVolumePositionAttributeChanged(QAttribute*)
        maxExtentChanged         : typing.ClassVar[Signal] = ... # maxExtentChanged(QVector3D)
        minExtentChanged         : typing.ClassVar[Signal] = ... # minExtentChanged(QVector3D)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, boundingVolumePositionAttribute: PySide6.Qt3DCore.Qt3DCore.QAttribute | None= ..., minExtent: PySide6.QtGui.QVector3D | None= ..., maxExtent: PySide6.QtGui.QVector3D | None= ...) -> None: ...

        def addAttribute(self, attribute: PySide6.Qt3DCore.Qt3DCore.QAttribute, /) -> None: ...
        def attributes(self, /) -> typing.List[PySide6.Qt3DCore.Qt3DCore.QAttribute]: ...
        def boundingVolumePositionAttribute(self, /) -> PySide6.Qt3DCore.Qt3DCore.QAttribute: ...
        def maxExtent(self, /) -> PySide6.QtGui.QVector3D: ...
        def minExtent(self, /) -> PySide6.QtGui.QVector3D: ...
        def removeAttribute(self, attribute: PySide6.Qt3DCore.Qt3DCore.QAttribute, /) -> None: ...
        def setBoundingVolumePositionAttribute(self, boundingVolumePositionAttribute: PySide6.Qt3DCore.Qt3DCore.QAttribute, /) -> None: ...

    class QGeometryView(PySide6.Qt3DCore.Qt3DCore.QNode):

        firstInstanceChanged     : typing.ClassVar[Signal] = ... # firstInstanceChanged(int)
        firstVertexChanged       : typing.ClassVar[Signal] = ... # firstVertexChanged(int)
        geometryChanged          : typing.ClassVar[Signal] = ... # geometryChanged(QGeometry*)
        indexBufferByteOffsetChanged: typing.ClassVar[Signal] = ... # indexBufferByteOffsetChanged(int)
        indexOffsetChanged       : typing.ClassVar[Signal] = ... # indexOffsetChanged(int)
        instanceCountChanged     : typing.ClassVar[Signal] = ... # instanceCountChanged(int)
        primitiveRestartEnabledChanged: typing.ClassVar[Signal] = ... # primitiveRestartEnabledChanged(bool)
        primitiveTypeChanged     : typing.ClassVar[Signal] = ... # primitiveTypeChanged(PrimitiveType)
        restartIndexValueChanged : typing.ClassVar[Signal] = ... # restartIndexValueChanged(int)
        vertexCountChanged       : typing.ClassVar[Signal] = ... # vertexCountChanged(int)
        verticesPerPatchChanged  : typing.ClassVar[Signal] = ... # verticesPerPatchChanged(int)

        class PrimitiveType(enum.Enum):

            Points                    = ...  # 0x0
            Lines                     = ...  # 0x1
            LineLoop                  = ...  # 0x2
            LineStrip                 = ...  # 0x3
            Triangles                 = ...  # 0x4
            TriangleStrip             = ...  # 0x5
            TriangleFan               = ...  # 0x6
            LinesAdjacency            = ...  # 0xa
            LineStripAdjacency        = ...  # 0xb
            TrianglesAdjacency        = ...  # 0xc
            TriangleStripAdjacency    = ...  # 0xd
            Patches                   = ...  # 0xe


        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, instanceCount: int | None= ..., vertexCount: int | None= ..., indexOffset: int | None= ..., firstInstance: int | None= ..., firstVertex: int | None= ..., indexBufferByteOffset: int | None= ..., restartIndexValue: int | None= ..., verticesPerPatch: int | None= ..., primitiveRestartEnabled: bool | None= ..., geometry: PySide6.Qt3DCore.Qt3DCore.QGeometry | None= ..., primitiveType: PySide6.Qt3DCore.Qt3DCore.QGeometryView.PrimitiveType | None= ...) -> None: ...

        def firstInstance(self, /) -> int: ...
        def firstVertex(self, /) -> int: ...
        def geometry(self, /) -> PySide6.Qt3DCore.Qt3DCore.QGeometry: ...
        def indexBufferByteOffset(self, /) -> int: ...
        def indexOffset(self, /) -> int: ...
        def instanceCount(self, /) -> int: ...
        def primitiveRestartEnabled(self, /) -> bool: ...
        def primitiveType(self, /) -> PySide6.Qt3DCore.Qt3DCore.QGeometryView.PrimitiveType: ...
        def restartIndexValue(self, /) -> int: ...
        def setFirstInstance(self, firstInstance: int, /) -> None: ...
        def setFirstVertex(self, firstVertex: int, /) -> None: ...
        def setGeometry(self, geometry: PySide6.Qt3DCore.Qt3DCore.QGeometry, /) -> None: ...
        def setIndexBufferByteOffset(self, offset: int, /) -> None: ...
        def setIndexOffset(self, indexOffset: int, /) -> None: ...
        def setInstanceCount(self, instanceCount: int, /) -> None: ...
        def setPrimitiveRestartEnabled(self, enabled: bool, /) -> None: ...
        def setPrimitiveType(self, primitiveType: PySide6.Qt3DCore.Qt3DCore.QGeometryView.PrimitiveType, /) -> None: ...
        def setRestartIndexValue(self, index: int, /) -> None: ...
        def setVertexCount(self, vertexCount: int, /) -> None: ...
        def setVerticesPerPatch(self, verticesPerPatch: int, /) -> None: ...
        def vertexCount(self, /) -> int: ...
        def verticesPerPatch(self, /) -> int: ...

    class QJoint(PySide6.Qt3DCore.Qt3DCore.QNode):

        inverseBindMatrixChanged : typing.ClassVar[Signal] = ... # inverseBindMatrixChanged(QMatrix4x4)
        nameChanged              : typing.ClassVar[Signal] = ... # nameChanged(QString)
        rotationChanged          : typing.ClassVar[Signal] = ... # rotationChanged(QQuaternion)
        rotationXChanged         : typing.ClassVar[Signal] = ... # rotationXChanged(float)
        rotationYChanged         : typing.ClassVar[Signal] = ... # rotationYChanged(float)
        rotationZChanged         : typing.ClassVar[Signal] = ... # rotationZChanged(float)
        scaleChanged             : typing.ClassVar[Signal] = ... # scaleChanged(QVector3D)
        translationChanged       : typing.ClassVar[Signal] = ... # translationChanged(QVector3D)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, scale: PySide6.QtGui.QVector3D | None= ..., rotation: PySide6.QtGui.QQuaternion | None= ..., translation: PySide6.QtGui.QVector3D | None= ..., inverseBindMatrix: PySide6.QtGui.QMatrix4x4 | None= ..., rotationX: float | None= ..., rotationY: float | None= ..., rotationZ: float | None= ..., name: str | None= ...) -> None: ...

        def addChildJoint(self, joint: PySide6.Qt3DCore.Qt3DCore.QJoint, /) -> None: ...
        def childJoints(self, /) -> typing.List[PySide6.Qt3DCore.Qt3DCore.QJoint]: ...
        def inverseBindMatrix(self, /) -> PySide6.QtGui.QMatrix4x4: ...
        def name(self, /) -> str: ...
        def removeChildJoint(self, joint: PySide6.Qt3DCore.Qt3DCore.QJoint, /) -> None: ...
        def rotation(self, /) -> PySide6.QtGui.QQuaternion: ...
        def rotationX(self, /) -> float: ...
        def rotationY(self, /) -> float: ...
        def rotationZ(self, /) -> float: ...
        def scale(self, /) -> PySide6.QtGui.QVector3D: ...
        def setInverseBindMatrix(self, inverseBindMatrix: PySide6.QtGui.QMatrix4x4 | PySide6.QtGui.QTransform, /) -> None: ...
        def setName(self, name: str, /) -> None: ...
        def setRotation(self, rotation: PySide6.QtGui.QQuaternion, /) -> None: ...
        def setRotationX(self, rotationX: float, /) -> None: ...
        def setRotationY(self, rotationY: float, /) -> None: ...
        def setRotationZ(self, rotationZ: float, /) -> None: ...
        def setScale(self, scale: PySide6.QtGui.QVector3D, /) -> None: ...
        def setToIdentity(self, /) -> None: ...
        def setTranslation(self, translation: PySide6.QtGui.QVector3D, /) -> None: ...
        def translation(self, /) -> PySide6.QtGui.QVector3D: ...

    class QNode(PySide6.QtCore.QObject):

        enabledChanged           : typing.ClassVar[Signal] = ... # enabledChanged(bool)
        nodeDestroyed            : typing.ClassVar[Signal] = ... # nodeDestroyed()
        parentChanged            : typing.ClassVar[Signal] = ... # parentChanged(QObject*)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, enabled: bool | None= ...) -> None: ...

        def blockNotifications(self, block: bool, /) -> bool: ...
        def childNodes(self, /) -> typing.List[PySide6.Qt3DCore.Qt3DCore.QNode]: ...
        def id(self, /) -> PySide6.Qt3DCore.Qt3DCore.QNodeId: ...
        def isEnabled(self, /) -> bool: ...
        def notificationsBlocked(self, /) -> bool: ...
        def parentNode(self, /) -> PySide6.Qt3DCore.Qt3DCore.QNode: ...
        def setEnabled(self, isEnabled: bool, /) -> None: ...
        def setParent(self, parent: PySide6.Qt3DCore.Qt3DCore.QNode, /) -> None: ...

    class QNodeId(Shiboken.Object):

        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, QNodeId: PySide6.Qt3DCore.Qt3DCore.QNodeId, /) -> None: ...

        def __copy__(self, /) -> typing.Self: ...
        def __eq__(self, other: PySide6.Qt3DCore.Qt3DCore.QNodeId, /) -> bool: ...
        def __gt__(self, other: PySide6.Qt3DCore.Qt3DCore.QNodeId, /) -> bool: ...
        def __lt__(self, other: PySide6.Qt3DCore.Qt3DCore.QNodeId, /) -> bool: ...
        def __ne__(self, other: PySide6.Qt3DCore.Qt3DCore.QNodeId, /) -> bool: ...
        def __repr__(self, /) -> str: ...
        @staticmethod
        def createId() -> PySide6.Qt3DCore.Qt3DCore.QNodeId: ...
        def id(self, /) -> int: ...
        def isNull(self, /) -> bool: ...

    class QNodeIdTypePair(Shiboken.Object):

        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, _id: PySide6.Qt3DCore.Qt3DCore.QNodeId, _type: PySide6.QtCore.QMetaObject, /) -> None: ...
        @typing.overload
        def __init__(self, QNodeIdTypePair: PySide6.Qt3DCore.Qt3DCore.QNodeIdTypePair, /) -> None: ...

        def __copy__(self, /) -> typing.Self: ...

    class QSkeleton(PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton):

        rootJointChanged         : typing.ClassVar[Signal] = ... # rootJointChanged(Qt3DCore::QJoint*)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, rootJoint: PySide6.Qt3DCore.Qt3DCore.QJoint | None= ...) -> None: ...

        def rootJoint(self, /) -> PySide6.Qt3DCore.Qt3DCore.QJoint: ...
        def setRootJoint(self, rootJoint: PySide6.Qt3DCore.Qt3DCore.QJoint, /) -> None: ...

    class QSkeletonLoader(PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton):

        createJointsEnabledChanged: typing.ClassVar[Signal] = ... # createJointsEnabledChanged(bool)
        rootJointChanged         : typing.ClassVar[Signal] = ... # rootJointChanged(Qt3DCore::QJoint*)
        sourceChanged            : typing.ClassVar[Signal] = ... # sourceChanged(QUrl)
        statusChanged            : typing.ClassVar[Signal] = ... # statusChanged(Status)

        class Status(enum.Enum):

            NotReady                  = ...  # 0x0
            Ready                     = ...  # 0x1
            Error                     = ...  # 0x2


        @typing.overload
        def __init__(self, source: PySide6.QtCore.QUrl, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, status: PySide6.Qt3DCore.Qt3DCore.QSkeletonLoader.Status | None= ..., createJointsEnabled: bool | None= ..., rootJoint: PySide6.Qt3DCore.Qt3DCore.QJoint | None= ...) -> None: ...
        @typing.overload
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, source: PySide6.QtCore.QUrl | None= ..., status: PySide6.Qt3DCore.Qt3DCore.QSkeletonLoader.Status | None= ..., createJointsEnabled: bool | None= ..., rootJoint: PySide6.Qt3DCore.Qt3DCore.QJoint | None= ...) -> None: ...

        def isCreateJointsEnabled(self, /) -> bool: ...
        def rootJoint(self, /) -> PySide6.Qt3DCore.Qt3DCore.QJoint: ...
        def setCreateJointsEnabled(self, enabled: bool, /) -> None: ...
        def setSource(self, source: PySide6.QtCore.QUrl | str, /) -> None: ...
        def source(self, /) -> PySide6.QtCore.QUrl: ...
        def status(self, /) -> PySide6.Qt3DCore.Qt3DCore.QSkeletonLoader.Status: ...

    class QTransform(PySide6.Qt3DCore.Qt3DCore.QComponent):

        matrixChanged            : typing.ClassVar[Signal] = ... # matrixChanged()
        rotationChanged          : typing.ClassVar[Signal] = ... # rotationChanged(QQuaternion)
        rotationXChanged         : typing.ClassVar[Signal] = ... # rotationXChanged(float)
        rotationYChanged         : typing.ClassVar[Signal] = ... # rotationYChanged(float)
        rotationZChanged         : typing.ClassVar[Signal] = ... # rotationZChanged(float)
        scale3DChanged           : typing.ClassVar[Signal] = ... # scale3DChanged(QVector3D)
        scaleChanged             : typing.ClassVar[Signal] = ... # scaleChanged(float)
        translationChanged       : typing.ClassVar[Signal] = ... # translationChanged(QVector3D)
        worldMatrixChanged       : typing.ClassVar[Signal] = ... # worldMatrixChanged(QMatrix4x4)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, matrix: PySide6.QtGui.QMatrix4x4 | None= ..., scale: float | None= ..., scale3D: PySide6.QtGui.QVector3D | None= ..., rotation: PySide6.QtGui.QQuaternion | None= ..., translation: PySide6.QtGui.QVector3D | None= ..., rotationX: float | None= ..., rotationY: float | None= ..., rotationZ: float | None= ..., worldMatrix: PySide6.QtGui.QMatrix4x4 | None= ...) -> None: ...

        @staticmethod
        def fromAxes(xAxis: PySide6.QtGui.QVector3D, yAxis: PySide6.QtGui.QVector3D, zAxis: PySide6.QtGui.QVector3D, /) -> PySide6.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxesAndAngles(axis1: PySide6.QtGui.QVector3D, angle1: float, axis2: PySide6.QtGui.QVector3D, angle2: float, /) -> PySide6.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxesAndAngles(axis1: PySide6.QtGui.QVector3D, angle1: float, axis2: PySide6.QtGui.QVector3D, angle2: float, axis3: PySide6.QtGui.QVector3D, angle3: float, /) -> PySide6.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxisAndAngle(axis: PySide6.QtGui.QVector3D, angle: float, /) -> PySide6.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxisAndAngle(x: float, y: float, z: float, angle: float, /) -> PySide6.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromEulerAngles(eulerAngles: PySide6.QtGui.QVector3D, /) -> PySide6.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromEulerAngles(pitch: float, yaw: float, roll: float, /) -> PySide6.QtGui.QQuaternion: ...
        def matrix(self, /) -> PySide6.QtGui.QMatrix4x4: ...
        @staticmethod
        def rotateAround(point: PySide6.QtGui.QVector3D, angle: float, axis: PySide6.QtGui.QVector3D, /) -> PySide6.QtGui.QMatrix4x4: ...
        @staticmethod
        def rotateFromAxes(xAxis: PySide6.QtGui.QVector3D, yAxis: PySide6.QtGui.QVector3D, zAxis: PySide6.QtGui.QVector3D, /) -> PySide6.QtGui.QMatrix4x4: ...
        def rotation(self, /) -> PySide6.QtGui.QQuaternion: ...
        def rotationX(self, /) -> float: ...
        def rotationY(self, /) -> float: ...
        def rotationZ(self, /) -> float: ...
        def scale(self, /) -> float: ...
        def scale3D(self, /) -> PySide6.QtGui.QVector3D: ...
        def setMatrix(self, matrix: PySide6.QtGui.QMatrix4x4 | PySide6.QtGui.QTransform, /) -> None: ...
        def setRotation(self, rotation: PySide6.QtGui.QQuaternion, /) -> None: ...
        def setRotationX(self, rotationX: float, /) -> None: ...
        def setRotationY(self, rotationY: float, /) -> None: ...
        def setRotationZ(self, rotationZ: float, /) -> None: ...
        def setScale(self, scale: float, /) -> None: ...
        def setScale3D(self, scale: PySide6.QtGui.QVector3D, /) -> None: ...
        def setTranslation(self, translation: PySide6.QtGui.QVector3D, /) -> None: ...
        def translation(self, /) -> PySide6.QtGui.QVector3D: ...
        def worldMatrix(self, /) -> PySide6.QtGui.QMatrix4x4: ...


    @staticmethod
    def qHash(id: PySide6.Qt3DCore.Qt3DCore.QNodeId, /, seed: int | None= ...) -> int: ...
    @staticmethod
    def qIdForNode(node: PySide6.Qt3DCore.Qt3DCore.QNode, /) -> PySide6.Qt3DCore.Qt3DCore.QNodeId: ...


# eof
