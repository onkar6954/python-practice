# Select column "Customer Name".

import pandas as pd

df = pd.read_excel('python-practice\Practice Day 11 pandas\SampleSuperstore.xlsx')

print(df['Customer Name'].head(15))