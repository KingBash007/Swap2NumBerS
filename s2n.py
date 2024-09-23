# Program to swap two numbers without using third variable
def swap1(a,b):
    # Code to swap a and b
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swapping: a =",a ,"b =",b )
swap1(1,2)