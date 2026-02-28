import pandas as pd

# ---------------------------
# Load Data
# ---------------------------
file_path = "sales_data.csv"   # Keep CSV in same folder
df = pd.read_csv(file_path)

# ---------------------------
# Data Preparation
# ---------------------------
df['date'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
df['month'] = df['date'].dt.month_name()
df['month_num'] = df['date'].dt.month

print("\n==============================")
print("        SALES ANALYSIS        ")
print("==============================\n")

# =========================================================
# 1️⃣ Top 10 Outlets by Total Revenue
# =========================================================
print("1. Top 10 Outlets by Total Revenue:\n")

top_outlets = (
    df.groupby('outlet_name', as_index=False)['revenue']
    .sum()
    .sort_values(by='revenue', ascending=False)
    .head(10)
)

for _, row in top_outlets.iterrows():
    print(f"{row['outlet_name']} : ₹{row['revenue']:,}")

print("\n")


# =========================================================
# 2️⃣ Monthly Revenue Trend
# =========================================================
print("2. Monthly Revenue Trend:\n")

month_order = ["October", "November", "December"]

monthly_revenue = (
    df.groupby('month', as_index=False)['revenue']
    .sum()
)

monthly_revenue['month'] = pd.Categorical(
    monthly_revenue['month'],
    categories=month_order,
    ordered=True
)

monthly_revenue = monthly_revenue.sort_values('month')

for _, row in monthly_revenue.iterrows():
    print(f"{row['month']} : ₹{row['revenue']:,}")

highest_month = monthly_revenue.loc[
    monthly_revenue['revenue'].idxmax()
]

print(f"\nHighest Revenue Month: {highest_month['month']} (₹{highest_month['revenue']:,})")
print("\n")


# =========================================================
# 3️⃣ Product Mix (% of Total Cases)
# =========================================================
print("3. Product Mix (% of Total Cases):\n")

total_cases = df['cases_sold'].sum()

product_mix = (
    df.groupby('product', as_index=False)['cases_sold']
    .sum()
)

product_mix['percentage'] = (
    (product_mix['cases_sold'] / total_cases) * 100
).round(2)

for _, row in product_mix.iterrows():
    print(f"{row['product']} : {row['cases_sold']} cases ({row['percentage']}%)")

print("\n")


# =========================================================
# 4️⃣ Declining (At Risk) Outlets
# =========================================================
print("4. Declining (At Risk) Outlets:\n")

# Average cases sold in October & November
oct_nov_avg = (
    df[df['month_num'].isin([10, 11])]
    .groupby('outlet_name', as_index=False)['cases_sold']
    .mean()
)

# December average
dec_sales = (
    df[df['month_num'] == 12]
    .groupby('outlet_name', as_index=False)['cases_sold']
    .mean()
)

# Merge to compare
comparison = pd.merge(
    oct_nov_avg,
    dec_sales,
    on='outlet_name',
    how='inner',
    suffixes=('_oct_nov_avg', '_dec')
)

declining = comparison[
    comparison['cases_sold_dec'] < comparison['cases_sold_oct_nov_avg']
]

if not declining.empty:
    for _, row in declining.iterrows():
        print(row['outlet_name'])
else:
    print("No declining outlets found.")

print("\n")


# =========================================================
# 5️⃣ Consistency Score
# =========================================================
print("5. Consistency Score (Number of Months Purchased):\n")

consistency = (
    df.groupby('outlet_name', as_index=False)['month']
    .nunique()
    .rename(columns={'month': 'months_purchased'})
    .sort_values(by='months_purchased', ascending=False)
)

for _, row in consistency.iterrows():
    print(f"{row['outlet_name']} : {row['months_purchased']} months")

print("\n==============================")
print("        END OF REPORT         ")
print("==============================")