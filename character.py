from pydantic import BaseModel
from uuid import UUID, uuid4
from weapons import Weapon
from armor import Armor, Shield


class PrimaryCharacteristics(BaseModel):
    vitality:int = 0
    wisdom:int = 0
    strength:int = 0
    intelligence:int = 0
    chance:int = 0
    agility:int = 0

    hp:int
    ap:int = 5
    mp:int = 3
    initiative:int
    prospecting:int = 100
    range:int = 0
    summons:int = 1


class SecondaryCharacteristics(BaseModel):
    pass

class Resistances(BaseModel):
    neutral_percent:int = 0
    neutral_flat:int = 0

    earth_percent:int = 0
    earth_flat:int = 0

    fire_percent:int = 0
    fire_flat:int = 0

    water_percent:int = 0
    water_flat:int = 0

    air_percent:int = 0
    air_flat:int = 0

    critical_flat:int = 0
    pushback_flat:int = 0


class Damage(BaseModel):
    damage:int = 0
    power:int = 0
    critical_damage:int = 0
    neutral_flat:int = 0
    earth_flat:int = 0
    fire_flat:int = 0
    water_flat:int = 0
    air_flat:int = 0
    weapon_skill:int = 0
    pushback:int = 0


class Skill(BaseModel)

class Race(BaseModel):
    pass


class Character(BaseModel):
    id: UUID = uuid4()
    race:str

    

    characteristics:Characteristics






    

class Hero(Character):
    name:str

class Monster(Character):
    pass
