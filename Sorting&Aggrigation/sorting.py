# sorting data
# SORTING DATA 1 COLUMN sort_values()
# df.sort_values(by="Column_name", ascending=True/False, inplace=True)

import pandas as pd

data = {
    "Name" : ["Arun", "Varun", "karun"],
    "Age" : [28, 30, 22],
    "Salary" : [10000, 20000, 15000]
}

df = pd.DataFrame(data)
df.sort_values(by="Age", ascending=False, inplace=True)
print("Sorted age by descending")
print(df)