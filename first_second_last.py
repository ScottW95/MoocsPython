# Write your solution here

def first_word(string):
    index = string.index(" ")
    return (string[:index])


def second_word(string):
    index1 = string.find(" ")
    index2 = string.find(" ",index1+1)

    if index2 != (-1):
        return(string[index1+1:index2])
    else:
        return(string[index1+1:])


def last_word(string):
    index = string.rfind(" ")

    return(string[index+1:])




# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word("happily ever after"))
    print(last_word(sentence))
