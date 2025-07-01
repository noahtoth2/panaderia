from fastapi import FastAPI
from app.routers import auth
from app.database import engine, Base

app = FastAPI()

# Crear las tablas (solo la primera vez)
Base.metadata.create_all(bind=engine)

# Incluir las rutas
app.include_router(auth.router)
