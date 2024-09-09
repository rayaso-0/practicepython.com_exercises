# Python Exercise Number 2
# Exercise: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Date: Mon Sep 9 2024

# Ask for the input integer
num = int(input("Give me a number: "))

# See if the given input can be divided by 2
odd_even = num % 2

# if statement saying if the remainder is more than zero, it is an odd number, else it's an even number
if odd_even > 0:
    print("You got a odd number!")
else:
    print("You got an even number! ")

# EXTRAS!!!!!
# -----------
# If the number is a multiple of 4, print out a different message.
mult_four = num % 4

if mult_four == 0: 
    print("This number is a multiple of 4!")
elif mult_four > 0:
    print("This number is NOT a multiple of 4!")

# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
num1 = int(input("Give me a second number: "))
check = int(input("Give me a third number to see if it can be divided evenly by the second number: "))

divided_evenly = num1 % check

if divided_evenly == 0:
    print("This number can be divided evenly.")
elif divided_evenly > 0:
    print("This number can NOT be divided evenly.")

