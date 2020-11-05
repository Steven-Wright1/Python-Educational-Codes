                            #Writing to a file
################################################################
writeMe = 'Example Text'

saveFile = open('Filename.txt','w')     #creates the fil
saveFile.write(writeMe)                 #writes to the file
saveFile.close()                        #closes the file

    #Appending to a file (Also creates a new file if non-existent)
################################################################
appendMe = 'This is the text that has been added to the file'

saveFile = open('Filename.txt','a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()

                            #Reading from a file
################################################################
readMe = open('Filename.txt','r').read()
print(readMe)
splitMe = readMe.split('\n')        #splits the test into a Python list by line
print(splitMe)
print(splitMe[0]) #prints the first entry of the Python list created above
