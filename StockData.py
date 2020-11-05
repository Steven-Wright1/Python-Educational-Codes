import urllib.request
import sys

################################
#Step 1 - Download the zip file
################################
'''
#intialise a variable with the url to download
urlOfFileName = "https://www.nseindia.com/content/historical/EQUTIES/2015/JUL/cm16OCT2020bhav.csv.zip"

#intialise a variable in which to store the URL


#boiler plate code to convince the website we're human
hdr = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

#request url
webRequest = urllib.request.Request(urlOfFileName, headers = hdr)

try:
    page = urllib.request.urlopen(urlOfFileName)
    content = page.read()
    output = open(LocalZipFilePath, "wb") # wb indicates we wish to write. b indicates that the file is binary
    output.write(bytearray(content)) # bytearray in a python library function that writes a binary file to a written file
    output.close() # always close the file

except urllib.error.HTTPError as e:
    print(e.fp.read())
    print("The file could not be downloaded")
    '''
#########################################
#Step 2 - Unzip the zip file and get csv
#########################################
    
import zipfile, os
#Give the zipFilePath
LocalZipFilePath = "D:\cm16OCT2020bhav.csv.zip"
#intialise a variable with the local directory in which to extract the zip files data
localExtractFilePath = "D:\unzipped"


#check if the zip file was downloaded correctly. If it has, execute the following
if os.path.exists(LocalZipFilePath):
    print("cool" + LocalZipFilePath + "exists")

    # Don't know how many files are in the zip file, so intialise an empty array to save the file names
    listOfFiles = []
    #unzip the file
    fh = open(localExtractFilePath, 'rb') # rb = reading binary file
    #zipFileHandler is boiler plate code that knows how to read a list of zipped files
    zipFileHandler = zipfile.ZipFile(fh)
    #iterate over the list
    for filename in zipFileHandler.namelist():
        #Extract files and append to list of files already extracted
        zipFileHandler.extract(filename,localExtractFilePath)
        listOfFiles.append(localExtractFilePath + filename)
        print("Extracted" + filename + " from the zip file to" + localExtractFilePath)
    print("in total, we extracted", str(len(listOfFiles)))
    fh.close()
else:
    print("Fuck knows what's happening")

#########################################
#Step 3 - Process the CSV File Line-by-Line
#########################################





















    

    
    
    
