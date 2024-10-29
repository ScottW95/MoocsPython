# Write your solution here
def no_vowels(word:str):
    vowels = 'aeiou'

    for x in vowels:
        word = word.replace(x,"")

    return word


#Test
print(no_vowels('hello'))
