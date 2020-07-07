# PyQt5控件-II
# 控件包含：QPixmap（图像处理控件）、QLineEdit（文本框控件）、 QSplitter（拖动调整子控件尺寸控件）,QComboBox（下拉列表控件）


# QSplitter 使用
# QSplitter，用户通过QSplitter，可拖动子控件的边界来调整子控件的尺寸，可看作是窗口拆分的功能。

# 本例：展示由两个QSplitter组织的QFrame控件。

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                             QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)  # 建立水平控件布局

        topleft = QFrame(self)  # 建立QFrame控件
        topleft.setFrameShape(QFrame.StyledPanel)  # 使用一个风格框架，为了看到QFrame小部件之间的界限

        col = QColor(0, 0, 0)
        topleft.setStyleSheet("QWidget { background-color: %s }" % col.name())  # 为topleft添加背景色

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)  # 创建一个QSplitter小部件，并且添加两个帧，分别为两个QFrame
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)  # 创建一个QSplitter小部件，将一个QSplitter添加到另一个QSplitter控件中
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)  # 将控件添加到控件布局hbox中
        self.setLayout(hbox)  # 应用窗口布局hbox


        self.setGeometry(900, 400, 900, 600)
        self.setWindowTitle('QSplitter')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())












