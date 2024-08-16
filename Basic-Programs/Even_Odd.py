# using modulus operator

num1 = int(input("enter a number: "))
if num1 % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#using lambda function

check_number = lambda num : "Even" if num % 2 == 0 else "Odd"
number = int(input("Enter a number: "))
result = check_number(number)
print(f"The Number {number} is {result}")