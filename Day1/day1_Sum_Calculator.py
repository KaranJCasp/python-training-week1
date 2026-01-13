'''
2. Sum Calculator
Write a program that:
Takes a number N as input
Calculates and prints sum of first N natural numbers


Sample Output:
Enter N: 5
Sum of first 5 numbers is: 15
'''

userInput=int(input("Enter N:"))
sum=0

if userInput<0:
    print(f'{userInput} number is negative')
else:
    for i in range(1,userInput+1):
        sum+=i


print(f"Sum of first {userInput} numbers is: {sum}")