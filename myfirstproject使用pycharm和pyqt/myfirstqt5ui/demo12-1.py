# PyQt5俄罗斯方块游戏

# 开发一个简易的俄罗斯方块游戏

# 每一个电脑游戏的背后都有一个数学模型。
# 俄罗斯方块游戏设计思想:
# 1、使用QtCore.QBasicTimer()来创建一个游戏循环。
# 2、俄罗斯方块是绘制的，图形是一个方块一个方块移动的（不是像素）
# 3、图形其实是一个简单的数字列表。
# 代码包括四类:
# Tetris，用来存放游戏
# Board，编写游戏逻辑
# Tetrominoe，包含所有俄罗斯方块的名称
# Shape，包含一个俄罗斯方块的代码。


import sys, random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor


'''
类名：Tetris
功能：用来存放游戏
'''
class Tetris(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tboard = Board(self)  # 创建一个面板类的实例
        self.setCentralWidget(self.tboard)  # 设置应用程序的核心部件

        self.statusbar = self.statusBar()  # 创建一个状态栏，用于显示消息
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        # 将自定义信号msg2Statusbar（在Board类中定义），连接到内置方法showMessage(),实现在状态栏显示一条消息。

        self.tboard.start()  # 启动游戏

        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    # center实现将游戏界面放置在屏幕中心位置
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


'''
类名：Board
功能：编写游戏逻辑
'''
class Board(QFrame):
    msg2Statusbar = pyqtSignal(str)  # 创建一个自定义信号。主要用于当想写一个信息或者状态栏显示游戏分数时，msg2Statusbar能发出一个信号

    BoardWidth = 10
    BoardHeight = 22
    Speed = 300  # Board类的变量，分别为游戏整体背景块的大小和游戏速度。
    # BoardWidth游戏块宽。BoardHeight游戏块高。Speed为毫秒，300表示300ms开始一个新的游戏循环

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    # 初始化一些重要变量
    def initBoard(self):

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0  # 消除的行数
        self.board = []  # board为一个0-7的数字列表，表示面板board上的各种形状和所在位置

        self.setFocusPolicy(Qt.StrongFocus)  # 设置获得焦点的方法，即设置为可以通过tab获得焦点，或者通过鼠标点击获得焦点
        self.isStarted = False  # 游戏是否开始的bool标识
        self.isPaused = False  # 游戏是否暂停的bool标识
        self.clearBoard()

    def shapeAt(self, x, y):
        return self.board[(y * Board.BoardWidth) + x]  # shapAt()方法，确定给定形状块的类型

    def setShapeAt(self, x, y, shape):
        self.board[(y * Board.BoardWidth) + x] = shape

    # squareWidth()计算单一方块像素的宽度并返回。主要服务于Board的动态调整大小。
    def squareWidth(self):
        return self.contentsRect().width() // Board.BoardWidth

    # squareHeight()计算单一方块像素的高度并返回。主要服务于Board的动态调整大小。
    def squareHeight(self):
        return self.contentsRect().height() // Board.BoardHeight

    def start(self):

        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.newPiece()
        self.timer.start(Board.Speed, self)

    def pause(self):

        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()  # 如果暂停，则暂停定时器
            self.msg2Statusbar.emit("paused")  # 发送信号到状态栏，emit为发射函数，当所有槽函数返回后，发射函数（emit）才返回

        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))  # 游戏继续进行，发送信号到状态栏，显示已经被消掉的行数（为累计值）

        self.update()

    # 游戏绘制。分为两步：1、绘制所有方块（保存在底部列表中。列表通过shapeAt()方法来添加方块）；2、绘制下降的方块
    def paintEvent(self, event):

        painter = QPainter(self)  # 建立画笔
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        # 绘制：1、绘制所有方块
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)

                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                                    rect.left() + j * self.squareWidth(),
                                    boardTop + i * self.squareHeight(), shape)

        # 绘制：2、绘制下降的方块
        if self.curPiece.shape() != Tetrominoe.NoShape:

            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                                boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                                self.curPiece.shape())

    # keyPressEvent()方法检查按下键
    def keyPressEvent(self, event):

        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)  # super()函数用于调用父类的一个方法，调用父类的keyPressEvent()方法
            return

        key = event.key()

        if key == Qt.Key_P:
            self.pause()
            return

        if self.isPaused:
            return

        # 按左箭头键，试图向左移动一块。调用tryMove函数，因为可能无法移动
        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)

        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)

        # 按向下箭头，旋转方块，。用tryMove函数，因为可能无法旋转
        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)

        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)

        # 按下空格键，下降到底部
        elif key == Qt.Key_Space:
            self.dropDown()

        # 按下D键，加速下降
        elif key == Qt.Key_D:
            self.oneLineDown()

        else:
            super(Board, self).keyPressEvent(event)

    # 检查块是否能放到有效区内。即，尝试移动方块，如果方块的边缘已经接触到面板边缘或者不能移动，则返回false，否则当前块位置更新到新位置。
    def tryMove(self, newPiece, newX, newY):

        for i in range(4):

            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True

    # 计时器事件，当前一个方块降到底部后，创建一个新的方块
    def timerEvent(self, event):

        if event.timerId() == self.timer.timerId():

            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()

        else:
            super(Board, self).timerEvent(event)

    # clearBoard()方法，通过设置Tetrominoe.NoShape清楚面板
    def clearBoard(self):

        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

    def dropDown(self):

        newY = self.curY

        while newY > 0:

            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break

            newY -= 1

        self.pieceDropped()

    def oneLineDown(self):

        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()

    def pieceDropped(self):

        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()

    # 如果块到达底部，调用removeFullLines()方法。检查完成的行，然后删除。接着，对所有的行高高于当前删除行的行，移动一行
    def removeFullLines(self):

        numFullLines = 0
        rowsToRemove = []

        # 检查哪一行已经完整
        for i in range(Board.BoardHeight):

            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        # 删除反的顺序行，否则会出错，会发现有整行没消除
        rowsToRemove.reverse()

        for m in rowsToRemove:

            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()

    # newPiece()方法，创建一个新块
    def newPiece(self):

        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1  # 新块位置位于board顶端中间
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        # 以下代码为判断代码，如果新块不能进入它的初始位置，游戏结束
        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()  # 时钟停止，游戏结束
            self.isStarted = False  # 游戏结束标识
            self.msg2Statusbar.emit("Game over")

    def drawSquare(self, painter, x, y, shape):

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
                         x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
                         y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)



'''
类名：Tetrominoe
功能：包含所有俄罗斯方块的名字
'''
class Tetrominoe(object):
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


'''
类名：Shape
功能：俄罗斯方块的代码
'''
class Shape(object):
    coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )
    # coordsTable元组包含所有可能的俄罗斯方块的坐标值，即一个模板的所有块坐标值

    def __init__(self):

        self.coords = [[0, 0] for i in range(4)]  # 创建一个空列表，保存俄罗斯方块的坐标值
        self.pieceShape = Tetrominoe.NoShape

        self.setShape(Tetrominoe.NoShape)

    def shape(self):
        return self.pieceShape

    def setShape(self, shape):

        table = Shape.coordsTable[shape]

        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape

    def setRandomShape(self):
        self.setShape(random.randint(1, 7))

    def x(self, index):
        return self.coords[index][0]

    def y(self, index):
        return self.coords[index][1]

    def setX(self, index, x):
        self.coords[index][0] = x

    def setY(self, index, y):
        self.coords[index][1] = y

    def minX(self):

        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

    def maxX(self):

        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

    def minY(self):

        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

    def maxY(self):

        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

    # 向左旋转方块
    def rotateLeft(self):

        if self.pieceShape == Tetrominoe.SquareShape:  # 方块本身不能旋转，例如四方块，在放回当前对象本身
            return self

        # 如果方块能旋转，创建一个新方块，设置其坐标值为旋转后的左边，返回这个新方块
        result = Shape()  # 创建新方块
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

    def rotateRight(self):

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result


if __name__ == '__main__':
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())






