def fact(n):  
   if n == 1:  
       return n  
   else:  
       return n*fact(n-1) #recursion 

num = int(input("Enter a whole number to find Factorial: "))  
if num < 0:  
   print("Factorial can't be calculated for negative number")  
elif num == 0:  
   print("Factorial of 0 is 1")  
else:  
   print("Factorial of",num,"is",fact(num))  
