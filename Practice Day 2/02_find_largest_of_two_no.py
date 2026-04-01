num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if(num1>num2):
  print(f"{num1} is Greater than {num2}")
elif(num2>num1):
  print(f"{num2} is Greater than {num1}")
else:
  print(f"{num1} and {num2} both are equal")