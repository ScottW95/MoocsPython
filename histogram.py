# Please write a function named histogram, 
# which takes a string as its argument. 
# The function should print out a histogram 
# representing the number of times each letter 
# occurs in the string. Each occurrence of a letter 
# should be represented by a star on the specific 
# line for that letter.


def histogram(string:str):
    letters = {}

    length = len(string)

    for i in range(0,length):
        letter = string[i]

        if letter not in letters:
            letters[letter] = 0

        letters[letter] += 1

    for key,value in letters.items():
        print(f'{key} {'*' * value}') 

# print(histogram('hello'))

    