# Write your solution here
N = int(input("Type a positive integer:"))

for i in range(-(N),N+1):
    if i == 0:
        continue
    else:
        print(i)
