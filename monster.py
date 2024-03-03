from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import UUID
from character import Monster,Hit
from data import monsters_data

monsters=monsters_data
router=APIRouter()


@router.post("")
def create_monster(monster: Monster):
    monsters.append(monster)
    return monsters


@router.get("")
async def list_monsters():
    return monsters


@router.get("/{monster_id}", response_model=Monster)
async def get_monster(monster_id:int)->Monster:
    try:
        return monsters[monster_id]
    except Exception:
        raise HTTPException(status_code=404, detail=f"Monster ID {monster_id} was not found")
    

@router.get("/{monster_id}/hp")
async def get_monster_hp(monster_id:UUID):
    for monster in monsters:
        if monster.id==monster_id:
            return monster.hp
    
    raise HTTPException(status_code=404, detail=f"Monster ID {monster_id} was not found")


@router.put("/{monster_id}/damage")
async def hurt_monster(monster_id:UUID, hit:Hit):
    for character in monsters:
        if character.id==monster_id:
            character.hp=character.take_damage(hit)
            if character.hp<=0:
                kill_monster(character)
                return 0
            else:
                return character.hp
            
    raise HTTPException(status_code=404, detail=f"Monster ID {monster_id} was not found")

@router.post("/{monster_id}/atack")
async def monster_atack(monster_id:UUID):
    for character in monsters:
        if character.id==monster_id:
            damage=character.normal_atack()
            return damage
        
    raise HTTPException(status_code=404, detail=f"Monster ID {monster_id} was not found")

async def kill_monster(monster):
    monsters.remove(monster)