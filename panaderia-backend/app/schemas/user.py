from pydantic import BaseModel, constr
from typing import Literal

RoleType = Literal["administrador", "jefe_bodega", "produccion", "ventas"]

class UserBase(BaseModel):
    username: constr(strip_whitespace=True, min_length=3, max_length=50)
    role: RoleType

class UserCreate(UserBase):
    password: constr(min_length=6)
    master_key: str

class UserLogin(BaseModel):
    username: constr(strip_whitespace=True, min_length=3, max_length=50)
    password: constr(min_length=6)

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
