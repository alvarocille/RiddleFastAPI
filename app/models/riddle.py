# app/models/riddles.py
from sqlalchemy import Column, Integer, String
from app.data.database import Base

class Riddle(Base):
    __tablename__ = "riddles"

    id: int = Column(Integer, primary_key=True, index=True)
    question: str = Column(String(200), nullable=False)
    solution: str = Column(String(100), nullable=False)
    category: str = Column(String(50), nullable=False, default="General")