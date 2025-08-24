# This final exercise in this part is a relatively 
# demanding problem solving task. It can be solved in 
# many different ways. Even though this current 
# section in the material covers tuples, tuples are 
# not necessarily the best way to go about solving 
# this.

# Please write a program which prints out a square of 
# letters as specified in the examples below. You may 
# assume there will be at most 26 layers.
import string

layers = int(input('Layers:'))

total_layers = (layers*2)-1

print(total_layers)

alpha = string.ascii_uppercase

layer_list = []

letter = alpha[layers-1]

middle_layer = []

for i in range(layers-1,-1,-1):
    middle_layer.append(alpha[i])

for i in range(len(middle_layer)-2,-1,-1):
    middle_layer.append(middle_layer[i])

str_middle_layer = ''.join(middle_layer)

print(str_middle_layer)

for i in range(layers,-1,-1):

    if i == (layers):
        layer_list.append(middle_layer)
    else:
        for j in range(layers)


    







    



