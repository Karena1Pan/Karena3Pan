# PyQt5对话框

# 对话框的主要作用，用于输入数据、修改数据、更改应用程序设置

# QInputDialog 使用
# QInputDialog提供了一种简单方便的对话框从用户得到一个值。输入值可以是字符串,一个数字,或一个项目从一个列表。

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)  # 创建button控件
        self.btn.move(20, 20)  # button控件位置
        self.btn.clicked.connect(self.showDialog)  # 将点击button控件信号连接到showDialog插槽，即显示对话框

        self.le = QLineEdit(self)  # 建立行编辑框控件
        self.le.move(130, 22)

        self.setGeometry(900, 500, 600, 300)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        '''
        该行代码显示输入对话框。第一个字符串为对话框标题，第二个是对话框中的消息。
        对话框返回一个文本和一个bool值。点击ok按钮，bool值是true
        '''
        if ok:
            self.le.setText(str(text))  # 将获取到的text文本（即对话框收到的文本信息）显示到建立的le行编辑框控件


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






