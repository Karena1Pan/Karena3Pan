# PyQt5绘图

# 颜色

# 绘制三个颜色不同的矩形


import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(900, 500, 600, 400)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)  # 绘制矩形
        qp.end()

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')  # 定义一个使用16进制符号的颜色
        qp.setPen(col)

        # 设置画笔，绘制矩形
        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(10, 15, 150, 300)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(200, 15, 150, 300)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(390, 15, 150, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


