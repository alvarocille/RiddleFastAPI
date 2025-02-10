from fastapi import APIRouter, Depends, HTTPException
from datetime import timedelta
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .. import models, schemas, auth
from ..data import database

router = APIRouter(
    prefix="/api",
    tags=["Users"]
)

# Modelo para recibir el login vía JSON
class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/signup", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(database.get_db)):
    user = auth.authenticate_user(db, request.username, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=schemas.UserRead)
def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user