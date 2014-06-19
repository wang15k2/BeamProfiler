# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameraview.ui'
#
# Created: Wed May 28 18:29:43 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CameraView(object):
    def setupUi(self, CameraView):
        CameraView.setObjectName(_fromUtf8("CameraView"))
        CameraView.resize(400, 374)
        self.graphicsView = QtGui.QGraphicsView(CameraView)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 381, 331))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.pushButton = QtGui.QPushButton(CameraView)
        self.pushButton.setGeometry(QtCore.QRect(140, 340, 114, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(CameraView)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), CameraView.close)
        QtCore.QMetaObject.connectSlotsByName(CameraView)

    def retranslateUi(self, CameraView):
        CameraView.setWindowTitle(_translate("CameraView", "Form", None))
        self.pushButton.setText(_translate("CameraView", "Close", None))

