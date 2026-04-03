string = input("Enter a String: ")
rstring = ""

for i in range(len(string)-1,-1,-1):
  rstring+=string[i]

if(string==rstring):
  print("It's a Palindrome")
else:
  print("It's not a Palindrome")