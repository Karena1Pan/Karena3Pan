# 创建包含菜单条，工具栏，状态栏的小窗口


import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)  # 创建一个QTextEdit，并把它设置为窗口的布局

        exitAction = QAction(QIcon('exiticon.jpg'), 'Exit', self)  #  创建一个事件，一个特定的图标，一个“退出”的标签
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')  # 创建一个鼠标指针悬停的时候的提示信息，该消息为状态栏消息
        exitAction.triggered.connect(self.close)  # 工具栏创建

        self.statusBar()  # 状态栏创建

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')  # 添加菜单
        fileMenu.addAction(exitAction)  # 添加菜单事件，事件为exitAction

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(900, 500, 600, 400)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







