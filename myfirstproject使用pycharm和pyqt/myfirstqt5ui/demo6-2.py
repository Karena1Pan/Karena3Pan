# QColorDialog 使用
# QColorDialog显示一个用于选择颜色值的对话框


import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)  # 颜色为黑色

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)  # btn.clicked信号连接到showDialog

        self.frm = QFrame(self)  # 建立一个QFrame
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())  # 设置QFrame的颜色为黑色
        self.frm.setGeometry(200, 100, 200, 200)  # 前两个参数，QFrame的显示位置，后两个参数，QFrame的尺寸

        self.setGeometry(900, 500, 600, 350)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()  # 弹出QColorDialog对话框，获取颜色

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())  # 设置QFrame的颜色为获取的颜色
        # 通过样式表(style sheet)来改变背景色

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







