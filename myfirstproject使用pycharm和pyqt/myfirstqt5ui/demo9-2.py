# PyQt拖拽

# 拖放一个按钮

# 本例将设计按钮拖放，设计窗口显示QPushButton。如果鼠标左键单击按钮，在控制台输出press消息。右击进行拖动。


import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

    # 重实现mouseMoveEvent方法，该方法是拖拽产生的方法
    def mouseMoveEvent(self, e):

        # 设计只有鼠标右击时才进行拖拽操作
        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)  # QDrag提供了对基于MIME的拖放数据传输的支持
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)  # Drag对象的exec_()方法用于启动拖放操作

    # mousePressEvent()方法
    def mousePressEvent(self, e):

        QPushButton.mousePressEvent(self, e)  # 此处需要调用父按钮的mousePressEvent()方法，否则会看不到按钮的按下效果

        if e.button() == Qt.LeftButton:
            print('press')


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(900, 600, 600, 400)

    def dragEnterEvent(self, e):
        e.accept()

    # 释放右键后调用dropEvent()方法，即找出鼠标指针的当前位置，并将按钮移动过去
    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()








