someString = "This is a random string"

#A string is a string of characters, therefore, len(string) gives no. characters
print("the length of your string is", len(someString))

#print characters 6 - n
print(someString[6:])
#prints characters 0 - 5
print(someString[:5])
#prints 9-14
print(someString[9:14])

#counts the number of times a substring occurs
print(someString.count("random"))
#gives the index of when random starts. 
print(someString.index("random"))

#converts all string to lower case. Takes no argumeents.
print(someString.lower())
#Upper does the same. To capitalise certain characters, could do like this
print(someString[0:8].lower() + someString[9:14].upper() + someString[14:len(someString)].lower() )

#Can split the string into a list, based on the character in the split function
print(someString.split())
print(someString.split("s"))

#Can also check is a sequence starst with or ends with certain character sequences
print(someString.startswith("Some")) # returns false
print(someString.endswith("string")) # returns true

#Indexing operator can take negative values. It causes the index
#operator to go from the end of the string
print(someString[-6:])  # prints the last 6 string characters
print(someString[-1])   # prints the last string characters
print(someString[-7:-3]) # prints 7th from last to 3rd from last characters
