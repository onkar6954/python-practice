# Load Excel file and print its shape.

import pandas as pd

df = pd.read_excel('python-practice\Practice Day 11 pandas\SampleSuperstore.xlsx')

print(df.shape)