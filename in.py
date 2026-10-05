import pandas as pd


# df = pd.read_json("sample_Data.json")
data = {
    "Name" : ["Ram", "Shyam", "Ghanshyam"],
    "Age" : [10, 20, 30],
    "City" : ["Nagpur", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

print("Display the info of data set: ")
print(df.info()) 