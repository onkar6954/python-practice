# Display last 3 rows of df.

import pandas as pd

df = pd.read_csv('python-practice\Practice Day 11 pandas\sales_data_sample.csv', encoding='latin1')

print(df.tail(3))