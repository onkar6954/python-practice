# Using .loc[]
# Select "Name" and "Salary" where Age > 30.

import pandas as pd

df = pd.read_excel('python-practice\Practice Day 11 pandas\SampleSuperstore.xlsx')

print(df.loc[df["Sales"]>100,["Quantity","Profit","Sales"]])
# print(df)