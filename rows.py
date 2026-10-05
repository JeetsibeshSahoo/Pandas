# How to read rows

# head() tail()
# head(n) 5
# tail(n) 5

import pandas as pd

df = pd.read_json("sample_Data.json")

print("Display 10 rows of first: ")
# print(df.head(10))
print(df.head())

print("Display 10 rows of last: ")
# print(df.tail(10))
print(df.tail())