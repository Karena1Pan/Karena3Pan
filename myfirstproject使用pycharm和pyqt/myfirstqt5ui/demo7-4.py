# PyQt5控件
# 常用控件包含：QCheckBox（复选框）,ToggleButton（开关按钮）,QSlider（滑动条）,QProgressBar（进度条）,QCalendarWidget（日历控件）


# QProgressBar 使用
# QProgressBar显示任务进展，提供水平或垂直PyQt5工具包的进度条。进度条最大值和最小值可设置，默认为0-99

# 本例：显示水平进度条和按钮，用户通过点击按钮开始和停止进度条。


import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar,
                             QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)  # QProgressBar的构造方法，创建进度条
        self.pbar.setGeometry(30, 40, 550, 25)  # 进度条位置参数和尺寸参数

        self.btn = QPushButton('Start', self)  # 建立按钮控件
        self.btn.move(250, 80)  # 设定按钮位置
        self.btn.clicked.connect(self.doAction)  # 将按钮的clicked信号连接到用户定义的doAction槽函数， 本例中该槽函数中启动定时器

        self.timer = QBasicTimer()  # 用QtCore的QBasicTimer()方法，定义一个定时器，使用定时器激活QProgressBar
        self.step = 0

        self.setGeometry(900, 600, 600, 200)
        self.setWindowTitle('QProgressBar')
        self.show()

    # 每个QObject及其子类都有一个timerEvent()事件处理器。我们要重新实现这个事件处理器来响应定时器事件。
    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(50, self)  # 调用start()方法启动一个计时器。start()方法有两个参数:超时（可看成定时器时间间隔）和对象将接收的事件
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



