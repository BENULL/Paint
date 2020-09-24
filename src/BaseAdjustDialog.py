# coding =utf-8

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from src.view.BaseAdjustDialog import  Ui_baseAdjustDialog

class BaseAdjustDialog(QDialog,Ui_baseAdjustDialog):

    def __init__(self,*args,**kwargs):
        super(BaseAdjustDialog, self).__init__(*args,**kwargs)
        self.setupUi(self)