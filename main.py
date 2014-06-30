#!/usr/bin/local/python
# encoding: utf-8

import sys
from PyQt4.QtGui import QApplication, QDialog, QMainWindow
from ui_profilewindow import Ui_ProfileWindow

def main():
	app = QApplication(sys.argv)
	window = QMainWindow()
	ui = Ui_ProfileWindow(window)
	ui.setupUi()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()