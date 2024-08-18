# Finding Minimum Value

array = [7, 23, 5, 76, 345, 6]

minVal = array[0]

for i in array:
    if i < minVal:
        minVal = i

print(f'The Minimum Value of given array is {minVal}')