from typing import Optional, Annotated
from sqlmodel import Field, SQLModel
from datetime import datetime
from pydantic import BaseModel, constr, FutureDate

## APPOINTMENT MODELS
# SqlModel
class Appointment(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    time: datetime
    reason: str = Field(index=True)
    doctor: str = Field(index=True)
    patient_id: int = Field(foreign_key="patient.id")

# Validation model
class AppointmentInput(BaseModel):
    time: FutureDate
    reason: Annotated[str, constr(min_length=1)]
    doctor: Annotated[str, constr(min_length=1)]
    patient_id: int