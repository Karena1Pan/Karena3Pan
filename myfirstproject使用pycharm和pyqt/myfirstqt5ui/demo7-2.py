# PyQt5控件
# 常用控件包含：QCheckBox（复选框）,ToggleButton（开关按钮）,QSlider（滑动条）,QProgressBar（进度条）,QCalendarWidget（日历控件）


# Toggle button 使用
# ToggleButton是QPushButton的一种特殊模式。具有状态按下与未按下，通过点击在两者间切换

# 本例：建立多个ToggleButton,改变QWidget的背景色

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QFrame, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)  # 初始颜色设置

        # 创建QPushButton，并通过setCheckable()方法得到一个ToggleButton
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)  # 将clicked信号连接到用户自定义的方法（槽函数）

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 110)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 210)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)  # 建立QFrame
        self.square.setGeometry(150, 15, 550, 300)  # 设置QFrame位置和大小
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(900, 500, 800, 400)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):

        source = self.sender()  # 通过sender()方法获取消息来源

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



