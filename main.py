from fastapi import FastAPI
from database import Base, engine
from auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth API")

app.include_router(auth_router)