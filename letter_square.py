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


while True:
    try:
        layers = int(input('Layers:'))
    except ValueError:
        print('Invalid input. Please enter an integer between 1 and 26')
        continue

    if layers > 26 or layers < 1:
        print("You're entry is out of bounds, please enter again")
        continue
    else:
        break
    

total_layers = (layers*2)-1

alpha = string.ascii_uppercase

layer_list = []

letter = alpha[layers-1]

first_layer = []

for i in range(0,layers):
    if i == 0:
        for j in range(0,total_layers):
            first_layer.append(letter)
        
        layer_list.append(first_layer)
    else:
        next_letter = alpha[(layers-1)-i]

        next_layer = layer_list[i-1].copy()

        for j in range(i,((total_layers-i))):

            next_layer[j] = next_letter

        layer_list.append(next_layer)

for i in range(layers-2,-1,-1):
    copy_layer = layer_list[i].copy()

    layer_list.append(copy_layer)
            

for inex,layer in enumerate(layer_list):
    print(''.join(layer))





    







    



