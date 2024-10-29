# Write your solution here
def most_common_character(word:str):
    number = 0

    for i in word:
        amount = word.count(i)

        if amount > number:
            number = amount
            letter = i

    return letter


#Test
print(most_common_character("aaabcddddeeeee"))
