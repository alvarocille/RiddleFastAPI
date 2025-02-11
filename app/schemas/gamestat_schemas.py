from datetime import datetime
from pydantic import BaseModel, ConfigDict


class GameStatCreate(BaseModel):
    riddles_solved: int
    failed_attempts: int
    rooms_visited: int
    elapsed_time: float

class GameStatRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    riddles_solved: int
    failed_attempts: int
    rooms_visited: int
    elapsed_time: float
    created_at: datetime

