#!/usr/local/bin/python
# encoding: utf-8
import cv2
import numpy
 
from PyQt4 import QtCore
from PyQt4 import QtGui
from opencvqimage import OpenCVQImage
 
class CameraWidget(QtGui.QWidget):
 
    newFrame = QtCore.pyqtSignal(numpy.ndarray)
 
    def __init__(self, cameraDevice, parent=None):
        super(CameraWidget, self).__init__(parent)
 
        self._frame = None
 
        self._cameraDevice = cameraDevice
        self._cameraDevice.newFrame.connect(self._onNewFrame)
 
        w, h = self._cameraDevice.frameSize
        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)
 
    @QtCore.pyqtSlot(numpy.ndarray)
    def _onNewFrame(self, frame):
        self._frame = frame
        self.newFrame.emit(self._frame)
        self.update()
 
    def changeEvent(self, e):
        if e.type() == QtCore.QEvent.EnabledChange:
            if self.isEnabled():
                self._cameraDevice.newFrame.connect(self._onNewFrame)
            else:
                self._cameraDevice.newFrame.disconnect(self._onNewFrame)
 
    def paintEvent(self, e):
        if self._frame is None:
            return
        painter = QtGui.QPainter(self)
        painter.drawImage(QtCore.QPoint(0, 0), OpenCVQImage(self._frame))