# pd.merge(df1, df2, on="Column_name", how="type of join")
import pandas as pd

# customer dataframe
df_customers = pd.DataFrame({
    "CustomerID" : [1,2,3],
    "Name" : ["Ramesh", "Suresh", "Kalpesh"]
})

# order dataframe
df_orders = pd.DataFrame({
    "CustomerID" : [1,2,4],
    "OrderAmount" : [250, 450, 350]
})

# merge
# Inner
# df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="inner")
# print("Inner join")
# print(df_merged)

# Outer
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="outer")
print("Outer join")
print(df_merged)

# Left
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="left")
print("Left join")
print(df_merged)

# Right
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="right")
print("Right join")
print(df_merged)

# cross
"""
1df = m rows
2df = n rows
m * n rows
"""

df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="cross")
print("Cross join")
print(df_merged)

