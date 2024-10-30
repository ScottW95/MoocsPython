# Write your solution here

def no_shouting(list:list):
    new_list=[]

    for i in list:

        if i.isupper() == False:
            new_list.append(i)
        else:
            continue

    return new_list

#Test
print(no_shouting(["hello","HELLO","BYE","no"]))
