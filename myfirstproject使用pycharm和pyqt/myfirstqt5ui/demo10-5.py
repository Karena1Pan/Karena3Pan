# PyQt5绘图

# QBrush（笔刷）的使用
# QBrush为一个基本的图形对象。用于油漆的背景图形形状,如矩形、椭圆形或多边形。三种不同类型的刷可以:一个预定义的刷,一个梯度,或纹理模式

# 绘制九个不同的矩形

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(900, 500, 580, 620)
        self.setWindowTitle('Brushes')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):
        brush = QBrush(Qt.SolidPattern)  # 创建笔刷对象
        qp.setBrush(brush)  # 将创建的笔刷对象设置给QPainter对象
        qp.drawRect(10, 15, 150, 180)  # 调用painter的drawRect()方法绘制矩形

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(210, 15, 150, 180)

        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(410, 15, 150, 180)

        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 215, 150, 180)

        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(210, 215, 150, 180)

        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(410, 215, 150, 180)

        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 415, 150, 180)

        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(210, 415, 150, 180)

        brush.setStyle(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(410, 415, 150, 180)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())








