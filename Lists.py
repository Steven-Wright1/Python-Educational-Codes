List = [1,2,3,4,5]

List.append(76)
List.insert(0,0)
List.insert(2,63)

#Remove a specific number
List.remove(76)
#Deletes the desired index
del List[len(List)-1]
#Returns the deleted element
a = List.pop(1)

print(a)
print(List)
