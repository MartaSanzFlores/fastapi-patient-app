from typing import Optional
from sqlmodel import Field, SQLModel


class Patient(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    firstName: str = Field(index=True)
    lastName: str = Field(index=True)
    age: Optional[int] | None = Field(default=None, index=True)