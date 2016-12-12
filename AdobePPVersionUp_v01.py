
import fileinput
import sys
import re
import platform
import os
import glob

#Regular Expression Pattern Options
#1: (((FOB_306_\d\d\d\d)_v(\d\d\d\d?)).mov)
			# Full match	0-22	`FOB_306_3490_v0003.mov`
			# Group 1.	0-22	`FOB_306_3490_v0003.mov`
			# Group 2.	0-18	`FOB_306_3490_v0003`
			# Group 3.	0-12	`FOB_306_3490`
			# Group 4.	14-18	`0003`

#Constant Variables
ProResFileLocations = "R:\Fresh_Off_The_Boat_s03\Final_Renders\FOB_306\ProRes_4444_Rec709"
PP_fileLocation = raw_input("Drag and drop unzipped Premiere project here:")







# Find Latest version of render
# Spit out whole name

def latestVersion(shotName):
	#Create list of all files starting with Shot name
	#shotName format has to be TRI_EPI_####
	versionList = []
	for name in glob.glob('R:\Fresh_Off_The_Boat_s03\Final_Renders\FOB_306\ProRes_4444_Rec709\{0}*'.format(shotName)):
		versionList.append(os.path.basename(name))# Getfilename only

	sorted(versionList)
	print versionList
	print "The latest version of this shot is: " + versionList[-1]
	return versionList[-1]

latestVersion("FOB_306_3490")








