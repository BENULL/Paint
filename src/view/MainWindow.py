# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 631)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolBox = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setObjectName("toolBox")
        self.formLayout = QtWidgets.QFormLayout(self.toolBox)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(10, -1, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.penBtn = QtWidgets.QToolButton(self.toolBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.penBtn.setIcon(icon1)
        self.penBtn.setIconSize(QtCore.QSize(32, 32))
        self.penBtn.setCheckable(True)
        self.penBtn.setObjectName("penBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.penBtn)
        self.bucketBtn = QtWidgets.QToolButton(self.toolBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/bucket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bucketBtn.setIcon(icon2)
        self.bucketBtn.setIconSize(QtCore.QSize(32, 32))
        self.bucketBtn.setCheckable(True)
        self.bucketBtn.setObjectName("bucketBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bucketBtn)
        self.lineBtn = QtWidgets.QToolButton(self.toolBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lineBtn.setIcon(icon3)
        self.lineBtn.setIconSize(QtCore.QSize(32, 32))
        self.lineBtn.setCheckable(True)
        self.lineBtn.setObjectName("lineBtn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lineBtn)
        self.rectBtn = QtWidgets.QToolButton(self.toolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rectBtn.sizePolicy().hasHeightForWidth())
        self.rectBtn.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/rect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rectBtn.setIcon(icon4)
        self.rectBtn.setIconSize(QtCore.QSize(32, 32))
        self.rectBtn.setCheckable(True)
        self.rectBtn.setObjectName("rectBtn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.rectBtn)
        self.ellipseBtn = QtWidgets.QToolButton(self.toolBox)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img/ellipse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ellipseBtn.setIcon(icon5)
        self.ellipseBtn.setIconSize(QtCore.QSize(32, 32))
        self.ellipseBtn.setCheckable(True)
        self.ellipseBtn.setObjectName("ellipseBtn")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.ellipseBtn)
        self.eraseButton = QtWidgets.QToolButton(self.toolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eraseButton.sizePolicy().hasHeightForWidth())
        self.eraseButton.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/img/erase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eraseButton.setIcon(icon6)
        self.eraseButton.setIconSize(QtCore.QSize(32, 32))
        self.eraseButton.setCheckable(True)
        self.eraseButton.setObjectName("eraseButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.eraseButton)
        self.preColorBtn = QtWidgets.QPushButton(self.toolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preColorBtn.sizePolicy().hasHeightForWidth())
        self.preColorBtn.setSizePolicy(sizePolicy)
        self.preColorBtn.setStyleSheet("background-color: #000000")
        self.preColorBtn.setText("")
        self.preColorBtn.setIconSize(QtCore.QSize(32, 32))
        self.preColorBtn.setObjectName("preColorBtn")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.preColorBtn)
        self.baseAdjustBtn = QtWidgets.QPushButton(self.toolBox)
        self.baseAdjustBtn.setObjectName("baseAdjustBtn")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.baseAdjustBtn)
        self.cannyBtn = QtWidgets.QPushButton(self.toolBox)
        self.cannyBtn.setObjectName("cannyBtn")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.SpanningRole, self.cannyBtn)
        self.blurBtn = QtWidgets.QPushButton(self.toolBox)
        self.blurBtn.setObjectName("blurBtn")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.SpanningRole, self.blurBtn)
        self.pxLabel = QtWidgets.QLabel(self.toolBox)
        self.pxLabel.setObjectName("pxLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pxLabel)
        self.penSizeBtn = QtWidgets.QComboBox(self.toolBox)
        self.penSizeBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.penSizeBtn.setEditable(True)
        self.penSizeBtn.setObjectName("penSizeBtn")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.penSizeBtn)
        self.backColorBtn = QtWidgets.QPushButton(self.toolBox)
        self.backColorBtn.setStyleSheet("background-color:#FFFFFF")
        self.backColorBtn.setText("")
        self.backColorBtn.setObjectName("backColorBtn")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.backColorBtn)
        self.sharpenBtn = QtWidgets.QPushButton(self.toolBox)
        self.sharpenBtn.setObjectName("sharpenBtn")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.SpanningRole, self.sharpenBtn)
        self.grayBtn = QtWidgets.QPushButton(self.toolBox)
        self.grayBtn.setObjectName("grayBtn")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.grayBtn)
        self.invertBtn = QtWidgets.QPushButton(self.toolBox)
        self.invertBtn.setObjectName("invertBtn")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.SpanningRole, self.invertBtn)
        self.binaryBtn = QtWidgets.QPushButton(self.toolBox)
        self.binaryBtn.setObjectName("binaryBtn")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.binaryBtn)
        self.embossBtn = QtWidgets.QPushButton(self.toolBox)
        self.embossBtn.setObjectName("embossBtn")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.SpanningRole, self.embossBtn)
        self.horizontalLayout_3.addWidget(self.toolBox)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setFocusPolicy(QtCore.Qt.TabFocus)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 658, 413))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.board = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.board.sizePolicy().hasHeightForWidth())
        self.board.setSizePolicy(sizePolicy)
        self.board.setLineWidth(0)
        self.board.setText("")
        self.board.setScaledContents(True)
        self.board.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.board.setIndent(0)
        self.board.setObjectName("board")
        self.gridLayout.addWidget(self.board, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 971, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menu_3)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/img/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon7)
        self.actionNew.setObjectName("actionNew")
        self.actionOpenImg = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/img/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenImg.setIcon(icon8)
        self.actionOpenImg.setObjectName("actionOpenImg")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/img/img/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon9)
        self.actionSave.setObjectName("actionSave")
        self.actionClear = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/img/img/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon10)
        self.actionClear.setObjectName("actionClear")
        self.actionClearDraw = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/img/img/clearImg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearDraw.setIcon(icon11)
        self.actionClearDraw.setObjectName("actionClearDraw")
        self.actionClockWise = QtWidgets.QAction(MainWindow)
        self.actionClockWise.setObjectName("actionClockWise")
        self.actionAntiClockWise = QtWidgets.QAction(MainWindow)
        self.actionAntiClockWise.setObjectName("actionAntiClockWise")
        self.actionVerFilp = QtWidgets.QAction(MainWindow)
        self.actionVerFilp.setObjectName("actionVerFilp")
        self.actionHorFilp = QtWidgets.QAction(MainWindow)
        self.actionHorFilp.setObjectName("actionHorFilp")
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionOpenImg)
        self.menu.addAction(self.actionSave)
        self.menu_2.addAction(self.actionClear)
        self.menu_2.addAction(self.actionClearDraw)
        self.menu_4.addAction(self.actionClockWise)
        self.menu_4.addAction(self.actionAntiClockWise)
        self.menu_4.addAction(self.actionVerFilp)
        self.menu_4.addAction(self.actionHorFilp)
        self.menu_3.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Paint"))
        self.penBtn.setText(_translate("MainWindow", "画笔"))
        self.bucketBtn.setText(_translate("MainWindow", "喷桶"))
        self.lineBtn.setText(_translate("MainWindow", "直线"))
        self.rectBtn.setText(_translate("MainWindow", "矩形"))
        self.ellipseBtn.setText(_translate("MainWindow", "椭圆"))
        self.eraseButton.setText(_translate("MainWindow", "橡皮擦"))
        self.baseAdjustBtn.setText(_translate("MainWindow", "图像调节"))
        self.cannyBtn.setText(_translate("MainWindow", "边缘检测"))
        self.blurBtn.setText(_translate("MainWindow", "模糊"))
        self.pxLabel.setText(_translate("MainWindow", "px"))
        self.penSizeBtn.setItemText(0, _translate("MainWindow", "2"))
        self.penSizeBtn.setItemText(1, _translate("MainWindow", "4"))
        self.penSizeBtn.setItemText(2, _translate("MainWindow", "6"))
        self.penSizeBtn.setItemText(3, _translate("MainWindow", "8"))
        self.penSizeBtn.setItemText(4, _translate("MainWindow", "10"))
        self.penSizeBtn.setItemText(5, _translate("MainWindow", "12"))
        self.penSizeBtn.setItemText(6, _translate("MainWindow", "14"))
        self.sharpenBtn.setText(_translate("MainWindow", "锐化"))
        self.grayBtn.setText(_translate("MainWindow", "灰度化"))
        self.invertBtn.setText(_translate("MainWindow", "反相"))
        self.binaryBtn.setText(_translate("MainWindow", "二值化"))
        self.embossBtn.setText(_translate("MainWindow", "浮雕"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "图像"))
        self.menu_4.setTitle(_translate("MainWindow", "旋转"))
        self.actionNew.setText(_translate("MainWindow", "新建"))
        self.actionOpenImg.setText(_translate("MainWindow", "打开图像"))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionClear.setText(_translate("MainWindow", "清空"))
        self.actionClearDraw.setText(_translate("MainWindow", "还原"))
        self.actionClockWise.setText(_translate("MainWindow", "顺时针"))
        self.actionAntiClockWise.setText(_translate("MainWindow", "逆时针"))
        self.actionVerFilp.setText(_translate("MainWindow", "垂直"))
        self.actionHorFilp.setText(_translate("MainWindow", "水平"))
import img
