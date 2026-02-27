# 📊 Sales Analytics & Performance Monitoring System

> A full-stack sales analytics system that identifies revenue trends,
> high-performing outlets, and at-risk accounts using Python-based data
> analysis.

------------------------------------------------------------------------

## 🚀 Project Overview

This project analyzes outlet-level sales data to generate actionable
business insights.

It includes:

-   Backend API service\
-   Frontend interface\
-   Data analysis module (Python + Pandas)\
-   Business performance insights

The system helps answer key business questions like:

-   Which outlets drive the highest revenue?
-   How is monthly revenue trending?
-   Which outlets are declining?
-   How consistent are outlet purchase patterns?

------------------------------------------------------------------------

## 🏗️ Tech Stack

**Backend** - Python - Flask / FastAPI

**Frontend** - React / HTML / CSS / JavaScript

**Data Analysis** - Python - Pandas

------------------------------------------------------------------------

## 📁 Project Structure

project-root/ │ ├── backend/ │ └── app.py / main.py │ ├── frontend/ │
└── UI source code │ ├── data-analysis/ │ ├── sales_data.csv │ └──
analysis.py │ └── README.md

------------------------------------------------------------------------

# ⚙️ Setup & Run Instructions

## 🔹 Backend Setup

Install dependencies:

    pip install flask pandas

Run server:

    cd backend
    python app.py

If using FastAPI:

    uvicorn main:app --reload

Backend runs at:

    http://localhost:5000

------------------------------------------------------------------------

## 🔹 Frontend Setup

    cd frontend
    npm install
    npm start

Frontend runs at:

    http://localhost:3000

------------------------------------------------------------------------

## 🔹 Data Analysis Execution

Navigate to analysis folder:

    cd data-analysis
    pip install pandas
    python analysis.py

------------------------------------------------------------------------

# 📈 Key Analysis Features

1.  Top 10 Revenue Outlets\
2.  Monthly Revenue Trend\
3.  Product Mix Analysis\
4.  At-Risk Outlet Detection\
5.  Consistency Score

------------------------------------------------------------------------

# ⚠️ Challenges & Solutions

### Date Parsing Issue

Problem: ValueError: time data does not match format

Solution:

    df['date'] = pd.to_datetime(df['date'], format="%d-%m-%Y")

------------------------------------------------------------------------

### Incorrect Month Ordering

Used categorical sorting to maintain chronological month order.

------------------------------------------------------------------------

### Pandas Series Metadata in Output

Converted grouped results into DataFrame and formatted clean console
output.

------------------------------------------------------------------------

# 🎯 What This Project Demonstrates

-   Data cleaning & preprocessing
-   Advanced Pandas groupby operations
-   Business logic implementation
-   Performance comparison modeling
-   Full-stack integration

------------------------------------------------------------------------

# 🔮 Future Enhancements

-   Add interactive dashboard
-   Add visualization using Matplotlib
-   Automated PDF report export
-   Deploy backend to cloud

------------------------------------------------------------------------

# 👨‍💻 Author

Mugilanandam R\
Full Stack Developer \| Data Analytics Enthusiast
