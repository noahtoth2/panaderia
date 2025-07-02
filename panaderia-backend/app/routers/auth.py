from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user, get_user_by_username
from app.schemas.user import UserLogin
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth")  # ✅ prefijo agregado

MASTER_KEY = "123"

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if user.master_key != MASTER_KEY:
        raise HTTPException(status_code=403, detail="Clave de administrador inválida")

    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Este usuario ya existe")

    return create_user(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = create_access_token(data={"sub": db_user.username, "role": db_user.role})
    return {"access_token": token, "token_type": "bearer", "role": db_user.role}
