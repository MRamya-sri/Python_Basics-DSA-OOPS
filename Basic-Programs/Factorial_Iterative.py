
num = int(input("enter the number to calculate factorial: "))

factorial = 1

if num < 0:
    print("Factorial can't be calculated for negative numbers")

elif num == 0:
    print("Factorial of 0 is 1")

else:
    for i in range(1, num+1):
        factorial = factorial*i
    print("Factorial of ", num , "is", factorial)