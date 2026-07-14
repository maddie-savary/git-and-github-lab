import pandas as pd
df = pd.read_csv("Data.csv")
print("Number of rows:", len(df))
print("Mean transaction price:", df["price"].mean())
# print the largest sales
print("Largest transaction:", df["price"].max())