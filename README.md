# LVI Holding — Sales Visit Tracker

A full-stack web application for tracking sales representative visits to outlets. Built with **FastAPI** (Python) on the backend and **React** on the frontend, using SQLite as the database.

---

## Project Structure

```
LVI_HOLDING/
├── backend/
│   ├── auth.py           # JWT token creation
│   ├── database.py       # SQLAlchemy engine & session setup
│   ├── main.py           # FastAPI app & all API routes
│   ├── models.py         # Database models (User, Outlet, Visit)
│   ├── schemas.py        # Pydantic request/response schemas
│   ├── seed.py           # Seed script to populate sample data
│   ├── requirements.txt  # Python dependencies
│   └── sales.db          # SQLite database (auto-generated)
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── pages/
│       │   ├── Login.js       # Login page with link to Register
│       │   ├── Register.js    # New user registration page
│       │   ├── Dashboard.js   # Summary stats & navigation
│       │   ├── LogVisit.js    # Form to log a new outlet visit
│       │   └── Visits.js      # Table of all logged visits
│       ├── App.js             # Route definitions
│       └── index.js           # React entry point
│
├── data-analysis/
│   ├── sales_data.csv     # Raw sales dataset
│   ├── analysis.py        # Python analysis script
│   └── report.md          # Analysis findings report
│
├── README.md
└── REFLECTION.md
```

---

## Features

- JWT-based user authentication (register, login, protected routes)
- View dashboard with total visits, total cases sold, and top 3 outlets
- Log a new visit with outlet selection, cases sold, date, and notes
- View all visits in a table
- Token-based route protection on both frontend and backend
- Seed script with 2 users, 5 outlets, and 10 sample visits

---

## Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Backend   | FastAPI, SQLAlchemy, SQLite         |
| Auth      | python-jose (JWT), passlib (bcrypt) |
| Frontend  | React, React Router DOM             |
| API Comm  | Fetch API (REST)                    |

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+ and npm

---

### Backend Setup

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```



Seed the database with sample data:

```bash
python seed.py
```

Start the backend server:

```bash
python -m uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

---

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

The app will open at `http://localhost:3000`

---

## Default Login Credentials (from seed)

| Role  | Email           | Password   |
|-------|-----------------|------------|
| Admin | admin@test.com  | admin123   |
| User  | user@test.com   | user123    |

---

## API Endpoints

| Method | Endpoint     | Auth Required | Description                        |
|--------|--------------|---------------|------------------------------------|
| POST   | /register    | No            | Register a new user                |
| POST   | /login       | No            | Login and receive JWT token        |
| GET    | /dashboard   | Yes           | Total visits, cases, top outlets   |
| GET    | /outlets     | Yes           | List all outlets                   |
| POST   | /outlets     | Yes           | Create a new outlet                |
| GET    | /visits      | Yes           | List all visits                    |
| POST   | /visits      | Yes           | Log a new visit                    |

All protected routes require the header:
```
Authorization: Bearer <token>
```

---

## Pages

| Route        | Page        | Description                            |
|--------------|-------------|----------------------------------------|
| `/`          | Login       | Email & password login, link to Register |
| `/register`  | Register    | Create a new user account              |
| `/dashboard` | Dashboard   | Stats summary and navigation           |
| `/log-visit` | Log Visit   | Form to log a new outlet visit         |
| `/visits`    | Visits      | Table of all visits with outlet info   |

---

## Notes

- The `SECRET_KEY` in `auth.py` and `main.py` is hardcoded for development. Replace it with a secure environment variable before deploying to production.
- CORS is configured to allow only `http://localhost:3000`. Update `origins` in `main.py` for production.
- `sales.db` is auto-created when the backend starts for the first time.
