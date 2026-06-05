-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3. Transactions by State
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 4. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Transaction Type Distribution
SELECT transaction_type, COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

-- 6. Top 5 Fund Houses by Number of Schemes
SELECT fund_house, COUNT(*) AS schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY schemes DESC
LIMIT 5;

-- 7. Average 1-Year Return by Category
SELECT category,
AVG(return_1yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;

-- 8. Highest Sharpe Ratio Funds
SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 9. Risk Grade Distribution
SELECT risk_grade, COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;

-- 10. Top States by Investment Amount
SELECT state,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;