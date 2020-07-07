# QFileDialog 使用
# QFileDialog用于让用户选择文件和目录，可以选择打开或者保存

import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()  # 创建TextEdit控件（编辑框）
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('openfile.jpg'), 'Open', self)  # 创建事件
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')  # 鼠标放置时显示状态栏信息为Open new File
        openFile.triggered.connect(self.showDialog)  # openFile.triggered信号连接到showDialog槽

        menubar = self.menuBar()  # 创建菜单栏
        fileMenu = menubar.addMenu('&File')  # 添加菜单
        fileMenu.addAction(openFile)  # 添加菜单事件

        self.setGeometry(900, 500, 600, 600)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:/Users/zhzj0/Desktop')  # 弹出文件选择对话框，获取选择的文件名
        # 第一个字符串参数为对话框标题，第二个字符串参数为指定对话框的工作目录。默认情况显示所有类型的文件

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)  # 将选择的文件的内容，加载到TextEdit控件


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



