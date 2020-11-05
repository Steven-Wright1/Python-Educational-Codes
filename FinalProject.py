from statistics import mean as m 

admins = {'Python':'Pass123@', 'a':'b'}
studentDict = {'Jeff':[78,88,93],
               'Alex':[92,76,88],
               'Sam':[89,92,93]}

def enterGrades():
    exit = 1; 
    while(exit != 0):
        nameToEnter = input('Student Name:')
        gradetoEnter = int(input('Grade:'))

        if nameToEnter in studentDict:
            print('Adding Grade..')
            studentDict[nameToEnter].append(gradetoEnter)
        else:
            print("Student does not exist")

        exit = int(input('''Would you like to add another grade?
        [1] Yes [0] No
                         '''))

def removeStudent():
    nameToRemove = input('Which Student Do You Want to Remove? \n')
    if nameToRemove in studentDict:
        del studentDict[nameToRemove]
    else:
        print('That Student Does Not Exist')
    

def studentAVG():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
        print(eachStudent, 'has an average grade of:', avgGrade)
        
      



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
        enterGrades()
        print(studentDict)
    elif action == 2:
        removeStudent()
        print('\n', studentDict)
    elif action == 3:
        studentAVG()
    elif action == 4:
        exit()
    else:
        print("Invalid input! Please select an option")


login = input('Username: ')
passw = input('Password: ')
if login in admins:
    if admins[login] == passw:
        print("Welcome", login)        
        while True:
                main()
    else:
        print('Invalid Password')
else:
        print('Username does not exist')


    


