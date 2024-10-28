# Write your solution here
#Function that takes a list of strings
#and returns the list reversed with each
#string also reversed
def everything_reversed(my_list:list):

    #Initialize a variable for the length of the list
    length = len(my_list)

    #Initialize a variable for the new list
    new_list = []

    #Create a for loop that takes the last element in
    #the list, reverses it, appends it to new_list
    #and then moves on to the next item
    for i in my_list[length::-1]:
        reversed = i[::-1]
        new_list.append(reversed)

    #Return new_list to the function call
    return new_list


#Test
print(everything_reversed(["hello","wee","gee"]))
