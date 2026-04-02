num = input("Enter a number: ")
rnum = ""

for i in range(len(num)-1,-1,-1):
    rnum+=num[i]

if(num==rnum):
    print("It's a Palindrome num")
else:
    print("It's not a Palindrome num")
    
