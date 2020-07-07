# PyQt5控件-II
# 控件包含：QPixmap（图像处理控件）、QLineEdit（文本框控件）、 QSplitter（拖动调整子控件尺寸控件）,QComboBox（下拉列表控件）


# QPixmap 使用
# QPixmap用于处理图像的控件，能够优化的在屏幕上显示图像。

# 本例：使用QPixmap窗口显示一个图像。

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)  # 建立水平控件布局
        pixmap = QPixmap("basiguangnian.jpg")  # 创建QPixmap控件

        lbl = QLabel(self)  # 创建标签控件
        lbl.setPixmap(pixmap)  # 将pixmap放到Qlabel（标签）控件中，将标签控件用于显示图像

        hbox.addWidget(lbl)  # 将标签控件添加到控件布局中
        self.setLayout(hbox)  # 应用程序窗口布局hbox

        self.move(900, 400)
        self.setWindowTitle('BaSiGuangNian')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



