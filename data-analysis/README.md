# Data Analysis — LVI Holding Sales Report

This folder contains the sales data and Python analysis script for LVI Holding's outlet performance across October to December 2025.

---

## Folder Contents

```
data-analysis/
├── sales_data.csv   # Raw sales dataset (38 records)
├── analysis.py      # Python analysis script
└── report.md        # Analysis findings report
```

---

## Dataset Overview

**File:** `sales_data.csv`

| Column       | Description                          |
|--------------|--------------------------------------|
| outlet_id    | Unique ID for each outlet            |
| outlet_name  | Name of the outlet                   |
| city         | City where the outlet is located     |
| date         | Date of the sale (DD-MM-YYYY)        |
| product      | Product sold (Boroka Gin)            |
| cases_sold   | Number of cases sold in that visit   |
| revenue      | Revenue generated (in ₹)            |

- **Total Records:** 38 rows
- **Period Covered:** October 2025 — December 2025
- **City:** Bangalore
- **Outlets:** 15 unique outlets
- **Product:** Boroka Gin

---

## How to Run

Make sure you have Python and pandas installed:

```bash
pip install pandas
```

Run the analysis script:

```bash
cd data-analysis
python analysis.py
```

The output will be printed directly in the terminal.

---

## Analysis Sections

The script performs 5 analyses:

**1. Top 10 Outlets by Total Revenue**
Ranks all outlets by their total revenue generated across the 3-month period. Helps identify the highest value outlets.

**2. Monthly Revenue Trend**
Shows total revenue for each month — October, November, and December — and highlights the highest revenue month.

**3. Product Mix (% of Total Cases)**
Breaks down what percentage of total cases sold each product accounts for across all outlets.

**4. Declining (At Risk) Outlets**
Compares each outlet's December sales against their October–November average. Outlets where December sales dropped are flagged as at risk.

**5. Consistency Score**
Counts how many months each outlet made a purchase. Outlets that bought across all 3 months are considered the most consistent and reliable customers.

---

## Requirements

- Python 3.10+
- pandas
