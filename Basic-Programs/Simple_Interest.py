#taking the values of principal, rate of interest and time from the user
principal = int(input("Enter the principal amount: "))  
rate = int(input("Enter the rate of interest: "))  
time = int(input("Enter the time of interest in year: "))  
#using the input values calculate simple interest
simpleInterest = (principal * rate * time) / 100
print(f'Simple Interest : {simpleInterest}')
