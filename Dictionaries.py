#A dictionary has keys and values
#A dictionary is the equivalent of unordered_map in c++

#ALL KEYS HAVE TO BE UNIQUE, THE VALUES DON'T HAVE TO BE
gradeDict = {'Kelly':89,'David':65,'Jack':95,'Samantha':78}
            # key  value  key  value

print(gradeDict)

# to reference a specific grade
print(gradeDict['David'])       

# Allows us to change dict entries
gradeDict['David'] = 56         
print(gradeDict['David'])

#Adding entries to the dictionary
gradeDict ['Jessy'] = 92
print(gradeDict)

#Deleting entries from the dictionary
del gradeDict['David']
print(gradeDict)

#Let's pretend another test was taken. Can add second test scores to keys by
#assigning the values as a list
gradeDict = {'Kelly':[89,88],
             'Jack':[95,87],
             'Samantha':[78,89],
             'Jessy':[92,99]}
print(gradeDict)
print(gradeDict['Jessy'])
print(gradeDict['Jessy'][0]) #Allows you to reference specific list elements

