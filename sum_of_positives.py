# Write your solution here

def sum_of_positives(my_list:list):

    su = 0

    for item in my_list:
        if item > 0:
            su = su + item
        else:
            continue
    
    return su
