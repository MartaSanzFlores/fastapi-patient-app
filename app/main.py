from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routes.patients import router as patients_router
from app.routes.appointments import router as appointments_router
from fastapi.middleware.cors import CORSMiddleware

# Create db tables at app startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code executed at startup
    create_db_and_tables()
    yield
    # Code executed at shutdown

app = FastAPI(lifespan=lifespan)
    
app.include_router(patients_router)
app.include_router(appointments_router)

@app.get("/")
def read_root():
    return {"message": "API is up and running"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


