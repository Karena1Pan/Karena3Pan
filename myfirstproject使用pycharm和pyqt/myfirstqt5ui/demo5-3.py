# 事件发送者

# 有时候需要知道信号是由哪个控件发出的。对此，PyQt5提供了sender()方法

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)  # 构建控件1

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)  # 构建控件2

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        # 如上两行：两个按钮连接到了同一个插槽，及btn1和btn2都连接到了buttonClicked。即两个按钮为触发同一事件的两个信号源对象

        self.statusBar()

        self.setGeometry(900, 500, 500, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()  # 通过调用sender()方法来判断信号源
        self.statusBar().showMessage(sender.text() + ' was pressed')  # 将sender的信息显示在窗口的状态栏
    '''
    buttonClicked()方法通过调用sender()方法来判断当前按下的是哪个按钮
    '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







