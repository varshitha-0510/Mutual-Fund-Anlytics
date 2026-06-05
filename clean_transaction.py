import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Check column names
print(df.columns)

# Convert date column
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Keep only positive amounts
df = df[df["amount_inr"] > 0]

print("\nTransaction Types:")
print(df["transaction_type"].unique())

print("\nKYC Status:")
print(df["kyc_status"].unique())

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("\nCleaned file saved successfully")
print("Final Shape:", df.shape)