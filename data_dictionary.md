# Data Dictionary

## 01_fund_master.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| fund_house | Text | Fund House Name |
| scheme_name | Text | Scheme Name |
| category | Text | Fund Category |
| sub_category | Text | Fund Sub Category |
| risk_category | Text | Risk Classification |

---

## 02_nav_history.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

## 08_investor_transactions.csv

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | Integer | Investor ID |
| transaction_date | Date | Transaction Date |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount_inr | Float | Transaction Amount |
| state | Text | Investor State |
| city | Text | Investor City |
| city_tier | Text | Tier 1/2/3 |
| kyc_status | Text | KYC Verification Status |

---

## 07_scheme_performance.csv

| Column | Data Type | Description |
|----------|----------|----------|
| return_1yr_pct | Float | 1 Year Return |
| return_3yr_pct | Float | 3 Year Return |
| return_5yr_pct | Float | 5 Year Return |
| alpha | Float | Alpha Metric |
| beta | Float | Beta Metric |
| sharpe_ratio | Float | Sharpe Ratio |
| sortino_ratio | Float | Sortino Ratio |
| expense_ratio_pct | Float | Expense Ratio |
| aum_crore | Float | Assets Under Management |