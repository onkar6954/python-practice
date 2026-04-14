# Load a CSV file employees.csv and show first 5 rows.

import pandas as pd

df = pd.read_csv('python-practice\Practice Day 11 pandas\sales_data_sample.csv', encoding='latin1')

print(df.head(5))