# read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

if number2 > number1: largest_number = number2
if number3 > largest_number: largest_number = number3

print("The largest number is", largest_number, end="\n")
