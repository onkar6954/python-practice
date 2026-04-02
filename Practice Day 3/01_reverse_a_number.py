num = input("Enter a number: ")
print("Your Number:", num)
count = ""
for i in range(len(num) - 1, -1, -1):
    count+=num[i]
print("Reversed Number:",count)