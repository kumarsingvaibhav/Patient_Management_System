# models.py
from pydantic import BaseModel, Field, computed_field
from datetime import datetime
from typing import Literal, Optional, Annotated

class Patient(BaseModel):
    patient_id: Annotated[str, Field(..., description="Id of the Patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the Patient", examples=["Aman"])]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the Patient", examples=[40])]
    gender: Annotated[Literal["Male", "Female", "Others"], Field(..., description="Gender of the Patient")] 
    blood_group: Annotated[str, Field(..., description="Blood Group of the Patient")]
    phone: Annotated[str, Field(..., description="Phone Number of the Patient")]
    email: Annotated[str, Field(..., description="Email of the Patient")]
    diagnosis: Annotated[str, Field(..., description="Diagnosis of the Patient")]
    admission_date: Annotated[str, Field(..., description="Admission Date of the Patient")]
    is_insured: Annotated[bool, Field(..., description="Does Patient have Insurance")]
    height: Annotated[float, Field(..., gt=0, description="Height in meters")]
    weight: Annotated[float, Field(..., gt=0, description="Weight in kg")]
    is_completed: bool = False
    is_deleted: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
