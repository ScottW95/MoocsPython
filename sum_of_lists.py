# Write your solution here

#Function that sums list items by index and returns them
def list_sum(my_list: list,other_list:list):
    total = []

    for i,x in zip(my_list,other_list):
        total.append(i + x)

    return total


#test
print(list_sum([1,2,3],[100,200,300]))
