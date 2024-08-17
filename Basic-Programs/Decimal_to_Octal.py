Decimal = int(input("Enter the Decimal: "))  # 13

temp = Decimal

octal = ""

while temp > 0:
    remainder = temp % 8
    octal = str(remainder) + octal
    temp = temp // 8

print(f"The Octal number of {Decimal} is {octal}")