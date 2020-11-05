
def ReverseString(someString):
    #Base cases - ie - deal within instances in which the function wouldn't be used
    if someString is None:
        return someString
    if len(someString) <= 1:
        return someString

    #takes the first charcater of the string and tacks it onto the end
    #then it recurses, tacking the 2nd char on the end. Then the 3rd. 
    return ReverseString(someString[1:]) + someString[0]

string = "Hello world"
print("The reverse is", ReverseString(string))

#This was just an exmaple of a recursive function though
#A string can be reversed much simpler by indexing
newstring = "The house on the other side of the street is green"
print("The reverse of newstring is", newstring[::-1])
