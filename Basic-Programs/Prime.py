num = int(input("enter the number:"))
 
i, temp = 0, 0

for i in range(2, num//2):
    if num % i == 0:
         temp = 1
    break

if temp == 1:
     print("IT'S NOT PRIME NUMBER")

else:
     print("IT'S PRIME  NUMBER")
   

    
