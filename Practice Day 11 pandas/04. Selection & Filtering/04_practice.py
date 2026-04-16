# Select rows where "price" > 400.

import pandas as pd

df = pd.read_json('python-practice\Practice Day 11 pandas\sample_Data.json')

print(df[df['price']>400])