num = int(input("Enter the number:"))

#declaring
sum = 0
count = len(str(num))
#assigning temp to store num
temp = num

#loop and logic
while temp > 0:
    digit = temp % 10
    sum += digit** count
    temp //= 10

# condition
if num == sum:
    print("its Armstrong!")
else:
    print("Its not Armstrong.")