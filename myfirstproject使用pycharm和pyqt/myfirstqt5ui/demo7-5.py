# PyQt5控件
# 常用控件包含：QCheckBox（复选框）,ToggleButton（开关按钮）,QSlider（滑动条）,QProgressBar（进度条）,QCalendarWidget（日历控件）


# QCalendarWidget 使用
# QCalendarWidget提供了一个基于月份的日历控件，可以用于选择日期。

# 本例：创建一个日历控件和一个标签控件，选择的日期显示在标签控件。


import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication)
from PyQt5.QtCore import QDate


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)  # 创建日历控件
        cal.setGridVisible(True)
        cal.move(75, 80)
        cal.clicked[QDate].connect(self.showDate)  # 如果点击了一个日期，就发出QDate信号，将这个信号连接到用户定义的showDate槽函数

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())  # 用日历控件中选择的日期初始化标签控件，默认为当前系统日期
        self.lbl.move(75, 30)

        self.setGeometry(900, 400, 500, 400)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):  # date用来接收信号
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


