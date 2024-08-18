#  finding maximum value
array = [7, 23, 5, 76, 345, 6]

maxVal = array[0]

for i in array:
    if i > maxVal:
        maxVal = i

print(f'The Maximum Value of given array is {maxVal}')

