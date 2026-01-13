'''
3. Word Frequency Counter
Write a program that:
Reads text from a file called "sample.txt"
Counts how many times each word appears
Stores results in a dictionary
Prints top 5 most frequent words
Handles FileNotFoundError gracefully


Hint: Use .split() and dictionary


Sample Output:
Word frequencies:
'the': 15 times
'and': 12 times
'python': 8 times
'is': 7 times
'for': 5 times
'''


#read the file 

try:
    file = open("sample.txt", "r")
    content = file.read()
    split =content.split(' ')
    # print(split)

    # dist={}
    # for i in split:
    #     word=i.lower()
    #     count=0
    #     cal=0
    #     for i in range(len(word)):
    #         count+=1
    #     cal=count
    #     dist[word]=cal
    # # print(dist)

    #how many times word frequent
    countword=0
    HowMany={}
    for i in split:
        separete_word=i.lower()
        HowMany[separete_word] =HowMany.get(separete_word,0)+1
    # print(HowMany)
            
    # in the word which are frequent times that print 5 word and frequ

    import operator
    res = dict(sorted(HowMany.items(), key=operator.itemgetter(1)))
    print("sorted item ",res)

    i = len(HowMany) - 1
    count=0
    while i >= 0:
        count=count+1
        if(count==5):
            break
        print("key from last 5 ",res.keys())
        i -= 1
    print()
except FileNotFoundError:
    print(f"Error: The file '{file.name}' was not found.")   

        
finally:
    file.close()
'''
import operator

a = {"Gfg": 5, "is": 7, "Best": 2, "for": 9, "geeks": 8}
res = dict(sorted(a.items(), key=operator.itemgetter(1)))
print(res)
'''