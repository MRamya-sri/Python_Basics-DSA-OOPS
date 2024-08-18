import array as arr 

# Creating an array of integers
my_array = arr.array('i', [23, 65, 99, 21, 34, 63])

# Accessing elements
print(my_array[3])

# modify elements
my_array[1] = 20
print(my_array)

# Iterating
for num in my_array:
    print(num)