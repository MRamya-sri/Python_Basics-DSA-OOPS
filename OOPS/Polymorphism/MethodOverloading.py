# Method Overloading:

# Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. These methods are called overloaded methods and this is called method overloading. 

# Like other languages (for example, method overloading in C++) do, python does not support method overloading by default. But there are different ways to achieve method overloading in Python. 

# The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method. 

# First product method.
# Takes two argument and print their
# product
def product(a, b):
    p = a * b
    print(p)

# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b*c
    print(p)

# Uncommenting the below line shows an error
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)



# Thus, to overcome the above problem we can use different ways to achieve the method overloading.

# Method 1 (Efficient One):
# By Using Multiple Dispatch Decorator 
# Multiple Dispatch Decorator Can be installed by: 
# pip install multipledispatch

from multipledispatch import dispatch

#passing two parameters
@dispatch(int, int)
def product(first, second):
    result= first*second
    print(result)

#passing three parameter
@dispatch(float, float, int)
def product(first, second, third):
    result= first*second*third
    print(result)

# calling methods with different parameters
product(4,6)
product(78.2, 8.5, 91)
 