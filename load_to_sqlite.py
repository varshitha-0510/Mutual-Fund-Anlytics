import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

# Load files
fund_df = pd.read_csv("data/raw/01_fund_master.csv")
nav_df = pd.read_csv("data/processed/nav_history_clean.csv")
txn_df = pd.read_csv("data/processed/investor_transactions_clean.csv")
perf_df = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Save into SQLite
fund_df.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)
txn_df.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf_df.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("All tables loaded successfully!")