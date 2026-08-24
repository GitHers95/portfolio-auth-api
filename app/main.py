from fastapi import FastAPI

from app.database import Base, engine
from app.routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portfolio Auth API",
    description="API REST avec authentification JWT — Projet 1",
    version="1.0.0",
)

app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "API en ligne"}