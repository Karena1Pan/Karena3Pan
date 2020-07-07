# 重新实现事件处理器

# 实例：在PyQt5中通过重新实现事件处理器来处理事件

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(900, 500, 600, 400)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
    '''
    重新实现了keyPressEvent()事件处理器，按下Escape键使程序退出
    '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






