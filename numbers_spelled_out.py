# Please write a function named dict_of_numbers(), 
# which returns a new dictionary. The dictionary 
# should have the numbers from 0 to 99 as its keys. 
# The value attached to each key should be the number 
# spelled out in words. Please have a look at the 
# example below:

def dict_of_numbers():
    numbers = {0:'zero',1:'one',2:'two',
               3:'three',4:'four',5:'five',
               6:'six',7:'seven',8:'eight',
               9:'nine',10:'ten',11:'eleven',
               12:'twelve',13:'thirteen',15:'fifteen',18:'eighteen'}

    single_digits = [1,2,3,4,5,6,7,8,9]

    tens = ['twenty','thirty','forty',
            'fifty','sixty','seventy','eighty','ninety']

    tens_place = 0

    subtractor = 21

    for i in range(14,100):
        if 14 <= i <= 19 and i != 15 and i != 18:
            dig_index = (i - 11)

            numbers[i] = f'{numbers[single_digits[dig_index]]}teen'
        elif 20 <= i <= 99:
            if i % 10 == 0:
                numbers[i]=tens[tens_place]
            else:
                numbers[i]=f'{tens[tens_place]}-{numbers[single_digits[i-subtractor]]}'

                if abs(i)% 10 == 9:
                    tens_place += 1
                    subtractor += 10



    return numbers



# numbers = dict_of_numbers()

# print(numbers)
        
