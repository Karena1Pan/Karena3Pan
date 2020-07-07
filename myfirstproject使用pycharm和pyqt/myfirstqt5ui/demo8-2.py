# PyQt5控件-II
# 控件包含：QPixmap（图像处理控件）、QLineEdit（文本框控件）、 QSplitter（拖动调整子控件尺寸控件）,QComboBox（下拉列表控件）


# QLineEdit 使用
# QLineEdit用于输入或编辑单行文本，它具有撤销重做，剪切复制和拖拽功能。

# 本例：展示QLineEdit与一个QLabel，将QLineEdit中输入的文字，显示到QLabel中。


import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)  # 创建QLineEdit

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)
        # textChanged消息连接到onChanged槽函数，当文本框的内容发生改变的时候，会调用onChanged方法

        self.setGeometry(900, 600, 300, 200)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)  # 将QLabel控件的文本设置为输入的内容
        self.lbl.adjustSize()  # 调用adjustSize()方法将QLabel控件的尺寸调整为文本的长度


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

