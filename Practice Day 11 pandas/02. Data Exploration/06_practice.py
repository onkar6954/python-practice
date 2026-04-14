# Display complete info of df.

import pandas as pd

df = pd.read_json('python-practice\Practice Day 11 pandas\sample_Data.json')

print(df.info())