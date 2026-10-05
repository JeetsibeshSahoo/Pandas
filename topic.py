"""
1- How big is your dataset.
2- What are the names of columns.

shape and columns
"""

import pandas as pd

data = {
    "Name" : ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age" : [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary" : [50000, 60000, 45000, 52000, 49000, 70000, 48000, 50000],
    "Performance Score" : [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)
print(f"Shape: {df.shape}")
print(f"Column Names: {df.columns}")

"""
use of shape & columns

(100000, 20) - shape tells you that means 100000 rows and 20 columns.
(5,4) - Easy to find

using columns you can find the there is eny error with the columns name or not.
"""
