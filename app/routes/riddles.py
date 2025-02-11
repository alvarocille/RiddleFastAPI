from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from .. import models, schemas
from ..data import database

router = APIRouter(
    prefix="/api/riddles",
    tags=["Riddles"]
)

@router.post("/", response_model=schemas.RiddleResponse)
def create_riddle(riddle: schemas.RiddleCreate, db: Session = Depends(database.get_db)):
    new_riddle = models.Riddle(
        question=riddle.question,
        solution=riddle.solution,
        category=riddle.category
    )
    db.add(new_riddle)
    db.commit()
    db.refresh(new_riddle)
    return new_riddle

@router.get("/", response_model=List[schemas.RiddleResponse])
def read_riddles(
    category: Optional[str] = Query(None, description="Filtrar acertijos por categoría"),
    db: Session = Depends(database.get_db)
):
    query = db.query(models.Riddle)
    if category:
        query = query.filter(models.Riddle.category == category)
    riddles = query.all()
    return riddles

@router.get("/{riddle_id}", response_model=schemas.RiddleResponse)
def read_riddle(riddle_id: int, db: Session = Depends(database.get_db)):
    riddle = db.query(models.Riddle).filter(models.Riddle.id == riddle_id).first()
    if not riddle:
        raise HTTPException(status_code=404, detail="Acertijo no encontrado")
    return riddle

@router.put("/{riddle_id}", response_model=schemas.RiddleResponse)
def update_riddle(riddle_id: int, updated_riddle: schemas.RiddleCreate, db: Session = Depends(database.get_db)):
    riddle = db.query(models.Riddle).filter(models.Riddle.id == riddle_id).first()
    if not riddle:
        raise HTTPException(status_code=404, detail="Acertijo no encontrado")
    riddle.question = updated_riddle.question
    riddle.solution = updated_riddle.solution
    riddle.category = updated_riddle.category
    db.commit()
    db.refresh(riddle)
    return riddle

@router.delete("/{riddle_id}", status_code=204)
def delete_riddle(riddle_id: int, db: Session = Depends(database.get_db)):
    riddle = db.query(models.Riddle).filter(models.Riddle.id == riddle_id).first()
    if not riddle:
        raise HTTPException(status_code=404, detail="Acertijo no encontrado")
    db.delete(riddle)
    db.commit()
    return

