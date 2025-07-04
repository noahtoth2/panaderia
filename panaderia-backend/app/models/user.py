from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    # Máximo 50 caracteres para evitar abuso y optimizar índices
    username = Column(String(50), unique=True, index=True, nullable=False)

    # Hash de bcrypt suele ser ~60, pero damos margen hasta 128
    hashed_password = Column(String(128), nullable=False)

    # Role limitado a 20 caracteres: "administrador", "ventas", etc.
    role = Column(String(20), nullable=False)
