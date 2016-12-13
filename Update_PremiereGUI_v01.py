# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Update_PremiereGUI_v01.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(394, 300)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 291))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.verticalLayoutWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.Instructions = QtGui.QPlainTextEdit(self.frame)
        self.Instructions.setEnabled(True)
        self.Instructions.setGeometry(QtCore.QRect(10, 10, 371, 141))
        self.Instructions.setAutoFillBackground(False)
        self.Instructions.setObjectName(_fromUtf8("Instructions"))
        self.fileLocation = QtGui.QLineEdit(self.frame)
        self.fileLocation.setGeometry(QtCore.QRect(10, 160, 331, 20))
        self.fileLocation.setText(_fromUtf8(""))
        self.fileLocation.setObjectName(_fromUtf8("fileLocation"))
        self.UpdateBtn = QtGui.QPushButton(self.frame)
        self.UpdateBtn.setGeometry(QtCore.QRect(8, 190, 371, 23))
        self.UpdateBtn.setObjectName(_fromUtf8("UpdateBtn"))
        self.selectFile = QtGui.QPushButton(self.frame)
        self.selectFile.setGeometry(QtCore.QRect(350, 160, 31, 23))
        self.selectFile.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Folder-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectFile.setIcon(icon)
        self.selectFile.setObjectName(_fromUtf8("selectFile"))
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayoutWidget.raise_()
        self.UpdateBtn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Instructions.setPlainText(_translate("Form", "1. Save and version up your Premiere Project\n"
"2. Copy & Paste project to new location\n"
"3. Right-Click the .prproj >  7zip > Extract here\n"
"4. You should now have a new file without any extension\n"
"5. Put that file in a folder seperate from the .prproj\n"
"6. Copy file location and paste into program\n"
"7. Run Program\n"
"8. Add the .prproj file extension to the file you just processed\n"
"9. You should now have a updated Premiere Project :)", None))
        self.fileLocation.setPlaceholderText(_translate("Form", "Copy Premiere Project file here", None))
        self.UpdateBtn.setText(_translate("Form", "Update Project File", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

