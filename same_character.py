# Write your solution here

def same_chars(string,a,b):

    if a >= len(string) or b >= len(string):
        return(False)

    a = string[a]
    b = string[b]

    if a == b:
        return(True)
    else:
        return (False)




# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 7))
