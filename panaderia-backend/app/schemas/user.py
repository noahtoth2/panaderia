from pydantic import BaseModel
from typing import Literal

class UserCreate(BaseModel):
    username: str
    password: str
    role: Literal["administrador", "jefe_bodega", "produccion", "ventas"]
    master_key: str

class UserOut(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True
class UserLogin(BaseModel):
    username: str
    password: str