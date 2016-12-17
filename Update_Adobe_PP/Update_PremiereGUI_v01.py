from __future__ import division
from PySide import QtGui,QtCore # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
import os
import PP_VersionUP_GUI_v03
import math
import shutil
import fileinput
import sys
import re
import platform
import glob
import StringIO




# This file holds our MainWindow and all design related things
            # it also keeps events etc that we defined in Qt Designer


class ExampleApp(QtGui.QMainWindow, PP_VersionUP_GUI_v03.Ui_MainWindow):

    ProResFileLocations = "R:\Cox\Final_Renders\Cox_Cable\ProRes_4444_Rec709"
    unzipLocation = "R:\IO Bullshit\VersionUpPriemere\COX\unzipped"

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        self.updateProjectBtn.clicked.connect(self.updateBtn)
        self.fileBrowse.clicked.connect(self.openFolder)
        




    def openFolder(self):
        fileName = QtGui.QFileDialog.getOpenFileName()
        theFile =fileName[0]
        self.fileLocation.setText(theFile)

    def updateBtn(self):
        theFile = self.fileLocation.text()
        self.runUpdate(theFile)
        

       



    def runUpdate(self,project_Location):

        ProResFileLocations = "R:\Cox\Final_Renders\Cox_Cable\ProRes_4444_Rec709"
        PP_fileLocation = project_Location
        unzipLocation = "R:\IO Bullshit\VersionUpPriemere\COX\unzipped"

        def correct_VersionNames(shotName):
            for name in glob.glob('R:\Cox\Final_Renders\Cox_Cable\ProRes_4444_Rec709\{0}*'.format(shotName)):
                fullFileName = name
                nameLen = len(fullFileName)
                print fullFileName + "Is this long: " + str(nameLen)
                if nameLen == 65:
                    try:
                        os.rename(name,insert_0(name,58))
                    except:
                        print "file already exists!!!! \n So I will not rename this file, but I will delete it."
                        os.remove(name)
                        pass
                else:
                    pass



        def findAndReplace():
            pattern = re.compile("(((COX_\d\d\d\d)_v(\d\d\d\d?)).mov)")
            dictofReplacments = {}
            openFile = open(PP_fileLocation, 'rb')

            #Create Dict of words
            for i, line in enumerate(openFile):
                for match in re.finditer(pattern,line):
                    print "\nI found shot " + match.group(1)
                    fullName = match.group(1)
                    shotName = match.group(3)
                    #Time to find the latest version
                    newestVersion = latestVersion(shotName)

                    dictofReplacments[fullName] = newestVersion
            openFile.close()

            print dictofReplacments


            # Use dict to replace words
            for key in dictofReplacments:
                print key
                print dictofReplacments[key]
                newVersion = dictofReplacments[key]

                openFile = open(PP_fileLocation).read()
                openFile = openFile.replace(key,newVersion)
                f = open(PP_fileLocation,'w')
                f.write(openFile)
                f.close()



        def latestVersion(shotName):
            #Create list of all files starting with Shot name
            #shotName format has to be TRI_EPI_####
            versionList = []
            sorting_dic = {}
            #Sanitize names
            for name in glob.glob('R:\Cox\Final_Renders\Cox_Cable\ProRes_4444_Rec709\{0}*'.format(shotName)):
                correct_VersionNames(shotName)

            #Create dic for sorting
            for name in glob.glob('R:\Cox\Final_Renders\Cox_Cable\ProRes_4444_Rec709\{0}*'.format(shotName)):
                # Getfilename only
                versionNumber = re.search(r'(\d+).mov$',name).group(1)
                print versionNumber
                sorting_dic[os.path.basename(name)] = versionNumber
            #add version in order from smallest to largest in list
            for key, value in sorted(sorting_dic.iteritems(), key=lambda (k,v): (v,k)):
                print "%s: %s" % (key, value)
                versionList.append(key)

            
            
            print versionList
            print "The latest version of this shot is: " + versionList[-1] # Get last item in list. Which should be the highest number
            return versionList[-1]



        def insert_0(string, index):
            return string[:index] + '0' + string[index:]

        findAndReplace()











def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()