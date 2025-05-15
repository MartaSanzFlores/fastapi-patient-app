from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routes.patients import router as patients_router

# Create db tables at app startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code executed at startup
    create_db_and_tables()
    yield
    # Code executed at shutdown

app = FastAPI(lifespan=lifespan)
    
app.include_router(patients_router)

@app.get("/")
def read_root():
    return {"message": "API is up and running"}


