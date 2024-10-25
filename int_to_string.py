# Write your solution here
def formatted(my_list:list):

    new_list=[]

    for i in my_list:
        number = f"{i:.2f}"

        new_list.append(number)

    return(new_list)

#Test
print(formatted([1.32343,123.134243,12312.435]))
