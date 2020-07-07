# 工具栏

# 工具栏能提供快速访问的入口
# 本例创建一个简单工具栏，包含一个按钮，点击可以关闭窗口

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exiticon.jpg'), 'Exit', self)  # 创建事件
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')  # 添加工具栏
        self.toolbar.addAction(exitAction)  # 点击退出窗口

        self.setGeometry(900, 500, 600, 400)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())








