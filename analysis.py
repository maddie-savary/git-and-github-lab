import pandas as pd
df = pd.read_csv("Data.csv")
print("Number of rows:", len(df))
print("Mean price:", df["price"].mean())
# print the largest sale:
print("Largest sale:", df["price"].max())