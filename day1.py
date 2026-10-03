#tip calculator
# bill_amount=float(input("Enter the bill amount:"))
# tip_amount=bill_amount*0.01
# print("The tip amount is:",tip_amount)
# total_amount=bill_amount+tip_amount
# print("total Bill is:",total_amount)
# n=int(input("Enter the number of people to split the bill:"))
# split_amount=total_amount/n
# print("Each person should pay:",split_amount)

#swapping of two numbers
# a=input("Enter the first number:")
# b=input("Enter the second number:")
# a,b=b,a
# print("After swapping a:",a)
# print("After swapping b:",b)    

#convert Celsius to Fahrenheit
# temp=float(input("Enter the temperature in Celsius:"))
# fahrenheit=(temp*1.8)+32
# print("The temperature in Fahrenheit is:",fahrenheit,"°F")

#simple greeting
# name=input("Enter your name:")
# age=int(input("Enter your age:"))
# print(f"Hello {name},you are {age} years old.")

#Area and perimeter of a rectangle
# length=float(input("Enter the length of the rectangle:"))
# width=float(input("Enter the width of the rectangle:"))
# area=length*width
# perimeter=2*(length+width)
# print("The area of the rectangle is:",area) 
# print("The perimeter of the rectangle is:",perimeter) 



#Number Guessing Game v1: computer picks a random number (random module), user guesses once,
#program says right or wrong. (use if/else)


import random
import pyfiglet #need to install pyfiglet module using pip install pyfiglet

def number_guessing_game():
    attempts=0
    max_attempts=5
    secret_number=random.randint(1,100)
    print("Welcome to the Number Guessing Game!")
    print("You have", max_attempts, "chances to guess the number.")
    while attempts<max_attempts:
        try:
            guess=int(input("Guess a number between 1 and 100:"))
            if guess<1 or guess>100:
                print("Please enter a valid number between 1 and 100.")
                continue
            attempts += 1
            print("You have",max_attempts-attempts,"chances left.")
            if guess==secret_number:
                print(f"congratulations! you still had {max_attempts-attempts} attempts left.")
                print("You are right! the number is:\n",pyfiglet.figlet_format(str(secret_number)))
                break
            elif guess > secret_number:
                print("Your guess is too high.")    
            elif guess < secret_number:
                print("Your guess is too low.")
        except ValueError:
            print("Please enter digits only.")
    else:
        print("You have used all your chances. The number was:",secret_number)


while True:
    number_guessing_game()
    play_again=input("Do you want to play again?(y/n):").lower()
    if play_again=="n":
        print("Thanks for playing!")
        break
    else:
        print("Starting a new game...")
        