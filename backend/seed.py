#Seed.py

from database import SessionLocal, engine
import models
from passlib.context import CryptContext
from datetime import date

# CREATE TABLES
models.Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def seed_data():

    db = SessionLocal()

    # Clear old data
    db.query(models.Visit).delete()
    db.query(models.Outlet).delete()
    db.query(models.User).delete()
    db.commit()

    # Create users
    user1 = models.User(
        name="Mugil Admin",
        email="admin@test.com",
        password=pwd_context.hash("admin123")
    )

    user2 = models.User(
        name="User Mugil",
        email="user@test.com",
        password=pwd_context.hash("user123")
    )

    db.add_all([user1, user2])
    db.commit()

    # Create outlets
    outlets = [
        models.Outlet(name="Skybar", address="MG Road", city="Bangalore"),
        models.Outlet(name="Metro Club", address="Indiranagar", city="Bangalore"),
        models.Outlet(name="Urban Lounge", address="Koramangala", city="Bangalore"),
        models.Outlet(name="Cloud Nine", address="Whitefield", city="Bangalore"),
        models.Outlet(name="Jazz Corner", address="HSR Layout", city="Bangalore")
    ]

    db.add_all(outlets)
    db.commit()

    # Create visits
    visits = [
        models.Visit(outlet_id=1, notes="Good sales", cases_sold=5, date=date(2026,2,1)),
        models.Visit(outlet_id=2, notes="Average day", cases_sold=3, date=date(2026,2,2)),
        models.Visit(outlet_id=3, notes="Strong demand", cases_sold=7, date=date(2026,2,3)),
        models.Visit(outlet_id=4, notes="Slow day", cases_sold=2, date=date(2026,2,4)),
        models.Visit(outlet_id=5, notes="Excellent sales", cases_sold=8, date=date(2026,2,5)),
        models.Visit(outlet_id=1, notes="Repeat order", cases_sold=4, date=date(2026,2,6)),
        models.Visit(outlet_id=2, notes="Festival boost", cases_sold=6, date=date(2026,2,7)),
        models.Visit(outlet_id=3, notes="Good response", cases_sold=5, date=date(2026,2,8)),
        models.Visit(outlet_id=4, notes="Low traffic", cases_sold=2, date=date(2026,2,9)),
        models.Visit(outlet_id=5, notes="Steady sales", cases_sold=6, date=date(2026,2,10))
    ]

    db.add_all(visits)
    db.commit()

    db.close()

    print("Seed data inserted successfully!")

if __name__ == "__main__":
    seed_data()