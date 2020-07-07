# PyQt5控件
# 常用控件包含：QCheckBox（复选框）,ToggleButton（开关按钮）,QSlider（滑动条）,QProgressBar（进度条）,QCalendarWidget（日历控件）


# QSlider 使用
# QSlider是滑块控件。

# 本例：建立滑块和一个标签，标签用于显示图片，滑块控制图片显示。

import sys
from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)  # 建立水平滑块控件
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(160, 40, 250, 30)
        sld.valueChanged[int].connect(self.changeValue)  # 将valueChanged消息连接到用户定义的changeValue槽函数

        self.label = QLabel(self)  # 建立标签控件
        self.label.setPixmap(QPixmap('audio.jpg'))
        self.label.setGeometry(160, 60, 300, 300)

        self.setGeometry(900, 600, 600, 400)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('audio.jpg'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('audiomin.jpg'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('audiomed.jpg'))
        else:
            self.label.setPixmap(QPixmap('audiomax.jpg'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


