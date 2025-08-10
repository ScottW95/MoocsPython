phone_book = {}

while True:
    choice = int(input('command(1 search, 2 add, 3 quit):'))


    if choice == 1:
        name = input("Name: ")

        if name in phone_book:
            print (phone_book[name])
        else:
            print('no number')
    elif choice == 2:
        name = input('Name: ')

        number = input('Number: ')

        phone_book[name] = 0

        phone_book[name] = number

        print('ok!')
    elif choice == 3:
        print('quitting...')
        break
    else:
        print('Not a valid choice. Try again')
