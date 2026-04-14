# Print all column names of df.

import pandas as pd

df = pd.read_excel('python-practice\Practice Day 11 pandas\SampleSuperstore.xlsx')

# print(df.columns)

df2 = pd.DataFrame(df.columns)
print(df2)