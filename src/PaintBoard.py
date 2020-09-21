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
        self._establishConnections()
        self._setDefaultBoard()
        self._initParam()

    def _initParam(self):
        self.drawing = False
        self.lastPoint = QPoint()
        self.brushSize = 3
        self.brushColor = Qt.red

    def _getToolBoxStatus(self):
        pass


    def mousePressEvent(self, event: QMouseEvent) -> None:

        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = self._getPosFromGlobal(event.pos())

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def mouseMoveEvent(self, event: QMouseEvent) -> None:

        if event.buttons() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.img)
            painter.setRenderHint(QPainter.Antialiasing,True)
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            boardPos = self._getPosFromGlobal(event.pos())
            painter.drawLine(self.lastPoint,boardPos )

            self.lastPoint = boardPos
            print(self.lastPoint)
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
        self.brushSizeBtn.currentIndexChanged.connect(self._chooseBrushSize)
        self.lineBtn.clicked.connect(self._toolBoxClicked)
        self.ellipseBtn

    def _drawLine(self):
        pass

    def _drawEllipse(self):
        pass

    def _drawRect(self):
        pass


    def _toolBoxClicked(self):
        pass


    def _chooseBrushSize(self):
        pass

    def _choosePreColor(self):
        self.preColorBtn.setStyleSheet("background-color:%s" % self._getColor())

    def _chooseBackColor(self):
        self.backColorBtn.setStyleSheet("background-color:%s" % self._getColor())

    def _getColor(self):
        color = QColorDialog.getColor()
        colorName = color.name()
        return colorName

    def _refreshButtons(self):
        self.penBtn.setChecked(False)
        self.brushBtn.setChecked(False)
        self.lineBtn.setChecked(False)
        self.ellipseBtn.setChecked(False)

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