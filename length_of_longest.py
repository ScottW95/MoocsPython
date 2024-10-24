# Write your solution here
def length_of_longest(my_list:list):

    longest = ""

    for i in my_list:
        if len(i) > len(longest):
            longest = i
        else:
            continue

    return len(longest)

#Test: Should print the length of the longest word, gibberish (9)
print(length_of_longest(["hello","bye","gibberish"]))
