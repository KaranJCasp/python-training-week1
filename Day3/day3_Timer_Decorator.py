'''3. Timer Decorator
Write a decorator called 'timer' that:
Measures how long a function takes to execute
Prints the execution time
Works with any function

Test it with:
A function that calculates factorial of 1000
A function that generates 100000 random numbers

Sample Output:
Function 'calculate_factorial' took 0.0023 seconds
'''
import random 
import time 

def timer_decorator(func): 
    def wrapper(*args, **kwargs): 
        start_time = time.time() 
        result = func(*args, **kwargs) 
        end_time = time.time() 
        print(f"'{func.__name__}' took {end_time - start_time:.4f} seconds") 
        return result 
    return wrapper 

@timer_decorator 
def Calculate_factorial(num): 
    if num == 0 or num == 1:
        return 1
    sum=1
    for i in range(1,num):
        sum=sum*i
    return sum

def GenerateNum(userNum_val):
    li = random.sample(range(1, userNum_val + 1), userNum_val)
    return li

#for Factorial
num = int(input("Enter number for factorial: ")) 
print_factorial = Calculate_factorial(num) 
print(f'Factorial of number {num}: {print_factorial}')

#for Random number genrate
userNum = int(input("Enter number for random number: "))

print_RandomNumber = GenerateNum(userNum)

print(f"Generated random number list: {print_RandomNumber}")





# def generate_random_num(count):

#     return [random.random() for _ in range(count)]

# list_of_random_numbers = generate_random_num(100000)
# print(list_of_random_numbers)