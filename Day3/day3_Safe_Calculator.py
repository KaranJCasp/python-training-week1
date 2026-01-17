'''
1. Safe Calculator
Write a calculator that:
Takes two numbers and an operator (+, -, *, /) as input
Handles these exceptions:
ValueError (if user enters non-numeric input)
ZeroDivisionError (if dividing by zero)
Prints appropriate error messages
Keeps asking until user types 'quit'

Sample Output:
Enter first number: abc
Error: Please enter a valid number!
Enter first number: 10
Enter second number: 0
Enter operator: /
Error: Cannot divide by zero!

'''
def cal(userNum1,userNum2,userOperator):
    if userOperator == '+':
        return userNum1 + userNum2
    elif userOperator == '-':
        return userNum1 - userNum2
    elif userOperator == '*':
        return userNum1 * userNum2
    elif userOperator == '/':
        # if userNum2 == 0:
        #     return "Error: Cannot divide by zero"
        return userNum1 / userNum2
    else:
        return "Error: Invalid operator entered"

while (True):
    try:
        userNum1=int(input("Enter First Number : "))
        userNum2=int(input("Enter Second Number : "))
        userOperator = input("Enter Operator (+, -, *, /) or 'q' to quit: ")

        if userOperator.lower() == 'q':
                print("Exiting calculator.")
                break
        result = cal(userNum1, userNum2, userOperator)
        print(f"Result: {result}\n")
    except ValueError:
        print('Error: Please enter a valid number!')
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")



    



    


