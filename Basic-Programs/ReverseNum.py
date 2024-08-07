## using WHILE LOOP
num = int(input("Enter a Number that you want to Reverse:"))

reverse = 0
while num!=0:
    reverse = reverse*10 + num%10
    num = num//10

print("The reversed number is :", reverse)



## using string slicing
num1 = int(input("Enter a Number that you want to Reverse:"))
rev = int(str(num1)[::-1])
print("The reversed number is :", rev)



## using recursion
def reverse(num2):
    # Base case: if num2 is a single-digit number, return num2
    if num2 < 10:
        return num2
    else:
        # Recursive case: construct the reverse number
        num_length = len(str(num2)) - 1
        return (num2 % 10) * 10**num_length + reverse(num2 // 10)

# Input number from user
num2 = int(input("Please enter a number: "))
print("Before reverse your number is: %d" % num2)
rev = reverse(num2)
print("After reverse the number:", rev)
