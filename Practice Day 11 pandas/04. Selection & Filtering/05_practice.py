# Select rows where "STATE" is null(empty).

import pandas as pd

df = pd.read_csv('python-practice\Practice Day 11 pandas\sales_data_sample.csv', encoding='latin1')

print(df[df['STATE'].isnull() == True])