# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#  Enter 7, 2, bob, 10, and 4 and match the output below.

# Setting Largest and Smallest to none

Largest = None
Smallest = None

# creating a loop that will iterate through the user inputted values
while True:
    
    number = input ("Enter an integer: ")
# code to end the loop
    if number == "done":
        break
    try:
        inumber = int (number)
        snumber = int (number)
    except :
        print ("enter valid integer")
    if Smallest is None :
        Smallest = snumber
    elif snumber < Smallest:
        Smallest = snumber



    if Largest is None:
        Largest = inumber
    elif inumber > Largest:
        Largest = inumber
    

    
print ("Smallest = " +  str (Smallest) )
print ("Largest is : " + str (Largest))

