# PyQt5自定义控件

# 自定义控件需要使用工具库提供的绘图工具，可能有两种方式：在已有的控件上进行拓展或从头开始创建自定义控件

# 本例：绘制Burning widget（烧录控件）


import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen


class Communicate(QObject):
    updateBW = pyqtSignal(int)

# 基于QWidget设计烧录控件
class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setMinimumSize(1, 30)  # 改变控件的最小大小(高度),因为默认值为有点小
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def setValue(self, value):

        self.value = value

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):

        font = QFont('Serif', 7, QFont.Light)  # 使用一个比默认要小的字体
        qp.setFont(font)

        # 采用动态绘制技术，即窗体越大，控件也随之变大；反之亦然。因此需要计算自定义控件载体（即窗体）的大小
        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10.0))

        till = int(((w / 750.0) * self.value))  # till 定义需要绘制的总尺寸
        full = int(((w / 750.0) * 700))  # full定义红色区域的绘制起点
        # 采用浮点数运算的原因是为了在绘制的时候取得较大的精度

        # 绘制分为三个步骤，1、黄色或红色矩形的绘制；2、刻度线的绘制；3、刻度值的绘制
        # 1、绘制黄色或者红色矩形
        if self.value >= 700:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till - full, h)

        else:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        # 2、绘制刻度线
        pen = QPen(QColor(20, 20, 20), 1,
                   Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w - 1, h - 1)

        # 3、绘制刻度值
        j = 0

        for i in range(step, 10 * step, step):
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()  # 使用字体度量来绘制文本，需要知道文本的宽度，以中心为基点垂直线
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i - fw / 2, h / 2, str(self.num[j]))
            j = j + 1


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)  # 创建滑块控件
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1, 750)
        sld.setValue(75)
        sld.setGeometry(30, 20, 500, 30)  # 设置滑块控件的位置及尺寸

        self.c = Communicate()
        self.wid = BurningWidget()  # 创建自定义的BurningWidget控件
        self.c.updateBW[int].connect(self.wid.setValue)

        sld.valueChanged[int].connect(self.changeValue)  # 将滑块valueChanged消息连接到changeValue槽函数，实现相应功能
        hbox = QHBoxLayout()  # 构建水平布局
        hbox.addWidget(self.wid)  # 将自定义控件加载的到水平布局中

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(900, 500, 600, 150)
        self.setWindowTitle('Burning widget')
        self.show()

    def changeValue(self, value):
        self.c.updateBW.emit(value)
        self.wid.repaint()
        # 当滑块发生移动时，changeValue()方法会被调用
        # changeValue中该方法触发了一个自定义的updateBW信号，其参数是当前滚动条的值
        # 该值被用于计算BurningWidget的容量值。然后对自定义控件进行重绘。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


'''
使用了滑块与一个自定义控件。
自定义控件受滑块控制。
控件显示了媒体介质的容量和剩余空间。
该控件的最小值为1,最大值为750。
在值超过700时颜色变为红色。
这通常意味着超刻(即实际写入光盘的容量超过刻录盘片官方标称容量的一种操作)。
BurningWidget控件通过QHBoxLayout与QVBoxLayout置于窗体的底部。
'''




