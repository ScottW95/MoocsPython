# Write your solution here

list = [1,2,3,4,5]

newvalue = 0

while newvalue != -1:

    index = int(input("Enter a index for new number:"))
    newvalue = int(input("Enter a new value:"))

    if newvalue == -1:
        break
    else:
        list[index] = newvalue
        print(list)
        continue
