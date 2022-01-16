from fastapi import Depends, HTTPException
from fastapi import FastAPI
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
conf = ConnectionConfig(
    MAIL_USERNAME="email address",
    MAIL_PASSWORD="email password",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM="dayeon0914@ewhain.net",
    MAIL_TLS=True,
    MAIL_SSL=False
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.EmailBase)
def create_user(user: schemas.EmailCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.post("/email")
async def simple_send(email: schemas.EmailBase) -> JSONResponse:
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.email,  # List of recipients, as many as you can pass
        body="Amazon의 주가가 " + str(email.predicted_price) + "$를 넘을 것으로 예측됩니다.",
        subtype="text"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})

