from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.models import Patient, PatientInput, PatientUpdate
from app.database import get_session
from app import crud

router = APIRouter()

@router.get("/patients")
# Executes a SELECT query to retrieve all Patient records from the database.
# Returns a list of Patient objects, which FastAPI automatically converts to JSON (as a list of dictionaries) in the HTTP response.
def list_patients(session: Session = Depends(get_session)):
    return crud.get_patients(session)

@router.post("/patients", response_model=Patient)
def add_patient(patient_input: PatientInput, session: Session = Depends(get_session)):
    patient = Patient(**patient_input.model_dump())
    return crud.create_patient(session, patient)

@router.put("/patients/{patient_id}", response_model=Patient)
def edit_patient(patient_id: int, patient_input: PatientUpdate, session: Session = Depends(get_session)):
    return crud.update_patient(patient_id, session, patient_input)

@router.delete("/patients/{patient_id}")
def remove_patient(patient_id: int, session: Session = Depends(get_session)):
    return crud.delete_patient(patient_id, session)