n = int(input("enter a number: "))

reverse = 0
temp = n

while temp != 0:
    reverse = reverse*10 + temp % 10
    temp //= 10

if reverse == n:
    print("Its palindrome")
else:
    print("Its not palindrome")
