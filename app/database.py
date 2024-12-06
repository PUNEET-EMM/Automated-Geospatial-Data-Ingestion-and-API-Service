from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL  # Ensure DATABASE_URL is set correctly

# Create the database engine
engine = create_engine(DATABASE_URL)  # Remove connect_args for PostgreSQL

# Configure sessionmaker with autocommit=False, autoflush=False
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare the base for ORM models
Base = declarative_base()

# Dependency to provide database sessions
def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield the session to be used by the caller
    finally:
        db.close()  # Ensure the session is closed after the operation




