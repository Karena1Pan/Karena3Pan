# QFontDialog 使用
# QFontDialog用于选择字体

import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QLabel, QFontDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)  # 创建button控件，dialog为控件显示的信息
        btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)  # 垂直排列控件

        btn.clicked.connect(self.showDialog)  # button控件的clicked消息连接到showDialog槽

        self.lbl = QLabel('Knowledge only matters', self)  # 创建Label控件
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)  # 垂直排列空间

        self.setGeometry(900, 500, 300, 200)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())





