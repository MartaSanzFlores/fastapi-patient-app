from sqlmodel import Session, select
from app.models.Appointment import Appointment, AppointmentInput

def create_appointment(session: Session, data: AppointmentInput):
    appointment = Appointment(**data.model_dump())
    session.add(appointment)
    session.commit()
    session.refresh(appointment)
    return appointment

def get_appointments_for_patient(session: Session, patient_id: int):
    return session.exec(
        select(Appointment).where(Appointment.patient_id == patient_id)
    ).all()