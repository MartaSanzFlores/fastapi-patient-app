from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import get_session
from app.models.Appointment import Appointment, AppointmentInput
from app.crud.appointment import create_appointment, get_appointments_for_patient

router = APIRouter()

@router.post("/appointments", response_model=Appointment)
def add_appointment(data: AppointmentInput, session: Session = Depends(get_session)):
    return create_appointment(session, data)

@router.get("/patients/{patient_id}/appointments", response_model=list[Appointment])
def list_appointments(patient_id: int, session: Session = Depends(get_session)):
    return get_appointments_for_patient(session, patient_id)
