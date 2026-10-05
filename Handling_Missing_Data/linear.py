import pandas as pd

data = {
    "Time" : [1,2,3,4,5],
    "Value" : [10, None, 30, None, 50]
}

df = pd.DataFrame(data)
print("Before interpolation")
print(df)

df["Value"] = df["Value"].interpolate(method="linear")
print("\n After interpolation")
print(df)

"""
Use of interpolation

1- time series data
2- numeric data with trends
3- avoid dropping rows
"""