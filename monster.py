from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models import Monster
from data import monsters_data

monsters=monsters_data
router=APIRouter()


@router.post("")
def set_monster(monster: Monster):
    monsters.append(monster)
    return monsters


@router.get("")
def list_monster():
    return monsters


@router.get("/{monster_id}", response_model=Monster)
def get_monster(monster_id:int)->Monster:
    if monster_id < len(monsters):
        return monsters[monster_id]
    else:
        raise HTTPException(status_code=404, detail=f"There isn't id {monster_id}")