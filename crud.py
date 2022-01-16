from sqlalchemy.orm import Session

import models
import datetime


def get_email(db: Session, price: float):
    return db.query(models.Email).filter(models.Email.predicted_price >= price).all()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Email).filter(models.Email.email == email).first()


'''
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
'''


def create_stock(db: Session, price: float):
    db_stock = models.Stock(price=price, date=datetime.now())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock


'''
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
'''
