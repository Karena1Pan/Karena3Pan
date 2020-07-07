# pyQt5布局管理
# 布局有两种方式，绝对定位和布局类

# 本例：绝对定位
# 绝对定位的含义：程序指定每个空间的位置和大小

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 空间布局，位置设置
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        # 窗口设置
        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

'''
# 绝对定位的限制：
# 如果我们调整窗口，控件的大小和位置不会改变
# 在各种平台上应用程序看起来会不一样
# 如果改变字体，我们的应用程序的布局就会改变
# 如果我们决定改变我们的布局,我们必须完全重做我们的布局
'''

