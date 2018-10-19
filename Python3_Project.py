#This is the Python3 project to parse a log file
import urllib.request
import re
import os
from datetime import time
from datetime import date
from datetime import datetime

urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "Amazon_Logfile.txt")
#Opens and reads the text file. Closes afterwards
log = "Amazon_Logfile.txt"
file = open ("Amazon_Logfile.txt", 'r')
lines = file.readlines()
file.close()

#Look for the patterns
countline = 0
for line in lines:
	if line != -1:
		countline = countline + 1
print("There are " + str(countline) + " lines in this document")
