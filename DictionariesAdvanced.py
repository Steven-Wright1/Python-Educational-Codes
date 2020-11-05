#In a real dictionary, you look up a word and find a meaning
#In a python dictionary (or map), you look up a key, and find a value

Eg_Dictionary = {"pi":3.14 , 25:"The square of 5" , "Vitthal":"A name"}

# Value Lookup
print("The value for key, pi, is", Eg_Dictionary["pi"])


print(Eg_Dictionary.keys())
print(Eg_Dictionary.values())
print(len(Eg_Dictionary.keys()))


# CHECK IF KEYS ARE IN THE DICTIONARY. IF SO, REMOVE
Key_to_Delete = input("Please enter the key you would like to remove ")

if Key_to_Delete in Eg_Dictionary:
    Eg_Dictionary.pop(Key_to_Delete)
    print("The key-value pair for", Key_to_Delete, "has been removed")

print(Eg_Dictionary)
