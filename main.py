from fastapi import FastAPI

from hero import router as heroes_router
from monster import router as monsters_router

app = FastAPI()

@app.get("/")
def root():
    return {"test":"test1"}

app.include_router(heroes_router, prefix="/hero", tags=["hero"])
app.include_router(monsters_router, prefix="/monster", tags=["monster"])