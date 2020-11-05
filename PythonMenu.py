def main(): 
     print('''
           Welcome to Grade Central
           [1] - Enter Grades
           [2] - Remove Student
           [3] - Student Average Grades
           [4] - Exit
           \n
           ''')

     action = int(input("What would you like to do today? \n"))
     if action == 1:
         print(1)
     elif action == 2:
         print(2)
     elif action == 3:
         print(3)
     elif action == 4:
         print("The program has been exited")
     else:
         print("Invalid input! Please select an option")
     return action

action = main()
while action != 4:
     action = main()
