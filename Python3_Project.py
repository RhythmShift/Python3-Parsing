#This is the Python3 project to parse a log file
import urllib.request
import re

urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "Amazon_Logfile.txt")

log = "Amazon_Logfile.txt"
file = open(log, 'r')
file.mode == 'r'
contents = file.readlines()
print(contents)
