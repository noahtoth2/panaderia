from fastapi import FastAPI
from app.routers import auth
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Crear las tablas (solo la primera vez)
Base.metadata.create_all(bind=engine)

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O por seguridad: ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas
app.include_router(auth.router)
