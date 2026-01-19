'''
1. Factorial Calculator (Two Ways)
Write TWO functions to calculate factorial of N:
factorial_iterative(n) - using a loop
factorial_recursive(n) - using recursion

Test both with n = 5, 7, 10

Sample Output:
Factorial of 5 (iterative): 120
Factorial of 5 (recursive): 120

'''
# factorial_iterative(n) - using a loop

def factorial_iterative(n):
    sum=1
    if n==0 | n==1:
        return 1
    for i in range(1,n+1):
        sum=sum*i
    print(sum)
userInput=int(input("Enter N:"))
factorial_iterative(userInput)

# factorial_recursive(n) - using recursion

def factorial_recursive(n):
    if n==0 | n==1:
        return 1
    return n*factorial_recursive(n-1)
userInput=int(input("Enter Number:"))
print(f'factorial for {userInput } ans :{factorial_recursive(userInput)}')