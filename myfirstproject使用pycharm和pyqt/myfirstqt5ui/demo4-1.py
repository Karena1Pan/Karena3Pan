# PyQt5的菜单和工具栏

# QMainWindow 类提供了一个主要的应用程序窗口。用它可以给应用程序添加状态栏,工具栏和菜单栏

# 本例为状态栏：状态栏用于显示状态信息


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        # QMainWindow类第一次调用statusBar()创建一个状态栏，后续调用返回状态栏对象，showMessage()在状态栏上显示一条消息

        self.setGeometry(900, 500, 600, 400)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






