'''
3. Number Guessing Game
Write a program that:
Generates a random number between 1 and 100 
Asks user to guess the number
Gives hints: "Too high!" or "Too low!"
Counts the number of attempts
Ends when user guesses correctly
Bonus: Limit to 7 attempts

Sample Output:
Guess the number (1-100): 50
Too high! Try again.
Guess the number (1-100): 25
Too low! Try again.
Guess the number (1-100): 37
Congratulations! You guessed it in 3 attempts!

'''
import random

attempt = 0
# Generates a random number between 1 and 3
randomNumber = random.randint(1, 100)
limit=7
while True:
    userInput = int(input("Enter N: "))
    attempt += 1
    if attempt==7:
        break
    elif userInput<0:
        print(f'user input is neagtive ')
    elif userInput==0:
        print('number is zero')
    
    elif userInput == randomNumber:
        print(f"Congratulations! You guessed it in {attempt} attempts!")
        break  
    elif randomNumber > userInput:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


