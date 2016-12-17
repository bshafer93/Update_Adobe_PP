# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\IE\Desktop\Update_Premiere\Update_Adobe_PP\PP_VersionUp_v01.ui'
#
# Created: Fri Dec 16 23:25:24 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 362)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 360))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(450, 360))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.fileLocation = QtGui.QLineEdit(self.gridLayoutWidget)
        self.fileLocation.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileLocation.sizePolicy().hasHeightForWidth())
        self.fileLocation.setSizePolicy(sizePolicy)
        self.fileLocation.setMinimumSize(QtCore.QSize(200, 0))
        self.fileLocation.setReadOnly(False)
        self.fileLocation.setObjectName("fileLocation")
        self.gridLayout.addWidget(self.fileLocation, 1, 0, 1, 1)
        self.fileBrowse = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileBrowse.sizePolicy().hasHeightForWidth())
        self.fileBrowse.setSizePolicy(sizePolicy)
        self.fileBrowse.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("R:\Assets\Online_Tools\IO_Scripts\Update_Adobe_PP\icon\Folder-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileBrowse.setIcon(icon)
        self.fileBrowse.setObjectName("fileBrowse")
        self.gridLayout.addWidget(self.fileBrowse, 1, 1, 1, 1)
        self.updateProjectBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.updateProjectBtn.setObjectName("updateProjectBtn")
        self.gridLayout.addWidget(self.updateProjectBtn, 2, 0, 1, 2)
        self.instructionText = QtGui.QPlainTextEdit(self.gridLayoutWidget)
        self.instructionText.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instructionText.sizePolicy().hasHeightForWidth())
        self.instructionText.setSizePolicy(sizePolicy)
        self.instructionText.setAutoFillBackground(False)
        self.instructionText.setObjectName("instructionText")
        self.gridLayout.addWidget(self.instructionText, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.fileLocation.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Unzipped Premiere file here", None, QtGui.QApplication.UnicodeUTF8))
        self.updateProjectBtn.setText(QtGui.QApplication.translate("MainWindow", "Update Shots", None, QtGui.QApplication.UnicodeUTF8))
        self.instructionText.setPlainText(QtGui.QApplication.translate("MainWindow", "1. Save and version up your Premiere Project\n"
"2. Copy & Paste project to new location\n"
"3. Right-Click the .prproj >  7zip > Extract here\n"
"4. You should now have a new file without any extension\n"
"5. Put that file in a folder seperate from the .prproj\n"
"6. Click folder and navigate to file\n"
"7. Click \"Update Shots\"\n"
"8. Add the .prproj file extension to the file you just processed\n"
"9. You should now have a updated Premiere Project :)", None, QtGui.QApplication.UnicodeUTF8))

