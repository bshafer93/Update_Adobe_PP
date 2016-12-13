
import fileinput
import sys
import re
import platform
import os
import glob
import zipfile
import StringIO
#reg find version number
			#(\d+).mov$
			# Full match	0-22	`008.mov`
			# Group 1.	0-22	`008`
#Regular Expression Pattern Options
#1: (((FOB_306_\d\d\d\d)_v(\d\d\d\d?)).mov)
			# Full match	0-22	`FOB_306_3490_v0003.mov`
			# Group 1.	0-22	`FOB_306_3490_v0003.mov`
			# Group 2.	0-18	`FOB_306_3490_v0003`
			# Group 3.	0-12	`FOB_306_3490`
			# Group 4.	14-18	`0003`

#Regular Expression Pattern Options
#1: (((COX_\d\d\d\d)_v(\d\d\d\d?)).mov)
			# Full match	0-22	`COX_306_3490_v0003.mov`
			# Group 1.	0-22	`COX_1020_v0010.mov`
			# Group 2.	0-18	`COX_1020_v0010`
			# Group 3.	0-12	`COX_1020`
			# Group 4.	14-18	`0010`

#Constant Variables
ProResFileLocations = "R:\Cox\Final_Renders\Cox_Cable\ProRes_4444_sRGB"
PP_fileLocation = raw_input("Drag and drop unzipped Premiere project here:")
unzipLocation = "R:\IO Bullshit\VersionUpPriemere\COX\unzipped"


def correct_VersionNames(shotName):
	for name in glob.glob('R:\Cox\Final_Renders\Cox_Cable\ProRes_4444_sRGB\{0}*'.format(shotName)):
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
	for name in glob.glob('R:\Cox\Final_Renders\Cox_Cable\ProRes_4444_sRGB\{0}*'.format(shotName)):
		correct_VersionNames(shotName)

	#Create dic for sorting
	for name in glob.glob('R:\Cox\Final_Renders\Cox_Cable\ProRes_4444_sRGB\{0}*'.format(shotName)):
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



#findAndReplace()





			


