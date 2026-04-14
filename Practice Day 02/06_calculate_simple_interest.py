principal = int(input("Enter the initial amount borrowed or invested: "))
interestRate = int(input("Enter the annual rate of interest: "))
time = int(input("Enter the duration for which the money is lent or invested, typically in years: "))

simple_interest = (principal*interestRate*time)/100

print(f"Your Simple Interest Rate will be {simple_interest}")