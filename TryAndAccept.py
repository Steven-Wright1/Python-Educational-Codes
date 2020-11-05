
try:
    print('Running the try...')     #this is like troubleshooting
    print('5'+ 5)                   #if you do not include try and except then
                                    #code will break entirely


#except Exception as e:
#    print(str(e))                   #This code ignores ANY error
#    print('Do more things...')


except TypeError as t:              #We know the error is a type error and can 
    print('Type Error Triggered')   #ensure the code responds and ignores ONLY
                                    #type errors

    
try:
    print('Running the try...')
    import mars                     #can trigger general exception by importing
    print('5'+ x)                   #a module that doesn't exist
    
    
except NameError as n:              #We know the error is a Name error and can 
    print('Name Error Triggered')   #get the code to respond specifically also

except Exception as e:
    print('General exception hit... ie - error is not type or name')
    print(str(e))                   #This allows us to print the specific error

    
#However, as clear here, the code can carry on with try and except
print('Code continues onwards')
