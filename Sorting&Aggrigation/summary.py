"""
df["Column_name"].mean()
df["Column_name"].sum()
df["Column_name"].min()
df["Column_name"].max()
"""
import pandas as pd

data = {
    "Name" : ["Arun", "Varun", "karun"],
    "Age" : [28, 30, 22],
    "Salary" : [10000, 20000, 15000]
}

df = pd.DataFrame(data)

avg_salary = df["Salary"].mean()
print(avg_salary)