# Select multiple columns

import pandas as pd

df = pd.read_excel('python-practice\Practice Day 11 pandas\SampleSuperstore.xlsx')

# print(pd.DataFrame(df.columns))

print(df[["Customer ID","City","Category"]])