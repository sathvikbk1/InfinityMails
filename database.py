from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Database setup
DATABASE_URL = "sqlite:///emails.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Email Data Model
class Contact(Base):
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    company = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    email_sent = Column(Boolean, default=False)
    follow_up_count = Column(Integer, default=0)
    last_email_sent = Column(DateTime, nullable=True)

# Create the database tables
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print("Database initialized.")
