# PyQt5控件-II
# 控件包含：QPixmap（图像处理控件）、QLineEdit（文本框控件）、 QSplitter（拖动调整子控件尺寸控件）,QComboBox（下拉列表控件）


# QComboBox 使用
# QComboBox，允许用户从下拉列表中进行选择的一种控件。

# 本例：展示一个QComboBox控件，具有多个选项，用户选择某个选项，将选项内容显示在QLabel控件中。


import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Windows 10 System", self)

        combo = QComboBox(self)  # 建立QComboBox控件
        combo.addItem("Anaconda")
        combo.addItem("Cuda")
        combo.addItem("CudNN")
        combo.addItem("Pytorch")
        combo.addItem("PyQt5")  # 为QComboBox控件添加下拉列表项

        combo.move(50, 50)
        self.lbl.move(50, 200)

        combo.activated[str].connect(self.onActivated)
        # 将信号activated连接到onActivated槽函数，当某一个下拉列表项被激活时，发送str消息

        self.setGeometry(900, 600, 600, 400)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())










