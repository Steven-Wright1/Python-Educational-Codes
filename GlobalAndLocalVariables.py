# x here is a global variable
x = 6

########################################################################
def example():
    z = 5
    print(z)    

#print(z) cannot be done outside of the fnc, as z local to fnc    
example()

                #BEST PRACTISE FOR CHANGING GLOBAL VARIABLE
########################################################################
def example2():
    z = 7
    print(z)
    print(x)

    #x += 1       #x is a global variable. It cannot be edited inside a function
    #print(x)     #Unless you use some kind of pointer or something

    y = x + 1     #can change x by assigning to a temp variable and returning
    return y
    
x = example2()    #then chnage the global variable x
print('Now The Global Value of x is ',x)

                #ANOTHER WAY TO DO IT - CAN CAUSE ISSUES THOUGH!
########################################################################
def exmaple3():
    global x
    x += 1
    print(x)

exmaple3()
