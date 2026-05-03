""" Write a Python program to print "Hello World"."""
# print("Hello World")

""" Write a Python program to do arithmetical operations addition and division."""
# Addition
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))
# print(num1 + num2)

# Division
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))
# if(num1==0 or num2==0):
#   print("Cannot divide by zero")
# else:
#   print(num1/num2)

""" Write a Python program to find the area of a triangle."""
# base = int(input("Enter base: "))
# height = int(input("Enter height: "))
# areaOfTriangle = (1/2)*base*height
# print(f"Area of Triangle with base={base} and height={height} is {areaOfTriangle}")

""" Write a Python program to swap two variables."""
# var1 = input("Enter first variable: ")
# var2 = input("Enter second variable: ")
# print("var1 =",var1)
# print("var2 =",var2)
# temp = var1
# var1 = var2
# var2 = temp
# print("var1 =",var1)
# print("var2 =",var2)

""" Write a Python program to convert kilometers to miles."""
# km = int(input("Enter kilometers: "))
# miles = km * 0.621371
# print(f"{km}km in miles is {miles}miles")

""" Write a Python program to convert Celsius to Fahrenheit"""
# c = int(input("Enter temp in celsius: "))
# f = int(c*(9/5)+32)
# print(f"{c}°C in fahrenheit is {f}°f")

""" Write a Python program to display calendar."""
# import calendar

# year = int(input("Enter year: "))
# month = int(input("Enter month: "))

# cal = calendar.month(year,month)
# print(cal)

""" Write a Python program to solve quadratic equation."""
# import cmath

# a = float(input("Enter value 'a' Note: a must be greater then 0: "))
# b = float(input("Enter value 'b': "))
# c = float(input("Enter value 'b': "))

# d = (b**2)-(4*a*c)

# root1 = (-b+cmath.sqrt(d))/(2*a)
# root2 = (-b-cmath.sqrt(d))/(2*a)

# print(root1)
# print(root2)

""" Write a Python program to swap two variables without temp variable."""
# a=6
# b=7
# a,b = b,a
# print("a=",a)
# print("b=",b)

""" Write a Python Program to Check if a Number is Positive, Negative or Zero."""
# num = int(input("Enter a number: "))
# if(num>0):
#   print("Entered number is Positive")
# elif(num==0):
#   print("Entered number is Zero")
# else:
#   print("Entered number is Negative")