from typing import Optional, Annotated
from sqlmodel import Field, SQLModel
from pydantic import BaseModel, constr, conint, EmailStr

## PATIENTS MODELS
# SqlModel
class Patient(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    firstName: str = Field(index=True)
    lastName: str = Field(index=True)
    age: Optional[int] | None = Field(default=None, index=True)
    email: str = Field(index=True, unique=True)
    phone: str = Field(index=True)

# Validation model    
class PatientInput(BaseModel):
    firstName: Annotated[str, constr(min_length=1)]
    lastName: Annotated[str, constr(min_length=1)]
    age: Annotated[Optional[int], conint(ge=0)]
    email: EmailStr
    phone: Annotated[str, constr(min_length=7)]
    
# Update model
class PatientUpdate(BaseModel):
    firstName: Annotated[Optional[str], constr(min_length=1)] = None
    lastName: Annotated[Optional[str], constr(min_length=1)] = None
    age: Annotated[Optional[int], conint(ge=0)] = None
    email: Optional[EmailStr] = None
    phone: Annotated[Optional[str], constr(min_length=7)] = None
    