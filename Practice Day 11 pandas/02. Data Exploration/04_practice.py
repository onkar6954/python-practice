# Print column names of df.

import pandas as pd

df = pd.read_csv('python-practice\Practice Day 11 pandas\sales_data_sample.csv', encoding='latin1')

print(pd.DataFrame(df.columns))