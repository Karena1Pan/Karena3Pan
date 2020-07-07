import sys

# Qt5的ui文件转换后的py文件需要添加的代码
'''
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 每一个pyqt5应用程序必须创建一个对象。sys.argv参数式一个列表
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

sys.exit(app.exec_())

'''

# Qt5的基本控件位于PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)

    # QWidget部件是pyqt5所有用户界面对象的基类。它为QWidget提供默认构造函数。默认构造函数没有父类。
    w = QWidget()

    # resize()方法调整窗口的大小，这里设置窗口大小为是250px宽150px高
    w.resize(250, 150)

    # move()方法移动窗口在屏幕上的位置，这里设置移动到x = 300，y = 300坐标位置上。
    w.move(300, 300)

    # 设置窗口的标题
    w.setWindowTitle('SimpleDemo')

    # 窗口显示在屏幕上
    w.show()

    # 系统exit()方法确保应用程序干净的退出
    # exec_()方法有下划线，主要因为执行是一个Python关键词。因此用exec_()代替
    sys.exit(app.exec_())
