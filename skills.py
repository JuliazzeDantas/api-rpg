
from pydantic import BaseModel
from uuid import UUID, uuid4
from weapons import Damage_Type
from character import Character


class Skills_Effects(Damage_Type):
    buff:str='buff'
    debuff:str='debuff'
    healing:str = 'healing'
    burning:str = 'burning'
    freezing:str = 'freezing'
    poisoning:str = 'poisoning'
    no_effect:str = 'no_effect'


class Target(BaseModel):
    self_target:str='self_target'
    single_target:str='single_target'
    multiple_target:str='multiple_target'
    global_target:str='global_target'


class Skills(BaseModel):
    id:UUID = uuid4()
    name:str
    description:str
    target:Target


class Buff(Skills):
    skills_effect:Skills_Effects
    buff_multiplier:int
    buff_adder:int

    def __init__(self, effect:Skills_Effects):
        self.skills_effect=effect.buff
    



class Debuff(Skills):
    skills_effect:Skills_Effects

    def __init__(self, effect:Skills_Effects):
        self.skills_effect=effect.debuff


class Healing(Skills):
    skills_effect:Skills_Effects
    heal_multiplier: int = 1
    heal_adder: int = 0

    def __init__(self, effect:Skills_Effects):
        self.skills_effect=effect.healing



class Damage(Skills):
    skills_effect:Skills_Effects
    damage_multiplier: int = 1
    damage_adder: int = 0
    damage_type: Damage_Type