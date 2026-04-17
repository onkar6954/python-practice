# Multiple Conditions
# Profit > 100 AND Sales > 100.

import pandas as pd

df = pd.read_excel('python-practice\Practice Day 11 pandas\SampleSuperstore.xlsx')

print(df[(df["Profit"]>100) & (df["Sales"]>100)])