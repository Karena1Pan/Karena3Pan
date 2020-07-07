# PyQt5事件和信号

# 所有的GUI程序都靠事件驱动。当调用QApplication的exec_()方法时，会使程序进入主循环。主循环会获取并分发事件

# 在事件模型中，有三个参与者：事件源、事件对象、事件接收者
# 事件源：状态发生变化的对象，它会生成事件
# 事件对象：事件对象封装了事件源中状态的变动
# 事件接收者： 是要通知的对象。
# 事件源对象将事件处理的工作交给事件接收者。

# 实例：信号槽Signals & slots

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)

'''
PyQt5有一个独特的signal&slot(信号槽)机制来处理事件。
信号槽用于对象间的通信。
signal在某一特定事件发生时被触发，slot可以是任何callable对象。当signal触发时会调用与之相连的slot。
'''

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)  # 创建两个控件，一个QtGui.QLCDNumber控件（LCD数字控件），一个QtGui.QSlider控件（滑块控件）

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)  # 垂直布置控件

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)  # 将滚动条的valueChanged信号连接到lcd的display插槽

        self.setGeometry(900, 500, 600, 400)
        self.setWindowTitle('Signal & slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






