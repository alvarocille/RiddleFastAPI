from pydantic import BaseModel

class RiddleBase(BaseModel):
    question: str
    solution: str
    category: str = "General"

class RiddleCreate(RiddleBase):
    pass

class RiddleResponse(RiddleBase):
    id: int

    class Config:
        from_attributes = True
