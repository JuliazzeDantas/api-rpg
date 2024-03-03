from pydantic import BaseModel
from uuid import UUID, uuid4

class Damage_Type(BaseModel):
    piercing:str ='piercing'
    slashing:str ='slashing'
    bludgeoning:str ='bludgeoning'


class Weapon(BaseModel):
    id:UUID = uuid4()
    name:str

    #damage = multiplier * (1d6) + adder
    damage_multiplier: int = 1
    damage_adder: int = 0
    damage_type: Damage_Type
