from sqlmodel import Session, select
from .models import Patient

def get_patients(session: Session):
    return session.exec(select(Patient)).all()

def create_patient(session: Session, patient: Patient):
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient
