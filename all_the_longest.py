# Write your solution here
def all_the_longest(my_list:list):
    longest = []

    for i in my_list:
        if len(longest)<1 or len(i) > len(longest[0]):
            longest.clear()
            longest.append(i)
        elif len(i) == len(longest[0]):
            longest.append(i)
        else:
            continue

    if len(longest)==0:
        longest = "Please enter a list of strings"

    return longest

#Tests
#Will return error statement
print(all_the_longest([]))
#Will return x
print(all_the_longest(["x"]))
#Will return both puppies and kittens
print(all_the_longest(["test","puppies","kittens","book"]))
#Will return textbook
print(all_the_longest(["test","puppies","kittens","textbook"]))
