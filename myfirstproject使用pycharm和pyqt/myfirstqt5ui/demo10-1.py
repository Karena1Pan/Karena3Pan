# PyQt5绘图
# PyQt5绘画系统能够呈现矢量图形,图像,和大纲font-based文本。也可以在程序中调用系统api自定义绘图控件

# 绘图要在paintEvent()方法中实现。在QPainter对象的begin()与end()方法间编写绘图代码。它会在控件或其他图形设备上进行低级的图形绘制

# 本例在窗体内绘制文本


import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

        self.setGeometry(900, 500, 600, 400)
        self.setWindowTitle('Draw text')
        self.show()

    # paintEvent方法内部实现绘制工作
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()
        '''
        QPainter类负责所有的初级绘制。bengin与end之间为绘图方法，此处实际的绘画被委托给drawText()方法
        '''

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))  # 定义画笔
        qp.setFont(QFont('Decorative', 10))  # 定义字体
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)  # drawText()方法将文本绘制在窗体，显示在中心


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






