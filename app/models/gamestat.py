from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.data.database import Base


class GameStat(Base):
    __tablename__ = "game_stats"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    riddles_solved = Column(Integer, default=0)
    failed_attempts = Column(Integer, default=0)
    rooms_visited = Column(Integer, default=0)
    elapsed_time = Column(Float, default=0.0)  # Tiempo en segundos
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    user = relationship("User", back_populates="game_stats")

