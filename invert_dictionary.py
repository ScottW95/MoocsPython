# Please write a function named invert
# (dictionary: dict), which takes a dictionary as 
# its argument. The dictionary should be inverted 
# in place so that values become keys and keys 
# become values.

def invert(dictionary: dict):
    length = len(dictionary)

    keys = list(dictionary.keys())
    print(keys)

    i = 0

    for index, item in enumerate(keys):

        popped = dictionary.pop(item)

        dictionary[popped] = item

    






# dictionary = {'scott':123,'Dustin':1234,'Marlene':12345}

# invert(dictionary)

# print(dictionary)