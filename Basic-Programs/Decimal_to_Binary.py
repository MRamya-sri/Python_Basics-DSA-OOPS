# Decimal to Binary

Decimal = int(input("Enter the Decimal: ")) #13

temp = Decimal

binary = " "

while temp>0:
    remainder = temp % 2
    binary = str(remainder) + binary
    temp = temp // 2

print(f"The Binary number of {Decimal} is {binary}")
