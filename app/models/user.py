from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.data.database import Base


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(String(50), unique=True, index=True, nullable=False)
    email: str = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password: str = Column(String(200), nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now(timezone.utc))

    game_stats = relationship("GameStat", back_populates="user")

