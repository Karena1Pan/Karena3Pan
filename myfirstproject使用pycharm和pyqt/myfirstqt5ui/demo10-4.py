# PyQt5绘图

# QPen（画笔）的使用
# QPen为一个基本的图形对象。用于绘制线条、曲线和轮廓的矩形、椭圆、多边形或其他形状

# 绘制几个不同线条的直线


import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(900, 500, 600, 700)
        self.setWindowTitle('Pen styles')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)  # 绘制直线
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 50, 580, 50)  # 四个参数为绘制直线的两个点的坐标

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 150, 580, 150)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 250, 580, 250)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 350, 580, 350)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 450, 580, 450)

        pen.setStyle(Qt.CustomDashLine)  # 定义画笔风格
        pen.setDashPattern([1, 4, 5, 4])  #setDashPattern()方法参数为一个列表，定义了一种风格，必须是偶数个数字
        # 奇数表示绘制实线，偶数表示留空，数值越大，直线或留白越大。此处为1个像素实线，4个像素留白，5个像素实线，4个像素留白的模式
        qp.setPen(pen)
        qp.drawLine(20, 550, 580, 550)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())











