n = int(input("enter a number for fibonacci series:"))

first = 0
second = 1

print("Fibonacci series are : ")

for i in range(0, n):
    if i<= 1:
        result = i
    
    else:
        result = first + second
        first = second
        second = result

print(result) 