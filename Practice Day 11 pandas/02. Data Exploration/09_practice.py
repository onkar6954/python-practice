# Show first 3 rows and column names.

import pandas as pd

df = pd.read_json('python-practice\Practice Day 11 pandas\sample_Data.json')

print(df.head(3))
print(df.columns)