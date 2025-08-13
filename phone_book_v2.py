# Please write an improved version of the phone book 
# application. Each entry should now accommodate 
# multiple phone numbers. The application should 
# work otherwise exactly as above, but this time 
# all numbers attached to a name should be printed.
phone_book = {}

while True:
    choice = int(input('command(1 search, 2 add, 3 quit):'))


    if choice == 1:
        name = input("Name: ")

        if name in phone_book:
            for i in phone_book[name]:
                print(i)
        else:
            print('no number')
    elif choice == 2:
        name = input('Name: ')

        number = input('Number: ')

        if name not in phone_book:
            phone_book[name] = []
            phone_book[name].append(number)
        else:
            phone_book[name].append(number)

        print('ok!')
    elif choice == 3:
        print('quitting...')
        break
    else:
        print('Not a valid choice. Try again')