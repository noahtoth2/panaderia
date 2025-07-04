from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.crud.user import create_user, get_user_by_username
from app.core.security import verify_password, create_access_token
import os
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth")

MASTER_KEY = os.getenv("MASTER_KEY", "dev-master-key")

# 📌 Seguimiento de intentos fallidos (en memoria)
FAILED_ATTEMPTS = {}
LOCK_TIME = timedelta(minutes=15)
MAX_ATTEMPTS = 5

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if user.master_key != MASTER_KEY:
        raise HTTPException(status_code=403, detail="Clave de administrador inválida")

    if not user.username.strip() or not user.password.strip():
        raise HTTPException(status_code=400, detail="Usuario y contraseña no pueden estar vacíos")

    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Este usuario ya existe")

    return create_user(db, user)


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    now = datetime.utcnow()
    username = user.username

    # Verificar si está bloqueado
    if username in FAILED_ATTEMPTS:
        attempts, last_attempt = FAILED_ATTEMPTS[username]
        if attempts >= MAX_ATTEMPTS and now - last_attempt < LOCK_TIME:
            remaining = LOCK_TIME - (now - last_attempt)
            raise HTTPException(
                status_code=403,
                detail=f"Cuenta bloqueada. Intenta nuevamente en {remaining.seconds // 60} minutos."
            )
        elif now - last_attempt >= LOCK_TIME:
            FAILED_ATTEMPTS[username] = (0, now)  # Reiniciar contador tras bloqueo

    db_user = get_user_by_username(db, username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        attempts, _ = FAILED_ATTEMPTS.get(username, (0, now))
        FAILED_ATTEMPTS[username] = (attempts + 1, now)
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    # Inicio de sesión exitoso
    if username in FAILED_ATTEMPTS:
        del FAILED_ATTEMPTS[username]  # Resetear intentos tras login correcto

    token = create_access_token(data={"sub": db_user.username, "role": db_user.role})
    return {"access_token": token, "token_type": "bearer", "role": db_user.role}
