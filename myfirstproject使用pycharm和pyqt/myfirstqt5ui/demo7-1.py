# PyQt5控件
# 常用控件包含：QCheckBox（复选框）,ToggleButton（开关按钮）,QSlider（滑动条）,QProgressBar（进度条）,QCalendarWidget（日历控件）


# QCheckBox 使用
# QCheckBox具有两个状态，打开和关闭，它是一个带有文本标签（label）的控件

# 本例：建立复选框，切换窗口的标题

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self)  # 建立复选框控件，即构造复选框
        cb.move(20, 20)
        cb.toggle()  # 检查复选框选项
        cb.stateChanged.connect(self.changeTitle)  # 将信号stateChange连接到changTitle槽

        self.setGeometry(900, 500, 400, 300)  # 设置窗口大小
        self.setWindowTitle('QCheckBox')  # 设置窗口标题
        self.show()

    def changeTitle(self, state):  # 复选框的状态经state参数传入changeTitle()方法

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('UnChecked')  # 此处空字符串时，默认为python


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



