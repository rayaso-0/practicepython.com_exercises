# --------------------
# Python Exercise Number 3
# Exercise: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that prints out all the elements of the list that are less than 5.
# Date: Mon Sep 9 2024
# --------------------

# create list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

# for function that checks each number in the list and compares it to 5
for i in a:
    if i < 5:
        b.append(i)

print (b)

# EXTRAS

#Create lists
numbers = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11]
lessFnums = []
lessNnums =[]
#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
for num in numbers:
    if num < 5: #Compare numbers in list against 5
        lessFnums.append(num) #Add numbers that are less than 5 to our list
        lessFnums.sort() # Sort list
#Print the List
print(lessFnums)
print()

# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
num = int(input("Enter a number: ")) #Get a number from user
for n in numbers:
    if n < num: #Compare user number against numbers in list
        lessNnums.append(n) #Add numbers that are less than user name to our list
        lessNnums.sort() # Sort list
#Print the list
print(lessNnums)