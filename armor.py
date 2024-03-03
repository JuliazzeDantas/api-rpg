from pydantic import BaseModel
from uuid import UUID, uuid4


class Armature(BaseModel):
    id:UUID = uuid4()
    name:str

class Shield(Armature):
    pass

class Armor(Armature):
    pass
