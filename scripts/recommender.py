import pandas as pd

scheme = pd.read_csv("../data/processed/scheme_performance_clean.csv")

risk = input("Enter Risk Level: ")

result = scheme[
    scheme["risk_grade"] == risk
].sort_values(
    "sharpe_ratio",
    ascending=False
)

print(
    result[
        [
            "scheme_name",
            "sharpe_ratio"
        ]
    ].head(3)
)