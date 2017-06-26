# This program takes a random number between 1-20 and grants the user 5 guesses to get it.
import random  # importing module "random"

guessesTaken = 0  # assigning 0 to variable "guessesTaken"

print('Hello! What is your name?')  # question for the desired input
myName = input()  # storing the input into variable "myName"

number = random.randint(1, 20)  # assigning a random number between 1 and 20 to variable "number"
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # informational string for the user

while guessesTaken < 6:  # a loop that executes until guessesTaken reaches 6
    print('Take a guess.')  # prints request for a guess
    guess = input()  # assigns the user input to variable "guess"
    guess = int(guess)  # converts the variable's value to an integer

    guessesTaken += 1  # adds 1 to variable guessesTaken

    if guess < number:  # # condition for a low guess
        print('Your guess is too low.')  # tells the user if the guess is lower the the original one

    if guess > number:  # condition for a high guess
        print('Your guess is too high.')  # tells the user if the guess is higher the the original one

    if guess == number:  # condition for the right guess
        break  # breaks the loop if the guess is right

if guess == number:  # condition for the right guess
    guessesTaken = str(guessesTaken)  # coverts guessesTaken to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # tells the user how many guesses it took to guess the right number

if guess != number:  # condition for no right guesses
    number = str(number)  # converts the original number to a string
    print('Nope. The number I was thinking of was ' + number)   # tells the user the original number
