# 表格布局 QGridLayout

# 表格布局将空间划分为行和列，使用QGridLayout类创建一个网格布局

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)
        # 创建QGridLayout实例，并设置应用程序窗口的布局

        # 按钮的标签
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # 创建一个网格中的位置列表，五行四列
        positions = [(i, j) for i in range(5) for j in range(4)]

        # 创建按钮并使用addWidget()方法添加到布局中
        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(800, 500)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())





