# Remove columns that contain missing values.

import pandas as pd

df = pd.read_json('python-practice\Practice Day 11 pandas\sample_Data.json')

print(df.shape)
print(df.dropna(axis=1))