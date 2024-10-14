# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def reverse(word):
    word2 = ""
    x=0
    for i in word:
        word2 += (word[(len(word))-1-x])
        x+=1

    return word2


def palindromes(word,word2):
    if word2 == word:
        return True
    else:
        return False

    


while True:
    word = input("Enter a palindrome: ")
    word2 = reverse(word)

    if palindromes(word2,word) == True:
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
        continue
