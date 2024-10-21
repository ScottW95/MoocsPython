# Write your solution here

def distinct_numbers(my_list:list):

    new_list = []

    for i in my_list:

        if i not in new_list:
            new_list.append(i)
        else:
            continue

    new_list.sort()

    return new_list

my_list = [1,4,2,3,4,52,3,4,5]

print(distinct_numbers(my_list))
