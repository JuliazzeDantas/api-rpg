from pydantic import BaseModel

class Character(BaseModel):
    race:str
    hp:int = 20
    mp:int = 10
    defense:int = 0
    #wepon:Weapon
    #shield:Armor
    #armor:Armor

class Hero(Character):
    name:str

class Monster(Character):
    pass
