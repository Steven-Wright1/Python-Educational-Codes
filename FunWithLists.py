King_name = input('''
My Leige,, dareth thee you pardon my candour and behold unto
me your reverent name?\n''')
n_jewels = int(input(King_name+  " sire, how many jewels are there? "))
avg_value = int(input("And the average value of such? "))
n_jewels_value = n_jewels * avg_value

print(n_jewels_value)

Musketeer_Names = ["Athos","Pothos","Aramis"]
Musketeer_ages = [55,34,67]
Musketeer_Names.insert(0, "D'artagnan")
Musketeer_ages.append(16)
print(Musketeer_Names)

Musketeer_ages.insert(0,Musketeer_ages.pop(len(Musketeer_ages)-1))
print(Musketeer_ages)

Muskeeter_to_execute = input("Sire, whom shall be executed? ")

count = 0; 
for i in Musketeer_Names:
    if(i == Muskeeter_to_execute):
        Musketeer_Names.remove(Muskeeter_to_execute)
        del Musketeer_ages[count]
        print("My leige ", Muskeeter_to_execute, "has been executed \n" )
        print("Sire, the names and ages of the remaining Musketeers \n", Musketeer_Names, '\n', Musketeer_ages)
    count +=1
        
if(len(Musketeer_Names) == 4):
    print("My holiness, he was not involved in the plot")




