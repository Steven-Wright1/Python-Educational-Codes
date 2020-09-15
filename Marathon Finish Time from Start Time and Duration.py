import math

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))


total_mins = mins + dura

#Calculates the number of hours (correct)
hours_passed = math.floor(total_mins/60)
hour = (hour + hours_passed) % 24

#Calculates the number of minutes passed
mins_passed = total_mins % 60


print("End time is: " + str(hour) + ":" + str(mins_passed))
