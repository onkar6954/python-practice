# Display shape and summary statistics together.

import pandas as pd

df = pd.read_json('python-practice\Practice Day 11 pandas\sample_Data.json')

print(df.shape)
print(df.describe())