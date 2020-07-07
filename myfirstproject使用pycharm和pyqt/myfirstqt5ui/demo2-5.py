# 消息框

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 注意：
'''
reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
关闭窗口时，触发QCloseEvent，因此需要填写closeEvent()事件处理程序
本程序显示一个消息框,两个按钮:“是”和“不是”。
第一个字符串出现在titlebar，可看成消息框的标题
第二个字符串是消息对话框中显示的文本
第三个参数指定按钮的组合出现在对话框中
最后一个参数是默认按钮，这个是默认的按钮焦点
'''

'''
if reply == QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()

处理返回值，yes按钮，关闭小部件终止应用程序（即关闭本例中的窗口）
no按钮，忽略关闭事件
'''