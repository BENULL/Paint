# coding = utf-8

from src.view.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import (QWidget,QApplication,QMainWindow,QFileDialog)
from PyQt5 import uic
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *


class PaintBoard(QMainWindow,Ui_MainWindow):

    def __init__(self,*args,**kwargs):
        super(PaintBoard, self).__init__(*args,**kwargs)
        self.setupUi(self)
        #uic.loadUi('./view/MainWindow.ui',self)
        self._initParam()
        self._setDefaultBoard()
        self._establishConnections()
        self._initPainter()

    def _initPainter(self):
        painter = QPainter(self.img)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(self.penColor, self.penSize,Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        return painter


    def _initParam(self):
        self.drawing = False
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.penSize = 2
        self.penColor = Qt.black
        self.preColor = Qt.black
        self.backColor = Qt.white
        self.toolBtns = [self.penBtn,self.rectBtn,self.bucketBtn,self.lineBtn,self.ellipseBtn,self.eraseButton]
        self.toolBtnEvents = [self._drawPen,self._drawRect,self._drawBucket,self._drawLine,self._drawEllipse,self._drawErase]

    def _getToolBoxStatus(self):
        pass


    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.penColor = self.preColor
        elif event.button() == Qt.RightButton:
            self.penColor = self.backColor

        self.drawing = True
        self.lastPoint = self._getPosFromGlobal(event.pos())
        self.startPoint = self._getPosFromGlobal(event.pos())

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
            self.endPoint = self._getPosFromGlobal(event.pos())
            self.drawing = False
            self.update()



    def mouseMoveEvent(self, event: QMouseEvent) -> None:

        if event.buttons() and Qt.LeftButton and self.drawing:
            [toolBtnEvent(event) for toolBtn,toolBtnEvent in  zip(self.toolBtns,self.toolBtnEvents) if toolBtn.isChecked()]
            self.update()

    def paintEvent(self, event: QPaintEvent) -> None:

        pix = QPixmap.fromImage(self.img)
        self.board.setPixmap(pix)


    def _getPosFromGlobal(self,pos):
        globalPos = self.mapToGlobal(pos)
        boardPos = self.board.mapFromGlobal(globalPos)
        return boardPos

    def _setDefaultBoard(self):
        self.img = QImage(self.scrollAreaWidgetContents.size(), QImage.Format_RGB32)
        self.img.fill(Qt.white)
        self._refreshBoard()

    def _establishConnections(self):
        self.actionNew.triggered.connect(self._clear)
        self.actionClear.triggered.connect(self._clear)
        self.actionSave.triggered.connect(self._save)
        self.actionOpenImg.triggered.connect(self._openImg)

        self.preColorBtn.clicked.connect(self._choosePreColor)
        self.backColorBtn.clicked.connect(self._chooseBackColor)
        self.penSizeBtn.currentIndexChanged.connect(self._choosePenSize)

        list(map(lambda btn:btn.clicked.connect(self._toolBoxClicked),self.toolBtns))

    def _drawLine(self,event):
        painter = self._initPainter()
        boardPos = self._getPosFromGlobal(event.pos())
        painter.drawLine(self.startPoint, boardPos)
        self.lastPoint = boardPos




    def _drawEllipse(self,event):
        print('drawEllipse')

    def _drawRect(self,event):
        print('drawRect')
        painter = self._initPainter()
        boardPos = self._getPosFromGlobal(event.pos())
        painter.drawRect(QRect(self.startPoint,boardPos))


    def _drawErase(self,event):
        self.penColor = self.backColor
        self._drawPen(event)

    def _drawBucket(self,event):
        pass

    def _drawPen(self,event):
        painter = self._initPainter()
        boardPos = self._getPosFromGlobal(event.pos())
        painter.drawLine(self.lastPoint, boardPos)
        self.lastPoint = boardPos


    def _toolBoxClicked(self):
        self._refreshButtons()
        toolBtn = self.sender()
        toolBtn.setChecked(True)
        print(toolBtn.text())


    def _choosePenSize(self):
        self.penSize = int(self.penSizeBtn.currentText())

    def _choosePreColor(self):
        colorName,self.preColor= self._getColor()
        self.preColorBtn.setStyleSheet("background-color:%s" % colorName)

    def _chooseBackColor(self):
        colorName,self.backColor= self._getColor()
        self.backColorBtn.setStyleSheet("background-color:%s" % colorName)

    def _getColor(self):
        color = QColorDialog.getColor()
        colorName = color.name()
        return colorName,color

    def _refreshButtons(self):
        [btn.setChecked(False) for btn in self.toolBtns]

    def _refreshBoard(self):
        pix = QPixmap.fromImage(self.img)
        # fitpixmap = pix.scaled(self.board.width(), self.board.height(), Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.board.resize(pix.size())
        self.board.setPixmap(pix)
        self.scrollAreaWidgetContents.resize(pix.size())

    def _save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "保存图像", "","PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if filePath == "": return
        self.img.save(filePath)

    def _clear(self):
        self.img.fill(Qt.white)
        self._refreshBoard()

    def _openImg(self):
        fileName, fileType = QFileDialog.getOpenFileName(self,"选取文件","All Files (*)")
        self.img = QImage(fileName)
        self._refreshBoard()





def main():
    app = QApplication(sys.argv)
    application = PaintBoard()
    application.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()