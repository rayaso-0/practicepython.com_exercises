# Python Exercise Number 1
# Exercise: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Date: Mon Sep 9 2024


# Variables for user name and age. Input function added.
name = input("Hello, What is your name?: ")
print("Hello, " + name)

age = int(input("What is your age?: "))

# Calculate the amount of years to 100 for the user
year_to_one_hundred = 100 - age
info = name + ", you will turn 100 in " + str(year_to_one_hundred ) + " years..."
print(info)

# Calcute the exact year the user turns 100
exact_year = 2024 + 100 - age
year = "Meaning you will turn 100 in the year " + str(exact_year) + "." 
print(year)
