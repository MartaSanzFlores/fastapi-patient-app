from sqlmodel import Session, select
from app.models.Patient import Patient, PatientUpdate

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

def get_patients(session: Session):
    return session.exec(select(Patient)).all()

def create_patient(session: Session, patient: Patient):
    try:
        session.add(patient)
        session.commit()
        session.refresh(patient)
        return patient
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=400, detail="Patient ID already exists")
    
def update_patient(patient_id: int, session: Session, patient_input: PatientUpdate):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    patient_data = patient_input.model_dump(exclude_unset=True)
    patient.sqlmodel_update(patient_data)
    
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient
    
def delete_patient(patient_id: int, session: Session):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    session.delete(patient)
    session.commit()
    return {"ok": True}  
