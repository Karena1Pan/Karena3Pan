# 窗口显示在屏幕中间

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(900, 300)
        self.center()  # 定义窗口显示在中间的方法

        self.setWindowTitle('Center')
        self.show()

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()

        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

'''
# 获得屏幕中心点
cp = QDesktopWidget().availableGeometry().center()

QtGui,QDesktopWidget类提供了用户的桌面信息,包括屏幕大小

'''