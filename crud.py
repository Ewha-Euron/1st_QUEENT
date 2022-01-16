from sqlalchemy.orm import Session

import models
import datetime


def get_email(db: Session, price: float):
    return db.query(models.Email).filter(models.Email.predicted_price >= price).all()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Email).filter(models.Email.email == email).first()


def create_stock(db: Session, price: float):
    db_stock = models.Stock(price=price, date=datetime.now())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

