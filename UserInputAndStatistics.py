name = input('What is your name?: ')
print('Hello', name)

#Input is a string by default, therefore this code will write number 5 times
number = input("Enter a number: ")
print(number * 5)

#Must prefix input with int if you want to enter an integer
number = int(input("Enter a number: "))
print(number * 5)

                            #Statistics
###########################################################################
import statistics
exList = [6,3,3,7,2,6,5,3,7,9,6,5,3,1,1,4,6,8,4,3,2,5,6,2,3]

x = statistics.mean(exList)
print('The mean is',x)
x = statistics.median(exList)
print('The median is',x)
x = statistics.mode(exList)
print('The mode is',x)
x = statistics.variance(exList)
print('The variance is',x)
x = statistics.stdev(exList)
print('The standard deviation is',x)
