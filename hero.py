from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models import Hero
from data import heroes_data

heroes=heroes_data
router=APIRouter()


@router.post("/")
def set_hero(hero: Hero):
    heroes.append(hero)
    return heroes


@router.get("/")
def list_heroes():
    return heroes


@router.get("/{hero_id}", response_model=Hero)
def get_hero(hero_id:int)->Hero:
    if hero_id < len(heroes):
        return heroes[hero_id]
    else:
        raise HTTPException(status_code=404, detail=f"There isn't id {hero_id}")