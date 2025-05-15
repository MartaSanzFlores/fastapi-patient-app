from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.models import Patient
from app.database import get_session
from app import crud

router = APIRouter()

@router.get("/patients")
def list_patients(session: Session = Depends(get_session)):
    return crud.get_patients(session)

@router.post("/patients", response_model=Patient)
def add_patient(patient: Patient, session: Session = Depends(get_session)):
    return crud.create_patient(session, patient)
