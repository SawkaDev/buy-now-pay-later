# core/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from core.base import Base

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Import all models here
    from models import loan  # This imports the Loan model
    Base.metadata.create_all(bind=engine)
