from pydantic import BaseModel, ConfigDict


class RiddleBase(BaseModel):
    question: str
    solution: str
    category: str = "General"

class RiddleCreate(RiddleBase):
    pass

class RiddleResponse(RiddleBase):
    model_config = ConfigDict(from_attributes=True)
    id: int