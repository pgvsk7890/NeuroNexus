#Functions for basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y  
    else:
        raise ValueError("Division by zero is not allowed.")
def power(x, y):
    return x ** y

#taking inputs from users
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
print("Choose option for operation:")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power")
option=int(input("Choose option(1/2/3/4/5):"))
if option==1:
    print(add(x,y))
if option==2:
    print(subtract(x,y))
if option==3:
    print(multiply(x,y))
if option==4:
    print(divide(x,y))
if option==5:
    print(power(x,y))
