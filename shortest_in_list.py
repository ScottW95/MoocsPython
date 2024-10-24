# Write your solution here
def shortest(my_list:list):
    short = ""

    for i in my_list:
        if len(i) < len(short) or len(short)==0:
            short = i
        else:
            continue
    
    return short

#Test: Will return shortest string in list
print(shortest(["hello","we","they","puppy"]))
