string = input("Enter a String: ")
count = 0
for i in range(0,len(string)):
  if(string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u'):
    count+=1

if(count>0):
  print(f"{count} vowels are present")
else:
  print("0 vowels are present")