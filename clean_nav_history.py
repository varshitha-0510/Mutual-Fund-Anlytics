import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["amfi_code", "date"])

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

df = df.drop_duplicates()

df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)

df.to_csv("data/processed/nav_history_clean.csv", index=False)

print("Cleaned file saved successfully")