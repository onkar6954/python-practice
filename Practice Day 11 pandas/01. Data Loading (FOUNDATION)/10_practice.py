# Load JSON file users.json and display column names.

import pandas as pd

df = pd.read_json('python-practice\Practice Day 11 pandas\sample_Data.json')

print(pd.DataFrame(df.columns))