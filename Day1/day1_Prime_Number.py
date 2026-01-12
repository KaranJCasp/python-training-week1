'''

4. Prime Number Analyzer
Write a program that:
Takes a number N as input
Finds and prints ALL prime numbers from 2 to N
Also prints the COUNT of prime numbers found
Also prints the SUM of all prime numbers found

Sample Output:
Enter N: 20
Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19
Count: 8
Sum: 77

'''

userInput=int(input("Enter N:"))

# create function for prime number check
def IsPrime(userInput):
    if userInput<2:
        return False
    for i in range(2,userInput):
        if userInput%i==0:
            return False
    return True

count=0
sum=0
print(f"Prime numbers:",end=' ')
for i in range(2,userInput+1):

    if(IsPrime(i)):
        count+=1
        print(i,end=" ")
        sum+=i
        
print(f"Count:{count}")
print(f"Sum:{sum}")

