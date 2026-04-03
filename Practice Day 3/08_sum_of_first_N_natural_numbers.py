num = int(input("Enter a number: "))
count=0
if(num<1):
    print("Enter a positive number.")
else:
    for i in range(0,num+1):
        count+=i
    print(count)