# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtSql, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtSql`

import PySide6.QtSql
import PySide6.QtCore
import PySide6.QtWidgets

import enum
from typing import Any, ClassVar, Dict, List, Optional, Type, Union, overload
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


NoneType = type(None)


class QIntList(object): ...


class QSql(Shiboken.Object):

    class Location(enum.Enum):

        AfterLastRow             : QSql.Location = ... # -0x2
        BeforeFirstRow           : QSql.Location = ... # -0x1


    class NumericalPrecisionPolicy(enum.Enum):

        HighPrecision            : QSql.NumericalPrecisionPolicy = ... # 0x0
        LowPrecisionInt32        : QSql.NumericalPrecisionPolicy = ... # 0x1
        LowPrecisionInt64        : QSql.NumericalPrecisionPolicy = ... # 0x2
        LowPrecisionDouble       : QSql.NumericalPrecisionPolicy = ... # 0x4


    class ParamTypeFlag(enum.Flag):

        In                       : QSql.ParamTypeFlag = ... # 0x1
        Out                      : QSql.ParamTypeFlag = ... # 0x2
        InOut                    : QSql.ParamTypeFlag = ... # 0x3
        Binary                   : QSql.ParamTypeFlag = ... # 0x4


    class TableType(enum.Enum):

        Tables                   : QSql.TableType = ... # 0x1
        SystemTables             : QSql.TableType = ... # 0x2
        Views                    : QSql.TableType = ... # 0x4
        AllTables                : QSql.TableType = ... # 0xff


class QSqlDatabase(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, driver: PySide6.QtSql.QSqlDriver) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtSql.QSqlDatabase) -> None: ...
    @overload
    def __init__(self, type: str) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    @overload
    @staticmethod
    def addDatabase(driver: PySide6.QtSql.QSqlDriver, connectionName: str = ...) -> PySide6.QtSql.QSqlDatabase: ...
    @overload
    @staticmethod
    def addDatabase(type: str, connectionName: str = ...) -> PySide6.QtSql.QSqlDatabase: ...
    @overload
    @staticmethod
    def cloneDatabase(other: PySide6.QtSql.QSqlDatabase, connectionName: str) -> PySide6.QtSql.QSqlDatabase: ...
    @overload
    @staticmethod
    def cloneDatabase(other: str, connectionName: str) -> PySide6.QtSql.QSqlDatabase: ...
    def close(self) -> None: ...
    def commit(self) -> bool: ...
    def connectOptions(self) -> str: ...
    def connectionName(self) -> str: ...
    @staticmethod
    def connectionNames() -> List[str]: ...
    @staticmethod
    def contains(connectionName: str = ...) -> bool: ...
    @staticmethod
    def database(connectionName: str = ..., open: bool = ...) -> PySide6.QtSql.QSqlDatabase: ...
    def databaseName(self) -> str: ...
    def driver(self) -> PySide6.QtSql.QSqlDriver: ...
    def driverName(self) -> str: ...
    @staticmethod
    def drivers() -> List[str]: ...
    def exec(self, query: str = ...) -> PySide6.QtSql.QSqlQuery: ...
    def exec_(self, query: str = ...) -> PySide6.QtSql.QSqlQuery: ...
    def hostName(self) -> str: ...
    @staticmethod
    def isDriverAvailable(name: str) -> bool: ...
    def isOpen(self) -> bool: ...
    def isOpenError(self) -> bool: ...
    def isValid(self) -> bool: ...
    def lastError(self) -> PySide6.QtSql.QSqlError: ...
    def numericalPrecisionPolicy(self) -> PySide6.QtSql.QSql.NumericalPrecisionPolicy: ...
    @overload
    def open(self) -> bool: ...
    @overload
    def open(self, user: str, password: str) -> bool: ...
    def password(self) -> str: ...
    def port(self) -> int: ...
    def primaryIndex(self, tablename: str) -> PySide6.QtSql.QSqlIndex: ...
    def record(self, tablename: str) -> PySide6.QtSql.QSqlRecord: ...
    @staticmethod
    def registerSqlDriver(name: str, creator: PySide6.QtSql.QSqlDriverCreatorBase) -> None: ...
    @staticmethod
    def removeDatabase(connectionName: str) -> None: ...
    def rollback(self) -> bool: ...
    def setConnectOptions(self, options: str = ...) -> None: ...
    def setDatabaseName(self, name: str) -> None: ...
    def setHostName(self, host: str) -> None: ...
    def setNumericalPrecisionPolicy(self, precisionPolicy: PySide6.QtSql.QSql.NumericalPrecisionPolicy) -> None: ...
    def setPassword(self, password: str) -> None: ...
    def setPort(self, p: int) -> None: ...
    def setUserName(self, name: str) -> None: ...
    def tables(self, type: PySide6.QtSql.QSql.TableType = ...) -> List[str]: ...
    def transaction(self) -> bool: ...
    def userName(self) -> str: ...


class QSqlDriver(PySide6.QtCore.QObject):

    notification             : ClassVar[Signal] = ... # notification(QString,QSqlDriver::NotificationSource,QVariant)

    class DbmsType(enum.Enum):

        UnknownDbms              : QSqlDriver.DbmsType = ... # 0x0
        MSSqlServer              : QSqlDriver.DbmsType = ... # 0x1
        MySqlServer              : QSqlDriver.DbmsType = ... # 0x2
        PostgreSQL               : QSqlDriver.DbmsType = ... # 0x3
        Oracle                   : QSqlDriver.DbmsType = ... # 0x4
        Sybase                   : QSqlDriver.DbmsType = ... # 0x5
        SQLite                   : QSqlDriver.DbmsType = ... # 0x6
        Interbase                : QSqlDriver.DbmsType = ... # 0x7
        DB2                      : QSqlDriver.DbmsType = ... # 0x8


    class DriverFeature(enum.Enum):

        Transactions             : QSqlDriver.DriverFeature = ... # 0x0
        QuerySize                : QSqlDriver.DriverFeature = ... # 0x1
        BLOB                     : QSqlDriver.DriverFeature = ... # 0x2
        Unicode                  : QSqlDriver.DriverFeature = ... # 0x3
        PreparedQueries          : QSqlDriver.DriverFeature = ... # 0x4
        NamedPlaceholders        : QSqlDriver.DriverFeature = ... # 0x5
        PositionalPlaceholders   : QSqlDriver.DriverFeature = ... # 0x6
        LastInsertId             : QSqlDriver.DriverFeature = ... # 0x7
        BatchOperations          : QSqlDriver.DriverFeature = ... # 0x8
        SimpleLocking            : QSqlDriver.DriverFeature = ... # 0x9
        LowPrecisionNumbers      : QSqlDriver.DriverFeature = ... # 0xa
        EventNotifications       : QSqlDriver.DriverFeature = ... # 0xb
        FinishQuery              : QSqlDriver.DriverFeature = ... # 0xc
        MultipleResultSets       : QSqlDriver.DriverFeature = ... # 0xd
        CancelQuery              : QSqlDriver.DriverFeature = ... # 0xe


    class IdentifierType(enum.Enum):

        FieldName                : QSqlDriver.IdentifierType = ... # 0x0
        TableName                : QSqlDriver.IdentifierType = ... # 0x1


    class NotificationSource(enum.Enum):

        UnknownSource            : QSqlDriver.NotificationSource = ... # 0x0
        SelfSource               : QSqlDriver.NotificationSource = ... # 0x1
        OtherSource              : QSqlDriver.NotificationSource = ... # 0x2


    class StatementType(enum.Enum):

        WhereStatement           : QSqlDriver.StatementType = ... # 0x0
        SelectStatement          : QSqlDriver.StatementType = ... # 0x1
        UpdateStatement          : QSqlDriver.StatementType = ... # 0x2
        InsertStatement          : QSqlDriver.StatementType = ... # 0x3
        DeleteStatement          : QSqlDriver.StatementType = ... # 0x4


    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def beginTransaction(self) -> bool: ...
    def cancelQuery(self) -> bool: ...
    def close(self) -> None: ...
    def commitTransaction(self) -> bool: ...
    def createResult(self) -> PySide6.QtSql.QSqlResult: ...
    def dbmsType(self) -> PySide6.QtSql.QSqlDriver.DbmsType: ...
    def escapeIdentifier(self, identifier: str, type: PySide6.QtSql.QSqlDriver.IdentifierType) -> str: ...
    def formatValue(self, field: PySide6.QtSql.QSqlField, trimStrings: bool = ...) -> str: ...
    def hasFeature(self, f: PySide6.QtSql.QSqlDriver.DriverFeature) -> bool: ...
    def isIdentifierEscaped(self, identifier: str, type: PySide6.QtSql.QSqlDriver.IdentifierType) -> bool: ...
    def isOpen(self) -> bool: ...
    def isOpenError(self) -> bool: ...
    def lastError(self) -> PySide6.QtSql.QSqlError: ...
    def maximumIdentifierLength(self, type: PySide6.QtSql.QSqlDriver.IdentifierType) -> int: ...
    def numericalPrecisionPolicy(self) -> PySide6.QtSql.QSql.NumericalPrecisionPolicy: ...
    def open(self, db: str, user: str = ..., password: str = ..., host: str = ..., port: int = ..., connOpts: str = ...) -> bool: ...
    def primaryIndex(self, tableName: str) -> PySide6.QtSql.QSqlIndex: ...
    def record(self, tableName: str) -> PySide6.QtSql.QSqlRecord: ...
    def rollbackTransaction(self) -> bool: ...
    def setLastError(self, e: PySide6.QtSql.QSqlError) -> None: ...
    def setNumericalPrecisionPolicy(self, precisionPolicy: PySide6.QtSql.QSql.NumericalPrecisionPolicy) -> None: ...
    def setOpen(self, o: bool) -> None: ...
    def setOpenError(self, e: bool) -> None: ...
    def sqlStatement(self, type: PySide6.QtSql.QSqlDriver.StatementType, tableName: str, rec: PySide6.QtSql.QSqlRecord, preparedStatement: bool) -> str: ...
    def stripDelimiters(self, identifier: str, type: PySide6.QtSql.QSqlDriver.IdentifierType) -> str: ...
    def subscribeToNotification(self, name: str) -> bool: ...
    def subscribedToNotifications(self) -> List[str]: ...
    def tables(self, tableType: PySide6.QtSql.QSql.TableType) -> List[str]: ...
    def unsubscribeFromNotification(self, name: str) -> bool: ...


class QSqlDriverCreatorBase(Shiboken.Object):

    def __init__(self) -> None: ...

    def createObject(self) -> PySide6.QtSql.QSqlDriver: ...


class QSqlError(Shiboken.Object):

    class ErrorType(enum.Enum):

        NoError                  : QSqlError.ErrorType = ... # 0x0
        ConnectionError          : QSqlError.ErrorType = ... # 0x1
        StatementError           : QSqlError.ErrorType = ... # 0x2
        TransactionError         : QSqlError.ErrorType = ... # 0x3
        UnknownError             : QSqlError.ErrorType = ... # 0x4


    @overload
    def __init__(self, driverText: str = ..., databaseText: str = ..., type: PySide6.QtSql.QSqlError.ErrorType = ..., errorCode: str = ...) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtSql.QSqlError) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def databaseText(self) -> str: ...
    def driverText(self) -> str: ...
    def isValid(self) -> bool: ...
    def nativeErrorCode(self) -> str: ...
    def swap(self, other: PySide6.QtSql.QSqlError) -> None: ...
    def text(self) -> str: ...
    def type(self) -> PySide6.QtSql.QSqlError.ErrorType: ...


class QSqlField(Shiboken.Object):

    class RequiredStatus(enum.Enum):

        Unknown                  : QSqlField.RequiredStatus = ... # -0x1
        Optional                 : QSqlField.RequiredStatus = ... # 0x0
        Required                 : QSqlField.RequiredStatus = ... # 0x1


    @overload
    def __init__(self, fieldName: str = ..., type: Union[PySide6.QtCore.QMetaType, PySide6.QtCore.QMetaType.Type] = ..., tableName: str = ...) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtSql.QSqlField) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def clear(self) -> None: ...
    def defaultValue(self) -> Any: ...
    def isAutoValue(self) -> bool: ...
    def isGenerated(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isReadOnly(self) -> bool: ...
    def isValid(self) -> bool: ...
    def length(self) -> int: ...
    def metaType(self) -> PySide6.QtCore.QMetaType: ...
    def name(self) -> str: ...
    def precision(self) -> int: ...
    def requiredStatus(self) -> PySide6.QtSql.QSqlField.RequiredStatus: ...
    def setAutoValue(self, autoVal: bool) -> None: ...
    def setDefaultValue(self, value: Any) -> None: ...
    def setGenerated(self, gen: bool) -> None: ...
    def setLength(self, fieldLength: int) -> None: ...
    def setMetaType(self, type: Union[PySide6.QtCore.QMetaType, PySide6.QtCore.QMetaType.Type]) -> None: ...
    def setName(self, name: str) -> None: ...
    def setPrecision(self, precision: int) -> None: ...
    def setReadOnly(self, readOnly: bool) -> None: ...
    def setRequired(self, required: bool) -> None: ...
    def setRequiredStatus(self, status: PySide6.QtSql.QSqlField.RequiredStatus) -> None: ...
    def setSqlType(self, type: int) -> None: ...
    def setTableName(self, tableName: str) -> None: ...
    def setValue(self, value: Any) -> None: ...
    def tableName(self) -> str: ...
    def typeID(self) -> int: ...
    def value(self) -> Any: ...


class QSqlIndex(PySide6.QtSql.QSqlRecord):

    @overload
    def __init__(self, cursorName: str = ..., name: str = ...) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtSql.QSqlIndex) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    @overload
    def append(self, field: PySide6.QtSql.QSqlField) -> None: ...
    @overload
    def append(self, field: PySide6.QtSql.QSqlField, desc: bool) -> None: ...
    def cursorName(self) -> str: ...
    def isDescending(self, i: int) -> bool: ...
    def name(self) -> str: ...
    def setCursorName(self, cursorName: str) -> None: ...
    def setDescending(self, i: int, desc: bool) -> None: ...
    def setName(self, name: str) -> None: ...


class QSqlQuery(Shiboken.Object):

    class BatchExecutionMode(enum.Enum):

        ValuesAsRows             : QSqlQuery.BatchExecutionMode = ... # 0x0
        ValuesAsColumns          : QSqlQuery.BatchExecutionMode = ... # 0x1


    @overload
    def __init__(self, db: PySide6.QtSql.QSqlDatabase) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtSql.QSqlQuery) -> None: ...
    @overload
    def __init__(self, query: str = ..., db: PySide6.QtSql.QSqlDatabase = ...) -> None: ...
    @overload
    def __init__(self, r: PySide6.QtSql.QSqlResult) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def addBindValue(self, val: Any, type: PySide6.QtSql.QSql.ParamTypeFlag = ...) -> None: ...
    def at(self) -> int: ...
    @overload
    def bindValue(self, placeholder: str, val: Any, type: PySide6.QtSql.QSql.ParamTypeFlag = ...) -> None: ...
    @overload
    def bindValue(self, pos: int, val: Any, type: PySide6.QtSql.QSql.ParamTypeFlag = ...) -> None: ...
    @overload
    def boundValue(self, placeholder: str) -> Any: ...
    @overload
    def boundValue(self, pos: int) -> Any: ...
    def boundValues(self) -> List[Any]: ...
    def clear(self) -> None: ...
    def driver(self) -> PySide6.QtSql.QSqlDriver: ...
    @overload
    def exec(self) -> bool: ...
    @overload
    def exec(self, query: str) -> bool: ...
    def execBatch(self, mode: PySide6.QtSql.QSqlQuery.BatchExecutionMode = ...) -> bool: ...
    @overload
    def exec_(self) -> bool: ...
    @overload
    def exec_(self, arg__1: str) -> bool: ...
    def executedQuery(self) -> str: ...
    def finish(self) -> None: ...
    def first(self) -> bool: ...
    def isActive(self) -> bool: ...
    def isForwardOnly(self) -> bool: ...
    @overload
    def isNull(self, field: int) -> bool: ...
    @overload
    def isNull(self, name: str) -> bool: ...
    def isSelect(self) -> bool: ...
    def isValid(self) -> bool: ...
    def last(self) -> bool: ...
    def lastError(self) -> PySide6.QtSql.QSqlError: ...
    def lastInsertId(self) -> Any: ...
    def lastQuery(self) -> str: ...
    def next(self) -> bool: ...
    def nextResult(self) -> bool: ...
    def numRowsAffected(self) -> int: ...
    def numericalPrecisionPolicy(self) -> PySide6.QtSql.QSql.NumericalPrecisionPolicy: ...
    def prepare(self, query: str) -> bool: ...
    def previous(self) -> bool: ...
    def record(self) -> PySide6.QtSql.QSqlRecord: ...
    def result(self) -> PySide6.QtSql.QSqlResult: ...
    def seek(self, i: int, relative: bool = ...) -> bool: ...
    def setForwardOnly(self, forward: bool) -> None: ...
    def setNumericalPrecisionPolicy(self, precisionPolicy: PySide6.QtSql.QSql.NumericalPrecisionPolicy) -> None: ...
    def size(self) -> int: ...
    def swap(self, other: PySide6.QtSql.QSqlQuery) -> None: ...
    @overload
    def value(self, i: int) -> Any: ...
    @overload
    def value(self, name: str) -> Any: ...


class QSqlQueryModel(PySide6.QtCore.QAbstractTableModel):

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def beginInsertColumns(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], first: int, last: int) -> None: ...
    def beginInsertRows(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], first: int, last: int) -> None: ...
    def beginRemoveColumns(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], first: int, last: int) -> None: ...
    def beginRemoveRows(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], first: int, last: int) -> None: ...
    def beginResetModel(self) -> None: ...
    def canFetchMore(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> bool: ...
    def clear(self) -> None: ...
    def columnCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int: ...
    def data(self, item: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role: int = ...) -> Any: ...
    def endInsertColumns(self) -> None: ...
    def endInsertRows(self) -> None: ...
    def endRemoveColumns(self) -> None: ...
    def endRemoveRows(self) -> None: ...
    def endResetModel(self) -> None: ...
    def fetchMore(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> None: ...
    def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = ...) -> Any: ...
    def indexInQuery(self, item: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> PySide6.QtCore.QModelIndex: ...
    def insertColumns(self, column: int, count: int, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> bool: ...
    def lastError(self) -> PySide6.QtSql.QSqlError: ...
    def query(self) -> PySide6.QtSql.QSqlQuery: ...
    def queryChange(self) -> None: ...
    @overload
    def record(self) -> PySide6.QtSql.QSqlRecord: ...
    @overload
    def record(self, row: int) -> PySide6.QtSql.QSqlRecord: ...
    def removeColumns(self, column: int, count: int, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> bool: ...
    def roleNames(self) -> Dict[int, PySide6.QtCore.QByteArray]: ...
    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int: ...
    def setHeaderData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, value: Any, role: int = ...) -> bool: ...
    def setLastError(self, error: PySide6.QtSql.QSqlError) -> None: ...
    @overload
    def setQuery(self, query: PySide6.QtSql.QSqlQuery) -> None: ...
    @overload
    def setQuery(self, query: str, db: PySide6.QtSql.QSqlDatabase = ...) -> None: ...


class QSqlRecord(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtSql.QSqlRecord) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def append(self, field: PySide6.QtSql.QSqlField) -> None: ...
    def clear(self) -> None: ...
    def clearValues(self) -> None: ...
    def contains(self, name: str) -> bool: ...
    def count(self) -> int: ...
    @overload
    def field(self, i: int) -> PySide6.QtSql.QSqlField: ...
    @overload
    def field(self, name: str) -> PySide6.QtSql.QSqlField: ...
    def fieldName(self, i: int) -> str: ...
    def indexOf(self, name: str) -> int: ...
    def insert(self, pos: int, field: PySide6.QtSql.QSqlField) -> None: ...
    def isEmpty(self) -> bool: ...
    @overload
    def isGenerated(self, i: int) -> bool: ...
    @overload
    def isGenerated(self, name: str) -> bool: ...
    @overload
    def isNull(self, i: int) -> bool: ...
    @overload
    def isNull(self, name: str) -> bool: ...
    def keyValues(self, keyFields: PySide6.QtSql.QSqlRecord) -> PySide6.QtSql.QSqlRecord: ...
    def remove(self, pos: int) -> None: ...
    def replace(self, pos: int, field: PySide6.QtSql.QSqlField) -> None: ...
    @overload
    def setGenerated(self, i: int, generated: bool) -> None: ...
    @overload
    def setGenerated(self, name: str, generated: bool) -> None: ...
    @overload
    def setNull(self, i: int) -> None: ...
    @overload
    def setNull(self, name: str) -> None: ...
    @overload
    def setValue(self, i: int, val: Any) -> None: ...
    @overload
    def setValue(self, name: str, val: Any) -> None: ...
    @overload
    def value(self, i: int) -> Any: ...
    @overload
    def value(self, name: str) -> Any: ...


class QSqlRelation(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QSqlRelation: PySide6.QtSql.QSqlRelation) -> None: ...
    @overload
    def __init__(self, aTableName: str, indexCol: str, displayCol: str) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def displayColumn(self) -> str: ...
    def indexColumn(self) -> str: ...
    def isValid(self) -> bool: ...
    def swap(self, other: PySide6.QtSql.QSqlRelation) -> None: ...
    def tableName(self) -> str: ...


class QSqlRelationalDelegate(PySide6.QtWidgets.QStyledItemDelegate):

    def __init__(self, aParent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def createEditor(self, aParent: PySide6.QtWidgets.QWidget, option: PySide6.QtWidgets.QStyleOptionViewItem, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> PySide6.QtWidgets.QWidget: ...
    def setEditorData(self, editor: PySide6.QtWidgets.QWidget, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> None: ...
    def setModelData(self, editor: PySide6.QtWidgets.QWidget, model: PySide6.QtCore.QAbstractItemModel, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> None: ...


class QSqlRelationalTableModel(PySide6.QtSql.QSqlTableModel):

    class JoinMode(enum.Enum):

        InnerJoin                : QSqlRelationalTableModel.JoinMode = ... # 0x0
        LeftJoin                 : QSqlRelationalTableModel.JoinMode = ... # 0x1


    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ..., db: PySide6.QtSql.QSqlDatabase = ...) -> None: ...

    def clear(self) -> None: ...
    def data(self, item: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role: int = ...) -> Any: ...
    def insertRowIntoTable(self, values: PySide6.QtSql.QSqlRecord) -> bool: ...
    def orderByClause(self) -> str: ...
    def relation(self, column: int) -> PySide6.QtSql.QSqlRelation: ...
    def relationModel(self, column: int) -> PySide6.QtSql.QSqlTableModel: ...
    def removeColumns(self, column: int, count: int, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> bool: ...
    def revertRow(self, row: int) -> None: ...
    def select(self) -> bool: ...
    def selectStatement(self) -> str: ...
    def setData(self, item: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], value: Any, role: int = ...) -> bool: ...
    def setJoinMode(self, joinMode: PySide6.QtSql.QSqlRelationalTableModel.JoinMode) -> None: ...
    def setRelation(self, column: int, relation: PySide6.QtSql.QSqlRelation) -> None: ...
    def setTable(self, tableName: str) -> None: ...
    def updateRowInTable(self, row: int, values: PySide6.QtSql.QSqlRecord) -> bool: ...


class QSqlResult(Shiboken.Object):

    class BindingSyntax(enum.Enum):

        PositionalBinding        : QSqlResult.BindingSyntax = ... # 0x0
        NamedBinding             : QSqlResult.BindingSyntax = ... # 0x1


    class VirtualHookOperation(Shiboken.Enum): ...


    def __init__(self, db: PySide6.QtSql.QSqlDriver) -> None: ...

    def addBindValue(self, val: Any, type: PySide6.QtSql.QSql.ParamTypeFlag) -> None: ...
    def at(self) -> int: ...
    @overload
    def bindValue(self, placeholder: str, val: Any, type: PySide6.QtSql.QSql.ParamTypeFlag) -> None: ...
    @overload
    def bindValue(self, pos: int, val: Any, type: PySide6.QtSql.QSql.ParamTypeFlag) -> None: ...
    @overload
    def bindValueType(self, placeholder: str) -> PySide6.QtSql.QSql.ParamTypeFlag: ...
    @overload
    def bindValueType(self, pos: int) -> PySide6.QtSql.QSql.ParamTypeFlag: ...
    def bindingSyntax(self) -> PySide6.QtSql.QSqlResult.BindingSyntax: ...
    @overload
    def boundValue(self, placeholder: str) -> Any: ...
    @overload
    def boundValue(self, pos: int) -> Any: ...
    def boundValueCount(self) -> int: ...
    def boundValueName(self, pos: int) -> str: ...
    def boundValues(self) -> List[Any]: ...
    def clear(self) -> None: ...
    def data(self, i: int) -> Any: ...
    def detachFromResultSet(self) -> None: ...
    def driver(self) -> PySide6.QtSql.QSqlDriver: ...
    def exec(self) -> bool: ...
    def execBatch(self, arrayBind: bool = ...) -> bool: ...
    def exec_(self) -> bool: ...
    def executedQuery(self) -> str: ...
    def fetch(self, i: int) -> bool: ...
    def fetchFirst(self) -> bool: ...
    def fetchLast(self) -> bool: ...
    def fetchNext(self) -> bool: ...
    def fetchPrevious(self) -> bool: ...
    def handle(self) -> Any: ...
    def hasOutValues(self) -> bool: ...
    def isActive(self) -> bool: ...
    def isForwardOnly(self) -> bool: ...
    def isNull(self, i: int) -> bool: ...
    def isSelect(self) -> bool: ...
    def isValid(self) -> bool: ...
    def lastError(self) -> PySide6.QtSql.QSqlError: ...
    def lastInsertId(self) -> Any: ...
    def lastQuery(self) -> str: ...
    def nextResult(self) -> bool: ...
    def numRowsAffected(self) -> int: ...
    def numericalPrecisionPolicy(self) -> PySide6.QtSql.QSql.NumericalPrecisionPolicy: ...
    def prepare(self, query: str) -> bool: ...
    def record(self) -> PySide6.QtSql.QSqlRecord: ...
    def reset(self, sqlquery: str) -> bool: ...
    def resetBindCount(self) -> None: ...
    def savePrepare(self, sqlquery: str) -> bool: ...
    def setActive(self, a: bool) -> None: ...
    def setAt(self, at: int) -> None: ...
    def setForwardOnly(self, forward: bool) -> None: ...
    def setLastError(self, e: PySide6.QtSql.QSqlError) -> None: ...
    def setNumericalPrecisionPolicy(self, policy: PySide6.QtSql.QSql.NumericalPrecisionPolicy) -> None: ...
    def setQuery(self, query: str) -> None: ...
    def setSelect(self, s: bool) -> None: ...
    def size(self) -> int: ...


class QSqlTableModel(PySide6.QtSql.QSqlQueryModel):

    beforeDelete             : ClassVar[Signal] = ... # beforeDelete(int)
    beforeInsert             : ClassVar[Signal] = ... # beforeInsert(QSqlRecord&)
    beforeUpdate             : ClassVar[Signal] = ... # beforeUpdate(int,QSqlRecord&)
    primeInsert              : ClassVar[Signal] = ... # primeInsert(int,QSqlRecord&)

    class EditStrategy(enum.Enum):

        OnFieldChange            : QSqlTableModel.EditStrategy = ... # 0x0
        OnRowChange              : QSqlTableModel.EditStrategy = ... # 0x1
        OnManualSubmit           : QSqlTableModel.EditStrategy = ... # 0x2


    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ..., db: PySide6.QtSql.QSqlDatabase = ...) -> None: ...

    def clear(self) -> None: ...
    def clearItemData(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> bool: ...
    def data(self, idx: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role: int = ...) -> Any: ...
    def database(self) -> PySide6.QtSql.QSqlDatabase: ...
    def deleteRowFromTable(self, row: int) -> bool: ...
    def editStrategy(self) -> PySide6.QtSql.QSqlTableModel.EditStrategy: ...
    def fieldIndex(self, fieldName: str) -> int: ...
    def filter(self) -> str: ...
    def flags(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> PySide6.QtCore.Qt.ItemFlag: ...
    def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = ...) -> Any: ...
    def indexInQuery(self, item: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> PySide6.QtCore.QModelIndex: ...
    def insertRecord(self, row: int, record: PySide6.QtSql.QSqlRecord) -> bool: ...
    def insertRowIntoTable(self, values: PySide6.QtSql.QSqlRecord) -> bool: ...
    def insertRows(self, row: int, count: int, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> bool: ...
    @overload
    def isDirty(self) -> bool: ...
    @overload
    def isDirty(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> bool: ...
    def orderByClause(self) -> str: ...
    def primaryKey(self) -> PySide6.QtSql.QSqlIndex: ...
    def primaryValues(self, row: int) -> PySide6.QtSql.QSqlRecord: ...
    @overload
    def record(self) -> PySide6.QtSql.QSqlRecord: ...
    @overload
    def record(self, row: int) -> PySide6.QtSql.QSqlRecord: ...
    def removeColumns(self, column: int, count: int, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> bool: ...
    def removeRows(self, row: int, count: int, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> bool: ...
    def revert(self) -> None: ...
    def revertAll(self) -> None: ...
    def revertRow(self, row: int) -> None: ...
    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int: ...
    def select(self) -> bool: ...
    def selectRow(self, row: int) -> bool: ...
    def selectStatement(self) -> str: ...
    def setData(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], value: Any, role: int = ...) -> bool: ...
    def setEditStrategy(self, strategy: PySide6.QtSql.QSqlTableModel.EditStrategy) -> None: ...
    def setFilter(self, filter: str) -> None: ...
    def setPrimaryKey(self, key: PySide6.QtSql.QSqlIndex) -> None: ...
    def setRecord(self, row: int, record: PySide6.QtSql.QSqlRecord) -> bool: ...
    def setSort(self, column: int, order: PySide6.QtCore.Qt.SortOrder) -> None: ...
    def setTable(self, tableName: str) -> None: ...
    def sort(self, column: int, order: PySide6.QtCore.Qt.SortOrder) -> None: ...
    def submit(self) -> bool: ...
    def submitAll(self) -> bool: ...
    def tableName(self) -> str: ...
    def updateRowInTable(self, row: int, values: PySide6.QtSql.QSqlRecord) -> bool: ...


# eof
