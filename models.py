
from sqlalchemy import Column, String, DateTime, Float

from database import Base


class Email(Base):
    __tablename__ = "emails"
    email = Column(String, primary_key=True, index=True)
    predicted_price = Column(Float, index=True)


class Stock(Base):
    __tablename__ = "prices"
    date_time = Column(DateTime, primary_key=True, index=True)
    price = Column(Float, index=True)