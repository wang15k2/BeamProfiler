import cv2
import numpy
 
from PyQt4 import QtGui
 
class OpenCVQImage(QtGui.QImage):
 
    def __init__(self, opencvBgrImg):
        img = cv2.cvtColor(opencvBgrImg, cv2.cv.CV_BGR2RGB)
        super(OpenCVQImage, self).__init__(img.data, img.shape[1], img.shape[0], \
            QtGui.QImage.Format_RGB888)