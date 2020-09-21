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
        self.brushSize = 2
        self.brushColor = Qt.black

    def _getToolBoxStatus(self):
        pass


    def mousePressEvent(self, event: QMouseEvent) -> None:

        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def mouseMoveEvent(self, event: QMouseEvent) -> None:

        if event.buttons() and Qt.LeftButton and self.drawing:
            # creating painter object
            painter = QPainter(self.img)

            # set the pen of the painter
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            # draw line from the last point of cursor to the current point
            # this will draw only one step
            painter.drawLine(self.lastPoint, event.pos())

            # change the last point
            self.lastPoint = event.pos()
            print(self.lastPoint)
            # update
            self.update()

    def paintEvent(self, event: QPaintEvent) -> None:
        canvasPainter = QPainter(self)
        canvasPainter.setRenderHint(QPainter.Antialiasing,True)
        canvasPainter.drawImage(self.rect(), self.img, self.img.rect())

    def _setDefaultBoard(self):
        self.img = QImage(self.scrollAreaWidgetContents.size(), QImage.Format_RGB32)
        self.img.fill(Qt.white)
        self._refreshBoard()

    def _establishConnections(self):
        self.actionNew.triggered.connect(self._clear)
        self.actionClear.triggered.connect(self._clear)
        self.actionSave.triggered.connect(self._save)
        self.actionOpenImg.triggered.connect(self._openImg)

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
        self.update()

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