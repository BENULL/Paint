# coding =utf-8

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from src.view.BaseAdjustDialog import  Ui_baseAdjustDialog
from functools import partial

class BaseAdjustDialog(QDialog,Ui_baseAdjustDialog):

    brightSliderReleased = pyqtSignal(object)
    brightSliderValueChanged = pyqtSignal(object)
    dialogRejected = pyqtSignal()
    dialogAccepted = pyqtSignal()


    def __init__(self,*args,**kwargs):
        super(BaseAdjustDialog, self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.sliders = [self.brightSlider,self.saturabilitySlider,self.contrastSlider,self.warmSlider]
        self.sliderLabels = [self.brightLabel,self.saturabilityLabel,self.contrastLabel,self.warmLabel]
        self._establishConnections()

    def _establishConnections(self):
        self.dialogBtnBox.accepted.connect(self._dialogAccepted)
        self.dialogBtnBox.rejected.connect(self._dialogRejected)
        [self._buildSliderConnected(slider) for slider in self.sliders]

    def _buildSliderConnected(self,slider):
        slider.sliderReleased.connect(self._brightSliderReleased)
        slider.valueChanged.connect(partial(self._sliderValueChanged,slider))

    def _sliderValueChanged(self,slider):
        self.sliderLabels[self.sliders.index(slider)].setNum(self.brightSlider.value())

    def _brightSliderReleased(self):
        lightValue = self.brightSlider.value()
        self.brightLabel.setNum(lightValue)
        self.brightSliderReleased.emit(lightValue)

    def _dialogAccepted(self):
        self.dialogAccepted.emit()

    def _dialogRejected(self):
        self.dialogRejected.emit()








