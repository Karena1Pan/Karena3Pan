# PyQt拖拽

# 简单拖拽

# 本例将设计一个QLineEdit控件和QPushButton，拖拽文本编辑控件放到按钮控件上，改变按钮控件标签。


import sys
from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)

# 创建继承自QPushButton的Button类，以重新实现某些方法使得QPushButton接受拖拽，实现拖拽
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)  # 使该控件接受drop（放下）这一事件

    # 重新实现dragEnterEvent()方法，设置可接受的数据类型
    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    # 重新实现dropEvent()方法，定义drop事件发生时的行为
    def dropEvent(self, e):

        self.setText(e.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)  # QLineEdit内置了对drag(拖动)操作的支持。只需要调用setDragEnabled()方法即可
        edit.move(30, 100)

        button = Button("Button", self)
        button.move(30, 200)

        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(900, 600, 600, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()









