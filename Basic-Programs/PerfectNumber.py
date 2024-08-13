num = int(input("enter a number: "))

sum = 0

for i in range(1, (num//2)+ 1):
    remainder = num%i
    if remainder == 0:
        sum = sum + i

if sum == num:
    print("its perfect number")
else:
    print("its not perfect number")