#Exercise 1 (and Solution)

#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extras:

#    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


import datetime;
name = input("Enter your name: ")
print("Usename is "+name)
age = int(input("Enter your age: "))
# calculate the year when they turn 100
present_year = datetime.datetime.now().year

time_remaining = 100 - age
print(time_remaining)
time_in_years = str(present_year + time_remaining)
print(" You will turn 100 in "+time_in_years)



