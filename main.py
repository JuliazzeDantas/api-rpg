from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from random import randint

'''class Weapon(BaseModel):
    name:str
    multiplier:int = 1
    adder:int = 0

class Armor(BaseModel):
    name:str
    defense:int = 0
'''
class Hero(BaseModel):
    name:str
    race:str
    hp:int = 20
    mp:int = 10
    defense:int = 0
    #wepon:Weapon
    #shield:Armor
    #armor:Armor

class Monster(BaseModel):
    race:str
    hp:int = 20
    mp:int = 10
    defense:int = 0
    #damage_multiplier:int = 1
    #damage_adder:int = 0
    #armor:int = 0

heroes = []
monsters = []

app = FastAPI()

@app.get("/")
def root():
    return {"test":"test1"}

@app.post("/hero")
def set_hero(hero: Hero):
    heroes.append(hero)
    return heroes

@app.get("/hero")
def list_heroes():
    return heroes

app.get("/hero/{hero_id}", response_model=Hero)
def get_hero(hero_id:int)->Hero:
    if hero_id < len(heroes):
        return heroes[hero_id]
    else:
        raise HTTPException(status_code=404, detail=f"There isn't id {hero_id}")

@app.post("/monster")
def set_monster(monster: Monster):
    monsters.append(monster)
    return monsters

@app.get("/monster")
def list_monster():
    return monsters

@app.get("/monster/{monster_id}", response_model=Monster)
def get_monster(monster_id:int)->Monster:
    if monster_id < len(monsters):
        return monsters[monster_id]
    else:
        raise HTTPException(status_code=404, detail=f"There isn't id {monster_id}")
    

