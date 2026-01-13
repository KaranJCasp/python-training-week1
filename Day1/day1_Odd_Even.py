'''
1. Even or Odd Checker
Write a program that:
Takes a number as input from user
Checks if it's even or odd
Prints appropriate message
Sample Output:
Enter a number: 7
7 is an Odd number

'''


userInput=int(input("Enter a number:"))

if userInput<0:
    print(f'{userInput} number is negative')
else:
    res= "Even" if userInput %2==0 else "Odd"

print(f"{userInput} is an {res} number")