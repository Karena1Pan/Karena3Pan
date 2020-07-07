# 发出信号

# 通过QObject创建的对象可以发出信号。本例为如何发出自定义的信号。

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()  # 创建一个名为closeApp的信号
# 信号closeApp是Communicate的类属性，它由pyqtSignal()创建


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.c = Communicate()  # 创建closeApp的信号
        self.c.closeApp.connect(self.close)  # closeApp的信号连接到QMainWindow的close()插槽

        self.setGeometry(900, 500, 600, 400)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()  # 定义鼠标触发，当窗体上点击鼠标时会触发closeApp信号，使程序退出


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






