from datetime import datetime

from pydantic import BaseModel


class StockBase(BaseModel):
    pass


class Stock(StockBase):
    date: datetime
    price: float

    class Config:
        orm_mode = True


class EmailBase(BaseModel):
    email: str
    predicted_price: float


class EmailCreate(EmailBase):
    pass

'''
class Email(EmailBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
'''