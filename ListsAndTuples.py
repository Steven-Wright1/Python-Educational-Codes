                                #TUPLE
####################################################################### 
# A tuple is unchangeable once it has been defined.
# A tuple might be used for variable assignments in sequence unpacking

def example():
    return 15,19

#here a,b is a tuple. It unpacks the return of exmaple and assigns to a,b
a,b = example()
'''
A tuple may be defined simply with commas 5,2,5,7,3,5 for eg. or
using brackets, such as (5,2,5,7,3,5)
'''
print(a,b) 

     #LIST (often referred to as array but it is really a Python list)
#######################################################################
# A list is changeable. IT IS DEFINED USING SQUARE BRACKETS
x = [6,3,3,6,2,5,78,3,6,7]
print(x)
print(x[5])

#List Operations
x.append(1221)
print(x)

x.insert(2,876544)
print(x)

#removes a specific value. 
x.remove(876544)
print(x)

#Important to note that if the number is repeated, remove only removes the first
x.remove(3)
print(x)

#gives us the index of the number 78. Again, doesn't work for repeated numbers
print(x.index(6))

#Gives us the number of 3's in our list
print(x.count(3))

#sorts the list
x.sort()
print(x)

#sorting and reversing string list orders
x = ['Sam','Dan','Bob','Alex','Piglet']
print(x)
x.sort()
print(x)
x.reverse()
print(x)









