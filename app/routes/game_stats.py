from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, auth
from ..data import database

router = APIRouter(
    prefix="/api/game_stats",
    tags=["GameStats"]
)

@router.post("/", response_model=schemas.GameStatRead)
def create_game_stat(game_stat: schemas.GameStatCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    new_stat = models.GameStat(
        user_id=current_user.id,
        riddles_solved=game_stat.riddles_solved,
        failed_attempts=game_stat.failed_attempts,
        rooms_visited=game_stat.rooms_visited,
        elapsed_time=game_stat.elapsed_time
    )
    db.add(new_stat)
    db.commit()
    db.refresh(new_stat)
    return new_stat

@router.get("/", response_model=List[schemas.GameStatRead])
def read_game_stats(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    stats = db.query(models.GameStat).filter(models.GameStat.user_id == current_user.id).all()
    return stats

@router.get("/{stat_id}", response_model=schemas.GameStatRead)
def read_game_stat(stat_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    stat = db.query(models.GameStat).filter(models.GameStat.id == stat_id, models.GameStat.user_id == current_user.id).first()
    if not stat:
        raise HTTPException(status_code=404, detail="Estadística no encontrada")
    return stat

@router.put("/{stat_id}", response_model=schemas.GameStatRead)
def update_game_stat(stat_id: int, updated_stat: schemas.GameStatCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    stat = db.query(models.GameStat).filter(models.GameStat.id == stat_id, models.GameStat.user_id == current_user.id).first()
    if not stat:
        raise HTTPException(status_code=404, detail="Estadística no encontrada")
    stat.riddles_solved = updated_stat.riddles_solved
    stat.failed_attempts = updated_stat.failed_attempts
    stat.rooms_visited = updated_stat.rooms_visited
    stat.elapsed_time = updated_stat.elapsed_time
    db.commit()
    db.refresh(stat)
    return stat

@router.delete("/{stat_id}", status_code=204)
def delete_game_stat(stat_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    stat = db.query(models.GameStat).filter(models.GameStat.id == stat_id, models.GameStat.user_id == current_user.id).first()
    if not stat:
        raise HTTPException(status_code=404, detail="Estadística no encontrada")
    db.delete(stat)
    db.commit()
    return
