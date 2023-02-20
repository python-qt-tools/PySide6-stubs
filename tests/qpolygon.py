from typing import List, Union, Any

from PySide6.QtGui import QPolygon
from PySide6.QtCore import QPoint


point: QPoint
point_list: List[QPoint]


point = QPoint()
point_list = [point]

polygon = QPolygon()    # type: QPolygon
polygon << point
polygon << point << point
polygon << [point, point]
polygon << (point, point)
polygon << [point, point] << [point, point] << (point, point) << (point, point)

assert type(polygon << point) == QPolygon
poly: QPolygon
poly = polygon << point

assert type(polygon << [point]) == QPolygon
poly = polygon << [point]

point_list = polygon + [point]
assert type(point_list) == list
assert type(point_list[0]) == QPoint


poly_or_pointlist: Union[QPolygon, List[QPoint]]
poly_or_pointlist = [point]
poly_or_pointlist = QPolygon()

# we can no capture the fact the += changes the type of the result
poly_or_pointlist += [point]        # type: ignore[misc]
assert type(poly_or_pointlist) == list
assert type(poly_or_pointlist[0]) == QPoint     # type: ignore[index]

