# Python program to swap two number without using third variable

a = int(input("please give first number a: "))
b = int(input("please give second number b: "))

a = a-b
b = a+b
a = b-a

print("After swapping")
print("Value of a is : ", a)
print("value of b is:", b)

# using third variable

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))

temp = num1 
num1 = num2
num2 = temp

print("After swapping")
print("Value of num1 is : ", num1)
print("value of num2 is:", num2)


