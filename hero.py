from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import UUID
from models import Hero, Hit
from data import heroes_data

heroes=heroes_data
router=APIRouter()


@router.post("")
def create_hero(hero: Hero):
    heroes.append(hero)
    return heroes


@router.get("")
def list_heroes():
    return heroes


@router.get("/{hero_id}")
def get_hero(hero_id:UUID)->Hero:
    for character in heroes:
        if character.id==hero_id:
            return character
        
    raise HTTPException(status_code=404, detail=f"Hero ID {hero_id} was not found")
    

@router.get("/{hero_id}/hp")
def get_hero_hp(hero_id:UUID):
    for character in heroes:
        if character.id==hero_id:
            return character.hp
        
    raise HTTPException(status_code=404, detail=f"Hero ID {hero_id} was not found")


@router.put("/{hero_id}/damage")
def hurt_hero(hero_id:UUID, hit:Hit):
    for character in heroes:
        if character.id==hero_id:
            character.hp=character.take_damage(hit)
            if character.hp<=0:
                kill_hero()
                return 0
            else:
                return character.hp
            
    raise HTTPException(status_code=404, detail=f"Monster ID {hero_id} was not found")


@router.post("/{hero_id}/damage")
def normal_atack(hero_id:UUID):
    for character in heroes:
        if character.id==hero_id:
            damage=character.normal_atack()
            return damage

    raise HTTPException(status_code=404, detail=f"Hero ID {hero_id} was not found")


def kill_hero():
    pass