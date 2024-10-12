# Write your solution here

mylist = []

print(f"The list is now {mylist}")

i = 0


while True:

    action = input("Add, remove, or exit:")

    if action == "d":
        if not mylist:
            mylist.append(1)
            print(f"The list is now {mylist}")
        else:
            mylist.append(mylist[i]+1)
            i +=1
            print(f"The list is now {mylist}")
    elif action == "r":
        mylist.pop(i)
        print(f"The list is now {mylist}")
        if i == 0:
            continue
        else:
            i -=1
    else:
        print("Bye!")
        break
