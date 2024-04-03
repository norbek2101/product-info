from pydantic import BaseModel
from typing import Optional


class MaterialBase(BaseModel):
    name: str


class MaterialCreate(MaterialBase):
    pass


class MaterialRead(MaterialBase):
    id: int

    class Config:
        orm_mode = True
 

class MaterialUpdate(BaseModel):
    name: Optional[str] = None
    product_id: Optional[int] = None
    