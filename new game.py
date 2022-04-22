#import the random library
import random

#Declare the start and end point of your range of numbers
computervalue = random.randrange(1,10)

#Declare your variables
playervalue = int(input("Guess a number between 1 & 10"))
numberoftries = 0
trylimit = 3

#Using if statements and for loops
for x in range(2):
 if playervalue == computervalue:
    print("You got it right!")
 else:
    print("Oops you are wrong, Better luck next time")
print("Out of tries")

#while loop & if loops
for numberoftries in range(2):
 while playervalue != computervalue:
    numberoftries += numberoftries
    playervalue = int(input("Oops!, try again"))
print("Out of tries")



print("You have won")
