from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.data.database import Base, engine
from .data.default_riddles import default_riddles
from .routes import users, game_stats, riddles
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(aplication: FastAPI):
    db = Session(bind=engine)
    try:
        default_riddles(db)
        yield
    finally:
        db.close()

app = FastAPI(
    title="API de Mansión Embrujada",
    description="Backend para la aplicación de juego en Kotlin.",
    version="1.0.0",
    lifespan=lifespan
)

# Incluir routers
app.include_router(users.router)
app.include_router(game_stats.router)
app.include_router(riddles.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
