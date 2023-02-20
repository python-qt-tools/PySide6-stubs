from PySide6.QtCore import QLine, QLineF, QPoint, QPointF, QRect, QRectF
from PySide6.QtGui import QPainter, QPaintEvent
from PySide6.QtWidgets import QWidget, QApplication

if __name__ == '__main__':
    app = QApplication([])


class MyWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

    def paintEvent(self, e: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.beginNativePainting()
        painter.drawConvexPolygon([QPoint(0, 0), QPoint(1, 1), QPoint(2, 2)])
        painter.drawConvexPolygon([QPointF(0.0, 0.0), QPointF(1.0, 1.0), QPointF(2.0, 2.0)])

        painter.drawPolygon([QPoint(0, 0), QPoint(1, 1), QPoint(2, 2)])
        painter.drawPolygon([QPointF(0.0, 0.0), QPointF(1.0, 1.0), QPointF(2.0, 2.0)])
        painter.drawPolyline([QPoint(0, 0), QPoint(1, 1), QPoint(2, 2)])
        painter.drawPolyline([QPointF(0.0, 0.0), QPointF(1.0, 1.0), QPointF(2.0, 2.0)])
        painter.drawRects([QRectF(0.0, 1.0, 2.0, 3.0), QRectF(1.0, 2.0, 3.0, 4.0), QRectF(2.0, 3.0, 4.0, 5.0),])
        painter.drawRects([QRect(0, 1, 2, 3), QRect(1, 2, 3, 4), QRect(2, 3, 4, 5)])
        painter.drawLines([QLineF(0.0, 1.0, 2.0, 3.0), QLineF(1.0, 2.0, 3.0, 4.0), QLineF(2.0, 3.0, 4.0, 5.0),])
        painter.drawLines([QLine(0, 1, 2, 3), QLine(1, 2, 3, 4), QLine(2, 3, 4, 5)])
        painter.drawPoints([QPoint(0, 0), QPoint(1, 1), QPoint(2, 2)])
        painter.drawPoints([QPointF(0.0, 0.0), QPointF(1.0, 1.0), QPointF(2.0, 2.0)])
        painter.end()
