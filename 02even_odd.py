'''Exercise 2 (and Solution)

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

'''Exercise 2 (and Solution)

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
user_input = int(input("Enter any positive number: "))
if (user_input%2 == 0):
  #print("Number that you entered is even")
  if (user_input%4 == 0):
    print("Number that you entered is multiple of 4")
  else:
    print("Number that you entered is even")
  
else:
  print("You have entered an odd number")


num = int(input("OK! now enter any other number: "))
check = int(input("Enter a number which divides "+ str(num)))
dividend = num/check
if ( dividend >= 0):
  print(str(num) +" is divisible by "+str(check)+ " " +str(dividend) +" times")
else:
  print("Invalid number")

# calculate the year when they turn 100


#print(time_remaining)
#time_in_years = str(present_year + time_remaining)

  
