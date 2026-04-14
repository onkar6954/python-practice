while(True):
  print()
  print()
  print("👇 Calculator (CLI) 👇")
  print("Enter (1) for Addition")
  print("Enter (2) for Substraction")
  print("Enter (3) for Multiplication")
  print("Enter (4) for Division")
  print("Enter (5) to print Natural Numbers till N")
  print("Enter (6) for Square")
  print("Enter (7) for Cube")
  print("Enter (8) for exit")

  inp = int(input("Enter any option: "))
  if(inp == 1):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Addition of {num1} and {num2} is {num1+num2}")
  elif(inp==2):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Substraction of {num1} and {num2} is {num1-num2}")
  elif(inp==3):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Multiplication of {num1} and {num2} is {num1*num2}")
  elif(inp==4):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Division of {num1} and {num2} is {num1/num2}")
  elif(inp==5):
    num1 = int(input("Enter a number: "))
    for i in range(1,num1+1):
      print(i," ",end='')
  elif(inp==6):
    num1 = int(input("Enter a number: "))
    print(f"Square of {num1} is {num1**2}")
  elif(inp==7):
    num1 = int(input("Enter a number: "))
    print(f"Cube of {num1} is {num1**3}")
  elif(inp==8):
    break
  else:
    print("Enter Options from 1 to 8")