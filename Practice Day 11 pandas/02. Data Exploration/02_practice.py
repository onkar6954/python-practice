# Show last 7 rows of df.

import pandas as pd

df = pd.read_excel('python-practice\Practice Day 11 pandas\SampleSuperstore.xlsx')

print(df.tail(7))