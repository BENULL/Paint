# coding = utf-8

from src.view.MainWindow import Ui_MainWindow
from src.BaseAdjustDialog import BaseAdjustDialog
from PyQt5.QtWidgets import (QWidget,QApplication,QMainWindow,QFileDialog)
from PyQt5 import uic
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from src.util import ImageUtil
from functools import partial


class PaintBoard(QMainWindow,Ui_MainWindow):

    def __init__(self,*args,**kwargs):
        super(PaintBoard, self).__init__(*args,**kwargs)
        self.setupUi(self)
        #uic.loadUi('./view/MainWindow.ui',self)
        self._initParam()
        self._initDefaultBoard()
        self._establishConnections()
        self._initPainter()

    def _initPainter(self,board = None):
        painter = QPainter(board or self.img)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(self.penColor, self.penSize,Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        return painter


    def _initParam(self):
        self.drawing = False
        self.adjusting = False
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.penSize = 2
        self.penColor = Qt.black
        self.preColor = Qt.black
        self.backColor = Qt.white
        self.toolBtns = [self.penBtn,self.bucketBtn,self.rectBtn,self.lineBtn,self.ellipseBtn,self.eraseButton]
        self.toolBtnEvents = [self._drawPen,self._drawBucket,self._drawRect,self._drawLine,self._drawEllipse,self._drawErase]

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
            [toolBtnEvent(event) for toolBtn,toolBtnEvent in  zip(self.toolBtns,self.toolBtnEvents) if toolBtn.isChecked()]

    def mouseMoveEvent(self, event: QMouseEvent) -> None:

        if event.buttons() and Qt.LeftButton and self.drawing:
            [toolBtnEvent(event) for toolBtn,toolBtnEvent in  zip(self.toolBtns,self.toolBtnEvents) if toolBtn.isChecked()]
            self.update()

    def paintEvent(self, event: QPaintEvent) -> None:
        if self.drawing and True in [btn.isChecked() for btn in self.toolBtns[2:5]] or self.adjusting:
            self.board.setPixmap(QPixmap.fromImage(self.bufferImg))
        else:
            pix = QPixmap.fromImage(self.img)
            self.board.setPixmap(pix)


    def _getPosFromGlobal(self,pos):
        globalPos = self.mapToGlobal(pos)
        boardPos = self.board.mapFromGlobal(globalPos)
        return boardPos

    def _initDefaultBoard(self):
        self.img = QImage(self.scrollAreaWidgetContents.size(), QImage.Format_RGB32)
        self.img.fill(Qt.white)
        self.bufferImg = self.img.copy()
        self.oriImg = self.img.copy()
        self._refreshBoard()

    def _establishConnections(self):
        self.actionNew.triggered.connect(self._clear)
        self.actionClear.triggered.connect(self._clear)
        self.actionSave.triggered.connect(self._save)
        self.actionOpenImg.triggered.connect(self._openImg)
        self.actionClearDraw.triggered.connect(self._clearDraw)
        self.actionClockWise.triggered.connect(partial(self._wiseAction,'clock'))
        self.actionAntiClockWise.triggered.connect(partial(self._wiseAction,'antiClock'))
        self.actionVerFilp.triggered.connect(partial(self._wiseAction,'verFilp'))
        self.actionHorFilp.triggered.connect(partial(self._wiseAction,'horFilp'))
        self.preColorBtn.clicked.connect(self._choosePreColor)
        self.backColorBtn.clicked.connect(self._chooseBackColor)
        self.penSizeBtn.currentIndexChanged.connect(self._choosePenSize)
        self.baseAdjustBtn.clicked.connect(self._openBaseAdjustDialog)

        self.blurBtn.clicked.connect(self._blur)
        self.sharpenBtn.clicked.connect(self._sharpen)
        self.cannyBtn.clicked.connect(self._canny)
        self.binaryBtn.clicked.connect(self._binaryzation)
        self.invertBtn.clicked.connect(self._invert)
        self.grayBtn.clicked.connect(self._gray)
        list(map(lambda btn:btn.clicked.connect(self._toolBoxClicked),self.toolBtns))


    def _openBaseAdjustDialog(self):
        self.baseAdjustDialog = BaseAdjustDialog()
        self.baseAdjustDialog.dialogRejected.connect(self._baseAdjustDialogRejected)
        self.baseAdjustDialog.dialogAccepted.connect(self._baseAdjustDialogAccepted)
        self.baseAdjustDialog.brightSliderReleased.connect(self._adjustBright)
        self.baseAdjustDialog.warmSliderReleased.connect(self._adjustWarm)
        self.baseAdjustDialog.saturabilitySliderReleased.connect(self._adjustSaturation)
        self.baseAdjustDialog.contrastSliderReleased.connect(self._adjustContrast)
        self.baseAdjustDialog.show()

    def _baseAdjustDialogAccepted(self):
        self.adjusting = False
        self.img = self.bufferImg
        self.update()

    def _baseAdjustDialogRejected(self):
        self.adjusting = False
        self.update()

    def _adjustContrast(self,value):
        self.adjusting = True
        self.bufferImg = ImageUtil.adjustContrast(self.img, value)
        self.update()

    def _adjustBright(self,value):
        self.adjusting = True
        self.bufferImg = ImageUtil.adjustBright(self.img,value)
        self.update()

    def _adjustWarm(self,value):
        self.adjusting = True
        self.bufferImg = ImageUtil.adjustWarm(self.img,value)
        self.update()

    def _adjustSaturation(self,value):
        self.adjusting = True
        self.bufferImg = ImageUtil.adjustSaturation(self.img, value)
        self.update()

    def _drawLine(self,event):
        boardPos = self._getPosFromGlobal(event.pos())
        if self.drawing:
            self.bufferImg = self.img.copy()
            painter = self._initPainter(board=self.bufferImg)
            painter.drawLine(self.startPoint, boardPos)
        else:
            painter = self._initPainter()
            painter.drawLine(self.startPoint, self.endPoint)

    def _drawEllipse(self,event):
        boardPos = self._getPosFromGlobal(event.pos())
        if self.drawing:
            self.bufferImg = self.img.copy()
            painter = self._initPainter(board=self.bufferImg)
            painter.drawEllipse(QRect(self.startPoint, boardPos))

        else:
            painter = self._initPainter()
            painter.drawEllipse(QRect(self.startPoint, self.endPoint))

    def _drawRect(self,event):
        boardPos = self._getPosFromGlobal(event.pos())
        if self.drawing:
            self.bufferImg = self.img.copy()
            painter = self._initPainter(board=self.bufferImg)
            painter.drawRect(QRect(self.startPoint, boardPos))
        else:
            painter = self._initPainter()
            painter.drawRect(QRect(self.startPoint, self.endPoint))

    def _drawBucket(self,event):
        boardPos = self._getPosFromGlobal(event.pos())
        fillPositions = ImageUtil.floodFill(self.img,boardPos)
        painter = self._initPainter()
        [painter.drawPoint(x,y) for x,y in fillPositions]

    def _drawErase(self,event):
        self.penColor = self.backColor
        self._drawPen(event)

    def _drawPen(self,event):
        painter = self._initPainter()
        boardPos = self._getPosFromGlobal(event.pos())
        painter.drawLine(self.lastPoint, boardPos)
        self.lastPoint = boardPos
        self.update()

    def _toolBoxClicked(self):
        self._refreshButtons()
        toolBtn = self.sender()
        toolBtn.setChecked(True)


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

    def _blur(self):
        self.img = ImageUtil.blur(self.img)
        self._refreshBoard()

    def _canny(self):
        self.img = ImageUtil.canny(self.img)
        self._refreshBoard()

    def _sharpen(self):
        self.img = ImageUtil.sharpen(self.img)
        self._refreshBoard()

    def _gray(self):
        self.img = ImageUtil.gray(self.img)
        self._refreshBoard()

    def _invert(self):
        self.img = ImageUtil.invert(self.img)
        self._refreshBoard()

    def _binaryzation(self):
        self.img = ImageUtil.binaryzation(self.img)
        self._refreshBoard()

    def _refreshButtons(self):
        [btn.setChecked(False) for btn in self.toolBtns]

    def _refreshBoard(self):
        pix = QPixmap.fromImage(self.img)
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

    def _clearDraw(self):
        self.img = self.oriImg.copy()
        self._refreshBoard()

    def _wiseAction(self,action):
        if action == 'clock':
            transform = QTransform()
            transform.rotate(90)
            self.img = self.img.transformed(transform)
        elif action == 'antiClock':
            transform = QTransform()
            transform.rotate(-90)
            self.img = self.img.transformed(transform)
        elif action == 'verFilp':
            self.img = self.img.mirrored(True,False)
        else:
            self.img = self.img.mirrored(False,True)
        self._refreshBoard()

    def _openImg(self):
        fileName, fileType = QFileDialog.getOpenFileName(self,"选取文件","All Files (*)")
        self.img = QImage(fileName)
        self.oriImg = self.img.copy()
        self._refreshBoard()

def main():
    app = QApplication(sys.argv)
    application = PaintBoard()
    application.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()