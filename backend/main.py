#main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy import func

from database import engine, SessionLocal
import models
import schemas

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# CORS
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
models.Base.metadata.create_all(bind=engine)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT Settings
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Security scheme
security = HTTPBearer()


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- REGISTER ----------------
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = pwd_context.hash(user.password)

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


# ---------------- LOGIN ----------------
@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {
        "sub": db_user.email,
        "exp": expire
    }

    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": access_token}


# ---------------- JWT VALIDATION ----------------
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(models.User).filter(models.User.email == email).first()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user


# ---------------- PROTECTED ROUTE ----------------
@app.get("/protected")
def protected_route(current_user: models.User = Depends(get_current_user)):
    return {
        "message": f"Hello {current_user.name}, you are authenticated!"
    }


@app.post("/outlets")
def create_outlet(
    outlet: schemas.OutletCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    new_outlet = models.Outlet(
        name=outlet.name,
        address=outlet.address,
        city=outlet.city
    )

    db.add(new_outlet)
    db.commit()
    db.refresh(new_outlet)

    return {"message": "Outlet created successfully"}


@app.get("/outlets")
def get_outlets(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    outlets = db.query(models.Outlet).all()

    return outlets


@app.post("/visits")
def create_visit(
    visit: schemas.VisitCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    # Check if outlet exists
    outlet = db.query(models.Outlet).filter(
        models.Outlet.id == visit.outlet_id
    ).first()

    if not outlet:
        raise HTTPException(status_code=404, detail="Outlet not found")

    new_visit = models.Visit(
        outlet_id=visit.outlet_id,
        notes=visit.notes,
        cases_sold=visit.cases_sold,
        date=visit.date
    )

    db.add(new_visit)
    db.commit()
    db.refresh(new_visit)

    return {"message": "Visit logged successfully"}


@app.get("/visits")
def get_visits(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    visits = db.query(models.Visit).all()

    result = []

    for visit in visits:
        result.append({
            "date": visit.date,
            "outlet_name": visit.outlet.name,
            "cases_sold": visit.cases_sold,
            "notes": visit.notes
        })

    return result



@app.get("/dashboard")
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    # Total visits
    total_visits = db.query(func.count(models.Visit.id)).scalar()

    # Total cases sold
    total_cases = db.query(func.sum(models.Visit.cases_sold)).scalar()

    if total_cases is None:
        total_cases = 0

    # Top 3 outlets by total cases sold
    top_outlets = (
        db.query(
            models.Outlet.name,
            func.sum(models.Visit.cases_sold).label("total_cases")
        )
        .join(models.Visit, models.Outlet.id == models.Visit.outlet_id)
        .group_by(models.Outlet.id)
        .order_by(func.sum(models.Visit.cases_sold).desc())
        .limit(3)
        .all()
    )

    top_outlets_list = [
        {"outlet_name": outlet[0], "total_cases": outlet[1]}
        for outlet in top_outlets
    ]

    return {
        "total_visits": total_visits,
        "total_cases_sold": total_cases,
        "top_3_outlets": top_outlets_list
    }