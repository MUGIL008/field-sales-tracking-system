# REFLECTION.md

## Project: LVI Holding — Sales Visit Tracker

---

### 1. What was the hardest part of this assignment?

I encountered an error with bcrypt because passlib was unable to read bcrypt's version number correctly due to compatibility issues with newer versions of passlib. I had to downgrade bcrypt to version 4.0.1.

These types of environment and dependency issues are not coding issues; they are issues of understanding how Python is packaged, which was a real learning experience for me. After I got that working, everything else was pretty easy.

---

### 2. How did you use Claude/AI tools? Give 2-3 specific examples of prompts you used.

I used Claude sometimes as a reference and for solving errors I got stuck on during the project. Here are three specific examples:

**Example 1:**
> *"I am getting ModuleNotFoundError for sqlalchemy. How do I install all my dependencies at once?"*

Claude explained how I could use `pip install -r requirements.txt` and also provided the entire command with the list of common FastAPI packages in case the requirements.txt was not already present. This saved a lot of my time.

**Example 2:**
> *"I have a sales CSV with outlet names, dates, products and cases sold. How do I find the top 10 outlets by total revenue using pandas?"*

Claude explained how to use `groupby` and `sum`, and how to chain `sort_values` and `head(10)` to get the top 10. I would have had to do it with a loop before, which would have been much longer code.

**Example 3:**
> *"How do I find declining outlets — outlets whose December sales are lower than their October and November average?"*

Claude explained how I could filter the dataframe by month number, find the average for October and November separately, and then combine them by comparing columns. I didn't know how to use `pd.merge` before — I learned it directly from this prompt.

---

### 3. Pick one piece of code Claude helped you write. Explain what it does in your own words.

The code I'd like to explain is the Top 10 Outlets by Total Revenue calculation in `analysis.py`:

```python
top_outlets = (
    df.groupby('outlet_name', as_index=False)['revenue']
    .sum()
    .sort_values(by='revenue', ascending=False)
    .head(10)
)
```

This code aggregates all the rows in the sales data and groups them by outlet name. So instead of seeing 38 rows of individual sales, we're seeing a single row for each outlet. It then adds up all the revenue for each outlet using `.sum()`. After that, it orders the outlets in descending order of revenue using `sort_values`. Finally, it selects the top 10 using `.head(10)`.

The code gives us a clean list of the top 10 outlets in order of revenue. I understand this code because `groupby` is just a function that does what a pivot table does in Excel — aggregates rows — and `sort_values` just orders those rows so we can see the best ones first.

---

### 4. What would you improve if you had more time?

If I had more time, the first thing I would do is rebuild the UI to be fully responsive and interactive. Right now the application works well functionally, but the design is very basic. I would want users to feel good when they open the app — with smooth transitions, clean layouts, proper colors, and a design that works well on both desktop and mobile. The way an app looks and feels matters just as much as how it works, and I would want users to enjoy using it, not just tolerate it.

- **Add proper Register page validation** — clear error messages if the email is already taken or the password is too short.
- **Make the dashboard dynamic** — add date filters so the user can view performance for a specific month or week.
- **Secure the SECRET_KEY** — move the JWT secret key into an environment variable using a `.env` file so it is never exposed in the code.
- **Add charts to the data analysis** — use `matplotlib` or `plotly` to generate visual charts for the revenue trend and product mix, making findings easier to understand at a glance.

---

### 5. Rate your Python comfort: Before vs After

| | Rating | Notes |
|---|---|---|
| **Before starting** | 6/10 | I was comfortable with Python basics — variables, loops, functions, and simple scripts. But I had never built a full backend API or worked with SQLAlchemy, FastAPI, or JWT before. |
| **After finishing** | 9/10 | After completing this project, I am much more confident. I know now how to create REST APIs using FastAPI, database models using SQLAlchemy, authentication using JWT and bcrypt, and actual data analysis using pandas. Making something from scratch has allowed me to understand everything in a way that reading about it has not. |
