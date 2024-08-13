# Python Program to Check number representation is in Binary

num = int(input("Enter the number: "))

while(num > 0):
    i = num % 10 #remainder should be 0 or 1
    if i != 0 and i != 1:
        print("It's not a binary")
        break
    num //= 10
    if num == 0:
        print("num is binary")

