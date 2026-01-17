'''
Write a program that:
Creates a list of 10 numbers (user input)
Prints: maximum, minimum, average, sum
Prints all even numbers from the list
Prints the list in reverse order
Use list methods and built-in functions.
'''

def List_Operation():
    li=[]

    for i in range(1,4):
        userinput=input("Enter Number :")
        if(userinput==''):
            print('user must enter the number')
            continue
        li.append(int(userinput))
    
    # maximum
    max=li[0] 
    min=li[0]
    avg=0
    sum=0
    for i in range(1,len(li)):
        sum+=li[i]
        if max<li[i]:
            max=li[i]
        elif max!=min | min >li[i] :
            min=li[i]
    avg=sum/len(li)
    print({"Maximum":max,"Minimum":min,"avg":avg,"sum":sum})

    #print all even number
    print("Even numbers in the list:",end=" ")
    even_numbers = []
    for num in li:
        if num % 2 == 0:
            even_numbers.append(num)
    
    if even_numbers:
        print(even_numbers)
    else:
        print("There are no even numbers in the list.")


    #print the list in reverse order 
    print("list in reverse order ",end=" ")
    i = len(li) - 1
    while i >= 0:
        print(li[i],end=" ")
        i -= 1
    print()
List_Operation()
