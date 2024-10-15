# Write your solution here

#Create function that returns the even numbers from a list of integers
def even_numbers(my_list:list):
    new = []

    for i in my_list:
        if i%2 == 0:
            new.append(i)
        else:
            continue

    return new


#Test
print(even_numbers([2,3,4,5,6]))
