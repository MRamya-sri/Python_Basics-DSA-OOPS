n = int(input("Enter the number for fibonacci: "))

first = 0
second = 1

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
    
print("fibonacci series are : ")

for i in range(0, n):
    print(fibonacci(i))