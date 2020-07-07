# 菜单栏

# 本例创建一个菜单栏和一个菜单。菜单用于终止应用程序，Ctrl+Q的行动是可访问的快捷方式


import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exiticon.jpg'), '&Exit', self)  # 第一行，含义看注释
        exitAction.setShortcut('Ctrl+Q')  # 第二行，含义看注释
        exitAction.setStatusTip('Exit application')  # 第三行，含义看注释
        exitAction.triggered.connect(qApp.quit)  # 第四行，含义看注释

        '''
        QAction可以操作菜单栏，工具栏，自定义键盘快捷键
        第一行，创建一个事件，一个特定的图标，一个“退出”的标签
        第二行，定义创建事件的快捷键
        第三行，创建一个鼠标指针悬停在菜单项上的时候的提示信息，该消息为状态栏消息
        第四行，当点击菜单的时候，调用qApp.quit，终止应用程序
        '''

        self.statusBar()

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('&File')
        # 添加事件
        fileMenu.addAction(exitAction)

        self.setGeometry(900, 500, 600, 400)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






