binary_str = input("enter the Binary Value: ")

Decimal = 0
power = 0

for digit in binary_str[::-1]:
    Decimal += int(digit) * (2 ** power)
    power += 1

print(f'The Decimal Number of {binary_str} is {Decimal}')