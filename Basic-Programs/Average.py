# Using a Simple Loop and Input from the User

size = int(input("Enter the size of elements: "))
arr = []

for i in range(0, size):
    elmt = int(input("Enter the Number " + str(i+1) + ": "))
    arr.append(elmt)

avg = sum(arr) / size
print("The average of given numbers is: ", avg)

# using sum() and len() functions

elements = [10, 34, 67, 43, 89, 54, 33]

def calculate_average(elements):
    return sum(elements) / len(elements)

print("Average of number is: ", calculate_average(elements))