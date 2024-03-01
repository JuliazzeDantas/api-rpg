from uuid import uuid4, UUID
from pydantic import BaseModel
from random import randint


class Hit(BaseModel):
    damage:int = 0
    

class Character(BaseModel):
    id:UUID=uuid4
    race:str
    hp:int=20
    mp:int=10
    defense:int=0
    #wepon:Weapon
    #shield:Armor
    #armor:Armor
    multiplier:int=1
    adder:int=0
    def take_damage(self, hit:Hit):
        return self.hp-hit.damage
    
    def normal_atack(self):
        atack=self.multiplier*randint(1,6)+self.adder
        return Hit(damage=atack)
    

class Monster(Character):
    pass


class Hero(Character):
    pass


