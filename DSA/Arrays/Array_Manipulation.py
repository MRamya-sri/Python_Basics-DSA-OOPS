import array as arr 

my_array = arr.array('i', [89, 7, 56, 76, 9])

# append an element
my_array.append(32)
print(my_array)

# insert an element at specific index
my_array.insert(2, 87)
print(my_array)

# remove an element
my_array.remove(56)
print(my_array)