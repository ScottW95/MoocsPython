# Please write a function named double_items(numbers: list), which takes a list of integers as its argument.

# The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.

# An example of the function at work:

# if __name__ == "__main__":
#     numbers = [2, 4, 5, 3, 11, -4]
#     numbers_doubled = double_items(numbers)
#     print("original:", numbers)
#     print("doubled:", numbers_doubled)


def double_items(numbers: list):
    new_numbers = []

    for i in numbers:
        new_numbers.append(i*2)

    return new_numbers





# numbers = [1,2,3]
# numbers_doubled = double_items(numbers)

# print(numbers)
# print(numbers_doubled)