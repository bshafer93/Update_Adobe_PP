from __future__ import division
from PySide import QtGui,QtCore # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
import os
import Update_PremiereGUI_v01
import math
import shutil



# This file holds our MainWindow and all design related things
            # it also keeps events etc that we defined in Qt Designer




class ExampleApp(QtGui.QMainWindow, Update_PremiereGUI_v01.Ui_Form):

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        
        self.selectFile.clicked.connect(self.getFile)
        self.AE2015.clicked.connect(self.update2015)
        self.AE20153.clicked.connect(self.update20153)



    def getFile(self):
        print "Howdy Ho!"
        filename = QFileDialog.getOpenFileName(w, 'Open File', '/')

        self.fileLocation.setText(filename)
        print filename
    def update2015(self):
        self.WORKIT("2015")
    def update2014(self):
        self.WORKIT("2014")


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()