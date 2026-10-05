# df.sort_values(by=["Age", "Salary"], ascending = True, inplace = True)

import pandas as pd

data = {
    "Name" : ["Arun", "Varun", "karun"],
    "Age" : [28, 30, 22],
    "Salary" : [10000, 20000, 15000]
}

df = pd.DataFrame(data)
df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print("Sorted age by descending")
print(df)