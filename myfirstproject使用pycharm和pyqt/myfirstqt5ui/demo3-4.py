# 实例:评论的例子

# 控件可以在网格中跨越多个行和列，本例进行说明

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 创建一个窗口，有三个标签，两个行编辑，一个文本编辑窗口控件，使用QGridLayout完成布局
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')  # 三个标签， title， author， review

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()  # 两个行编辑
        reviewEdit = QTextEdit()  # 一个文本编辑控件

        grid = QGridLayout()  # 创建一个网格布局
        grid.setSpacing(10)  # 设置组件之间的距离

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)  # 添加控件，提供控件的行和列跨

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)  # 添加控件，提供控件的行和列跨

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)  # 添加文本编辑控件，跨度为5行，即从第三行一列位置，横跨到第五行一列

        self.setLayout(grid)

        self.setGeometry(900, 500, 600, 400)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




